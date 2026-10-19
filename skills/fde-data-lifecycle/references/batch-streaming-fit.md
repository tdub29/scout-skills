
# FDE Batch Streaming Fit

Use this when deciding how data should move and be processed over time. The output is a workload-fit matrix and recommendation.

## Artifact

Produce a batch/streaming decision matrix with:

1. **Freshness requirement** - actual decision latency, not aspirational real-time language.
2. **Event characteristics** - volume, velocity, ordering, lateness, replayability, and statefulness.
3. **Consumer tolerance** - acceptable delay, duplicate handling, correction workflow, and degraded-mode behavior.
4. **Operational burden** - monitoring, incident response, backfills, state recovery, cost, and team experience.
5. **Recommendation** - batch, microbatch, streaming, CDC-to-batch, or hybrid, with a migration path if requirements change.

## Process

1. Translate "real time" into a number. Ask what breaks at 5 seconds, 5 minutes, 1 hour, or 1 day of delay.
2. Separate ingestion latency from serving latency. A stream into a warehouse may still serve batch reports; a batch extract may feed near-real-time cache updates.
3. Evaluate event semantics. Streaming is a fit when event order, incremental state, reaction time, or continuous processing matter enough to pay the operational cost.
4. Account for replay and correction. Choose a design that can reprocess history, handle late data, and reconcile outputs after upstream fixes.
5. Start with the simplest cadence that meets the consumer outcome. Recommend streaming only when it changes a decision, user experience, risk control, or system action.

## Failure Modes

- **Real-time theater** - building streaming infrastructure for dashboards or workflows where hourly or daily data would make the same decision.
- **No replay plan** - adopting event streams without durable retention, idempotency, backfill, or state-rebuild strategy.
- **Latency metric confusion** - optimizing pipeline latency while the serving layer, approval process, or human workflow remains slow.
- **Operational mismatch** - selecting streaming when the team cannot monitor stateful jobs, recover checkpoints, or debug late/out-of-order data.
- **Batch lock-in** - keeping batch when risk, personalization, fraud, IoT, or operational use cases require continuous reaction.

## Output Format

Return the matrix, a clear recommendation, reasons against the rejected alternatives, and the minimum observability/backfill controls required for the chosen mode.

## References

- Joe Reis and Matt Housley, *Fundamentals of Data Engineering* (O'Reilly, 2022), Chapters 2 and 7.
- Sibling skills: `fde-lifecycle-architecture-map`, `fde-source-ingestion-contract`.
