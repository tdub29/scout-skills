# Technical audit â€” `<path/to/god-file>`

> Phase 1 output. A complete, technical description of everything the file does.
> Group symbols by concern; the groups become module boundaries in the plan.
> Keep updating this in Phase 3 until it agrees exactly with the file.

- **File:** `<path>`
- **Lines:** `<n>`
- **Language / stack:** `<e.g. vanilla JS, Flask, Rails model>`
- **Audited:** `<YYYY-MM-DD>`
- **Baseline tests:** `refactor/baseline-tests.txt` (`<X passing / Y failing>`)

## Concern groups (â†’ future modules)

| Group | What it is | Rough symbol count | Target module (fill in Phase 2) |
|---|---|---|---|
| Config / constants | env, feature flags, magic numbers | | |
| Types / models | shapes, schemas, DTOs | | |
| Data access | DB, storage, fetch, cache | | |
| Business logic | the actual rules | | |
| Presentation / UI | DOM, rendering, templates | | |
| Wiring / entry | routes, listeners, bootstrap | | |

## Symbol inventory

One row per top-level symbol. Side effects = I/O, DOM, network, globals, mutation of shared state.

| Symbol | Kind | Concern group | Inputs â†’ outputs | Side effects | Depends on | Depended on by | Flags |
|---|---|---|---|---|---|---|---|
| `fooHandler` | function | wiring | `(req,res)` â†’ writes response | network, DB | `getUser`, `render` | route table | |
| `getUser` | function | data access | `(id)` â†’ user object | DB read | `db` | `fooHandler`, ... | |
| `LEGACY_MAP` | const | config | â€” | â€” | â€” | `oldThing` | suspected dead |

## Notes

- **Dead-code suspects:** `<list â€” confirm unreferenced before Phase 7 removal>`
- **Duplication:** `<repeated logic that could collapse â€” park for later pass, don't fix now>`
- **Hidden coupling / globals:** `<shared mutable state, load-order dependencies, monkeypatches>`
- **Top-level side effects:** `<code that runs on import/load â€” these constrain extraction order>`
- **Surprises:** `<anything the audit almost missed: closures, event handlers, dynamic dispatch>`
