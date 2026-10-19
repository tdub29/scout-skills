# Plan: Multi-tenant Auth Refactor (reviewed)

Reviewed by `/plan-eng-review` on 2026-09-10 against `PLAN.md` at commit `1d48c77`.
Scope decision: **SCOPE_REDUCED** (D4) from one 12-file / 5-component PR to three
sequenced, bisectable PRs with one storage facade. Every finding below was walked
through interactively; the chosen remedy is recorded per issue.

## Context

The auth layer serves multiple tenants from one cache. The original plan (PLAN.md)
introduces `AuthBroker` and `SessionMint`, three storage/policy classes
(`TokenStore`, `AuthCache`, `RequestPolicy`), rewrites `legacyAuthFlow()`, and
parallelizes token validation, all in one change touching 12 files. The existing
cache adapter already keys entries by tenant ID, issuer, audience, and policy
version, evicts expired tokens, and invalidates on logout, revocation, and tenant
suspension (PLAN.md:7-9). The review's job was to keep every capability the plan
wants while making the change safe to land in an auth path where a mistake is a
cross-tenant leak.

Intended outcome: the legacy flow is retired, both new services are testable in
isolation, tenant scoping is enforced by signatures rather than convention, a
revocation can never be overwritten by a racing mint, and token validation is
bounded by the slowest identity provider (IDP) call instead of the sum of five.

## Existing contracts retained

Unchanged from PLAN.md:7-13. The existing cache adapter keys entries by tenant ID,
issuer, audience, and policy version. It evicts expired tokens and invalidates
entries on logout, token revocation, or tenant suspension. `AuthCache` retains these
validity and tenant-key rules. `AuthCache` is a service-facing facade over that same
existing adapter, with one backing cache. The adapter, its invalidation hooks, and
their existing tests remain in use unchanged.

Changed by this review: the adapter does not serialize mutations (PLAN.md:10), so
`AuthCache` becomes the **single writer** and applies invalidation-wins ordering
(issue 2). Coverage now **does** exercise `legacyAuthFlow()` via characterization
tests (regression rule), reversing PLAN.md:14-16.

## What already exists

| Sub-problem | Existing code | Plan reuses or rebuilds? |
|---|---|---|
| Tenant-keyed token storage, eviction, invalidation | Existing cache adapter (PLAN.md:7-9) | **Reused.** `AuthCache` wraps it; `TokenStore` folded into `AuthCache` unless PR2 shows it is durable storage the adapter cannot provide (D4). |
| Policy versioning | Adapter's policy-version key (PLAN.md:7) | **Reused.** `RequestPolicy` is built only if it carries logic beyond that key; otherwise cut and captured as TODO 1 (D10). |
| Invalidation hooks for logout / revocation / suspension | Existing adapter hooks and tests (PLAN.md:12-13) | **Reused.** New facade-level tests prove the hooks are visible through `AuthCache` (issue 4). |
| Current auth behavior | `legacyAuthFlow()` | **Reused as the oracle.** Characterization tests pin it in PR1; it delegates to the new pipeline in PR2; deleted in PR3. |
| Module-level singleton pattern | Runtime module cache already guarantees one instance per import [Layer 1] | **Replaced** by construction at a composition root and constructor injection (issue 1). |

## Architecture

### Component boundaries (after review)

```
                    composition root (bootstrap)
                    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                    â”‚  adapter = existingCacheAdapter()         â”‚
                    â”‚  cache   = new AuthCache(adapter)          â”‚  â† constructed ONCE
                    â”‚  idp     = new IdpClient(metadataCache)    â”‚
                    â”‚  broker  = new AuthBroker(cache, idp)      â”‚  â† injected, no module export
                    â”‚  mint    = new SessionMint(cache, idp)     â”‚
                    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                   â”‚                â”‚
              reads/invalidates    â”‚                â”‚  writes (mint)
                                   â–¼                â–¼
                          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                          â”‚ AuthCache  (SINGLE WRITER)      â”‚
                          â”‚  get(tenantId, key)             â”‚
                          â”‚  put(tenantId, key, tok, pver)  â”‚â”€â”€â” dropped if a newer
                          â”‚  invalidate(tenantId, reason)   â”‚  â”‚ invalidation for that
                          â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â”‚ tenant key already landed
                                          â”‚                    â”˜
                                          â–¼
                          â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                          â”‚ existing cache adapter          â”‚
                          â”‚  key = tenant|issuer|aud|pver   â”‚
                          â”‚  hooks: logout/revoke/suspend   â”‚  â† unchanged, tests unchanged
                          â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

Every `AuthCache` method takes `tenantId`; a call without one does not compile.
`AuthBroker` and `SessionMint` never touch the adapter directly.

### Issue 1 â€” Shared global mutable `AuthCache` via module-level export
`[P1] (confidence: 8/10) PLAN.md:19-20` â€” "share a global mutable AuthCache instance
via module-level export. Both services mutate it."
**Decision 1A (D5): inject at the composition root, tenant-scoped API.** Both
services take `AuthCache` in their constructor. Tests pass a fake cache and assert
cross-tenant reads are rejected. The module-level export is removed. [Layer 1]

### Issue 2 â€” Two writers, unserialized mutations
`[P1] (confidence: 7/10) PLAN.md:10 + PLAN.md:20` â€” the adapter rules "do not
serialize mutations" and "Both services mutate it." A `SessionMint` write landing
after an `AuthBroker` invalidation for the same tenant key resurrects a token for a
suspended or logged-out tenant.
**Decision 2A (D6): single-writer facade with invalidation-wins ordering.** Only
`AuthCache` writes to the adapter. Each tenant key carries a generation; `put`
supplies the policy version and generation it observed, and is dropped if a newer
invalidation for that key has landed. A test interleaves mint and revoke in both
orders and asserts the token is never readable after revoke.

```
 mint(t1) observes gen=3 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
 revoke(t1): gen=3 â†’ gen=4, entry gone â”‚
                                       â–¼
 put(t1, tok, gen=3) â†’ gen 3 < 4 â†’ DROPPED (no resurrection)
```

### Strangler fig sequencing (Step 0, D4)

```
 PR1 (behavior-preserving)     PR2 (new structure)              PR3 (retire)
 â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
 â”‚ characterization tests  â”‚   â”‚ AuthCache facade (1A,2A)  â”‚    â”‚ delete           â”‚
 â”‚ pin legacyAuthFlow()    â”‚â”€â”€â–¶â”‚ composition root          â”‚â”€â”€â–¶ â”‚ legacyAuthFlow() â”‚
 â”‚ split validateAndDisp.  â”‚   â”‚ AuthBroker + SessionMint  â”‚    â”‚ + delegation shimâ”‚
 â”‚ IDP client: cache+par.  â”‚   â”‚ legacyAuthFlow delegates  â”‚    â”‚ fold char. tests â”‚
 â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â”‚ behind a feature flag     â”‚    â”‚ into pipeline    â”‚
                               â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

A feature flag is a runtime switch that routes traffic to old or new code without a
deploy. Characterization tests from PR1 must pass against both paths in PR2.

### Production failure scenarios per new codepath

| Codepath | Realistic failure | Plan accounts for it? |
|---|---|---|
| `AuthBroker.validate` via `AuthCache` | Forgotten tenant argument reads another tenant's entry | Yes: `tenantId` is required by every method signature (1A) |
| `SessionMint.mint` write | Lands after a revocation for the same key | Yes: invalidation-wins generation check (2A) + interleaving test |
| `IdpClient` parallel calls | One endpoint hangs; the others succeed | Yes: per-call timeout, `allSettled`, typed failure naming the call (5A) |
| `IdpClient` metadata cache | Signing keys rotate inside the TTL | Yes: TTL bounds staleness; test asserts refetch after TTL. Mid-TTL rotation is accepted risk, see NOT in scope |
| Composition root | Two roots constructed in one process (test + app) | Yes: fake cache in tests; only one root in production code |
| `legacyAuthFlow` delegation shim (PR2) | Flag flips mid-request | Flag read once per request at entry; characterization tests cover both paths |

## Code quality

### Issue 3 â€” `validateAndDispatch()` nested try/catch swallowing errors
`[P1] (confidence: 8/10) PLAN.md:23-24` â€” "60 lines with three nested try/catch
blocks; each catch swallows a different error class."
**Decision 3A (D7): split into `validate` / `authorize` / `dispatch` stages
returning a typed result.** Each stage is a flat function returning a discriminated
result (`ok | { kind, cause }`). No catch swallows. Every failure is logged with
tenant and kind. The dispatcher maps result kinds to HTTP outcomes in one place.
Call sites that relied on the silent pass-through are found and updated in PR1,
guarded by the characterization tests.

```
 request â”€â”€â–¶ validate(token) â”€â”€okâ”€â”€â–¶ authorize(claims, policy) â”€â”€okâ”€â”€â–¶ dispatch()
                 â”‚                          â”‚
                 â””â”€ {kind: 'malformed'|      â””â”€ {kind: 'forbidden'|'policy_mismatch'}
                    'expired'|'bad_sig'|
                    'idp_unavailable'|'idp_timeout'}
                                                   â–¼
                              one mapper: kind â†’ status + log line (tenant, kind, cause)
```

DRY: `TokenStore` and `AuthCache` were two wrappers over one adapter; folded (D4).
`RequestPolicy` overlapped the adapter's policy-version key; built only if it
carries real logic (D4, TODO 1).

Inline ASCII diagram comments to add during implementation: `AuthCache` (write
ordering diagram above), the composition root (wiring diagram), the
validate/authorize/dispatch module (pipeline diagram), and the interleaving test
(setup diagram). No existing diagrams were found in this repo to go stale.

## Tests

Test framework: none detected (no CLAUDE.md Testing section, no runtime markers in
this repo). Coverage diagram produced; test file generation deferred to
implementation, where naming follows the host repo's convention.

### REGRESSION (CRITICAL, mandatory)
`PLAN.md:27-28` â€” "legacyAuthFlow() will get rewritten as part of this work; no
regression test for the prior behavior is planned." This is existing behavior being
modified with no covering test. **PR1 adds characterization tests that pin every
observable outcome of `legacyAuthFlow()`** (valid token, expired, bad signature,
wrong tenant, wrong audience, revoked, suspended tenant, IDP unreachable) before any
rewrite. They run against the legacy path in PR1, against both paths in PR2, and are
folded into pipeline tests in PR3. Pre-authorized by the regression rule.

### Issue 4 â€” Adapter tests do not prove invalidation through the facade
`[P1] (confidence: 8/10) PLAN.md:12-16` â€” existing tests stay at the adapter level;
coverage for new components is "success/error paths" only.
**Decision 4A (D8): facade invalidation integration tests + E2E auth journeys.**

### Coverage diagram

```
CODE PATHS                                                   USER FLOWS
[+] auth/legacy/legacyAuthFlow (PR1 oracle)                  [+] Login â†’ request â†’ logout
  â””â”€â”€ [GAP][CRITICAL REGRESSION] 8 characterization cases      â”œâ”€â”€ [GAP][â†’E2E] login â†’ ok â†’ logout â†’ denied
[~] auth/dispatch/validateAndDispatch â†’ 3 stages (3A)          â”œâ”€â”€ [GAP][â†’E2E] suspension mid-session â†’ denied
  â”œâ”€â”€ validate()                                               â”œâ”€â”€ [GAP][â†’E2E] expiry mid-session â†’ expiry reason
  â”‚   â”œâ”€â”€ [GAP] ok                                             â””â”€â”€ [GAP][â†’E2E] IDP unreachable â†’ clear error, no hang
  â”‚   â”œâ”€â”€ [GAP] malformed / expired / bad_sig
  â”‚   â””â”€â”€ [GAP] idp_unavailable / idp_timeout                [+] Tenant isolation
  â”œâ”€â”€ authorize()                                              â”œâ”€â”€ [GAP] tenant A token vs tenant B resource â†’ denied
  â”‚   â”œâ”€â”€ [GAP] ok                                             â””â”€â”€ [GAP] missing tenantId â†’ rejected at facade
  â”‚   â””â”€â”€ [GAP] forbidden / policy_mismatch
  â””â”€â”€ dispatch(): [GAP] kind â†’ status mapping, one per kind  [+] Interaction edge cases
[+] auth/idp/IdpClient (5A)                                    â”œâ”€â”€ [GAP] double-submit login â†’ one session
  â”œâ”€â”€ [GAP] metadata cached within TTL, refetched after        â””â”€â”€ [GAP] concurrent mint + revoke (both orders)
  â”œâ”€â”€ [GAP] one call times out â†’ named failure kind
  â”œâ”€â”€ [GAP] one call 5xx â†’ others still reported
  â””â”€â”€ [GAP] latency bounded by max, not sum
[+] auth/cache/AuthCache (1A, 2A)
  â”œâ”€â”€ [GAP] get/put/invalidate per tenant
  â”œâ”€â”€ [GAP] put with stale generation dropped
  â””â”€â”€ [â˜…â˜…â˜… TESTED at adapter level] eviction + 3 invalidation hooks â€” existing adapter tests
      â””â”€â”€ [GAP] same 4 triggers visible THROUGH the facade (logout, revoke, suspend, expiry)
[+] auth/bootstrap composition root
  â””â”€â”€ [GAP] services receive the same AuthCache; fake cache injectable in tests

COVERAGE: 1/25 paths tested (4%)  |  Code paths: 1/17 (6%)  |  User flows: 0/8 (0%)
QUALITY: â˜…â˜…â˜…:1 â˜…â˜…:0 â˜…:0  |  GAPS: 24 (4 E2E, 0 eval, 1 CRITICAL regression)
```

Legend: â˜…â˜…â˜… behavior + edge + error | â˜…â˜… happy path | â˜… smoke check
[â†’E2E] = needs integration test | [â†’EVAL] = needs LLM eval (none: no LLM calls)

### Test requirements added to the plan

- **PR1, unit (CRITICAL):** `legacyAuthFlow` characterization suite, 8 cases above, recorded outputs become the parity oracle.
- **PR1, unit:** one test per result kind for `validate`, `authorize`, `dispatch`; assert no error is swallowed (spy on logger, assert kind + tenant present).
- **PR1, unit:** `IdpClient` timeout, 5xx, metadata TTL hit/miss, latency bound.
- **PR2, unit:** `AuthCache` tenant-scoped get/put/invalidate; stale-generation put dropped.
- **PR2, integration:** for each of logout, revocation, suspension, expiry: write via `SessionMint`, read via `AuthBroker` through `AuthCache`, assert miss; cross-tenant read rejected; mint/revoke interleaving both orders.
- **PR2, E2E (fake IDP):** the four journeys in the diagram plus double-submit login.
- **PR2, parity:** characterization suite passes with the flag on and off.
- **PR3:** characterization suite folded into pipeline tests; delete shim.

QA test plan artifact written for `/qa` and `/qa-only`:
`~/.gstack/projects/gstack-plan-count-u2LYM3/vercel-sandbox-main-eng-review-test-plan-20260910-142850.md`

## Performance

### Issue 5 â€” Five sequential IDP calls
`[P2] (confidence: 6/10, medium: verify which of the 5 calls are per-token vs.
static IDP metadata) PLAN.md:31-32` â€” "5 sequential API calls to the IDP; they
could be parallelized via Promise.all trivially."
**Decision 5A (D9): cache static IDP metadata; parallelize the rest with per-call
timeout and typed failure mapping.** Classify the five calls in PR1. Signing-key and
discovery-style calls move to a TTL cache keyed by issuer. Remaining per-token calls
run via `Promise.allSettled` with an `AbortSignal` timeout each, mapped into the
typed result from 3A. Plain `Promise.all` was rejected because it fails fast, loses
which call failed, and multiplies IDP load five-fold at login spikes.

```
 before:  â”€call1â”€â–¶â”€call2â”€â–¶â”€call3â”€â–¶â”€call4â”€â–¶â”€call5â”€â–¶   latency = sum(5)
 after:   metadata cache (TTL) â”€â”€ hit â”€â”€â”
                                        â”œâ”€â–¶ allSettled(per-token calls, each with timeout)
                                        â”‚       latency = max(remaining), each failure named
                                        â””â”€ miss â†’ fetch once, then as above
```

No N+1 query pattern (repeated per-item database calls) applies; no database access
changes in this plan. Memory: the metadata cache holds one small document per issuer.

## Failure modes

| New codepath | Failure | Test? | Handling? | User sees | Gap |
|---|---|---|---|---|---|
| `AuthCache.put` after revoke | mint resurrects revoked token | Yes (interleaving, 2A) | Yes (generation check) | denied, reason logged | closed (was critical in original plan) |
| `validate` stage | error swallowed, wrong branch runs | Yes (per-kind, 3A) | Yes (typed result) | specific denial reason | closed (was critical in original plan) |
| `AuthBroker` read | missing tenantId | Yes (facade rejection) | Yes (signature) | denied | closed |
| `IdpClient` | one call hangs | Yes (timeout) | Yes (per-call abort) | `idp_timeout` within budget | closed |
| `IdpClient` | 5xx on one call | Yes | Yes (allSettled) | failure names the call | closed |
| metadata cache | key rotation inside TTL | Yes (refetch after TTL) | Partial | bad_sig until TTL expires | accepted, see NOT in scope |
| delegation shim | flag flips mid-request | Yes (parity both paths) | flag read once per request | consistent outcome | closed |
| composition root | fake cache leaks into prod wiring | Yes (single root test) | Yes | none | closed |

Critical gaps flagged in the original plan: 2 (mint-after-revoke race; swallowed
auth errors). Both closed by approved remedies 2A and 3A. Open critical gaps: 0.

## NOT in scope

- **Big-bang rewrite of `legacyAuthFlow()` in one PR** â€” replaced by strangler fig across PR1-PR3 (D4).
- **`TokenStore` as a separate class** â€” folded into `AuthCache`; revisit in PR2 only if it is durable storage the adapter cannot provide (D4).
- **`RequestPolicy` as a separate class** â€” built only if PR2 shows logic beyond the adapter's policy-version key; otherwise TODO 1 (D10).
- **IDP circuit breaker and backoff** â€” genuine follow-up needing PR1 latency data; TODO 2 (D11).
- **Signing-key rotation inside the metadata TTL** â€” accepted risk; a `kid`-miss-triggered refetch is a candidate follow-up, not required for this refactor.
- **Serializing mutations inside the adapter itself** â€” ordering is enforced in the single-writer facade; pushing it into the adapter would change a shared component the plan promises to leave unchanged.
- **Distribution pipeline** â€” no new binary, package, or image is introduced; nothing to publish.
- **UI changes** â€” none; no design review needed.

## Worktree parallelization strategy

| Step | Modules touched | Depends on |
|---|---|---|
| PR1-a characterization tests | auth/legacy/, auth/__tests__/ | â€” |
| PR1-b IdpClient cache + parallel + timeouts | auth/idp/, auth/__tests__/ | â€” |
| PR1-c split validateAndDispatch | auth/dispatch/, auth/__tests__/ | PR1-a (tests must exist first) |
| PR2-a AuthCache facade + composition root | auth/cache/, auth/bootstrap/ | PR1 merged |
| PR2-b AuthBroker | auth/broker/ | PR2-a |
| PR2-c SessionMint | auth/mint/ | PR2-a |
| PR2-d facade integration + E2E + delegation shim | auth/__tests__/integration/, e2e/auth/, auth/legacy/ | PR2-b, PR2-c |
| PR3 retire legacy | auth/legacy/, auth/__tests__/ | PR2 in production with parity |

Lanes:
- `Lane A: PR1-a â†’ PR1-c (sequential, shared auth/__tests__/ and tests-first ordering)`
- `Lane B: PR1-b (independent)`
- `Lane C: PR2-a (after PR1 merge)`
- `Lane D: PR2-b (after C)` and `Lane E: PR2-c (after C)` run in parallel
- `Lane F: PR2-d (after D + E)` then `PR3` sequential.

Execution order: launch A + B in parallel worktrees, merge both as PR1. Then C. Then
D + E in parallel worktrees, merge. Then F. Then PR3.

Conflict flags: Lanes A and B both add files under auth/__tests__/; keep test files
per module (legacy vs idp) to avoid merge conflicts. Lanes D and E both consume
`AuthCache` from C but touch disjoint directories; no conflict expected.

## Implementation Tasks
Synthesized from this review's findings. Each task derives from a specific
finding above. Run with Claude Code or Codex; checkbox as you ship.
Module paths are directory-level intent; the repo under review contains no source,
so exact file names are set at implementation time.

- [ ] **T1 (P1, human: ~1 day / CC: ~20 min)** â€” PR1 legacy auth â€” Write characterization (regression) tests pinning `legacyAuthFlow()` prior behavior before any rewrite
  - Surfaced by: Test review REGRESSION RULE â€” PLAN.md:27-28 rewrites legacyAuthFlow with no regression test
  - Files: auth/legacy/, auth/__tests__/
  - Verify: suite green against unmodified legacy path; 8 cases recorded as oracle
- [ ] **T2 (P1, human: ~1 day / CC: ~15 min)** â€” PR1 validateAndDispatch â€” Split into validate/authorize/dispatch stages returning a typed result; no catch swallows
  - Surfaced by: Code quality 3A â€” PLAN.md:23-24 three nested try/catch each swallowing an error class
  - Files: auth/dispatch/, auth/__tests__/
  - Verify: one unit test per result kind; logger spy asserts tenant + kind on every failure; T1 still green
- [ ] **T3 (P2, human: ~1 day / CC: ~20 min)** â€” PR1 IDP client â€” Classify the 5 IDP calls; TTL-cache static metadata by issuer; run per-token calls via `Promise.allSettled` with per-call `AbortSignal` timeout mapped to typed failures
  - Surfaced by: Performance 5A â€” PLAN.md:31-32 five sequential IDP calls
  - Files: auth/idp/, auth/__tests__/
  - Verify: timeout, 5xx, TTL hit/miss, latency-bound tests
- [ ] **T4 (P1, human: ~1 day / CC: ~20 min)** â€” PR2 AuthCache facade â€” Implement `AuthCache` as the single writer over the existing adapter: every method takes `tenantId`; `put` carries policy version + generation and is dropped after a newer invalidation for that key
  - Surfaced by: Architecture 1A + 2A â€” PLAN.md:10,19-20 unserialized mutations by two services on a shared cache
  - Files: auth/cache/
  - Verify: stale-generation put dropped; tenant-scoped get/put/invalidate tests
- [ ] **T5 (P1, human: ~half day / CC: ~10 min)** â€” PR2 composition root â€” Construct `AuthCache` once at the composition root and inject into `AuthBroker` and `SessionMint` constructors; remove the module-level export
  - Surfaced by: Architecture 1A â€” PLAN.md:19-20 module-level shared mutable export
  - Files: auth/bootstrap/, auth/broker/, auth/mint/
  - Verify: grep shows no module-level `AuthCache` export; both services unit-tested with a fake cache
- [ ] **T6 (P1, human: ~1 day / CC: ~20 min)** â€” PR2 facade tests â€” Integration tests: logout, revocation, suspension, expiry each visible through `AuthCache` reads; cross-tenant read rejected; mint/revoke interleaving in both orders never serves a revoked token
  - Surfaced by: Tests 4A + Architecture 2A â€” PLAN.md:12-16 adapter tests only, no facade-level coverage
  - Files: auth/__tests__/integration/
  - Verify: all 4 triggers + isolation + both interleavings green
- [ ] **T7 (P1, human: ~1 day / CC: ~20 min)** â€” PR2 E2E â€” Journeys with a fake IDP: loginâ†’okâ†’logoutâ†’denied; suspension mid-session; expiry mid-session; IDP unreachable yields clear error within timeout; double-submit login yields one session
  - Surfaced by: Tests 4A â€” no end-to-end auth journey in PLAN.md:14-16
  - Files: e2e/auth/
  - Verify: E2E suite green with flag on and off
- [ ] **T8 (P2, human: ~half day / CC: ~10 min)** â€” PR2 strangler fig â€” Make `legacyAuthFlow` delegate to the new pipeline behind a feature flag; T1 characterization tests pass against both paths
  - Surfaced by: Step 0 D4 scope reduction â€” strangler fig instead of big-bang rewrite
  - Files: auth/legacy/
  - Verify: T1 suite green with flag on and off
- [ ] **T9 (P2, human: ~half day / CC: ~10 min)** â€” PR3 retire legacy â€” Delete `legacyAuthFlow` and the delegation shim once parity holds in production; fold characterization tests into pipeline tests
  - Surfaced by: Step 0 D4 scope reduction â€” PR3
  - Files: auth/legacy/, auth/__tests__/
  - Verify: no references to legacyAuthFlow remain; full suite green
- [ ] **T10 (P3, human: ~30 min / CC: ~3 min)** â€” Post-plan-mode housekeeping â€” Create TODOS.md entries (TODO 1 RequestPolicy evaluation; TODO 2 IDP circuit breaker) and append gstack skill routing rules to CLAUDE.md, then commit
  - Surfaced by: D1, D10, D11 â€” writes deferred because plan mode permits editing only the plan file
  - Files: TODOS.md, CLAUDE.md
  - Verify: both files committed on a non-main branch or as directed

Tasks JSONL for `/autoplan`:
`~/.gstack/projects/gstack-plan-count-u2LYM3/tasks-eng-review-20260910-143141.jsonl` (10 tasks)

## TODOS.md entries (to create at implementation start, format per gstack TODOS-format)

### Decide RequestPolicy's fate after PR2
**What:** Audit what `RequestPolicy` (PLAN.md:35) was meant to hold; build it as a small pure module or close the idea.
**Why:** The scope reduction keeps it only if it carries logic beyond the adapter's existing policy-version key; without a note the intent is lost.
**Context:** PLAN.md names it with no description. The adapter already keys on policy version (PLAN.md:7). Start by listing every place a policy decision is made in `authorize()` after PR2.
**Effort:** S  **Priority:** P3  **Depends on:** PR2 merged

### IDP circuit breaker and backoff
**What:** Wrap per-token IDP calls in a breaker keyed by issuer with exponential backoff; serve a fast `idp_unavailable` while open.
**Why:** 5A bounds per-request latency but under a login spike with a degraded IDP every request still spends its full timeout budget and full call fan-out.
**Context:** PR1 lands per-call timeouts and typed failures, which is the hook a breaker needs. Tune thresholds from production latency after PR1.
**Effort:** M  **Priority:** P3  **Depends on:** PR1 merged; production latency data

## Decisions log

| ID | Question | Chosen | Completeness |
|---|---|---|---|
| D1 | Add gstack routing rules to CLAUDE.md | A: add (deferred to T10 by plan mode) | kind |
| D2 | Run /office-hours first | B: standard review | 7/10 |
| D3 | Cross-project learnings | A: enabled | kind |
| D4 | Scope: 12 files / 5 components | A: 3 sequenced PRs, one facade | kind |
| D5 | Issue 1 shared singleton | 1A: inject at composition root, tenant-scoped API | 10/10 |
| D6 | Issue 2 unserialized mutations | 2A: single writer, invalidation-wins | 10/10 |
| D7 | Issue 3 nested try/catch | 3A: typed stages | 10/10 |
| D8 | Issue 4 facade + E2E coverage | 4A: both | 10/10 |
| D9 | Issue 5 IDP calls | 5A: cache metadata + allSettled + timeouts | 10/10 |
| D10 | TODO 1 RequestPolicy | A: add | kind |
| D11 | TODO 2 circuit breaker | A: add | kind |

Durable decision ids: scope `bcaa148b-750a-45f0-a14e-254e3792a24a`, architecture `ed428d7c-ca2d-4e2c-bc71-738ad200d92a`.

## Completion summary

- Step 0: Scope Challenge â€” scope reduced per recommendation (3 PRs, TokenStore folded, RequestPolicy conditional)
- Architecture Review: 2 issues found (both resolved: 1A, 2A)
- Code Quality Review: 1 issue found (resolved: 3A)
- Test Review: diagram produced, 24 gaps identified (1 CRITICAL regression, 4 E2E); all added as requirements
- Performance Review: 1 issue found (resolved: 5A)
- NOT in scope: written
- What already exists: written
- TODOS.md updates: 2 items proposed to user, 2 accepted
- Failure modes: 2 critical gaps flagged in the original plan, both closed; 0 open
- Outside voice: skipped (codex_reviews disabled)
- Parallelization: 6 lanes, 2 parallel pairs (A+B, D+E) / rest sequential
- Lake Score: 5/5 recommendations chose complete option

## Review readiness dashboard

```
+====================================================================+
|                    REVIEW READINESS DASHBOARD                       |
+====================================================================+
| Review          | Runs | Last Run            | Status    | Required |
|-----------------|------|---------------------|-----------|----------|
| Eng Review      |  1   | 2026-09-10 14:31    | CLEAR (PLAN) | YES   |
| CEO Review      |  0   | â€”                   | â€”         | no       |
| Design Review   |  0   | â€”                   | â€”         | no       |
| Adversarial     |  0   | â€”                   | â€”         | no       |
| Outside Voice   |  1   | 2026-09-10 14:28    | SKIPPED (disabled) | no |
+--------------------------------------------------------------------+
| VERDICT: CLEARED â€” Eng Review passed                                |
+====================================================================+
```

Staleness: both entries record commit `1d48c77`, matching HEAD. No staleness notes.
Next steps: no UI scope, so no design review; a refactor, not a product change, so no
CEO review. All relevant reviews complete. Run /ship when ready.

## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/plan-ceo-review` | Scope & strategy | 0 | â€” | â€” |
| Outside Review | codex via `/plan-eng-review` (host: claude, phase: plan-review) | Independent 2nd opinion | 1 | disabled | skipped, codex_reviews disabled; no outside coverage |
| Eng Review | `/plan-eng-review` | Architecture & tests (required) | 1 | clean (SCOPE_REDUCED) | 6 issues, 0 critical gaps |
| Design Review | `/plan-design-review` | UI/UX gaps | 0 | â€” | â€” |
| DX Review | `/plan-devex-review` | Developer experience gaps | 0 | â€” | â€” |

- **OUTSIDE COVERAGE:** provider codex, phase plan-review, outside_status disabled (user config `codex_reviews=disabled`), no findings; no native fallback dispatched because disabled is a terminal opt-out. Re-enable: `gstack-config set codex_reviews enabled`.
- **VERDICT:** ENG CLEARED â€” ready to implement (PR1 first).

NO UNRESOLVED DECISIONS
