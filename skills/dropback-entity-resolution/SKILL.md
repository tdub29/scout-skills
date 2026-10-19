---
name: dropback-entity-resolution
description: Design or audit an entity-resolution (record-linkage) layer that recognizes when the same real-world entity appears across different source systems under different IDs and spellings, and consolidates them into ONE canonical identity that evolves as new evidence arrives. Apply Dropback's "Universal Entity Resolution" pillar from the Data Engine whitepaper. Use this skill WHENEVER the user is reconciling, merging, deduping, or joining records that describe the same people, customers, companies, products, or accounts across two or more sources â€” even if they never say "entity resolution." Trigger on: "dedupe," "deduplication," "record linkage," "fuzzy match," "the same person shows up twice," "same player/customer across systems," "master data," "golden record," "canonical ID," "single source of truth for who," "merge these tables on name," "match records," "identity resolution," "households," "their IDs don't line up," "we have four records for Marcus," "join two datasets that share no common key," "MDM," "patient/account/vendor matching," or any time someone is about to JOIN on a name or eyeball a spreadsheet to merge duplicates. Also trigger when a data model has the same entity entering from multiple feeds (CRM + scraper + manual notes + vendor export) and the user needs a strategy to unify them without over-merging different people or under-merging spelling variants. Output is an entity-resolution design (blocking keys + match strategy + confidence threshold + corroborating attribute + canonical-ID/merge policy + new-evidence handling) OR a concrete match decision (matched/not-matched + confidence score + the reason + which attribute confirmed it). DO NOT TRIGGER FOR: append-only storage of raw observations (see dropback-append-only-ledger), time-versioning of facts (see dropback-bitemporal-truth), or relationship traversal between already-resolved entities (see dropback-graph-native).
---

# Dropback: Universal Entity Resolution

## When to use

Trigger the moment the user is trying to make scattered records agree about *who* â€” when the same real-world thing (a person, customer, company, account, product) shows up in more than one place and the IDs and spellings don't line up. Concrete cues:

- The user has the same entity in multiple feeds â€” e.g. "Marcus in the CRM, Marcus in the scraper output, Marcus in someone's notes, Marcus in the vendor export are four different records" â€” and wants one thread to pull.
- They are about to `JOIN` two datasets on a name, or eyeball a spreadsheet to delete duplicate rows by hand.
- They say dedupe, record linkage, fuzzy match, golden record, master data, canonical ID, single source of truth, "same person across systems," or "their IDs don't match."
- A pipeline ingests an entity from several sources and needs a rule for when two rows are the same entity and when they are merely similar.
- They've been bitten already: two real people collapsed into one, or one person split across two records, and they want a defensible strategy.

Don't trigger for: storing raw observations immutably (`dropback-append-only-ledger`), versioning a fact across valid-time/system-time (`dropback-bitemporal-truth`), or traversing edges between entities that are *already* resolved (`dropback-graph-native`). Those are siblings; this skill is specifically about deciding *which records are the same entity*.

## The framework

### Core thesis: identity is a living conclusion, not a given key

Fragmented sources don't agree about *who*. The same entity arrives under different surrogate IDs, different spellings, accents, nicknames, suffixes, and stale attributes. You cannot just `JOIN` on a shared key because there is no shared key â€” that's the whole problem. Entity resolution is **probabilistic record linkage**: identity is *figured out* from partial, contradictory evidence rather than read off a column. The output is **one canonical identity per real-world entity** â€” "one player, one identity, one thread to pull" â€” but the assignment is **a living conclusion that gets sharper as more evidence arrives**. The right answer can legitimately change as you learn more, so the design must let identity be *recomputed*, not frozen the day the row was inserted. The payoff is a substrate that tells the truth about *who*, so every downstream question (history, scoring, dedup counts, relationships) is asked against real entities instead of accidental duplicates.

### Role vs. permanent identity

A subtle but load-bearing distinction: the *role* an entity plays is temporary, but the *entity* is permanent. A player at School A and the same human at School B are two roles of one permanent identity; a contact at one company and the same person at their next employer are two roles of one human. Resolve to the **permanent identity** so you can "follow the human across every school/role they've ever touched and ask what you knew about them at each step." Don't let a change of role (school, employer, account) spawn a new canonical entity.

### The match ladder: deterministic key â†’ fuzzy â†’ confidence gated by a second attribute

A sound resolver runs cheapest-and-surest first, then escalates:

1. **Blocking / candidate generation.** Don't compare every record to every record (O(nÂ²)). Bucket records by a cheap key (normalized last name, first letter + soundex, ZIP, school) so you only score plausible pairs.
2. **Deterministic exact-key match.** Build a *normalized* key and treat an exact key hit as a confident match (score 100, reason `exact-key`). Normalization is where most of the win lives â€” fold accents, lowercase, strip punctuation/digits, drop generational suffixes (Jr/Sr/II/III), expand nicknames (Mikeâ†’Michael), and **sort the tokens** so "First Last" and "Last, First" collapse to the same key.
3. **Fuzzy similarity.** For records that miss the exact key, score string similarity (e.g. token-set ratio) against an explicit threshold. Token-set ratio is robust to word order and extra middle names.
4. **Gate the fuzzy match on a corroborating attribute.** A fuzzy *name* match alone is dangerous (common names) â€” require a second attribute to agree before accepting. If both records carry the attribute (school, DOB, employer, email domain, ZIP), require it to clear its own threshold; only then accept, and blend the scores (e.g. 0.7Â·name + 0.3Â·school). If the corroborating attribute is missing on one side, either fall back to name-only at a *higher* bar or leave it for human review â€” never silently accept.

### Canonical-ID and merge policy: immutable id, evolving attributes

Each resolved entity gets a **stable, immutable canonical ID** that never changes once minted. Source-specific IDs are kept as *external IDs* (a `{source: id}` map) attached to the canonical entity, so you can round-trip back to any feed. When a new record merges in, **enrich, don't clobber**: fill attributes that are currently empty, merge the external-ID map, and bump a `last_updated` stamp â€” but keep the canonical ID fixed. Track `first_seen` so you know when the entity entered. Merges and the *reason* for each merge must be recorded so resolution is auditable and reversible.

### New evidence can re-decide a match

Because identity is a living conclusion, the layer must accommodate evidence arriving later: a newly-learned DOB confirms a previously-uncertain pair; a corrected spelling turns a near-miss into a hit; a contradiction reveals an over-merge. Design for **recompute and split/merge**, not one-shot insertion. Keep enough provenance (which records, which scores, which attribute confirmed it) that a future, better match can supersede an earlier guess.

## How to apply (step-by-step)

1. **Name the entity and its grain.** State exactly what one canonical record represents (one human, not one role; one company, not one account). Decide role-vs-identity now â€” it dictates whether a school/employer change spawns a new entity (it shouldn't).
2. **Inventory the sources and their keys.** List every feed, its native ID, and which attributes it carries (name, school, DOB, email, ZIP). Identify that there is no shared key â€” that's why you're resolving.
3. **Choose the blocking key.** Pick a cheap bucket that plausible matches will share (normalized surname, ZIP, school) to avoid O(nÂ²) comparison. State it explicitly.
4. **Define the normalized match key.** Specify the normalization: de-accent, lowercase, strip punctuation/suffixes, expand nicknames, sort tokens. This is the deterministic layer â€” write it down as a function.
5. **Set the fuzzy threshold and the corroborating attribute.** Pick the similarity metric and a numeric cutoff, and name the second attribute that must agree to confirm a fuzzy name match (plus its own threshold). State the score blend.
6. **Write the canonical-ID + merge policy.** Immutable ID, external-IDs map, enrich-don't-clobber on merge, `first_seen`/`last_updated`. Decide what happens when the corroborating attribute is missing (higher name bar, or queue for review).
7. **Specify new-evidence handling.** How a later record can confirm, correct, or split a prior decision â€” and what provenance/audit trail you keep so the merge is reversible.
8. **Emit the artifact.** Produce either (a) the resolution design â€” blocking key, normalization, thresholds, corroborating attribute, canonical-ID/merge policy, new-evidence rule â€” or (b) a specific match decision: matched/not-matched, the confidence score, the human-readable reason (e.g. `fuzzy name=91 school=84`), and which attribute confirmed it.
9. **Sanity-check both directions.** Run a few known-same and known-different pairs through the design. If two different real entities collapse, your corroborating gate is too loose; if one entity stays split, your normalization or threshold is too strict.

## Worked example: the USD baseball portal pipeline

A real implementation lives in `c:\Users\TrevorWhite\Downloads\Big Projects\baseball\src\portal\`. The same player enters from public trackers, X/Twitter, 6-4-3 Portal HQ, and manual notes under different spellings and source IDs.

- **Normalization (`util.py`).** `normalize_name` de-accents (`strip_accents`/NFKD), lowercases, drops punctuation/digits, removes suffixes (`jr/sr/ii/iii/iv/v`), expands a nickname map (`mikeâ†’michael`, `zachâ†’zachary`), and merges single-letter runs so "A. J." == "AJ". `name_key` then **sorts the tokens**, so "First Last" and "Last, First" produce one stable key.
- **Match ladder (`resolve.py`).** `Resolver` builds an exact normalized-key index first; an exact key hit returns a `Candidate` with score `100.0` and reason `exact-key`. On a miss it runs `rapidfuzz.token_set_ratio` against `NAME_THRESHOLD = 88`. Crucially, **a fuzzy name match is gated by school agreement**: if both records have a school, the school must clear `SCHOOL_THRESHOLD = 80`, and the final score is blended `0.7*name + 0.3*school` with the reason recorded as `fuzzy name=NN school=MM`. No school on either side â†’ name-only with the reason flagged `(no school check)`. This is exactly "deterministic key â†’ fuzzy â†’ confidence gated by a corroborating attribute."
- **Canonical ID + merge (`db.py`).** `PlayerIndex.get_or_create` merges by `name_key` into a stable integer `player_id`; cross-source IDs live in an `external_ids` JSON map (`_merge_external_ids`). New rows **enrich without clobbering** (`_fill_missing` only sets NULL columns), and `first_seen`/`last_updated` track the evolving identity â€” the canonical ID never changes.

The pillar is general; baseball is just one instantiation. Swap "school" for DOB, email domain, or ZIP and the same ladder resolves customers, patients, or vendors.

## Common failure modes

- **Over-merging on common names.** Accepting a high name similarity with no second attribute collapses two different real entities ("J. Smith" at two schools become one player). Always gate a fuzzy name match on a corroborating attribute; if it's absent, raise the bar or send to review rather than auto-accept.
- **Under-merging on spelling drift.** Accents, nicknames, suffixes, and reordered tokens leave the same entity split across records. The fix is upstream: invest in normalization (de-accent, nickname map, suffix strip, sorted-token key) *before* you ever compare strings â€” most missed matches die here, not at the threshold.
- **Joining on a raw key that isn't shared.** Treating a source's surrogate ID (or a raw name string) as if it were a universal key. There is no shared key â€” that's the premise. Resolve first, then keep each source's ID as an *external* ID under the canonical entity.
- **Freezing identity at insert time.** Minting a canonical record once and never revisiting it, so a later, better match (new DOB, corrected spelling) can't supersede the guess. Identity is a living conclusion â€” design for recompute/split/merge and keep the provenance to do it.
- **Mutable canonical IDs / clobbering attributes.** Letting the canonical ID change on merge breaks every downstream reference; overwriting good attributes with a new feed's blanks loses information. Keep the ID immutable, enrich-don't-clobber, and merge external-ID maps additively.
- **Resolving to a role instead of the permanent entity.** Spawning a new entity every time someone changes school/employer/account, so you can't follow the human across roles. Resolve to the permanent identity; treat role/affiliation as an attribute that changes over time, not as the identity itself.
- **No audit / why-merged trail.** Storing the merged result without the score, the threshold, or which attribute confirmed it. When a merge is later questioned (or needs unwinding), you have nothing to reason from. Record matched/not-matched, the confidence, and the reason string on every decision.

## References

- Source: Dropback â€” *The Data Engine* whitepaper, https://www.dropback.com/blog/data-engine-whitepaper, "Universal Entity Resolution" (probabilistic record linkage; "one player, one identity, one thread to pull"; "a living conclusion that gets sharper as more evidence arrives"; "tell the truth about who").
- Sibling carved skills:
  - `dropback-append-only-ledger` â€” never overwrites raw observations; preserves the history that lets a resolution decision be recomputed.
  - `dropback-bitemporal-truth` â€” versions facts across valid-time/system-time; truth recomputes when matching improves.
  - `dropback-graph-native` â€” treats relationships as first-class edges; runs *after* identities are resolved, traversing connections between canonical entities.
- Worked example (real implementation): `c:\Users\TrevorWhite\Downloads\Big Projects\baseball\src\portal\resolve.py`, `util.py`, `db.py`.
