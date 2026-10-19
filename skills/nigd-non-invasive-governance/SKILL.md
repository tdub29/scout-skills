---
name: nigd-non-invasive-governance
description: Apply Robert Seiner's non-invasive data governance: stewardship accountability matrix, common data matrix, activity matrix. Triggers: data governance, stewardship, data steward, governance council, RACI, accountability matrix, common data, domain ownership, embed governance in projects, policy change, access approval, quality remediation. Load the matching reference file when a specific framework is needed.
---

# nigd-non-invasive-governance

Book provenance: **Robert Seiner - Non-Invasive Data Governance (Technics Publications, 2014)**. Load the matching `references/*.md` file when a specific framework is needed.

## When to use

Use this hub when the user's question matches any sub-framework trigger in the frontmatter description. Route to **one** reference file, read it fully, then execute that framework's process and output format.

Do not improvise a hybrid of multiple frameworks unless the user explicitly asks for a combined pass.

## Quick routing

| User cue (examples) | Reference |
| Steward roles, accountability matrix, operational/tactical/strategic layers | `references/stewardship-accountability-matrix.md` |
| Common data matrix, domain vs role, who governs customer/product data | `references/common-data-matrix.md` |
| Activity matrix, embed governance in projects/issues/policy | `references/activity-matrix.md` |

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

- [references/stewardship-accountability-matrix.md](references/stewardship-accountability-matrix.md)
- [references/common-data-matrix.md](references/common-data-matrix.md)
- [references/activity-matrix.md](references/activity-matrix.md)

- **Book:** Robert Seiner - Non-Invasive Data Governance (Technics Publications, 2014)