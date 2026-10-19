---
name: saliba-straddles-strangles
description: Trade magnitude rather than direction with straddles and strangles â€” long when forecasting a large move either way or rising implied volatility, short when forecasting little movement and seeking time decay and falling IV â€” including why the long straddle starts at-the-money and delta neutral, and the intrinsic-versus-extrinsic paths to profit. Use when asked "how do I trade an earnings move without picking a side," "straddle or strangle," "I think it moves big but don't know which way," "how do I sell volatility," "what's a delta-neutral options trade," or "IV is crushed/elevated, what do I do." From Anthony J. Saliba, Option Spread Strategies, Chapter 4.
---

# Saliba Straddles and Strangles

## What they are

Buy or sell **both a call and a put simultaneously**. Both are nondirectional:
the forecast is **magnitude**, not direction.

- **Straddle** â€” call and put at the **same strike**, same expiration.
- **Strangle** â€” call and put at **different strikes** (typically both
  out-of-the-money), same expiration.

## Long: forecasting movement or rising IV

Use a long straddle or strangle when forecasting **a large-magnitude move in
either direction, or an overall increase in implied volatility.**

There are two distinct profit paths, and they are worth separating because they
have different timelines:

1. **Intrinsic value** rises as either the call or the put goes in-the-money. This
   requires an actual move.
2. **Extrinsic value** rises on *both* legs as implied volatility rises. This
   requires no move at all.

A long straddle can therefore profit from an IV expansion before anything
happens, which is why entering ahead of a known volatility event and exiting into
it can work even when the eventual move disappoints.

**Strike choice:** usually at-the-money for a long straddle, because the trader
wants to start close to **delta neutral** â€” they do not know which way it goes,
so they do not want a directional tilt at inception.

## Short: forecasting stillness or falling IV

Use a short straddle or strangle when forecasting **little or no directional
movement**, aiming to profit from the decline in the position's overall value via
**time decay or falling implied volatility**, both of which shrink the extrinsic
value of the call and the put together.

Short straddles and strangles carry the risk profile that follows from being net
short options: losses grow with movement in either direction. Uncovered writing
carries margin requirements and requires the appropriate account approval level.

## Straddle or strangle: the tradeoff

| | Straddle | Strangle |
|---|---|---|
| Strikes | Same | Different (usually OTM) |
| Cost (long) | Higher | Lower |
| Move needed to profit (long) | Smaller | Larger |
| Premium collected (short) | Higher | Lower |
| Range of stillness tolerated (short) | Narrower | Wider |

A strangle is a straddle with the breakevens pushed apart: cheaper, but it needs
a bigger move to pay.

## The two-question test before entering

1. **Is the expected move larger than what the position already costs?** A long
   straddle bought into an elevated IV regime already prices in a large move; the
   realized move must exceed the implied one, not merely be large.
2. **Which side of the volatility trade am I actually on?** Long straddle is long
   vega and long gamma with negative theta. Short straddle is the reverse. State
   the Greeks and confirm they match the forecast.

## Related

- [[saliba-spread-selection]] for choosing between this family and
  butterflies/condors, which forecast magnitude in the opposite direction.
- [[saliba-butterflies-condors]] as the defined-risk expression of the same
  stillness view.
- [[saliba-ratio-and-backspreads]] when a directional tilt should be added to a
  magnitude view.
