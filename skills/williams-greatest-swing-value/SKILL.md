---
name: williams-greatest-swing-value
description: Compute a Greatest Swing Value (GSV) entry offset from failure swings â€” the average open-to-high (buy) or open-to-low/open-to-close (sell) move on days that closed against the signal direction, scaled by ~180-225% and added to or subtracted from tomorrow's open. Use when the user wants to set a specific entry price off a volatility measure derived from recent failed swings, wants a Talon/Chalek-style greatest-swing-value system, asks "how far above/below the open should I buy/sell," needs a contra-trend fade level or support/resistance band from swing values, or references GSV, failure swings, Talon system, or Mike Chalek by name. Not for range-breakout entries off yesterday's full range (see williams-volatility-breakout) or for exit/stop placement alone (see williams-bailout-exit).
---

# Williams' Greatest Swing Value (GSV)

## What this decides

A single number: the dollar/point offset from tomorrow's opening price at
which to place a buy-stop (above the open) or sell-stop (below the open),
derived from how far price has recently swung *against* the eventual close â€”
i.e., swings that failed to hold. Generalizes Mike Chalek's "Talon" system.
Output is an entry price, gated by an overbought/oversold setup â€” not a
standalone signal.

## Core logic: failure swings, not full range

A "failure swing" is the amount price moved in one direction on a day that
then closed in the *opposite* direction â€” proof the market could swing that
far and still not hold it:

- **Buy swing** = `open to high`, measured **only on down-close days** (close < open). This is how far the market rallied before sellers won the day.
- **Sell swing** = `open to low` (or `open to close`, see sub-rule 1), measured **only on up-close days** (close > open). This is how far the market fell before buyers won the day.

The logic: if tomorrow's move exceeds the recent failure-swing average, that
is fresh, unprecedented buying/selling pressure â€” proof the market is
"tracking in fresh ground" â€” not just noise the market has already
absorbed and rejected.

## When to use

- Setting a specific entry price for tomorrow, not just a directional call.
- You already have (or are building) an overbought/oversold setup and need
  a volatility-scaled trigger distance, not an arbitrary tick count.
- Building or reproducing Williams'/Chalek's bond, S&P, or generic
  GSV systems.
- Fading an overextended intraday move (contra-trend variant) or finding a
  rough support/resistance band.

Do not use when: you want a breakout off yesterday's full high-low range
(use `williams-volatility-breakout` instead) or you only need a stop/exit
rule (use `williams-bailout-exit`).

## Method

1. **Pick N (lookback window).** Use 1-4 days. Williams tested up to 10 days
   expecting more stability from more observations and found the opposite:
   1-4 days consistently outperformed. Default to 4 unless you have evidence
   for a shorter window.

2. **Compute the raw swing series for each of the last N days**, direction-filtered:
   - For a **buy** signal: `open_to_high[i] = high[i] - open[i]`, but only include day `i` if `close[i] < open[i]` (down-close day).
   - For a **sell** signal: `open_to_low[i] = open[i] - low[i]`, only if `close[i] > open[i]` (up-close day). (Williams also used `open[i] - close[i]` on up-close days in the bond system â€” see sub-rule 1.)

3. **Average the filtered swings** over the N days to get the GSV:
   `GSV_buy = mean(open_to_high on down-close days, last N)`
   `GSV_sell = mean(open_to_low on up-close days, last N)`

4. **Scale it.** Multiply by a percentage in the ~180-225% range:
   - 180% is Williams' standard entry multiplier (both buy and sell sides, both bonds and S&P).
   - 225% of the GSV is his standard *stop* distance from the open when trading the long/short established by the 180% entry.
   - Chalek's original Talon used asymmetric 80% (buy) / 120% (sell) â€” evidence the exact percentage is tunable per market, not fixed law. Backtest before trusting a percentage outside 80-225%.

5. **Apply an overbought/oversold setup filter before computing the entry** â€” GSV is a volatility offset, not a directional signal by itself:
   - Buy setup: today's close < close N-days-ago (e.g., 5 days ago for bonds, 6 for S&P) â€” market is oversold, due for failure-swing rally.
   - Sell setup: today's close > close N-days-ago (mirror, e.g., 6-day lookback) â€” market is overbought.
   - Only compute/place the GSV entry when the corresponding setup fires.

6. **Set the entry price:**
   - Buy: `entry = tomorrow_open + (GSV_buy x scaling%)`
   - Sell: `entry = tomorrow_open - (GSV_sell x scaling%)`
   Place as a stop order at that price once tomorrow's open is known.

7. **Layer the TDW (day-of-week) and intermarket filters** (see sub-rules 4-5)
   before finalizing whether to place the order at all.

## Sub-rules and failure modes

1. **Sell-swing definition varies by market â€” check both.** In the bond
   system Williams defines the sell swing as `open to low` (mirroring the
   buy swing's `open to high`). Elsewhere he generalizes it as `open to
   close` on up-close days ("the amount price could decline without
   triggering a down close day"). These are NOT the same number â€” open-to-low
   is always >= open-to-close on an up day. Default to `open to low` for
   symmetry with the buy side; only switch to `open to close` if you're
   reproducing a specific published result that used it, and document
   which you used.

2. **The direction filter is not optional â€” averaging unfiltered swings
   defeats the concept.** Averaging open-to-high across *all* days (not
   just down-close days) mixes in "buying that succeeded" with "buying that
   failed," diluting the signal into a generic volatility measure. If you
   skip the close-direction filter you've built `williams-volatility-breakout`
   (full-range breakout), not GSV â€” route there instead.

3. **N â‰  10.** Williams explicitly tested a 10-day window on the assumption
   that more data would stabilize the average and found 1-4 days won. Longer
   windows stale the measurement â€” swing size should track *current*
   volatility regime, not a smoothed long-run average. Default to 4;
   backtest 1-4 explicitly before shipping any other N.

4. **TDW gates which days you're even allowed to act on.** Williams'
   examples restrict buys to specific days (e.g., Tuesday/Wednesday/Friday
   for bonds; Monday/Tuesday/Wednesday for S&P) and sells to the complement.
   Compute the GSV entry every day, but only submit the order on an allowed
   TDW day â€” this is a hard filter, not a tiebreaker. See
   `williams-tdw-tdm-seasonality` for the day-of-week reference tables.

5. **Add an intermarket filter for markets driven by rates.** Bonds:
   compare gold's trend (buy setup wants gold lower than 20 days ago).
   S&P: compare bonds' trend (buy setup wants bonds closing higher than 15
   days ago; sell wants bonds lower than 15 days ago) â€” Williams' framing
   is "Bonds are the dog that wags the tail, which is stocks." Skipping
   this filter is not wrong, but historically cut into performance
   materially in his tests â€” treat it as a strong recommendation for
   rate-sensitive instruments, not a hard requirement for every market.

6. **Two distinct applications â€” don't conflate them.** (a) *Breakout
   entry*: buy/sell stop placed beyond the GSV offset expecting continuation
   once that fresh ground is broken (the bond/S&P systems above). (b)
   *Contra-trend fade*: sell into strength at the GSV offset above the open
   (expecting resistance) and buy into weakness at the GSV offset below the
   open (expecting support), with a stop-and-reverse just beyond the level â€”
   this is the *opposite* trade direction from (a) at the *same* price level.
   State explicitly which application you're building; the offset math is
   identical, the order type and expected reaction are opposite.

7. **This is a "dumb" mechanical technique â€” trade every signal or don't
   trade it at all.** Williams is explicit: cherry-picking which GSV signals
   to take reliably means skipping winners and keeping losers. If the
   downstream use case wants a discretionary overlay, say so up front;
   don't silently add a "does this look good" filter on top of GSV signals.

## Worked mini-example (bonds, from the book)

Setup check for a long: today's close < close 5 trading days ago, AND
today is Tuesday, Wednesday, or Friday. Setup fires.

1. N = 4 days. Open-to-high on the last 4 down-close days averages 3.57 (the 4-day sell-side average in the book's S&P table; use the analogous buy-side number for bonds).
2. Scaling = 180% for entry, 225% for stop.
3. Entry offset = 3.57 x 1.80 â‰ˆ 6.43 above/below the open (S&P example: 5.50 points below a 1092.20 open â†’ buy stop at 1086.70).
4. Stop offset = 3.57 x 2.25 â‰ˆ 8.03 (book rounds to 8.00) beyond the open on the far side of the position â†’ stop at 1084.20 for a long entered at 1086.70 off a 1092.20 open.
5. Exit: first profitable opening after 2 days in the trade, or a fixed dollar stop ($1,600 bonds / $2,500 S&P in Williams' tests) / bailout exit â€” see `williams-bailout-exit`.

## References

- Source: Larry Williams, *Long-Term Secrets to Short-Term Trading* (1999, Wiley), Chapter 8, "Separating the Buyers from the Sellers" (GSV concept, pp. 121-129) and Chapter 4 (Chalek/Talon precursor, pp. 71-72).
- Siblings: `williams-volatility-breakout` (full prior-range breakout entries â€” the non-direction-filtered cousin of GSV), `williams-tdw-tdm-seasonality` (day-of-week/month filters referenced in sub-rule 4), `williams-position-sizing`, `williams-reversal-setups` (oversold/overbought setup construction referenced in method step 5), `williams-bailout-exit` (exit rules referenced in the worked example).
