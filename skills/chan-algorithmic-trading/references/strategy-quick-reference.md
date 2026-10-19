# Strategy Quick Reference (Chan, all chapters)

Every named strategy in the book: camp, instrument, signal, why it should work, reported
unlevered APR / Sharpe, and the pitfall that most threatens it. Metrics are the book's backtest
figures (no transaction costs, S&P universe often has survivorship bias); treat them as
illustrative, not promises. Deeper mechanics in `mean-reversion-strategies.md` and
`momentum-method-and-strategies.md`.

## Mean reversion

| Strategy | Instrument | Signal / rule | Rationale | APR / Sharpe | Key pitfall |
|---|---|---|---|---|---|
| Linear Z-score (parameterless) | Any stationary series or cointegrating portfolio | Units = -Z-score of price vs MA(look-back=half-life) | Regression to the mean; no free parameters = no data-snooping | EWA-EWC-IGE 12.6% / 1.4 | Needs unbounded capital; use Bollinger instead |
| Bollinger bands | GLD-USO spread | Enter at Z=+/-1, exit at 0 | Practical bounded version of linear MR | 17.8% / 0.96 | Data errors inflate; picks entry/exit params |
| Kalman-filter pair | EWA-EWC | Enter when forecast error e < -sqrt(Q) | Dynamic hedge ratio + mean/std without arbitrary look-back | 26.2% / 2.4 | Tuning delta, Ve on training data |
| Buy-on-gap (long-only) | S&P 500 stocks intraday | Gap down < -1 std AND open > 20-day MA; buy 10 lowest; exit at close | Panic selling at open reverts intraday; MA = momentum filter | 8.7% / 1.5 | Signal noise (preopen vs official open); primary-vs-consolidated; survivorship |
| Short-on-gap | S&P 500 stocks intraday | Mirror of buy-on-gap | Same, inverted | 46% / 1.27 | Short-sale constraint; steep drawdown |
| Index arb (subset) | SPY vs ~98 component stocks | Johansen-select cointegrating stocks, linear MR on log spread | Basket cointegrates with ETF; subset widens the edge | 4.5% / 1.3 | Decays without retraining; short-sale on stock leg |
| Cross-sectional linear long-short | S&P 500 stocks | w_i = -(r_i - r_mkt)/sum|r-r_mkt|, dollar-neutral, daily | Relative returns serially anti-correlate | 13.7% / 1.3 (close-to-close); 73% / 4.7 (intraday) | Intraday: 2x costs + signal noise |
| FX cross-rate pair | AUD.USD vs CAD.USD | Johansen hedge ratio, linear MR, common quote currency | Commodity economies cointegrate | 11% / 1.6 | Wrong quote-currency math; rollover interest |
| FX pair w/ rollover | AUD.CAD | Linear MR, add rollover interest to return | Same, accounting for carry | 6.2% / 0.54 | Triple rollover Wed/Thu; T+1 vs T+2 |
| Calendar spread | CL 12-month | Linear MR on log spread ~ gamma; look-back = half-life (36d) | Roll return (not spot) mean-reverts | 8.3% / 1.3 | Must price-back-adjust; seasonality |
| Calendar spread (ratio) | VX back/front | Linear MR on back/front ratio | Empirical stationarity (model fails for VX) | 17.7% / 1.5 | Only post-Oct-2008 regime |
| Volatility vs index (MR) | VX + ES | Long 0.3906 VX + 1 ES; short at +1 std | Vol anti-correlated with equity index; the one good intermarket spread | 12.3% / 1.4 | Regime split (~Aug 2008); different point values |

## Momentum

| Strategy | Instrument | Signal / rule | Rationale | APR / Sharpe | Key pitfall |
|---|---|---|---|---|---|
| Time-series sign-of-return | TU (and BR, HG) futures | Buy if 12-mo return > 0, hold 1 mo; daily 1/25 tranche | Persistent sign of roll return | TU 1.7% / 1.04; BR 17.7% / 1.09; HG 18.0% / 1.05 | Few independent signals; data-snooping |
| Roll-return-signal momentum | TU futures | Long/short on lagged roll return vs +/- threshold | Cleaner proxy than total return | 2.5% / 2.1 | Roll-return estimation |
| Cross-sectional futures momentum | ~52 commodities | Rank 12-mo return; long top / short bottom, hold 1 mo | Spot returns cancel, roll returns remain | 18% / 1.37 (05-07), -33% (08-09) | Momentum crash after crisis |
| Cross-sectional stock momentum | S&P 500 | Long top-decile / short bottom-decile 12-mo return, hold 1 mo | Slow news diffusion | 37% / 4.1 (2007), -30% (08-09) | Momentum crash |
| News-sentiment factor | US stocks | Long positive / short negative sentiment change | Slow diffusion of news, quantified | 52-156% / 3.9-5.3 (pre-cost) | Vendor/algorithm dependence, costs |
| Forced-sale (Coval-Stafford) | US stocks | Trade on fund PRESSURE factor (momentum + front-run + reversion) | Redemption fire sales move held stocks | ~41% combined (pre-cost) | ~$10k/yr CRSP data; slippage |
| Roll-return extraction | XLE vs USO | Short USO+long XLE in contango; reverse in backwardation | Capture roll return via spot proxy | 16% / ~1 | Producer ETF may not track spot |
| Roll-return extraction | GLD vs GC | Long GLD / short GC | Capture gold roll return | 1.9% but ~0 excess | GLD financing cost ~ eats the roll |
| VX-ES roll momentum (Simon-Campasano) | VX + ES | Short both in contango / buy both in backwardation vs VIX, hold 1 day | Large VX roll + VX-ES anti-correlation | 6.9% / 1.0 | Use price-based hedge ratio 0.3906 |
| Opening gap (breakout) | FSTX future | Buy gap up / short gap down past prior high/low, exit at close | Clustered stops fire on gap | 13% / 1.4 (FSTX); GBPUSD 7.2% / 1.3 | Define open/close per market |
| PEAD | S&P 500 stocks | After-close earnings; buy if C2O return >= 0.5 std, short if <= -0.5, exit at close | Slow drift after earnings, direction set by market | 6.7% / 1.5 (leverable ~4x) | Overnight loses; drift shortened to intraday |
| Leveraged-ETF close | DRN (3x REIT) | Buy if close-to-15min-before-close return > 2%, sell if < -2%, exit at close | Forced constant-leverage rebalancing near close | 15% / 1.8 | Grows with leveraged-ETF AUM |
| HFT: ratio trade / ticking / flipping / stop hunt / order flow | Order book | Bid/ask size imbalance predicts next tick; signed order flow predicts direction | Microstructure imbalance and informed flow | (latency-dependent) | Only profits from slower traders; shrinking NBBO sizes |

## Sizing (applies to all)

| Method | When | Formula / rule |
|---|---|---|
| Kelly | Gaussian returns, sanity-check upper bound | f = m / s^2; multi: F = C^-1 M |
| Half-Kelly | Default deployment | f_deploy = 0.5 * Kelly f |
| Monte-Carlo growth optimization | Fat-tailed returns | maximize < log(1+f*R) > over Pearson-system draws |
| CPPI | Hard drawdown cap -D, single strategy | trade D of equity at Kelly f, rest in cash; reset only at new highs |
| Stop loss | Momentum: natural. Mean reversion: only beyond backtest max drawdown | reversed signal = de facto momentum stop |

## Cross-cutting rationale (the "why")

- **Simple linear > complex nonlinear**: fewer parameters and rules = less data-snooping.
- **Mean reversion**: capped upside, unlimited downside, high Sharpe, needs a fundamental story,
  stops fight the entry. Dominant in stocks/ETFs and manufactured spreads.
- **Momentum**: unlimited upside, bounded downside, lower Sharpe, thrives on fat tails, crashes
  after crises, stops are natural. Dominant in futures/currencies.
- **Roll return** is the hinge of futures behavior: it drives futures momentum (persistent
  sign) and prevents spot mean reversion from carrying to the future.
- **Regime change** is the ever-present risk: any strategy can stop working when the underlying
  inefficiency or relationship breaks; understand the inefficiency so you can spot and repair
  the break.
