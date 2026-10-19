---
name: mcgilvray-data-quality-project
description: Apply McGilvray's Ten Steps data quality discipline: project charter, assessment baseline, root-cause remediation, monitoring control plan. Triggers: data quality project, DQ charter, quality baseline, profiling, root cause, remediation, monitoring controls, Ten Steps. Load the matching reference file when a specific framework is needed.
---

# mcgilvray-data-quality-project

Book provenance: **Danette McGilvray - Executing Data Quality Projects (Morgan Kaufmann, 2008)**. Load the matching `references/*.md` file when a specific framework is needed.

## When to use

Use this hub when the user's question matches any sub-framework trigger in the frontmatter description. Route to **one** reference file, read it fully, then execute that framework's process and output format.

Do not improvise a hybrid of multiple frameworks unless the user explicitly asks for a combined pass.

## Quick routing

| User cue (examples) | Reference |
| DQ charter, scope, business case, Ten Steps subset | `references/dq-project-charter.md` |
| Assessment baseline, profiling, dimensions, current state | `references/dq-assessment-baseline.md` |
| Root cause, remediation, corrective and preventive actions | `references/dq-root-cause-remediation.md` |
| Monitoring, control plan, thresholds, ongoing quality | `references/dq-monitoring-control-plan.md` |

## How to apply

1. Match the user request to a row in **Quick routing** (or the description triggers).
2. Read the corresponding file under `references/`.
3. Follow that reference's artifact, process, failure modes, and output format.
4. Return the reference's output artifact; add hub-level manipulation-risk or cross-reference notes only when the reference requires it.

## Common failure modes (hub-level)

- **Wrong reference** - loading one sub-framework when another row in Quick routing fits better.
- **Router-only answer** - summarizing the hub without loading the reference's full framework.
- **Retired atomic names** - legacy per-framework skill folders were collapsed into this hub; use `references/` only.
- **Skipping evidence** - each reference requires evidence-backed scores and explicit unknowns; do not default to parity.

## References

- [references/dq-project-charter.md](references/dq-project-charter.md)
- [references/dq-assessment-baseline.md](references/dq-assessment-baseline.md)
- [references/dq-root-cause-remediation.md](references/dq-root-cause-remediation.md)
- [references/dq-monitoring-control-plan.md](references/dq-monitoring-control-plan.md)

- **Book:** Danette McGilvray - Executing Data Quality Projects (Morgan Kaufmann, 2008)