# Refactor plan â€” `<path/to/god-file>`

> Phase 2 output, reconciled in Phase 3. Cross-reference: every audit symbol
> maps to exactly one extraction step; every step traces to real symbols.

## Target architecture

- **Pattern chosen:** `<e.g. feature folders / layered service+repo / Flask blueprints>`
- **Why this one:** `<fits the stack + matches the rest of THIS repo's conventions>`
- **Sources consulted (Phase 2 research):**
  - `<url â€” best-practice layout for this stack>`
  - `<repo's own existing structure this mirrors>`

## Target directory tree

```
<feature-or-layer>/
  config.<ext>        # constants, env, flags
  models.<ext>        # types / shapes / schemas
  data/               # data access (DB, storage, fetch)
  services/           # business logic
  ui/                 # presentation / rendering
  index.<ext>         # slim entry point that wires the above
```

| Path | Responsibility (one line) |
|---|---|
| `config.<ext>` | |
| `models.<ext>` | |
| `data/...` | |
| `services/...` | |
| `ui/...` | |
| `index.<ext>` | |

## Extraction sequence (leaf-first, dependency-ordered)

Each step depends only on already-extracted or not-yet-touched code. Execute in this order in Phase 4.

| # | Extract (audit group / symbols) | â†’ target path | Depends on steps | Done |
|---|---|---|---|---|
| 1 | constants / config | `config.<ext>` | â€” | â˜ |
| 2 | types / models | `models.<ext>` | 1 | â˜ |
| 3 | data access | `data/...` | 1,2 | â˜ |
| 4 | business logic | `services/...` | 1,2,3 | â˜ |
| 5 | presentation | `ui/...` | 1,2,4 | â˜ |
| 6 | wiring / entry | `index.<ext>` | all | â˜ |

## Shim strategy

While extracting, the original file re-exports moved symbols so no downstream caller breaks mid-refactor:

```
// original.js â€” after moving getUser to data/users.js
export { getUser } from './data/users.js';
```

```python
# original.py â€” after moving get_user to data/users.py
from .data.users import get_user  # noqa: F401  (compat shim, removed in Phase 7)
```

Shims are removed one at a time in Phase 7, after parity is proven.

## Later pass (NOT done during this refactor)

Behavior-preserving means parking every improvement you notice:

- `<dead-code suspect â€” confirm + remove in Phase 7 or a later pass>`
- `<duplication to collapse â€” separate pass with its own tests>`
- `<rename / API cleanup â€” separate pass>`
- `<actual bug found â€” fix in its own change, with a test, after the move lands>`
