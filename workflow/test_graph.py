"""Meaningful graph routing and release-gate tests, using injected specialists."""
import json
from pathlib import Path
import tempfile
import unittest

from workflow.graph import build_graph, SPECIALISTS, evidence_valid, sha256


class GraphTests(unittest.TestCase):
    def run_graph(self, root, runner, **extra):
        initial = {"completed": [], "reports": {}, "history": [], "repair_count": 0,
                   "max_repairs": 1, "simulator_evidence": "", **extra}
        return build_graph(root, runner).invoke(initial, config={
            "configurable": {"thread_id": self.id()}, "recursion_limit": 100})

    def test_all_seven_report_and_native_gate_remains_pending(self):
        calls = []
        def runner(name, *args):
            calls.append(name)
            return {"status": "passed"}
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_graph(Path(directory), runner)
        self.assertEqual(calls, list(SPECIALISTS))
        self.assertEqual(result["release_status"], "awaiting_simulator")
        self.assertEqual(set(result["reports"]), set(SPECIALISTS))

    def test_transient_build_failure_routes_back_through_code_and_test(self):
        calls = []
        def runner(name, *args):
            calls.append(name)
            return {"status": "failed" if name == "code" and calls.count("code") == 1 else "passed"}
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_graph(Path(directory), runner)
        self.assertEqual(calls[-2:], ["code", "test"])
        self.assertEqual(result["repair_count"], 1)
        self.assertEqual(result["release_status"], "awaiting_simulator")

    def test_persistent_failure_stops_at_retry_limit(self):
        calls = []
        def runner(name, *args):
            calls.append(name)
            return {"status": "failed" if name == "world" else "passed"}
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_graph(Path(directory), runner, max_repairs=2)
        self.assertEqual(calls.count("world"), 3)
        self.assertEqual(result["release_status"], "changes_required")
        self.assertIn("Failed specialist: world", result["unresolved_issues"])

    def test_specialist_exception_becomes_failure(self):
        def runner(name, *args):
            if name == "story":
                raise RuntimeError("deliberate failure")
            return {"status": "passed"}
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_graph(Path(directory), runner, max_repairs=0)
        self.assertEqual(result["release_status"], "changes_required")
        self.assertEqual(result["reports"]["story"]["error"], "deliberate failure")

    def test_evidence_bound_to_both_source_and_cartridge(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "main.py").write_text("source")
            (root / "Find-My-Drum-Audio-project.png").write_bytes(b"cartridge")
            evidence = root / "evidence.json"
            evidence.write_text(json.dumps({"source_sha256": sha256(root / "main.py"),
                "cartridge_sha256": sha256(root / "Find-My-Drum-Audio-project.png"),
                "compiler_passed": True, "fresh_import_passed": True, "gameplay_passed": True,
                "observer": "test fixture", "observed_at": "test fixture", "notes": "test fixture"}))
            self.assertTrue(evidence_valid(str(evidence), root)[0])
            result = self.run_graph(root, lambda *args: {"status": "passed"}, simulator_evidence=str(evidence))
            self.assertEqual(result["release_status"], "ready_for_review")
            (root / "Find-My-Drum-Audio-project.png").write_bytes(b"changed")
            self.assertFalse(evidence_valid(str(evidence), root)[0])
            (root / "main.py").write_text("changed")
            self.assertFalse(evidence_valid(str(evidence), root)[0])


if __name__ == "__main__":
    unittest.main()
