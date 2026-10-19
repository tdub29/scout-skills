---
name: saliba-ratio-and-backspreads
description: Trade complex views combining direction, implied volatility and timing with ratio spreads (sell more than you buy â€” net short options, short vega, positive theta, for low-magnitude contratrend moves with falling IV or the passage of time) and backspreads (buy more than you sell â€” net long options, long gamma, long vega, negative theta, for high-velocity high-magnitude moves in a short window, ideal for breakouts from low-volatility ranges). Use when asked "how do I trade a bounce that will take time," "how do I position for a breakout from this coiled range," "what's a 1x2 spread," "backspread vs ratio spread," "how do I get long gamma cheaply," or "I'm bullish but only mildly and vol is high." From Anthony J. Saliba, Option Spread Strategies, Chapters 7 and 8.
---

# Saliba Ratio Spreads and Backspreads

## The pair

These are **exact opposites**, which is why they belong in one skill. Both
combine a directional view with a volatility view and a timing view, which is
what makes them the right tools for complex scenarios that a vertical cannot
express.

| | Ratio spread | Backspread |
|---|---|---|
| Construction | Buy 1 nearer-the-money, sell **more** further OTM (same class, same expiration) | Buy **more** OTM, sell 1 at- or nearer-the-money (same class, same expiration) |
| Net options | Short | Long |
| Vega | Short (wants falling IV) | Long (wants rising IV) |
| Theta | Positive (time helps) | Negative (time hurts) |
| Gamma | Short | Long |
| Wants | **Low**-magnitude directional move | **High**-magnitude, high-velocity move |
| Timeframe | Slow; time is an ally | Fast; a short window |
| Classic setting | Contratrend bounce or mild correction | Breakout from a low-volatility range |

Common ratios are 1-to-2, 2-to-3, and 1-to-4; any ratio works as long as the
direction of the imbalance is right. Depending on ratio, strikes, time to
expiration, and IV levels, either structure can be executed for a **debit, even
money, or a credit**.

## Ratio spreads: the contratrend tool

> Buy one March 100 call, sell two March 110 calls. That is a call ratio spread.
> Buy one June 90 put, sell three June 75 puts. That is a put ratio spread.

Because the position is always net short options, it carries a **short volatility
bias (short vega)** and **positive theta**. It is therefore most effective when
expecting a **low-magnitude directional move coupled with either declining
implied volatility or simply the passage of time.**

The canonical scenario is a contratrend recovery:

- **Call ratio spread** â€” the market has been declining with **rising** implied
  volatility, and you forecast a bounce or mild correction during which the
  underlying trades higher for a time **while implied volatility declines**. Both
  legs of that forecast pay you.
- **Put ratio spread** â€” the mirror image: a low-magnitude downward move, usually
  a pullback in a rising market, with IV behaving accordingly.

The reason this is the right structure rather than a long call: a long call
needs the move to be big and fast. A bounce that is real but modest, arriving
while IV deflates, loses money on a long call and makes money on a ratio spread.

**The risk that defines it:** because more options are sold than bought, a move
that goes *too far* in the forecast direction turns the extra short options into
an unbounded liability. The structure is right only when "mild" is a genuine
forecast rather than a hope. Position sizing and an exit plan for the
move-goes-too-far case belong in the trade at inception.

## Backspreads: the breakout tool

Also called **volatility spreads**. Built to capture **high-magnitude,
high-velocity directional moves occurring in a short time frame.**

> Buy two June 150 calls, sell one June 140 call. That is a call backspread.
> Buy four July 90 puts, sell one July 100 put. That is a put backspread.

Net long options, so **long gamma and long vega**, benefiting from rising
volatility and strong movement, with **negative theta** â€” the position bleeds if
nothing happens.

Where they are especially effective:

- **breakouts from low-volatility trading ranges**,
- **continuation patterns**,
- any high-velocity directional move.

That list is not incidental: a low-volatility range means cheap options (low IV)
and a coiled market, which is precisely the setup where long vega and long gamma
are cheapest and most likely to pay.

**Gearing.** The ratio is the trader's choice and depends on pricing and how much
gearing is wanted. **The greater the ratio, the greater the gearing â€” and the
more profit potential *and* loss the position carries.** Common ratios are 1-to-2,
1-to-3, and 1-to-4.

## Choosing between them

Ask one question: **do I expect the move to be small or large?**

- Small and slow, with IV falling -> ratio spread.
- Large and fast, with IV rising -> backspread.

Then ask the honesty question: **what happens if I am right about direction but
wrong about magnitude?** A ratio spread punished by a runaway move and a
backspread bled dry by a slow grind are the same error, mirrored. Both structures
demand a magnitude forecast, not just a directional one.

## Checklist

```
[ ] Direction, magnitude, IV direction, and velocity all stated separately
[ ] Structure matches magnitude: small -> ratio, large -> backspread
[ ] Ratio chosen deliberately (gearing = ratio; it scales BOTH profit and loss)
[ ] Debit / even / credit at entry known and acceptable
[ ] Ratio spread: exit plan for the move-goes-too-far tail; sized for it
[ ] Backspread: how long can this bleed before the thesis is void? (negative theta)
[ ] Account approved for the level; margin understood for the net-short legs
```

## Related

- [[saliba-spread-selection]] for routing here from a raw market view.
- [[saliba-straddles-strangles]] when there is no directional component at all.
- [[kezeli-balance-imbalance]] for identifying the low-volatility balance phase
  that precedes the breakout a backspread is built for.
