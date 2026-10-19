
# Kleppmann - Transaction Isolation Anomaly Audit

## The Framework

Use this skill to produce: **An isolation anomaly checklist with workflow steps, concurrent interleavings, required guarantees, and implementation options.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- Two users can update related records at the same time
- A balance/report changes while being read
- Unique or capacity constraints span multiple rows
- An ORM transaction passes tests but fails under concurrency
- Choosing between read committed, snapshot isolation, and serializable

## How To Apply

- Write the business invariant in plain language.
- Map the read and write set for each transaction step.
- Simulate two concurrent transactions and identify anomaly classes.
- Choose isolation, locks, constraints, compare-and-set, or retry strategy.

## Sub-Rules

- Read committed prevents some dirty reads/writes but leaves many race conditions.
- Snapshot isolation gives consistent reads but can allow write skew.
- Lost updates require explicit protection, not hope.
- Serializable isolation is the reference behavior; lower levels need anomaly acceptance.

## Common Failure Modes

- Single-user reasoning: validates transactions only in sequential examples.
- ORM comfort: assumes framework transaction wrappers imply serializability.
- Constraint gap: checks a condition in application code without protecting the rows it depends on.
- Retry omission: detects conflicts but has no idempotent retry path.

## Overlap Guardrails

Do not use for generic database API syntax; use when concurrent correctness is the question.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- Martin Kleppmann - Designing Data-Intensive Applications, 2nd ed. early release (O'Reilly, 2025/2026), Chapter 7.
- Sibling skills: references/kleppmann-rsm-tradeoff-audit.md, references/kleppmann-storage-index-choice.md, references/kleppmann-replication-topology-choice.md, references/kleppmann-partitioning-hotspot-audit.md, references/kleppmann-stream-batch-derived-data-choice.md, references/kleppmann-consensus-coordination-boundary.md, references/kleppmann-schema-evolution-compatibility.md.
