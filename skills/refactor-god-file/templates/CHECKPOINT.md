# Refactor checkpoint â€” `<path/to/god-file>`

> Resumable state. Update after EVERY extraction/purge step. A fresh session
> reads this first and continues from "Next action" without redoing finished work.

- **Goal:** decompose `<path>` into `<target tree>` without changing behavior.
- **Branch / worktree:** `<name>`
- **Baseline captured:** `<yes/no>` â†’ `refactor/baseline-tests.txt`
- **Current phase:** `<0â€“7>`
- **Last green commit:** `<sha / short desc>`

## Phase status

| Phase | Status |
|---|---|
| 0 Baseline & safety net | â˜ |
| 1 Technical audit | â˜ |
| 2 Research + plan | â˜ |
| 3 Cross-reference & lock plan | â˜ |
| 4 Extract (loop) | â˜ |
| 5 Parity cross-check | â˜ |
| 6 Full verification | â˜ |
| 7 Purge shims + dead code | â˜ |

## Extraction steps (Phase 4)

| # | Step | Status | Commit |
|---|---|---|---|
| 1 | config | â˜ | |
| 2 | models | â˜ | |
| ... | | | |

## Purge steps (Phase 7)

| Shim / dead symbol | Callers migrated | Shim removed | Commit |
|---|---|---|---|
| `getUser` | â˜ | â˜ | |

## Next action

`<the single exact next step on resume â€” e.g. "Phase 4 step 3: extract data access into data/users.js, then smoke test">`

## Blockers / notes

- `<anything that stalled; self-unblock first, escalate only what needs a person>`
