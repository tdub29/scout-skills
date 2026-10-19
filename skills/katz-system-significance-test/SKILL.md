---
name: katz-system-significance-test
description: "Is a backtest edge real or data mining. t-test"
---

# Katz System Significance Test

## What it decides

Whether a system's backtested edge is likely real or is explainable by chance
and curve-fitting. Outputs a single verdict â€” SIGNIFICANT / MARGINAL /
NOT SIGNIFICANT â€” built from four numbers: the t-statistic and raw p-value on
the average trade, the p-value re-corrected for the number of variants
searched during development, a serial-dependence discount, and a binomial
confidence interval on the win rate. This is the last gate before a system
goes from "backtested" to "trusted."

## When to use

- A backtest reports a positive average trade and the question is "could
  this be zero, or negative, in the population?"
- The system (or its parameters) was chosen from a set of candidates â€”
  any optimization run, grid search, or "I tried a few variants and kept
  the best" counts.
- Someone wants to know if a streak of wins is proof of skill or just what
  a coin flip looks like some of the time.
- Not for: judging whether the *strategy design* is sound (see
  `katz-component-isolation-testing`), picking exits (see
  `katz-exit-strategy-taxonomy`), building filters (see
  `katz-filter-bank-cycles`), or evolving rules (see
  `katz-ga-rule-discovery`). This skill only tests the numbers those
  produce.

## Method

1. **Get the raw series.** Pull every individual trade P/L (or, for a
   portfolio/continuous system, daily returns). Never run the test on the
   equity curve total or the cumulative return â€” a single number has no
   variance to test against.

2. **Run the t-test on that series.**
   `t = mean(x) / (stdev(x) / sqrt(n))`, `df = n - 1`, two-tailed p-value
   against `t` with `df` degrees of freedom (H0: mean = 0). `n` = number of
   trades (or days), not number of parameters.

3. **Correct for optimization search â€” the data-mining guard.**
   If the system or its parameters were chosen as the best of `m` variants
   (grid cells, GA generations Ã— population, walk-forward re-optimizations,
   or just "I eyeballed 20 tweaks and picked the winner"), the raw p-value
   understates the true chance of a false positive. Adjust:

   ```
   p_adj = 1 - (1 - p_raw)^m
   ```

   Report `p_adj`, not `p_raw`, as the headline number whenever `m > 1`.
   `m` is the count of *distinct configurations evaluated*, not the count
   kept â€” undercounting `m` is the single most common way this test gets
   gamed (see Sub-rule 2).

4. **Discount for serial dependence.** Trades are not i.i.d.: winners and
   losers cluster (see the runs test / correlational-statistics discussion
   in Ch. 4). Before trusting `df = n - 1`, check the lag-1 autocorrelation
   `r1` of the trade series. If `|r1|` is non-trivial (rule of thumb:
   `|r1| > 0.1`), shrink the effective sample size before re-running the
   t-test:

   ```
   n_eff â‰ˆ n * (1 - r1) / (1 + r1)
   ```

   Re-run step 2 with `n_eff` in place of `n`. This is a rough correction,
   not a substitute for a proper runs test â€” it exists so a streaky system
   doesn't get credited with more independent evidence than it has.

5. **Bound the win rate.** Compute a binomial confidence interval (95% by
   default; Wilson score interval preferred over the normal approximation
   when `n` is small or the win rate is near 0 or 1) on percent-wins using
   `n` = actual trade count (not `n_eff` â€” the binomial CI is about the
   proportion, not the mean-return test, and doesn't need the serial
   correction). Report the interval, e.g. "52% wins, 95% CI [44%, 60%]."

6. **Render the verdict.**
   - **SIGNIFICANT**: `p_adj < 0.05` after the serial-dependence discount,
     and the win-rate CI doesn't straddle a rate that would make the
     average trade uneconomic (e.g., breakeven win rate given payoff
     ratio).
   - **MARGINAL**: `0.05 â‰¤ p_adj < 0.20`, or the win-rate CI is wide enough
     to include both a profitable and unprofitable scenario. Flag for more
     out-of-sample data before trusting it.
   - **NOT SIGNIFICANT**: `p_adj â‰¥ 0.20`, or `n` too small to compute a
     meaningful `n_eff`. Treat the backtest as noise regardless of how good
     the equity curve looks.
   State all four numbers (`t`, `p_raw`, `p_adj`, CI) in the verdict â€”
   never report just one.

## Sub-rules / failure modes

1. **Trade-by-trade, not equity total.** Testing the total or the equity
   curve's slope throws away the variance the t-test needs and will nearly
   always look "significant" by construction. Always assemble the vector
   of individual trade (or period) returns first.
2. **Count every variant evaluated, not just the survivors.** `m` in
   `p_adj = 1-(1-p)^m` is the size of the search space actually explored â€”
   every parameter combination the optimizer touched, every walk-forward
   window re-fit, every manual tweak tried and discarded. Reporting `m=1`
   because "I only kept one system" after running a 500-cell grid search is
   the classic way this guard gets defeated. When `m` is genuinely unknown
   (informal tweaking), estimate it generously rather than assume `m=1`.
3. **Don't skip the serial-dependence discount because it complicates the
   math.** A system with strong winner/loser clustering can show a
   nominally significant t-test purely because `n` overstates independent
   observations. If a runs test or autocorrelation check isn't feasible,
   at minimum flag the result as unverified for serial dependence rather
   than silently assuming i.i.d.
4. **A high win rate is not the same as significance.** A system can have
   70% winners and still fail the t-test (small wins, rare huge losses) or
   pass the t-test with a 40% win rate (big winners, small losers). Report
   both the t-test verdict and the win-rate CI â€” never let one substitute
   for the other.
5. **Small `n` breaks everything here.** Below roughly 30 trades, both the
   t-test and the binomial CI are unreliable regardless of how the numbers
   compute â€” report NOT SIGNIFICANT / insufficient data rather than a
   precise-looking p-value on a thin sample.

## Worked mini-example

System: 84 trades, mean trade = $310, stdev = $1,450. Developer optimized
2 parameters over a 15Ã—12 grid (`m = 180` variants evaluated) and kept the
best cell. Lag-1 autocorrelation of the trade series `r1 = 0.22`. 46 of 84
trades were winners.

1. `t = 310 / (1450/sqrt(84)) = 310 / 158.2 = 1.96`, `df = 83` â†’
   `p_raw â‰ˆ 0.053` (two-tailed).
2. `p_adj = 1 - (1 - 0.053)^180 â‰ˆ 1 - (0.947)^180 â‰ˆ 1 - 0.00007 â‰ˆ 0.9999.`
   The optimization search alone erases the apparent edge â€” a t-statistic
   this good is close to guaranteed to appear somewhere in a 180-cell grid
   even under pure noise.
3. Serial-dependence discount: `n_eff = 84 * (1-0.22)/(1+0.22) â‰ˆ 84 * 0.639 â‰ˆ
   54`. Re-running the t-test with `df = 53` moves `p_raw` slightly worse,
   reinforcing the same conclusion.
4. Win-rate CI (Wilson, 95%, n=84, 46 wins = 54.8%): roughly [43.9%, 65.2%].
5. **Verdict: NOT SIGNIFICANT.** `p_adj â‰ˆ 1.00` â€” after correcting for the
   180-variant search this "edge" is statistically indistinguishable from
   chance, despite a raw p-value that looked borderline-passable at
   `p_raw = 0.053`. Recommend re-testing on genuinely fresh out-of-sample
   data with the parameters frozen, not re-optimized.

## References

- Katz & McCormick, *The Encyclopedia of Trading Strategies* (2000,
  McGraw-Hill), Ch. 4: Statistics â€” t-tests on trade series and returns,
  degrees-of-freedom cost of optimization/curve-fitting, serial dependence
  and the runs test, confidence intervals on correlational statistics.
- Sibling skills: `katz-component-isolation-testing` (isolates which system
  component produced the edge before you test it), `katz-exit-strategy-taxonomy`,
  `katz-filter-bank-cycles`, `katz-ga-rule-discovery` (the optimization
  processes whose variant count `m` this skill consumes).
- Generic mechanics (t-test math, CI formulas, hypothesis-testing pitfalls
  beyond trading) live in `quantitative-research`; out-of-sample /
  walk-forward robustness is `fitschen`'s domain, not this skill's.
