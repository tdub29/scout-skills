---
name: evidence-based-technical-analysis
description: "Is this backtest signal real? Stats, data-mining bias"
---

# Evidence-Based Technical Analysis (Aronson)

Aronson's thesis: most technical analysis stands where medicine stood before it became a
science, defended by colorful narratives and cherry-picked anecdotes instead of statistical
evidence. A trading rule is a testable claim ("this rule has predictive power"), and the only
rational way to decide whether that claim is true is the scientific method plus statistical
inference. This skill is the anti-self-deception layer. Its job is to answer one question about
any signal, screen, or backtest: is the observed edge real predictive power, or is it good luck
dressed up as gold?

Use this skill to pressure-test a proposed signal before it drives capital, to audit a backtest
someone hands you, or to decide whether an out-of-sample dropoff is decay or just the luck
draining out. It always ends in a verdict (real edge, unproven, or spurious) with the reason,
never a lecture.

## When to use

- Someone claims a rule, screen, or indicator combo "works" and shows a backtest.
- A data-mined or optimized signal looks great in-sample and you must judge its future.
- Out-of-sample or live performance came in worse than the backtest and you need to know why.
- You are about to search many rules/parameters and want the honest significance test up front.
- A chart-pattern or discretionary claim needs to be converted into something testable or rejected.

## Step 1: Is the claim even testable? Objective vs subjective TA

Aronson's first cut. Only objective TA can be validated at all.

- Objective TA: a well-defined, repeatable procedure that issues unambiguous signals, so it can
  be coded as an algorithm and back-tested. Two analysts running it on the same data get the
  same result. These are the only claims worth testing.
- Subjective TA: vague methods that require the analyst's private interpretation, so two analysts
  reach different conclusions. Hand-drawn trendlines, classical chart patterns, Elliott Wave,
  Gann, "Magic T's." Aronson calls these "not even wrong": they are insulated from evidence, so
  no backtest can confirm or refute them, and no pile of cherry-picked winning examples cures that.

Action: if the signal cannot be reduced to an unambiguous rule that outputs a defined position
(for a binary reversal rule, +1 long or -1 short) each period, stop. Either operationalize it
into a testable rule or reject it as untestable. Do not spend statistics on a claim that has no
truth value.

## Step 2: Frame it as a hypothesis and demand a falsifiable prediction

A rule is a conjecture. Following Popper's demarcation, a claim is scientific only if it is
falsifiable: there must be an outcome that would prove it wrong. Set up the test as competing
hypotheses:

- Null hypothesis (Ho): the rule has no predictive power. Its expected return is zero (or its
  signals are uninformative noise that a roulette wheel could have produced).
- Alternative (Ha): the rule has predictive power, expected return greater than zero.

You never prove Ha true. You gather evidence strong enough to reject Ho, and knowledge stays
provisional. Larger p-values mean the observed statistic is consistent with Ho (no edge).

## Step 3: Strip the nuisance component (detrend and benchmark)

A backtest return has two independent parts. Only one is the edge.

1. The wanted part: the rule's actual predictive power.
2. The unwanted part: the rule's long/short position bias multiplied by the market's net trend
   over the test window. This has nothing to do with predictive power.

Position bias is how lopsided the rule's time in +1 vs -1 is. A rule whose long condition is
easy to satisfy sits long most of the time; run it over a rising market and it books a positive
return with zero predictive power. A worthless rule can look great, and a genuinely predictive
rule fighting the trend can look negative. This must be removed before you judge anything.

The expected return of a non-predictive rule with a given bias:

    ER = [ p(L) x ADC ] - [ p(S) x ADC ]

where p(L) and p(S) are the fractions of time long and short, and ADC is the market's average
daily change over the test period. That ER is the correct benchmark: the return a coin-flip rule
with the same bias would have earned. Subtract it from the rule's observed return.

The simpler equivalent Aronson uses: detrend the market data first. Subtract the average daily
price change from every day's change so the series has zero net trend. Compute rule returns on
the detrended series (signals are still generated from real, untrended data). With zero trend,
any position bias earns an expected zero, so the benchmark is automatically zero and a positive
detrended return signals real predictive power. Aronson's Appendix proves detrending is
mathematically equivalent to benchmarking against an equal-position-bias rule. Always report
benchmark-relative (detrended) returns, never raw returns.

## Step 4: Know which job the backtest number is doing

This is the pivot of the whole book. The same statistic is legitimate for one job and a trap for
the other.

- Single rule, tested once: the observed mean return is an unbiased estimator of the rule's
  expected future return. It may land high or low, but neither error is more likely. Using it as
  your forecast is fair.
- Many rules searched, pick the best (data mining): the observed return is a legitimate selection
  criterion (the best-observed rule is the best bet among those tested), but it is NOT a fair
  estimator of that winner's future return.

The data miner's mistake is using the best rule's in-sample return to estimate its expected
return. The winner's return is positively biased: the level that let it win the competition
overstates its true edge. That gap is the data-mining bias, "the fool's gold of objective TA."
The winner combined some (possibly zero) predictive power with a big slug of good luck, and luck
does not repeat. So its out-of-sample performance settles down to its true power. That is not the
rule decaying; it is the luck moving on. Out-of-sample deterioration of the best-of-many rule is
expected, not surprising.

Multiple comparisons are the engine. Just as more lottery tickets raise the odds someone wins
twice, more rules tested raise the odds that a worthless rule posts an extreme lucky return, and
that is exactly the rule the search selects.

## Step 5: Size the bias with the five factors

The data-mining bias gets larger when:

1. More rules are back-tested (the search is wider).
2. Fewer observations are used to compute the performance statistic.
3. Rule returns are less correlated with each other (more independent shots at luck).
4. Positive outlier returns are present (a few huge days), an effect diluted by more observations.
5. There is less variation in true merit across the tested rules (when all rules are similarly
   weak, luck decides the winner).

Read: a wide search over a short history of near-identical weak rules with a couple of monster
days is the maximum-bias setup. Treat any winner from that regime as guilty until proven innocent.

## Step 6: Test significance the right way for a searched rule

A plain single-rule significance test understates risk once you have searched many rules, because
it ignores that you cherry-picked the best. Two computer-intensive tests fix this by building the
sampling distribution of the BEST rule's performance under the null across the entire rule
universe, then asking how often chance alone beats the observed winner.

- Monte Carlo permutation (MCP), Aronson and Timothy Masters, public domain. Ho: the rule's
  output values (+1/-1) are randomly paired with future price changes, i.e. the signal is
  uninformative noise. Randomly re-pair rule outputs with market returns WITHOUT replacement
  (a permutation) many times, recompute the best-rule statistic each time, and build its null
  distribution. Needs the daily output sequence plus the daily price changes.
- Bootstrap / White's Reality Check, patented. Ho: the population distribution of rule returns
  has expected value zero or less. Resample the daily rule returns WITH replacement many times to
  approximate the sampling distribution. Needs the daily return history.

Run both on detrended data; on detrended data they generally agree. The p-value is the fraction
of null trials that match or beat the observed best rule. Reject Ho (declare a real edge) only if
that p-value is small. If the search space was large and the winner is not significant after this
multiple-comparisons-aware test, the honest verdict is "no proven edge," not "promising."

## Step 7: Out-of-sample and walk-forward as the honest read

Hold out data the mining and optimization never touched. In-sample fit is where the bias lives;
out-of-sample is where true power shows without the luck component. Walk-forward extends this:
fit on a window, test on the next unseen window, roll forward. Judge the rule on the aggregated
out-of-sample record, not the in-sample fit. Remember Step 4: some dropoff from in-sample to
out-of-sample is the normal evaporation of luck, so calibrate expectations to the true-power
level, not the backtest peak.

## Why subjective TA fools smart people (Chapter 2 background)

Humans invent illusory correlations: they perceive a signal-outcome link that is not there. We
attend only to the hits (the times the pattern "worked") and ignore the other three cells of the
2x2 outcome table, and studies show people cannot even see a real correlation until it exceeds
about 0.70, far stronger than anything in markets. Hindsight bias and the absence of falsifiable
forecasts let the belief survive contradictory evidence. This is the psychological reason the
statistical discipline above is non-negotiable: intuition systematically manufactures edges that
are not real.

## Validation checklist

Run a signal through this before trusting it.

1. Objective? The rule is unambiguous and computable; if not, reject as untestable.
2. Hypothesis framed? Ho (no power) vs Ha stated, with a falsifiable prediction.
3. Nuisance removed? Returns are detrended / benchmark-relative, not raw; position bias noted.
4. Estimator vs selector? If many rules were searched, the winner's in-sample return is NOT the
   forecast. Flag it.
5. Bias sized? Number of rules, sample length, rule-return correlation, outliers, and merit
   spread assessed against the five factors.
6. Multiple-comparisons test done? MCP or White's Reality Check across the full universe, on
   detrended data, with a small p-value before any "significant" claim.
7. True out-of-sample / walk-forward record, distinct from the mining data.
8. Verdict stated: real edge, unproven, or spurious, with the dominant reason.

## Common ways backtests lie (quick reference)

- Raw returns that bank the market's trend through a position bias, mistaken for skill.
- Reporting the best-of-N rule's in-sample return as its expected return (the data-mining bias).
- A single-rule p-value applied after searching hundreds of rules or parameter sets.
- Optimizing and testing on the same data (no genuine out-of-sample).
- Calling out-of-sample dropoff "decay" when it is just the luck component leaving.
- Defending an untestable subjective method with cherry-picked winning charts.
