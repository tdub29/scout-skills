# seam-stamp.mjs + seam-gate.mjs â€” usage + ledger schema

Generate-and-verify pair for the Seam Gate. Zero npm deps (node â‰¥ 22 + a local Chrome;
the gate finds `~/.cache/puppeteer` chrome-headless-shell or system Chrome automatically).

```bash
# STAMP: write the master seam block (base sets + all wrapper tweens) from the ledger.
# Replaces the // <seams:auto> â€¦ // </seams:auto> block (inserts after the
# window.__timelines["main"] registration if markers are absent). Stamped seams pass
# the gate by construction. match-cut/morph rows get visibility sets only â€” the
# carrier handoff stays hand-authored.
node <SKILL_DIR>/scripts/seam-stamp.mjs --ledger ledger.json --write index.html
```

Per-seam stamp options in the ledger: `exit.dur` / `entry.dur` (durations),
`entry.travel` (xPercent/yPercent offset, default 10 â€” use 8 for a soft entry),
`blur` (Z seams, default 18px full-frame / set 10 for text-scale).

```bash
# verify every seam in the ledger (exit 0 = gate passed)
node <SKILL_DIR>/scripts/seam-gate.mjs verify --ledger ledger.json --project <project-dir>

# reuse a RUNNING preview server (restart it after comp edits â€” stale bundle!)
node <SKILL_DIR>/scripts/seam-gate.mjs verify --ledger ledger.json --url http://localhost:5244

# discover movers around a cut time (use to author/fix ledger rows)
node <SKILL_DIR>/scripts/seam-gate.mjs probe --t 44.8 --project <project-dir>
```

`--project` spawns a fresh preview server with `HYPERFRAME_RUNTIME_URL` unset and kills
it after â€” preferred. `--json` for machine output. `--fps 30` default.

## ledger.json

Lives at the project root. One row per seam; this is the vector ledger as data.

```json
{
  "fps": 30,
  "seams": [
    {
      "id": "hookâ†’claim",
      "cut": 4.2,
      "technique": "cut-the-curve LEFT",
      "exit": { "selector": "#el-hook", "axis": "x", "dir": -1 },
      "entry": { "selector": "#el-claim", "axis": "x", "dir": -1 }
    },

    {
      "id": "claimâ†’payoff",
      "cut": 10.2,
      "technique": "inverse zoom-through",
      "exit": { "selector": "#el-claim", "axis": "z", "dir": -1 },
      "entry": { "selector": "#el-payoff", "axis": "z", "dir": -1, "scanRoot": "#el-payoff" }
    },

    {
      "id": "uiâ†’player (match cut)",
      "cut": 60.6,
      "type": "match-cut",
      "carrier": { "out": "#resting-card", "in": "#product-video" }
    }
  ]
}
```

- `cut` â€” seconds on the master clock, the frame the incoming side ignites.
- `type` â€” `"cut"` (default; full vector checks), `"match-cut"` / `"morph"`
  (carrier-continuity + overlap only; motion may start AT the boundary).
- `axis` â€” `"x"`, `"y"`, or `"z"` (z = scale). `dir` â€” sign of motion:
  x âˆ’1 = leftward, y âˆ’1 = upward, z +1 = push (growing), z âˆ’1 = pull (shrinking).
- `selector` â€” the element that CARRIES the seam motion. Use the wrapper when the
  master timeline moves the wrapper; use the in-comp hero (id or `[data-hf-id=â€¦]`)
  when the seam motion is authored inside the sub-comp. `probe` tells you which.
- `entry.scanRoot` (z seams) â€” subtree scanned for sign-fighting internal entrances;
  defaults to the entry selector.
- `carrier` â€” optional on `"cut"` rows; required on match-cut/morph. `out`/`in` rects
  must match at cutÂ±1 frame (12px center / 5% size tolerance, ancestors included).

## What each check enforces (Seam Gate rule â†” report row)

| Report row                           | Rule                                                           |
| ------------------------------------ | -------------------------------------------------------------- |
| `ledger`                             | exit/entry vectors match in the PLAN (axis + dir)              |
| `exit-moving` / `entry-moving`       | rule 1/3 â€” no settled exits, no from-rest entries              |
| `exit-direction` / `entry-direction` | rule 3 â€” measured sign matches the ledger                      |
| `speed-match` (WARN)                 | law Â§3 â€” entry velocity â‰ˆ exit velocity                        |
| `zero-overlap`                       | rule 6 â€” one side visible per frame, never both                |
| `z-sign-scan`                        | rule 7 â€” incoming scene's own entrances don't fight the Z sign |
| `carrier-*`                          | rules 3/4 â€” carrier rect continuity, ancestor scale included   |

Velocities are measured on `getBoundingClientRect` (center for x/y, width-ratio for z),
so ancestor wrapper transforms are automatically included.
