
# DAMA - Data Lifecycle and Retention Map

## The Framework

Use this skill to produce: **A lifecycle-retention map with creation/acquisition, storage, usage, sharing, archive, retention, disposition, owners, controls, and exceptions.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- A team keeps data forever by default
- Retention obligations differ by dataset
- Archival is mixed up with backup
- A dataset has no owner for disposal
- Privacy/security programs need lifecycle controls

## How To Apply

- Define lifecycle states for each dataset or data domain.
- Map owners, systems, controls, value, risk, and metadata at each state.
- Attach retention triggers, legal holds, archive requirements, and disposal methods.
- Define review cadence and exceptions for business, legal, or historical value.

## Sub-Rules

- Lifecycle begins at acquisition/creation, not when data lands in the warehouse.
- Retention is a business/legal control, not just a storage-cost decision.
- Archive, backup, and records retention serve different purposes.
- Disposition needs evidence, authority, and operational procedures.

## Common Failure Modes

- Forever default: keeps data because deletion is scary or unowned.
- Backup confusion: assumes backups satisfy archive or records requirements.
- No hold process: retention automation deletes data under legal or audit hold.
- Lifecycle blind spot: derived copies and exports escape the retention map.

## Overlap Guardrails

Do not use for database backup strategy alone; use when lifecycle governance and retention/disposition are the decision.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- DAMA International - DAMA-DMBOK: Data Management Body of Knowledge, 2nd ed. (Technics Publications, 2017), lifecycle concepts across DMBOK knowledge areas.
- Sibling skills: references/dama-data-management-capability-assessment.md, references/dama-governance-function-map.md, references/dama-metadata-management-plan.md, references/dama-master-reference-data-control.md, references/dama-data-architecture-blueprint.md, references/dama-data-security-privacy-classification.md.
