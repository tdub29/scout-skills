---
name: intermarket-divergence-signals
description: Build a normalized intermarket divergence score and a 0-100 Intermarket Momentum Oscillator (IMO) reading that flags decoupling between a base security and one or more correlated predictor markets, then convert the extreme reading into a buy/sell/short/cover threshold-crossing signal. Use when the user wants to (1) build an intermarket divergence signal between two correlated securities, e.g. "build me an intermarket divergence signal between crude oil and XLE"; (2) turn a known correlation into a mean-reversion oscillator, e.g. "these two markets are correlated 0.85, give me a 0-100 oscillator that flags when they decouple far enough to trade the reversion"; (3) combine 2-3 predictor markets into one oscillator without double-counting shared variance, e.g. "combine SPX, EuroStoxx and the VIX into one intermarket momentum oscillator using part-correlation weighting"; (4) turn a regression predicted-vs-actual gap into a signal, e.g. "gold vs gold miners regression divergence with thresholds"; (5) compute a Bollinger Band, disparity, LRS, or Z-score divergence between a correlated pair and get the threshold crossing to go long/short. Also covers system-design validation (walk-forward testing, Profitability/PRR/Luck Coefficient/Efficiency/t-test metrics) so a built system can be judged genuinely tradable, intermarket relative-strength asset-allocation rotation across asset classes, and forex-specific application with a TNX/CRB veto and SD*ADX volatility filter. Source: Katsanos, "Intermarket Trading Strategies" (Wiley, 2009), Ch.9 (core), Ch.10, Ch.16, Ch.17 (bundled references).
---

# Intermarket Divergence Signals

## What this decides

Given a base security (the one you want to trade/predict) and 1-3 correlated
intermarket predictor securities, this skill produces:

1. A **divergence score** â€” a scale-free number describing how far the base
   security has decoupled from what its correlated predictor(s) imply it
   should be doing, using one of five structurally parallel formulas.
2. A **0-100 Intermarket Momentum Oscillator (IMO)** reading â€” the divergence
   score normalized against its own trailing extremes, comparable across any
   pair of markets regardless of price scale.
3. A **threshold-crossing signal** (buy / sell / short / cover) derived from
   the IMO or raw divergence peaking/bottoming past a chosen extreme level and
   reversing.

This is not a trend indicator. Divergence is a **leading, mean-reverting**
concept: it flags decoupling, not direction of the next trend. Always wait for
the indicator to peak/bottom and reverse before signaling â€” never act on the
extreme reading alone.

## When to use

- Two (or a small basket of) securities are meaningfully correlated (|r| roughly
  0.4-0.8) and the user wants to trade the base security when it detaches from
  what the correlated market(s) imply.
- The user names a specific divergence flavor (Bollinger, disparity, LRS,
  regression, Z-score) or just says "divergence" / "decoupling" / "oscillator"
  / "part-correlation weighting" for an intermarket pair or basket.
- Do NOT use this for single-market technical divergence (e.g. RSI vs. price on
  the same instrument) â€” that's classic TA, not intermarket. This skill always
  needs a *second* data source.

## Method

### Step 1 â€” Establish and validate the relationship first
Before building any divergence formula, confirm the predictor is usable:
- Compute Pearson's r between base and predictor **percentage yields** (not
  raw prices â€” raw price series violate the linearity/normality assumptions
  regression and Z-scores depend on). Use a yield interval matched to your
  holding period; correlations rise with longer yield intervals up to a point,
  then plateau (a ~9-day yield interval is a reasonable default for
  short/medium-term systems; test intraday intervals empirically if day-trading).
- Note the **sign** of the correlation â€” you will need it in Step 3.
- If combining more than one predictor, check the predictors' correlation
  with each other (see Sub-rule 3).

### Step 2 â€” Pick and compute one divergence formula
All five formulas below share the same shape: compute a normalized position/
value for both securities from the *same* transform, then subtract predictor
from base (or base from predictor, sign-adjusted â€” pick one convention and
stay consistent). Smooth the raw subtraction with a short EMA (e.g. 3-day) to
cut noise.

| Formula | Base security transform | Divergence |
|---|---|---|
| **Bollinger Band Divergence** | Relative position in its own Bollinger Bands: `SEC_BOL = 1 + (C - MA + 2*SD) / (4*SD)` (0 = lower band, 1 = upper band, +1 offset removes negative values) | `EMA(3)[(SEC2_BOL - SEC1_BOL) / SEC1_BOL * 100]` |
| **Intermarket Disparity** | Percent distance from its own moving average: `DS = (C - MA(C,n)) / MA(C,n) * 100` | `ID = c * DS2 - DS1` (c = Â±1, see Sub-rule 2) |
| **LRS Divergence** | Linear regression slope of price over n bars, volatility-adjusted | `slope(SEC2)_adj - slope(SEC1)` |
| **Regression Divergence** | Predicted yield from the regression equation: `Y_pred = r * StDev(Y)/StDev(X) * X` (add intercept term if scatterplot shows the line doesn't cross the origin) | `Y_pred - Y_actual` |
| **Z-Score Divergence** | Standardized position: `Z = (C - MA) / SD` | `(Z2 - Z1) * r` (correlation-weighted) |

Values are unbounded and scale differently per market pair â€” that's expected;
Step 3 fixes it.

### Step 3 â€” Normalize with the Intermarket Momentum Oscillator (IMO)
Extreme divergence levels differ by market pair because of price-scaling
differences, so automate threshold-finding with:

```
IMO = MA(3, Indicator - Lowest(Indicator, 200)) * 100
      / MA(3, Highest(Indicator, 200) - Lowest(Indicator, 200))
```

This rescales any of the five divergence formulas to 0-100 on a rolling
200-bar lookback, so thresholds are comparable across pairs. Interpret it
like a stochastic, but reversed in intent â€” you want to buy at maximum
positive divergence and sell at maximum negative divergence:
- Buy when IMO falls below a floor (e.g. 30) then rises back above it; sell
  the mirror image above a ceiling (e.g. 80).
- Wider bands for trending markets: buy below 30 then above 40; sell above 90
  then below 80 â€” avoids getting stopped out while divergence stays pinned in
  the overbought/oversold zone during a strong trend.
- Or: buy/sell on IMO crossing its own short moving average (signal line).

### Step 4 â€” Combine multiple predictors (if more than one)
If using 2-3 predictor markets, do not just average their raw divergences â€”
weight each by its **part (semi-partial) correlation** with the base security
so shared variance isn't double-counted (see Sub-rule 3). Sum the
part-correlation-weighted divergences, then run the combined series through
Step 3's IMO normalization.

### Step 5 â€” Set thresholds and emit the signal
- Pick an extreme level per side (book examples range +10 to +40 positive,
  -10 to -40 negative, or 70/30 and 80/50 on the IMO scale). There is no
  universal number â€” back-test peak/trough behavior for the specific pair.
- Signal fires only on **peak-and-decline** (sell/short) or
  **trough-and-rise** (buy/cover) past the threshold â€” never on the raw
  extreme value alone, since divergence indicators lead price and can stay
  extreme for a while.
- If correlation is negative (Sub-rule 4), the "buy" and "sell" polarity of
  the raw divergence flips â€” verify against a known historical decoupling
  event before trusting the sign.

### Step 6 â€” Report the artifact
Deliver: (a) the divergence formula used and its current smoothed value, (b)
the IMO 0-100 reading, (c) the threshold levels chosen and why, (d) the
resulting signal (buy/sell/short/cover/none) with the bar where it triggered,
and (e) the correlation coefficient(s) and lookback window used, so the user
can audit the inputs.

## Sub-rules and failure modes

1. **Structural parallel, not five separate systems.** All five formulas
   (Bollinger, disparity, LRS, regression, Z-score) are the same idea â€”
   normalize both securities the same way, then subtract. Don't reinvent per
   formula; reuse the same EMA-smoothing and threshold-crossing signal logic
   across all five and let the user pick the flavor that fits their data
   (Z-score for eyeballing multiple markets on one chart, regression when you
   want an explicit predicted value, disparity/Bollinger when you just want a
   fast oscillator, LRS when trend slope matters more than level).

2. **Sign-flip for negative correlation.** Intermarket Disparity and
   Z-Score Divergence both require a correlation-sign correction (`c = -1`
   when base and predictor are negatively correlated, e.g. gold vs. the
   dollar index). Skipping this silently inverts every buy/sell call. Bollinger
   Band Divergence has no such correction term and is documented to work
   poorly on negatively correlated pairs because of the scaling assumptions â€”
   prefer disparity or Z-score for negatively correlated pairs.

3. **Part-correlation weighting when combining predictors (cap â‰ˆ3).**
   Two correlated predictors both "explaining" the base security share
   variance; naively adding their divergences double-counts it. Weight each
   predictor by its part correlation:
   `r_y1(2) = (r_y1 - r_y2*r_12) / sqrt(1 - r_12^2)` (and the symmetric
   `r_y2(1)` for the second predictor). Practical cap: it is rarely feasible
   to find more than about three predictor markets that are simultaneously
   well-correlated with the base security and weakly correlated with each
   other â€” beyond that, added predictors contribute noise, not signal.

4. **0.80 correlation ceiling between predictors.** When choosing which
   predictor markets to include, keep pairwise correlation between predictors
   below ~0.80 â€” above that the weighting becomes unstable (near
   multicollinearity). A predictor with near-zero correlation to the base
   security can still help if it's correlated with your *other* predictors and
   absorbs shared noise that isn't relevant to the base security â€” don't drop
   low-r predictors reflexively without checking their part correlation.

5. **Normality assumption is fragile â€” say so.** Bollinger, Z-score, and
   regression divergence all assume the underlying price/yield distribution is
   normal (they use standard deviation as the unit of measure). Financial
   series are rarely normal. This isn't disqualifying, but: (a) always compute
   correlation and regression coefficients on **percentage yields**, not raw
   prices, to get closer to the normality/linearity assumptions the math
   needs; (b) flag to the user that in periods of serious non-normality
   (fat tails), further decoupling is more likely than the normal-distribution
   math implies â€” divergence can keep going before it reverts.

6. **LRS needs a volatility adjustment, and disparity/LRS have no natural
   ceiling.** Unlike Bollinger/Z-score (bounded by construction) or IMO
   (normalized to 0-100 by construction), raw Intermarket Disparity and LRS
   Divergence have no natural upper/lower bound â€” their extreme levels are
   pair-specific and must be back-tested, not assumed from another pair's
   thresholds. When comparing slopes across two securities with different
   volatilities, scale the intermarket security's regression slope by the
   ratio of standard deviations before subtracting, or the "divergence" is
   just measuring which security is more volatile, not which is decoupling.

## Worked mini-example

Base: Gold ETF (GLD). Predictor: Dollar Index (DXY). 9-day % yields, 15-year
Pearson r = -0.33 (negative â€” dollar up, gold down).

1. Compute `DS1` (GLD 30-day disparity) and `DS2` (DXY 30-day disparity).
2. Apply the sign correction: `c = -1` (negative correlation).
3. `ID = -1 * DS2 - DS1`. Positive ID now correctly means gold is
   under-performing what a *falling* dollar implies it should do (bullish
   divergence for gold), because the sign flip makes DXY weakness read as a
   positive contribution.
4. Feed `ID` into the IMO formula over a 200-day lookback â†’ 0-100 reading.
5. Chosen thresholds from back-testing this pair: buy when ID (or IMO) peaks
   above +3% and turns down... no â€” for a bullish gold divergence you act on
   ID bottoming below a *negative* extreme and turning up (gold has further to
   catch up); short-lived positive spikes above +3% that reverse are the sell
   side. Confirm polarity against one known historical divergence (e.g. a
   dollar rally with gold failing to fall) before trusting the automated
   signal.
6. Report: "ID = +2.1 (bottomed at -4.3 five days ago, now rising) â†’ IMO = 34
   â†’ no new signal yet; watch for IMO crossing back above 30 to confirm the
   reversal a buy."

## References

- `references/system-design-and-validation.md` â€” Ch.10: walk-forward testing,
  cluster spotting / profit mapping, and the Katsanos/Harris/Vince
  profitability metrics (Profitability Rating Ã—10, Pessimistic Rate of
  Return, Luck Coefficient, Entry/Exit/Total Efficiency, t-test with
  normality/autocorrelation/sample-size caveats) â€” use this to decide whether
  a divergence system you built is genuinely tradable or curve-fit before
  going live.
- `references/asset-allocation-rotation.md` â€” Ch.16: ranking asset
  classes/ETFs by relative strength vs. an S&P 500 benchmark and rotating
  capital into the strongest, static vs. dynamic rebalancing.
- `references/forex-application.md` â€” Ch.17: applying regression divergence /
  IMO / disparity to currency pairs, plus a TNX/CRB two-market intermarket
  veto condition and an SD*ADX volatility-squeeze filter for timing entries.
- Katsanos, Markos. *Intermarket Trading Strategies*. Wiley, 2009. Chapter 9
  (Intermarket Indicators â€” primary source for all formulas above), Chapter
  3/8 (base regression equation), Chapter 10, Chapter 16, Chapter 17.

Sibling skills: none currently carved from this book.
