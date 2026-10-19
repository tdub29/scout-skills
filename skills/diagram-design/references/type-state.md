# State Machine

**Best for:** finite state logic â€” order status, auth state, connection lifecycle, form wizard, job queue status.

## Layout conventions
- States are rounded rectangles (`rx=8`), labeled in Geist.
- **Start**: filled ink dot (`r=6`). **End**: ringed dot (outer `r=8` outline, inner filled `r=5`).
- Transitions: curved arrows labeled in Geist Mono as `event [guard] / action` (omit sections you don't need).
- Self-loops curve above the state.
- Orient along the dominant flow direction (leftâ†’right or topâ†’down); rearrange before crossing transitions.
- Coral on the state the reader should notice â€” typically the error state, or "happy completion".

## Anti-patterns
- More transitions than states Ã— 2 â†’ likely two state machines.
- "From any state" transitions drawn from every state â€” use a single annotation (`* â†’ Error on timeout`) instead.
- Unlabeled transitions (the whole point is *what triggers this*).

## Examples
- `assets/example-state.html` â€” minimal light
- `assets/example-state-dark.html` â€” minimal dark
- `assets/example-state-full.html` â€” full editorial
