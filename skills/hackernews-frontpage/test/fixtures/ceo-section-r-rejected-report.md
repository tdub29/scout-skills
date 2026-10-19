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

## CEO Review â€” HOLD SCOPE Mode
*Conducted 2026-09-09 â€” automated run, AskUserQuestion unavailable; skill-recommended options auto-selected.*

### Step 0: Scope Challenge + Mode

**Mode: HOLD SCOPE** (requested by caller; appropriate â€” this is a backend performance fix with well-measured targets, not a greenfield feature).

**0A. Premise Challenge**

1. Is this the right problem? Yes. 70% DB CPU and 120 ms p95 on ~900 hot keys is measured, not hypothetical. A process-local cache is the canonical first response.
2. Is the plan the most direct path? Yes. The read/write pseudocode is minimal, and the rollout uses an existing flag.
3. What happens if we do nothing? DB CPU stays at 70%, approaching saturation; tail latency and error risk grow.

**0B. Existing Code Leverage**

| Sub-problem | Existing code | Reused? |
|---|---|---|
| LRU eviction + byte cap | Existing LRU adapter | Yes |
| Concurrent miss coalescing | Existing per-key single-flight wrapper | Yes |
| Bypass on adapter failure | Existing adapter behavior | Yes |
| Feature flag rollout | Existing runtime flag | Yes |
| Tenant/auth scoping | Existing key encoding + auth layer | Yes |

Nothing is being rebuilt. This is a thin orchestration wrapper.

**0C. Dream State Mapping**

```
CURRENT STATE                    THIS PLAN                      12-MONTH IDEAL
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
DB CPU 70%, p95 120ms     â†’  In-process LRU, 60%+ hit rate  â†’  DB CPU <50%,
900 hot keys repeated          DB CPU <50%, p95 <60ms            p95 <60ms,
No cache layer                 Staged rollout w/ flag             possible Redis
                                                                  if multi-process
                                                                  needed later
```

This plan moves directly toward the 12-month ideal. The interface preserves the Redis upgrade path.

**0C-bis. Implementation Alternatives**

```
APPROACH A: Process-local LRU wrapper (CHOSEN by plan)
  Summary: Wrap existing repository with cache.get/set/delete at call sites.
  Effort:  S
  Risk:    Low
  Pros:    No new dependencies; reuses existing LRU adapter and single-flight
           wrapper; rollback via existing flag; synchronous/atomic in JS event loop.
  Cons:    Cache lost on restart; does not help if multi-process is ever needed.
  Reuses:  Existing LRU adapter, single-flight wrapper, feature flag.

APPROACH B: Redis-backed distributed cache
  Summary: Replace in-process LRU with Redis read-through.
  Effort:  L
  Risk:    High
  Pros:    Survives restarts; supports multi-process; higher cache capacity.
  Cons:    New infrastructure dependency; network RTT adds latency; multi-process
           coherence becomes a real problem; overkill for single-process service.
  Reuses:  None of the existing LRU infrastructure.

APPROACH C: DB-level read replica / materialized view
  Summary: Move hot reads to a read replica with DB-level caching.
  Effort:  XL
  Risk:    High
  Pros:    No application-layer cache; DB manages consistency.
  Cons:    Infrastructure changes outside the service; 6-month lead time;
           out of the service team's control.
  Reuses:  None.
```

**RECOMMENDATION:** Approach A. The service is single-process by contract; Approach A is the minimum correct solution. Approaches B and C are valid future paths if the architecture changes â€” the plan's interface intentionally preserves those paths.

**0D. HOLD SCOPE Analysis**

Complexity check: The change touches one repository wrapper (2 functions). No new services, no new classes. Well within complexity budget.

Minimum set: The plan is already minimal â€” the pseudocode is the complete implementation surface. No work can be deferred without blocking the core objective.

**0E. Temporal Interrogation**

```
HOUR 1 (foundations):  Does the existing LRU adapter expose the exact
                        get/set/delete/bypass interface the wrapper assumes?
                        Confirm the adapter's undefined-on-miss contract.
HOUR 2-3 (core logic): What is the concrete type of the sentinel? A specific
                        symbol, null, or an object? undefined must be reserved
                        for cache miss.
HOUR 4-5 (integration):How does the single-flight wrapper interact with
                        cache.set â€” does it call readProfile or repository.read
                        directly? The cache.set must be inside the single-flight
                        scope to avoid double population.
HOUR 6+ (polish/tests):Controlled pause/release tests for concurrent read+write
                        interleaving (read starts, write completes + deletes,
                        read resumes and calls cache.set with stale value).
                        This is the hardest behavior to reason about.
```

---

### Section 1: Architecture Review

**System architecture:**

```
  CALLER
    â”‚
    â–¼
  ProfileRepository (interface unchanged)
    â”‚
    â”œâ”€ cache.get(key) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¶ LRU Adapter (in-process)
    â”‚        â”‚                                â”‚
    â”‚    [hit: value]                    [synchronous,
    â”‚        â”‚                           atomic in JS
    â”‚    return cached â—€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€  event loop]
    â”‚        â”‚
    â”‚    [miss: undefined]
    â”‚        â”‚
    â–¼        â–¼
  repository.read(key)  â—€â”€â”€â”€â”€ DB
    â”‚
    â”œâ”€[success]â”€â”€â–¶ cache.set(key, value) â”€â”€â–¶ LRU Adapter
    â”‚                   â”‚
    â”‚               return value
    â”‚
    â””â”€[error]â”€â”€â–¶ propagate (no cache.set)

  WRITE PATH:
  CALLER
    â”‚
    â–¼
  repository.write(key, update) â”€â”€â–¶ DB
    â”‚
    â”œâ”€[success]â”€â”€â–¶ cache.delete(key) â”€â”€â–¶ LRU Adapter
    â”‚                   â”‚
    â”‚               return saved
    â”‚
    â””â”€[error]â”€â”€â–¶ propagate (cache.delete NOT called â€” intentional)

  FAILURE PATH:
  Any cache.get / cache.set / cache.delete throws
    â”‚
    â–¼
  LRU Adapter enters BYPASS mode (existing behavior)
    â”‚
    â–¼
  All reads/writes go directly to DB until adapter reinitialized (empty cache)
```

**Cache state machine:**

```
  [flag disabled] â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¶ BYPASS (all ops â†’ DB)
       â”‚
  [flag enabled]
       â”‚
       â–¼
     EMPTY â”€â”€(first miss)â”€â”€â–¶ WARMING â”€â”€(adapter error)â”€â”€â–¶ BYPASS
       â–²                        â”‚                              â”‚
       â”‚                    (write)                      (reinit/empty)
       â”‚                        â”‚                              â”‚
       â”‚                   key deleted                         â”‚
       â”‚                        â”‚                              â–¼
       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ (TTL expiry) â—€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ EMPTY â—€â”€â”€â”˜
```

**Coupling concerns:** The wrapper introduces coupling between ProfileRepository and the LRU Adapter. This coupling is intentional and bounded: the adapter is an existing shared component, and the bypass behavior decouples the failure modes.

**Before/after dependency graph:**

```
BEFORE:                          AFTER:
Caller â”€â”€â–¶ Repository â”€â”€â–¶ DB    Caller â”€â”€â–¶ Repository â”€â”€â–¶ LRU Adapter
                                                        â””â”€â”€â–¶ DB (on miss)
```

**Single points of failure:**
- The LRU Adapter: mitigated by bypass mode.
- The single process: by design; multi-process is explicitly unsupported and rejected at startup.

**Scaling:**
- 10x load: Hot 900 keys still cached; miss rate is unchanged; DB load stays lower. Holds.
- 100x load: Single-process limit is reached before the cache becomes the bottleneck. Out of scope by contract.

**Security architecture:** Auth runs before repository access; keys encode tenant+profile IDs; no new API surface; no new secrets; cached values cannot bypass authorization. OK.

**Production failure scenarios:**
- LRU Adapter throws on get: Bypass mode. DB reads continue. OK.
- LRU Adapter throws on set: Bypass mode. Worst case: one read returns stale (see Section 4). OK.
- LRU Adapter throws on delete: The plan states "any cache failure" triggers bypass. This must include delete â€” see Section 2 gap.
- DB connection fails during read: Error propagates as before. Adapter not written. OK.
- OOM: 16 MiB byte cap + 1000-entry cap prevents unbounded growth. OK.

**Rollback posture:** Disable feature flag â†’ reads and writes bypass cache â†’ DB returns to baseline behavior. Enabling creates an empty cache. Rollback is fast, clean, and reversible. 5/5.

**Assessment:** Architecture is sound. No structural issues. Required diagram produced above.

---

### Section 2: Error & Rescue Map

```
METHOD/CODEPATH         | WHAT CAN GO WRONG            | EXCEPTION CLASS
------------------------|------------------------------|--------------------
cache.get(key)          | Adapter internal error       | AdapterError
repository.read(key)    | DB connection failure         | DBConnectionError
                        | Query timeout                | TimeoutError
                        | Record not found             | (sentinel, not error)
cache.set(key, value)   | Adapter internal error       | AdapterError
                        | Byte cap full                | (handled by eviction)
repository.write(k,u)   | DB write failure             | DBWriteError
                        | Validation error             | ValidationError
                        | Conflict / constraint        | ConflictError
cache.delete(key)       | Adapter internal error       | AdapterError
```

```
EXCEPTION CLASS         | RESCUED?  | RESCUE ACTION                  | USER SEES
------------------------|-----------|--------------------------------|----------------
AdapterError (get)      | Y         | Bypass mode until reinit       | Transparent
AdapterError (set)      | Y         | Bypass mode until reinit       | Transparent
AdapterError (delete)   | Y*        | Bypass mode until reinit       | Transparent*
DBConnectionError       | Y         | Existing typed API mapping     | Existing error
TimeoutError            | Y         | Existing typed API mapping     | Existing error
DBWriteError            | Y         | Propagate; cache NOT deleted   | Existing error
ValidationError         | Y         | Propagate; cache NOT deleted   | Existing error
ConflictError           | Y         | Propagate; cache NOT deleted   | Existing error
```

*AdapterError (delete): The plan says "on any cache failure the existing adapter bypasses the cache." This SHOULD cover delete failures, but the adapter-failure test suite must explicitly verify this case (see Section 6 gap).

**GAP identified:** If cache.delete throws after a successful repository.write, bypass mode should activate. This preserves the write's committed value (all reads go to DB). The plan's wording covers this but the test suite does not explicitly verify it.

**Assessment:** No critical gaps. One test coverage gap on delete-path adapter failure. Error handling architecture is correct.

---

### Section 3: Security & Threat Model

| Threat | Likelihood | Impact | Mitigated? |
|---|---|---|---|
| Cross-tenant cache read | Low | High | Yes â€” keys encode tenant ID + profile ID |
| Auth bypass via cache | Low | High | Yes â€” auth runs before repository access |
| PII in logs/metrics | Low | High | Yes â€” raw IDs excluded from all monitoring |
| Stale cache serving wrong user | Low | Med | Yes â€” tenant ID in key prevents cross-user access |
| Cache poisoning via write | Low | Med | Yes â€” write path deletes key; cache only stores DB-confirmed values |
| DoS via cache bypass (flag off) | Low | Low | Yes â€” existing DB capacity handles cold starts |
| New dependency exploit surface | None | â€” | N/A â€” no new dependencies added |

**Assessment:** Security posture is solid. No new attack surfaces. The key-encoding contract and auth-before-cache design are correctly stated. No findings.

---

### Section 4: Data Flow & Interaction Edge Cases

**Read flow (all paths):**

```
  KEY â”€â”€â–¶ cache.get(key)
              â”‚
         [hit: value] â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¶ return value
              â”‚
         [miss: undefined]
              â”‚
              â–¼
         repository.read(key)
              â”‚
         [nil/absent] â”€â”€â–¶ cache.set(key, SENTINEL, TTL=10s) â”€â”€â–¶ return sentinel
              â”‚
         [value] â”€â”€â–¶ cache.set(key, value, TTL=30s) â”€â”€â–¶ return value
              â”‚
         [error] â”€â”€â–¶ propagate (no cache.set)
              â”‚
         [adapter error on set] â”€â”€â–¶ bypass mode; return value anyway
```

**Write flow (all paths):**

```
  KEY, UPDATE â”€â”€â–¶ repository.write(key, update)
                        â”‚
                  [success: saved]
                        â”‚
                  cache.delete(key) â”€â”€[adapter error]â”€â”€â–¶ bypass mode
                        â”‚
                  return saved
                        â”‚
                  [write error] â”€â”€â–¶ propagate
                                    (cache.delete NOT called â€” correct)
```

**Async ordering â€” the in-flight read race:**

```
T0: Read R1 starts â†’ cache.get(key) = undefined (miss)
T1: Write W1 commits â†’ repository.write returns â†’ cache.delete(key) called
T2: R1 resumes â†’ repository.read returns old snapshot
T3: R1 calls cache.set(key, OLD_VALUE)  â† stale write to cache
T4: New Read R2 starts â†’ cache.get(key) = OLD_VALUE (stale hit)
```

**Finding (WARNING):** The plan's consistency invariant states: "Every read begun after that write completes must observe the committed version." But R2 in the timeline above begins after W1 completes and may see the stale value R1 wrote at T3. The stale window is bounded by the 30s TTL, and the plan explicitly excludes "additional version checks or coordination." However, the current invariant wording overstates the guarantee â€” the implementation provides *eventual* consistency with a bounded stale window (max 30s), not strict post-write read-your-writes for concurrent reads.

The plan should clarify: the consistency guarantee applies to reads that begin AFTER both (a) the write commits AND (b) any in-flight concurrent read's cache.set has completed. For the narrow window between W1's cache.delete and R1's cache.set, a subsequently-started reader may see a stale cache entry for up to 30s. This is acceptable given the "immutable profile-summary DTO" semantics (updates are infrequent), but it should be stated rather than implied by "TTL expiry is not a substitute."

**No interaction edge cases apply** â€” there is no user-visible interaction (backend-only change).

**Assessment:** One WARNING on consistency invariant wording. No critical data flow gaps.

---

### Section 5: Code Quality Review

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

- **Organization:** Correct. Two functions, each with a single responsibility.
- **DRY:** No violations. The cache adapter is the single source of eviction/TTL logic.
- **Naming:** Clear. `readProfile`/`writeProfile` are semantic and consistent with the repository interface.
- **Error handling:** Delegated correctly. Cache errors flow to the adapter's bypass mechanism; DB errors propagate through existing typed mapping.
- **Over-engineering:** None. The plan correctly resists building a general cache framework.
- **Under-engineering:** The async race (Section 4) is an inherent property of read-through caching without version checks. Given the plan explicitly excludes version checks, this is an accepted design choice, not a quality gap â€” but must be documented.
- **Cyclomatic complexity:** Both functions have â‰¤1 branch. No concern.
- **Sentinel handling:** `undefined` as the cache-miss signal is correct as long as the repository never returns `undefined` for a valid absent record. The plan uses a sentinel object for absent records â€” this distinction must be verified in implementation (absent â‰  undefined).

**Assessment:** Code quality is high. One documentation gap (consistency model for in-flight race). No structural defects.

---

### Section 6: Test Review

**New items introduced:**

```
NEW UX FLOWS:
  None â€” backend-only change.

NEW DATA FLOWS:
  1. readProfile: cache hit path
  2. readProfile: cache miss â†’ DB read â†’ cache.set
  3. readProfile: absent key â†’ sentinel
  4. writeProfile: success â†’ cache.delete
  5. writeProfile: failure â†’ no cache.delete

NEW CODEPATHS:
  1. cache.get returns hit
  2. cache.get returns miss (undefined)
  3. cache.set called on successful read
  4. cache.set skipped on read error
  5. cache.delete called on successful write
  6. cache.delete skipped on failed write
  7. Adapter failure â†’ bypass mode (get path)
  8. Adapter failure â†’ bypass mode (set path)
  9. Adapter failure â†’ bypass mode (delete path)  â† gap
  10. Single-flight coalescing (existing wrapper, new context)

NEW BACKGROUND JOBS / ASYNC WORK:
  None.

NEW INTEGRATIONS / EXTERNAL CALLS:
  None (existing DB, existing adapter).

NEW ERROR/RESCUE PATHS:
  1. Adapter failure on get â†’ bypass
  2. Adapter failure on set â†’ bypass
  3. Adapter failure on delete â†’ bypass (needs explicit test)
```

**Coverage per plan vs. required:**

| Test | In Plan? | Gap? |
|---|---|---|
| Cache hit | Yes | No |
| Cache miss | Yes | No |
| Eviction + byte limits | Yes | No |
| TTL expiry | Yes | No |
| Adapter-failure fallback (get) | Yes (implied) | No |
| Adapter-failure fallback (set) | Yes (implied) | No |
| Adapter-failure fallback (delete) | Unclear | **GAP** |
| Successful write invalidation | Yes | No |
| Failed write preservation | Yes | No |
| Concurrent-miss coalescing | Yes | No |
| Concurrent read+write interleave | Not listed | **GAP** |
| Absent key sentinel (10s TTL) | Implied by TTL test | Partial |
| Sentinel vs. undefined distinction | Not listed | **GAP** (minor) |

**Missing test specs:**

```javascript
// GAP: cache.delete adapter failure triggers bypass
test('adapter failure on cache.delete enters bypass mode', async () => {
  cache.simulateDeleteFailure(true);
  const saved = await writeProfile(key, update);
  expect(bypassMode).toBe(true);
  expect(saved).toEqual(expectedSaved); // write still succeeds
});

// GAP: concurrent read+write interleave
test('read started before write completes may set stale cache entry', async () => {
  // Pause R1 after repository.read, before cache.set
  // Let W1 complete (write + cache.delete)
  // Resume R1: cache.set with old value
  // Verify: new reads see stale value until TTL
  // Verify: stale window is bounded by TTL (â‰¤30s)
});

// GAP (minor): sentinel vs. undefined contract
test('absent key uses sentinel, not undefined, so undefined remains cache-miss signal', async () => {
  const result = await readProfile(absentKey);
  expect(result).not.toBeUndefined(); // sentinel, not miss signal
  expect(cache.get(absentKey)).not.toBeUndefined(); // sentinel is cached
});
```

**Test pyramid:** Unit tests (cache hit/miss/TTL/eviction) + integration tests (write invalidation, single-flight) + contract tests (existing). No E2E needed for this backend change. Pyramid is well-formed.

**Flakiness risk:** The concurrent interleave test requires controlled pause/resume points (e.g., `--expose-gc` or manual promise sequencing). Must not rely on timing.

**2am Friday test:** "Does a write always invalidate the cache, even when the adapter throws on delete?" â€” currently not tested.

**Hostile QA test:** "What if a read and a write race, and the read wins the cache?" â€” currently not tested.

**Chaos test:** "What if the adapter throws intermittently â€” does bypass mode activate, and do reads still return correct DB data?" â€” partially covered by adapter-failure test if it's thorough.

**Assessment:** 3 test gaps (delete-path bypass, read/write interleave, sentinel contract). No blocking gaps, but the interleave test is important for validating the consistency claim.

---

### Section 7: Performance Review

**Acceptance target analysis:**

The target (p95 < 60 ms) with 60% cache hit rate requires the DB tail latency to drop, not just the volume. The key insight: DB CPU at 70% is likely in the queuing-saturated zone where latency grows super-linearly. Going from 70% â†’ <50% CPU utilization can reduce the 95th-percentile queuing delay by 3-5x (M/M/1 queuing model). DB p95 could drop from 120 ms to ~50-60 ms after load reduction, making the overall p95 target achievable even though p95 falls in the DB-served 40%.

The plan's acceptance targets are achievable but depend on this queuing dynamic â€” not just cache hit rate alone. The rollout monitoring will empirically confirm this.

**Memory:** 16 MiB / 1000 entries = ~16 KB average entry size. Profile summaries at this size are plausible but should be verified in staging (large profiles with many fields could skew this).

**Cache miss penalty:** On a cold start or after bypass reinit, all 900 hot keys miss. With 120 ms DB p95 and 70% CPU (warm period), a burst of 900 sequential misses takes ~108 s at 120 ms each, or less in parallel (event loop concurrency). The single-flight wrapper prevents stampede. Cold starts remain within existing DB capacity â€” this is stated and correct.

**Connection pool pressure:** No new DB connections. Cache operations are in-process. No change to connection pool.

**Slow paths:**
1. Cold cache (post-enable or post-bypass): All reads hit DB at 120 ms p95 until warm. Bounded by hot key TTL (30s from first fill).
2. Bypass mode (sustained adapter failure): All reads hit DB indefinitely. Monitor fallback errors.
3. Eviction pressure (>1000 entries or >16 MiB): Evicted keys promote misses. Monitor eviction rate; if high, the 900 hot keys may not all fit â€” investigate DTO sizes.

**Assessment:** No blocking performance issues. One observation to add to the plan: p95 target depends on DB queuing-load reduction, not cache hit rate alone. Verify average DTO size in staging to confirm 16 MiB cap is sufficient.

---

### Section 8: Observability & Debuggability Review

**What the plan specifies:**
- Metrics: hit/miss, eviction, cache bytes, fallback errors, DB CPU, read p95

**Gaps:**

| Observability item | Plan covers? | Gap |
|---|---|---|
| Structured log at adapter failure | No | Missing |
| Log when bypass mode activates | No | Missing |
| Alert: fallback errors > threshold | No | Missing |
| Alert: DB CPU > 60% (early warning) | No | Missing |
| Alert: read p95 > 80 ms (regression warning) | No | Missing |
| Alert: hit rate < 50% (cache degradation) | No | Missing |
| Dashboard: hit rate trend over rollout | No | Missing |
| Dashboard: eviction rate (cap pressure indicator) | No | Missing |
| Runbook: adapter failure â†’ bypass â†’ reinit procedure | No | Missing |
| Runbook: rollback decision criteria | No | Missing |
| Debuggability: can a 3-week-old incident be reconstructed from logs? | Partial | Only if fallback errors are logged with timestamp + bypass entry event |

**Required additions to plan:**

1. **Structured log on bypass activation:** `{event: "cache_bypass_activated", reason: "adapter_error", error_class: "<class>", ts: <ts>}` â€” no key or value content.
2. **Structured log on bypass exit (reinit):** `{event: "cache_reinitialized", ts: <ts>}`.
3. **Alert thresholds:**
   - `fallback_errors > 0 for 5 minutes` â†’ page (adapter likely broken)
   - `cache_hit_rate < 50%` for 10 minutes â†’ warn (eviction pressure or warm-up issue)
   - `db_cpu > 60%` â†’ warn (cache not holding)
   - `read_p95 > 80ms` â†’ warn (regression early warning; flag off if sustained)
4. **Day 1 dashboard panels:** hit rate %, eviction rate/s, cache bytes used, fallback error rate, DB CPU %, read p95 (5m rolling).
5. **Runbook (adapter failure):** (1) Observe fallback_errors alert. (2) Check adapter health (memory pressure? process restart?). (3) Restart process to reinitialize cache. (4) Monitor that bypass exits and hit rate recovers. (5) If repeated, open incident â€” do not re-enable flag until root cause clear.
6. **Runbook (rollback decision):** If error-rate or p95 exceeds baseline by >10% for >5 min, disable flag immediately. Both reads and writes go to DB. Investigate before re-enabling.

**Assessment:** Significant observability gaps. Alerts, dashboard spec, and runbooks are needed for safe operation. These should be added to the plan before implementation.

---

### Section 9: Deployment & Rollout Review

**What the plan specifies:**
- Feature flag: existing runtime flag
- Stages: 10% â†’ 50% â†’ 100%
- Advance criterion: "one healthy hour at each stage"
- Rollback trigger: "error-rate or latency regression"

**Gaps:**

**Finding (P1):** "One healthy hour" is undefined. Without explicit success criteria, the service owner cannot make a consistent, objective advance decision. Define:

```
HEALTHY = all of the following for 60 consecutive minutes:
  - Cache hit rate â‰¥ 40% (warming, approaching target)
  - Fallback error rate = 0
  - DB CPU < previous-stage DB CPU (trending down)
  - read p95 â‰¤ previous-stage read p95 (trending down or flat)
  - Application error rate within existing SLO
```

**Finding:** "Error-rate or latency regression" as the rollback trigger needs quantification:
```
ROLLBACK if any of:
  - Application error rate increases > 10% above baseline
  - read p95 increases > 20% above the stage-entry baseline
  - Fallback errors > 0 for > 5 consecutive minutes
```

**Other deployment items:**

- **No DB migrations:** In-memory cache only. Deploy is a code deploy. Zero downtime.
- **Old/new code interop:** Feature flag gates the wrapper. Old code path (bypass) is always valid. No interop risk.
- **Cold start risk:** Bounded. Single-flight wrapper prevents stampede. OK.
- **Staging test:** Not mentioned. Should validate hit rate and bypass behavior before production rollout.
- **Post-deploy verification (first 5 min):** Check fallback errors = 0, hit rate rising, DB CPU trending down.
- **Post-deploy verification (first hour):** Confirm hit rate â‰¥ 40% at 10% stage, no error regressions.
- **Smoke test:** Run the existing contract test suite post-deploy to confirm correctness is preserved.

**Assessment:** One P1 finding (healthy hour definition) and one gap (rollback quantification). Both should be added to the plan.

---

### Section 10: Long-Term Trajectory Review

**Technical debt:**
- Code debt: Minimal. The wrapper is 2 functions over existing infrastructure.
- Operational debt: Cache state adds a new invisible variable (what's cached, when was it warmed?). Mitigated by bypass mode and short TTL (30s max staleness).
- Testing debt: 3 gaps identified in Section 6. Small.
- Documentation debt: The in-flight read race (Section 4 finding) must be documented in a code comment, or future maintainers will strengthen the invariant incorrectly.

**Path dependency:** The interface is not locked. The plan explicitly states the repository interface "preserves a future replacement path." Redis or another adapter can be substituted without changing the caller interface. Two-way door.

**Knowledge concentration:** The sentinel pattern (absent â‰  undefined â‰  null) and the bypass model are non-obvious. A code comment or inline doc on the consistency model prevents future bugs.

**Reversibility:** 4/5. Flag off = instant rollback. Process restart = empty cache. Only risk: a bypass mode bug could persist until restart.

**Ecosystem fit:** Standard JS async/await pattern with process-local LRU. Aligns with the ecosystem.

**1-year question:** The wrapper is simple enough to be understood immediately. The race condition in the consistency model is the one non-obvious piece â€” document it.

**Assessment:** Long-term trajectory is clean. One documentation debt item (consistency model comment).

---

### Section 11: Design & UX Review

**SKIPPED** â€” no UI scope. The plan explicitly states "no UI, API, schema, pricing, or developer onboarding change." This is a backend-only performance change.

---

### Outside Voice

**Codex review skipped** (`codex_reviews: disabled` per isolated config). Re-enable: `gstack-config set codex_reviews enabled`.

Outside coverage: **disabled** (intentional opt-out, not a provider failure).

---

## Required Outputs

### NOT in scope
| Item | Rationale |
|---|---|
| Distributed (Redis) caching | Single-process contract; multi-process is rejected at startup |
| Cross-process cache coherence | Same as above |
| Cache prewarming | Not needed; hot keys warm naturally within one TTL cycle |
| Changing consistency semantics | Out of scope by plan |
| Cache compression / serialization | Not needed for 16 MiB cap with current DTO sizes |
| New product surfaces or API changes | Explicitly excluded |
| Cache statistics admin UI | Operational tooling beyond current scope |

### What already exists
| Component | Existing code | Used by plan |
|---|---|---|
| LRU adapter | 1000 entries, 16 MiB cap, 30s TTL, sentinel support | Yes â€” cache.get/set/delete |
| Per-key single-flight wrapper | Coalesces concurrent misses | Yes â€” wraps repository.read |
| Runtime feature flag | Existing flag mechanism | Yes â€” rollout stages |
| Tenant/profile key encoding | Auth layer + key schema | Yes â€” no changes needed |
| Repository contract tests | Tenant isolation, key validation, absence, DB failures, authorization | Yes â€” extended, not replaced |
| Adapter bypass behavior | On any adapter failure, bypass until reinit | Yes â€” error handling relies on this |

### Dream state delta
```
  THIS PLAN LEAVES US AT:
    DB CPU < 50%           (from 70%)         â†’ target met
    read p95 < 60 ms       (from 120 ms)      â†’ target met (after queuing load drops)
    Cache hit rate 60%+                        â†’ target met for hot 900 keys
    No UI/API/schema change                    â†’ clean internal change
    Future Redis path preserved               â†’ interface is adapter-agnostic

  REMAINING DELTA TO 12-MONTH IDEAL:
    If multi-process operation is needed later, the LRU wrapper becomes invalid
    and a distributed cache (Redis) is required. The interface is ready; the
    infrastructure and coherence design are not yet built.
    Runbooks, alerts, and dashboard spec are deferred â€” they should be built
    before or during rollout.
```

### Error & Rescue Registry

| Method/Codepath | What can go wrong | Exception class | Rescued? | Rescue action | User sees |
|---|---|---|---|---|---|
| cache.get(key) | Adapter internal error | AdapterError | Y | Bypass mode | Transparent |
| repository.read(key) | DB connection failure | DBConnectionError | Y | Existing typed API | Existing error |
| repository.read(key) | Query timeout | TimeoutError | Y | Existing typed API | Existing error |
| repository.read(key) | Record not found | (sentinel, not error) | Y | Sentinel cached | Absent result |
| cache.set(key, v) | Adapter internal error | AdapterError | Y | Bypass mode | Transparent |
| cache.set(key, v) | Byte cap | (handled by eviction) | Y | Eviction | Transparent |
| repository.write(k,u) | DB write failure | DBWriteError | Y | Propagate; no delete | Existing error |
| repository.write(k,u) | Validation error | ValidationError | Y | Propagate; no delete | Existing error |
| repository.write(k,u) | Conflict | ConflictError | Y | Propagate; no delete | Existing error |
| cache.delete(key) | Adapter internal error | AdapterError | Y* | Bypass mode* | Transparent* |

*Bypass on delete failure: covered by "any cache failure" language; needs explicit test.

### Failure Modes Registry

| Codepath | Failure mode | Rescued? | Test? | User sees | Logged? |
|---|---|---|---|---|---|
| cache.get | Adapter throws | Y | Yes (implied) | Transparent | Should be (gap) |
| cache.get | Returns stale (in-flight race) | N/A | No (gap) | Stale data â‰¤30s | No |
| cache.set | Adapter throws | Y | Yes (implied) | Transparent | Should be (gap) |
| cache.delete | Adapter throws | Y* | No (gap) | Transparent | Should be (gap) |
| repository.read | DB failure | Y | Yes (existing) | Existing error | Yes (existing) |
| repository.write | DB failure | Y | Yes (existing) | Existing error | Yes (existing) |
| Bypass mode | Sustained adapter failure | Y | Partial | Transparent | Gap (no log) |
| Cold start | All keys miss | Y | Implicit | Temporary latency | No |

Rows with `Test? = No (gap)` are test gaps; none are CRITICAL GAPSSince bypass mode prevents silent failures. The in-flight race row is a documentation gap, not a rescue gap (the bounded stale window is accepted behavior).

### TODOS.md updates

No TODOs proposed for HOLD SCOPE mode beyond the implementation tasks below. The observability and test additions are within-scope for the current PR, not deferred work. The future Redis path is already noted in the plan's "out of scope" section.

### Diagrams produced
1. System architecture â€” Section 1 âœ“
2. Cache state machine â€” Section 1 âœ“
3. Before/after dependency graph â€” Section 1 âœ“
4. Read flow (all paths) â€” Section 4 âœ“
5. Write flow (all paths) â€” Section 4 âœ“
6. Async race timeline â€” Section 4 âœ“

Rollback flowchart: feature flag disable â†’ bypass mode â†’ empty cache on re-enable. Single step; no diagram needed beyond the state machine above.

### Stale Diagram Audit
No existing ASCII diagrams found in the plan file prior to this review. No stale diagrams to audit.

---

## Implementation Tasks

Synthesized from this review's findings. Each task derives from a specific finding above. Run with Claude Code or Codex; checkbox as you ship.

- [ ] **T1 (P1, human: ~30min / CC: ~5min)** â€” Plan document â€” Define rollout "healthy hour" success criteria
  - Surfaced by: Section 9 â€” "one healthy hour" is undefined; operators cannot make objective advance decisions
  - Files: PLAN.md (or inline rollout runbook)
  - Verify: Criteria are quantitative and unambiguous (hit rate %, fallback errors, DB CPU, p95 bounds)

- [ ] **T2 (P2, human: ~1h / CC: ~10min)** â€” Wrapper tests â€” Add explicit test: cache.delete adapter failure triggers bypass mode
  - Surfaced by: Section 2 / Section 6 â€” "adapter-failure fallback" test set does not explicitly cover the delete code path
  - Files: `<wrapper test file>`
  - Verify: Test simulates adapter throw on delete; asserts bypass mode activates; write still returns saved value

- [ ] **T3 (P2, human: ~2h / CC: ~15min)** â€” Wrapper tests â€” Add concurrent read+write interleave test
  - Surfaced by: Section 4 / Section 6 â€” Async race where read's cache.set follows write's cache.delete is untested and invalidates the stated consistency invariant
  - Files: `<wrapper test file>`
  - Verify: Controlled pause/release test confirms bounded stale window (â‰¤30s TTL); no panic or error

- [ ] **T4 (P2, human: ~1h / CC: ~10min)** â€” Plan document â€” Clarify consistency invariant to reflect the in-flight read race
  - Surfaced by: Section 4 â€” Current invariant ("every read begun after write completes must observe committed version") is overstated; the implementation allows a bounded stale window for concurrent in-flight reads
  - Files: PLAN.md (consistency contract section), `<wrapper implementation file>` (comment)
  - Verify: Updated invariant accurately describes actual guarantees; code comment explains the race

- [ ] **T5 (P2, human: ~2h / CC: ~20min)** â€” Observability â€” Add structured logs, alert thresholds, and runbooks
  - Surfaced by: Section 8 â€” Bypass activation/exit have no log events; no alert thresholds defined; no operational runbook
  - Files: `<wrapper implementation file>` (logs), monitoring config, runbook doc
  - Verify: Bypass activation logs `{event: "cache_bypass_activated", reason, error_class}`; alerts fire in staging test; runbook covers adapter failure and rollback decision

- [ ] **T6 (P2, human: ~30min / CC: ~5min)** â€” Wrapper tests â€” Add sentinel vs. undefined contract test
  - Surfaced by: Section 6 â€” The absent-key sentinel must not be undefined (which is the cache-miss signal); this contract is untested
  - Files: `<wrapper test file>`
  - Verify: Absent key returns sentinel; `cache.get` of an absent key returns sentinel (not undefined)

_No new tasks from Section 1 (Architecture) â€” no structural issues._
_No new tasks from Section 3 (Security) â€” no attack surfaces introduced._
_No new tasks from Section 5 (Code Quality) â€” code is minimal and correct._
_No new tasks from Section 7 (Performance) â€” targets are achievable; p95 dependency on queuing dynamics is an observation, not a gap._
_No new tasks from Section 10 (Long-term) â€” documentation need is captured in T4._
_No new tasks from Section 11 (Design) â€” skipped, no UI scope._

---

## Completion Summary

```
+====================================================================+
|            MEGA PLAN REVIEW â€” COMPLETION SUMMARY                   |
+====================================================================+
| Mode selected        | HOLD SCOPE                                   |
| System Audit         | Skipped (automated run, per instructions)    |
| Step 0               | HOLD SCOPE confirmed; Approach A accepted;   |
|                      | In-flight read race identified as key concern|
| Section 1  (Arch)    | 0 issues found; architecture is sound       |
| Section 2  (Errors)  | 9 error paths mapped, 1 gap (delete bypass) |
| Section 3  (Security)| 0 issues found; 0 High severity             |
| Section 4  (Data/UX) | 1 WARNING: consistency invariant overstated;|
|                      | in-flight read race bounded by 30s TTL      |
| Section 5  (Quality) | 0 issues found                              |
| Section 6  (Tests)   | Diagram produced; 3 gaps (delete bypass,    |
|                      | read/write interleave, sentinel contract)    |
| Section 7  (Perf)    | 0 issues; p95 target achievable via         |
|                      | queuing-load reduction                       |
| Section 8  (Observ)  | 6 gaps: logs, alerts, dashboard, runbooks   |
| Section 9  (Deploy)  | 1 P1: "healthy hour" undefined; 1 gap:      |
|                      | rollback trigger not quantified             |
| Section 10 (Future)  | Reversibility: 4/5; 1 doc debt item        |
| Section 11 (Design)  | SKIPPED (no UI scope)                       |
+--------------------------------------------------------------------+
| NOT in scope         | written (7 items)                            |
| What already exists  | written (6 components mapped)               |
| Dream state delta    | written                                      |
| Error/rescue registry| 10 paths, 0 CRITICAL GAPS                   |
| Failure modes        | 8 total, 0 CRITICAL GAPS                    |
| TODOS.md updates     | 0 items proposed (gaps are in-PR tasks)     |
| Scope proposals      | 0 proposed, 0 accepted (HOLD SCOPE)        |
| CEO plan             | skipped (HOLD SCOPE)                        |
| Outside voice        | disabled (codex_reviews=disabled in config) |
| Lake Score           | 6/6 findings chose complete option          |
| Diagrams produced    | 6 (arch, state machine, dep graph,          |
|                      | read flow, write flow, race timeline)       |
| Stale diagrams found | 0                                           |
| Unresolved decisions | 0 (automated run; all auto-selected)        |
+====================================================================+
```

### Unresolved Decisions
None. All decision points were auto-selected per spawned-session rules (recommended option). No outstanding AskUserQuestion items.

---

## Review Readiness Dashboard

```
+====================================================================+
|                    REVIEW READINESS DASHBOARD                       |
+====================================================================+
| Review          | Runs | Last Run            | Status    | Required |
|-----------------|------|---------------------|-----------|----------|
| CEO Review      |  1   | 2026-09-09          | HOLD SCOPE| no       |
| Eng Review      |  0   | â€”                   | â€”         | YES      |
| Design Review   |  0   | â€”                   | â€”         | no       |
| Adversarial     |  0   | â€”                   | â€”         | no       |
| Outside Voice   |  0   | â€”                   | disabled  | no       |
+--------------------------------------------------------------------+
| VERDICT: NOT CLEARED â€” Eng Review required before shipping         |
+====================================================================+
```

**Outside coverage:** `codex_reviews: disabled` â€” intentional opt-out. No outside review ran and no fallback was dispatched (disabled is a terminal branch, not a failure state).

**Next step:** Run `/plan-eng-review` to complete the required shipping gate. This CEO review found no blocking issues â€” eng review should be straightforward.

---

## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/plan-ceo-review` | Scope & strategy | 1 | HOLD SCOPE / issues_open | mode: HOLD_SCOPE, 0 critical gaps; 6 tasks (1 P1, 5 P2) |
| Outside Review | disabled | Independent 2nd opinion | 0 | disabled | codex_reviews=disabled; no fallback dispatched |
| Eng Review | `/plan-eng-review` | Architecture & tests (required) | 0 | â€” | not yet run |
| Design Review | `/plan-design-review` | UI/UX gaps | 0 | â€” | not applicable (no UI scope) |
| DX Review | `/plan-devex-review` | Developer experience gaps | 0 | â€” | not yet run |

**OUTSIDE COVERAGE:** Disabled via `codex_reviews: disabled` in isolated config. No provider invoked; no native fallback dispatched. This is an intentional opt-out, not a missing-coverage failure.

**VERDICT:** CEO review complete (HOLD SCOPE). Eng Review required before shipping â€” not yet run.

NO UNRESOLVED DECISIONS
