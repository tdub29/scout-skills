# Component map â€” where the god file went

> Phase 4 output, one row added per move. This is the README that answers
> "the original had X, where is it now and why." Keep it current every step.

**Original:** `<path/to/god-file>` (`<n>` lines at start)

## New structure

```
<paste the actual resulting tree here as it fills in>
```

## Symbol â†’ new home

| Original symbol | New location | Concern | Why here |
|---|---|---|---|
| `getUser` | `data/users.js` | data access | all DB reads for users live together |
| `renderRow` | `ui/table.js` | presentation | DOM building, no business logic |
| `PRICE_TIERS` | `config.js` | config | shared constant, no logic |

## Module responsibilities

| Module | Owns | Does NOT own |
|---|---|---|
| `config.<ext>` | constants, env, flags | any logic |
| `data/` | reads/writes to store | business rules |
| `services/` | business rules | I/O details, rendering |
| `ui/` | rendering | data fetching, rules |
| `index.<ext>` | wiring the above | any real logic |

## Import graph (leaf â†’ entry)

```
config  â†  models  â†  data  â†  services  â†  ui  â†  index
```

No arrows point backwards. If a lower layer needs something from a higher one, the boundary is wrong â€” revisit the plan.
