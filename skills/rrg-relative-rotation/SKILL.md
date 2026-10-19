---
name: rrg-relative-rotation
description: Read and build a Relative Rotation Graph â€” plot a universe's members on JdK RS-Ratio (x) versus JdK RS-Momentum (y) around a benchmark anchored at 100,100, identify which of the four quadrants each name sits in, and use the clockwise Leading to Weakening to Lagging to Improving rotation plus tail length and direction to decide overweight, underweight, and (most importantly) what to avoid. Use when asked "which sectors should I overweight," "read this RRG," "is this sector rotation real," "what does the bottom-right quadrant mean," "how do I compare relative strength across a whole universe," "what should I sell/avoid," or when someone asks for "your top five picks" in a universe. From Julius de Kempenaer in Paul Ciana (ed.), New Frontiers in Technical Analysis, Chapter 2.
---

# Relative Rotation Graphs

## What this decides

Which members of a universe (sectors, stocks, countries, factors) to overweight,
underweight, or leave alone, relative to a benchmark, and how urgent the change
is based on where each one is heading rather than only where it is.

## The two measures

Raw relative strength (a price ratio) is not comparable across a universe: two
ratio lines drawn against the same benchmark are on different scales and cannot
be ranked. The fix is a pair of normalized measures.

**JdK RS-Ratio** â€” the security's relative strength against the benchmark,
normalized so every member of the universe is on one comparable scale. This is
what you can rank a universe on.

**JdK RS-Momentum** â€” the direction and rate of change of the RS-Ratio line. It
answers the question the ranking cannot: how did this name get to that ranking,
and where is it going next.

Both are anchored at 100. **Above 100 is good, below 100 is bad; further from
100 is more so.** Because everything is scaled against the benchmark, the
benchmark itself sits permanently at the 100,100 crossing.

## The graph

Abandon the price-chart habit of time on the x-axis. Plot a scatter:

- x-axis: JdK RS-Ratio
- y-axis: JdK RS-Momentum
- one point per universe member
- axes crossing at 100,100 (the benchmark)

Then add a **tail**: the last N observations for each member, so you see
direction and pace, not just position. Tail length is a readability tradeoff.
With many members, long tails turn the chart into spaghetti; shorten them.

## The four quadrants

| Quadrant | RS-Ratio | RS-Momentum | Name | Meaning | Action |
|---|---|---|---|---|---|
| Top right | >100 | >100 | Leading | Strong relative strength, still strengthening | Overweight / long |
| Bottom right | >100 | <100 | Weakening | Still outperforming, but momentum rolling over | Trim, prepare to exit |
| Bottom left | <100 | <100 | Lagging | Weak relative strength, still getting weaker | Underweight / short |
| Top left | <100 | >100 | Improving | Still underperforming, but momentum has turned up | Watch, start accumulating |

## The rotation is clockwise, and it has an order

The sequence is not arbitrary, and knowing it is the whole edge:

1. **Leading (top right).** Strong and getting stronger.
2. Before relative strength turns negative, **momentum levels off and weakens
   first**. That drops the name into **Weakening (bottom right)**. Relative
   strength is still positive here, which is exactly why it feels safe and is
   not.
3. If relative strength keeps eroding and negative momentum accelerates, it is
   pushed into **Lagging (bottom left)**.
4. Bad things end too: downward momentum levels off and turns up, pushing the
   name into **Improving (top left)** while RS-Ratio is still below 100.
5. Continued improvement carries it back into Leading, and the circle closes.

The practical consequence: **momentum leads the ratio**. A move from top right
into bottom right is the early warning, arriving before the ranking table shows
any deterioration at all. Rank-only workflows are structurally late.

This is also the answer to a long-standing claim: traders talk about sector
rotation, and the RRG is what shows that sectors really do rotate around the
benchmark, clockwise.

## The finding that changes the question you ask

Across roughly 3,456 recommendation-months (18 sectors, 1987 to 2003), measuring
excess return three months after each recommendation, both the outperform and
underperform calls generated excess return on average. But **the average excess
return of the underperform calls was significantly higher.**

So "what are your five best picks?" is the wrong question. The right one is
**"which five should I avoid?"** Avoid the bleeders and outperformance largely
follows on its own. Anyone can look back at a year and name the handful of
positions that, absent them, would have made the year.

Build reports accordingly: rank the whole universe on RS-Ratio and show the
weakest five as prominently as the strongest five, at both the sector and
individual-name level.

## Reading checklist

```
[ ] Benchmark chosen deliberately (it is the anchor; changing it changes everything)
[ ] Universe is genuinely comparable (one asset class, one classification level)
[ ] Tail length set so the chart is readable, not spaghetti
[ ] For each name: quadrant, heading, and pace of the tail
[ ] Flag every name that has crossed from Leading into Weakening (earliest signal)
[ ] Flag every name in Lagging with momentum turning up (earliest re-entry)
[ ] Name the five to AVOID before naming the five to buy
```

## Common misreadings

- **Treating bottom-right as still-good.** It is the exit warning. RS-Ratio being
  above 100 is a lagging comfort.
- **Treating top-left as still-bad.** It is the accumulation zone.
- **Ranking on RS-Ratio alone.** That is a snapshot with no direction, which the
  whole two-measure design exists to fix.
- **Mixing classification levels** (a sector next to a single stock) so distances
  from the benchmark are not comparable.
- **Reading a single snapshot with no tails.** Position without direction cannot
  distinguish a name entering a quadrant from one about to leave it.

## Related

- [[ciana-indicator-popularity]] for what the rest of the universe is actually
  watching.
- [[erlanger-seasonal-validation]] for a second, independent lens on which names
  to avoid in a given window.
