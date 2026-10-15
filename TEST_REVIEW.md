# Independent code review and host validation

Run `.venv\Scripts\python.exe validate_game.py` after rebuilding `main.py`.

The suite now contains 13 contract tests. It checks generated map bytes against all three source maps; map dimensions, layer shape and tile indices; floor connectivity and objective reachability; population bounds; pickup scoring; combat cooldowns and projectile direction; dash expiry; damage grace; level cleanup and victory; and action suppression during transitions.

The tilemap regression test requires the first argument of each `tiles.create_tilemap` call to be a direct literal `hex(...)` call. This guards against reintroducing the inferred intermediate Buffer variables implicated by the reported errors. The host runtime also rejects an Image in that argument. This is a structural guard, not proof that MakeCode's Python compiler accepts the project.

Audio checks require three different map melodies, no restart when requesting the same map, music replacement on transitions, and loop shutdown on victory and defeat. They check cues for shots, dash, pickups, enemy hits, player damage, portal unlock, level transitions, victory and defeat. Repeated attack/dash inputs within cooldown and damage during grace must not emit extra cues. Ordinary effects must not stop the map loop.

The fake runtime records audio requests. It does not synthesize or hear sounds, emulate Arcade physics, compile MakeCode Python, emulate browser behavior, or decode the exported PNG. Compiler acceptance, audible music quality, terminal cue playback across scene changes, controls, collision behavior and successful PNG re-import require platform verification.

Reviewed against primary MakeCode sources: [tilemap argument signature and Buffer layout](https://github.com/microsoft/pxt-common-packages/blob/master/libs/game/tilemap.ts), [game-over playable API and scene transition](https://github.com/microsoft/pxt-common-packages/blob/master/libs/game/game.ts), and [sound instruction/channel behavior](https://arcade.makecode.com/developer/sound).

Current host result: all 13 tests passed after audio integration. Simulator and replacement cartridge status are reported separately by the orchestrator.
