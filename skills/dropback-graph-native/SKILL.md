---
name: dropback-graph-native
description: Apply Dropback's "Graph-Native Architecture" pillar (from The Data Engine whitepaper) to model a domain as nodes and temporal edges, decide which relationships deserve to be first-class data structures, write traversal-style queries, and rule go/no-go on whether graph-native beats relational joins or a spreadsheet. Use this skill whenever the user is asking a relationship question their current schema makes hard â€” "connections between X and Y," "everyone who moved from A to B," "staff-to-player paths," "which high schools feed which programs," "shared-coach networks," "transfer lineage over time," "who was on the roster that week," or any multi-hop / network / traversal question. Trigger even when the user does not say "graph": phrases like "I keep adding join tables for every new link," "this is a forest of nested JOINs," "I have a column for from_school and to_school but can't ask follow-the-chain questions," "I'm tracking relationships in a spreadsheet with one row per pair," "I need a column for every possible connection," or "how do I model movement/lineage over time" all qualify. Also trigger when reviewing a flat or relational model to audit whether it is hiding relationships behind foreign keys that cannot be cheaply traversed. Output is a node/edge model (or an audit of a flat one): a list of node types, first-class edge types with direction/cardinality/time-validity, the traversal queries the model unlocks, and an explicit go/no-go recommendation on graph-native vs. joins vs. spreadsheet. DO NOT TRIGGER FOR canonical identity/dedup of entities (use dropback-entity-resolution), for the immutability/event-log mechanics of changes (use dropback-append-only-ledger), or for the valid-time vs. system-time semantics of "as of when" (use dropback-bitemporal-truth) â€” this skill assumes those and focuses only on the shape of the relationships.
---

# Dropback: Graph-Native Architecture

## When to use

Trigger when the user is trying to force a relationship question through a structure that fights it â€” a wall of nested JOINs, a join table they keep hand-migrating, a `from_school`/`to_school` column pair they can't follow past one hop, or a spreadsheet with one row per pairing. The Dropback framing: "Relationships are not columns. The interesting questions are rarely about one row." Concrete cues:

- The user asks for "connections between X and Y," "the network of," "paths from," "everyone who moved from / to," "who is linked to," or "shared ___ across."
- The question is multi-hop: "high schools that sent a player to a current conference rival who later entered the portal" needs 3+ relationship traversals.
- The schema adds a new join table or a new wide column every time a new *kind* of link appears.
- The user is asking a relationship "as of" a past date and the model has no place to store when the link was true.
- Lineage / movement / membership-over-time questions: roster history, coaching trees, transfer chains, conference realignment.
- The user is reviewing a flat model and asks "is this the right shape?" â€” audit it for buried relationships.

Don't trigger for: assigning canonical IDs to messy duplicate entities (that's `dropback-entity-resolution` â€” it supplies the node identities this skill connects); the immutability/event-sourcing mechanics of recording changes (`dropback-append-only-ledger`); or the precise valid-time vs. system-time semantics behind "as of when" (`dropback-bitemporal-truth`). This skill assumes canonical nodes and a notion of time-validity already exist; it decides the *shape of the edges* between them.

## The framework

### Core thesis: a relationship is not a column

The relational model was optimized for 1970s storage, not for relationship-heavy questions. When relationships live as foreign-key columns or bespoke join tables, every new *kind* of relationship demands a schema migration, and every interesting question â€” which are "rarely about one row" â€” turns into a chain of JOINs that gets exponentially more expensive per hop. Graph-native flips the primitive: model the domain as **vertices (nodes) and edges**, and treat **every relationship as a first-class edge with its own validity window, so traversing them is a query â€” not a migration.** The leverage is that new link types and multi-hop questions become *data*, not *DDL*. The cost is real: graphs are overkill for single-hop lookups and add operational complexity, so the skill must also know when *not* to reach for one.

### Nodes: the things

Nodes are the stable entities in the domain â€” the nouns. In the baseball pipeline: a *player*, a *school*, a *game*, a *staff member*, a *conference*, a *summer team*. A node should be something you'd want to ask questions *about* and *connect to other things*. Node identity must be canonical (one node per real-world thing across all sources) â€” that canonicalization is `dropback-entity-resolution`'s job; this skill connects nodes it assumes are already resolved.

### Edges: the relationships, reified

An edge is a relationship between two nodes, promoted to a first-class object with its own type, direction, cardinality, and â€” critically â€” **time-validity**. The key move is **reifying the relationship**: a transfer is not a `to_school` column on the player row; it is its own `TRANSFERRED` edge from playerâ†’school with attributes (entry date, commit date, source, status). Reified edges can carry data, be queried as a set, and be reconstructed historically. The whitepaper's litmus: if a "relationship" needs attributes, a lifecycle, or a time window, it is an entity in its own right, not a column.

### Time-validity on every edge

Every edge carries a validity window so you can ask the relationship "as of" any point in time. "Boise State was Mountain West in 2023 and Pac-12 in 2026" is two edges with different windows, not an overwritten field. "Who was on the roster *that week*?" filters team-membership edges by window. This skill *uses* time-validity to shape edges; the formal valid-time/system-time mechanics belong to `dropback-bitemporal-truth`, and the rule that edge facts are appended-never-overwritten belongs to `dropback-append-only-ledger`.

### Traversal: the questions you can finally ask

The payoff is multi-hop queries that are a single traversal instead of a JOIN explosion. Dropback's worked example: **"every high school that has sent a player to a current conference rival who later entered the portal."** That is four hops â€” high school â†’(attended)â†’ player â†’(committed-to)â†’ school â†’(member-of, *as-of-now*)â†’ conference, intersected with player â†’(entered)â†’ portal â€” all crossing temporal boundaries. In a flat model each hop is a JOIN and the temporal filters multiply; as a graph it is a path pattern. Other traversals the same model unlocks: coaching trees (staffâ†’staff via shared programs), feeder pipelines (high schoolâ†’program over years), shared-network paths between any two people.

### When graph-native pays â€” and when it doesn't

Graph-native wins when: relationships are many *kinds* and growing; questions are multi-hop or path-shaped; relationships carry attributes and time; or you need to reconstruct the network historically. It loses when: you only ever do single-hop lookups (a foreign key + JOIN is simpler and faster); the relationship set is small, fixed, and attribute-free; or the team can't operate a graph store. You do **not** need a dedicated graph database to be graph-native â€” a relational schema with an explicit, reified, time-stamped edge table (like `portal_events`) is a graph model expressed in SQL. Recommend the lightest structure that makes the target traversals cheap.

## How to apply (step-by-step)

1. **List the questions first, not the tables.** Write the actual relationship/traversal questions the user wants to answer ("which high schools feed our rivals," "who was on the roster as of last June"). The questions decide which relationships must be first-class.

2. **Extract the node types.** From the questions, pull the nouns you ask *about* and *connect* â€” player, school, game, staff, conference. Confirm each has (or needs) a canonical identity; if identities are fuzzy, flag `dropback-entity-resolution` before proceeding.

3. **Extract the edge types.** For each relationship between nodes, name it as a verb: `ATTENDED`, `TRANSFERRED`/`ENTERED_PORTAL`, `COMMITTED_TO`, `COACHED_AT`, `MEMBER_OF`, `PLAYED_IN`. One edge type per kind of link.

4. **For every edge, decide direction, cardinality, and time-validity.** Direction (playerâ†’school, not symmetric), cardinality (a player has many portal events; a game has exactly two teams), and a validity window (when was this link true?). An edge missing a time window can't answer "as of when" â€” add one unless the link is genuinely timeless.

5. **Decide which relationships to reify as their own entity.** If a relationship has attributes, a lifecycle, or multiple instances over time (a transfer has entry/commit dates, a source, a status that changes), promote it from a column to a first-class edge-with-data. A bare, attribute-free, one-time link can stay a foreign key.

6. **Map the existing flat/relational model onto the node/edge model.** Translate each table and FK: which are nodes, which are edges, which are buried relationships hiding in columns. (Baseball example below â€” `players.from_school`/`to_school` are *frozen* edges; `portal_events` is already the *correct* time-stamped edge table.)

7. **Write the target traversals against the model.** Express each question from step 1 as a path pattern. Confirm the model supports it in one traversal; if a question still requires a fan-out of JOINs, a needed edge type is missing â€” go back to step 3.

8. **Give the go/no-go.** State explicitly: graph-native (dedicated graph DB), graph-model-in-SQL (reified edge tables), or stay relational/spreadsheet. Justify by hop-count, number of growing relationship kinds, attribute/time needs, and operational cost. Recommend the lightest option that makes the target traversals cheap.

## Worked example: the USD portal schema, read graph-natively

The pipeline's `db/schema.sql` is relational, but it is *already* a graph model in places â€” and hiding relationships in others.

- **Nodes:** `players` (canonical human, stable across sources via `external_ids`), and the implicit `school`, `staff`, `summer_team`, `game`, `conference` entities currently living as text columns.
- **The good edge (already reified):** `portal_events` is a textbook time-stamped edge: `player_id` â†’(`event_type` ENTERED/WITHDRAWN/COMMITTED)â†’ school, with `event_date` (when the link became true) and `observed_at` (when we saw it). It is append-only and idempotent â€” exactly "every relationship change is an immutable edge fact." This is what lets you ask "all players who entered the portal from school A in the last year."
- **The buried relationships (columns that should be edges):** `players.from_school` and `players.to_school` are a *flattened, point-in-time snapshot* of relationships that actually live in `portal_events`. They answer "where now?" cheaply but can't be traversed historically or multi-hop. `summer_team`, `division`, and the `scout_notes` JSON similarly collapse what are really playerâ†”org and staffâ†”player edges into cells.
- **Edges to add to support traversal:** `ATTENDED(playerâ†’high_school, window)`, `MEMBER_OF(schoolâ†’conference, window)` â€” needed because conference membership changes over seasons â€” and `COACHED_AT(staffâ†’school, window)`. With these, Dropback's "every high school that sent a player to a current conference rival who later entered the portal" becomes one path pattern instead of an unwriteable JOIN.
- **Go/no-go for this project:** stay relational, but lean into the **graph-model-in-SQL** pattern â€” keep `portal_events` as the source of truth for playerâ†”school over time, demote `from_school`/`to_school` to derived convenience views, and add explicit edge tables for high-school, conference, and staff links. A dedicated graph DB is not warranted yet (single-school scout tool, modest data), but the *modeling discipline* is what unlocks the relationship questions a spreadsheet never could.

## Common failure modes

- **Relationships buried as foreign keys you can't traverse.** A `to_school` column answers "where now?" but the moment you ask "follow the chain" or "as of last season," it's a dead end. If a question is multi-hop, the link must be a first-class edge, not a column on the node.

- **Edges without time-validity.** An edge with no validity window can't answer "as of when," so conference realignment, roster-that-week, and lineage questions become impossible or wrong. Every non-timeless edge needs a window â€” defer the formal valid-time semantics to `dropback-bitemporal-truth`, but never ship a temporal relationship as a bare overwriteable field.

- **Not reifying the relationship.** Treating a transfer, a commitment, or a coaching stint as an attribute on a node instead of its own entity. The relationship has dates, a source, a status, and multiple instances over time â€” that is an entity, and squashing it into a column destroys the very history the user wants to query.

- **Over-graphing simple lookups.** Reaching for a graph DB when every real question is single-hop ("what's this player's position?"). A foreign key plus a JOIN is simpler, faster, and cheaper to operate; graph machinery here is pure overhead. Graph-native is for relationship-shaped questions, not for everything with a link.

- **Ignoring edge direction and cardinality.** Modeling playerâ†’school as if it were symmetric, or letting a game point to "many" teams when it has exactly two. Wrong direction breaks traversals; wrong cardinality corrupts counts and lets bad data in. Pin both for every edge.

- **One join table per relationship, hand-migrated forever.** Adding a bespoke table + migration for each new *kind* of link is the relational anti-pattern the whitepaper targets: it makes new relationships DDL instead of data. Prefer a uniform, reified edge model where a new link type is a new row, not a new schema.

- **Confusing the node-identity problem with the edge-shape problem.** Trying to fix duplicate/fragmented entities by changing the graph shape. Canonical identity is upstream â€” resolve nodes with `dropback-entity-resolution` first, then connect the clean nodes here.

## References

- Dropback â€” The Data Engine whitepaper, https://www.dropback.com/blog/data-engine-whitepaper, "Graph-Native Architecture." Key phrasing: "Relationships are not columns. The interesting questions are rarely about one row"; "every relationship as a first-class edge with its own validity window, so traversing them is a query â€” not a migration"; worked traversal "every high school that has sent a player to a current conference rival who later entered the portal."
- Worked example schema: `c:\Users\TrevorWhite\Downloads\Big Projects\baseball\db\schema.sql` (`players`, `portal_events`, `from_school`/`to_school`, `external_ids`, `roster_info`, `call_assignments`).
- Sibling carved skills:
  - `dropback-entity-resolution` â€” supplies the canonical node identities this skill connects edges between; resolve nodes first.
  - `dropback-append-only-ledger` â€” the rule that every edge fact is immutable and appended, never overwritten (cf. `portal_events`).
  - `dropback-bitemporal-truth` â€” the valid-time vs. system-time semantics behind the edge validity windows this skill places.
