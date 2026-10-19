---
name: katz-scientific-system-development
description: "Test a trading entry or exit in isolation, statistically."
---

# Katz Scientific System Development

## What this decides

How to set up a trading-system investigation so its results mean something.
Most system research fails not at the idea but at the design of the test: entries
and exits are varied together, "signals" are never turned into orders, and no
statistical claim is ever made. This gives the experimental frame.

## 1. A system is not complete until it exits

A partially mechanical model that produces only entries is not a trading system.
Without mechanical exits, every exit is a subjective judgment call, which is
exactly where discipline fails, and nothing can be measured: no net profit, no
maximum drawdown, no Sharpe ratio, no equity curve, no estimate of future
profitability.

The requirement is **complete round-turns**: every entry followed by a defined
exit. Enter and never exit and there are no completed trades to evaluate.

## 2. Orders, not signals

Never accept a "buy signal" as a testable object. It is ambiguous: buy at the
next open? on a stop? on a limit? at what price? Each choice produces different
results. An exit "signal" is worse: at the close, on a profit target, or on a
money-management stop?

**A method must eventually issue a fully specified entry or exit order.** Only
then can it be tested at all. If someone cannot state the order, they do not yet
have a system, they have an opinion with a timestamp. (See
`katz-entry-order-selection` for choosing among stop, limit, and market.)

## 3. What "good" means, precisely

**A good entry order** puts the trader in at a point of relatively low risk and
fairly high potential reward. The measurable proxy is **adverse excursion**, the
largest unrealized loss inside a trade. The theoretical ideal is a limit fill at
the exact extreme of every turning point, where adverse excursion is a tick or
two. Real entries only need to keep adverse excursion acceptable and the
risk-reward ratio satisfying.

**A good exit** does three things at once, and they conflict:

- gets out fast when a trade has gone wrong, preserving capital,
- without cutting so many would-be winners into small losses,
- while being able to ride a large move to its conclusion.

The third requirement relaxes if the entry model can re-enter sustained trends,
which is why exits cannot be judged in a vacuum.

## 4. The three core elements of the method

1. **Isolation of system elements.** Hold everything fixed and manipulate one or
   two critical elements at a time.
2. **Standardized tests that allow valid comparisons.** Same portfolio, same
   platform, same reporting, so numbers can be laid side by side.
3. **Statistical assessment of results.** Not just "it made money," but how
   likely that is to hold on other samples.

Formally, the object of study must be observable without subjective judgment
(mechanical systems plus simulation software give this), there must be an orderly
way to assess its behavior (back-testing over long history plus inferential
statistics), and the task must be made tractable by fixing most parameters.

## 5. The isolation trick, which is the useful part

Entries and exits cannot be discussed independently, yet both must be studied
independently. The resolution is a fixed standard counterpart:

- **To test entries:** hold one standardized exit strategy constant across every
  entry model tested. Differences in results are then attributable to the entry.
- **To test exits:** enter with a **random number generator**. Long and short
  entries taken on the fall of a die.

The random-entry model is the part people flinch at, and it is the most valuable
idea here. An exit strategy that extracts profit from randomly entered trades is
demonstrably doing real work rather than borrowing an edge from a good entry. It
is a harsh test, and it is passable.

## 6. The tooling the method presumes

- **Data** with known quality and an appropriate time frame; garbage history
  invalidates everything downstream.
- **A simulator** whose reliability, capacity, speed, and reporting you have
  actually checked, because the performance summary and trade-by-trade report are
  the measuring instrument.
- **An optimizer** used under discipline (see `katz-optimization-discipline`).
- **Inferential statistics** (see `katz-system-significance-test`).
- **Equalization of dollar volatility** across markets, and one basic test
  portfolio, so per-market results are comparable rather than dominated by
  whichever contract happens to be biggest.

## Design checklist for any test

```
[ ] Entry expressed as a specific ORDER (type + price rule)
[ ] Exit expressed as specific ORDERS (money-management stop at minimum)
[ ] Complete round-turns produced
[ ] Exactly one element varied; counterpart held to the standard
    - testing an entry?  -> fixed standardized exit
    - testing an exit?   -> random entries
[ ] Same portfolio, same period, same cost/slippage assumptions across arms
[ ] Dollar volatility equalized across markets
[ ] Adverse excursion recorded, not just net P/L
[ ] Out-of-sample arm reserved
[ ] Inferential statistics computed on both arms
```

If a comparison cannot state which single element differed between two arms, it
is not evidence, and the conclusion drawn from it should be discarded.

## Related

- [[katz-optimization-discipline]]
- [[katz-system-significance-test]]
- [[katz-entry-order-selection]]
- [[katz-exit-strategy-taxonomy]]
