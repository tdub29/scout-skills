---
name: saliba-calendar-spreads
description: Use calendar spreads â€” same option class, different expiration cycles â€” to express views a single-expiration structure cannot, covering horizontal (time) spreads at one strike versus diagonal spreads across strikes and expirations, and the fact that a horizontal calendar can be built with a bullish, bearish, sideways, or big-move bias depending on construction. Use when asked "what's a calendar spread," "time spread vs diagonal," "how do I trade the difference between front-month and back-month volatility," "how do I profit from front-month decay," "which expiration should I sell," or when a view involves two different time horizons. From Anthony J. Saliba, Option Spread Strategies, Chapter 6.
---

# Saliba Calendar Spreads

## What it is

Options of the **same class** but with **different expiration cycles**. This is
the only family in the toolkit that trades *time* as the primary axis rather than
price or magnitude.

Two categories:

- **Horizontal calendar spread (time spread)** â€” same class, **same strike**,
  different expirations.
- **Diagonal calendar spread** â€” same class, **different strikes AND different
  expirations**.

The source introduces horizontal calendars in detail; diagonals are the same idea
with a directional tilt added by the strike offset.

## The property that makes them worth learning

A horizontal calendar spread:

- can be composed of **calls or puts**,
- can be **long or short**,
- can carry a **bullish** bias,
- can carry a **bearish** bias,
- can carry a **sideways** bias,
- can carry a **movement** bias (a large move in either direction).

That is the whole point: **the same structural family can express any of the
directional views**, depending on which expiration is bought, which is sold, and
where the strike sits relative to the underlying. They are, in the source's
phrase, wonderfully complex, and the complexity is the feature.

## How to think about the two legs

The two expirations differ in how fast they decay and how sensitive they are to
a change in implied volatility. Time decay accelerates as expiration approaches,
so the **near-dated leg decays faster** than the far-dated one; the far-dated leg
carries **more vega**, so it responds more to a shift in implied volatility.

That gives the two standard motivations:

1. **Sell the fast decay, own the slow decay.** Short the near expiration, long
   the far one, at a strike where you expect the underlying to sit. The near leg
   melts faster than the leg you own.
2. **Own the vega where it lives.** Because the back month carries more vega, a
   long-back-month calendar is a way to be long volatility with the front month
   paying part of the bill.

The strike placement sets the directional bias; the choice of which expiration is
long sets the volatility and decay bias.

## What makes calendars different from every other spread here

Every other structure in this toolkit has one expiration, so all legs share an
expiration date and the payoff at expiration is a clean piecewise-linear diagram.
A calendar does not have that: **when the near leg expires, the far leg is still
alive.** Consequences:

- There is no single expiration payoff diagram; the outcome depends on the
  underlying price **and** the implied volatility of the surviving leg at the
  near expiration.
- The position converts into a different position at the near expiry. Know what
  it becomes, and decide in advance whether you want to hold that.
- **Assignment risk on the short near-dated leg is a live operational issue.**
  Exercising or closing one side while the other remains outstanding increases
  risk exposure, and legging out of a calendar is not a partial exit.

## Checklist

```
[ ] Horizontal (same strike) or diagonal (different strikes) â€” say which and why
[ ] Which expiration is LONG? That sets the vega and decay stance
[ ] Where is the strike relative to spot? That sets the directional bias
[ ] State the intended bias explicitly: bullish / bearish / sideways / movement
[ ] What does this position BECOME when the near leg expires? Do I want that?
[ ] Early-assignment plan for the short near-dated leg
[ ] Front-month vs back-month implied volatility compared, not assumed equal
[ ] Commissions across two cycles plus a likely roll accounted for
```

## Related

- [[saliba-spread-selection]] for when a two-expiration view is the right frame
  at all.
- [[saliba-verticals]] as the single-expiration alternative when the view has no
  time dimension.
