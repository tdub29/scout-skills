# Backtesting Pitfalls and Statistical Significance (Chan Ch 1)

A backtest with a hidden pitfall is worse than no backtest: it misleads and loses money.
**Almost every pitfall inflates a mean-reverting backtest and deflates a momentum one**, so
an inflated result is the dangerous case. Run this list against any strategy before trusting
a single number.

## Why backtest at all (even a published strategy)

- Profitability is sensitive to implementation details a paper glosses over (MOO vs market
  order after open; 4:00 vs 4:15 futures close; bid/ask/last as trigger). The only way to
  pin them down is to backtest yourself.
- A published strategy lets you do TRUE out-of-sample testing (the period after publication).
  A backtest also lets you find refinements.
- Follow the scientific method: hypothesis -> backtest -> refine. Small detail changes
  (look-back, entry at open vs close) can bring large improvements.

## The bias checklist

### 1. Look-ahead bias
Using future information to make a present decision (e.g., using the day's high/low to set
that same day's entry). It is a programming error that can only exist in a backtest.
**Fix**: make the backtest and live program the same code, differing only in the data fed in.
Then look-ahead is structurally impossible.

### 2. Data-snooping bias and the beauty of linearity
Too many free parameters fitted to random past patterns that will not recur.
- Detect with out-of-sample testing, but honestly: if you retune after a poor out-of-sample
  result, you have converted it to in-sample. Use cross-validation across several subsets.
- **Prefer simple, linear models with few parameters.** A model with few parameters but many
  complicated rules is just as vulnerable. Nonlinear models have more parameters and fit past
  noise better without predicting better; every nonlinear model has a linear Taylor-series
  approximation, so the linear one needs a reason NOT to be used.
- Occam on distributions: assume Gaussian returns unless there is strong theoretical/empirical
  reason otherwise.
- Equal-weight factor models (Kahneman: "formulas that assign equal weights ... are often
  superior") and simple rank-and-sign combinations work well for ranking stocks (e.g.
  Greenblatt's magic formula: ROC + earnings yield, 30.8% APR 1988-2004 vs 12.4% for S&P).
- High Sharpe + short max-drawdown duration almost guarantees passing cross-validation.
- **Final gate**: a walk-forward test, ideally with real money at minimal leverage. Expect
  live Sharpe better than half the backtest value.

### 3. Stock splits and dividend adjustments
An N-for-1 split divides the price by N; a $d dividend drops the price by $d. Unadjusted, the
price gap triggers false signals. Back-adjust historical prices before the ex-date (divide by
N; subtract $d), in live trading too. (earnings.com for events; csidata.com for adjusted data.)

### 4. Survivorship bias
Data lacking delisted stocks inflates strategies that buy beaten-down survivors. Most
dangerous to mean-reverting LONG-ONLY stock strategies (buys low, sells high on names that
happened to survive). Long-short is partly self-canceling but still net inflated. Momentum is
deflated (profitable short trades on dead names are missing). Fix: survivorship-bias-free data
(csidata, kibot, tickdata, crsp), collect your own, or limit to the last ~3 years.

### 5. Primary vs consolidated stock prices
MOC/MOO orders route to the primary exchange (NYSE for IBM, Arca for SPY, Nasdaq for MSFT),
but consolidated historical closes/opens/highs/lows reflect any venue. Small off-primary
prints create outlier prices that a mean-reverting backtest "reverts from," inflating results.
If a strategy depends on MOO/MOC or on highs/lows, use primary-exchange prices or hold a
healthy skepticism.

### 6. Venue dependence of currency quotes
FX is fragmented with no best-bid/ask rule across venues. Backtest with data from the same
venue(s) you will trade. Trade prices/sizes are often unavailable or delayed; use bid-ask
quotes, since spreads (and thus transaction costs) vary a lot by venue.

### 7. Short-sale constraints
Hard-to-borrow stocks may cost interest to short, or be unshortable (SEC banned financial
shorts 2008-09; even SPY was unborrowable). The alternative uptick rule (2010): once a stock
falls 10% from prior close, a circuit breaker forbids short market orders that day and the
next. A backtest that shorts unshortable names shows unrealistic profit. Small-caps are worse
than large-caps; ETFs can be hard to borrow too.

### 8. Futures continuous contracts
A strategy trades many contracts; you roll to the next month (10 days before expiry, or at
open-interest crossover). Concatenating front-month prices creates a false P&L gap at the roll.
- **Price back-adjustment** (add q(T+1)-p(T+1) to all prior prices) makes P&L correct but
  return wrong; **return back-adjustment** makes return correct but P&L wrong. You cannot have
  both on a continuous series. Trading individual contracts with explicit rollover gets both.
- Spread strategies must use **price** back-adjustment (a small error in a small spread is a
  big % error and a false signal), especially calendar spreads. Ratio-signal strategies must
  use **return** back-adjustment.
- Price back-adjustment can push distant prices negative; add a constant to fix. Know exactly
  how your vendor back-adjusts.

### 9. Futures close vs settlement prices
The vendor's daily close is usually the exchange settlement price, which exists even with no
trade and generally differs from the last trade. **Use settlement prices** (closest to what
you would transact near the close). Critical for futures pairs so both legs are
contemporaneous. Intermarket spreads across exchanges have different closing times, so use
intraday bid-ask data for synchronicity, or trade an ETF that holds the future (e.g. GLD vs
GDX both on Arca instead of GC vs GDX).

## Statistical significance

**Hypothesis testing.** Null: true average return is zero. For a Gaussian null, the test
statistic is `mean(ret)/std(ret)*sqrt(n)` = daily Sharpe x sqrt(days). This is why high-Sharpe
strategies are more significant. Reject if the statistic beats the critical value:

| p-value | Critical value (sqrt(n) x daily Sharpe) |
|---|---|
| 0.10 | 1.282 |
| 0.05 | 1.645 |
| 0.01 | 2.326 |
| 0.001 | 3.091 |

More round-trip trades = higher significance. But even a clean, significant backtest is not
guaranteed predictive: a regime shift can spoil everything.

**Monte Carlo null (two variants).**
1. Simulate price series with the SAME first four moments (mean, std, skew, kurtosis) as the
   real returns (MATLAB `pearsrnd`), run the strategy on each, and count how often simulated
   average return >= observed. If often, the strategy is not capturing real serial correlation.
   (Chan's TU momentum example: rejected at only 88%, showing the returns-distribution SHAPE,
   not just serial correlation, drives the profit.)
2. Randomize the entry dates of the actual long/short trades over the real price series,
   keeping the same trade counts and holding periods, and measure how often random placement
   beats the observed return.

Each method compares against a different benchmark of randomness, so they legitimately give
different answers.
