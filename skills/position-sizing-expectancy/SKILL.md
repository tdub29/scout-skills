---
name: position-sizing-expectancy
description: Size trades and grade a system's edge using Van Tharp's R-multiples, expectancy, and position-sizing models. Use for position sizing, expectancy, R-multiple, R multiple, system quality number, SQN, percent risk, fixed fractional, risk per trade, low-risk idea, trade objectives, money management, and bet sizing questions.
---

# Position Sizing and Expectancy

Van Tharp's operating model from *Trade Your Way to Financial Freedom* (2nd ed, 2006). The premise: the entry signal almost everyone obsesses over is the least important part of a system. What actually produces returns is the size of each bet (position sizing) and how you exit, measured through R-multiples and expectancy. This skill is for sizing a trade and for grading whether a system has a real edge.

For portfolio-level risk (VaR, CVaR, Sharpe, Sortino, drawdown), use `risk-metrics-calculation`; this skill is specifically the trade-level R-multiple / expectancy / bet-sizing layer.

## The core reframe: six variables, two that matter

Tharp lists six variables behind any result: reliability (win rate), relative size of wins vs losses, cost, opportunity (how often you trade), capital, and position size. Most traders pour all their energy into variable one, the need to be right. That is the trap. The first four variables define **expectancy**; the last two are **money management (position sizing)**. Tharp weights the drivers of success roughly: psychology ~60%, position sizing ~30%, system development (including entry) the least. His own words: "Entry is probably the least important component of my trading."

The golden rule "cut your losses short and let your profits run" is entirely about **exits**, not entries. Cutting losses short is an exit; letting profits run is an exit. A system with a random entry can still be profitable if the exits and position sizing are right.

## R-multiples

R is the initial risk on a trade: the distance from your entry to your initial stop, per unit, in dollars or points. R is the symbol for "1 unit of initial risk."

An **R-multiple** is a trade's result expressed as a multiple of its own initial risk. To compute it, take the profit (or loss) captured at exit and divide by the initial risk.

Tharp's worked example: enter at 2,511 with a 3x-ATR stop of 104 points, so the initial exit sits at 2,407 and initial risk is 104 points (1R). The trade eventually exits at 3,069 for a 558-point profit. 558 / 104 = **5.37R**. Losing trades are simply negative R-multiples; if you risked $500 and lost $500 that is a -1R, a $1,000 loss on that same trade is -2R.

Why R matters: different trades have different dollar risks, but once you express every result in R and then size each position to risk a constant percentage of equity, every 1R becomes the same bet. If 1R is $1 per share you buy 1,000 shares; if 1R is $10 per share you buy 100 shares; either way you risk the same 1% of a $100,000 account. R is what makes trades comparable and sizeable.

Record every closed trade as an R-multiple. That list of R-multiples IS your system.

## Expectancy

Expectancy is the average amount you can expect to make (or lose) per dollar risked, over many trades. It is the mean of your R-multiple distribution.

**Formula 6-1** (simple two-outcome case):

```
Expectancy = (PW * AW) - (PL * AL)
```

where PW = probability of a win, PL = probability of a loss, AW = average win, AL = average loss (all expressed per dollar risked, i.e. in R).

Tharp's marble game: PW = 0.6, PL = 0.4, win or lose exactly what you risk. Expectancy = (0.6 * 1) - (0.4 * 1) = **0.20**, i.e. 20 cents per dollar risked.

**Formula 6-2** (many outcomes, additive): sum each winning bucket's (PW * AW), sum each losing bucket's (PL * AL), subtract.

```
Expectancy = Sum(PW_i * AW_i) - Sum(PL_j * AL_j)
```

His second marble game wins only **36%** of the time yet has an expectancy of **0.78** (78 cents per dollar risked), nearly four times better than the 60%-win game above. The lesson that sells the whole book: **win rate is not the edge.** A low-reliability system with big winners beats a high-reliability system with small ones.

### Expectancy from a trade list (the practical method)

1. List every closed trade as an R-multiple (profit or loss / that trade's initial risk).
2. **Expectancy (in R) = the average of all those R-multiples.** Add them up, divide by the number of trades.
3. Equivalently in dollars: net profit / number of trades gives dollar expectancy per trade; divide by average risk to get it back into R.

Tharp's sample system: 103 trades, 60 winners (58.3%), average gain $1,353.68, average loss $721.73, net profit $10,843. Expectancy per trade is net profit divided by trade count. Always reduce it to "per dollar risked" (R) so you can compare systems that trade different instruments at different prices over different time frames. That comparability is the entire reason to compute expectancy instead of just eyeballing total profit.

Expectancy alone is not enough. Multiply by **opportunity** (trades per period) to get expected return per unit time: a 0.20R edge over 100 trades a day dwarfs the same edge over 100 trades a year.

## System Quality Number (SQN)

SQN is Tharp's later refinement (post-2006) built directly on the R-multiple distribution this book teaches, so it belongs here. It grades a system by how consistent its edge is, not just how large:

```
SQN = (mean R / standard deviation of R) * sqrt(number of trades)
```

Mean R is your expectancy; the standard deviation of your R-multiples measures how noisy the results are (the 2006 edition already tells you to study the standard deviation of your R distribution). A high mean R with low dispersion scores well; a fat edge that swings wildly scores poorly. Rough reading (over ~100 trades): under 1.5 is hard to trade, 2.0-3.0 good, 3.0-5.0 excellent, above 5.0 superb, and a negative SQN means no edge. Higher SQN means the edge is real enough to size up aggressively. Note: the sqrt(N) term inflates SQN for large samples, so compare systems at a common trade count (Tharp standardizes around 100).

## Position-sizing models

Position sizing answers "how much / how many units," and it is where most of the money is made or lost. Four models, weakest to strongest:

**Model 1 - Units per fixed amount of money.** One unit per $X of equity (e.g. one contract per $50,000). Simple but weak: for a small account equity must nearly double before you can add a unit, so it is effectively no position sizing, and it forces you to take a position even when the risk is far too large.

**Model 2 - Equal value units (stocks).** Divide capital into N equal-dollar slices (e.g. five units of $10,000). Buy $10,000 of each name. Gives equal weighting and shows your leverage plainly, but again scales up slowly and ignores each position's actual risk.

**Model 3 - Percent risk (the workhorse).** Size so that your worst-case loss on the trade equals a fixed percentage of equity.

```
units = (equity * risk%) / (initial risk per unit)
```

Tharp's example: gold at $380, stop at $370, so risk is $1,000 per contract. On a $50,000 account you cap risk at 2.5% = $1,250. $1,250 / $1,000 = 1.25, so you buy **1 contract**. Same day, short corn with a 5-cent stop = $250 risk per contract; $1,250 / $250 = **5 contracts**. This is the model that makes every 1R equal across markets. It is what most people mean by "fixed-fractional" or "risk per trade." Typical settings are 0.5% to 2% of equity per trade; going too high courts ruin even with a positive expectancy.

**Model 4 - Percent volatility.** Size so that each position's daily volatility (average true range) equals a fixed percentage of equity.

```
units = (equity * volatility%) / (ATR-in-dollars per unit)
```

Tharp's example: gold ATR of $3 = $300 per contract, allow 2% of $50,000 = $1,000, so $1,000 / $300 = 3.3, buy **3 contracts**. This equalizes how much each position can swing overnight, which is what lets you sleep. Tharp himself trades a portfolio at set risk AND volatility limits as a percentage of equity.

The percentage you choose dominates the outcome. In Tharp's backtests, raising percent-risk from 0.1% to 2.5% swings net profit and drawdown by orders of magnitude; the "best reward-to-risk" setting usually carries a drawdown no human can actually tolerate, so you pick the size your objectives and stomach allow, not the size that maxes the backtest.

## Objectives first, then design

Setting objectives is a major part of system work, not an afterthought. Decide the return you want and, more importantly, the maximum peak-to-trough drawdown you can live with, before building anything. Position sizing is the knob that hits those objectives; expectancy tells you the raw edge; the entry is chosen last and matters least.

Tharp's target is a **low-risk idea**, defined exactly:

> A methodology with a long-term positive expectancy and a reward (overall return) to risk (maximum peak-to-trough drawdown) ratio with which you can live. That methodology must be traded at a risk level (usually based upon percentage of equity) that will protect you from the worst possible conditions in the short run while still allowing you to achieve the long-term expectancy.

The common failure is trading at a risk level too high to survive a normal losing streak. Even a fair coin throws long streaks of heads; a real system will hand you 5, 6, 10 losers in a row. Size small enough that such a streak cannot take you out, or the positive expectancy never gets a chance to play out.

## Operating checklist

1. Log every trade as an R-multiple (result / that trade's initial risk).
2. Expectancy (R) = average of all R-multiples. Positive is required; the bigger the better.
3. SQN = (mean R / std dev of R) * sqrt(N). Grade the edge and its consistency; compare systems at a common N.
4. Multiply expectancy by trade frequency for return per unit time.
5. Set drawdown and return objectives before sizing.
6. Size with Model 3 (percent risk) or Model 4 (percent volatility), usually 0.5% to 2% per trade, chosen to fit the drawdown you can survive, not the backtest peak.
7. Focus effort on exits and size, not the entry.
