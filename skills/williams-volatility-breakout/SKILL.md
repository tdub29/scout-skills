---
name: williams-volatility-breakout
description: Build a Larry Williams-style volatility-breakout entry â€” a buy/sell stop set at today's open plus/minus a percentage of yesterday's range, paired with a protective dollar stop and a bailout exit, optionally filtered by TDW and bond-trend. Use when the user wants a mechanical momentum/breakout entry price, asks what percent of yesterday's range to add to the open, wants an "explosion of price" or "expansion in volatility" system, needs a range-multiplier calibrated per market, or wants Williams' open-based breakout coded up (crude, bonds, S&P, or any futures/equity market with daily OHLC).
---

# Williams Volatility Breakout

## What this decides

Given yesterday's daily range (high âˆ’ low) and today's open, this skill produces two concrete stop-order
prices â€” a buy-stop above the open and a sell-stop below the open â€” plus the paired protective stop and
exit rule needed to actually trade the signal. It is a **momentum continuation** entry: price that explodes
away from the open in one direction tends to keep going until an equal-or-greater explosion happens in the
opposite direction ("freight-train logic"). It does not decide *whether* to trade today â€” that's TDW /
bond-filter gating, layered on as an optional step 5.

## When to use

- User wants a mechanical entry price for tomorrow/today based on "yesterday's range."
- User mentions "volatility breakout," "volatility expansion," "momentum breakout," or Larry Williams'
  open-plus-range technique by name.
- User is building/backtesting a short-term (1â€“5 day hold) futures or index system and needs an
  objective, repeatable trigger instead of a discretionary chart call.
- User asks to combine a range-breakout entry with a day-of-week filter or a bond-trend filter (link to
  `williams-tdw-tdm-seasonality` for the filter mechanics â€” this skill only says *where* it plugs in).

Do not use this for a reversal/fade system (see `williams-reversal-setups`), for sizing the trade once
triggered (see `williams-position-sizing`), or for a swing-based (non-range) volatility measure (see
`williams-greatest-swing-value`, the Chalek/"Talon" method).

## Method

1. **Compute yesterday's range.** `range = yesterday_high - yesterday_low`. This is the reference
   measure â€” not the average of several days, not a swing calculation. Williams tested averages and
   multi-day swings and yesterday's single-day range outperformed as the simplest, most robust base.

2. **Pick the reference point: today's OPEN â€” not the close, high, or low.** This is the load-bearing
   sub-rule. Williams back-tested adding/subtracting the range percentage to (a) yesterday's close, (b)
   yesterday's high/low, and (c) today's open. The open won on every axis: highest average profit per
   trade ($389 vs. $327 close-based vs. $313 high/low-based) and higher accuracy. If a request says
   "breakout off the close" or "off yesterday's high," flag that this deviates from the validated method
   before coding it.

3. **Set the range multiplier per market â€” do not use one universal percentage.** Book examples, all
   tested against different markets:
   - Bonds: buy at open + 100% of yesterday's range, sell at open âˆ’ 100% of yesterday's range.
   - S&P 500 (base case): 50% of range each side.
   - S&P 500 (tuned by day, no TDW filter): buy at open + 40% of range, sell at open âˆ’ 200% of range
     (asymmetric â€” the buy and sell multipliers do not have to match).
   - Cattle (close-based variant, historical reference only): 70% add for buys, 50% subtract for sells.
   Treat 40â€“200% of yesterday's range as the plausible calibration band (Williams' "Table 4.1"), and
   re-optimize per instrument rather than reusing another market's number. Compute both:
   ```
   buy_stop  = today_open + (buy_pct  * yesterday_range)
   sell_stop = today_open - (sell_pct * yesterday_range)
   ```
   Enter long on a stop at `buy_stop`, short on a stop at `sell_stop` â€” whichever triggers first.

4. **Attach a protective dollar stop, not a percentage stop.** Book examples: $1,500 (bonds, ~50% of
   yesterday's range in dollar terms), $1,750 (S&P swing-value variant). Size it to the instrument's
   dollar-per-point value and cap it near half of yesterday's dollar range as a starting point, then treat
   it as tunable. Pair with the **bailout exit**: close the trade at the first profitable opening after entry
   if neither the stop nor an opposite signal has fired first (full mechanics in
   `williams-bailout-exit` â€” this skill only names it as the required exit partner).

5. **Direction persists until an equal-or-greater OPPOSITE explosion â€” this is what makes it a
   continuation system, not a single-shot trade.** Do not close a winning position just because price
   pulled back; the freight-train logic says the trend holds until a new explosive move (of the same or
   greater magnitude, measured the same way) fires in the other direction. Practically, this means once
   filled, the position rides the bailout/stop rules from step 4 rather than being time-exited on a fixed
   day count.

6. **Optional gating layer â€” apply BEFORE sizing, not after.** Two independently validated filters, each
   stacked on top of the raw signal:
   - **TDW (Trade Day of Week):** restrict entries to the historically strongest buy/sell weekdays for
     that instrument (e.g., bonds: buy Tue/Thu, sell Wed/Thu in the book's dataset). Effect shown:
     fewer trades, average profit per trade $113 â†’ $173, drawdown $10,031 â†’ $3,500, accuracy 70% â†’
     84%. Full weekday-by-weekday method: `williams-tdw-tdm-seasonality`.
   - **Bond-trend filter (for stock-index systems only):** take S&P buy signals only if bond closes are
     higher than 5 days ago; take sells only if bonds are lower than 5 days ago (rationale: rising bonds
     are bullish for stocks). Effect shown: average profit per trade $228 â†’ $281, drawdown $13,025 â†’
     $5,250, largest loss $8,150 â†’ $2,075.
   - Combined (TDW + bond filter together): fewer trades, average profit per trade jumps to $444,
     accuracy to 90%, drawdown roughly unchanged. State this trade-off explicitly when a user stacks
     filters: total dollar profit typically *drops* (fewer trades) while quality per trade rises â€” confirm
     which objective (total P&L vs. edge-per-trade vs. drawdown) the user is optimizing before
     recommending how many filters to stack.

7. **Small-range/large-range cycle is context, not a separate signal.** Chapter 2's cycle â€” ranges
   alternate between clusters of small days and clusters of large days, never staying static â€” is *why*
   the range-expansion measure works: a volatility breakout firing after a run of small-range days (a
   "coiled" market) is the setup this whole technique is designed to catch. When a user asks "is now a
   good time to be watching for a breakout," check whether recent ranges have been contracting
   (small-range cluster) rather than already large â€” that's the pre-condition, not the trigger itself. Do
   not build a separate signal for it; it's read qualitatively off recent range history.

## Sub-rules / failure modes

- **Reference-point drift.** If any spec, chart tool, or prior code measures the expansion off the close
  or off yesterday's high/low instead of today's open, it is reproducing an inferior variant Williams
  explicitly tested and rejected. Correct it to the open before treating results as representative.
- **One multiplier for all markets.** Copying "50%" or "100%" across instruments without
  re-checking against that market's own range/volatility profile silently degrades edge â€” the book's own
  numbers range from 40% to 200% and are asymmetric (buy % â‰  sell % in the tuned S&P case).
- **No protective stop / no bailout.** The raw open+range formula alone is an entry price, not a system.
  Every worked example in the book pairs it with both a fixed-dollar stop and the bailout exit; presenting
  just the entry price as "the system" understates the drawdown risk.
- **Treating filters as free money.** Stacking TDW and bond-trend filters improves accuracy and average
  profit per trade but reduces total trade count and total dollar P&L â€” a system optimized purely for
  "most total profit" should NOT default to the fully-filtered version without the user confirming that
  trade-off.
- **Confusing this with the swing-based volatility measure.** "Talon"-style swing volatility (high 3 days
  ago vs. today's low, etc.) is a *different* measurement method for the same open-based entry
  structure â€” same steps 3â€“4 mechanics, different step-1 range calculation. Route swing-based requests
  to `williams-greatest-swing-value`.

## Worked mini-example

Request: "Set a Larry Williams volatility breakout entry for T-Bonds off today's open, book-default
settings."

1. Yesterday's bond range = 1'18 (1.5625 points), say $1,562.50 in dollar terms for a $1,000/point
   contract convention (example only â€” use the instrument's real point value).
2. Reference point: today's open, e.g., 118'00.
3. Bonds multiplier from the book: 100% each side.
   - `buy_stop = 118'00 + 1'18 = 119'18`
   - `sell_stop = 118'00 - 1'18 = 116'14`
4. Protective stop: $1,500 fixed (book example), i.e., roughly 1'00 from entry on a bond contract.
   Exit: bailout at first profitable opening if not stopped out first.
5. Direction rule: once filled (long or short), hold until stopped, bailed out, or an equal/greater opposite
   explosion signal fires â€” not on a fixed day count.
6. Optional: gate with TDW (book found Tue/Thu best buy days, Wed/Thu best sell days for bonds) before
   placing the order, if the user wants the higher-accuracy/lower-drawdown variant instead of the raw
   signal.

Output to hand the user: the two stop prices, the dollar stop, the exit rule, and â€” if filters weren't
requested â€” a one-line note that TDW/bond filters exist and change the profit/accuracy/drawdown
trade-off, per `williams-tdw-tdm-seasonality`.

## References

- Larry Williams, *Long-Term Secrets to Short-Term Trading* (Wiley, 1999), Ch. 4 "Volatility Breakouts â€”
  The Momentum Breakthrough" (open-vs-close/high/low test, Tables 4.1â€“4.3, bond/S&P worked models,
  TDW and bond-trend filter results); Ch. 2 "It's a Question of Price and Time" (small-range/large-range
  cycle as setup context).
- Sibling skills: `williams-tdw-tdm-seasonality` (day-of-week/month filter mechanics that shape step 6
  here); `williams-greatest-swing-value` (Chalek/"Talon" swing-based alternative to step 1);
  `williams-position-sizing` (how much to trade once the entry triggers); `williams-reversal-setups`
  (fade-based entries, contrast case to this continuation system); `williams-bailout-exit` (full mechanics
  of the "first profitable opening" exit named in step 4).
