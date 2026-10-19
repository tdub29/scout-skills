---
name: turtle-trading-system
description: "The original Turtle rules. Donchian, N sizing, 2N stop"
---

# Turtle Trading System

The mechanical trend-following system Richard Dennis and William Eckhardt taught the
"Turtles" in 1983, documented by Curtis Faith (the most successful Turtle) in *Way of
the Turtle* (2007). Its thesis: a positive-expectancy edge, applied with total
consistency and volatility-normalized risk, beats discretion. The specific rules were
"a fairly unimportant component" of the edge. The discipline to follow them through
drawdowns was everything. Two or three big trends a year produce all the profit, so
you cannot miss one.

This is the canonical MECHANICAL BREAKOUT SYSTEM with volatility-unit sizing. For
generic indicator/chart reading see `technical-analysis`; for standalone volatility,
VaR, Sharpe, drawdown math see `risk-metrics-calculation`. This skill is the complete
end-to-end ruleset, not those primitives.

## N: the volatility unit (do this first, everything keys off it)

N is the market's own daily volatility, measured in the contract's price points. It is
the 20-day exponential moving average of True Range (what is now called ATR).

True Range = maximum( H - L, H - PDC, PDC - L )
  H = current high, L = current low, PDC = previous day's close (captures gaps).

N = ( 19 * PDN + TR ) / 20
  PDN = previous day's N, TR = current day's True Range.
  Seed the recursion with a 20-day simple average of True Range.

N is recomputed daily; the Turtles were handed a fresh N-and-unit sheet each Monday.

## Position sizing: 1 Unit = 1% of equity risked per N of move

The core insight is volatility normalization. Size every position so that a 1N price
move equals 1% of account equity. Then a trend in a quiet market and a trend in a wild
market carry the same dollar risk, which is what makes diversification across many
markets actually work.

Dollar volatility per contract = N * dollars-per-point (the contract's point value).

Unit size (contracts) = ( 1% of account equity ) / ( N * dollars-per-point )

Worked example from the book (heating oil, Dec 2002): N = 0.0141, account =
$1,000,000, dollars-per-point = 42,000 (a 42,000-gallon contract quoted in dollars).
Unit = (0.01 * 1,000,000) / (0.0141 * 42,000) = 16.88, truncated to 16 contracts.
Never round up and never trade partial contracts. Note the granularity trap: a
$100,000 account gives 1.688 -> 1 contract, too coarse to diversify. Small accounts
cannot run this system properly.

## Entries: two Donchian breakout systems

A breakout = price exceeding the highest high or lowest low of the preceding N days.
Enter the moment price trades one tick beyond the level, intraday, not on the close.
On a gap open through the level, enter at the open. Buy 1 unit on an upside breakout
(go long), sell 1 unit on a downside breakout (go short). You allocate equity between
the two systems as you like (all System 2, a 50/50 split, etc.).

- System 1 (short-term): 20-day breakout entry.
  FILTER: skip a System 1 breakout if the LAST breakout in that market would have been
  a winner. A breakout counts as a loser if price moved 2N against it before a
  profitable 10-day exit. Direction of the last breakout is irrelevant; a losing long
  OR losing short breakout re-enables the next signal in either direction. This filter
  keeps you from re-entering right after a trend has already paid out and is rolling
  over. FAILSAFE: if you skip a System 1 entry because the prior trade won, still take
  the trade if price reaches the 55-day breakout, so you never miss a major move.

- System 2 (long-term): 55-day breakout entry. NO filter. Take every 55-day breakout
  whether or not the previous trade won. This is the simpler, always-in system.

(The narrative chapters round System 2 to "60-day"; the definitive Original Turtle
Trading Rules specify 55-day. Use 55.)

## Adding units (pyramiding)

Build a position in up to 4 units. After the initial breakout entry, add one unit each
time price moves a further 1/2N in your favor, measured from the actual fill of the
prior unit (so if the first order slipped 1/2N, the next add is a full N past the
breakout). In a fast market you can go from 1 unit to the full 4 in a single day.

Gold example, N = 2.50, breakout at 310: units added at 310.00, 311.25, 312.50,
313.75 (each +1/2 * 2.50). Always buy strength and sell weakness: when several
correlated signals fire at once, take the strongest markets long and weakest short,
and only one contract month per market (the most liquid one).

## Stops: 2N, no exceptions

Every trade risks at most 2%, which by construction is 2N of adverse price movement
(since 1N = 1%). Stop = entry - 2N for longs, entry + 2N for shorts. Predefine the
exit price before entering; if the market trades there, you are out every time,
without fail. The Turtles usually did not park stop orders with the broker (to hide
size) but exited by limit or market order the instant the stop price traded.

As you add units, raise the stops on the earlier units by 1/2N per add, so the whole
position's stop sits 2N from the most recently added unit. Total open risk therefore
stays near 2% even at 4 units. (If later units were placed with extra spacing from
gaps or skid, the stops can differ.)

Crude oil example, N = 1.20, entries at 28.30 / 28.90 / 29.50 / 30.10: after the 4th
unit all four stops sit at 27.70 (= 30.10 - 2*1.20).

ALTERNATIVE (Whipsaw): stop each unit at just 1/2N (0.5% risk), and re-enter a
stopped-out unit if price returns to its original entry. More losses and a lower win
rate but historically higher profitability, and stops never need moving because total
risk never exceeds 2% at 4 units.

## Exits: give the trend room, this is the hardest part

Exits are opposite-direction breakouts, and they are wide on purpose so you hold the
big winners.

- System 1 exit: 10-day low (for longs) / 10-day high (for shorts). Exit ALL units.
- System 2 exit: 20-day low (for longs) / 20-day high (for shorts). Exit ALL units.

These exits routinely give back 20% to 100% of open profit before triggering. The
discipline to watch profit evaporate rather than bail early is the defining trait of a
successful trend follower. Do not substitute a tighter discretionary profit target;
that is how you turn the system's few large winners into small ones and lose the edge.

## Portfolio heat: unit caps by correlation

Units are the risk currency, so cap total units across four levels to survive
correlated shocks (the day after the 1987 crash cost loaded interest-rate positions
40-60% of equity in one session; the caps kept it from being worse):

| Level | Scope | Max units |
|---|---|---|
| 1 | Single market | 4 |
| 2 | Closely correlated markets (crude+heating oil; gold+silver; the currencies) | 6 per direction |
| 3 | Loosely correlated markets (gold+copper; grains) | 10 per direction |
| 4 | Single direction, all long or all short | 12 |

"Loaded" = holding the max units for a risk level.

## Drawdown de-gearing (notional account)

Cut trading size fast in a losing streak. The Turtles ran "notional" accounts and
reduced the size used for sizing by 20% for every 10% drawdown of the original
account. A $1,000,000 account down 10% ($100,000) trades as if it were $800,000; down
another 10% (of $800,000) trades as $640,000, and so on until equity recovers. This is
geometric de-risking that protects the capital base so you live to catch the next
trend.

## Expectancy and psychology (the actual edge)

Trade only with positive expectation: over many trades the system must make money even
though most individual trades lose. Trend-following breakouts have a LOW win rate. Most
breakouts fail. In the book's 22-year test, losing trades (3,746) outnumbered winners
(1,854) roughly 2:1. The edge comes from asymmetry, cut losers near 1R, let winners
run to many R.

- R-multiple = trade profit divided by the amount risked at entry (1R). Buy gold at
  $450 with a $440 stop = $1,000 risk = 1R; a $5,000 profit is a 5R trade. Losses are
  held near 1R by the 2N stop; winners reach 10R and beyond. A handful of large-R
  trends carry the whole year.
- Because you exit losers at ~2N and many winners are worth far more, you do NOT need a
  high win rate. You need to take every signal, because skipping the one that becomes
  the 20R trend destroys the year's expectancy.
- Consistency is the system. The Turtles with the best records took every entry
  mechanically; the ones dropped from the program cherry-picked and missed trends.
- Money management is survival: avoid both extended drawdowns beyond your
  psychological limit and single-day price shocks. Aggressive sizing (risking ~3% per
  trade on this system) risked ruin overnight in 1987; steady 20-30% annual compounding
  turns $50k into millions over 20 years only if you never blow up.

## Applying this as an agent

1. Compute N per market (ATR/True Range recursion above).
2. Size each unit so 1N = 1% equity: unit = 0.01 * equity / (N * point value), truncate.
3. Enter on a 20-day (System 1, with the last-loser filter + 55-day failsafe) or
   55-day (System 2, unfiltered) breakout, one tick past the level.
4. Pyramid up to 4 units at 1/2N intervals; buy strength, sell weakness.
5. Stop every unit at 2N from entry; ratchet earlier stops +1/2N per add.
6. Exit ALL units on the 10-day (System 1) or 20-day (System 2) counter-breakout.
7. Enforce unit caps (4 / 6 / 10 / 12) and de-gear 20% per 10% drawdown.
8. Judge the strategy by expectancy and R-multiple distribution, not win rate, and
   check whether every rule was followed with no discretionary overrides.
