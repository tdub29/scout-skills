# Plan: Multi-tenant Auth Refactor (reviewed by /plan-eng-review, 2026-09-10)

Source plan: `PLAN.md` @ commit 974c858, branch `main`.
Review mode: SCOPE_REDUCED (complexity gate fired; reduction accepted in D1).
All seven decisions (D1â€“D7) were put to the user individually and resolved; each chose the
complete option. The remedies below are approved and folded in.

## Context

The original plan (PLAN.md) describes a refactor of the tenant-aware auth path: two new
services (`AuthBroker`, `SessionMint`) plus `TokenStore`, `AuthCache`, and `RequestPolicy`,
a rewrite of `legacyAuthFlow()`, and a change to how token validation talks to the identity
provider (IDP). It does not state the problem being solved, the success criteria, or how the
change reaches production. This reviewed plan keeps the original intent, records what the
review found, and folds the approved remedies in so implementation starts complete.

Auth is the highest-blast-radius code in a multi-tenant system: a wrong cache key is a
cross-tenant data leak, a swallowed error is a silent auth bypass or a silent outage. The
review is calibrated to that.

## Step 0: Scope Challenge

**Complexity check: TRIGGERED.** PLAN.md:35-36 says "touches 12 files and introduces 4 new
classes (TokenStore, SessionMint, AuthCache, RequestPolicy)". PLAN.md:19 adds `AuthBroker`
as a new service too, so it is 5 new types, not 4. The plan is internally inconsistent on
its own scope.

**What already exists (reuse check):**
- The existing cache adapter (PLAN.md:7-9) already keys by tenant ID, issuer, audience, and
  policy version, evicts expired tokens, and invalidates on logout / revocation / tenant
  suspension. Its invalidation hooks and tests stay in use unchanged (PLAN.md:12-13). Good.
- `AuthCache` is "a service-facing facade over that same existing adapter, with one backing
  cache" that "retains these unchanged validity and tenant-key rules" (PLAN.md:10-12). A facade
  that changes no rule and adds no serialization is a pass-through class. It is accidental
  complexity (Brooks). **Decision: dropped; inject the adapter directly.**
- `TokenStore` is never defined relative to the "one backing cache" (PLAN.md:12). If it is a
  second store of tokens, tenant-key rules now live in two places. If it is the adapter under
  another name, it is a duplicate. **Decision: define it against the one backing cache or merge
  it into the adapter; it does not ship as a separate token-holding class.**
- `legacyAuthFlow()` already works in production (PLAN.md:27). Its behavior is the
  specification the new path must match. The plan treated it as disposable; it is now the
  golden reference (see Tests).

**Minimum change that achieves the goal (ACCEPTED as D1 = 1A):** `AuthBroker` + `SessionMint`
taking the existing adapter by constructor injection, `RequestPolicy` as a pure policy
evaluator, the `validateAndDispatch()` cleanup, the IDP call change, all behind a per-tenant
flag. That is 3 new types instead of 5 and removes the two classes that carry the most
tenant-key risk.

**Search check** (Aside not installed; WebSearch used, read-only):
- **[Layer 1]** Module-level mutable singletons in Node are a known race and test-isolation
  hazard even single-threaded, because many requests are in flight against the same object;
  the standard remedy is factory / dependency injection. Sources:
  [Singleton pitfalls under load](https://dev-aditya.medium.com/the-singleton-pattern-in-node-js-power-pitfalls-and-performance-under-load-3d841ea5c226),
  [Singletons: tool or trap](https://blog.openreplay.com/singletons-javascript-tool-trap/),
  [Event loop and safe singletons](https://dev.to/devunionx/understanding-nodejs-the-event-loop-and-the-safe-use-of-singletons-fmn).
- **[Layer 1]** `Promise.all` is the built-in for the IDP fan-out; it fails fast, which is the
  correct all-or-nothing semantics for validation. `Promise.allSettled` is for partial-success
  cases, which auth is not. Sources:
  [MDN Promise.all](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all),
  [all vs allSettled](https://leapcell.io/blog/handling-multiple-api-requests-with-promise-all-and-promise-allsettled).
- **[Layer 1]** Catch-and-continue without surfacing is the documented "error hiding"
  anti-pattern; let errors bubble to one boundary that maps them to typed results. Sources:
  [Error hiding](https://en.wikipedia.org/wiki/Error_hiding),
  [TypeScript error handling pitfalls](https://www.dhiwise.com/post/typescript-error-handling-pitfalls-and-how-to-avoid-them).
- **[Layer 3 / EUREKA]** The plan's performance fix is "parallelize 5 calls". First-principles:
  in OIDC-style validation, several of those calls are usually discovery-document and JWKS
  fetches that change on the order of hours. The bigger win is making fewer calls (cache
  discovery + JWKS with TTL), then parallelizing what remains. See Performance #1. Logged to
  the eureka journal.

**TODOS.md:** does not exist in this repo. Nothing to cross-reference; one item is proposed
below (D7) and approved.

**Completeness check:** the plan took one explicit shortcut, "no regression test for the
prior behavior is planned" (PLAN.md:28) while its coverage "does not exercise
legacyAuthFlow() or assert compatibility with its prior behavior" (PLAN.md:15-16). With
CC+gstack a characterization suite is ~30 minutes. The REGRESSION RULE makes it mandatory
(see Tests). No decision was needed there.

**Distribution check:** no new artifact type (binary, package, image). Not applicable.

### Decision D1 (complexity gate) â€” RESOLVED: 1A Reduce
Drop the `AuthCache` facade and inject the adapter; define or merge `TokenStore`; ship 3 new
types (`AuthBroker`, `SessionMint`, `RequestPolicy`). Completeness 9/10. Not re-argued in
later sections.

## Architecture (reviewed)

### Data flow (target design)

```
 request(tenant, token)
        â”‚
        â–¼
 â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  flag OFF   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
 â”‚ per-tenant flag â”‚â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–¶â”‚ legacyAuthFlow() â”‚â”€â”€â–¶ response (unchanged)
 â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜             â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
        â”‚ flag ON
        â–¼
 â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
 â”‚ AuthBroker                                                  â”‚
 â”‚  validate(req) â”€â”€â–¶ RequestPolicy.evaluate(policyVersion)    â”‚
 â”‚      â”‚                      â”‚ allow / deny / unknown        â”‚
 â”‚      â”‚  cache miss          â–¼                               â”‚
 â”‚      â”œâ”€â”€â–¶ idpClient.validateAll(token)  [5 calls, parallel] â”‚
 â”‚      â”‚        â””â”€ discovery+JWKS from TTL cache              â”‚
 â”‚      â–¼                                                      â”‚
 â”‚  dispatch(result) â”€â”€â–¶ Ok | Denied | AuthError(class)        â”‚
 â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                 â”‚ reads only
                 â–¼
        â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   writes (single owner)   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
        â”‚ existing cache     â”‚â—€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”‚ SessionMint â”‚
        â”‚ adapter (injected) â”‚                           â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
        â”‚ key: tenant,issuer,â”‚â—€â”€â”€ invalidation hooks: logout / revoke / suspend
        â”‚ audience,policyVer â”‚
        â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### Cache write ordering (approved in D2)

```
  SessionMint.mint()            adapter                 revoke hook
  â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€           â”€â”€â”€â”€â”€â”€â”€                 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
  v = adapter.version(key) â”€â”€â”€â–¶ v=7
  ... IDP round trip ...
                                v=8  â—€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ invalidate(key)  (revocation)
  write(key, entry, ifVersion=7) â”€â–¶ REJECTED (7 â‰  8) â†’ mint returns Denied/re-validate
```

### Findings

**#1 [P1] (confidence: 8/10) PLAN.md:19-20 â€” global mutable `AuthCache` mutated by two services.**
Quoted: "share a global mutable `AuthCache` instance via module-level export. Both services
mutate it." Combined with PLAN.md:10 "they do not serialize mutations". Realistic production
failure: `SessionMint` writes a freshly minted entry while `AuthBroker` processes a revocation
for the same key. Without ordering, the revoked token is written back after the invalidation
and stays valid until expiry. Nothing in the original plan detects this. Second failure: test
files reset module caches differently (Jest/Vitest workers), so the singleton under test is not
the singleton the other file mutated, hiding the race in CI.

**Decision D2 â€” RESOLVED: 2A.** Constructor-inject one cache instance from a composition root
(`src/auth/composition.ts`); `SessionMint` is the only writer, `AuthBroker` is read-only;
invalidation goes through the existing hooks; writes carry the version they started from and
are rejected if an invalidation landed in between (diagram above). One shared key builder.
Completeness 10/10. Maps to: explicit over clever; DRY.

**#2 [P1] (confidence: 8/10) PLAN.md:27 â€” no rollout path for replacing `legacyAuthFlow()`.**
Quoted: "The existing `legacyAuthFlow()` will get rewritten as part of this work". No flag,
canary, or rollback anywhere in the plan. Realistic failure: one tenant's IDP returns a claim
shape the new path rejects; every request for that tenant fails at once, with no switch back.

**Decision D3 â€” RESOLVED: 3A.** Per-tenant feature flag with a global kill switch; keep
`legacyAuthFlow()` callable until the flag is at 100% for two weeks, then delete flag and
legacy path in a follow-up PR. The characterization suite (Tests) is the parity gate: both
flag states must pass it. Completeness 10/10. Reversibility preference; strangler fig.

**#3 [P2] (confidence: 6/10) PLAN.md:35 â€” `TokenStore` relationship to the single backing cache undefined.**
Medium confidence. Quoted: "one backing cache" (PLAN.md:12) alongside a new `TokenStore` class
(PLAN.md:35). If `TokenStore` holds tokens outside the adapter, tenant-key isolation is
duplicated and the adapter's invalidation hooks do not reach it: suspend a tenant and its
tokens survive in `TokenStore`. **Resolved by D1**: define against the one backing cache or
merge.

**Security architecture:** tenant isolation depends entirely on the adapter's composite key.
Every write path builds keys through one shared key builder. A test asserts that a token
minted for tenant A is rejected on a tenant B request with identical issuer/audience.

**Distribution architecture:** none, no new artifact.

## Code quality (reviewed)

**#1 [P1] (confidence: 9/10) PLAN.md:23-24 â€” `validateAndDispatch()` swallows three error classes.**
Quoted: "60 lines with three nested try/catch blocks; each catch swallows a different error
class." Textbook error hiding. Failure the user sees: an IDP outage, a malformed token, and a
policy-engine bug all look identical from outside, or worse, look like success.

**Decision D4 â€” RESOLVED: 4A.** Split into `validate()` (pure: token + policy â†’ typed result)
and `dispatch()` (side effects). One error boundary maps each error class to a discriminated
union `Ok | Denied | AuthError<kind>`, logs it with tenant + kind, and returns an explicit
response. No catch block exits without either rethrowing or producing a typed value. Callers
that relied on the swallow are updated to handle the explicit error. Completeness 10/10.
Explicit over clever; one boundary instead of three is DRY.

**#2 [P2] (confidence: 7/10) PLAN.md:19-20 vs 35 â€” DRY: two writers, two key builders, and an inconsistent class list.**
Two services mutating the same cache means cache-write and key-construction code exists twice.
Remedy is included in D2 (single writer, one key builder). The "4 new classes" list omitting
`AuthBroker` is corrected in this document (5 types as written, 3 after D1).

**Diagrams:** the plan had none. This document adds the request-flow and write-ordering
diagrams above. In code: `AuthBroker` gets the request-flow diagram as a header comment,
`SessionMint` gets the mint / invalidate ordering diagram, and the cache adapter gets a
key-shape + invalidation-trigger diagram. No existing ASCII diagrams were found to go stale
(no source in this repo).

## Tests (reviewed)

Test framework: none detected in this repo (0 test files, no `package.json`). Coverage
requirements are stated as plan items; file names assume a TypeScript `*.test.ts` convention
and should be adjusted to the target repo's layout.

### REGRESSION RULE (mandatory, no decision required)
`legacyAuthFlow()` is existing behavior being rewritten (PLAN.md:27-28) with no covering
test (PLAN.md:15-16, 28). **CRITICAL:** before any rewrite, record a characterization suite
in `tests/auth/legacyAuthFlow.regression.test.ts`: for each supported tenant configuration,
capture inputs (token, tenant, policy version, IDP responses) and the exact output (status,
claims, cache side effects, error shape). The new path must pass the same suite with the
flag on. This is the parity gate for D3.

### Coverage diagram (state of the original plan)

```
CODE PATHS                                                    USER FLOWS
[+] src/auth/AuthBroker.ts                                    [+] Login â†’ mint â†’ first authed request
  â”œâ”€â”€ validate()                                                â””â”€â”€ [GAP] [â†’E2E] per tenant, two tenants same run
  â”‚   â”œâ”€â”€ [GAP] valid token + policy allow                     [+] Logout â†’ retry last request
  â”‚   â”œâ”€â”€ [GAP] error class 1 surfaced (typed, logged)           â””â”€â”€ [GAP] [â†’E2E] expect 401, no cached success
  â”‚   â”œâ”€â”€ [GAP] error class 2 surfaced                         [+] Tenant suspended mid-session
  â”‚   â”œâ”€â”€ [GAP] error class 3 surfaced                           â””â”€â”€ [GAP] [â†’E2E] next request rejected, others unaffected
  â”‚   â””â”€â”€ [GAP] IDP partial failure (1 of 5 rejects/times out)  [+] Token expires mid-session
  â””â”€â”€ dispatch()                                                â””â”€â”€ [GAP] re-mint or clear re-login, never stale success
      â”œâ”€â”€ [GAP] tenant isolation (A's token on B's request)    [+] Two tabs / concurrent requests
      â””â”€â”€ [GAP] revoke-during-mint: revoked token not revived    â””â”€â”€ [GAP] no duplicate mint, no lost invalidation
[+] src/auth/SessionMint.ts                                   [+] IDP slow (10 s on one call)
  â”œâ”€â”€ [GAP] mint() happy path writes one keyed entry            â””â”€â”€ [GAP] user sees timeout error, not a hang
  â””â”€â”€ [GAP] mint() when IDP unreachable â†’ typed error         [+] Flag OFF â†’ legacy parity
[+] src/auth/RequestPolicy.ts                                   â””â”€â”€ [GAP] [â†’E2E] identical to golden recording
  â”œâ”€â”€ [GAP] allow
  â”œâ”€â”€ [GAP] deny
  â””â”€â”€ [GAP] unknown / bumped policy version â†’ old entries not served
[+] existing cache adapter (unchanged)
  â””â”€â”€ [â˜…â˜…â˜… TESTED] eviction + logout/revoke/suspend invalidation â€” existing suite
[+] legacyAuthFlow() rewrite
  â””â”€â”€ [GAP] [CRITICAL] characterization suite (REGRESSION RULE)

COVERAGE: 1/21 paths tested (5%)  |  Code paths: 1/14 (7%)  |  User flows: 0/7 (0%)
QUALITY: â˜…â˜…â˜…:1 â˜…â˜…:0 â˜…:0  |  GAPS: 20 (4 E2E, 0 eval, 1 CRITICAL regression)
```

Legend: â˜…â˜…â˜… behavior + edge + error | â˜…â˜… happy path | â˜… smoke check | [â†’E2E] integration test

**Decision D5 â€” RESOLVED: 5A.** All 19 non-regression gaps close in this PR: unit tests plus
the four E2E journeys against a fake IDP fixture. Target after implementation: 21/21.
Completeness 10/10.

### Test requirements (all in scope)
- `tests/auth/legacyAuthFlow.regression.test.ts` â€” CRITICAL golden characterization, flag off
  and flag on must both pass.
- `tests/auth/AuthBroker.test.ts` â€” validate() allow; each of the 3 error classes yields its
  typed variant and a log line with tenant + kind; 1-of-5 IDP rejection and 1-of-5 timeout both
  fail closed within the request budget.
- `tests/auth/tenantIsolation.test.ts` â€” token for tenant A with identical issuer/audience is
  rejected for tenant B; key builder output differs only by tenant.
- `tests/auth/cacheOrdering.test.ts` â€” start mint, fire revoke, complete mint: cache holds no
  valid entry (write-version check rejects the late write).
- `tests/auth/SessionMint.test.ts` â€” one keyed write per mint; IDP unreachable â†’ typed error,
  no cache write.
- `tests/auth/RequestPolicy.test.ts` â€” allow, deny, unknown version, version bump does not
  serve prior entries.
- `tests/auth/idpClient.test.ts` â€” warm cache makes â‰¤2 network calls; unknown kid triggers
  JWKS refetch once; per-call timeout aborts and surfaces a typed error.
- `tests/e2e/auth.e2e.ts` â€” loginâ†’requestâ†’logout per tenant; suspend tenant; flag-off parity;
  slow-IDP timeout is visible to the user.

QA test plan artifact written to
`~/.gstack/projects/gstack-plan-count-RacHBI/vercel-sandbox-main-eng-review-test-plan-20260910-153621.md`
for `/qa` and `/qa-only`.

## Performance (reviewed)

**#1 [P2] (confidence: 8/10) PLAN.md:31-32 â€” five sequential IDP calls.**
Quoted: "Token validation issues 5 sequential API calls to the IDP; they could be parallelized
via Promise.all trivially (calls are independent)." Parallelizing is correct and `Promise.all`
fail-fast is the right semantics for validation. "Trivially" hides two things: (1) five
concurrent calls per request multiplies IDP burst load by 5 and can trip provider rate limits
under a login storm; (2) no per-call timeout means one slow call still hangs the request.
**[EUREKA]** the larger win is fewer calls: discovery and JWKS documents are cached with TTL so
the hot path is typically one or two network calls.

**Decision D6 â€” RESOLVED: 6A.** `Promise.all` + per-call timeout (AbortSignal) + TTL cache for
discovery/JWKS with refetch-on-unknown-kid + a metric on IDP call count per validation.
Completeness 10/10. Built-ins only, no new dependency.

No N+1 or memory concern found: one backing cache, keyed entries, existing eviction.

## Failure modes (per new codepath)

| Codepath | Realistic failure | Test (after this plan) | Handling (after this plan) | User sees | Critical gap in original? |
|---|---|---|---|---|---|
| SessionMint write vs revoke | Revoked token written back after invalidation | cacheOrdering.test.ts | write-version check rejects late write (D2) | mint re-validates or Denied | **YES â†’ closed** |
| validateAndDispatch catch blocks | IDP outage classed as generic failure or success | 3 error-class tests | typed boundary, logged with kind (D4) | distinct explicit error | **YES â†’ closed** |
| legacyAuthFlow rewrite | Claim-shape difference for one tenant | characterization suite (mandatory) | per-tenant flag + kill switch (D3) | flag flip, no outage | **YES â†’ closed** |
| IDP fan-out | One of five calls hangs | idpClient timeout test | AbortSignal timeout (D6) | timeout error within budget | no |
| TokenStore (if separate) | Suspend does not reach it | suspend E2E | merged into adapter (D1) | session rejected | resolved by D1 |
| RequestPolicy version bump | Old entries served | RequestPolicy.test.ts | key includes version (existing) | none | no |

Critical gaps flagged in the original plan: **3**. All three are closed by approved remedies
(D2, D4, D3 + mandatory regression suite). Remaining critical gaps in this reviewed plan: 0.

## NOT in scope
- Deleting `legacyAuthFlow()` and the flag â€” follow-up PR after the flag has been 100% for two
  weeks (D3).
- Replacing the existing cache adapter â€” it works, is keyed correctly, and is tested; reuse it.
- Repo-wide dependency-injection composition â€” only the auth composition root is in scope;
  broader adoption is the approved TODO (D7).
- `AuthCache` facade and a standalone `TokenStore` â€” cut in D1.
- IDP provider change or protocol migration â€” unrelated to this refactor.
- Distribution / packaging â€” no new artifact.

## What already exists
- Existing cache adapter with tenant/issuer/audience/policy-version keys, eviction, and
  invalidation hooks + tests (PLAN.md:7-13): **reused as-is**, injected directly (D1, D2).
- `legacyAuthFlow()` (PLAN.md:27): **becomes the specification** via the characterization suite
  and stays live behind the flag (D3).
- Invalidation hooks for logout / revoke / suspend (PLAN.md:8-9): **reused**; the single-writer
  design routes through them instead of adding a second invalidation path.

## Worktree parallelization strategy

| Step | Modules touched | Depends on |
|---|---|---|
| S1 Regression characterization suite | tests/auth/ | â€” |
| S2 Composition root + single-writer cache wiring + write-version check | src/auth/ (AuthBroker, SessionMint, composition) | â€” |
| S3 validateAndDispatch split + typed errors | src/auth/AuthBroker, src/auth/errors | S2 (injection shape) |
| S4 Feature flag + rollout | src/auth/flags, src/auth/AuthBroker | S2 |
| S5 IDP client: parallel + timeout + TTL cache | src/auth/idpClient | â€” |
| S6 Unit tests for new paths | tests/auth/ | S2, S3, S5 |
| S7 E2E journeys + fake IDP | tests/e2e/ | S4 |

Lane A: S1 (independent, tests/auth/)
Lane B: S2 â†’ S3 â†’ S4 (sequential, shared src/auth/)
Lane C: S5 (independent, src/auth/idpClient only)
Then: S6 and S7 in parallel after A, B, C merge.

Execution: launch A + B + C in parallel worktrees. Merge. Then S6 âˆ¥ S7.
Conflict flag: Lanes B and C both live under `src/auth/`; C touches only `idpClient`, so
conflicts are unlikely, but rebase C onto B before merge.

## Implementation Tasks
Synthesized from this review's findings. Each task derives from a specific finding above and
an approved decision. Run with Claude Code or Codex; checkbox as you ship.

- [ ] **T1 (P1, human: ~1 day / CC: ~30 min)** â€” tests/auth â€” Write the `legacyAuthFlow()` characterization (regression) suite before any rewrite
  - Surfaced by: Tests â€” REGRESSION RULE, PLAN.md:27-28
  - Files: tests/auth/legacyAuthFlow.regression.test.ts
  - Verify: suite green on current code; green again with flag on after rewrite
- [ ] **T2 (P1, human: ~1 day / CC: ~20 min)** â€” src/auth â€” Replace module-level `AuthCache` export with constructor injection and a single cache writer with write-version check
  - Surfaced by: Architecture #1, PLAN.md:19-20 (D2 = 2A)
  - Files: src/auth/AuthBroker.ts, src/auth/SessionMint.ts, src/auth/composition.ts
  - Verify: tests/auth/cacheOrdering.test.ts; grep shows no module-level cache export
- [ ] **T3 (P1, human: ~4 h / CC: ~15 min)** â€” src/auth â€” Split `validateAndDispatch()` into `validate()` and `dispatch()` with one typed error boundary
  - Surfaced by: Code quality #1, PLAN.md:23-24 (D4 = 4A)
  - Files: src/auth/AuthBroker.ts, src/auth/errors.ts
  - Verify: three error-class tests in tests/auth/AuthBroker.test.ts; no catch without rethrow or typed return
- [ ] **T4 (P1, human: ~4 h / CC: ~15 min)** â€” src/auth â€” Per-tenant feature flag with kill switch; keep `legacyAuthFlow()` callable
  - Surfaced by: Architecture #2 (D3 = 3A)
  - Files: src/auth/flags.ts, src/auth/AuthBroker.ts
  - Verify: flag-off parity E2E; flag-on passes T1 suite
- [ ] **T5 (P1, human: ~1 day / CC: ~30 min)** â€” tests/auth â€” Tenant-isolation, revoke-during-mint, error-class surfacing, IDP partial-failure, policy-version tests
  - Surfaced by: Tests â€” coverage diagram, 20 gaps, 3 critical (D5 = 5A)
  - Files: tests/auth/AuthBroker.test.ts, tests/auth/SessionMint.test.ts, tests/auth/tenantIsolation.test.ts, tests/auth/RequestPolicy.test.ts, tests/auth/idpClient.test.ts
  - Verify: coverage diagram code paths 14/14
- [ ] **T6 (P2, human: ~4 h / CC: ~15 min)** â€” src/auth/idpClient â€” `Promise.all` + per-call timeout + TTL cache for discovery/JWKS, refetch on unknown kid, call-count metric
  - Surfaced by: Performance #1, PLAN.md:31-32 (D6 = 6A)
  - Files: src/auth/idpClient.ts
  - Verify: 1-of-5 timeout test fails closed within budget; metric shows â‰¤2 calls on warm cache
- [ ] **T7 (P2, human: ~2 h / CC: ~10 min)** â€” src/auth â€” Drop the `AuthCache` facade; define `TokenStore` against the one backing cache or merge it into the adapter
  - Surfaced by: Step 0 complexity check, PLAN.md:11-13, 35-36 (D1 = 1A)
  - Files: src/auth/AuthCache.ts (delete), src/auth/TokenStore.ts (define or delete)
  - Verify: new-type count is 3; suspend-tenant E2E rejects the session
- [ ] **T8 (P2, human: ~1 h / CC: ~5 min)** â€” src/auth â€” ASCII request-flow and write-ordering diagrams as header comments
  - Surfaced by: Required outputs â€” Diagrams
  - Files: src/auth/AuthBroker.ts, src/auth/SessionMint.ts, cache adapter
  - Verify: diagrams match the flow in this document
- [ ] **T9 (P2, human: ~1 day / CC: ~30 min)** â€” tests/e2e â€” loginâ†’requestâ†’logout, tenant suspend, flag-off parity, slow-IDP journeys with a fake IDP
  - Surfaced by: Tests â€” user flows marked [â†’E2E] (D5 = 5A)
  - Files: tests/e2e/auth.e2e.ts, tests/e2e/fakeIdp.ts
  - Verify: 4 E2E journeys green in CI

Tasks JSONL: `~/.gstack/projects/gstack-plan-count-RacHBI/tasks-eng-review-20260910-153621.jsonl` (9 tasks).

## TODOS.md (approved item, D7 = 7A)

Plan mode forbids editing repo files other than the plan, so TODOS.md is created at
implementation start with this entry (format per gstack TODOS-format):

### Adopt a composition-root / DI pattern for auth-adjacent services

**What:** Extend the composition root introduced for `AuthBroker` / `SessionMint` to the other
services that currently import shared mutable state at module level.

**Why:** The singleton race found in Architecture #1 likely exists elsewhere; one pattern
repo-wide keeps the fix from being a one-off.

**Context:** Start from `src/auth/composition.ts` once T2 lands; grep for module-level
`export const` of mutable objects to size the work. Pros: testable services, no hidden
coupling, one place to see the object graph. Cons: touches files outside the auth refactor; a
migration, not a patch.

**Effort:** M
**Priority:** P2
**Depends on:** T2

## Outside voice
Codex review skipped (codex_reviews disabled). Re-enable: `gstack-config set codex_reviews enabled`.
No outside coverage this run; logged as `outside_status: disabled`. No Claude-subagent
fallback was dispatched, per the disabled branch. No cross-model tension to report.

## Retrospective learning
Git history is a single seed commit (974c858). No prior review cycle to compare against.

## Next steps
Backend-only change, no UI surface: `/plan-design-review` not applicable. Refactor, not a
product-direction change: `/plan-ceo-review` optional and not suggested. All relevant reviews
complete. Run /ship when ready.

## Completion summary
- Step 0: Scope Challenge â€” scope reduced per recommendation (5 â†’ 3 new types, D1 = 1A)
- Architecture Review: 3 issues found (2 P1, 1 P2), all resolved (D2 = 2A, D3 = 3A, #3 via D1)
- Code Quality Review: 2 issues found (1 P1, 1 P2), all resolved (D4 = 4A, #2 via D2)
- Test Review: diagram produced, 20 gaps identified (1 CRITICAL regression, mandatory); all 20 in scope (D5 = 5A)
- Performance Review: 1 issue found (P2, with a fewer-calls eureka), resolved (D6 = 6A)
- NOT in scope: written
- What already exists: written
- TODOS.md updates: 1 item proposed, approved (D7 = 7A)
- Failure modes: 3 critical gaps flagged in the original plan, 3 closed by approved remedies, 0 remaining
- Outside voice: skipped (codex_reviews disabled)
- Parallelization: 3 lanes, 3 parallel then 2 parallel test lanes
- Lake Score: 7/7 recommendations chose the complete option
- Session setup items (not issue approvals, deferred to next healthy run): gstack CLAUDE.md routing rules, cross-project learnings preference
- Durable learning logged: this repo is a fixture with only CLAUDE.md and PLAN.md; findings are evidenced by PLAN.md line quotes, no source or test framework to verify against

Review log written (`plan-eng-review`, status clean, unresolved 0, critical_gaps 0,
issues_found 26, mode SCOPE_REDUCED, commit 974c858). Decision log written. Telemetry
(`gstack-skill-end`, outcome success) run.

## GSTACK REVIEW REPORT

| Review | Trigger | Why | Runs | Status | Findings |
|--------|---------|-----|------|--------|----------|
| CEO Review | `/plan-ceo-review` | Scope & strategy | 0 | â€” | â€” |
| Outside Review | codex via `/plan-eng-review` (plan-review phase) | Independent 2nd opinion | 1 | disabled | skipped, no outside coverage |
| Eng Review | `/plan-eng-review` | Architecture & tests (required) | 2 | clean (PLAN) | 26 issues, 0 critical gaps remaining (3 flagged, 3 closed); 7/7 decisions resolved |
| Design Review | `/plan-design-review` | UI/UX gaps | 0 | â€” | â€” |
| DX Review | `/plan-devex-review` | Developer experience gaps | 0 | â€” | â€” |

**OUTSIDE COVERAGE:** provider codex, phase plan-review, outside_status disabled (user setting `codex_reviews=disabled`), 0 findings; native fallback not dispatched. Host claude.

**VERDICT:** ENG CLEARED â€” ready to implement (scope reduced to 3 new types; all remedies approved and folded in).

NO UNRESOLVED DECISIONS
