
# Kleppmann - Schema Evolution and Compatibility

## The Framework

Use this skill to produce: **A compatibility matrix covering old/new writers, old/new readers, migration order, defaults, unknown fields, and rollback safety.**

This is not a summary route. It should fire only when the user needs the artifact above and the request matches the trigger surface in the frontmatter.

## Trigger Checks

- Changing an event schema consumed by multiple services
- Adding/removing columns in a rolling deploy
- Migrating stored JSON or Avro records
- A consumer breaks after a producer upgrade
- Designing long-lived data formats

## How To Apply

- Identify all readers, writers, stored formats, and deployment order constraints.
- Classify change as backward-compatible, forward-compatible, both, or neither.
- Specify defaults, optionality, unknown-field handling, and semantic versioning rules.
- Plan expand-migrate-contract steps and rollback behavior.

## Sub-Rules

- Backward compatibility means new readers can read old data.
- Forward compatibility means old readers can read new data.
- Rolling upgrades require mixed-version operation, not just final-state correctness.
- Data formats carry semantic contracts beyond field names and types.

## Common Failure Modes

- Flag-day migration: requires all producers and consumers to change simultaneously.
- Optional field abuse: makes every change syntactically safe but semantically ambiguous.
- Unknown-field loss: intermediate services drop data they do not understand.
- Schema registry theater: registers schemas but does not test real consumer behavior.

## Overlap Guardrails

Do not use for UI API versioning alone unless persisted messages/data and mixed-version consumers are central.

## Output Format

Return the artifact in this order:

1. **Decision context:** one paragraph naming the business/system decision.
2. **Working table or checklist:** the concrete rows, columns, scores, or mappings required by the artifact.
3. **Recommendation:** the chosen design or next action and why.
4. **Risks and tests:** the top failure modes to verify before adoption.

## References

- Martin Kleppmann - Designing Data-Intensive Applications, 2nd ed. early release (O'Reilly, 2025/2026), Chapter 4 and system evolution chapters.
- Sibling skills: references/kleppmann-rsm-tradeoff-audit.md, references/kleppmann-storage-index-choice.md, references/kleppmann-replication-topology-choice.md, references/kleppmann-partitioning-hotspot-audit.md, references/kleppmann-transaction-isolation-anomaly-audit.md, references/kleppmann-stream-batch-derived-data-choice.md, references/kleppmann-consensus-coordination-boundary.md.
