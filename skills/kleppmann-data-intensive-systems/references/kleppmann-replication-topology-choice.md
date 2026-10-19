
# Kleppmann - Replication Topology Choice

## The Framework

Use this skill to produce: **A replication decision record with topology, consistency guarantees, lag expectations, conflict policy, and failover runbook questions.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- Adding replicas for read scale or regional availability
- Users write in multiple regions
- Replica lag causes stale reads
- Failover could lose acknowledged writes
- Conflict resolution is undefined

## How To Apply

- State why replication is needed: availability, latency, read scale, durability, or migration.
- Choose topology and name the write authority path.
- Define read guarantees and stale-read tolerance per user workflow.
- Specify failover and conflict resolution before production use.

## Sub-Rules

- Single-leader simplifies writes but introduces failover and lag concerns.
- Multi-leader helps local writes but creates conflict-resolution requirements.
- Leaderless replication trades coordination for quorum choices and read repair complexity.
- Replication lag is a product behavior whenever users read after writing.

## Common Failure Modes

- Replica-as-cache fantasy: assumes stale reads cannot affect user promises.
- Multi-leader without conflicts: discovers duplicate edits and divergent records after launch.
- Automatic failover optimism: promotes a stale replica and loses acknowledged writes.
- Global consistency handwave: says active-active without naming which anomalies are acceptable.

## Overlap Guardrails

Do not use for distributed consensus selection; use `kleppmann-consensus-coordination-boundary` when the issue is agreement/coordination rather than copied data.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- Martin Kleppmann - Designing Data-Intensive Applications, 2nd ed. early release (O'Reilly, 2025/2026), Chapter 5.
- Sibling skills: references/kleppmann-rsm-tradeoff-audit.md, references/kleppmann-storage-index-choice.md, references/kleppmann-partitioning-hotspot-audit.md, references/kleppmann-transaction-isolation-anomaly-audit.md, references/kleppmann-stream-batch-derived-data-choice.md, references/kleppmann-consensus-coordination-boundary.md, references/kleppmann-schema-evolution-compatibility.md.
