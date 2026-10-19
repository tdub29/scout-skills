---
name: chan-algorithmic-trading
description: >
  Design, diagnose, and size a systematic trading strategy the way Ernie Chan does in
  Algorithmic Trading: Winning Strategies and Their Rationale (2013). Use when the task is
  to build or critique a quant/algo strategy for stocks, ETFs, currencies, or futures and
  you need the DURABLE method, not a tip: deciding mean-reversion vs momentum for a given
  instrument, testing for stationarity/cointegration (ADF, Hurst, Variance Ratio, half-life,
  CADF, Johansen), building pairs/spreads (price vs log vs ratio, Bollinger bands, Kalman
  filter, scaling-in), understanding roll returns / contango / backwardation, extracting a
  known Chan strategy (buy-on-gap, cross-sectional linear long-short, calendar spread, VX-ES,
  PEAD, opening gap, leveraged-ETF close, futures time-series momentum), scrubbing a backtest
  for bias (look-ahead, data-snooping, survivorship, primary-vs-consolidated, short-sale,
  futures continuous/settlement), Kelly / half-Kelly leverage sizing and CPPI, or judging
  whether a live drawdown is a normal loss or a regime change. Triggers on: "backtest,"
  "mean reversion," "momentum," "pairs trading," "cointegration," "stationarity," "ADF test,"
  "Hurst exponent," "half-life," "Johansen," "hedge ratio," "Kalman filter," "roll return,"
  "contango," "backwardation," "calendar spread," "Kelly formula," "optimal leverage,"
  "position sizing," "Sharpe ratio sanity check," "why did my strategy stop working,"
  "regime change," "stat arb," "statistical arbitrage." Not for discretionary chart-reading,
  options pricing, or fundamental valuation.
---

# Chan Algorithmic Trading Method

Ernie Chan's thesis: profit does not come from a clever, complicated strategy. It comes from
an **intrinsic market inefficiency hidden in plain sight** (regression to the mean, the roll
return in futures, forced end-of-day rebalancing by leveraged ETFs, slow diffusion of news).
Understand the inefficiency first, then the simplest linear strategy that exploits it is
usually the right one. Complexity is a data-snooping trap, not an edge.

Use this skill to turn a vague strategy idea into a concrete, defensible design AND to catch
the pitfalls that make backtests lie. It always ends in a decision or an artifact, never a
lecture.

## What this skill produces

Pick the one that fits the request and deliver it:

1. **A strategy design brief** for a named instrument or pair: mean-reversion vs momentum
   verdict, the specific Chan template to copy, the signal, the entry/exit rule, the
   look-back, and the reason it should work. See `references/strategy-quick-reference.md`.
2. **A backtest-bias audit**: the strategy run through the pitfall checklist, each pitfall
   marked applicable/clean, and the corrected treatment. See `references/backtest-pitfalls-and-bias.md`.
3. **A stationarity / cointegration test plan**: which test (ADF, Hurst+VR, half-life, CADF,
   Johansen), on what series (price, log price, ratio), and how to read the statistic vs the
   critical value. See `references/mean-reversion-detection.md`.
4. **A sizing recommendation**: Kelly or half-Kelly leverage, the Monte-Carlo caveat for
   fat tails, and CPPI or stop-loss for a drawdown cap. See `references/risk-management-kelly.md`.
5. **A regime / "why did it stop working" diagnosis**: normal loss vs cointegration breakdown
   vs momentum crash vs data error, with the remedy. See `references/mean-reversion-detection.md`
   and `references/momentum-method-and-strategies.md`.

## The decision flow

Run these in order. Stop when you have the artifact the user asked for.

### Step 1: Mean-reversion or momentum?

The two camps have **diametrically opposite risk-return profiles**, so this choice governs
everything downstream (sizing, stop-loss logic, expected Sharpe).

- **Mean reversion**: prices revert to a mean. Upside is capped at the mean; downside is
  unlimited if the series regime-changes. Easy to build (you can manufacture stationary
  portfolios via cointegration), high Sharpe from many short-horizon trades, but a rare loss
  can be catastrophic. Dominant in stocks/ETFs and manufactured spreads. Stop losses fight
  the entry logic.
- **Momentum**: past returns predict future returns. Upside unlimited; downside limited by a
  natural exit (reversed signal = de facto stop). Harder to find, lower Sharpe (few
  independent signals from long holding periods), thrives on black swans and fat tails, but
  **crashes for years after a financial crisis**. Dominant in futures and currencies.

Rule of thumb from the book: stocks and ETFs lean mean-reverting (especially intraday and
cross-sectionally); futures and currencies lean momentum (driven by persistent roll-return
signs). A single series can be mean-reverting at one time frame and trending at another, so
test the specific horizon (`references/mean-reversion-detection.md`).

### Step 2: Prove the inefficiency exists before backtesting the strategy

Do NOT jump straight to a strategy backtest. The preliminary statistical tests use every
bar of data and have far higher statistical significance than a strategy backtest, which
produces only a handful of independent round-trip trades. Detection first, strategy second.

- Single series: ADF (tests mean reversion) or Hurst + Variance Ratio (tests stationarity),
  then compute the **half-life** of mean reversion. Half-life sets the natural look-back
  (use a small multiple of it, not a brute-force-optimized number). See
  `references/mean-reversion-detection.md`.
- Manufactured portfolio: CADF (a pair) or Johansen (any number; its eigenvector gives the
  hedge ratios, and the largest-eigenvalue relation has the shortest half-life).
- Momentum: correlation of past vs future returns over non-overlapping windows; scan
  look-back x holding pairs for the best (coefficient, p-value) compromise.

### Step 3: Choose the specific strategy template

Copy the closest Chan template rather than inventing rules. The full catalog with signals,
rationale, and reported APR/Sharpe is in `references/strategy-quick-reference.md`, with the
mechanics in `references/mean-reversion-strategies.md` (stocks/ETFs/currencies/futures) and
`references/momentum-method-and-strategies.md` (interday + intraday momentum).

### Step 4: Scrub for bias before trusting any number

Every applicable pitfall in `references/backtest-pitfalls-and-bias.md` inflates or deflates
the result. Most pitfalls **inflate** mean-reverting backtests and **deflate** momentum ones.
The single best defense against look-ahead bias: the backtest and live program are the same
code, differing only in the data fed in.

### Step 5: Size with Kelly, temper with reality

Optimal leverage f = mean excess return / variance of excess return. Treat full Kelly as an
**upper bound**, deploy half-Kelly, and for fat-tailed returns optimize the growth rate by
Monte Carlo (Pearson system) instead of trusting the Gaussian formula. Cap drawdown with CPPI.
See `references/risk-management-kelly.md`.

## Non-negotiables (Chan's binding rules)

- **Simple and linear beats complex and nonlinear.** More parameters and more rules both
  invite data-snooping bias. A linear model has a Taylor-series justification; a nonlinear one
  needs a specific reason to exist.
- **Detection tests outrank strategy backtests** for statistical significance. Trust the ADF /
  half-life / cointegration result over a thin backtest's Sharpe.
- **Never size on full Kelly.** Overestimating the mean or underestimating the variance
  overestimates leverage, and enough overestimated leverage means eventual ruin.
- **Stop losses are logical for momentum, dangerous for mean reversion.** A mean-reversion
  stop should sit beyond the backtest max drawdown so it only ever fires on a true regime
  change, never during normal reversion.
- **A cointegrating pair should have a fundamental story** (EWA-EWC: both commodity economies;
  GLD-GDX: miners own gold). When the story breaks (GLD-GDX split when oil spiked in 2008), the
  strategy breaks. No story = "greater fool" momentum that can stop without warning.
- **Out-of-sample means after publication.** Anything retuned on the "out-of-sample" set is
  now in-sample. Walk forward with real money at minimal leverage; expect live Sharpe around
  half of backtest.

## References

Load the file that matches the task:

- `references/backtest-pitfalls-and-bias.md` - Ch 1. Look-ahead, data-snooping/linearity,
  survivorship, primary-vs-consolidated, venue-dependent FX quotes, short-sale constraints,
  futures continuous-contract back-adjustment, close-vs-settlement, hypothesis testing +
  Monte Carlo significance.
- `references/mean-reversion-detection.md` - Ch 2. ADF, Hurst exponent, Variance Ratio,
  half-life (Ornstein-Uhlenbeck), cointegration (CADF, Johansen), the parameterless linear
  Z-score strategy, pros/cons of mean reversion.
- `references/mean-reversion-strategies.md` - Ch 3 + 4 + 5. Price vs log vs ratio spreads,
  Bollinger bands, scaling-in vs all-in, Kalman filter (dynamic hedge ratio + market-making),
  data-error danger; stock-pair difficulties, ETF pairs/triplets, buy-on-gap, index arb,
  cross-sectional linear long-short; currency cross-rates + rollover interest; roll return,
  contango/backwardation, calendar spreads, crack spread, VX-ES.
- `references/momentum-method-and-strategies.md` - Ch 6 + 7. Four drivers of momentum,
  time-series vs cross-sectional momentum, roll-return extraction (futures-vs-ETF, VX-ES),
  news sentiment, forced asset sales, momentum crashes; opening gap, PEAD, event drift,
  leveraged-ETF close rebalancing, HFT tactics (ratio trade, ticking, flipping, stop hunting,
  order flow).
- `references/risk-management-kelly.md` - Ch 8. Constant-leverage requirement, Kelly formula
  (single + multi-strategy F = C^-1 M), half-Kelly, Monte-Carlo growth-rate optimization,
  CPPI, stop loss for MR vs momentum, leading risk indicators (VIX, TED, HYG, ONN/OFF, MXN,
  order flow).
- `references/strategy-quick-reference.md` - one-line-per-strategy catalog: asset, signal,
  rationale, reported APR/Sharpe, key pitfall. The fast lookup.

## Source

Ernest P. Chan, *Algorithmic Trading: Winning Strategies and Their Rationale* (Wiley Trading,
2013, ISBN 978-1-118-46014-6). Follow-up to Chan, *Quantitative Trading* (2009). All book
examples are MATLAB; this skill captures the method and rationale, not the code.
