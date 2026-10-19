# Format Math: Seeds, Title Odds, Weekly Math, Scarcity

## Contents

- [1. Structural seed equity: two cliffs, nothing else](#1-structural-seed-equity-two-cliffs-nothing-else)
- [2. Title % by projected starter-point rank](#2-title--by-projected-starter-point-rank)
- [3. Weekly math (the conversion engine)](#3-weekly-math-the-conversion-engine)
- [4. Record thresholds and the win-value curve](#4-record-thresholds-and-the-win-value-curve)
- [5. Starter demand sets scarcity, not NFL talent](#5-starter-demand-sets-scarcity-not-nfl-talent)

## 1. Structural seed equity: two cliffs, nothing else

Simulate 300k brackets with all six playoff teams set to identical strength. Structure alone, zero team quality:

| Seed | Title % |
|---|---|
| 1 | 25.1 |
| 2 | 25.0 |
| 3 | 12.5 |
| 4 | 12.5 |
| 5 | 12.4 |
| 6 | 12.4 |
| missed | 0.0 |

Bye multiplier = 2.00x exactly. Seed 1 over seed 2 = 0.0 points. Seed 3 over seed 6 = 0.0 points.

There are exactly two cliffs:
- **6/7 boundary**: missing to qualifying = +12.5 points.
- **2/3 boundary**: the bye = +12.5 points.

Buying seeding anywhere else buys zero. A team that pays a first to move from projected 5th to projected 3rd bought nothing structural.

## 2. Title % by projected starter-point rank

10 teams, team-strength SD 12, projection error tau 9, sigma 26, 14 weeks, 200k sims:

| Rank | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Title % | 33.9 | 20.5 | 14.3 | 10.4 | 7.6 | 5.4 | 3.8 | 2.4 | 1.3 | 0.4 |
| Bye % | 64 | 42 | 30 | 21 | 16 | 11 | 8 | 5 | - | - |

Ceiling for the best roster is 25-35%, with 30-35% typical. Nothing under a +30 points/week lineup edge over league average breaks 50%. **Treat any single-season model output above 30-35% in this format as suspect and re-check the sim before acting on it.**

## 3. Weekly math (the conversion engine)

p = Phi(delta / (sigma x sqrt(2))), sigma ~= 26 PPR points for a 10-starter lineup.

| delta (pts/wk) | +5 | +10 | +15 | +20 | +25 | +30 |
|---|---|---|---|---|---|---|
| p | 55.4% | 60.7% | 65.8% | 70.7% | 75.2% | 79.3% |

Title odds = 4p^2 x baseline with a bye, 8p^3 x baseline without.

| delta | bye mult | no-bye mult |
|---|---|---|
| +5 | 1.23x | 1.36x |
| +10 | 1.47x | 1.79x |
| +15 | 1.73x | 2.28x |
| +20 | 2.00x | 2.83x |

Rule of thumb: **+10 points per week of starter production is worth about the same as a first-round bye.**

Convexity from a **generic** projected-8th roster: +0/+5/+10/+15/+20/+25/+30 pts/wk gives 2.5/4.4/7.4/11.6/17.0/23.3/30.2% title. The 2.5% start is the structural rank-8 figure from section 2, not this roster; the owner's own sim reads 1.46%, below the generic shape. Do not read the two as the same baseline. Marginal gain per additional 5 points: 1.9, 3.1, 4.2, 5.4, 6.3, 6.9. Strictly increasing across the whole feasible range. Convex payoffs forbid half measures.

**Hard reject rule.** Any win-now trade that raises projected weekly starter points by less than 5 is rejected on structural grounds. It moves a single-week matchup from 50.0% to 55.4% and multiplies title odds ~1.25x, which never justifies a first in a 10-team league where firsts average roughly the 5.5th player off the board.

## 4. Record thresholds and the win-value curve

14-game season. P(make playoffs | record): 8-6 = 100%, 7-7 = 87%, 6-8 = 37%, 5-9 = 4%, 4-10 = 0%. Median seed 1 is 11-3, median seed 2 (last bye) is 10-4, median seed 6 is 7-7.

Marginal title equity per win: wins 1 through 7 buy 5.5 points total (~0.8/win). Wins 8 through 10 buy ~21 points (~7/win). Ratio 9:1 in favor of the last three wins.

Practical: at 7-7 with two weeks left, entry is settled at ~87%. Stop paying for it. Redirect remaining capital at the bye (needs ~10 wins) or bank it. At 6-8 or worse, entry is <=37% and the season is a sell window, not a push window.

Use projected starter points or all-play as the input, never record. Record carries schedule luck; the seed cliffs are what you are actually buying.

## 5. Starter demand sets scarcity, not NFL talent

10 teams x (QB/RB/RB/WR/WR/TE + 4 FLEX limited to RB/WR/TE) = **10 QB slots and 90 skill slots** weekly.

| Position | Supply / demand | Ratio |
|---|---|---|
| QB | ~32 / 10 | 3.2x oversupply, least scarce position in this format |
| TE | ~14 / ~14 | ~1.0x, scarcest |
| RB, WR | - | 1.1-1.2x |

**Roster exactly 1 QB in this league.** QB3 has ~0 value over replacement because QB11 is on waivers. QB2 is worth ~1.5 expected starts x 4-6 points of per-game edge = **6 to 9 points per season**, injury insurance only, and measured at 0.22pp of title odds. Traded for a startable WR the pair of spares is worth **+0.82pp**, so the second QB is a holding position, not a roster slot you defend. `dynasty-replacement-level` owns this call and carries the measurement; it is the authority if the two ever disagree.

### The 1QB discount, quantified

Never price a 1QB QB off a superflex or blended number. Here is the conversion,
measured across 337 players appearing on both KTC lists (`ktc-oneqb` vs `ktc-superflex`):

| Pos | median 1QB / SF | vs the skill baseline |
|---|---|---|
| QB | **0.859** | **0.70x** |
| RB | 1.231 | 1.00x (baseline) |
| WR | 1.229 | 1.00x |
| TE | 1.199 | 0.97x |

The two KTC lists are normalized differently, so the raw column is not the answer.
The right-hand column is: divide each position's ratio by the skill-position ratio
(~1.23). **A QB is worth ~70% as much, relative to skill players, in 1QB as in
superflex.**

The discount is steepest at the top, which is the opposite of most people's intuition:

| QB tier | median 1QB/SF | relative |
|---|---|---|
| QB1-6 | 0.770 | **0.63x** |
| QB7-12 | 0.835 | 0.68x |
| QB13-24 | 0.847 | 0.69x |
| QB25+ | 0.914 | 0.75x |

Tiers are by rank on the 1QB board (40 QBs appear on both lists). Re-derive with the check in `site/js/dynasty-claims.test.js` after any `build_ktc.py` run; the raw medians drift with the board, the relative column has been stable.

Elite QBs lose the MOST converting to 1QB, because superflex demands two starters
and scarcity concentrates at the top. In 1QB that scarcity does not exist.

**Operationally:** use `ktc-oneqb` directly; it already carries the adjustment. If a
counterparty quotes a superflex or "KTC value" number for a QB, multiply by 0.70 (0.63
if he is a top-6 QB) before comparing it to a skill player. Getting this wrong is how
you accept a QB1 as a headliner and think you won.

Pair with `dynasty-replacement-level` for the other half: what the QB you keep is worth
against the best QB sitting on waivers.
