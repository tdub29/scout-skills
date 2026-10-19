
# DAMA - Data Governance Function Map

## The Framework

Use this skill to produce: **A governance function map with decision domains, forums, roles, policies, issue escalation, and operating metrics.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- Standing up a governance council
- Clarifying which decisions governance owns
- Connecting policies to projects and operations
- Designing escalation for data issues
- Checking whether governance is real or ceremonial

## How To Apply

- Define the governance scope and business drivers.
- Map decision domains: definitions, quality thresholds, access, architecture, lifecycle, standards.
- Assign forums and roles for strategic, tactical, and operational decisions.
- Define policy lifecycle, issue escalation, metrics, and touchpoints with delivery work.

## Sub-Rules

- Governance is decision-making and accountability, not just a committee.
- Policies need standards, procedures, and enforcement paths to matter.
- Touchpoints embed governance into projects, operations, and change management.
- Metrics should measure decisions resolved, risk reduced, and adoption, not meeting volume.

## Common Failure Modes

- Committee-only governance: creates meetings without decision rights.
- Policy shelfware: publishes documents no one uses in delivery or operations.
- Stewardship ambiguity: names stewards but not their decisions or escalation authority.
- Governance bypass: projects change data definitions/access without a touchpoint.

## Overlap Guardrails

Overlaps with nigd-*; use this for DAMA function/operating-framework mapping, not non-invasive steward-role placement alone.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- DAMA International - DAMA-DMBOK: Data Management Body of Knowledge, 2nd ed. (Technics Publications, 2017), Chapter 3.
- Sibling skills: references/dama-data-management-capability-assessment.md, references/dama-metadata-management-plan.md, references/dama-master-reference-data-control.md, references/dama-data-architecture-blueprint.md, references/dama-data-security-privacy-classification.md, references/dama-data-lifecycle-retention-map.md.
