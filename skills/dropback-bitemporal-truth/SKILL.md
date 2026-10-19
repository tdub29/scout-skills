---
name: dropback-bitemporal-truth
description: Apply Dropback's "Bitemporal Truth" pillar (from The Data Engine whitepaper) to make a fact's current value DERIVED from an event/observation history rather than stored in a mutable column, using two time axes â€” valid-time (when the fact was true in the world) and system-time (when the system learned it) â€” so the model can answer "as-of" / point-in-time / time-travel queries. Use this skill whenever the user is designing or reviewing a schema and reaches for a mutable "status", "current_value", "state", "latest", or "is_active" column; whenever they ask "what did we believe on date X", "what was his grade then", "who was on the roster that week", "what was true as of <date>"; whenever they need slowly-changing dimensions done right, point-in-time joins, retroactive corrections, late-arriving / backfilled data, or reproducing a past decision; whenever they're tempted to UPDATE a row in place and would later regret losing history; or whenever a stored snapshot and an event log are drifting out of sync. Trigger even when the user never says "bitemporal" â€” "should this be a column or computed", "how do I keep history", "I need to query the past", "the status field is wrong after a correction", "why don't my old numbers reproduce", and "I overwrote it and lost the old value" all qualify. Output is a bitemporal model design (the two chosen time axes + an "as-of" projection query that returns the latest valid fact per entity as known at time T) OR an audit that flags stored mutable state that should be derived and shows the append-not-edit correction path. DO NOT TRIGGER FOR pure immutable-storage / write-discipline questions (use dropback-append-only-ledger), identity matching across sources (dropback-entity-resolution), or relationship/graph traversal (dropback-graph-native).
---

# Dropback: Bitemporal Truth

## When to use

Trigger when the user is deciding how a changeable fact lives in their data â€” and the honest answer is "it should be derived, not stored." Concrete cues:

- They're adding a `status` / `current_value` / `state` / `latest_*` / `is_active` column that one source will overwrite as things change.
- They ask, or will soon ask, a past-tense question: "what did we believe on date X," "what was his grade *then*," "who was on the roster *that week*," "what conference were they in *that season*."
- They've made a correction (a vendor fixed a date, a scout re-graded) and the "current" field is now wrong, ambiguous, or fighting the next feed.
- Data arrives late or out of order (a backfill, a retroactive entry, a delayed report) and they need it to slot into the *right* point in history, not just "now."
- A stored snapshot column and an event/observation log have drifted apart and nobody trusts which is right.
- They want to reproduce an old decision/report and the numbers no longer match because state was overwritten in place.

Don't trigger for: the *write discipline* of never overwriting rows (that's `dropback-append-only-ledger` â€” the immutable log THIS skill reads from); collapsing many source records into one entity (`dropback-entity-resolution`); or relationship traversal across entities (`dropback-graph-native`). This skill is specifically about deriving as-of truth across two time axes from a log that already exists.

## The framework

### Core thesis: truth is a function, not a stored opinion

Dropback's rule: "canonical truth â€” the value the platform presents as 'the real one' â€” is never a stored opinion. It is derived. Truth is computed from the full body of observations." Or, blunt: "Truth is a function, not a fact someone typed in once." A mutable `current_status` column is exactly the stored opinion the pillar rejects â€” it answers "what is true now" and *destroys* the ability to answer "what was true then" the moment it's overwritten. Because truth is a function over the observation history, it recomputes "all the way back through history, automatically" when matching gets smarter, a rule changes, or a new source arrives. You can't recompute history you've already erased; the log is the input, the current value is the output.

### The two time axes (this is what "bi-temporal" means)

A fact lives on two independent clocks. Conflating them is the central error.

1. **Valid-time** â€” *when the fact was true in the world.* Dropback frames this as "the dimension it varies along" (season, week, package, scout) and the basis for asking every question "as of" some moment. In the baseball log this is `event_date` (the date the entry/withdrawal/commit actually happened).
2. **System-time** â€” *when the system learned it.* Dropback: "every observation carries when we learned it on append-only storage." In the log this is `observed_at` (when we ingested the row).

They move independently. A portal entry can be valid June 2 (valid-time) but only learned by us June 5 (system-time) â€” late-arriving data. A vendor can correct that entry's date weeks later: same valid fact, new system-time row. Holding both lets you ask two genuinely different questions: "what was true as of June 3?" (valid-time slice) and "what did we *believe* on June 3, given only what we'd ingested by then?" (system-time slice). One axis can't answer both.

### The "as-of" projection: latest valid fact per entity, as known at time T

Current truth is a *query*, not a stored field. The projection over an append-only log is: for each entity, take the observations whose **valid-time â‰¤ T_valid** AND **system-time â‰¤ T_system**, then pick the one with the latest valid-time (tie-break on latest system-time). That single row's value is "the truth as of T." Set both T's to "now" and you get today's status; set them to a past date and you time-travel. This is slowly-changing-dimensions done right: no Type-2 row-versioning bookkeeping to maintain by hand â€” the version history *is* the log, and any point-in-time view is one query away.

### Corrections and late data: append, never edit

Dropback: "Your edits aren't sticky notes layered on top of someone else's truth. They flow through the same machinery as every other observation â€” attributed to you â€” which is why a correction you make stays put when the next vendor feed contradicts it." A correction is a *new observation* with a later system-time (and, often, a backdated valid-time), not an UPDATE to the old one. The old row stays untouched so you can still answer "what did we believe before the correction." Late-arriving data is the same move: append it with its true (earlier) valid-time and its real (later) system-time; the as-of projection slots it into the right place in history without disturbing what you believed at the time.

### Why the stored snapshot is the anti-pattern (the honest baseball example)

The USD pipeline already did the hard half right: `portal_events` is append-only and carries *both* axes â€” `event_date` (valid-time) and `observed_at` (system-time) â€” with a UNIQUE constraint for idempotent re-runs. But `players.current_status TEXT DEFAULT 'ENTERED'` is a *stored, mutable* snapshot. The moment a player goes ENTERED â†’ WITHDRAWN â†’ COMMITTED, the column overwrites and the earlier states are gone from `players`; you can no longer ask "was this player still in the portal as of June 10?" without going back to the log anyway. The column duplicates information the log already holds, can silently drift from it, and is indexed (`idx_players_status`) as if it were authoritative. The fix is not to add history columns to `players` â€” it's to *derive* status from `portal_events` and treat any `current_status` field as a disposable materialized cache, recomputable from the log at any time.

## How to apply (step-by-step)

1. **Find the mutable fact.** Name the column or field that gets overwritten as reality changes (`current_status`, `latest_grade`, `is_active`, `current_team`). That's your derivation target.

2. **Name the two axes explicitly.** Write down, in the user's domain words: valid-time = "when this was true in the world" (the source's event date), system-time = "when we learned it" (ingest timestamp). If only one timestamp exists, you can't time-travel both ways â€” flag the missing axis as a schema gap.

3. **Confirm the append-only log exists (or specify it).** The projection needs an immutable observation log keyed by entity, carrying both timestamps and the fact's value. If there isn't one, that's a `dropback-append-only-ledger` task first â€” cross-reference and stop here until it exists.

4. **Write the as-of projection.** Produce the concrete query: filter observations to `valid_time <= :as_of_valid AND system_time <= :as_of_system`, partition by entity, order by `valid_time DESC, system_time DESC`, take the first row per entity. State the default ("now/now") and how to pass a past T. This query, not the column, is the source of current truth.

5. **Re-express the stored column as a view or cache.** Replace direct reads of the mutable column with the projection at T=now. If a physical column is kept for speed, label it explicitly as a materialized cache, document that it's recomputable from the log, and define when it's refreshed (don't let callers treat it as authoritative).

6. **Define the correction / late-data path.** Specify that corrections and backfills are *appended* as new observations with their true valid-time and real system-time, attributed to the actor/source â€” never an UPDATE/DELETE of an existing row. Show the one example that matters for this domain (e.g., a vendor fixing an entry date weeks later).

7. **Add the two regression questions.** Pin down a valid-time query ("what was true as of <past date>?") and a system-time query ("what did we believe on <past date>, given only what we'd ingested by then?"). If the model can answer both, the design holds; if it can only answer "now," you've still got a stored-opinion problem.

8. **Sanity-check by trying to break reproducibility.** Pick a past decision (an old report, a graded board) and re-derive it as-of that date. If the numbers don't reproduce, some fact was stored-and-overwritten instead of derived â€” go back to step 1 for that field.

## Common failure modes

- **Storing `current_state` as a mutable column.** The single most common one (and the live one in the baseball schema). It answers "now" and annihilates "then" on the next overwrite, duplicates the log, and silently drifts from it. Derive it; keep any physical column only as a labeled, recomputable cache.

- **Conflating the two time axes.** Using one timestamp (usually ingest time) for both "when it was true" and "when we learned it." Then a late-arriving fact looks like it happened when you received it, valid-time slices are wrong, and "what did we believe then" becomes unanswerable. Keep `event_date` and `observed_at` distinct and always filter on the right one.

- **Editing facts instead of appending corrections.** UPDATE-ing or DELETE-ing an observation to "fix" it erases the prior belief and makes audits and recomputation impossible â€” and Dropback warns the edit then doesn't "stay put" against the next contradicting feed. Append a new attributed observation; let the projection prefer it.

- **Can't answer "what did we know on date X."** A model with only valid-time (no system-time) can time-travel through world-reality but not through the system's own knowledge â€” so you can't reproduce why a past decision was made on the information available *then*. Carry both axes or accept you've half-solved it.

- **Recompute cost without a materialized projection.** "Truth is a function" is right, but re-deriving every read from a huge log can be slow. The fix is a materialized/cached projection (refreshed on append, or on a schedule) that is *explicitly* derived from the log â€” not reverting to a hand-maintained mutable column. Cache the function's output; never replace the function.

- **Backfilling late data at "now" instead of its real valid-time.** Appending a retroactively-true fact with today's valid-time corrupts every as-of slice between when it was actually true and now. Append with the *true* (earlier) valid-time and the *real* (later) system-time so it lands in the right place in history.

## References

- Dropback â€” The Data Engine whitepaper, https://www.dropback.com/blog/data-engine-whitepaper, "Bitemporal Truth" (pillar 3, "Derived, Bitemporal Truth"). Key phrasings: "Truth is a function, not a fact someone typed in once"; truth recomputes "all the way back through history, automatically"; "every question is asked 'as of' some moment"; "every observation carries when we learned it on append-only storage; every fact that needs to travel through time carries the dimension it varies along."
- Worked example (honest, partial): USD baseball portal pipeline â€” `db/schema.sql` (`portal_events` carries both axes via `event_date` + `observed_at`; `players.current_status` is the stored-mutable anti-pattern) and `src/portal/db.py` (`add_portal_event`, `current_status` default).
- Sibling carved skills:
  - `dropback-append-only-ledger` â€” the immutable write discipline (never overwrite); produces the log THIS skill derives as-of truth *from*. Do that one first if no log exists.
  - `dropback-entity-resolution` â€” collapses fragmented source records into one canonical identity; supplies the stable entity key the projection partitions by.
  - `dropback-graph-native` â€” relationship-first storage with temporal validity windows; uses the same valid-time concept on edges rather than on a single entity's facts.
