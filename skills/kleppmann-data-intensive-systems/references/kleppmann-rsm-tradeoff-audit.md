
# Kleppmann - Reliability Scalability Maintainability Audit

## The Framework

Use this skill to produce: **A three-axis architecture audit with failure assumptions, load parameters, evolvability risks, and prioritized design moves.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- A team wants to pick a database or queue based on benchmarks alone
- An architecture works in demos but fails operationally
- Scaling fixes are making the system harder to operate
- Reliability requirements are vague
- A design review needs explicit tradeoffs

## How To Apply

- State the system's correctness promise when faults occur.
- Describe load parameters: volume, throughput, latency distribution, fanout, hot keys.
- List maintenance tasks: schema changes, debugging, backfills, migrations, onboarding.
- Score proposed changes against all three axes before recommending.

## Sub-Rules

- Reliability is continuing to work correctly despite faults, not merely uptime.
- Scalability is preserving performance as load grows, not choosing a distributed tool by default.
- Maintainability includes operability, simplicity, and evolvability.
- Optimizing one axis can degrade the others; make the trade visible.

## Common Failure Modes

- Availability-only reliability: ignores correctness, data loss, or human recovery procedures.
- Premature distribution: adds network and coordination failure before load requires it.
- Benchmark tunnel vision: average latency hides tail behavior and operational complexity.
- Hero-maintained system: relies on tribal knowledge instead of understandable design.

## Overlap Guardrails

Do not use as a generic system-design mega skill; route only when the artifact is a DDIA-style quality tradeoff audit.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- Martin Kleppmann - Designing Data-Intensive Applications, 2nd ed. early release (O'Reilly, 2025/2026), Chapter 1.
- Sibling skills: references/kleppmann-storage-index-choice.md, references/kleppmann-replication-topology-choice.md, references/kleppmann-partitioning-hotspot-audit.md, references/kleppmann-transaction-isolation-anomaly-audit.md, references/kleppmann-stream-batch-derived-data-choice.md, references/kleppmann-consensus-coordination-boundary.md, references/kleppmann-schema-evolution-compatibility.md.
