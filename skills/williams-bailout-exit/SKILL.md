---
name: williams-bailout-exit
description: Decide when to exit a Williams-system trade using the "bailout" / first-profitable-opening rule, paired with a fixed dollar stop and an exit-and-reverse override. Use when asking "when do I exit this trade," "should I take a one-tick profit," "exit on the first profitable opening," "should I wait for my stop or reverse now," or when pairing any Williams entry (volatility breakout, seasonality, reversal setup) with its exit. Triggers: set a bailout exit, first profitable opening, exit-and-reverse, slow-moving market exit delay, take a one-tick profit.
---

# Williams Bailout Exit

## What it decides

Given an open Williams-system position, produce one of three exit actions each session: **hold**, **bailout exit** (take the first profitable opening), or **exit-and-reverse** (opposite signal fired). This is the paired exit for every Williams entry system (volatility breakout, TDW/TDM seasonality, reversal setups) â€” none of those entries specify their own exit; they all hand off to this rule.

## When to use

- You have an open position from a Williams entry system and need to know whether today is an exit day.
- You're building or backtesting a Williams system and need an exit rule to pair with an entry.
- You're deciding whether to hold for more profit or take a small gain now.
- An opposite entry signal fires while you're still in a trade.

## The method

Run these three checks in order, every session, before the market opens:

1. **Protective stop check (always active).** Confirm a fixed-dollar stop is placed and live. Williams uses $1,500 or 50% of the previous day's range subtracted from entry, whichever the system specifies â€” but the stop is not negotiable and is not lifted on the entry day's placement logic; once in place it stays in place until the trade closes. If price already violated it, you're flat â€” skip to step 3 for the next entry, nothing to bail out of.

2. **Bailout check (first profitable opening).** At today's open, is the trade profitable by any amount â€” even one tick?
   - If **yes**: exit at the open. Take it. Do not hold out for more.
   - If **no**: hold, subject to the stop and step 3.
   - **Slow-market exception**: in slower-moving markets (not the S&P), you may delay the bailout by a day or two to let the trade develop and raise average profit per trade. This is the only sanctioned deviation from "take the first profitable opening" â€” it is a deliberate delay, not permission to wait for a bigger number once profitable.

3. **Exit-and-reverse check (overrides steps 1â€“2).** Did the paired entry system just generate a signal in the opposite direction (short and a buy signal fires, or long and a sell signal fires)?
   - If **yes**: exit and reverse immediately, at market, without waiting for the stop or for a profitable opening. The freshest signal always wins over the stop or the bailout.
   - If **no**: proceed with steps 1â€“2 as normal.

Output each day: **HOLD**, **BAILOUT EXIT**, or **EXIT-AND-REVERSE**, with the one line of reasoning ("profitable at open, took it" / "opposite signal fired, reversing" / "stop hit").

## Sub-rules and failure modes

- **Never remove the dollar stop to "let the bailout do the work."** The stop and the bailout are independent and both active at all times; the bailout doesn't replace stop protection, it's the profit-side complement to a loss-side stop.
- **A one-tick profit is a real exit, not a rounding error.** The common failure mode is holding past the first green open hoping for "a real profit" â€” that's greed overriding the system, the exact failure Williams calls out (it's not fear that wrecks traders, it's greed refusing to take the first win). If the open shows any profit, take it unless you're deliberately in the slow-market delay case.
- **Exit-and-reverse pulls rank on both other rules.** If an opposite signal fires while you're underwater and haven't hit your stop, or while you're flat waiting for a profitable open, reverse now â€” don't wait for the stop to trigger or for the bailout to clear first. Sequence collisions resolve to reverse-first.
- **The slow-market delay has a ceiling.** "A day or two," not indefinitely. If you're extending the delay past two sessions to avoid taking a small profit, that's greed again, not the sanctioned exception â€” revert to first-profitable-opening.
- **Don't confuse this with a stand-alone system.** The bailout is not a complete trading system by itself; it only fires once an entry system (williams-volatility-breakout, williams-tdw-tdm-seasonality, williams-reversal-setups) has put you in a position. Applied alone with no entry logic, it has nothing to exit.

## Worked mini-example

You're long the S&P from yesterday's volatility-breakout entry at 4500, protective stop live at entry âˆ’ $1,500-equivalent points. This morning's open is 4501 (one tick above entry).

- Step 1: stop hasn't been hit â€” still active.
- Step 2: open is profitable, even if only by one tick â†’ **BAILOUT EXIT** at the open. Reasoning: "profitable at open (+1 tick), took it per rule 2 â€” no holding out for more."

Contrast: same trade, but bond-market entry (a slower-moving market) opens flat. You may choose to delay the bailout check by a day or two to let the trade develop, rather than exiting flat or at breakeven â€” but only for up to two sessions.

Contrast: you're short the S&P, still below your stop and not yet profitable, when a fresh buy signal fires from the entry system. Ignore the stop and the bailout entirely â†’ **EXIT-AND-REVERSE** now, at market.

## References

- Source: Larry Williams, *Long-Term Secrets to Short-Term Trading* (1999, Wiley), Chapter 11, "When to Get Out of Your Trades" (the three-rule chapter this skill encodes verbatim), plus the applied example in Chapter 10 (S&P monthly-open system exiting on first profitable opening, $1,500 stop).
- Siblings: `williams-volatility-breakout`, `williams-tdw-tdm-seasonality`, `williams-greatest-swing-value`, `williams-position-sizing`, `williams-reversal-setups` â€” this skill is the exit half of every one of those entry systems.
