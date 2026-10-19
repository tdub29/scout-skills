---
name: fitschen-trade-like-it-backtests
description: Run a Build-Rebuild-and-Compare (BRAC) robustness gate on a backtested trading strategy before trading it live. Use when someone says a strategy "looks great in the backtest," asks whether it's curve-fit, wants a pass/fail check before risking real money, wants to estimate curve-fitting without sacrificing data to a holdout, is scoring/ranking setups (bar-scoring), or is about to trust a single chart/anecdote as proof of an edge. Triggers include "will this trade the same live as it backtested," "run a BRAC test," "is this over-optimized," "out-of-sample without wasting data," "pass/fail gate for a backtested edge," "develop a strategy so real-time matches the backtest."
---

# Trade Like It Back-Tests (BRAC)

## What this decides

Whether a backtested strategy is **safe to trade live as-is**, or is **curve-fit
and must be discarded/reworked** â€” using a method that produces its own
performance reference, unlike a naive train/test holdout that just throws
data away and tells you nothing to compare against.

## When to use

- Before committing capital to any backtested system, rule, filter, or
  parameter choice.
- Before trusting a bar-scoring / ranking model's edge (Ch. 8 extension).
- Before trusting a single compelling chart or trade example as evidence of
  an edge (Ch. 9 extension) â€” anecdotes get restated as testable rules and
  run through this same gate.
- At every point in development where you're tempted to add a rule, a
  filter, or a stop because it "improved the numbers."

Not for: strategies with no historical data to rebuild from, or one-off
discretionary trades with no rule set to re-derive.

## Method: Build, Rebuild, and Compare (BRAC)

1. **Build.** Develop the strategy on ALL available historical data. Write
   down every step in order: every parameter swept, every range tested, and
   the exact selection rule used at each step (e.g., "vary moving-average
   length 10â€“120 by 10, pick the value with highest net profit"). This log
   is not optional â€” step 2 depends on reproducing it exactly.
2. **Withhold a slice.** Cut a meaningful trailing chunk off the end of the
   data (Fitschen used the most recent 1 year off ~20+ years of daily bars â€”
   scale proportionally, but keep it recent and keep it a real chunk, not a
   token few trades).
3. **Rebuild.** Re-run the IDENTICAL steps and selection logic from step 1
   on the truncated (withheld-slice-removed) data. This is not a fresh
   optimization pass â€” same parameter grids, same "pick the max" rule, same
   order of operations. If you can't reproduce the exact steps, step 1 was
   under-documented; go back and log it properly.
4. **Compare.** Run the REBUILT strategy (with its own parameters, derived
   from the smaller dataset) forward through the withheld slice. Compare its
   performance over that slice against the ORIGINAL strategy's performance
   over the same slice.
   - **Similar performance** (parameter values match or performance
     magnitude/shape tracks) â†’ confidence the strategy is not materially
     curve-fit. Trade it.
   - **Divergent performance** (parameters swing wildly, or rebuilt
     performance collapses/inverts on the withheld slice) â†’ the edge is an
     artifact of the full-data fit. Discard or rework â€” do not trade it,
     and do not just re-tune and re-test the same slice (that's re-fitting
     to the "test" set).
5. **Record the verdict** alongside the strategy: BRAC pass/fail, the
   withheld-slice performance numbers on both builds, and the date. This
   becomes your curve-fit estimate â€” you didn't need a separate,
   data-wasting holdout to get it.

## Sub-rules and failure modes

- **BRAC gives you a performance reference; a plain out-of-sample holdout
  does not.** A holdout split before any building means you have no
  matching in-sample number to compare the holdout result against â€” you
  can't tell if a mediocre holdout result is normal variance or a broken
  system. BRAC's rebuild step manufactures that reference for free, on data
  you still get to use in the final (all-data) strategy.
- **The log from step 1 must be literal, not remembered.** "I think I tried
  10â€“120 by 10 and picked the best" is not a rebuild spec. Write the actual
  ranges, increments, and selection criteria as you go, not after the fact
  from memory â€” an approximate rebuild produces an uninformative compare.
- **Don't re-tune on the withheld slice after seeing it fail.** The
  withheld slice's entire value is that the rebuild never saw it during
  selection. One peek to "adjust" and re-test destroys the test â€” start a
  new BRAC cycle with a different withheld window instead.
- **Similar â‰  identical.** Small numeric drift in the selected parameter or
  moderate profit-per-trade variation is expected and fine; the failure
  signal is a different regime entirely (profitable â†’ unprofitable, or a
  wildly different "optimal" parameter each time), not decimal noise.
- **A large trade count matters.** BRAC's confidence scales with sample
  size â€” thousands of trades across a many-instrument basket produce stable
  parameters year over year (Fitschen: 80-day parameter held for 25+ years
  across a commodity basket); a system with a handful of trades on one
  instrument will look "stable" or "unstable" almost at random. If the
  trade count is thin, treat any BRAC verdict as low-confidence and widen
  the basket/history before trusting it either way.
- **Fold money-management gates into every step, not just the end (Ch. 7
  extension).** When step 1's selection logic adds a rule/filter/stop,
  gate that addition on gain-to-pain (return relative to drawdown/pain), not
  raw profit alone â€” a rule that raises total profit but blows up drawdown
  is not an improvement to carry into the rebuild. Bake this into the
  selection criteria you log in step 1, so the rebuild in step 3 inherits it.
- **Bar-scoring / ranking models still need BRAC (Ch. 8 extension).** If the
  "strategy" is really a ranking/scoring model used to pick the best
  candidates from a group, run the identical build/rebuild/compare cycle on
  the scoring rule itself, on a large multi-instrument sample â€” a scoring
  model overfit to one basket's history is just curve-fitting wearing a
  different hat.
- **A chart or trade anecdote is not evidence, it's a hypothesis (Ch. 9
  extension).** Before running BRAC at all, restate the "I noticed X sets up
  before big moves" claim as precise, mechanical, testable rules (exact
  entry/exit/filter conditions, no "looks like"), then run it across a
  large multi-decade, multi-instrument basket with a real parameter sweep.
  Only once that produces a real backtest do steps 1â€“5 apply â€” BRAC on an
  unfalsifiable eyeballed pattern is theater.

## Worked mini-example

Moving-average system, 37 domestic commodities, 20+ years daily data.

- **Build** (all data): sweep MA length 10â€“120 by 10 â†’ pick max profit
  (100 days). Sweep look-back filter (MA+10 to 200 by 10) â†’ pick max profit
  (200 days). Sweep catastrophic stop $250â€“$2,000 by $250 â†’ pick max profit
  ($2,000). Result: 2,103 wins / 4,326 losses / $2,555,125 net. Last year
  alone (the slice about to be withheld): 101 wins / 205 losses / $333,407.
- **Withhold**: drop the final 1 year of data.
- **Rebuild** on the truncated data using the identical three sweeps and the
  identical "pick max profit" rule at each step: selected values come out
  100 days / 200 days / $2,000 â€” the same parameters as the full-data build.
- **Compare**: run the rebuilt system forward through the withheld year and
  compare to the original's withheld-year numbers. Parameters matched and
  performance tracked â†’ **BRAC pass**. Verdict: trade it. (Fitschen notes a
  parameter from this class of test â€” 80 days on a 35-commodity basket â€”
  held stable for 25+ years live, evidence that large-sample BRAC passes
  correlate with real durability.)

## References

- Source: Keith Fitschen, *Building Reliable Trading Systems* (Wiley, 2013),
  Ch. 2 "Developing a Strategy So It Trades Like It Back-Tests" (BRAC method
  and BRAC-vs-out-of-sample argument); Ch. 7 (money-management/gain-to-pain
  feedback folded into each development step); Ch. 8 (bar-scoring models
  need the same out-of-sample curve-fit estimate); Ch. 9 (well-chosen-example
  guard â€” restate anecdotal edges as testable rules before backtesting).
- Siblings: none registered yet in this carve.
