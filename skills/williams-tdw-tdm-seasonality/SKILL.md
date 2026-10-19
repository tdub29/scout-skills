---
name: williams-tdw-tdm-seasonality
description: Judge whether TODAY is a historically favorable day to take a trade in a given market, using Larry Williams' Trade Day of Week (TDW) and Trading Day of the Month (TDM) seasonality filters â€” and identify which weekday/TDM number carries the long or short bias. Trigger on requests like "which weekdays are bullish for the S&P," "only trade my system on the best day of the month," "should I trade bonds today given day-of-week seasonality," "how do I count trading days into the month with holidays," or "stack a day-of-week filter on my breakout entry." Produces a pass/fail seasonality gate plus the biased weekday/TDM, not a summary of the concept.
---

# Williams TDW/TDM Seasonality Filter

## What this decides

Given a market and a calendar date, output one of:
- **PASS (long bias)** â€” today's weekday or TDM count matches a historically long-biased day for this market; take longs, skip/fade shorts.
- **PASS (short bias)** â€” same, inverted.
- **FAIL** â€” today is not a recognized bias day; either skip the trade or downgrade position size, per the trader's own stacking rules.

This is a **filter**, not a standalone system. It answers "is today a day worth acting on," not "what to buy." Apply it on top of an existing entry technique (e.g. `williams-volatility-breakout`, `williams-reversal-setups`).

## When to use

- Before taking any short-term (1-5 day hold) signal, to check if the calendar itself is working for or against you.
- When building/tuning a system and deciding which weekdays or month-position to restrict trading to.
- When a system's edge is thin and you want to compound it with a second, independent bias (TDW + TDM + intermarket trend).
- NOT for multi-week/multi-month position trades â€” TDW/TDM biases are measured and validated over 1-3 day holds.

## Method

1. **Identify the market's known bias.**
   - Measure bias two ways: **open-to-close** (the primary short-term-trader measure â€” your day starts at the open, ends at the close) and **close-to-close** (secondary/confirming). Do not use only close-to-close; it hides the intraday edge.
   - Book-documented weekday biases (verify/refresh per market before relying on them â€” these are Williams' 1977-1998 sample, not universal constants):
     - S&P 500: Monday closes above the open ~57% of the time, avg +$109/trade (open-to-close, since 1982).
     - T-Bonds: Monday open-to-close positive ~55% of the time, avg +$53; Tuesday-buy setups also documented.
     - Grains (esp. Soybeans): Wednesday bias, data back to 1968.
     - British Pound: Wednesday-open rally bias ~55% of the time.
     - Best buy weekdays tend to cluster Monday-Thursday; best sell weekdays cluster Wednesday-Thursday â€” the exact day is market-specific, never assume S&P's Monday bias transfers to Bonds.
   - Rule of thumb entry once a bias weekday is found: buy the opening of the bias day **+ X% of the prior day's range** (don't buy the raw open â€” wait for confirming follow-through), hold to the close (or use a 3-day hold variant, see sub-rule 4).

2. **Count the Trading Day of the Month (TDM), not the calendar date.**
   - TDM = the Nth trading session so far this month, counting only days the market is actually open. A month has ~22 trading days, never assume exactly 22.
   - Explicit holiday handling: if the computer/backtest says "the 15th calendar day is the bias day" but the 15th falls on a weekend or holiday, the calendar-date approach breaks (do you act Wed, Thu, or the following Monday?). TDM sidesteps this entirely â€” always count forward from trading-day 1 of the month, skipping weekends and exchange holidays, so "TDM 12" is always TDM 12 regardless of where holidays fall.
   - Maintain a running trading-day counter per instrument/exchange calendar; reset to 1 on the first session of each new month.

3. **Check the market's documented TDM setup windows.**
   - TDM windows are month-turn and mid-month effects, not spread evenly across the month. Book-documented examples (verify per market, these decay/shift over time):
     - T-Bonds: buy TDM 18 (3-day exit, ~$1,500 stop) â€” better still, delay to TDM 22 (fewer occurrences/month, higher accuracy in the source sample). Sell TDM 12 (3-day exit, ~$1,400 stop) for the mid-month dip.
     - S&P 500 and Bonds both: end-of-month rally â€” buy the third-to-last trading day of the month, hold ~6 sessions.
     - Bonds: Oops!-style reversal entries taken from TDM 1 through TDM 5 (spillover of the month-end rally into the new month).
     - "Oops! after the 17th trading day" â€” an S&P/Bonds reversal-pattern entry timed to trigger after TDM 17, riding the same end-of-month tendency.
   - TDM is a **setup**, not an automatic trigger â€” treat a TDM window as "pay attention, a bias trade is live here," then still require your entry technique's own confirmation before acting. Do not blindly auto-fire on TDM alone.

4. **Stack TDW + TDM + a trend/intermarket filter as a compound gate.**
   - Each filter independently cuts the trade count and raises average profit per trade / cuts drawdown; stacking multiplies the effect but shrinks trade frequency further â€” that's the intended trade-off (fewer, better trades).
   - Documented stacking example: S&P volatility breakout + best-TDW-only + Bond-trend-confirmation (bonds up over 5 days = bullish stocks, down over 35 days = bearish) took average profit/trade from $228 (unfiltered) â†’ $281 (bond filter only) â†’ $444 (bond filter + best TDW), while trade count and drawdown both fell.
   - Documented TDM stacking example: Bond TDM 18 buys, filtered to only fire when Gold is in a downtrend (Gold's close < its close 24 days ago) â€” accuracy and average profit per trade rose while drawdown was cut roughly in half; TDM 12 sells, filtered to only fire when Gold is in an uptrend (Gold's close > its close 10 days ago), cut drawdown-to-profit ratio from ~21% to ~11%.
   - Order of stacking: seasonality (TDW/TDM) first to select the day, then an intermarket-trend filter to select the environment, then your entry trigger (breakout, pattern, reversal) to select the exact trade.

5. **Choose the hold: same-day close vs. 3-day variant.**
   - Base measurement: enter on the open of the bias day, exit on that day's close (day-trade version).
   - 3-day-hold variant: enter on the open of the bias day, exit 3 trading days later on the close, or on a protective stop (~$1,500-$2,500 depending on market), whichever comes first. Williams reports this variant still beats a random-walk baseline for most markets tested (Bonds and S&P showed the strongest edge; Gold showed none â€” verify before assuming any market's 3-day hold works, don't extrapolate blindly).
   - Longer hold or larger stop generally raises average profit per trade at the cost of fewer qualifying occurrences per month â€” pick per your risk tolerance, not by default.

## Sub-rules / failure modes

- **Don't measure bias close-to-close only.** A short-term trader's "day" runs open-to-close; a close-to-close measure blends in the next day's overnight gap and will misstate the actual tradable edge.
- **Count trading days, not calendar days, for TDM â€” with explicit holiday logic.** Skipping this is the single most common implementation bug: hardcoding "the 15th of the month" instead of "the 15th session of the month" silently breaks every month a holiday shifts the count.
- **Every market has its own bias days and TDM windows â€” never transplant one market's calendar onto another.** S&P's Monday bias, Bonds' Tuesday bias, and grains' Wednesday bias are three separate, independently-measured findings; a bias must be (re-)measured per instrument before you rely on it.
- **TDM is a setup/leading indicator, not an unconditional signal.** Treat a TDM window hit as permission to look harder at the trade, not as the trade itself â€” the source explicitly reserves judgment at each occurrence rather than trading every one mechanically.
- **Stacked filters cut trade frequency â€” that's a feature.** If a stacked TDW+TDM+trend filter is producing as many trades as the unfiltered system, the stack isn't actually constraining anything; re-check the filter logic.
- **Biases can decay or shift.** These are historical measurements from specific sample windows (e.g. S&P since 1982, Bonds since 1977, grains since 1968); re-validate on recent data before hard-coding a bias day into a live system.

## Worked mini-example

Instrument: T-Bonds. Question: "Is today a valid TDM buy day, and should I take it?"

1. Count trading days elapsed this month, skipping weekends/holidays â†’ today is TDM 18.
2. Check the market's documented TDM window table â†’ TDM 18 is a known Bond buy window (base case: 139 trades since 1986, net $34,875, avg $250/trade, $8,625 drawdown).
3. Apply the intermarket stack: check Gold's close today vs. 24 trading days ago. If Gold's close < 24-days-ago close (Gold downtrending) â†’ filter PASSES, confidence upgraded (documented result: accuracy up, avg profit/trade up ~$100, drawdown roughly halved). If Gold is not downtrending â†’ filter still technically fires (TDM 18 alone is tradeable) but without the confirmation, size down or skip per the trader's stacking policy.
4. Decide hold: 3-day exit with a $1,500 stop (the documented rule for this setup) rather than an intraday-only exit, since TDM setups in this book are validated on a 3-day hold.
5. Output: **PASS (long bias), TDM 18, Gold-confirmed** â†’ enter on today's open with the $1,500 stop, exit on close 3 trading days out.

## References

- Source: Larry Williams, *Long-Term Secrets to Short-Term Trading* (Wiley, 1999) â€” Chapter 4 (TDW basics on Bonds/S&P volatility breakouts), Chapter 6 (TDW + TDM tables, weekday bias by market, TDM setup windows, monthly road maps), Chapter 10 (worked TDM 18/22/12 examples with Gold-trend stacking).
- Sibling skills: `williams-volatility-breakout` (the entry technique this filter sits on top of), `williams-greatest-swing-value` (an alternate volatility measure to combine with TDW/TDM), `williams-position-sizing` (how a stacked-filter's higher accuracy should change bet size), `williams-reversal-setups` (Oops!-pattern entries that combine directly with TDM windows, e.g. "Oops! after the 17th trading day"), `williams-bailout-exit` (the alternate exit technique referenced for turning a TDW day-trade into a larger-profit trade).
