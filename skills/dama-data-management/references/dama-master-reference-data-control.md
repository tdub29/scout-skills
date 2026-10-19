
# DAMA - Master and Reference Data Control

## The Framework

Use this skill to produce: **An MDM/reference data control plan with domains, authoritative sources, identifiers, matching/survivorship, distribution, and change governance.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- Customer or product entities differ across systems
- A code set changes and breaks reports
- Golden records are disputed
- Reference lists are copied in spreadsheets
- MDM scope is unclear

## How To Apply

- Classify the domain as master data, reference data, or both.
- Identify authoritative sources, consumers, identifiers, and matching rules.
- Define stewardship, survivorship, hierarchy, and exception handling.
- Specify distribution, synchronization, versioning, and change approval.

## Sub-Rules

- Master data describes core business entities shared across processes.
- Reference data defines permissible values and code sets used for classification.
- Survivorship rules must be business-owned and explainable.
- Reference data changes need versioning and effective dates when history matters.

## Common Failure Modes

- Golden-record mysticism: no explicit matching, survivorship, or exception process.
- Spreadsheet code-set drift: each team copies reference values and updates them independently.
- MDM overreach: tries to centralize every attribute before proving shared need.
- No distribution contract: authoritative data exists but consumers keep stale local copies.

## Overlap Guardrails

Do not use for Kimball conformed dimensions; use this for enterprise entity/code control before or outside dimensional models.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- DAMA International - DAMA-DMBOK: Data Management Body of Knowledge, 2nd ed. (Technics Publications, 2017), Chapter 10.
- Sibling skills: references/dama-data-management-capability-assessment.md, references/dama-governance-function-map.md, references/dama-metadata-management-plan.md, references/dama-data-architecture-blueprint.md, references/dama-data-security-privacy-classification.md, references/dama-data-lifecycle-retention-map.md.
