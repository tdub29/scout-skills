---
name: dynasty-league-format-leverage
description: Use BEFORE applying any dynasty heuristic, to recompute title-odds ceiling, seed values, replacement level, and positional scarcity from this league's own slot counts and playoff field. Triggers on "does league size change this", "is the number 1 seed worth chasing", "should I push for a bye", "what are the playoff odds", "how many QBs should I roster", "is my third QB worth anything", "how good do I need to be to win", "what's a realistic title percentage", "does 6 of 10 making playoffs matter", "is this advice right for a 10-team league", "taxi squad value", "how many wins do I need", "what does the format change", "seed value", "replacement level", "positional scarcity", "is 30% title odds realistic", "should I trade for a starter to make the playoffs".
---

# League format leverage

Format sets the payoff table. Every dynasty heuristic in circulation was written for some other format, usually 12 teams, 1 FLEX, 4 playoff spots. Recompute the payoff table from this league's own settings before quoting any rule of thumb.

Baseline league here: 10 teams, 1QB, PPR. Starters QB/RB/RB/WR/WR/TE + 4 FLEX (RB/WR/TE only). 6 of 10 make playoffs, top 2 get byes, 3 single-week rounds.

This skill prices the format. It does not decide phase (see `dynasty-roster-phase-diagnosis`), horizon (`dynasty-championship-equity-horizon`), sell timing (`dynasty-age-curve-timing`), pick math (`dynasty-pick-portfolio-valuation`), rebuild sequencing (`dynasty-rebuild-clock`), or offer shape (`dynasty-trade-construction`).

## Sections 1-5: Format Math

Sections 1-5: structural seed equity, title % by rank, weekly math, record thresholds, starter demand and the 1QB discount. The decision procedure below refers to these section numbers. See `references/format-math.md`.

## Sections 6-10: Replacement, Taxi, Risk

Sections 6-10: replacement level, taxi and IR, format sensitivity, risk posture, projection error. See `references/scarcity-and-risk.md`.

## Decision procedure

Run in order. Do not skip to a heuristic.

1. **Read the settings.** Team count, starter slots, FLEX count and eligibility, playoff field, bye count, round length, taxi/IR, waiver depth. If any is unknown, ask before answering.
2. **Recompute the payoff table.** Seed equity (section 1), rank-to-title map (section 2), win thresholds (section 4). Never quote a number from another format.
3. **Locate the roster on the rank table**, using projected starter points or all-play, not record.
4. **Price the ask in points per week** using section 3. Convert every proposed move to a delta in weekly starter points, then to a title-odds multiplier. Reject anything under +5.
5. **Check which cliff the move buys.** Only the 6/7 boundary and the 2/3 boundary carry structural equity. If the move lands inside seeds 3-6 or inside seed 1-2, it bought 0.
6. **Recompute scarcity from slot counts** (section 5). Flag every asset with zero marginal lineup contribution.
7. **Set replacement level** (section 6) and re-price all outgoing depth in any consolidation.
8. **Ask the taxi/IR rule** before valuing any stash (section 7).
9. **Set risk posture from current title odds** (section 9).
10. **State the number.** Every recommendation ships with the current title %, the delta in points per week required, and which cliff it buys. A recommendation without those three is invalid output.

## Diagnostic questions

Ask these before applying any dynasty rule of thumb.

1. How many teams, how many playoff spots, how many byes, and are rounds one week or two?
2. Exactly which slots start, and what is FLEX-eligible?
3. What is the projected starter-point rank, and what is the all-play record? (Not the win-loss record.)
4. How many points per week does this move add to the starting lineup?
5. Which cliff does that buy: the 6/7 boundary, the 2/3 boundary, or neither?
6. Are there taxi and IR slots, and are they open?
7. How deep is the waiver wire, and what does a replacement FLEX score per week?
8. Which rostered assets cannot enter the legal starting lineup this week?
9. What format was the advice being quoted originally written for?

## Worked Example

A step-by-step run of the decision procedure on the owner's 10-team league. See `references/worked-example.md`.

## Failure modes

1. **Chasing the 1 seed.** Seed 1 over seed 2 is worth 0.0 points of structural equity. The bye is the target, not the top line.
2. **Paying to move within seeds 3-6.** Worth 0.0 points. This is the single most common wasted purchase in a 6-team bracket.
3. **Presenting a projected top-2 finish as a plan without stating the failure rate.** The best projected roster wins 33.9% of the time. That plan fails ~66-70% of the time and the number must be said out loud.
4. **Quoting a title % above 30-35% for one season in this format.** Structurally impossible without a +30 pts/wk edge. Re-check the sim.
5. **Porting 12-team, 1-FLEX, 4-playoff-spot heuristics into a 10-team, 4-FLEX, 1QB league with live waivers.** "Never be mediocre", "bench depth is worthless", "QB depth has value", and "consolidation is expensive" all invert or weaken here.
6. **Pricing a 1QB QB surplus off KTC.** KTC blends superflex. QB3's KTC number is a superflex price for an asset with zero lineup contribution in this format.
7. **Using win-loss record as the input.** Record carries schedule luck. Use projected starter points or all-play.
8. **Valuing a young-asset stash without asking the taxi/IR rule.** The answer changes by 8-10 PPR points per week per stash.
9. **Buying floor at low title odds, or buying variance at high title odds.** The correct posture flips at roughly 10% and again at 20-25%.
10. **Using projection error as an argument to stay mediocre.** Higher tau moves the 8th team from 2.4% to 3.5%. That is a rounding error, not a strategy. Its real use is capping what a contender pays for a one-year peak.

## References

- `references/format-math.md`: load when computing seed equity, title % by rank, weekly win probability, record thresholds or the 1QB discount.
- `references/scarcity-and-risk.md`: load when pricing depth, taxi/IR stashes, single-week round effects, risk posture or projection error.
- `references/worked-example.md`: load when a full end-to-end application of the decision procedure helps.
