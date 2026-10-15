# Development orchestrator

This is an actual Python **LangGraph StateGraph** for developing the Arcade game.
The graph has an orchestrator and seven named specialist nodes. Every specialist
returns to the orchestrator; the orchestrator assigns the next role, integrates
build/test results, retries failures at most the configured number of times, and
records a release decision. It runs on the development computer, not in Arcade.

## Run

From the game directory, with the workflow dependencies installed:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements-workflow.txt
.venv\Scripts\python.exe -m workflow.graph
.venv\Scripts\python.exe -m unittest workflow.test_graph -v
```

Microsoft's official Arcade compiler is installed under `compiler/`. To install
it on another development computer with Node.js and npm, run
`npm install --prefix compiler --ignore-scripts`. The test node runs it when
available; the result is saved in `compiler/results/compile-report.json`.
Use `node compiler/check_game.js` to compile directly and
`node compiler/package_game.js` to rebuild the Audio Edition PNG after compiling.

The default **local mode is deterministic artifact auditing**, not seven
autonomous LLM agents. Story inventories narrative inputs; character inventories
sprites; world checks map dimensions; soundtrack and sound-effects inventory the
soundtrack and sound-effects modules; code invokes `build_game.py`; test independently invokes
`validate_game.py` and the official Arcade compiler when installed. Existing meaningful game tests remain the authority for
reachability, mechanics and audio trigger contracts. Repeated build/test failure
ends with `changes_required`, rather than an infinite retry loop. Missing audio
inputs also block integration. The workflow never invents missing game content.

Reports include input hashes, specialist findings, subprocess output, revisions
(retry count), full attempt history, requirements, decisions, maps and artifacts.
They are saved in `workflow/reports/latest.json`. A process-local in-memory
checkpointer preserves node state during a run; the JSON report is the durable
audit record. Cross-process crash resume is not implemented.

## Optional model-backed specialists

Set a compatible chat-completions endpoint and model, then run `--backend model`.
No provider or credential is hardcoded. Keys are optional for local model hosts:

```powershell
$env:WORKFLOW_MODEL_URL = 'http://localhost:8000/v1/chat/completions'
$env:WORKFLOW_MODEL = 'your-model-name'
# For a hosted provider, use its HTTPS endpoint and set WORKFLOW_API_KEY.
.venv\Scripts\python.exe -m workflow.graph --backend model
```

Each specialist receives its own editable prompt from `workflow/prompts.json`,
requirements, relevant source files, local check results and prior specialist
reports. Hosted mode sends those files to the
configured endpoint. Model reviews are stored alongside deterministic findings;
they also create concrete content and patch suggestions under `reports/proposals/`.
They cannot execute suggested commands or modify assets. Model mode is a genuine
model-backed review interface, not an unbounded autonomous coding system. Apply
reviewed edits through the development process, then rerun the graph. Deterministic
failures cannot be overridden by a model response.

## Native release evidence

Passing local checks ends with `awaiting_simulator`. It does not establish that
MakeCode compiled the source, that its PNG imports, or that gameplay works.
After actually observing those checks, write a JSON evidence record containing:

```json
{
  "source_sha256": "SHA256 of the exact main.py tested",
  "cartridge_sha256": "SHA256 of the exact Find-My-Drum-Audio-project.png imported",
  "compiler_passed": true,
  "fresh_import_passed": true,
  "gameplay_passed": true,
  "observer": "Who performed the checks",
  "observed_at": "ISO timestamp of the checks",
  "notes": "Compiler, fresh-project import and gameplay observations"
}
```

Then pass `--simulator-evidence path/to/evidence.json`. Evidence must match both
current source and cartridge hashes. A matching record permits `ready_for_review`;
this is operator-attested evidence, not an automatic simulator verification.
Never fill the record with assumed success. The original tilemap import issue
remains pending until a corrected export passes those native checks.

The Audio Edition now passes official compilation, exported-file-set compilation,
payload roundtrip, and a MakeCode UI import. Live gameplay and audible playback
remain unverified because the in-app simulator renderer crashed. The current
workflow therefore remains `awaiting_simulator`.

To supply future game specifications, save a text file and pass
`--requirements-file path/to/specs.txt`. Model mode saves each specialist's
review and concrete proposals under `workflow/reports/proposals/`.
