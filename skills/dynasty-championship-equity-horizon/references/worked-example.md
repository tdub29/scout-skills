# Worked Example

## Worked example: the owner's roster, same paths, opposite verdicts

10-team, 1QB PPR. 8th of 10 in projected starter points, titleOdds_now 1.4%,
titleOdds_reachable 10.2%, young top (RB Love 21, RB Achane 24, TE McBride 26), 5
firsts, three startable QBs in a 1QB league.

These are MEASURED trajectories from the simulator, not illustrative shapes.

| Plan | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| Convert and contend | 10.2% | 9.2% | 8.5% | 7.7% | 5.2% |
| Do nothing | 1.4% | 4.0% | 6.1% | 9.0% | 9.7% |
| Tear down and rebuild | 0.0% | 0.0% | 0.1% | 0.4% | 1.0% |

Over 10 seasons:

| Plan | Raw sum | DCE at delta=0.88 |
|---|---|---|
| Convert and contend | 61.9% | **43.1%** |
| Do nothing | 77.6% | 42.5% |
| Tear down and rebuild | 45.4% | 21.0% |

Two lessons, and the second one is the one that was learned the hard way.

**The horizon really does move verdicts.** Do-nothing's raw sum (77.6%) beats
contend's (61.9%), and discounting reverses it. A rebuild's raw sum likewise looks far
better than its discounted one, 45.4% against 21.0%. Anyone quoting an undiscounted
sum over a long window is arguing for patience by arithmetic sleight of hand.

**But the horizon is not a licence.** Here the rebuild loses at EVERY horizon and every
discount tested, and it spends five consecutive seasons in last place to do it. The
horizon rule exists to stop a good rebuild being rejected by a short window. It does
not make a bad rebuild good, and it is not a reason to skip
`dynasty-roster-phase-diagnosis`. On this roster the reachable number was 1.02x fair
share, which meant the correct call was CONVERT, and the horizon argument was being
used to defend a teardown that never should have been on the table.

**Check the reachable number first. Then argue about the window.**

- delta-star for this pair = **0.84**. Inside [0.80, 0.95], so this is discount-sensitive: it genuinely hinges on how many more seasons he plays.
- break-even year at p_0 = 1.4% in a 10-team league = **3 + 0.14 = year 3.1**.
- p_0 = 1.4% means the entire year-0 cost of rebuilding is 0.014 of a 5.70-unit budget, **under 0.25% of total equity**. "This hurts next season" is a rounding error. Say it numerically.
- Three startable QBs in a 1QB league contribute exactly zero to `p_t` in every year. Their whole market value converts at **zero p_t cost**. Flag that before analyzing any harder tradeoff.
