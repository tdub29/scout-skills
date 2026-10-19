---
name: saliba-verticals
description: Construct and manage vertical spreads â€” same class, same expiration, different strikes â€” including the four variants (bull call, bull put, bear call, bear put), the debit-versus-credit choice driven by an implied-volatility view, and the max-profit / max-loss / breakeven arithmetic. Use when asked "bull call spread or bull put spread," "how do I get bullish exposure when options are expensive," "what's my breakeven on this spread," "debit spread or credit spread," "how do I cap the risk on a directional options trade," or "how do I sell premium without unlimited risk." From Anthony J. Saliba, Option Spread Strategies, Chapter 2.
---

# Saliba Verticals

## What it is

The simultaneous purchase and sale of options of the **same class** (all calls or
all puts) and the **same expiration**, at **different strikes**. Direction comes
from which strike is bought and which is sold.

Four variants, two per direction:

- Bullish: **bull call spread** (debit), **bull put spread** (credit)
- Bearish: **bear put spread** (debit), **bear call spread** (credit)

## When a vertical is the right answer

Five situations, each worth checking explicitly:

1. **Capturing a moderate move** up or down. Not a large one; the short strike
   caps the upside, so a vertical is the wrong vehicle for a move you expect to
   run far past it.
2. **Implied volatility is high** and an outright call or put is too expensive.
   The short leg funds part of the long leg.
3. **Lowering the overall risk** of an existing bullish or bearish position.
4. **Combining a directional view with an IV view** in one structure.
5. **Generating short-premium income in a limited-risk fashion.** This is the
   disciplined alternative to naked writing.

## Debit or credit: let IV decide

Both a bull call (debit) and a bull put (credit) express the same direction. The
tiebreaker is the volatility view.

- **IV high and expected to fall** -> prefer the **credit** structure (bull put
  for bullish, bear call for bearish). You are net selling expensive premium.
- **IV low and expected to rise, or you simply need long optionality** -> prefer
  the **debit** structure.
- **IV high but you want the directional exposure anyway** -> the debit vertical
  is still cheaper than the outright, which is the classic use.

## The arithmetic (write it before entering)

For a debit vertical (long the nearer strike K1, short the farther strike K2):

- **Max profit** = (K2 - K1) - debit
- **Max loss** = debit paid
- **Breakeven** = K1 + debit (calls) or K1 - debit (puts)

For a credit vertical (short the nearer strike, long the farther strike):

- **Max profit** = credit received
- **Max loss** = (strike width) - credit
- **Breakeven** = short strike +/- credit

Two invariants worth internalizing: **strike width is the total capital at risk
across both sides**, and **max profit plus max loss always equals the strike
width**. If a quoted spread violates that, one of the numbers is wrong.

## Choosing strikes

- **Width** sets both the cost and the ceiling. Wider costs more and pays more;
  narrower is cheaper and caps sooner.
- **Short strike placement is the real directional forecast.** Placing it at
  a level you genuinely do not expect to be exceeded is what makes the capped
  payoff acceptable. If you would be upset to be capped there, the strike is
  wrong or the structure is wrong.
- The relationship between the strikes and current price sets the delta of the
  package, which is the directional exposure you are actually buying.

## Management

- Because both legs share an expiration, **time decay works on the package**, not
  on one leg; a credit vertical's positive theta is the reason to hold it, and a
  debit vertical's negative theta is the reason not to hold one indefinitely.
- Closing one leg while the other stays open converts a defined-risk position
  into an undefined one. That is an explicit risk-increasing decision, not a
  partial exit.
- Multi-leg commissions matter proportionally more on narrow spreads; a $0.25
  credit on a $1 wide spread does not survive heavy costs.

## Related

- [[saliba-spread-selection]] to confirm a vertical is the right family at all.
- [[saliba-ratio-and-backspreads]] when the move is expected to be much larger
  or much smaller than a vertical assumes.
