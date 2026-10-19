
# Kleppmann - Consensus and Coordination Boundary

## The Framework

Use this skill to produce: **A coordination boundary decision record identifying invariants that require agreement, candidate primitives, and where weaker consistency is acceptable.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- A distributed lock protects a critical invariant
- Leader election or cluster membership is being designed
- A product asks for global uniqueness or no double booking
- Quorum reads/writes are proposed without naming guarantees
- A system suffered split brain

## How To Apply

- List invariants that cannot tolerate concurrent disagreement.
- Separate coordination-required paths from eventually consistent paths.
- Choose the coordination primitive: consensus log, linearizable register, transaction, lease, fencing token.
- Define failure model, timeout behavior, and operational visibility.

## Sub-Rules

- Consensus is for agreement under faults, not a generic scale tool.
- Linearizability is a user-visible recency guarantee with latency and availability costs.
- Locks need fencing or they can be unsafe after pauses and timeouts.
- Total order broadcast, consensus, and replicated logs are related building blocks.

## Common Failure Modes

- Lock-name cargo cult: uses Redis or DB locks without fencing stale holders.
- Consensus everywhere: slows paths that could tolerate eventual consistency.
- Timeout-as-truth: assumes a slow node is dead and creates split-brain behavior.
- Quorum arithmetic without model: picks R/W/N numbers without failure or staleness assumptions.

## Overlap Guardrails

Do not use for ordinary replication topology choice; use when the problem is agreement, ordering, or distributed invariants.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- Martin Kleppmann - Designing Data-Intensive Applications, 2nd ed. early release (O'Reilly, 2025/2026), Chapters 8-9.
- Sibling skills: references/kleppmann-rsm-tradeoff-audit.md, references/kleppmann-storage-index-choice.md, references/kleppmann-replication-topology-choice.md, references/kleppmann-partitioning-hotspot-audit.md, references/kleppmann-transaction-isolation-anomaly-audit.md, references/kleppmann-stream-batch-derived-data-choice.md, references/kleppmann-schema-evolution-compatibility.md.
