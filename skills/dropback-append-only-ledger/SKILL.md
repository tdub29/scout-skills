---
name: dropback-append-only-ledger
description: Apply Dropback's "Append-Only Storage" pillar from The Data Engine whitepaper to design an immutable, event-sourced store where nothing is ever overwritten and every source observation is preserved permanently. Use this skill whenever the user is about to UPDATE, UPSERT, or overwrite a row they might later want history for; is designing a database table, ingestion job, scraper, sync, or ETL that records facts that change over time (status, grade, price, score, rating, address, ownership); is asking "how did this value change over time," "can we see what it was before," "why did this flip," or "what did we know on date X"; mentions event sourcing, immutable log, append-only, audit trail, change history, change data capture, "never overwrite," idempotent ingestion, re-ingestion, dedupe on re-run, bronze/silver layers, or raw payload retention; is debugging duplicate rows appearing after a re-run; or is wiring up a "last_updated" column and clobbering whatever was there before. Trigger even when the user does not say "append-only" â€” "I'll just update the record," "set status = X," "overwrite the old value," "keep only the latest," or "we re-ran the scraper and now there are dupes" all qualify. Output is a concrete append-only schema/ingest design (or an audit of an existing one): what to record as immutable observations, the natural idempotency key that makes re-ingestion safe, the split between event-time and observed-time, how raw payloads are retained for re-derivation, and how current state is projected over the log instead of stored as a mutable row. DO NOT TRIGGER FOR deriving as-of truth across two time axes or reconciling conflicting sources into one corrected value â€” that is `dropback-bitemporal-truth`; this skill is the storage discipline underneath it.
---

# Dropback: Append-Only Storage

## When to use

Trigger at the moment the user is about to destroy history â€” usually right before an `UPDATE`, `UPSERT`, or "overwrite the old value" â€” or while designing any store that records facts that mutate over time. Concrete cues:

- The user is writing a table where one row per entity gets overwritten as new data arrives (a `status`, `grade`, `price`, `rating`, `current_*` column).
- They are building a scraper / sync / ETL and ask how to avoid duplicate rows when it re-runs.
- They say "just update the record," "keep only the latest," "set X = Y," or "we don't need the old value."
- They want to answer "what did we know on date X," "how did this change," or "why did it flip" and the schema can't answer it.
- They are wiring `last_updated` / `updated_at` and clobbering the prior value in place.
- They mention bronze/silver tiers, change data capture, event sourcing, or audit requirements.

Don't trigger for: deriving the correct as-of value across valid-time and system-time, or reconciling conflicting sources into one canonical fact â€” that is `dropback-bitemporal-truth`. This skill builds the immutable log that the bitemporal skill reads from. If the question is "store it so nothing is lost," it's this skill; if it's "given the log, what was true as-of T," it's bitemporal.

## The framework

### Core thesis: Never. Overwrite. Anything.

Dropback's first architectural commitment is literal: nothing is ever edited in place. Every observation a source sends you is preserved permanently as an immutable event â€” stamped with what it said and when it arrived. The cost is more storage and compute; the payoff is a permanently queryable history you can never get back once you've overwritten it. The whitepaper's test case: retrieve a scout's grade for a player "during his junior year, but before his position switch." An overwriting system cannot answer that â€” the grade was stepped on. An append-only system can, because "no later update was allowed to step on it." The pattern is old and proven: financial ledgers reconstruct any account state at any moment, Git replays a repo at any commit, blockchains verify balances from inception. You are building a ledger, not a spreadsheet.

### Observations are immutable events, not mutable rows

The unit of storage is an *observation*: "source S reported fact F, on event-date D, and we recorded it at time O." Each observation is one append-only row. A correction is not an edit â€” it is a *new* observation that supersedes the old one in the projection, while both remain on the log forever. There is no `UPDATE` and no `DELETE` on the event table; the only write is `INSERT`.

### Bronze and silver: raw landing, then derived canon

Keep two append-only tiers. **Bronze** holds the raw observation exactly as the source sent it â€” the unparsed (or minimally parsed) payload, the source label, the URLs, the timestamps. **Silver** holds the cleaned/normalized event derived from bronze. Both are append-only; bronze exists so that when your parser, matcher, or scoring logic improves, you can re-derive silver from the original bytes "all the way back through history, automatically" â€” without re-scraping a source that may no longer serve the old data.

### Event-time vs observed-time are two different clocks

Every observation carries (at least) two timestamps and you must never collapse them:

- **Event-time** (valid time): when the thing happened *in the world* / the date the source reports â€” e.g. the date a player entered the portal.
- **Observed-time** (system/ingest time): when *you* recorded it â€” when your job ran and wrote the row.

These diverge constantly: you ingest a June 1 entry on June 3; a source backfills a correction dated last week today. Storing only one clock means you can never reconstruct "what we knew, when we knew it." (Deriving truth across both axes is `dropback-bitemporal-truth`'s job â€” but you cannot do it at all unless the storage layer captured both.)

### The natural idempotency key makes re-ingestion safe

A scraper that re-runs nightly will re-see the same observation many times. Without a key, every re-run appends duplicates and your log becomes garbage. The fix is a **natural key** on the *content of the observation* â€” the combination of fields that means "this is the same observation, not a new one." Re-inserting a row whose natural key already exists is a no-op (a swallowed conflict), not an error and not an update. This is what lets you run the pipeline as often as you like and converge to the same log.

### Current state is a projection, not a stored value

There is no authoritative "current status" row to update. Current state is *computed* â€” projected over the log by replaying or selecting the latest/winning observation per entity. You may *cache* a projection (a `current_status` column, a snapshot table, a materialized view) for read performance, but the cache is derived and disposable: the log is the source of truth, the projection is a convenience you can always rebuild. Snapshots also bound read cost on a log that grows without limit.

## How to apply (step-by-step)

1. **Name the observation.** Write one sentence: "source ___ reported that ___, on ___, and we recorded it at ___." If you can't fill all four blanks, you haven't found the event grain yet.
2. **Define the immutable event row.** Columns: entity id, event/fact type, the reported value(s), `event_date` (event-time), `observed_at` (observed-time), `source`, `source_url`, and a `raw` payload column. Forbid `UPDATE`/`DELETE` on it by convention (and ideally by trigger or permission).
3. **Choose the natural idempotency key.** Pick the field combination that uniquely identifies *one observation*. Add it as a `UNIQUE` constraint. Re-ingestion must hit this constraint and be swallowed, returning "already present" rather than inserting a dup or overwriting.
4. **Split the two clocks.** Confirm `event_date` comes from the source and `observed_at` is set by your code at write time. Never overwrite `event_date` with "now," and never let a re-run mutate `observed_at` of an existing row.
5. **Retain the raw payload.** Store the original blob (JSON/HTML/CSV row) on every event so silver can be re-derived if parsing or scoring logic changes. If you only keep parsed fields, you've thrown away your ability to fix the past.
6. **Make current state a projection.** Compute "latest/winning per entity" as a query, view, or rebuildable cache â€” not as the table you mutate. If you keep a `current_*` convenience column, document that it is derived from the log and can be regenerated. For a ledger where "winning" means an iterative refinement beating what came before (not just the newest fact), gate the promotion: a new entry becomes the accepted projection only when replay confirms it beats the prior accepted winner. Recursive confidence is not approval.
7. **Add snapshots/projections for read scale.** Once the log is large, materialize periodic snapshots or a denormalized read model so queries don't replay the entire history every time.
8. **Sanity-check by replaying the past.** Pose a "what did we know on date X, and what was the value before event Y" question and confirm the schema answers it from the log alone. If it can't, a clock is missing or something is being overwritten.

## Worked example: the USD portal `portal_events` table

The baseball portal pipeline (`db/schema.sql`, `src/portal/db.py`, `src/portal/sources/base.py`) is a textbook append-only ledger:

- **Immutable event log.** `portal_events` is commented "full history; never overwrite." It records `event_type` (ENTERED | WITHDRAWN | COMMITTED), the source, the URLs, and a `raw_json` blob â€” "original parsed blob, for re-processing" (the bronze-retention move).
- **Two clocks, explicitly.** `event_date` = "date reported (source's date)" (event-time); `observed_at` = "when WE ingested it" (observed-time). They are separate columns, never collapsed.
- **Natural idempotency key.** `UNIQUE(player_id, event_type, source, event_date)` â€” commented "idempotent re-runs." `add_portal_event()` does a plain `INSERT` and catches `sqlite3.IntegrityError`, returning `False` on a duplicate. It **never** issues an `UPDATE` to the event row â€” the only write is an append.
- **Current state is a projection.** The `players.current_status` column is a *cached* projection: `base.py` updates it only because COMMITTED/WITHDRAWN supersede ENTERED, while the immutable history of every transition still lives in `portal_events`. The log is truth; `current_status` is the convenience cache, rebuildable from the log.

This is the storage discipline. Turning that log into "what was the player's status as-of the May call window, given a correction filed later" is `dropback-bitemporal-truth`.

## Common failure modes

- **Mutating the row in place.** The default instinct â€” `UPDATE players SET status = 'COMMITTED'` â€” destroys the prior state permanently. You can never answer "what was it before," and you've silently lost the audit trail. Append a new observation instead; let current state be a projection.
- **No idempotency key â†’ duplicate events on re-run.** A scraper without a `UNIQUE` natural key appends the same observation every night, and the log fills with dupes that corrupt every downstream count and projection. Add the natural key; make re-insertion a swallowed no-op.
- **Conflating event-time and ingest-time.** Stamping the event with `now()` instead of the source's date (or vice-versa) makes "what we knew when" unanswerable, because both clocks have been smeared into one. Keep `event_date` (from source) and `observed_at` (from your code) as separate, independently-set columns.
- **Not storing the raw payload.** Keeping only parsed fields means that when your parser or scoring model improves, you cannot re-derive the past â€” you'd have to re-scrape a source that may no longer serve the old data. Retain the original blob (`raw_json`) on every event so silver is always rebuildable from bronze.
- **Unbounded log with no projection/snapshot.** A pure event log with no read model forces every query to replay all of history, which gets slow as the log grows. Materialize snapshots or a cached current-state projection for reads â€” while keeping the log as the rebuildable source of truth.
- **Treating a correction as an edit.** A late correction is a new observation that *supersedes* the old one in the projection, not an `UPDATE` that erases it. Append the correction; resolve which wins at read time. Both observations stay on the log forever.

## References

- Dropback â€” The Data Engine whitepaper, https://www.dropback.com/blog/data-engine-whitepaper, "Append-Only Storage" pillar ("Never. Overwrite. Anything."; bronze/silver tiers; the junior-year-before-position-switch grade example; ledger/Git/blockchain precedents).
- Worked example in this repo: `db/schema.sql` (`portal_events`), `src/portal/db.py` (`add_portal_event`), `src/portal/sources/base.py` (adapter `ingest()`).
- Sibling carved skills:
  - `dropback-bitemporal-truth` â€” derives as-of truth across valid-time and system-time; reads the immutable log this skill produces. (THIS skill = storage discipline; that skill = time-travel queries.)
  - `dropback-entity-resolution` â€” binds fragmented records to one canonical entity; append-only storage preserves the observation chains that justify each binding.
  - `dropback-graph-native` â€” models resolved entities and their observations as a graph; the event log is the immutable substrate the graph is built over.
