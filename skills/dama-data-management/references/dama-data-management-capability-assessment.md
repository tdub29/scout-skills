
# DAMA - Data Management Capability Assessment

## The Framework

Use this skill to produce: **A capability assessment scorecard across data management areas with current state, target state, evidence, gaps, and prioritized roadmap.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- A CDO needs a current-state data management baseline
- Teams argue whether the data program is governance, architecture, quality, or metadata first
- Budget needs a capability-based roadmap
- A data organization wants to compare maturity by domain
- Leadership asks what data management means operationally

## How To Apply

- List relevant DAMA knowledge areas and scope them to the organization.
- Score each area on practice existence, adoption, ownership, tooling, metrics, and risk.
- Collect evidence, not impressions, for each score.
- Prioritize investments by business impact, dependency, and readiness.

## Sub-Rules

- Capability assessment is broader than data governance or data quality alone.
- Scores need evidence and named owners to avoid maturity theater.
- Target state should differ by business need; not every area needs maximum maturity.
- Roadmaps should sequence foundational dependencies before advanced automation.

## Common Failure Modes

- Governance monoculture: calls every data problem governance and misses architecture/security/metadata gaps.
- Maturity vanity: assigns high scores with no artifacts or adoption evidence.
- Tool-first roadmap: buys catalog/MDM/security tools before practices and accountability exist.
- One-size target: assumes every domain needs the same maturity level.

## Overlap Guardrails

Do not use for McGilvray-style data quality baseline or Seiner stewardship matrices; use for cross-capability DMBOK assessment.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- DAMA International - DAMA-DMBOK: Data Management Body of Knowledge, 2nd ed. (Technics Publications, 2017), Chapter 1 and knowledge-area chapters.
- Sibling skills: references/dama-governance-function-map.md, references/dama-metadata-management-plan.md, references/dama-master-reference-data-control.md, references/dama-data-architecture-blueprint.md, references/dama-data-security-privacy-classification.md, references/dama-data-lifecycle-retention-map.md.
