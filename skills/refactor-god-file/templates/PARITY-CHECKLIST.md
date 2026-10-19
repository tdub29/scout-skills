# Parity checklist â€” nothing dropped

> Phase 5 gate. One row per symbol from the Phase 1 audit. Check a box only when
> you have CONFIRMED that symbol exists and is wired in its new home.
> Run this pass with FRESH eyes (a reviewer that saw only the audit + new tree),
> not the agent that moved the code.

**Audit symbol count:** `<N>`  Â·  **Confirmed relocated:** `<M>`  Â·  **Retired on purpose:** `<K>`  Â·  **Unaccounted:** `<N - M - K, must be 0>`

## Symbol accounting

| Audit symbol | Present in new tree? | New location | Status |
|---|---|---|---|
| `getUser` | âœ… | `data/users.js` | relocated |
| `LEGACY_MAP` | â€” | â€” | retired (see plan later-pass) |
| `hiddenClosure` | âŒ | â€” | **MISSING â†’ back to Phase 4** |

## Public surface diff

The set of names the original exposed must equal the union of what the new modules expose, minus deliberately-retired names.

- **Original exports:** `<list / command output>`
- **New modules' exports (union):** `<list / command output>`
- **Only in original (investigate â€” must be retired-on-purpose or a miss):** `<list>`
- **Only in new (new internal names, fine):** `<list>`

## Behavioral parity

- [ ] Characterization tests from Phase 0 still pass against the new structure
- [ ] Same tests pass now as passed at baseline (`refactor/baseline-tests.txt`)
- [ ] Any baseline failures still fail the *same way* (bugs preserved until later pass)
- [ ] Manual smoke checklist (if used) re-run and matches

**Gate:** Unaccounted = 0 and all boxes checked â†’ proceed to Phase 6/7. Otherwise, each miss becomes a new Phase 4 step.
