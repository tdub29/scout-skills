# Flowchart

**Best for:** decision logic, algorithms, user-facing branching flows ("Should Iâ€¦?"), onboarding routing, support-triage trees.

## Layout conventions
- Shape carries type, not color:
  - **Oval** (`rx=20`) â€” start / end
  - **Rectangle** (`rx=6`) â€” step / action
  - **Diamond** â€” decision (â‰¤3 exits)
  - **Small filled ink dot** (`r=4`) â€” merge point where branches rejoin
- Flow runs topâ†’down. From a diamond, conventional exits: Yes to the right, No below â€” but label every outgoing arrow regardless.
- Use coral on the happy path *or* on the single most consequential decision â€” never on every decision.
- If two arrows must cross, use a small arc jump on one so the crossing is readable.

## Anti-patterns
- Using fill color to signal node type (shape does that).
- Decision diamond with 4+ exits â€” refactor into nested diamonds.
- Unlabeled decision branches.

## Examples
- `assets/example-flowchart.html` â€” minimal light
- `assets/example-flowchart-dark.html` â€” minimal dark
- `assets/example-flowchart-full.html` â€” full editorial
