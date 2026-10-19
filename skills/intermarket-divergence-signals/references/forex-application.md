# Forex Application of Intermarket Divergence (Ch.17)

Use this when applying the core divergence/IMO method (SKILL.md) to a
currency pair.

## Why forex needs extra machinery

Divergence systems on currency pairs tend to be sparse (few qualifying
extreme-and-reverse events per year), which starves a t-test-based validation
of trades. The source's worked example (USD/JPY vs. the Dollar Index, the
10-year Treasury yield [TNX], and the S&P 500) generated only 28 trades over
seven years of out-of-sample testing â€” under the 30-trade minimum for a
meaningful t-test (see `system-design-and-validation.md`). Two additions fix
this: a second intermarket confirmation market as a veto, and a volatility
breakout component to raise trade count.

## The two additions

### 1. TNX / secondary-market veto condition
Use a second correlated market as a confirmation/veto, not as an independent
signal generator, when the primary predictor's correlation with the base
security is known to be regime-dependent (e.g. USD/JPY vs. S&P 500, whose
correlation is a recent "carry trade" artifact and wasn't stable historically).
Pattern:
- Primary signal comes from the main predictor (e.g. Dollar Index regression
  divergence via IMO).
- The signal is only **executed** if a secondary market confirms â€” e.g.
  require a positive YEN-TNX disparity, OR the S&P 500 up more than 2%, before
  acting on a Dollar Index-driven buy signal.
- If the secondary market's relationship with the base security is itself
  unstable across the full backtest history, substitute an older, more stable
  proxy (TNX substituted for S&P 500 when backtesting pre-2006 data, since the
  carry-trade correlation didn't exist yet) so the veto condition is
  testable across the full sample.
- **Sign correction still applies**: when the confirmation market is
  negatively correlated with the base security, add a minus sign to its
  disparity/divergence term, exactly as in Sub-rule 2 of the main skill. Also
  note: divergence extremes between negatively correlated markets tend to run
  smaller in absolute value than between positively correlated ones â€” don't
  reuse threshold levels tuned on a positively correlated pair.

### 2. SD*ADX volatility-squeeze filter (adds a volatility-breakout leg)
`SD*ADX = Wilder's ADX * (Standard Deviation / Moving Average)` â€” combines a
volatility measure (SD relative to price level) with a trend-strength measure
(ADX). Low SD*ADX readings flag a low-volatility squeeze (the "calm before
the storm") that tends to precede a breakout, similar in spirit to a
Bollinger Band contraction but empirically found to perform better than either
Bollinger contraction or low ADX alone.
- Use SD*ADX below a low threshold (source used 0.11) as a **filter**, not a
  standalone trigger: fire a buy only if SD*ADX is below that threshold AND
  the base security subsequently breaks above its own Bollinger Band top
  within a short window (e.g. 3 days) AND the intermarket veto condition
  (above) also confirms.
- This is a distinct, additive signal leg alongside the regression/IMO leg and
  the disparity leg â€” a combined system can run all three concurrently (each
  with its own buy/sell logic) to increase trade frequency without diluting
  any single leg's specificity.

## Combined system shape (pattern, not a literal recipe to copy verbatim)

A three-leg combined system looks like:
1. **Regression/IMO leg**: 200-bar IMO of an n-day regression divergence
   between base and primary predictor crosses an extreme and reverses, subject
   to a short moving-average price-reversal confirmation and the secondary-
   market veto.
2. **Disparity leg**: n-day disparity divergence between base and secondary
   predictor crosses its own extreme and reverses, subject to a short-term
   stochastic oversold/overbought filter.
3. **Volatility-breakout leg**: SD*ADX squeeze + Bollinger Band breakout,
   subject to the same intermarket veto.
Exit conditions mirror the entry legs (opposite threshold crossings) plus a
trailing stop (e.g. cross below/above a Bollinger Band as a stop-loss leg).

## Forex-specific mechanics to carry into any implementation

- Compute correlations and divergences on **percentage yields**, matching the
  interval where the pair's correlation with its predictor(s) is strongest
  (test a range, e.g. 15-20 day yields, rather than assuming a fixed window).
- Account for carry/interest-rate differential and commission (pips) in
  return calculations â€” forex P/L isn't just price delta.
- Forex trades 24 hours, so same-day-close execution is realistic (no
  overnight gap risk assumption needed the way it would be for an equity
  system).
