# Find My Drum

An original, family-friendly top-down scrolling adventure for Microsoft MakeCode Arcade, written in MakeCode Python.

## Story

Every year, the town of Beatwick celebrates the Lantern Parade. This year, a playful gust called the Hush scattered nine glowing fragments of the parade drum across three places. Without its rhythm, the parade lanterns cannot shine.

You play as Pip, a young drummer wearing a bright scarf. Travel through three connected places, recover the drum pieces, and bring the beat back. The creatures in your way are confused by the Hush; a musical pulse sends them gently away. Nobody is injured.

The story provides the premise for play. Gameplay starts immediately, with the current world name appearing above Pip. There is no blocking introduction or dialogue sequence. Completing the adventure triggers the standard Arcade victory screen with confetti.

## Worlds

Each world is a 32 × 12 tile map, measuring 512 × 192 pixels, viewed from above. The player can move in all four directions, and the camera follows the player on both axes. The maps primarily extend sideways; there is no jumping or platform gravity.

| World | Place and visual theme | Drum fragments | Obstacles and creatures |
| --- | --- | --- | --- |
| 1 | Lantern Meadow: green ground and darker green walls | Three pieces | Wall obstacles and Hush blobs |
| 2 | Echo Quarry: dusty ground and gray stone walls | Three pieces | Narrow passages and faster Hush blobs |
| 3 | Moonlight Grove: blue ground and dark walls | Three pieces | Wall obstacles and the fastest Hush blobs |

Three red-and-gold fragments are distributed across each world. Touching a fragment collects it and awards ten points. Collect all three to unlock the gold-and-blue beacon at the right side, then touch the beacon to travel onward. Complete all three worlds, collecting nine fragments in total, and enter the final beacon to win. There is no boss.

## Controls

- Arrow keys / directional pad: move Pip in four directions.
- A / Z or space: release a short musical pulse in the facing direction.
- B / X or enter: dash briefly in the facing direction, subject to a cooldown.

The MakeCode simulator displays its A and B buttons. Keyboard bindings may vary by host; clicking the simulator buttons always works.

## Rules and Feedback

- Begin with five hearts.
- Touching a creature costs one heart, followed by 1.2 seconds of protection so a single contact cannot drain all hearts. Entering a world also grants a short protection period.
- Musical pulses remove creatures and award two points. Pulses have a 0.25-second firing cooldown and stop at walls.
- Three creatures start in each world. New creatures can spawn every six seconds, capped at six at once. They follow Pip directly and become faster in later worlds; they can get caught behind walls because they do not use maze pathfinding.
- Dash lasts 0.25 seconds, protects Pip during the dash, and has a 1.5-second cooldown. Wall tiles still block it.
- Each recovered fragment awards ten points. Traveling to the next world restores one heart, capped at five.
- Zero hearts ends the game with a loss; entering the final unlocked beacon ends it with a win.
- The world name appears above Pip when a world loads; pickup messages track pieces out of three. The beacon changes from “Find 3 pieces” to “OPEN!” Hearts and score use MakeCode's standard HUD.

## Art Direction

Use original native pixel sprites that remain readable on Arcade's 160 × 120 display. Pip has a bright scarf and a clear silhouette, with idle and walking frames. Hush blobs use cool colors. Drum fragments use red and gold, and exit beacons use gold and blue. Walls and floors have different colors and simple textures. All sprites and tilemaps are embedded in the generated Python source, so loading the game requires no separate art files.

## Implementation Scope

Deliver one playable Python source file (`main.py`), development sources and validation tools, and instructions for pasting the complete source into a new MakeCode Arcade Python project. The user can then save a MakeCode project backup from the editor. Use only standard MakeCode Arcade APIs, with no extensions or network services. Include three wall-bounded maps, camera scrolling, player movement, attack, dash cooldown, creatures, damage protection, fragment collection, beacon progression, score, world-name text, and win/loss states.

The initial version excludes save files, multiplayer, custom music tracks, procedural maps, and a separate inventory screen. The complete loop should be playable in a few minutes and replayable from the simulator restart button.

## Validation Requirements

Check that the project converts and compiles with MakeCode Arcade's Python tooling. Inspect the resulting simulator when available. Verify walls block movement, camera scrolling exposes the full world, A attacks, B dashes and recovers after its cooldown, damage has a grace period, each fragment counts once, three pieces unlock a beacon, and the third world's beacon produces a win. Verify world transitions heal one heart up to five and zero hearts produces a loss. Report checks honestly and distinguish compilation, host-side rule checks, and interactive play testing. A successful compiler check alone does not establish a complete simulator playthrough or hardware performance.
