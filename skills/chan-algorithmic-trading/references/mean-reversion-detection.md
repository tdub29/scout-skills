# Detecting Mean Reversion: Stationarity, Half-Life, Cointegration (Chan Ch 2)

Most price series are geometric random walks; only the RETURNS distribute around a mean (and
you cannot trade the mean reversion of returns). The few price series that revert are called
**stationary**. You cannot find many prefabricated stationary assets, but you can **manufacture**
them by combining cointegrating series into a stationary portfolio. Test for the inefficiency
first, because these tests use every bar and are far more significant than a strategy backtest.

Two equivalent views, two families of test:
- **Mean reversion**: the change in price is proportional to (mean - current). Tested by ADF.
- **Stationarity**: variance of log price grows slower than a random walk (sublinear in time,
  ~ tau^(2H)). Tested by Hurst exponent + Variance Ratio.

This chapter covers **time series** mean reversion (revert to own history). **Cross-sectional**
mean reversion (a name reverts to the basket's return) is in `mean-reversion-strategies.md`.

## Augmented Dickey-Fuller (ADF) test

Model the price change as `dy(t) = lambda*y(t-1) + mu + beta*t + alpha1*dy(t-1) + ... + eps`.
ADF tests whether lambda = 0 (random walk). Test statistic = lambda / SE(lambda). For mean
reversion lambda must be NEGATIVE and MORE negative than the critical value.

- Assume nonzero offset (the mean price is seldom zero) but **zero drift** (constant price
  drift is tiny vs daily fluctuation). In the spatial-econometrics `adf(y, 0, 1)` convention:
  2nd arg 0 = offset-yes/drift-no, 3rd arg = lag k. Try k=0, but often only k=1 rejects the
  null (price changes have serial correlation).
- Sampling intraday does not raise ADF significance; use end-of-day.
- Example: USD.CAD gives ADF statistic ~ -1.84 vs 90% critical -2.594, so cannot reject
  random walk (it is a commodity currency), but lambda < 0 means at least not trending.

## Hurst exponent and Variance Ratio test

Variance of log-price diffusion: `Var(tau) = <|z(t+tau) - z(t)|^2> ~ tau^(2H)`, z = log(y).
- H = 0.5: geometric random walk.
- H < 0.5: mean reverting (more so as H -> 0).
- H > 0.5: trending (more so as H -> 1).

H is a degree-of-mean-reversion indicator. Compute with a generalized-Hurst function at q=2.
The **Variance Ratio test** supplies the significance: does Var(z(t)-z(t-tau)) / (tau x
Var(z(t)-z(t-1))) = 1? MATLAB `vratiotest` returns h (1 = reject random walk at 90%) and a
pValue (probability the random-walk null is true). USD.CAD: H = 0.49, vratiotest pValue = 0.37,
cannot reject random walk.

Note: "stationary" here does not mean range-bound (H = 0); it only means variance grows slower
than normal diffusion.

## Half-life of mean reversion (the practical shortcut)

The statistical tests demand 90%+ certainty, but you can trade profitably with less. Drop the
drift and lagged terms and ADF's model becomes the **Ornstein-Uhlenbeck** SDE
`dy = lambda*(y - mean)*dt + dW`. Its analytic solution decays to the mean with

    half-life = -log(2) / lambda

Get lambda by regressing `y(t) - y(t-1)` on `y(t-1)` (dependent vs independent). Then:
- lambda > 0: not mean reverting at all; do not write a mean-reversion strategy.
- lambda near 0: very long half-life; too few round trips to be profitable.
- lambda gives a **natural time scale**: set the look-back for moving average/std to a small
  multiple of the half-life. This AVOIDS brute-force optimizing the look-back (a data-snooping
  source), because half-life depends on the price series, not on your strategy.

Examples: USD.CAD half-life ~ 115 days (long, but at least you know the look-back and holding
period to expect); EWA-EWC-IGE portfolio ~ 23 days; CL 12-month calendar spread ~ 36 days.

## Cointegration: manufacturing a stationary portfolio

If a linear combination of nonstationary series is stationary, the series **cointegrate**
(the classic case is a long-short pair: "pairs trading"). The hedge ratio is the number of
units (shares) of each asset; you do not know it a priori, hence dedicated tests.

### CADF (Cointegrated ADF), for a pair only
Engle-Granger two-step: regress one price on the other (OLS) to get the hedge ratio, form the
residual spread, run ADF on it. `cadf(y, x, 0, 1)`. **Order-dependent**: the hedge ratio from
x-as-independent is not the reciprocal of y-as-independent, and often only one order yields a
stationary portfolio. Try both, keep the more negative t-statistic. Example: EWA-EWC gives
CADF ~ -3.64 vs 95% critical -3.359, cointegrating at 95%.

### Johansen test, for any number of series
Vector generalization; rank r of the coefficient matrix = number of independent cointegrating
portfolios. Trace statistic and eigen statistic both test r = 0, r <= 1, ... against critical
values. **Order-independent.** Its by-product is the prize: the **eigenvectors are the hedge
ratios**, and the eigenvector with the LARGEST eigenvalue gives the portfolio with the
SHORTEST half-life. (EWA-EWC-IGE: 3 cointegrating relations at 95%; best eigenvector portfolio
half-life 23 days.) Known implementation limit: max ~12 symbols.

## The parameterless linear strategy (the significance workhorse)

Once a series (or unit portfolio) is stationary with a short-enough half-life, trade it with a
strategy that has **no free parameters to optimize**: hold a number of units NEGATIVELY
proportional to the normalized deviation (Z-score) from the moving average:

    numUnits = -(y - movingAvg(y, lookback)) / movingStd(y, lookback)   # lookback = half-life

"Linear" means the number of units is proportional to the Z-score, not that the market value
is. It is impractical as-is (needs unbounded capital, continuous infinitesimal rebalancing),
but it PROVES the series yields profit with zero data-snooping and, by trading continuously,
has more statistical significance than any selective entry/exit rule. Moving average/std are
still used even for a "stationary" series because the mean drifts slowly and (for 0 < H < 0.5)
variance still grows with time. EWA-EWC-IGE version: APR 12.6%, Sharpe 1.4.

## Pros and cons of mean reversion

Pros: easy to build (manufacture stationary portfolios from a growing universe of ETFs);
usually a fundamental story (EWA-EWC both commodity economies; GDX-GLD miners own gold); spans
time scales from market-making (seconds) to value investing (years); short time scales give
many trades = high significance and Sharpe.

Cons: the seeming high consistency breeds overconfidence and overleverage (think LTCM). When
it breaks (often for a reason clear only in hindsight, and often at peak leverage after a
winning streak) the loss is severe. Risk management is both critical and hard, because normal
stop losses contradict the entry logic (see `risk-management-kelly.md`).

## Using this for a "why did it stop working" diagnosis

1. Re-run the cointegration test over the recent window vs the original. If it fails
   out-of-sample, the fundamental relationship broke (GLD-GDX lost cointegration on 2008-07-14
   when oil peaked at ~$145 and made mining expensive). Look for the fundamental cause and
   often a repaired strategy (add USO to make GLD-GDX-USO cointegrate again).
2. If cointegration holds but P&L is bad, check for data errors (see
   `mean-reversion-strategies.md`) and pitfalls (`backtest-pitfalls-and-bias.md`).
3. A mean-reverting series can regime-change into a trending one, maybe permanently. That is
   when a stop-loss beyond the backtest max drawdown earns its keep.
