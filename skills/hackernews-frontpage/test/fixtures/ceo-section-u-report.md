# Plan: cache profile summaries in one process

## Measured problem and accepted scope
The existing profile-summary service has one active process. A one-week trace
shows repeated reads of about 900 hot keys: DB CPU is 70%, with read p95 120 ms.
Add a process-local LRU wrapper to the existing repository. Acceptance targets
are at least 60% cache hits, DB CPU below 50%, and read p95 below 60 ms, with the
existing error-rate and correctness SLOs unchanged. This is an internal backend
change with no UI, API, schema, pricing, or developer onboarding change.

## Existing contracts retained
- All reads and writes use this repository in the same process; there are no
  external DB writers. Multi-process operation remains unsupported and startup
  rejects that configuration while caching is enabled.
- Authentication and authorization run before repository access. Keys encode
  the authenticated tenant ID and validated profile ID without ambiguity.
  Values are immutable profile-summary DTOs; secrets and cache keys are never
  logged. Cached results cannot bypass authorization.
- The existing LRU adapter supports 1000 entries, a 16 MiB byte cap, and a
  30-second TTL. Recorded hot data fits those limits. Absent records use a
  distinct sentinel with a 10-second TTL; undefined means a cache miss.
- Cache operations are synchronous and atomic in the single JS event loop.
  On any cache failure the existing adapter bypasses the cache until an empty
  cache is reinitialized; repository errors keep the current typed API error
  mapping. The existing per-key
  single-flight wrapper coalesces simultaneous misses and releases on failure.
- A read already in progress when a write commits may return its earlier DB
  snapshot to that caller. Every read begun after that write completes must
  observe the committed version. TTL expiry is not a substitute for this rule.

## Proposed wrapper integration
Keep the current read-through repository interface and shared adapters. These
are the complete new read/write ordering rules; no additional version checks or
coordination between a cache fill and a write are proposed:

```javascript
async function readProfile(key) {
  const cached = cache.get(key);
  if (cached !== undefined) return cached;
  const value = await repository.read(key);
  cache.set(key, value);
  return value;
}

async function writeProfile(key, update) {
  const saved = await repository.write(key, update);
  cache.delete(key);
  return saved;
}
```

## Verification and rollout
Existing repository contract tests cover tenant isolation, key validation,
absence, DB failures, and authorization. New wrapper tests cover hit/miss,
eviction and byte limits, TTL, adapter-failure fallback, successful-write
invalidation, failed-write preservation, and concurrent-miss coalescing.
The rollout uses the existing runtime feature flag: enable for 10% of keys,
then 50%, then all keys after one healthy hour at each stage. Monitor hit/miss,
eviction, cache bytes, fallback errors, DB CPU, and read p95 without raw IDs.
On error-rate or latency regression, disable the flag immediately; both reads
and writes bypass the cache while disabled, and enabling creates an empty cache.
Cold starts remain within the existing DB capacity. The service owner monitors
the rollout and records the results against the acceptance targets.

## Out of scope
Distributed caching, cross-process coherence, prewarming, changing consistency
semantics, or adding new product surfaces. The repository interface preserves a
future replacement path without introducing a general cache framework now.

---

## CEO REVIEW â€” HOLD SCOPE

*Mode: HOLD SCOPE. Scope is accepted as stated; review focuses on correctness,
security, observability, and deployment risk. No expansions surfaced.*

### Step 0 â€” Scope Confirmation

**0A. Premise Challenge**

The problem is measured, not hypothetical. A one-week trace showing 900 hot keys,
70% DB CPU, and p95 120 ms is solid evidence. The acceptance targets (â‰¥60% hits,
DB CPU <50%, p95 <60 ms) are concrete and verifiable. The direct path â€” process-
local LRU wrapping the existing repository â€” is correct. Doing nothing leaves the
DB pressure growing as the hot-key set grows.

**0B. Existing Code Leverage**

- The existing LRU adapter is reused without modification.
- The existing single-flight wrapper is reused.
- The existing runtime feature flag is the rollout mechanism.
- The existing repository interface is preserved unchanged.

Nothing is being rebuilt that already exists. The wrapper is purely additive.

**0C. Dream State Mapping**

```
CURRENT STATE              THIS PLAN                  12-MONTH IDEAL
DB CPU 70%        --->     Process-local LRU     --->  DB CPU <50%
p95 120 ms                 wrapper               --->  p95 <60 ms
900 repeated reads         Feature-flag rollout  --->  â‰¥60% cache hits
                           10% â†’ 50% â†’ 100%            Stable operation
                                                        Distributed cache
                                                        as next step if
                                                        scale requires
```

The 12-month ideal is essentially this plan's success state. The plan explicitly
defers distributed caching, which is the correct next evolution if process-count
scales.

**0C-bis. Implementation Approaches (auto-decided)**

Three approaches evaluated:

```
APPROACH A: Inline cache logic in repository methods
  Summary: Add cache calls directly inside existing read/write methods.
  Effort:  S
  Risk:    Low
  Pros:    Fewest files; no new layer
  Cons:    Harder to test independently; toggle coupling; harder to replace
  Reuses:  Existing adapter

APPROACH B: Wrapper layer (the plan's approach) [SELECTED]
  Summary: Thin wrapper module owns cache interaction; repository unchanged.
  Effort:  S
  Risk:    Low
  Pros:    Independently testable; clean separation; future-replaceable
  Cons:    One extra layer (trivial in practice)
  Reuses:  Existing adapter, single-flight, feature flag

APPROACH C: External cache (Redis)
  Summary: Move caching to Redis for cross-process coherence.
  Effort:  XL
  Risk:    High
  Pros:    Cross-process safe
  Cons:    Out of scope; network latency; cross-process coherence complexity
  Reuses:  None of the existing infrastructure
```

**RECOMMENDATION: Approach B** â€” matches "engineered enough" preference: clean
separation, independently testable, preserves future replacement path. The wrapper
is thin enough that the extra layer costs nothing. Auto-decided: proceed with the
plan's approach.

**0D. HOLD SCOPE Analysis**

1. *Complexity check:* The plan touches approximately 1 new module (the wrapper)
   and 1 new test file. No new services or classes beyond the wrapper. No
   complexity smell.
2. *Minimum set:* The plan is already scoped to wrapper + tests + rollout
   monitoring. Nothing extraneous.
3. *Stated invariants:* The ordering rule ("every read begun after write completes
   must observe the committed version") is a hard requirement. Several sections
   below check the implementation against it.

**0E. Temporal Interrogation**

```
HOUR 1 (foundations):   What is the exact cache key format? The plan asserts
                         "without ambiguity" but doesn't show the format.
                         Implementer needs to specify and document it.

HOUR 2-3 (core logic):  What happens when cache.delete throws during a
                         successful write? The code lets the exception
                         propagate, misleading the caller. Needs handling.

HOUR 4-5 (integration): The in-flight single-flight read can call cache.set
                         AFTER a concurrent write's cache.delete, re-populating
                         the cache with stale data. This violates the ordering
                         invariant. Needs a guard before cache.set.

HOUR 6+ (tests/polish): The rollout "healthy hour" criterion is qualitative.
                         What numeric thresholds govern advancement?
                         What clock mocking strategy handles TTL tests?
```

---

### Section 1: Architecture Review

**System architecture:**

```
  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
  â”‚              Profile-Summary Service Process     â”‚
  â”‚                                                 â”‚
  â”‚  Caller â”€â”€â–¶ AuthZ/AuthN â”€â”€â–¶ CacheWrapper        â”‚
  â”‚                                â”œâ”€â”€ LRU Adapter  â”‚
  â”‚                                â”‚   (1000 keys,  â”‚
  â”‚                                â”‚   16 MiB, 30s) â”‚
  â”‚                                â”‚                â”‚
  â”‚                                â”‚ miss           â”‚
  â”‚                                â–¼                â”‚
  â”‚                         SingleFlight            â”‚
  â”‚                                â”‚                â”‚
  â”‚                                â–¼                â”‚
  â”‚                         Repository â”€â”€â–¶ Database â”‚
  â”‚                                                 â”‚
  â”‚  Startup guard: rejects multi-process config    â”‚
  â”‚  Feature flag: bypasses wrapper when disabled   â”‚
  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜

  Coupling delta: CacheWrapper is a new dependency on top of Repository.
  No other coupling changes.
```

**Data flow â€” readProfile (all four paths):**

```
  key â”€â”€â–¶ cache.get(key)
            â”‚
            â”œâ”€ HIT  â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¶ return value  [HAPPY]
            â”‚
            â”œâ”€ FAIL â”€â”€â–¶ adapter bypass â†’ treat as miss [ERROR â†’ bypass]
            â”‚
            â””â”€ MISS â”€â”€â–¶ await repository.read(key)
                              â”‚
                              â”œâ”€ ERROR â”€â”€â–¶ propagate; sf releases     [ERROR]
                              â”‚
                              â””â”€ OK â”€â”€â–¶ cache.set(key, value) â”€â”€â–¶ return value
                                           â”‚
                                           â””â”€ FAIL â”€â”€â–¶ bypass; return value anyway
```

**Data flow â€” writeProfile (all four paths):**

```
  key, update â”€â”€â–¶ await repository.write(key, update)
                          â”‚
                          â”œâ”€ ERROR â”€â”€â–¶ cache NOT modified; propagate  [ERROR]
                          â”‚
                          â””â”€ OK â”€â”€â–¶ cache.delete(key) â”€â”€â–¶ return saved
                                           â”‚
                                           â””â”€ FAIL â”€â”€â–¶ exception propagates!
                                                        caller sees write failure
                                                        even though write succeeded
                                                        â† GAP (see Finding 2)
```

**State machine â€” LRU adapter:**

```
  [ACTIVE] â”€â”€â–¶ cache.get/set/delete â”€â”€â–¶ [ACTIVE]
     â”‚
     â””â”€ adapter failure â”€â”€â–¶ [BYPASS] â”€â”€â–¶ empty cache reinit â”€â”€â–¶ [ACTIVE]
                                â”‚
                                â””â”€ feature flag off â”€â”€â–¶ [DISABLED]
  [DISABLED] â”€â”€â–¶ flag on â”€â”€â–¶ [ACTIVE] (empty cache)
```

**CRITICAL FINDING 1: Post-write stale cache re-population**

The proposed code has a correctness gap in the concurrent read-during-write
scenario. The single-threaded JS event loop does not prevent this interleaving:

```
TIMELINE    readProfile(k)              writeProfile(k)      Cache[k]
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
T1          cache.get(k) â†’ miss         â€”                    undefined
T2          sf: await repo.read(k)      â€”                    undefined
T3          [awaiting at yield point]   repo.write resolves  v0 (old)
T4          [awaiting]                  cache.delete(k)      undefined âœ“
T5          repo.read returns v0        return saved         undefined
T6          cache.set(k, v0)  â† STALE  â€”                    v0 (BAD!)
T7          return v0                   â€”                    v0 (BAD!)
```

After T4 the cache correctly reflects the new write. At T6, the in-flight read
re-populates the cache with the pre-write snapshot. Reads begun after T7 (after
the write completes) will get v0 from cache until TTL expiry (up to 30 seconds).
This violates the invariant: "every read begun after that write completes must
observe the committed version."

**Recommended fix (auto-decided):** Add a re-check guard before cache.set in the
read path. Because no await occurs between the re-check and cache.set (single JS
event loop), this is safe:

```javascript
async function readProfile(key) {
  const cached = cache.get(key);
  if (cached !== undefined) return cached;
  const value = await repository.read(key);
  // Guard: only cache if write did not invalidate the key during our read
  if (cache.get(key) === undefined) {
    cache.set(key, value);
  }
  return value;
}
```

This requires that the absent-record sentinel is a distinct non-undefined value
(confirmed by the plan: "undefined means a cache miss"). When the write's
cache.delete ran at T4, cache.get(k) at T6 returns undefined â†’ guard fires â†’ we
do not re-populate. The read still returns v0 (which is allowed per the invariant
for reads in-flight during the write). Reads begun after the write see a miss and
fetch the committed version from DB.

**Single points of failure:**
- Cache adapter: covered by bypass fallback.
- DB: covered by existing repository error handling.
- Feature flag: disabling bypasses cache entirely; no SPOF in the flag path.

**Rollback posture:** Flag flip. Seconds. Both read and write bypass the cache
when disabled. Enabling creates an empty cache (no stale data on re-enable).

**Production failure scenario:**
- Cache adapter crashes mid-operation: bypass mode activates; DB load spikes
  temporarily to pre-cache levels. Not a service outage, but a load event.
- DB timeout during a miss: repository error propagates; single-flight releases;
  no cache poisoning (the failed read does not call cache.set).

*Section 1 findings: 1 CRITICAL GAP (post-write stale re-population).*

---

### Section 2: Error & Rescue Map

**Error/Rescue Registry:**

```
METHOD/CODEPATH            | WHAT CAN GO WRONG              | EXCEPTION CLASS
---------------------------|--------------------------------|-------------------
readProfile(key)           | cache.get adapter failure      | CacheAdapterError
                           | repository.read typed failure  | RepositoryError
                           | cache.set adapter failure      | CacheAdapterError
writeProfile(key, update)  | repository.write typed failure | RepositoryError
                           | cache.delete adapter failure   | CacheAdapterError â† GAP

EXCEPTION CLASS              | RESCUED? | RESCUE ACTION                | USER SEES
-----------------------------|----------|------------------------------|------------------
CacheAdapterError (get)      | Y        | Bypass; treat as miss        | Transparent
RepositoryError (read)       | Y        | Propagate typed error        | Typed API error
CacheAdapterError (set)      | Y        | Bypass; return value         | Transparent
RepositoryError (write)      | Y        | Propagate typed error        | Typed API error
CacheAdapterError (delete)   | N â† GAP  | None â€” exception propagates  | Spurious write
                             |          |                              | failure (BAD)
```

**CRITICAL FINDING 2: cache.delete failure exposes a successful write as failed**

In the proposed writeProfile:
```javascript
const saved = await repository.write(key, update);
cache.delete(key);   // if this throws, caller sees write failure
return saved;
```

If the LRU adapter's delete operation throws, the exception bubbles out of
`writeProfile`. The write succeeded (data is in the DB) but the caller receives
an error. This breaks the typed API contract and may trigger spurious retries,
causing double-writes.

**Recommended fix (auto-decided):** Wrap cache.delete in a try/catch. Cache
failure in the delete path is non-fatal â€” the adapter's bypass mechanism will
handle ongoing degradation, and the next read will miss (fetching the fresh DB
value after TTL or on the next miss):

```javascript
async function writeProfile(key, update) {
  const saved = await repository.write(key, update);
  try {
    cache.delete(key);
  } catch {
    // Adapter handles bypass; write already committed to DB
  }
  return saved;
}
```

*Section 2 findings: 1 CRITICAL GAP (cache.delete failure during write).*

---

### Section 3: Security & Threat Model

**Attack surface expansion:** None. Process-local in-memory cache has no network
surface. No new endpoints, no new parameters, no new file paths.

**Authorization:** AuthZ runs before repository access. Cached values are DTOs
scoped by the key encoding. Cached results cannot bypass authorization.

**Cross-tenant isolation:** Cache keys encode tenant ID + profile ID. A tenant A
key cannot collide with tenant B unless the key construction is ambiguous.

**FINDING 3 (documentation): Key format not specified**

The plan asserts keys are "without ambiguity" but does not document the format.
For example, if the key is `${tenantId}:${profileId}` and tenant IDs can contain
`:`, collisions are possible and cross-tenant data could leak.

Threat: Low likelihood (internal service, key construction is controlled).
Impact: High (cross-tenant data leakage if collision occurs).

**Recommended fix (auto-decided):** Document the exact key format in the plan and
in a code comment. The format must be collision-resistant (e.g., delimiter
escaping, URL encoding, or a structured separator that tenant/profile IDs cannot
contain).

**PII in cache:** Profile summary DTOs are already in application memory. The
cache holds the same data already in the running process â€” no additional PII
exposure beyond what the repository already holds. Correct to avoid logging raw
IDs.

**Secrets:** No new secrets. Existing env-var patterns unchanged.

**Dependency risk:** No new npm packages. Existing LRU adapter reused.

**Injection vectors:** Cache keys are constructed internally from authenticated,
validated IDs. No user-supplied raw strings reach cache key construction.

*Section 3 findings: 1 WARNING (key format documentation).*

---

### Section 4: Data Flow & Interaction Edge Cases

**This is a pure backend change. No user-visible interactions exist. The UX edge
case table is N/A.**

**Data flow diagram â€” full shadow paths:**

```
  readProfile(key):

  INPUT â”€â”€â–¶ [key null?]     â”€â”€â–¶ validated upstream (plan states this)
             â”‚
             â–¼
           cache.get(key)
             â”‚
             â”œâ”€ HIT        â”€â”€â–¶ return value                  [OK]
             â”‚
             â”œâ”€ FAIL       â”€â”€â–¶ bypass mode; proceed as miss  [OK]
             â”‚
             â””â”€ MISS (undefined)
                  â”‚
                  â–¼
             [await repo.read(key)] â† yield point; writes can run here
                  â”‚
                  â”œâ”€ ERROR   â”€â”€â–¶ propagate; sf releases      [OK]
                  â”‚
                  â””â”€ OK: value
                       â”‚
                       â–¼
                  [cache.get(key) === undefined?]   â† ADDED GUARD (Finding 1)
                       â”‚
                       â”œâ”€ YES (key was deleted by write) â”€â”€â–¶ skip set [OK]
                       â”‚
                       â””â”€ NO  â”€â”€â–¶ cache.set(key, value)
                                        â”‚
                                        â”œâ”€ FAIL â”€â”€â–¶ bypass; return value [OK]
                                        â””â”€ OK   â”€â”€â–¶ return value         [OK]
```

**Async ordering â€” read-write interleaving (the critical case):**

With the guard added (Finding 1), the race is closed:

```
T1: readProfile miss â†’ sf: await repo.read
T2: writeProfile â†’ repo.write completes â†’ cache.delete(k)  [cache: undefined]
T3: readProfile resumes, value = v0
T4: guard: cache.get(k) === undefined â†’ true â†’ skip cache.set  âœ“
T5: readProfile returns v0 (allowed: read was in-flight during write)
T6: new readProfile â†’ cache miss â†’ repo.read â†’ gets committed version âœ“
```

Invariant satisfied: reads begun after T2 (write completes) fetch from DB and
get the committed version.

**Concurrent miss coalescing + write interleaving:**

```
T1: read1(k) â†’ miss â†’ sf: await repo.read
T2: read2(k) â†’ sf coalesces with read1
T3: write(k) â†’ repo.write completes â†’ cache.delete(k)
T4: read1 resumes â†’ guard: cache.get(k) === undefined â†’ skip cache.set
T5: sf releases â†’ read1 returns v0; read2 returns v0 (both in-flight during write)
T6: read3(k) â†’ cache miss â†’ repo.read â†’ committed version âœ“
```

The guard correctly handles the coalesced case too, because the sf coalescence
means only one cache.set attempt occurs (for the primary flight) â€” and the guard
blocks it if the key was deleted.

**Absent record path:**

```
T1: readProfile(k) â†’ miss â†’ repo.read(k) â†’ returns absent-sentinel
T2: guard: cache.get(k) === undefined â†’ true (sentinel not yet set) â†’ cache.set(k, sentinel) with 10s TTL
T3: subsequent reads within 10s â†’ HIT â†’ return sentinel quickly
```

Ensure the absent-sentinel is a distinct non-undefined value (confirmed by plan).

*Section 4 findings: 0 new gaps (Findings 1 and 2 from Sections 1 and 2 cover
the identified issues here).*

---

### Section 5: Code Quality Review

**Organization:** Single wrapper module; clean separation from repository.
Appropriate pattern, consistent with existing adapter layer.

**DRY:** No duplication. Cache logic exists only in the wrapper. Repository
unchanged.

**Naming:** `readProfile`, `writeProfile` â€” imperative, domain-aligned. Correct.

**Error handling patterns:** Two gaps identified (Findings 1 and 2 above). The
wrapper code as proposed does not handle either.

**Missing edge cases in the proposed implementation:**

1. Post-write stale re-population (Finding 1 â€” CRITICAL).
2. cache.delete failure during successful write (Finding 2 â€” CRITICAL).
3. `undefined` value guard: the plan relies on `cache.get(key) === undefined`
   as the miss sentinel. If the repository ever returns `undefined` as a
   legitimate value (not the absent-sentinel), the hit/miss detection breaks.
   The plan says values are "immutable profile-summary DTOs" and absent records
   use "a distinct sentinel" â€” this constraint must be enforced by the repository
   layer and documented as an invariant the wrapper depends on.

**Over-engineering check:** The wrapper is appropriately thin. No unnecessary
abstractions.

**Under-engineering check:** The two critical gaps (Findings 1 and 2) represent
under-engineering â€” not handling known edge cases of async + cache interactions.

**Cyclomatic complexity:** readProfile: 1 branch. writeProfile: 0 branches.
Complexity is minimal and appropriate.

*Section 5 findings: 0 new (existing findings from Sections 1-2 cover the gaps).*

---

### Section 6: Test Review

**New codepaths introduced:**

```
NEW DATA FLOWS:
  1. Cache hit â€” readProfile returns cached value without DB call
  2. Cache miss â€” readProfile reads from DB and populates cache
  3. Absent record cached â€” sentinel returned and cached with 10s TTL
  4. Absent record expired â€” TTL expiry triggers re-fetch
  5. Cache failure read â€” adapter fails, bypass, DB read proceeds
  6. Cache failure write â€” adapter delete fails, write still succeeds (after fix)
  7. Successful-write invalidation â€” writeProfile writes then deletes cache key
  8. Failed-write preservation â€” write fails, cache NOT modified
  9. Concurrent-miss coalescing â€” single-flight prevents duplicate DB reads
  10. Eviction by count â€” cache exceeds 1000 entries â†’ LRU eviction
  11. Eviction by bytes â€” cache exceeds 16 MiB â†’ LRU eviction
  12. TTL expiry (hot key) â€” cached value expires after 30s
  13. TTL expiry (sentinel) â€” absent sentinel expires after 10s
  14. Feature flag disabled â€” all reads/writes bypass cache
  15. Post-write stale guard â€” concurrent write during in-flight read (FINDING 1)

NEW ERROR/RESCUE PATHS:
  - cache.get failure â†’ bypass mode (test: adapter mock throws â†’ bypass activated)
  - cache.set failure â†’ bypass; value still returned
  - cache.delete failure â†’ caught; write return value unaffected (after fix)
  - repository.read failure â†’ propagate; single-flight releases cleanly
  - repository.write failure â†’ propagate; cache unmodified
```

**Per-codepath test assessment:**

| Codepath | Exists in plan? | Missing test |
|----------|-----------------|--------------|
| Cache hit | Y | â€” |
| Cache miss | Y | â€” |
| Absent record | Y | â€” |
| Adapter failure fallback | Y | â€” |
| Write invalidation | Y | â€” |
| Failed-write preservation | Y | â€” |
| Concurrent miss coalescing | Y | â€” |
| Eviction (count + bytes) | Y | â€” |
| TTL expiry | Y | â€” |
| Feature flag disabled | **N** | Test: flag off â†’ cache.get never called |
| **Post-write stale guard (Finding 1)** | **N â€” CRITICAL** | See below |
| **cache.delete failure (Finding 2)** | **? (unclear)** | Test: delete throws â†’ writeProfile returns saved |

**Critical missing test â€” concurrent-read-during-write:**

```javascript
it('does not re-populate cache with stale data when write invalidates during read', async () => {
  // Pre-populate cache with v0
  cache.set('k', v0);
  // Start a read that will pause at the await
  const readPromise = readProfile('k');
  // While read is in-flight, complete a write
  await writeProfile('k', newData);
  // The write should have cleared the cache
  expect(cache.get('k')).toBe(undefined);
  // Let the read complete
  const readResult = await readPromise;
  // The read returns v0 (acceptable â€” it was in-flight during the write)
  expect(readResult).toBe(v0);
  // The cache must NOT be re-populated with v0
  expect(cache.get('k')).toBe(undefined);
  // A fresh read must get the committed version
  const freshResult = await readProfile('k');
  expect(freshResult).toBe(newData);
});
```

**Test ambition check:**
- "Ship at 2am?" â€” The concurrent-read-during-write test above. Not in the plan.
- "Hostile QA test?" â€” Same test. Also: cache.delete throws during successful write â†’ caller should NOT see a write failure.
- "Chaos test?" â€” Interleaved reads and writes at high frequency verifying no stale cache entry persists for more than TTL after a write.

**Test pyramid:** Unit tests for hit/miss/eviction/TTL + integration tests for
full flow. Appropriate for a single-process in-memory cache.

**Flakiness risk:** TTL tests depending on real wall-clock time will be flaky.
Use clock mocking (e.g., fake timers, dependency-injected clock) for TTL tests.
The plan does not mention this; it should be specified.

*Section 6 findings: 3 test gaps (feature flag, post-write guard, cache.delete
failure path). The post-write guard test is CRITICAL.*

---

### Section 7: Performance Review

**Memory usage:**
- LRU: bounded at 1000 entries and 16 MiB. 900 hot keys fit comfortably.
- No memory leak risk â€” LRU eviction prevents unbounded growth.
- Worst-case steady-state: 16 MiB additional heap per process.

**N+1 queries:** Cache reduces DB reads. No new query patterns introduced.

**Database indexes:** No new queries. Existing index coverage unchanged.

**Connection pool:** No new connections. Cache is in-memory. DB connections
are only opened on cache misses.

**Slow paths (estimated):**

| Path | Estimated p99 |
|------|---------------|
| Cache hit | < 1 ms (in-memory LRU lookup) |
| Cache miss with DB read | existing p99 (cache adds ~1 ms overhead) |
| Bypass mode | existing p99 (no overhead) |

**FINDING 4 (operational): Rollout advancement criterion is qualitative**

The plan says "enable for 10% of keys, then 50%, then all keys after one healthy
hour at each stage." "Healthy" is undefined. The acceptance targets (DB CPU <50%,
p95 <60 ms, â‰¥60% cache hits) are stated but not tied to the rollout gate criteria.

**Recommended (auto-decided):** Define explicit gate criteria in the plan. Example:
"Advance when cache hit rate â‰¥50% AND fallback error rate <0.1% AND p95 <80 ms
AND no error-rate regression, sustained over the preceding hour."

*Section 7 findings: 1 WARNING (undefined rollout gate criterion).*

---

### Section 8: Observability & Debuggability Review

**The plan specifies monitoring:** hit/miss, eviction, cache bytes, fallback
errors, DB CPU, read p95 â€” all without raw IDs. This is correct.

**Gaps:**

**FINDING 5 (observability): Metric names, alert thresholds, and "healthy" gate
criteria not defined**

The plan lists what to monitor but not:
1. Specific metric names (how to query them in the observability stack)
2. Alert thresholds (e.g., "alert when fallback error rate > 1%")
3. Dashboard panels (what does day-1 monitoring look like?)
4. Quantitative gate criteria for rollout advancement (links to Finding 4)
5. Runbook: "Cache fallback rate spiked â€” what do I do?"

Without metric names, the monitors cannot be set up before rollout, which
violates "observability is scope, not afterthought."

**Recommended (auto-decided):** Add an observability spec to the plan listing:
- Metric names for hit count, miss count, eviction count, byte usage, fallback
  error count, DB CPU, read p95
- Alert thresholds for fallback error rate and p95 regression
- Runbook stub: fallback spike â†’ check adapter health â†’ disable flag if
  error rate sustained > threshold â†’ investigate adapter failure mode

**Debuggability:** "If a bug is reported 3 weeks post-ship..." â€” The plan specifies
logging hit/miss and errors without raw IDs. Structured log lines at entry (key
hash, not raw key), exit (HIT/MISS/BYPASS), and on cache failure should give
enough context to reconstruct behavior. The plan does not specify log levels or
format; this should be added.

*Section 8 findings: 1 WARNING (observability spec incomplete).*

---

### Section 9: Deployment & Rollout Review

**Migration safety:** No DB migrations. Pure in-process change. Zero downtime.

**Feature flag:** Existing runtime feature flag is the deployment gating
mechanism. Correct.

**Rollout order:** Flag disabled by default. Enable at 10% â†’ 50% â†’ 100%.

**Rollback:**
1. Disable feature flag. (Seconds.)
2. Reads and writes bypass cache immediately.
3. Re-enable when ready â€” starts with empty cache.
4. No data migration, no schema rollback.

**Deploy-time risk:** Old code and new code run simultaneously only during the
deploy itself. Since the cache is disabled by default, there is no cache-state
risk during the deploy window.

**FINDING 6 (deployment): Multi-process detection relies only on startup check**

The plan says "startup rejects that configuration while caching is enabled." This
covers process boot. It does not cover:
- A process crash and respawn in an environment that has since added a second
  process (e.g., autoscaling event between restarts)
- Docker/k8s restart policies that could instantiate multiple replicas

The check runs once at startup; it does not re-validate at runtime.

**Recommended (auto-decided):** Document this as a known constraint: the startup
check is a single-point guard. If the deployment environment is changed (e.g.,
replica count increased), the operator must disable caching before scaling to
multiple processes. Add this to the runbook stub.

**Post-deploy verification:**

The plan mentions monitoring targets. The first-5-minutes check should include:
- Cache hit rate > 0% (cache is being used)
- Fallback error rate = 0% (adapter is healthy)
- p95 not elevated (no regression)
- DB CPU not elevated vs. baseline

*Section 9 findings: 1 WARNING (multi-process check robustness).*

---

### Section 10: Long-Term Trajectory Review

**Technical debt introduced:** Minimal. The wrapper is thin, testable, and
flag-controlled. No locking-in debt.

**Path dependency:** The plan explicitly preserves "a future replacement path
without introducing a general cache framework now." Distributed cache (Redis)
or a different LRU implementation can replace this without changing the
repository interface.

**Knowledge concentration:** The concurrent-read-during-write ordering rule is
subtle. It must be documented in a code comment in the wrapper, not just in this
plan. A new engineer who reads only the code needs to understand why the
post-write guard exists.

**Reversibility:** 5/5 â€” Feature flag makes this completely reversible. Disabling
returns the system to identical behavior as pre-cache with an empty-cache
clean state.

**Ecosystem fit:** In-process LRU in a Node.js single-threaded event loop is
idiomatic. The pattern is standard.

**1-year question:** The ordering invariant and the post-write guard are the only
non-obvious elements. With a code comment explaining the invariant and the guard's
purpose, a new engineer would understand the design. Without those comments, the
guard looks like dead code and may be "cleaned up" incorrectly.

**Dream state delta:** After this plan ships successfully:
- DB CPU: ~45% (estimated from â‰¥60% cache hit rate on 900 hot keys)
- p95: ~50 ms (estimated)
- Headroom for user growth before DB becomes the bottleneck

*Section 10 findings: 0 new. Documentation of the ordering invariant in code is
implied by Finding 1's fix.*

---

### Section 11: Design & UX Review

**SKIPPED â€” no UI scope detected.**

The plan states: "This is an internal backend change with no UI, API, schema,
pricing, or developer onboarding change." Section 11 does not apply.

---

## Required Outputs

### NOT in scope

| Item | Rationale |
|------|-----------|
| Distributed cache (Redis) | Out of scope; single-process constraint |
| Cross-process coherence | Not needed in single-process model |
| Cache prewarming | Complexity not justified by 900-key set |
| Changing consistency semantics | Out of scope; read-during-write window accepted |
| New product surfaces | Backend-only change |

### What already exists

| Component | Status |
|-----------|--------|
| LRU adapter (1000 entries, 16 MiB, 30s TTL) | Exists; reused unchanged |
| Single-flight per-key coalescing wrapper | Exists; reused unchanged |
| Runtime feature flag for rollout | Exists; reused unchanged |
| Repository contract tests (tenant isolation, key validation, absence, DB failures, auth) | Exists; unchanged |
| Typed API error mapping | Exists; preserved |

### Dream state delta

```
THIS PLAN LEAVES US AT:
  DB CPU: ~45% (from ~70%) â€” target met if â‰¥60% hit rate
  p95:    ~50 ms (from 120 ms) â€” target met
  Cache:  Process-local; no cross-process coherence

REMAINING GAP TO 12-MONTH IDEAL:
  Distributed caching (if process count scales)
  Prewarming strategies (if cold-start spikes become a concern)
  Full observability stack integration (metric names, dashboards, runbooks)
```

### Error & Rescue Registry

```
METHOD/CODEPATH            | WHAT CAN GO WRONG              | EXCEPTION CLASS
---------------------------|--------------------------------|-------------------
readProfile(key)           | cache.get adapter failure      | CacheAdapterError
                           | repository.read typed failure  | RepositoryError
                           | cache.set adapter failure      | CacheAdapterError
writeProfile(key, update)  | repository.write typed failure | RepositoryError
                           | cache.delete adapter failure   | CacheAdapterError â† GAP

EXCEPTION CLASS              | RESCUED? | RESCUE ACTION                   | USER SEES
-----------------------------|----------|---------------------------------|------------------
CacheAdapterError (get)      | Y        | Bypass; treat as miss           | Transparent
RepositoryError (read)       | Y        | Propagate typed error           | Typed API error
CacheAdapterError (set)      | Y        | Bypass; return value            | Transparent
RepositoryError (write)      | Y        | Propagate typed error           | Typed API error
CacheAdapterError (delete)   | N â† GAP  | None â€” propagates as write fail | Spurious error
```

### Failure Modes Registry

```
CODEPATH              | FAILURE MODE                     | RESCUED? | TEST? | USER SEES?           | LOGGED?
----------------------|----------------------------------|----------|-------|----------------------|--------
readProfile           | cache.get fails                  | Y        | Y     | transparent          | Y
readProfile           | repo.read fails                  | Y        | Y     | typed API error      | Y
readProfile           | cache.set fails                  | Y        | Y     | transparent          | Y
readProfile           | stale re-pop after write         | N â† GAP  | N     | stale data (silent)  | N  â† CRITICAL
writeProfile          | repo.write fails                 | Y        | Y     | typed API error      | Y
writeProfile          | cache.delete fails               | N â† GAP  | ?     | false write failure  | N  â† CRITICAL
writeProfile          | write succeeds, delete succeeds  | Y        | Y     | transparent          | Y
sf coalescing         | read fails while coalesced       | Y        | Y     | propagated error     | Y
adapter bypass        | bypass active, reads continue    | Y        | Y     | transparent          | Y
```

### Diagrams

**System architecture:** See Section 1.

**Data flow (including shadow paths):** See Section 1 and Section 4.

**State machine:** See Section 1.

**Error flow:**

```
  Error in readProfile:
  cache.get throws â”€â”€â–¶ bypass mode â”€â”€â–¶ treat as miss â”€â”€â–¶ repo.read
  repo.read throws â”€â”€â–¶ propagate â”€â”€â–¶ sf releases â”€â”€â–¶ caller gets RepositoryError
  cache.set throws â”€â”€â–¶ bypass mode â”€â”€â–¶ value still returned to caller

  Error in writeProfile (proposed fix applied):
  repo.write throws â”€â”€â–¶ propagate â”€â”€â–¶ cache not modified â”€â”€â–¶ caller gets error
  cache.delete throws â”€â”€â–¶ caught â”€â”€â–¶ bypass mode activates â”€â”€â–¶ caller gets saved
```

**Deployment sequence:**

```
  1. Deploy new code (cache disabled by default)
  2. Verify: no errors, p95 stable, DB CPU stable
  3. Enable flag at 10%
  4. Wait 1 healthy hour (gate criteria: see Finding 4)
  5. Advance to 50%
  6. Wait 1 healthy hour
  7. Advance to 100%
  8. Record results vs acceptance targets
```

**Rollback flowchart:**

```
  Error/regression detected
        â”‚
        â–¼
  Disable feature flag (seconds)
        â”‚
        â–¼
  Cache bypassed; empty on re-enable
        â”‚
        â–¼
  Investigate: adapter failure? Race? Load?
        â”‚
        â”œâ”€ Adapter issue â”€â”€â–¶ fix adapter â”€â”€â–¶ re-enable
        â””â”€ Race issue â”€â”€â–¶ apply guards (Finding 1/2) â”€â”€â–¶ re-enable
```

### Stale Diagram Audit

No existing ASCII diagrams found in plan or noted codebase files. N/A.

---

## Implementation Tasks

Synthesized from this review's findings. Each task derives from a specific
finding above. Run with Claude Code; checkbox as you ship.

- [ ] **T1 (P1, human: ~1h / CC: ~5min)** â€” CacheWrapper â€” Add post-write stale re-population guard
  - Surfaced by: Section 1 (Finding 1), Section 4 â€” concurrent-read-during-write race violates ordering invariant
  - Files: `cacheWrapper.js` (or equivalent wrapper module)
  - Code: add `if (cache.get(key) === undefined)` guard before `cache.set(key, value)` in readProfile
  - Verify: new concurrent-read-during-write test (see T3); existing tests pass

- [ ] **T2 (P1, human: ~30min / CC: ~5min)** â€” CacheWrapper â€” Handle cache.delete failure in writeProfile
  - Surfaced by: Section 2 (Finding 2) â€” delete failure propagates as spurious write error
  - Files: `cacheWrapper.js`
  - Code: wrap `cache.delete(key)` in try/catch in writeProfile; return saved regardless
  - Verify: test â€” delete throws â†’ writeProfile resolves with saved value

- [ ] **T3 (P1, human: ~1h / CC: ~10min)** â€” Tests â€” Add concurrent-read-during-write test
  - Surfaced by: Section 6 â€” no test covers the post-write stale re-population scenario
  - Files: `cacheWrapper.test.js`
  - Test: pause read at await, complete write, resume read, assert cache not re-populated with stale value
  - Verify: test fails without T1 fix, passes with it

- [ ] **T4 (P2, human: ~30min / CC: ~5min)** â€” Docs/Security â€” Document exact cache key format
  - Surfaced by: Section 3 (Finding 3) â€” "without ambiguity" asserted but format not specified
  - Files: plan doc + code comment in key construction logic
  - Specify: exact format, collision-resistance guarantee, characters that tenant/profile IDs may not contain

- [ ] **T5 (P2, human: ~30min / CC: ~5min)** â€” Rollout â€” Define quantitative gate criteria for rollout advancement
  - Surfaced by: Section 7 (Finding 4) and Section 8 (Finding 5)
  - Files: plan doc + runbook
  - Add: explicit numeric thresholds (hit rate, fallback error rate, p95, DB CPU) that define "healthy hour"

- [ ] **T6 (P2, human: ~20min / CC: ~5min)** â€” Observability â€” Add metric names, alert thresholds, and runbook stub
  - Surfaced by: Section 8 (Finding 5) â€” metric names and alert thresholds not defined
  - Files: plan doc + observability config (metrics definitions, alert rules)
  - Include: metric names for hit/miss/eviction/bytes/fallback/p95/DB CPU; alert on fallback spike and p95 regression

- [ ] **T7 (P3, human: ~20min / CC: ~5min)** â€” Deployment â€” Document multi-process constraint in runbook
  - Surfaced by: Section 9 (Finding 6) â€” startup check does not cover post-startup process scaling
  - Files: runbook
  - Add: "disable caching before scaling to multiple replicas; re-enable only after confirming single-process config"

- [ ] **T8 (P2, human: ~30min / CC: ~5min)** â€” Tests â€” Add clock-mocked TTL tests
  - Surfaced by: Section 6 â€” TTL tests depending on real wall-clock time are flaky
  - Files: `cacheWrapper.test.js`
  - Use fake timers / dependency-injected clock for 30s and 10s TTL expiry tests

- [ ] **T9 (P2, human: ~20min / CC: ~5min)** â€” Tests â€” Add feature-flag-disabled test
  - Surfaced by: Section 6 â€” no test verifies that flag-off bypasses cache entirely
  - Files: `cacheWrapper.test.js`
  - Test: flag disabled â†’ cache.get never called â†’ reads go directly to repository

---

```
+====================================================================+
|            MEGA PLAN REVIEW â€” COMPLETION SUMMARY                   |
+====================================================================+
| Mode selected        | HOLD SCOPE                                  |
| System Audit         | Skipped (per run instructions)              |
| Step 0               | HOLD SCOPE confirmed; Approach B selected;  |
|                      | ordering invariant identified as critical    |
| Section 1  (Arch)    | 1 CRITICAL GAP (post-write stale re-pop)    |
| Section 2  (Errors)  | 4 error paths mapped, 1 CRITICAL GAP        |
|                      | (cache.delete failure)                      |
| Section 3  (Security)| 1 WARNING (key format not documented)        |
| Section 4  (Data/UX) | 0 new gaps (Findings 1-2 cover)             |
| Section 5  (Quality) | 0 new (covered by Sections 1-2)             |
| Section 6  (Tests)   | Diagram produced, 3 gaps                    |
| Section 7  (Perf)    | 1 WARNING (rollout gate criterion undefined) |
| Section 8  (Observ)  | 1 WARNING (metric names/alerts/runbook)      |
| Section 9  (Deploy)  | 1 WARNING (multi-process check robustness)   |
| Section 10 (Future)  | Reversibility: 5/5, debt items: 0           |
| Section 11 (Design)  | SKIPPED (no UI scope)                       |
+--------------------------------------------------------------------+
| NOT in scope         | written (5 items)                           |
| What already exists  | written                                     |
| Dream state delta    | written                                     |
| Error/rescue registry| 5 methods, 1 CRITICAL GAP                   |
| Failure modes        | 9 total, 2 CRITICAL GAPS                    |
| TODOS.md updates     | 0 items proposed (all addressed in tasks)   |
| Scope proposals      | 0 (HOLD SCOPE)                              |
| CEO plan             | skipped (HOLD SCOPE)                        |
| Outside voice        | disabled (codex_reviews: disabled)          |
| Lake Score           | N/A (HOLD SCOPE, no coverage options)       |
| Diagrams produced    | 6 (architecture, data flow, state machine,  |
|                      | error flow, deployment, rollback)           |
| Stale diagrams found | 0                                           |
| Unresolved decisions | 0                                           |
+====================================================================+
```

### Unresolved Decisions

None. All findings were auto-decided in HOLD SCOPE mode as per run instructions.
All decisions favor the more complete, conservative fix option.

---

## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/plan-ceo-review` | Scope & strategy | 1 | issues_open | HOLD SCOPE, 2 critical gaps, 5 warnings |
| Outside Review | disabled | Independent 2nd opinion | 0 | disabled | â€” |
| Eng Review | `/plan-eng-review` | Architecture & tests (required) | 0 | â€” | â€” |
| Design Review | `/plan-design-review` | UI/UX gaps | 0 | â€” | â€” |
| DX Review | `/plan-devex-review` | Developer experience gaps | 0 | â€” | â€” |

**OUTSIDE COVERAGE:** codex_reviews: disabled. Outside review step skipped per configuration. No outside review was run or attempted. Re-enable: `gstack-config set codex_reviews enabled`.

**VERDICT:** CEO Review run (HOLD SCOPE). 2 critical gaps found (post-write stale re-population; cache.delete failure propagation). eng review required before shipping.

NO UNRESOLVED DECISIONS
