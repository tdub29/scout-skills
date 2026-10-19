# Target architectures & extraction mechanics

Reference for Phase 2 (pick a layout) and Phase 4 (move code safely). Prefer the conventions the target repo already uses over any ideal here. Always web-search the *current* best practice for the specific framework version in play; this is a starting map, not the last word.

## Pick a layout by stack

| Stack | Sane default layout | Notes |
|---|---|---|
| Vanilla JS / HTML-with-inline-`<script>` | `config.js`, `state.js`, `api.js`, `ui/*.js`, `main.js` as ES modules; keep the HTML as the shell | Extract inline script to modules first; `<script type="module">`. No build step needed. |
| React / Next | Feature folders (`features/<x>/{components,hooks,api,types}`) beat layer folders once past a few features | Co-locate; a shared `lib/` only for genuinely cross-feature code. |
| Node/Express | `routes/` (thin) â†’ `controllers/` â†’ `services/` (logic) â†’ `repositories/` (data) â†’ `models/` | Routes hold no logic; controllers translate HTTPâ†”service. |
| Flask | Blueprints per area; `services/` for logic, `models/` for ORM, `schemas/` for (de)serialization | App factory (`create_app`) wires blueprints. |
| Rails fat model/controller | Extract to POROs / service objects (`app/services/`), concerns, query objects, presenters/decorators | Keep it Rails-idiomatic; don't invent a framework. |
| Python CLI / library | `cli.py` (arg parsing only) â†’ `core/` (logic) â†’ `io/` (files, network) â†’ `config.py` | Logic must be importable and testable without the CLI. |
| Django | Split fat `models.py`/`views.py` into a package (`models/`, `views/`), managers/querysets, `services.py`, `selectors.py` | `services` = writes, `selectors` = reads is a common convention. |

## The layering rule that matters

Dependencies point one direction, from entry down to leaves:

```
entry/wiring â†’ presentation â†’ services (logic) â†’ data access â†’ models â†’ config
```

Lower layers never import higher ones. If a "constant" needs a service, it isn't config â€” it's logic in disguise. This direction is what makes the tree DRY: shared leaves are imported by many, and nothing reaches back up.

## Extraction order: leaf-first, always

Extract in dependency order so each step compiles on its own:

1. **Config / constants** â€” depend on nothing.
2. **Types / models / schemas** â€” depend on config at most.
3. **Pure helpers / utilities** â€” no side effects.
4. **Data access** â€” depends on config/models.
5. **Services / business logic** â€” depends on data + models.
6. **Presentation / UI** â€” depends on services + models.
7. **Wiring / entry point** â€” depends on everything; goes last, becomes slim.

Moving a top-level handler first pulls its entire transitive dependency set with it and the step never lands green. Start at the leaves.

## The shim (compatibility facade)

The trick that keeps the build green mid-refactor: the original file re-exports moved symbols from their new home. Callers keep importing from the old path until Phase 7 migrates them.

```js
// original.js after extracting users
export { getUser, listUsers } from './data/users.js';
export { PRICE_TIERS } from './config.js';
```

```python
# original.py after extracting users
from .data.users import get_user, list_users  # noqa: F401
from .config import PRICE_TIERS  # noqa: F401
```

```ruby
# original.rb â€” delegate to the extracted service
def get_user(id) = Users::Fetch.call(id)
```

Every shim is temporary and tracked in `REFACTOR-PLAN.md`; Phase 7 removes them one at a time after updating callers.

## Characterization tests (Phase 0, when coverage is thin)

You cannot prove parity against nothing. Pin current behavior, whatever it is:

- **Library / CLI:** feed a spread of representative inputs, snapshot the outputs. Golden-file tests are ideal â€” capture stdout/return values now, assert they don't change.
- **Web page / UI:** "renders without console errors, key selectors present, primary flow completes." A Playwright/Puppeteer smoke covers a lot cheaply.
- **HTTP service:** hit each route with representative payloads, snapshot status + body shape.

These tests assert the *existing* behavior including its bugs. You are not fixing anything yet; you are building the net that tells you a move changed something.

## Detecting the public surface (for the Phase 5 diff)

Compare what the original exposed vs the union of the new modules:

- **JS/TS:** grep `^export ` (and `module.exports`) across old vs new; compare the name sets.
- **Python:** compare `__all__` / top-level `def`/`class` names; `python -c "import mod; print(dir(mod))"`.
- **Ruby:** public instance/class methods (`Mod.instance_methods(false)`).

Any name only in the original must be either deliberately retired (in the plan's later-pass list) or a miss to fix. Names only in the new tree are new internals and are fine.
