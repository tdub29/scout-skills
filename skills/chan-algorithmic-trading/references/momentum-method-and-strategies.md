# Momentum: Method and Strategies (Chan Ch 6, 7)

## The four (plus one) drivers of momentum

Momentum exists for real, understandable reasons. Know the driver before trading it.

1. **Persistence of the sign of roll returns** (futures). A future stays in contango or
   backwardation for long stretches; spot return is noisy but roll return is steady, so over a
   long hold the roll return dominates and creates serial correlation of total return.
2. **Slow diffusion, analysis, and acceptance of new information** (stocks). News spreads
   slowly, so price drifts toward the new equilibrium over days (shortening as more traders
   catch on).
3. **Forced sales/purchases by funds**. Redemptions force mutual funds to dump held stocks,
   depressing prices and triggering contagion; inflows do the reverse. Index rebalances and
   leveraged-ETF rebalances force the same.
4. **Market manipulation by high-frequency traders** (intraday).
5. **Triggering of stops** (intraday only; breakout strategies). An overnight/weekend gap or a
   breached support/resistance level fires clustered stop orders that cascade.

Two types (mirror of mean reversion): **time-series momentum** (a series' own past returns
predict its future) and **cross-sectional momentum** (a series that outperformed its peers
keeps outperforming).

## Testing for time-series momentum

Correlate past return (look-back) with future return (holding), over NON-overlapping windows
(shift forward by the larger of look-back/holding). Scan look-back x holding pairs for the best
(coefficient, p-value) compromise; prefer short holding periods (better Sharpe). You can
correlate signs instead of magnitudes. Hurst + Variance Ratio detect long-term trending but
cannot pinpoint the time frame; a series often shows momentum at one horizon and mean reversion
at another (TU: Hurst 0.44 and VR fails to reject random walk, yet specific look-back/holding
pairs like 250/25 correlate at 0.27, p 0.02).

## Time-series momentum strategies

**Simple sign-of-return (Moskowitz-Yao-Pedersen).** Buy if the 12-month return is positive,
sell if negative, hold 1 month. Chan trades it daily, investing 1/25 of capital each day. TU:
Sharpe ~1.0, APR 1.7% (low because return is on ~$200k notional vs ~$400 margin, so lever it).
Works across futures with per-instrument optimal look-back/holding (BR 100/10 APR 17.7% Sharpe
1.09; HG 40/40 18.0%/1.05; TU 250/25 1.7%/1.04). Futures momentum works mainly on the
roll-return-sign persistence, so BR/HG/TU (roll return > spot return) work.

**Cleaner: use the lagged ROLL return as the signal** instead of total return. Go long above a
roll-return threshold, short below its negative, else flat. TU with 3% annualized threshold:
APR 2.5%, Sharpe 2.1, max drawdown 1.1% (better than the total-return version).

Other entries: N-day high, MA/EMA cross, upper Bollinger, up-days vs down-days; the classic
**Alexander Filter** (buy after a +x% move, reverse to short after -x% from a subsequent high).
Combining momentum + mean-reversion rules can beat either (CL: buy if price < 30 days ago but
> 40 days ago; APR 12%, Sharpe 1.1). Ready-made: S&P Diversified Trends Indicator (24 futures,
long above EMA / short below; Sharpe 1.3, max DD -16.6% 1988-2010; tradable via RYMFX/WDTI).

## Extracting roll returns directly

If total = spot + roll, isolate roll by buying the underlying and shorting the future in
contango (or the reverse in backwardation). Shorter hold, lower risk than buy-and-hold.
- Needs an instrument that tracks spot. GLD owns physical gold: long GLD / short GC. But GLD
  incurs financing cost ~ equal to the roll-return capture, so EXCESS return ~ zero. Precious
  metals only; no ETF holds other physical commodities (storage cost).
- Proxy with a producer ETF that cointegrates with spot: **XLE vs USO** (short USO + long XLE
  in contango; long USO + short XLE in backwardation). APR 16%, Sharpe ~1.
- **VX-ES roll-return momentum (Simon-Campasano).** VX roll return is huge (~ -50%) and VX is
  anti-correlated with ES. If front VX is above VIX by more than 0.1 x (trading days to
  settlement) = contango, short 0.3906 VX + short 1 ES; if below (backwardation), buy both;
  hold 1 day. APR 6.9%, Sharpe 1.0. (Use the price-based hedge ratio 0.3906 from Eq 5.11, not
  the returns-based one.)

## Cross-sectional momentum strategies

**Futures (Daniel-Moskowitz)**: rank ~52 physical commodities by 12-month return daily; long
the top, short the bottom, hold 1 month. Spot returns cancel, leaving favorable roll returns.
APR 18%, Sharpe 1.37 (2005-2007), but **-33% APR in 2008-2009** (the crisis ruined it). Works
across world indices, currencies, international and US stocks.

**Stocks**: buy top-decile 12-month-return names, short bottom decile, hold 1 month. APR 37%,
Sharpe 4.1 (mid-2007), but **-30% in 2008-2009** (Daniel-Moskowitz found 16.7% / 0.83 over
1947-2007). Rank by factors instead of returns: total = market return + factor returns, and a
cross-sectional portfolio nets out the market, leaving factor-driven returns. Factors:
earnings growth, book-to-price, PCA statistical factors; for futures, macro factors (GDP,
inflation).

**News sentiment as a factor.** Machine-readable newsfeeds + NLP sentiment scores predict
returns; buying positive-sentiment-change and shorting negative-sentiment-change names gave
APR 52-156%, Sharpe 3.9-5.3 before costs (Hafez-Xie, RavenPack). This is direct evidence that
slow news diffusion causes stock momentum. Vendors: RavenPack, Recorded Future, Thomson
Reuters, Bloomberg Event-Driven, Dow Jones Elementized.

**Forced asset sales (Coval-Stafford).** Funds facing redemptions dump held stocks (contagious
fire sale); funds with inflows add to existing holdings. Build a PRESSURE factor from the net %
of holding funds with >5% flows. Shorting top selling-pressure and buying top buying-pressure:
~17% annualized. Front-running the predictable flows: another ~17%. Post-pressure mean
reversion: another ~7%. Combined ~41% before costs (but needs ~$10k/yr CRSP data and slippage
is real).

## Pros and cons of momentum

Cons: harder to find and lower Sharpe than mean reversion (long holds = few independent
signals); **momentum crashes** for years after a crisis (S&P DTI drawdown -25.9% since Dec
2008; post-1929 a representative momentum strategy took 30+ years to recover; crash driven by
short positions rebounding); news-driven momentum keeps shortening as more traders learn it.

Pros: easy risk management (time-based exit OR stop loss; a reversed signal IS a stop, so loss
per position is bounded, unlike a mean-reverting position's unlimited downside); thrives on
black swans and high kurtosis (fat tails favor momentum); diversifies across asset classes and
countries (most futures/currencies trend), so adding momentum to a mean-reverting book raises
Sharpe and cuts drawdown.

---

# Intraday momentum strategies (Ch 7)

All four drivers except roll-return persistence operate intraday, plus stop-triggering. These
avoid the low-Sharpe and post-crisis weakness of interday momentum.

**Opening gap (breakout).** Opposite of buy-on-gap: buy when the instrument gaps UP past
yesterday's high x (1 + 0.1*std), short when it gaps DOWN past the low, exit at close. The
extended no-trade window makes the open differ from the close, firing clustered stops.
Works on futures (FSTX / DJ STOXX 50: APR 13%, Sharpe 1.4) and currencies (GBPUSD with London
open 5am ET / close 5pm ET: APR 7.2%, Sharpe 1.3; weekend gap is the natural trigger).

**Post-Earnings Announcement Drift (PEAD).** Known since 1968, still not arbitraged away. Only
use announcements AFTER the prior close and BEFORE today's open. Enter at the open: buy if the
close-to-open return >= 0.5 x (90-day close-to-open std), short if <= -0.5 std; exit at close.
Let the market decide good/bad; you do not interpret the earnings. S&P 500: APR 6.7%, Sharpe
1.5 (2011-2012), leverable ~4x to ~27%. Holding overnight loses money; the drift has shortened
to intraday as awareness grew.

**Other event drift**: earnings guidance, analyst rating changes, same-store sales, airline
load factors, M&A (~3% APR even purely technical; the acquiree can fall more than the
acquirer), index composition changes (buy adds, short deletes; also shortened to intraday).
Macro releases (FOMC, CPI) gave little EURUSD momentum; UK data / BoE moved GBPUSD for ~10 min
(pre-1999 data).

**Leveraged-ETF close rebalancing.** A 3x ETF must rebalance near the close to hold constant
leverage: if the index fell, it SELLS component stocks; if it rose, it BUYS, in the same
direction as the day's move, creating momentum. Both long and short leveraged ETFs push the
same way. Trade: buy DRN if the return from prior close to 15 min before close > 2%, sell if
< -2%, exit at close. APR 15%, Sharpe 1.8. A 1% SPX move can force trading ~17% of the
market-on-close volume. Return grows with total leveraged-ETF AUM.

**High-frequency tactics** (all exploit bid/ask size imbalance predicting the next tick; effect
stronger for lower-volume names). Order flow = signed volume (buy at ask = +, sell at bid = -)
and predicts short-term price direction because market makers read it as informed trading.
- **Ratio trade** (pro-rata markets like Eurodollar futures): join the bid when bid size >>
  ask size; you get a pro-rata fill, then sell up a tick or exit flat for commission only.
- **Ticking / quote matching** (spread > 2 ticks): buy at best bid + 1 tick, sell at best
  ask - 1 tick; if unfilled, exit at the original bid for a 1-tick loss. Needs round-trip
  commission < spread - 2 ticks.
- **Flipping / momentum ignition**: place a large buy limit at the bid (fake buying pressure) +
  a small sell at the ask; when others buy the ask expecting an uptick and fill your sell,
  cancel the big bid and buy back lower. Risk: someone fills your large order.
- **Stop hunting**: push price to a support/resistance level (or round number) to trigger
  clustered stops, then ride and cover the cascade.
These tactics only profit from slower traders; if only HFTs remain, net profit is zero. Their
prevalence shrank NBBO sizes across markets (market makers requote small to avoid being
front-run) and broke institutional orders into tiny child orders.
