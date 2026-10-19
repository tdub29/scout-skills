
# DAMA - Data Architecture Blueprint

## The Framework

Use this skill to produce: **A data architecture blueprint with current/target models, data domains, flows, standards, platform fit, gaps, and governance checkpoints.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- A data platform roadmap lacks architectural principles
- Multiple teams model the same domain differently
- Integration patterns are inconsistent
- Architecture review needs data-specific criteria
- A target data architecture is requested

## How To Apply

- Anchor architecture to business capabilities and information needs.
- Map data domains, conceptual/logical models, major stores, and flows.
- Define standards for modeling, integration, naming, storage, and interoperability.
- Identify current-target gaps and architecture governance checkpoints.

## Sub-Rules

- Data architecture connects business strategy to implementable data structures and movement.
- Models at conceptual, logical, and physical levels serve different decisions.
- Integration architecture should name patterns, contracts, and ownership boundaries.
- Architecture governance must be lightweight enough to shape real projects.

## Common Failure Modes

- Diagram-only architecture: produces boxes without standards, decisions, or adoption path.
- Physical-model tunnel vision: jumps to tables before conceptual/logical agreement.
- Platform-led architecture: lets tool selection define domain boundaries.
- Review-gate bottleneck: architecture governance arrives too late to influence design.

## Overlap Guardrails

Do not use for full software system design or data mesh domain ownership alone; use when DAMA-style enterprise data architecture is the artifact.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- DAMA International - DAMA-DMBOK: Data Management Body of Knowledge, 2nd ed. (Technics Publications, 2017), Chapter 4.
- Sibling skills: references/dama-data-management-capability-assessment.md, references/dama-governance-function-map.md, references/dama-metadata-management-plan.md, references/dama-master-reference-data-control.md, references/dama-data-security-privacy-classification.md, references/dama-data-lifecycle-retention-map.md.
