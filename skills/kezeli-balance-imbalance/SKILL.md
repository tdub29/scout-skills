---
name: kezeli-balance-imbalance
description: Classify what a market is doing right now into one of two mutually exclusive phases â€” horizontal/balanced (moving through time, supply meeting everyone's needs) or vertical/imbalanced (moving through price, favoring buyers or sellers) â€” then into one of only three segments (nontrending, uptrending, downtrending) so the matching tactic can be applied, on the premise that balance leads to imbalance and back again. Use when asked "is this a trend or a range," "should I be fading or following here," "what regime is this market in," "why do my breakout rules lose money in this tape," "how do I make discretionary trading rules-based," or before choosing any strategy that assumes trend or mean reversion. From Andrew Kezeli in Paul Ciana (ed.), New Frontiers in Technical Analysis, Chapter 5.
---

# Kezeli Balance and Imbalance

## What this decides

Which of two phases and three segments the market is in, because the tactic
follows from the classification. Applying trend tactics inside balance, or
fade tactics inside imbalance, is the single most common way a good rule set
loses money.

## Why this framing exists

Automated systems beat discretionary traders for structural reasons, not because
the logic is smarter:

- driven by technicals, not fundamentals,
- entirely rules-based, and they do not break rules,
- risk managed with specific, objective entry, management, and exit criteria,
- and above all they **do not question their rules or develop biases**.

The goal of this framework is to give a discretionary trader a rules-based
backbone that mimics that. The stated payoff is modest and honest: if a trader
eliminates just **the obvious 10 to 20 percent of trades where they are clearly
on the wrong side of the market**, unprofitable traders reach breakeven,
breakeven traders become profitable, and profitable traders improve, all at lower
cost because of fewer but higher-quality executions.

Distill market data into three questions:

1. **The past** â€” how price, and therefore traders, responded to key areas on the
   chart.
2. **The present** â€” what price is trying to do (higher, lower, stall) and
   whether it is succeeding.
3. **The future** â€” what the crowd is likely to do if and when specific price
   levels or key reference areas are hit.

## The two phases

In any given timeframe a market has exactly two repeatable, mutually exclusive
movements: **horizontal** and **vertical**.

**Horizontal / balanced.** Supply is balanced; it is meeting the needs of both
buyers and sellers in this timeframe. Price moves slowly through a relatively
narrow range. This is an expression of the **time** dimension: the market is
moving through time.

**Vertical / imbalanced.** Supply is imbalanced and cannot meet everyone's needs.
Price moves rapidly, favoring buyers or sellers but not both. This is an
expression of the **price** dimension: the market is moving through price.

The vocabulary maps one-to-one, which is useful when translating between
frameworks:

| Horizontal | Vertical |
|---|---|
| Sideways | Sloping |
| Nontrending | Trending |
| Nondirectional | Directional |
| Balanced | Imbalanced |
| Rotational | Nonrotational |
| Consolidation | Nonconsolidation |
| Efficient | Inefficient |
| Range-bound / bracketing | Non-range-bound |
| Overlapping value | Nonoverlapping value |
| Price-controlled | Non-price-controlled |
| Constrained by liquidity | Unconstrained by liquidity |
| Moving through time | Moving through price |
| Slow, boring | Fast, exciting |

## The building-block property (this is the forecast)

Because the two phases are mutually exclusive, **being in one tells you what
comes next: the other.**

> Balance leads to imbalance, and back to balance again.

A slow, low-volatility horizontal stretch will be followed by a relatively fast,
higher-volatility vertical move. A fast vertical move will eventually resolve
back into a slower horizontal one.

That is the practical content of the model. It does not predict direction; it
predicts the **character** of what comes next, which is enough to choose between
a fade tactic and a follow tactic, and to know when to widen or tighten stops.

## The three segments

All markets decompose into exactly three technical segments, each with its own
definition and its own tactics:

1. **Nontrending (sideways).** Formally: two or more relatively equal price pivot
   highs and relatively equal price pivot lows. Tactics: work the edges, fade
   extremes back toward value, expect rotation, size for a range not a run.
2. **Uptrending.**
3. **Downtrending.**

Identifying the segment first, and only then applying the matching technique, is
what produces the highest-probability outcome. The classification is the trade
decision's parent, not a commentary added afterward.

## Working checklist

```
[ ] Name the TIMEFRAME first. Phase is timeframe-specific; a balanced daily can
    contain many imbalanced 5-minute segments
[ ] Phase: horizontal (through time) or vertical (through price)?
[ ] Segment: nontrending / uptrending / downtrending?
      nontrending requires 2+ roughly equal pivot highs AND lows
[ ] Because phases alternate, state what is expected NEXT (character, not direction)
[ ] Choose the tactic that matches the segment, not the one you prefer
[ ] Past / present / future: how did price react at key areas, what is it trying
    to do now, what will the crowd do at the next reference level
[ ] Write the rule down before entry so it cannot be renegotiated mid-trade
```

## The failure this prevents

Trend rules applied in balance produce a stream of small whipsaw losses; fade
rules applied in imbalance produce a small number of very large ones. Both feel
like the strategy is broken when in fact the classification step was skipped.
Nearly all of the "obvious 10 to 20 percent" of clearly-wrong-side trades are
phase misclassifications.

## Related

- [[katz-breakout-threshold-design]] on the same problem from the breakout side:
  thresholds too close to price get eaten by balance-phase noise.
- [[kase-devstops]] for sizing the stop to the volatility the current phase
  implies.
