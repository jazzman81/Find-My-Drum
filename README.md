# Find My Drum

A complete small Microsoft MakeCode Arcade Python game. Pip must recover the
Lantern Parade drum across Lantern Meadow, Echo Quarry, and Moonlight Grove.
The camera follows Pip through three 512 x 192 pixel worlds. This uses a top-down
view with scrolling in both directions and maps that primarily extend sideways.

## Load the game into Microsoft MakeCode Arcade

The preferred method is to import **Find-My-Drum-Audio-project.png**. This PNG is
a project cartridge containing all the Python, converted TypeScript, artwork,
maps and audio. It replaces the earlier `Find-My-Drum-project.png` export.

1. Open https://arcade.makecode.com/ in your browser.
2. On the **home screen**, choose **Import → Import File**.
3. Select **Find-My-Drum-Audio-project.png** from this folder and choose **Go ahead!**.
4. Press **Play** in the simulator. Click it to give it keyboard focus.
5. Use the simulator's speaker button to unmute audio if needed.

If you are in the editor, click the **Home icon** in the top toolbar to find
Import. The Download button is for hardware and is not the import menu.

To load the Python by copying instead:

1. Open https://arcade.makecode.com/ and choose **New Project**.
2. Name the project **Find My Drum**, then choose **Create**.
3. Open the editor-language dropdown in the top toolbar and select **Python**.
4. Open `main.py` from this folder in a text editor. Select all its text and copy it.
5. Click inside MakeCode's Python code editor. Select all the existing code
   (**Ctrl+A** on Windows, **Cmd+A** on Mac), then paste the entire `main.py`.
6. Click the simulator's **Play** button. Use fullscreen if the simulator is
   collapsed on a narrow screen. The game begins in Lantern Meadow.
7. Click the simulator to give it keyboard focus, then play.
8. Use the **Save** disk button to save a MakeCode project backup. Reopen that
   backup later with **Import** on MakeCode's home page. Sign-in/cloud-save is
   optional; keep a local backup.

There is no separate image or tilemap upload: **main.py contains everything**.
Do not paste `build_game.py` or `validate_game.py` into MakeCode. Those two files
are local development tools. A plain `.py` file is loaded by copying its contents
into the Python editor, rather than by importing it as a MakeCode project.

## Controls and objective

| Action | Arcade control | Keyboard |
| --- | --- | --- |
| Move | D-pad | Arrow keys |
| Fire a directional sound pulse | A | Z or Space |
| Dash in the last movement direction | B | X or Enter |

Collect all three red-and-gold drum pieces in each world. The gold-and-blue beacon
at the right side says **OPEN!** once all three are collected. Touch it to travel
to the next world. Complete all three worlds to win and restore the parade.

You start with five hearts. Hush blobs pursue Pip; a pulse disperses one. Contact
costs one heart with 1.2 seconds of protection between hits. Dashes last 0.25
seconds and protect Pip during the dash, with a 1.5-second cooldown. Walls still
block dashes. New enemies spawn every six seconds, up to six at once. A completed
world restores one heart, capped at five. Losing every heart ends the game.
Use the simulator's restart control for another attempt.

Drum pieces score ten points each; dispersing a Hush scores two. The world name
appears above Pip at the start, and the pickup message tracks the three pieces.
The story and implementation scope are documented in `DESIGN.md`.

## Music and sound effects

Each map has a different original chip melody: R&B-inspired Lantern Bounce,
hip-hop-inspired Quarry Pocket, and soul-inspired Moonlit Return. Nine cues cover
shots, dashes, pickups, damage, enemy hits, portal unlocks, map transitions,
victory and defeat. Music changes with the map and stops on game over.

Approximate WAV previews are in `audio-previews/`; they are listening references
for the compositions, not recordings of actual Arcade playback. See `AUDIO.md`.

## LangGraph workflow

The development workflow in `workflow/graph.py` has one orchestrator and seven
reporting specialist nodes. Run `.venv\Scripts\python.exe -m workflow.graph`.
Default mode performs local artifact audits, building and testing. Optional
model-backed specialist reviews need a configured model endpoint; see
`workflow/README.md`. Only the game `main.py` goes into MakeCode. The LangGraph
workflow runs on the development computer.

## Validation and development

Run `python build_game.py` after editing `assets.py`, `worlds.py`, or
`gameplay.py`, then paste the rebuilt `main.py` into MakeCode again.

Run `python validate_game.py` for host-side checks. The tests stub the Arcade
APIs to check map data, reachability, art dimensions, and gameplay rules. They
do not emulate MakeCode physics or replace compiling in the Arcade editor.

The game uses MakeCode's Python dialect and built-in Arcade APIs. It does not
run as a desktop CPython game and needs no pip packages or Arcade extensions.
The separate LangGraph development workflow does use Python dependencies.
Enemies use direct following, so they can get caught behind obstacles; they do
not implement maze pathfinding. Hardware performance and a complete simulator
playthrough still need user playtesting.
The current source and exact exported file set pass Microsoft's Arcade 4.1.25
compiler with zero diagnostics. The PNG imports successfully into MakeCode;
the in-app simulator renderer crashed during live verification, so gameplay and
audible playback of this revision are not yet confirmed. `VALIDATION.md` records
the evidence and limits.

Official references:
- https://arcade.makecode.com/python
- https://arcade.makecode.com/reference/scene/camera-follow-sprite
