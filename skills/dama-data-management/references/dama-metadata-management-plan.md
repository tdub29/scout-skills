
# DAMA - Metadata Management Plan

## The Framework

Use this skill to produce: **A metadata management plan with metadata types, repositories, capture methods, ownership, standards, quality controls, and usage workflows.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- Launching or rescuing a data catalog
- Business glossary and technical metadata disagree
- Lineage exists but users do not trust it
- Metadata is manually curated and stale
- A data product needs discoverability and context

## How To Apply

- Classify metadata needed: business, technical, operational, process, lineage, security, quality.
- Inventory authoritative sources and capture methods for each type.
- Assign stewardship, standards, and quality controls.
- Design usage workflows: search, impact analysis, onboarding, controls, and change review.

## Sub-Rules

- Metadata has value only when tied to real consumer and management workflows.
- Business and technical metadata must be connected, not separate glossaries.
- Operational metadata proves freshness, lineage, and process behavior.
- Metadata quality needs ownership, cadence, and validation like data quality.

## Common Failure Modes

- Catalog as inventory dump: imports tables without definitions, owners, usage, or trust signals.
- Manual-entry trap: requires stewards to retype metadata already emitted by systems.
- Glossary isolation: terms are defined but not linked to fields, reports, or policies.
- Lineage overclaim: pretty graphs exist but transformation semantics are missing.

## Overlap Guardrails

Do not use for one-off lineage tracing; use tracing skills for a specific upstream/downstream question.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- DAMA International - DAMA-DMBOK: Data Management Body of Knowledge, 2nd ed. (Technics Publications, 2017), Chapter 12.
- Sibling skills: references/dama-data-management-capability-assessment.md, references/dama-governance-function-map.md, references/dama-master-reference-data-control.md, references/dama-data-architecture-blueprint.md, references/dama-data-security-privacy-classification.md, references/dama-data-lifecycle-retention-map.md.
