---
name: combinatorial-arb-detector
description: Detect and exploit multi-condition / dependent-market arbitrage on Polymarket using the Bregman projection + Frank-Wolfe + integer programming framework that extracted $40M from prediction markets in 2024-2025. Use this skill whenever the user mentions Bregman divergence, Frank-Wolfe, marginal polytope, integer programming for arbitrage, dependent markets, multi-condition mispricing, "sum of YES + NO â‰  1", LMSR cost functions, KL divergence between price vectors, or wants to detect arbitrage that simple pairwise checks miss. Also trigger for references to gabagool22's strategy, the $40M arXiv paper (2508.03474), Gurobi for prediction-market optimization, or questions like "why does my naive arb scanner miss real arb" â€” the answer is that real arb lives in the multi-condition dependency structure, not in single-market price sums.
---

# Combinatorial Arbitrage Detector (Polymarket)

Most retail "arb scanners" check whether YES + NO â‰ˆ $1 on a single market. That catches the cheapest opportunities and misses the structural ones. The traders extracting seven figures are solving a different problem: **find price vectors that lie outside the marginal polytope of the joint outcome space across multiple correlated markets**, then compute the optimal trade that projects the market back onto that polytope.

This skill is the bridge between the math in [math.md](../../../math.md) and a working detector. It's deliberately heavier on theory than the other skills in this project because the math *is* the edge here â€” without it you're just running a slower version of what every retail bot already does.

## What problem are we actually solving

Given a set of related markets with prices Î¸ (a vector in [0,1]^n), the question is:

> Does there exist a trade vector d such that for every possible outcome Ï‰, the payoff dÂ·Ï†(Ï‰) âˆ’ C(Î¸+d) + C(Î¸) is strictly positive?

If yes, that's guaranteed arbitrage. The maximum extractable profit equals the **Bregman divergence** D(Î¼*â€–Î¸), where Î¼* is the projection of Î¸ onto the marginal polytope M, and D is the divergence induced by the market maker's cost function C (for LMSR, that's KL divergence).

Two parts:

1. **Detection** â€” is Î¸ outside M? (an integer feasibility problem)
2. **Exploitation** â€” what's Î¼*? (a Bregman projection, which Frank-Wolfe makes tractable)

## Pipeline

### Stage 1 â€” Find candidate dependent market sets

You can't run the full optimization on every pair of markets â€” the search space is too large (305 election markets â†’ 46,360 pairs). Pre-filter:

- **Logical containment** â€” "X wins by 5+" implies "X wins". The wider market caps the narrower one.
- **Mutual exclusion** â€” "X wins" and "Y wins" can't both be true if X and Y compete in the same race.
- **Conditional implications** â€” "Trump wins PA" + "GOP wins Senate" + "Trump wins presidency" form a constraint graph.

The research paper used DeepSeek-R1-Distill-Qwen-32B to extract these from market descriptions at 81% accuracy. Claude itself can do this directly for small market sets â€” the job is producing a JSON that lists the valid joint outcomes and which condition is TRUE in each. If the count of valid outcomes is less than the cartesian product, dependency exists and the set is a candidate.

### Stage 2 â€” Encode the marginal polytope

For a candidate set with binary indicator variables z_i âˆˆ {0,1}, encode the valid outcome set Z as integer constraints:

```
Z = { z âˆˆ {0,1}^I : A^T z â‰¥ b }
```

Three concrete examples (from [math.md](../../../math.md)):

```
# Each market resolves to exactly one outcome
sum(z[duke, 0..6]) = 1
sum(z[cornell, 0..6]) = 1

# Mutual exclusion via tournament structure
z[duke, 5] + z[duke, 6] + z[cornell, 5] + z[cornell, 6] â‰¤ 1
```

The marginal polytope is M = conv(Z). You never enumerate Z explicitly â€” that's the whole point.

### Stage 3 â€” Test if Î¸ âˆˆ M (cheap path)

Before running Frank-Wolfe, run the cheap check first: solve the LP relaxation. Drop the integrality constraints and check whether Î¸ is feasible. If the LP says infeasible, no arbitrage exists. If feasible at the LP level but the IP would be infeasible, you need Stage 4.

In practice, the LP relaxation catches > 90% of negatives in milliseconds.

### Stage 4 â€” Bregman projection via Frank-Wolfe

When the LP can't decide, run the Frank-Wolfe loop with an IP oracle:

```
Z_0 = {initial vertex(es)}
for t = 1, 2, ...:
    Î¼_t = argmin over conv(Z_{t-1}) of F(Î¼)         # convex sub-problem
    z_t = argmin over Z of âˆ‡F(Î¼_t)Â·z                # IP, the expensive call
    Z_t = Z_{t-1} âˆª {z_t}
    g_t = âˆ‡F(Î¼_t) Â· (Î¼_t âˆ’ z_t)
    if g_t â‰¤ Îµ: break
```

For LMSR, F(Î¼) is the negative-entropy-induced KL divergence. âˆ‡F(Î¼) blows up as any coordinate approaches 0 â€” use the **Barrier Frank-Wolfe** variant with adaptive contraction:

```
M' = (1 - Îµ)Â·M + ÎµÂ·u    # u is the interior point with all coords in (0,1)
```

The research paper used Gurobi 5.5 with these parameters:

- alpha = 0.9 (extract â‰¥90% of available arb)
- initial epsilon = 0.1
- convergence threshold = 1e-6
- time limit = 30 minutes (relax as the outcome space shrinks)

Typical convergence: 50â€“150 iterations on real markets.

### Stage 5 â€” Validate against execution reality

A Bregman-optimal trade on paper isn't profitable if the order book can't absorb it. Before recommending execution:

- Compute **VWAP per leg** assuming you sweep the visible book at current depth
- Apply the rule: `actual_profit = (price_deviation Ã— min_volume_across_legs) âˆ’ fees âˆ’ gas`
- Reject if `actual_profit < 0.05` per dollar (the research's empirical execution-risk threshold)

For full execution mechanics, see [math.md](../../../math.md) Part IV ("Execution Under Non-Atomic Constraints"). The **non-atomic problem** is the killer: one leg fills, you submit the next, the market's already moved. Either submit all legs in the same block via direct RPC, or build an alternate flow that uses split/merge atomically through the Conditional Tokens Framework.

## Tooling notes

| Stage | Tool | Notes |
|-------|------|-------|
| Dependency extraction | Claude itself, or DeepSeek-R1-Distill-Qwen | Verify a sample by hand before trusting at scale |
| LP relaxation | `scipy.optimize.linprog` or PuLP | Fast enough for ~1000 conditions |
| IP oracle | **Gurobi** (free academic license, paid commercial), or `mip`/CBC for prototyping | Gurobi is roughly 10-100Ã— faster for non-trivial problems |
| Bregman projection | Custom Frank-Wolfe loop â€” there's no off-the-shelf library that does this for prediction markets | Reuse the loop pseudocode above; it's < 100 lines |
| Market data | `grimoire-polymarket` skill or `polymarket-api` skill | Get current order books and clob_token_ids |
| Historical validation | `SII-WANGZJ/Polymarket_data` (referenced in `github-resources.md`) | 1.1B trade records for backtesting your detector |

## When this skill helps and when it doesn't

**Use this skill when:**

- The user asks why their simple arb scanner finds nothing while traders are extracting millions
- Detecting cross-market dependencies that the eye misses (election market hierarchies, tournament brackets, conditional events)
- Sizing the optimal trade given a detected mispricing
- Understanding the math behind a paper or a trader profile (gabagool22, etc.)

**Don't use this skill for:**

- Single-market `YES+NO â‰  $1` checks â€” that's a 5-line script, no projection needed
- Latency arb â€” that's `chainlink-latency-arb`, a totally different edge
- Generic CLOB integration â€” `polymarket-api` covers it
- Live execution wiring â€” once you have Î¼*, the execution step is its own problem (and falls under `bot-ops-review` for risk controls)

## Sanity checks before running on real markets

The math is unforgiving. A bug in the constraint matrix or the cost-function gradient can produce trades that look profitable on paper and lose money on every outcome. Before any live trade:

1. **Verify on a known case.** Take the Duke vs Cornell example from [math.md](../../../math.md). Hand-construct the polytope. Confirm your IP solver returns the same valid outcome count (3, not 4).
2. **Reproduce a published result.** The arXiv paper (2508.03474) gives concrete numbers for the 2024 election period. Pick one of the 13 manually-verified pairs and reproduce the profit estimate.
3. **Paper-trade for a week.** Run the detector live, log proposed trades, but don't execute. Compare against the realized resolutions. If your detector says "guaranteed profit â‰¥ $0.10" and the realized P/L is negative, there's a bug â€” find it before risking capital.

## Failure modes

- **Numerical instability near polytope boundaries.** Îµ-contraction handles this in theory; in practice, watch for NaN/Inf in the gradient.
- **IP oracle timeouts.** Early iterations on large markets can take > 30s. Make the time limit configurable and have a graceful fallback to "skip this iteration".
- **Stale market data.** Order books move while you optimize. The freshness budget is the time it takes to compute Î¼* + submit all legs. If that exceeds the typical book half-life on the target markets, the trade dies on submission.
- **Capital efficiency.** With < $50K bankroll, gas + slippage eat most of the edge. The research's $0.05 minimum threshold exists for a reason â€” see [math.md](../../../math.md) Part IV's capital-efficiency discussion.
