# Replacement Level, Taxi, Format Sensitivity and Risk Posture

## 6. Replacement level and lineup depth

Measured, not estimated: **304 distinct rostered players, 30.4 per team** (active plus taxi plus reserve) against **559 projected skill players**, leaving **257 free, 46%**. Replacement FLEX production is **8-10 PPR points per week**, roughly 7% of a 125-point lineup.

Do not quote "~40%" or "roughly half"; both shipped in earlier passes of this family and both are wrong. The number is 46% and `dynasty-replacement-level` shows the four positional baselines that fall out of it.

Two consequences:

1. Four FLEX slots mean startable bodies 7 through 10 are real assets here. In a 1-FLEX league they are bench. Do not port bench-depth-is-worthless advice into this format.
2. Ten starters dilute stars. A +8 point/week edge is a 61.1% weekly win rate at 6 starters (SD 20), 59.7% at 8 (SD 23), **58.6% at 10 starters (SD 26)**, 57.9% at 12. Each added slot costs a star 0.5-1.0 percentage points of weekly leverage.

Discount the outgoing side of any 3-for-1 by waiver replacement level, not by KTC sum. That is the structural reason consolidation is cheaper in a 10-team league than a 14-team one.

## 7. Taxi and IR must be answered before pricing young-asset accumulation

Answer the rule before valuing any stash. Answer it, do not merely ask it: earlier passes of this family declared this question gating and then answered around it in every worked example, including the five-firsts accumulation plan.

- **No taxi/IR open**: an active-roster stash costs 8-10 PPR points per week of forgone FLEX production. Subtract that from the stash's expected value.
- **Taxi/IR open**: charge zero. Rebuilding is structurally cheaper in this league than in one without taxi, and the accumulation math changes materially.

### Measured, Password is taco 2026

`roster_positions` does not list TAXI or IR, which reads like "no taxi" and is wrong. Sleeper keeps the slot counts in league `settings` and the site export dropped them until 2026-08-08. The occupancy is observable anyway, on every roster:

| | taxi used | reserve used | total rostered |
|---|---|---|---|
| League, per team | [5, 4, 3, 5, 2, 5, 5, 4, 4, 2] | 0 to 2 | 27 to 35 |
| **The owner** | **2**, tied for fewest | 1 | 30 |

**Taxi is open and eight of nine rivals use at least as much of it as the owner.** So charge zero for a stash here, and note that the owner is carrying 2 where five rivals carry 4 and 5. On a roster whose thesis is accumulating young assets, unused taxi slots are the cheapest thing on this list to fix.

For the exact slot counts and the waiver rule, re-run `python site/data/fetch_sleeper.py && python site/data/build_site_data.py`; `build_site_data.py` now captures `taxi_slots`, `reserve_slots`, `waiver_type` and `waiver_budget`. Until that rebuild lands, read occupancy off the `taxi` and `reserve` arrays and say which you used.

Any young-asset plan quoted without this rule stated is unpriced.

## 8. Format sensitivity: single-week rounds tax excellence

| Format | Best team | Projected 8th |
|---|---|---|
| 6 teams, 3 single-week rounds (this league) | 33.9% | 2.4% |
| 6 teams, 3 two-week total-points rounds | 38.4% | 1.7% |
| 4 teams, 2 rounds | 34.0% | 2.3% |
| 8 teams, 3 rounds, no bye | 30.1% | 3.4% |

Single-week rounds are the maximum-variance setting. They tax regular-season excellence and subsidize merely qualifying, which weakens every "push for the top seed" argument by roughly 10-12% relative to a two-week format.

A 60% qualification rate makes "never be mediocre" far weaker here than the 12-team, 4-spot orthodoxy it came from. Entry is cheap; the bye is the expensive thing.

## 9. Risk posture is state-dependent

The payoff is a step function at the championship, so the correct risk preference flips with your own odds.

- **Below ~10% title odds**: buy variance. Concentrate, take the high-ceiling asset, accept the wider distribution.

**Tiebreak against `dynasty-trade-construction`.** That skill caps top-3 value
concentration at 35% while startable bodies are under 13. The cap wins. Risk-seeking
means preferring the higher-ceiling asset at equal cost, not fielding an illegal
lineup in week 9. Below 10% odds, concentrate UP TO the cap and no further; the
first constraint is that you can fill ten slots every week.
- **Above ~20-25%**: buy floor. Depth, bye coverage, injury insurance, handcuffs.

Maximizing expected starter points is the wrong objective in both regimes.

## 10. Projection error transfers equity to the field

Raising preseason projection error tau from 0 to 5 to 9 to 14 points per week:

| tau | 0 | 5 | 9 | 14 |
|---|---|---|---|---|
| Best team | 39.2% | 37.2% | 34.1% | 29.6% |
| 8th team | 1.2% | 1.6% | 2.4% | 3.5% |

Every point of forecast uncertainty moves title equity from favorites to the field. Use this to **cap what a contender pays for a one-year peak**. Never use it as a reason to stay mediocre; the 8th team's gain is 2.3 points, which buys nothing.
