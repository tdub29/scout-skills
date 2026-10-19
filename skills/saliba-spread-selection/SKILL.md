---
name: saliba-spread-selection
description: Pick the right option spread structure from a market view by decomposing the view into four inputs â€” direction, magnitude, implied-volatility direction, and time/velocity â€” then routing to verticals, collars, straddles/strangles, butterflies/condors, calendars, ratio spreads, or backspreads. Use when asked "what options strategy fits this view," "I think it goes up but slowly, what do I trade," "IV is high, what should I sell," "I expect a big move but don't know direction," "what's the opposite of a ratio spread," "which spread for a breakout," or whenever someone names a market opinion and needs a structure. From Anthony J. Saliba with Joseph C. Corona and Karen E. Johnson, Option Spread Strategies (2009, Bloomberg Press).
---

# Saliba Spread Selection

## What this decides

Which spread structure expresses a given view. The mistake this prevents is
picking a familiar structure and then rationalizing the view to fit it.

## Decompose the view into four inputs

Never start from a structure. Start from these:

1. **Direction** â€” up, down, or none.
2. **Magnitude** â€” large move, moderate move, small move, or no move.
3. **Implied volatility** â€” rising, falling, or flat. Separately: is IV *currently*
   high or low relative to its own history?
4. **Time / velocity** â€” does the move need to happen fast, or is there time?

Direction and magnitude are **different questions**. Nondirectional strategies
forecast magnitude without direction; that is their entire purpose.

## The routing table

| Direction | Magnitude | IV view | Timing | Structure |
|---|---|---|---|---|
| Up or down | Moderate | IV high now, or falling | Some time available | **Vertical** (bull call / bull put / bear call / bear put) |
| Up or down | Strong | either | Breakout / if-then trigger | **Collar (bearish) / reverse-collar (bullish)** |
| None | Large, either way | Rising | Soon | **Long straddle / strangle** |
| None | Small or none | Falling | Time to decay | **Short straddle / strangle** |
| None | Range-bound | Falling | Time to decay | **Long butterfly / condor** |
| None | Large, either way | Rising | Soon | **Short butterfly / condor** |
| Mild bias | Low magnitude | Falling | Slow, contratrend | **Ratio spread** |
| Directional | High magnitude | Rising | Fast, short window | **Backspread** |
| Bullish/bearish/sideways/movement | varies | varies | Two expirations in play | **Calendar (time) spread** |

## The polarity pairs (memorize these)

- **Ratio spread and backspread are exact opposites.** Ratio spreads sell more
  options than they buy: net short options, short vega, positive theta, and they
  want a *low*-magnitude move plus falling IV or the passage of time. Backspreads
  buy more than they sell: net long options, long gamma, long vega, negative
  theta, and they want a *high*-magnitude, high-velocity move with steady to
  rising IV.
- **Long butterfly/condor and long straddle/strangle are opposites** in magnitude
  even though both are nondirectional. Long butterflies want no movement; long
  straddles want a lot of it.
- **Long and short versions of every nondirectional structure** flip the magnitude
  forecast, not the direction forecast.

## The Greek shortcut

If the view can be stated in Greeks, the structure follows almost mechanically:

- Want **long gamma / long vega, accept negative theta** -> long straddle,
  long strangle, backspread, short butterfly/condor.
- Want **positive theta / short vega, accept short gamma** -> short straddle,
  short strangle, ratio spread, long butterfly/condor.
- Want **defined risk with a directional tilt** -> vertical.
- Want **exposure to the difference between two expiration cycles** -> calendar.

## When to use a vertical rather than an outright

Verticals are the workhorse. Reach for one when any of these hold:

- capturing a **moderate** move up or down (not a large one),
- **implied volatility is high** and buying an outright call or put is too
  expensive,
- lowering the overall risk of an existing bullish or bearish position,
- combining a **directional view with an IV view** in one structure,
- generating short-premium income **in a limited-risk fashion**.

That last one is the important discipline: sell premium inside a defined-risk
spread rather than naked.

## Constraints that change the answer

These are execution realities, not footnotes:

- **Legging risk.** For combinations, it can be impossible to execute all legs
  simultaneously. Exposure increases when you exercise or close one side while
  the other remains open.
- **Transaction costs bite hardest here.** Multi-leg spreads and straddles
  multiply commissions and slippage; textbook payoff diagrams exclude them.
- **Margin and approval level.** Most spreads require a margin account, and the
  account must be approved for that specific trading level. Uncovered writers
  face margin requirements.
- **Taxes** differ by structure; they belong in the selection, not after it.

## Selection checklist

```
[ ] State the view as four separate answers: direction / magnitude / IV / time
[ ] Is IV high or low RIGHT NOW versus its own history? (sets buy vs sell premium)
[ ] Does the view need direction at all? If not, use a nondirectional structure
[ ] Pick the structure from the table; then state its Greeks and confirm they
    match the view rather than merely being acceptable
[ ] Write max profit, max loss, and both breakevens BEFORE entering
[ ] Check: can all legs realistically be filled together?
[ ] Check: does the expected edge survive commissions on this many legs?
[ ] Define the adjustment in advance for the case where the view half-works
```

## Related

- [[saliba-verticals]]
- [[saliba-straddles-strangles]]
- [[saliba-butterflies-condors]]
- [[saliba-calendar-spreads]]
- [[saliba-ratio-and-backspreads]]
