# Find My Drum agent architecture

User-requested LangGraph architecture: one overarching orchestrator coordinates
seven specialist agents. The runtime is implemented in `workflow/graph.py` using
LangGraph StateGraph. Each specialist reports back to the orchestrator, which
dispatches work and applies a bounded repair loop. The default local mode audits
artifacts and performs reproducible build/test work. Optional model mode uses a
configured chat-completions endpoint to generate specialist reviews and content
or patch proposals; it requires a model configuration. See `workflow/README.md`.

| Agent | Responsibility | Deliverable |
| --- | --- | --- |
| Orchestrator | Maintain shared requirements, assign tasks, reconcile dependencies, and manage review and repair loops | Approved work plan and integrated release status |
| Story | Plot, characters' motivations, dialogue, and progression | Story and map-specific narrative |
| Character | Hero, enemies, collectibles, animation, and consistent pixel art | MakeCode-compatible sprite assets |
| World | Map layouts, obstacles, exploration, visual environment, and spawn positions | Tilemaps and reachability evidence |
| Soundtrack | Original background music inspired by R&B, hip hop, and soul; different music for each map | MakeCode-compatible map tracks and transitions |
| Sound effects | Effects for game mechanics such as attacks, dashes, pickups, damage, exits, victory, and defeat | MakeCode-compatible effects and trigger mapping |
| Code | Integrate approved narrative, visuals, maps, and audio into Arcade Python | Runnable game and importable project |
| Test | Independently check code, maps, mechanics, audio triggers, compilation, and exported-project behavior | Results, reproducible failures, and release recommendation |

## Intended graph flow

Requirements enter the orchestrator. Story, character, world, soundtrack, and
sound-effects work may proceed concurrently once their inputs are available.
World and soundtrack agents agree on map identity and track assignment. Code
receives the agreed assets and mechanics. Test then checks the integrated build
and the exported cartridge in a fresh MakeCode project.

Failures route through the orchestrator to the responsible specialist and code
agent. Revised work returns to test. Release requires passing checks and explicit
evidence of a working import; host-side stubs alone do not satisfy this gate.

## Shared state requirements

Track user requirements, current design decisions, map identifiers, asset paths,
music and effect assignments, revisions, dependencies, review findings, test
results, unresolved issues, and release artifacts. Preserve subsequent user
specifications before selecting runtime details or changing game content.

## Current unresolved issue

The original PNG produced tilemap buffer/number errors for the user. Direct hex
buffer literals now avoid that inference issue. The complete audio build and
exported project file set pass Microsoft's official Arcade compiler with zero
diagnostics. Thirteen game tests and five workflow tests pass. The updated
`Find-My-Drum-Audio-project.png` contains Python plus generated TypeScript and
passes a payload roundtrip. MakeCode successfully imports it as a Python project.
Live gameplay and audible results remain pending after repeated simulator
renderer crashes. Release remains gated on those observed checks.
