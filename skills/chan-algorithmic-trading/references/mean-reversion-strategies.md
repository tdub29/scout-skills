# Implementing Mean Reversion Strategies (Chan Ch 3, 4, 5)

Detection (`mean-reversion-detection.md`) tells you a series is tradable. This is how you
actually trade it, and the concrete strategies for stocks, ETFs, currencies, and futures with
their rationale and reported metrics. You do not always need true stationarity: short-term or
seasonal mean reversion (revert only during specific periods/conditions) can be captured if
you exit before the next equilibrium.

## Spread construction: price vs log price vs ratio

The trading signal is the market value of the unit portfolio y = h1*y1 + ... + hn*yn.

- **Price spread** (`y1 - h*y2`): use when you want a FIXED NUMBER OF SHARES per leg for the
  trade. Simplest.
- **Log price spread**: use when you want FIXED DOLLAR (capital) weights per leg. Requires
  daily rebalancing to hold the capital weights constant (extra transaction cost).
- **Ratio** (`y1/y2`): a special case (only stationary if h1 = -h2). Use it when the pair is
  NOT truly cointegrating but you believe the spread mean-reverts short-term, because the ratio
  stays stable across large price-level changes where the dollar spread would not. Good for
  currency pairs (EUR.GBP is literally EUR.USD/GBP.USD). But for a truly cointegrating pair, a
  price spread with an adaptive hedge ratio usually beats a ratio (GLD-USO example: price
  spread APR 10.9% / Sharpe 0.59 vs log 9%/0.5; ratio negative).

Non-cointegrating pairs need a **dynamically recalculated hedge ratio** (short look-back OLS,
e.g. 20 days) or a Kalman filter.

## Bollinger bands (the practical linear strategy)

The parameterless linear strategy needs unbounded capital. Bollinger bands fix that: enter
when the Z-score exceeds `entryZscore` std from the mean, exit at `exitZscore` (< entry).
At most one unit (long or short) at a time, so capital and risk are trivial to manage. Shorter
look-back and smaller entry/exit magnitudes give shorter holds, more round trips, higher
profit. GLD-USO with entryZscore=1, exitZscore=0: APR 17.8%, Sharpe 0.96 (much better than the
raw linear version). Set the look-back to the half-life or optimize it on a training set.

## Scaling-in (averaging-in): does it work?

Scaling-in = adding to a position as it deviates further (the linear strategy does this
inherently), and scaling out gradually so you bank small profits even if the series never
fully reverts. Implement with multiple Bollinger levels (entry at Z = 1,2,...,N; exit at
0,1,...,N-1).

**Schoenberg and Corwin proved that entering/exiting at two or more bands is never optimal
in-sample**: a single "all-in" level always beats it (there is a transition probability
p-hat = (F-L1)/(F-L2) that decides all-in-at-L1 vs all-in-at-L2, and average-in never wins).
BUT the proof assumes the probability of a further deviation is constant over time. In reality
volatility (and that probability) changes, so scaling-in often gives a better REALIZED Sharpe
out-of-sample, and reduces market impact for large size. Verdict: never optimal in a backtest,
often useful live.

## Kalman filter (two uses)

An optimal linear recursive estimator of a hidden variable from a noisy observable, assuming
Gaussian noise. You only specify four things: observable, hidden variable, state-transition
matrix, observation model. Everything else is a robotic algorithm (Box 3.1 in the book).

1. **Dynamic hedge ratio + moving mean/std in one shot.** Observable = price series y;
   hidden = the 2-vector (hedge-ratio slope, intercept); observation model = the other price x
   augmented with ones; state transition = identity (beta today = beta yesterday + noise). No
   arbitrary look-back or EMA decay choice. The intercept estimate replaces the moving average
   of the spread; the measurement-error std sqrt(Q) replaces the moving std for Bollinger
   bands. Tuning: Vw = delta/(1-delta)*I with delta ~ 0.0001 (delta=0 reduces to fixed OLS;
   delta=1 makes beta thrash); Ve ~ 0.001. EWA-EWC Kalman strategy (enter when e < -sqrt(Q)):
   APR 26.2%, Sharpe 2.4.
2. **Market-making mean-price update.** Single series; hidden = mean price m(t), observable =
   price. State update `m(t) = m(t-1) + K*(y - m(t-1))`. Make the measurement error Ve a
   function of trade size (large trade = small uncertainty = Kalman gain near 1 = trust the
   print), so it behaves like a volume-and-time-weighted average price.

## The danger of data errors

A single bad tick (100, 110, 100 instead of 100, 100, 100) makes a mean-reverting backtest
short the false spike and cover, booking a fictitious profit. Data errors INFLATE
mean-reverting backtests (and suppress momentum ones, so they are less dangerous there).
Spread strategies are worst hit: a small error in a leg is a large % error in the small spread
(a $1 error in a $5 spread = 20%), triggering false trades in both backtest and live. Use
reputable feeds with cancel-and-correct codes; Chan cut phantom losses just by switching a
broker feed to a third-party quote source.

---

# Concrete mean-reversion strategies

## Stocks and ETFs (Ch 4)

**Why stock pairs are now hard.** Individual stocks are almost never stationary; sensible
pairs (XOM-CVX, C-BAC) rarely cointegrate out-of-sample because one company's fortunes shift
fast (AAPL vs BBRY). Trading many pairs does not save you: the "bad" pairs' large losses
overwhelm the "good" pairs' small profits. Plus short-sale constraints (short squeeze, uptick
rule) and tiny NBBO sizes (AAPL often 100 shares) from dark pools/iceberg/HFT. Decimalization
narrowed spreads and killed the market-making profit pair traders captured.

**ETF pairs and triplets** are better: a basket's fundamentals change slowly, so cointegration
persists out-of-sample. Find ETFs sharing economic factors (EWA-EWC both commodity economies;
RTH-XLP; commodity ETF vs its producers ETF GLD-GDX). Watch the story: GLD-GDX lost
cointegration on 2008-07-14 when oil peaked (mining got expensive); adding USO restores
GLD-GDX-USO cointegration, or at least stop trading GLD-GDX when oil exceeds a threshold.
Caveat: an ETF holding FUTURES (USO) does not track spot, so it may not cointegrate with a
producer ETF the way a spot-holding ETF (GLD) does.

**Buy-on-gap (intraday seasonal mean reversion), long-only.** Rationale: on down-futures
mornings certain stocks are panic-sold at the open, then recover intraday.
1. Near the open, select stocks whose return from yesterday's low to today's open is below
   -1 std (90-day close-to-close std). These "gapped down."
2. Keep only those whose open is ABOVE the 20-day moving average of closes (a momentum filter:
   modest droppers revert; big droppers usually have bad news that does not revert).
3. Buy the 10 with the lowest low-to-open returns.
4. Liquidate all at the close.
APR 8.7%, Sharpe 1.5 (2006-2012). The momentum filter (rule 2) is a reusable trick: overlay a
long-term-MA filter on a mean-reversion entry to improve consistency. Mirror short-on-gap
version: APR 46%, Sharpe 1.27 but steeper drawdown and short-sale constraints. Signal-noise
caveat: you must use preopen (Arca) prices, not the official open, to generate the signal.

**Index arbitrage, modernized.** Classic stocks-vs-index-future arb is too tight to profit.
Widen the gap by using only a SUBSET of the constituents. SPY vs component stocks: Johansen-test
each stock vs SPY over a training year, keep the ~98 that cointegrate, confirm the equal-weight
long-only portfolio cointegrates with SPY (using log prices for daily rebalancing), then run
the linear mean-reversion strategy. APR 4.5%, Sharpe 1.3 (decays without periodic retraining).
Constrain hedge ratios positive (genetic algorithm / simulated annealing) to keep the stock
leg long-only. HFT version exploits that indices use only primary-exchange prints (<30% of
volume) updated every few seconds, so the future lags the true basket value.

**Cross-sectional mean reversion (linear long-short), Khandani-Lo.** Not time-series: a stock
reverts relative to the basket, via serial anti-correlation of relative returns. Weight each
stock `wi = -(ri - r_market) / sum|rk - r_market|`, so short big relative outperformers, buy
big relative underperformers; total gross capital = $1 daily. No parameters, dollar-neutral,
completely linear. Close-to-close: APR 13.7%, Sharpe 1.3 (2007-2011), including 30% in 2008.
Intraday (open-to-close) version: APR 73%, Sharpe 4.7, but double the transaction cost and
signal noise. Rank by other factors (P/E) to avoid shorting names with genuinely rising
earnings. Profits only in aggregate; some names act as hedges.

## Currencies and futures (Ch 5)

**Currency cross-rates.** Form stationary FX portfolios from countries with similar
fundamentals (commodity currencies AUD, CAD, ZAR, NOK). Mechanics differ from ETFs:
- To run Johansen and read the eigenvector as capital weights, both legs must share a **quote
  currency** (use AUD.USD and CAD.USD, not USD.CAD), so a point move is worth the same dollars
  in each. Live, "buy 1 CAD.USD" = "sell 1/y USD.CAD."
- Return formulas differ by whether the two cross-rates share base, quote, or neither; get the
  data prep and return math right (it is the hard part, not the strategy). AUD.USD vs CAD.USD
  with Johansen hedge ratio: APR 11%, Sharpe 1.6.
- **Rollover interest**: holding a pair B.Q past 5pm ET accrues iB - iQ daily; a debit if the
  quote-currency rate is higher. Triple on Wednesday (T+2 settlement crossing the weekend),
  triple on Thursday for USD.CAD/USD.MXN (T+1). Add `log(1+iB) - log(1+iQ)` to the return.
  Often small for short-term strategies (AUD.CAD: APR 6.2% with rollover vs 6.7% without).
  Sharpe uses EXCESS return (return minus financing); financing is zero for intraday, futures,
  and dollar-neutral long-short equity.

**Roll return, backwardation, contango.** A futures position has nonzero return even if spot
is flat, because prices converge to spot at expiry. Total return = spot return + roll return.
- **Backwardation**: near contracts priced ABOVE far -> roll return POSITIVE. Mnemonic
  (Keynes): "normal backwardation," futures below expected spot, speculators compensated.
- **Contango**: near below far -> roll return NEGATIVE.
Model `F(t,T) = c*exp(mu*t)*exp(gamma*(t-T))`: total return = mu + gamma, roll return = gamma.
Regress log prices on time (spot return mu) and log futures on time-to-maturity (roll gamma,
using the 5 nearest contracts). Roll returns can dwarf spot returns (corn: roll -12.8% vs spot
2.8%; VX front contract roll ~ -50% annualized, in contango ~3/4 of the time). Roll returns
ruined a naive spot-based strategy and cost Chan >$100k in 2006. **Because of roll return,
mean reversion of spot does not imply mean reversion of the future** (VIX is stationary at 99%,
but back-adjusted front-month VX is not).

**Calendar spreads.** Long far + short near, same underlying. The log spread ~ gamma*(T1-T2),
so the signal depends ONLY on roll return, not spot. Whether it mean-reverts depends on whether
the roll return mean-reverts. CL 12-month log calendar spread: stationary at 99%, half-life 36
days; linear MR strategy APR 8.3%, Sharpe 1.3. VX calendar spread: the futures model does not
hold (VIX is not a traded asset), but the back/front RATIO is empirically stationary at 99%;
ratio-signal MR strategy APR 17.7%, Sharpe 1.5 (only post-Oct 2008, a regime marker).

**Intermarket spreads are mostly not mean-reverting.** The crack spread (long 3 CL, short 2 RB,
short 1 HO) is NOT stationary. CL vs BZ 1:1 is not stationary (BZ outperformed on US
production, Cushing bottleneck, Iran embargo). Remember synchronous prices across exchanges.

**VX vs ES (the one good intermarket spread).** Volatility is anti-correlated with the equity
index (daily-return correlation ~ -0.75). Regression on the post-Aug-2008 regime:
`ES*50 = -0.3906*VX*1000 + $77,150`, residual std $2,047. A portfolio long 0.3906 VX + long 1
ES is stationary. Bollinger short at +1 std: APR 12.3%, Sharpe 1.4. (A momentum version of
VX-ES that exploits VX roll return is in `momentum-method-and-strategies.md`.)
