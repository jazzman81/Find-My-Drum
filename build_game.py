"""Bundle native MakeCode Python art, maps, and gameplay into one pasteable file."""
from pathlib import Path
import ast

ROOT = Path(__file__).resolve().parent
world_source = (ROOT / "worlds.py").read_text(encoding="utf-8")
module = ast.parse(world_source)
maps = {}
for statement in module.body:
    if isinstance(statement, ast.Assign):
        name = statement.targets[0].id
        if name.startswith("WORLD_"):
            maps[name] = ast.literal_eval(statement.value)
map_loader = ["def load_world_map(level: number, floor_tile: Image, wall_tile: Image):"]
for index in range(1, 4):
    rows = maps[f"WORLD_{index}"]
    assert len(rows) == 12 and all(len(row) == 32 for row in rows)
    data = bytes([32, 0, 12, 0]) + bytes(2 if ch == "#" else 1 for row in rows for ch in row)
    keyword = 'if' if index == 1 else 'elif'
    map_loader.append(f'    {keyword} level == {index - 1}:')
    map_loader.append(f'        tiles.set_current_tilemap(tiles.create_tilemap(hex("""{data.hex()}"""), image.create(32, 12), [image.create(16, 16), floor_tile, wall_tile], TileScale.SIXTEEN))')
parts = [
    "# FIND MY DRUM - paste this entire file into MakeCode Arcade's Python editor.\n# All sprite art and maps are included. No extensions or separate uploads.\n",
    (ROOT / "assets.py").read_text(encoding="utf-8"),
    world_source,
    "\n".join(map_loader),
    (ROOT / "soundtrack.py").read_text(encoding="utf-8"),
    (ROOT / "sound_effects.py").read_text(encoding="utf-8"),
    (ROOT / "gameplay.py").read_text(encoding="utf-8"),
]
(ROOT / "main.py").write_text("\n\n".join(parts), encoding="utf-8")
print("Built main.py: all art, three maps, and gameplay bundled.")
