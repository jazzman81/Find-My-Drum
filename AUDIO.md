# Find My Drum audio

The Soundtrack agent supplies three original 32-beat looping chip melodies. These are compact synthesized genre adaptations, with one melodic voice at a time, rather than recordings or full band arrangements. No songs or samples are copied.

| Map | Track | Inspiration and arrangement |
| --- | --- | --- |
| Lantern Meadow | Lantern Bounce | R&B: bright triangle tone, a C-major-seventh opening, question-and-answer phrases and rests. 176 playback beats per minute; treat each playback beat as an eighth-note subdivision, giving an 88 BPM feel. |
| Echo Quarry | Quarry Pocket | Hip-hop: short square-wave notes, low A-minor ostinato, deliberate gaps and repeated hooks. 192 playback BPM, giving a 96 BPM feel. |
| Moonlight Grove | Moonlit Return | Soul: softer sine tone, rising major-pentatonic phrases and a longer final resolution. 168 playback BPM, giving an 84 BPM feel. |

Music begins after each map loads. `start_map_music(level)` stops the prior loop before beginning the next and ignores repeated requests for the same active map. `stop_map_music()` stops all sounds and resets the active-map marker. Gameplay should start the new map loop before playing its transition cue, so the loop switch does not immediately cancel that cue.

The Sound Effects agent supplies short independent cues for pulse shots, dashes, drum pickups, player damage, enemy hits, portal unlocking and map transitions. Every cue uses background playback so controls continue responding. A pulse descends in pitch; a pickup rises; player damage falls into a low buzz; an enemy hit is a short square-wave fall; the portal rises with vibrato. Victory and defeat stop map music and register original ascending or descending jingles with `game.set_game_over_playable`. The subsequent `game.over` call plays the registered jingle once in the game-over scene. This prevents a background cue from being suspended during the scene transition and replaces the default end-game melody.

Arcade provides three hardware mixing channels, so overlapping cues can be dropped when all channels are busy. The single map voice and brief effects reduce that pressure. Browser sound may need a user gesture and an unmuted simulator. These source modules require MakeCode Arcade's compiler, not desktop CPython.

Verified APIs and syntax: [string playable](https://arcade.makecode.com/reference/music/string-playable), [music play](https://arcade.makecode.com/reference/music/play), [game-over playable](https://arcade.makecode.com/reference/game/set-game-over-playable), [melody syntax and channels](https://arcade.makecode.com/developer/sound), and [Microsoft SoundEffect implementation](https://github.com/microsoft/pxt-common-packages/blob/master/libs/mixer/soundEffect.ts). `create_sound_effect` returns a playable object directly; no extension or wrapper is required. Compilation and listening results should be recorded by the independent testing agent; this document describes the arrangement rather than claiming a completed listening test.

