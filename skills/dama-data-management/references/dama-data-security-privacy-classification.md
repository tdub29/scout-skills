
# DAMA - Data Security and Privacy Classification

## The Framework

Use this skill to produce: **A security/privacy classification matrix with data categories, sensitivity, legal basis, access rules, controls, monitoring, and retention implications.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- A dataset may include PII or regulated data
- Access rules differ by role and purpose
- Cloud or vendor sharing needs a control review
- Metadata lacks security attributes
- Privacy obligations are not connected to lifecycle

## How To Apply

- Identify data categories, subjects, sensitivity, jurisdictions, and business purposes.
- Map legal, regulatory, ethical, and contractual requirements.
- Define access, encryption, masking, logging, sharing, and monitoring controls.
- Bind classifications into metadata and lifecycle rules.

## Sub-Rules

- Security classification must be visible in metadata and operations, not just policy.
- Access decisions need purpose, role, least privilege, and approval path.
- Privacy controls include collection, use, sharing, retention, and deletion.
- Outsourcing/cloud changes responsibility allocation but not accountability.

## Common Failure Modes

- PII checkbox: treats sensitivity as yes/no and misses purpose or jurisdiction.
- Policy-control gap: rules exist but are not enforced in platforms or workflows.
- Access sprawl: exceptions accumulate with no review or recertification.
- Retention conflict: data is protected at rest but kept longer than allowed or needed.

## Overlap Guardrails

Do not provide legal advice; escalate jurisdiction-specific compliance decisions to counsel. Use this as a data management control artifact.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- DAMA International - DAMA-DMBOK: Data Management Body of Knowledge, 2nd ed. (Technics Publications, 2017), Chapters 2 and 7.
- Sibling skills: references/dama-data-management-capability-assessment.md, references/dama-governance-function-map.md, references/dama-metadata-management-plan.md, references/dama-master-reference-data-control.md, references/dama-data-architecture-blueprint.md, references/dama-data-lifecycle-retention-map.md.
