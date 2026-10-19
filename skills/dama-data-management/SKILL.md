---
name: dama-data-management
description: "DAMA-DMBOK: governance, MDM, metadata, retention."
---

# dama-data-management

Book provenance: **DAMA International - DAMA-DMBOK: Data Management Body of Knowledge (2nd ed.)**. Load the matching `references/*.md` file when a specific framework is needed.

## When to use

Use this hub when the user's question matches any sub-framework trigger in the frontmatter description. Route to **one** reference file, read it fully, then execute that framework's process and output format.

Do not improvise a hybrid of multiple frameworks unless the user explicitly asks for a combined pass.

## Quick routing

| User cue (examples) | Reference |
| Data architecture practice, target architecture, enterprise data model, data flow standards, architecture governance | `references/dama-data-architecture-blueprint.md` |
| Data lifecycle, retention schedule, archival, disposal, records management, data minimization | `references/dama-data-lifecycle-retention-map.md` |
| Data management maturity, DMBOK assessment, capability model, CDO priorities, program roadmap | `references/dama-data-management-capability-assessment.md` |
| Data security classification, privacy controls, sensitive/PII data, access policy, compliance risk | `references/dama-data-security-privacy-classification.md` |
| Governance operating framework, governance council, data policy map, stewardship roles, decision rights | `references/dama-governance-function-map.md` |
| MDM, reference data, golden record, code set governance, customer/product master, data matching | `references/dama-master-reference-data-control.md` |
| Metadata management, data catalog plan, business glossary, technical/lineage metadata, metadata quality | `references/dama-metadata-management-plan.md` |

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

- [references/dama-data-architecture-blueprint.md](references/dama-data-architecture-blueprint.md)
- [references/dama-data-lifecycle-retention-map.md](references/dama-data-lifecycle-retention-map.md)
- [references/dama-data-management-capability-assessment.md](references/dama-data-management-capability-assessment.md)
- [references/dama-data-security-privacy-classification.md](references/dama-data-security-privacy-classification.md)
- [references/dama-governance-function-map.md](references/dama-governance-function-map.md)
- [references/dama-master-reference-data-control.md](references/dama-master-reference-data-control.md)
- [references/dama-metadata-management-plan.md](references/dama-metadata-management-plan.md)

- **Book:** DAMA International - DAMA-DMBOK: Data Management Body of Knowledge (2nd ed.)