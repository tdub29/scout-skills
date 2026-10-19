---
name: williams-reversal-setups
description: Spot and trigger Larry Williams' four failed-breakout reversal patterns â€” "Oops!", smash day, hidden smash day, and the specialists' trap â€” and produce an exact next-bar entry price. Use when asked "is today an Oops! setup", "check for a smash day reversal", "did this breakout fail into a trap", "spot a hidden smash day", or any request to find a short-term reversal entry after price rejects an extreme and snaps back through a prior level, on daily or intraday bars (S&P, bonds, commodities, stocks).
---

# Williams Reversal Setups

## What this decides

Given a price series (OHLC bars, any timeframe), whether TODAY's bar (or the
most recently closed bar) qualifies as one of four Larry Williams
failed-breakout patterns, and if so, the exact trigger price and direction for
the NEXT bar's entry. Output is a decision, not commentary: **no setup** or
**setup found: [pattern], [buy/sell], trigger = [price], stop-reference =
[level]**.

All four patterns share one engine: an extreme move draws in the public
(the "twitching worm"), the move fails to follow through, and price snaps
back through a specific prior level. The snap-back through that level IS the
entry signal â€” never enter on the extreme bar itself, only on the reversal
through it.

## When to use

- Reviewing today's (or the last closed) bar on any market for a reversal entry.
- Checking whether a multi-day breakout from a trading range was a trap.
- Building/backtesting a short-term reversal system and need the exact rule set.
- Screening a watchlist for which symbols printed a qualifying setup bar.

Not for: trend-following breakout entries (the opposite bet â€” see
`williams-volatility-breakout`), position sizing, or exit/stop management
(see `williams-bailout-exit`).

## Method

1. **Identify candidate pattern by bar shape.** Check in this order â€” Oops!
   first (rarest, highest edge), then smash day, then hidden smash day, then
   specialists' trap (needs a prior range, checked last):

   | Pattern | Setup bar condition | Trigger bar / level |
   |---|---|---|
   | **Oops! buy** | Today's OPEN < yesterday's LOW (gap below the entire prior range) | Enter when price rallies back UP through yesterday's LOW |
   | **Oops! sell** | Today's OPEN > yesterday's HIGH (gap above the entire prior range) | Enter when price falls back DOWN through yesterday's HIGH |
   | **Smash day buy** | Today closes below yesterday's LOW ("naked close" down; may also take out the prior 3â€“8 days' lows) | Enter next day when price trades ABOVE today's HIGH |
   | **Smash day sell** | Today closes above yesterday's HIGH (naked close up) | Enter next day when price trades BELOW today's LOW |
   | **Hidden smash day buy** | Today has an UP close, but close is in the LOWER 25% of the day's range and below today's open | Enter next day when price trades ABOVE today's HIGH |
   | **Hidden smash day sell** | Today has a DOWN close, but close is in the UPPER 25% of the day's range and above today's open | Enter next day when price trades BELOW today's LOW |
   | **Specialists' sell trap** | Market chopped sideways in a 5â€“10 day box, then broke out UP with a naked close above the entire box | If price breaks back BELOW the breakout day's true low within 1â€“3 days, go SHORT |
   | **Specialists' buy trap** | Market chopped sideways in a 5â€“10 day box (downtrend context), then broke out DOWN with a naked close below the entire box | If price breaks back ABOVE the breakout day's true high within 1â€“3 days, go LONG |

2. **Confirm the setup bar, then wait one bar for the trigger.** Every
   pattern here is two bars: bar 1 sets the trap (extreme close or gap), bar
   2 (or bar 2â€“4 for the trap) confirms the failure by trading back through
   bar 1's key level. Never trade the setup bar itself â€” that's the public's
   entry, not yours.

3. **Apply the Oops!-specific filters before sizing conviction** (these do
   not apply to smash day / trap patterns):
   - **Day-of-week exclusion, S&P**: skip Wednesday and Thursday buys â€” those
     days statistically lead to declines. Best S&P buy days: Tuesday,
     Wednesday, Friday *when combined with the 9-day MA oversold filter*
     (rule 3b) â€” the day filter changes meaning once the MA filter is
     layered on, so use the paired combination, not the bare exclusion, when
     both are available.
   - **9-day MA overbought/oversold filter**: for buys, only take the Oops!
     if the 9-day moving average is falling into the setup day (comparing
     the prior day's average to the day before, e.g. "Friday's 9-day MA less
     than Thursday's" for bond buys) â€” confirms oversold. For sells, only
     take the Oops! if the 9-day MA is rising into the setup day â€” confirms
     overbought.
   - **Month-of-month bias**: Oops! buys taken after the 17th trading day of
     the month (S&P) or in the first 5 trading days of a new month (bonds)
     stack with the known end-of-month/turn-of-month rally bias â€” a real
     edge-on-edge, not curve-fitting, per Williams, because the bias predates
     his discovery of the pattern.
   - Exit is short-hold by design (Williams' own S&P Oops! trades average
     ~1.5 days: enter today, out on tomorrow's open, or use the bailout
     technique â€” see `williams-bailout-exit`).

4. **State the result as a trigger, not a forecast.** Format:
   `[PATTERN] [BUY|SELL] setup confirmed on [date]. Entry trigger: price
   [above|below] [level] on the next bar. Invalidation: no trigger by close
   of bar N+2 (traps: N+3) â€” setup expires, do not chase.`

## Sub-rules and failure modes

- **Don't confuse a real breakout with a smash day / trap.** Sometimes the
  extreme close or box breakout IS valid and price keeps going. The pattern
  only fires â€” and only then is it tradeable â€” if the very NEXT bar (traps:
  within 1â€“3 bars) trades back through the setup bar's opposite extreme. No
  reversal trigger = no trade, full stop; do not anticipate it.
- **"Naked close" is the load-bearing term** â€” it means the close itself is
  beyond the reference level (prior day's high/low, or the whole prior
  range), not just an intraday poke. A bar that pokes through intraday and
  closes back inside does not qualify as a smash day or Oops! setup bar.
- **Hidden smash day is easy to miss because the close direction is
  opposite the trap.** A hidden smash day BUY setup has an UP close (looks
  bullish) â€” the tell is the close sitting in the bottom 25% of that up bar's
  range, below the open. Screeners that only look for down closes will never
  find this pattern; check close-location-within-range, not close-vs-prior-close.
- **Specialists' trap requires the prior congestion, or it's just a smash
  day.** Confirm 5â€“10 sideways days exist before the breakout bar â€” without
  the box, this collapses into an ordinary smash day / naked-close pattern
  with a shorter reversal window (1 bar, not 1â€“3).
- **Timeframe-agnostic, but pair with a qualifier on intraday charts.**
  Williams confirms all four patterns work on 5-min/30-min/hourly bars, but
  warns against using price-predicts-price alone intraday â€” require a second
  independent condition (trend, TDW/TDM seasonality, overbought/oversold)
  before firing a live intraday trigger.

## Worked mini-example

Bond futures, five sessions:

| Day | Open | High | Low | Close |
|---|---|---|---|---|
| Mon | 100.00 | 100.20 | 99.80 | 100.10 |
| Tue | 100.15 | 100.30 | 99.60 | 99.65 |
| Wed | 99.30 | 99.75 | 99.20 | 99.70 |

- Tue closes at 99.65, below Mon's low (99.80) â†’ naked close down â†’
  **smash day buy setup** confirmed on Tue.
- Wed opens at 99.30 (below Tue's low too, but that's a separate Oops!
  check on Wed vs Mon â€” here we're tracking the Tue smash day trigger).
- Trigger level = Tue's HIGH = 100.30. Wed's high only reached 99.75 â†’ no
  trigger yet; setup remains live through the invalidation window (next 1
  bar for smash day) â€” since Wed didn't trigger, the smash day setup expires
  unfilled after Wed. Output: `SMASH DAY BUY setup confirmed Tue (naked
  close 99.65 < Mon low 99.80). Entry trigger: price above 100.30 next bar.
  No trigger by Wed close â€” setup expired.`

This demonstrates the discipline: a valid setup bar with no confirmed
trigger is a no-trade, not a "close enough."

## References

- Source: Larry Williams, *Long-Term Secrets to Short-Term Trading* (Wiley,
  1999), Chapter 7 â€” "My Smash Day Patterns," "Specialists' Trap," "Oops!
  This Is Not a Mistake."
- Siblings: `williams-volatility-breakout` (the trend-following counterpart â€”
  trade the breakout itself, not its failure), `williams-tdw-tdm-seasonality`
  (day-of-week/month filters referenced in rule 3), `williams-greatest-swing-value`
  (volatility-based stop placement for these entries), `williams-position-sizing`,
  `williams-bailout-exit` (time-based exit used after these triggers fire).
