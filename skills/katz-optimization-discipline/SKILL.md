---
name: katz-optimization-discipline
description: Decide whether a trading-system optimization is trustworthy or curve-fitted, using Katz and McCormick's four failure modes (small sample, large parameter set, single sample, no inferential statistics) and four success conditions (large representative sample, few free parameters, out-of-sample verification, corrected statistics), plus the shrinkage estimate and the walk-forward / self-adaptive alternatives. Use when asked "did I overfit this backtest," "how many parameters can I optimize on this much data," "how much of my backtested edge is curve-fitting," "should I use walk-forward instead of a single in-sample optimization," "is parameter-sensitivity a good robustness check," or when reviewing anyone's optimized system before it is traded. From Katz and McCormick, The Encyclopedia of Trading Strategies, Chapter 3.
---

# Katz Optimization Discipline

## What this decides

Whether an optimized trading system should be traded, rebuilt on a bigger
sample, simplified, or thrown away. The verdict is not a feeling about
"robustness"; it comes from the relationship between sample size, free
parameter count, and what verification was actually run.

The core claim: optimization itself is not dangerous. **Bad** optimization is.
Optimizing a large parameter set on a small sample with no out-of-sample test
and no inferential statistics is what produces systems that look great in a
backtest and destroy capital in real time.

## The four failure modes

Run these as a checklist. Any one of them is enough to void a result.

1. **Small sample.** A small sample is unlikely to represent the universe it was
   drawn from. The optimizer will faithfully find the best solution *for that
   sample*, which can be a terrible solution for the data actually traded. The
   failure is not a bad answer; it is a good answer to the wrong problem.
2. **Large parameter set.** As free parameters and rules rise relative to data
   points, more of the measured fitness is mathematical artifact. As the number
   of data points approaches the number of free parameters, almost any model
   fits even random data perfectly. A two-parameter line always passes through
   any two points, never reliably through three.
3. **Single sample.** No held-out data means the spurious solutions from (1) and
   (2) go undetected.
4. **No inferential statistics.** Without them there is no probability statement
   at all, only an anecdote about one sample.

What failure looks like in practice: excellent in-sample performance, terrible
live performance. Neural-network people call it poor generalization; traders
meet it as margin calls.

## The shrinkage estimate

For linear regression there is a closed-form correction that estimates how much
apparent fitness disappears once the artifact component is removed. It relates
N (data points), P (parameters) and R (the correlation found by optimization) to
RC, the shrinkage-corrected correlation.

Use it as a heuristic well beyond regression:

- It is a decent estimator for a fully trained neural network, which is just a
  particular nonlinear regression. Let P be the total number of connection
  weights.
- Use **simple** correlations, not squared ones. If the package reports R
  squared, take the square root first.
- The inverse form estimates how inflated an observed R will be given a true
  population correlation, which is the number to quote when someone shows you a
  gaudy in-sample fit.

The practical use is directional: it makes the N-versus-P tradeoff concrete
instead of rhetorical.

## The four success conditions

1. **Large, representative sample.** Representative beats merely long. The
   sample should contain bull and bear markets, trending and nontrending
   periods, and crashes, and should be recent enough to reflect current market
   behavior. There is a real tradeoff: reaching farther back adds size but can
   add irrelevance. Watch for structural break points (S&P 500 futures began
   trading in 1983 and changed the market's structure). The tradeoff mostly
   dissolves on short intraday time frames, where hundreds of thousands of bars
   are available from the recent past.
2. **Few rules and parameters, relative to sample size.** Several dozen
   parameters can be acceptable against thousands of trades on 100,000 one-minute
   bars. Two or three can be too many on a few years of end-of-day data. If a
   model genuinely needs many parameters, the answer is a far bigger sample, or
   optimizing one shared rule set across a whole portfolio.
3. **Verification.** The single most critical step. Discard any solution that is
   not profitable out of sample.
4. **Statistics, correctly corrected.** Compute inferential statistics on both
   in-sample and out-of-sample results. **In-sample optimization results must use
   statistics corrected for multiple tests**; out-of-sample results use standard
   uncorrected statistics. (See `katz-system-significance-test` for the actual
   test.)

## Count trades, not just bars

A system that takes only a few trades can be profitable by chance or artifact
regardless of how many data points the test covered. Sample size in the sense
that matters is the number of trades.

## Parameter sensitivity is not robustness

A widely repeated check is to nudge parameters and see whether performance
survives. Do not lean on it. Many genuinely robust models are highly sensitive
to particular parameter values. The only real arbiters are statistical tests and,
above all, out-of-sample tests.

## The two alternatives worth using

Both make every reported trade effectively out-of-sample, which retires
shrinkage corrections, multiple-test corrections, and most curve-fitting worry.

**Walk-forward optimization.** Optimize on points 1..M, trade M+1..M+K,
reoptimize on K+1..K+M, trade forward again, and repeat to the end of the
series. M is the look-back (optimization) window; K is the reoptimization
interval. Every trade sits in the future relative to the optimization that
produced it.

**Self-adaptive systems.** Same idea, except the adaptation lives inside the
system rather than in the test harness: the system updates its own parameters or
rules as bars arrive, then acts on the next bar. Updates need not happen every
bar.

## Verdict template

State the four numbers first, then the call.

```
Sample:        <bars> bars, <trades> trades, <start>-<end>, regimes covered: <...>
Free params:   <count> (rules + parameters)
Verification:  <out-of-sample? walk-forward? none>
Statistics:    <corrected p in-sample / uncorrected p out-of-sample>

Verdict: TRADEABLE | REBUILD ON MORE DATA | SIMPLIFY | DISCARD
Reason:  <which failure mode fired, or which success conditions are met>
```

Bias toward DISCARD when verification is missing entirely. An unverified system
is not a weak result, it is an unmeasured one.

## Related

- [[katz-system-significance-test]] for the actual t-test, multiple-test
  correction, and serial-dependence discount.
- [[katz-exit-strategy-taxonomy]] once a system passes and needs an exit.
- [[katz-scientific-system-development]] for where optimization sits in the
  whole development loop.
