---
name: dynasty-roster-phase-diagnosis
description: Assign a dynasty roster exactly one of four phases (contend, retool, rebuild, dead zone) from simulated title odds vs fair share, projected starter-point rank, core age, and pick share. Use when the user asks what phase am I in, am I a contender, should I be buying or selling, am I in the middle, is my team good, where does my roster stand, do I need to rebuild, am I a fringe team, how long is my window, is standing pat fine, is my team competitive, should I tear it down, am I close, what is my timeline. Also use before any trade, sell-off, or multi-year plan, because every downstream recommendation depends on the phase call.
---

# Dynasty roster phase diagnosis

One roster gets exactly one phase. Contend, retool, rebuild, or dead zone. The phase is a measurement, not a mood, and it is produced from four numbers plus one gate.

Phase assignment only. Horizon math lives in `dynasty-championship-equity-horizon`. Sell sequencing and flip triggers live in `dynasty-rebuild-clock`. Player-level hold/sell lives in `dynasty-age-curve-timing`. Pick math lives in `dynasty-pick-portfolio-valuation`. Format ceilings live in `dynasty-league-format-leverage`. Offer shape lives in `dynasty-trade-construction`.

## The four measurements

Compute all four before naming a phase. Missing any one means no verdict.

1. **titleOdds(y=0)** from the Monte Carlo simulator, expressed as a multiple of fair share.
2. **Projected starter-point rank** from the best legal starting lineup, out of N.
3. **Value-weighted core age** of the top 5 starting assets.
4. **Pick value share** = pick dynasty value / total roster dynasty value.

Fair share = 1/N. In this 10-team league fair share is **10.0% per season**, which is **1.0 expected title per decade**. Use the 10-team basis everywhere. Do not import the 8.33% twelve-team constant; it mislabels a 10-team roster by roughly a fifth of a band.

## Phase bands

Title odds relative to fair share (10-team absolute values in parentheses).

**Read these bands against titleOdds_REACHABLE, never titleOdds_now.** Current odds
are depressed by every asset that contributes nothing to today's lineup, and picks
contribute exactly nothing by construction. See the conversion gap under Decision
procedure.

| Band | Multiple of 1/N | 10-team absolute |
|---|---|---|
| CONTEND | >= 1.5x | >= 15% |
| WIN-NOW CAPABLE | 0.8x to 1.5x | 8% to 15% |
| DEAD ZONE | 0.6x to 0.8x | 6% to 8% |
| REBUILD | < 0.6x | < 6% |
| DEEP REBUILD | < 0.4x | < 4% |

A roster in WIN-NOW CAPABLE whose CURRENT odds sit in REBUILD is the common and
expensive case: it is unconverted, not weak, and the fix is a trade rather than a
teardown.

Projected starter-point rank in a 10-team:

| Rank | Read |
|---|---|
| 1-2 | contend |
| 3 | fringe |
| 4-7 | dead zone unless the retool gate passes |
| 8-10 | rebuild |

When the two bands disagree, the lower one wins and the retool gate decides whether the roster is rebuilding on purpose or by accident.

## Measure the starting lineup, never the roster

A window is a property of the projected STARTING lineup, not of total roster value. Value you cannot start is inventory.

- Measure with best legal starting lineup points at each projected year.
- Never use rostered KTC sum.
- Never use last season's record or finish. Record is a lagging indicator and carries near zero information in the first two years of any phase.

In a 1QB league with FLEX restricted to RB/WR/TE, QB2 and QB3 contribute approximately zero starting points. They are inventory in every phase.

## Retool gate

Retool is the hardest phase to earn and the easiest to fake. All four gates required:

- (a) At least one top-12-overall-value asset under age 26 already owned.
- (b) At least 3 startable assets whose peak windows overlap for at least 3 consecutive seasons, beginning within 2 seasons. Peak ranges: QB 26-33, RB 23-27, WR 24-29, TE 25-30.
- (c) At least 15% of total roster value sitting in assets that produce zero starting points.
- (d) Pick value share between 15% and 35%.

Scoring:

- 4 of 4: retool is available.
- Exactly 3: retool is not yet available, and **the missing gate names the first move**. No gate (a) means acquire a headliner. No gate (b) means the roster is a barbell and one end must be sold. No gate (c) means there is no ammunition and the retool cannot be funded. No gate (d) below 15% means no ammunition, above 35% means liquidity-locked and picks must be converted first.
- 2 or fewer: retool is not on the menu. The real choice is contend or rebuild. Say so.

**Young-core shortcut.** If at least 2 of the top 4 starters are under the position's growTo age (RB 24, WR 25, TE 26, QB 27) AND pick share >= 22%, the phase is RETOOL even in the mid band. This is the one override that pulls a roster out of dead zone without the full gate.

## Window length W

W = the smallest y where the sum of productionRetention across starting slots falls below 0.85x the year-0 sum.

- Old core: W = 1-2.
- Balanced: W = 3.
- Young core: W = 5+.

Report W with every phase call. "You are a contender" is incomplete. "Contender with W = 2" is a decision.

Production curves for the retention sum: growth +7%/yr below growTo; flat to holdTo; then compounding decline accelerating 15% per additional year past the shoulder. RB growTo 24 / holdTo 26 / -13%. WR 25 / 28 / -8%. TE 26 / 29 / -7%. QB 27 / 33 / -6%.

## Dead zone is a failure state, not a strategy

Inside 0.6x to 1.0x fair share, never output a neutral or stand-pat recommendation. Force a phase choice and print CTE(8) for both committed paths.

Simulated 8-year expected titles in this format:

| Path | Expected titles over 8 yrs | P(at least one) |
|---|---|---|
| Perpetual mid (~7%/yr) | 0.56 | 44% |
| All-in 3 years then collapse | 0.63 | 49% |
| Committed rebuild | 0.85 | 60% |
| Sustained top-4 | 0.96 | 64% |

The middle is dominated by both alternatives. It is the only square on the board with no upside tail, and its draft slot is a mid-first.

If a stand-pat recommendation is ever made from the mid band, it must state its own CTE(8) against both committed paths and beat both. Feeling safe is not a result.

## Diagnostic questions before any verdict

1. What year do you intend to flip?
2. What horizon is this evaluated on, and is it at least flip year + 4?
3. Which of your top-8 assets pass the flip-year age test (age + years_to_flip <= holdTo: RB 26, WR 28, TE 29, QB 33)?
4. What is your value share versus 1/N?
5. What are the written flip triggers, and who checks them?
6. Which assets have zero marginal lineup contribution today?

Any question without an answer means the phase call is unspecified. Say which one is missing rather than guessing.

## Decision procedure

1. Compute best legal starting lineup points and rank, for all N rosters, at y=0.
2. Run the simulator for **titleOdds_now** (y=0, roster exactly as it stands).
3. Run it again for **titleOdds_reachable**: the same roster with every
   zero-lineup-contribution asset converted into startable production at market
   rates. That means picks, QB2 and beyond in a 1QB league, TE3 and beyond behind
   an elite TE1, and anyone at or below replacement
   (`dynasty-replacement-level` measures which). Model both sides of each trade.
4. **Classify on titleOdds_reachable. Report both.** Express as multiples of 1/N.
5. Compute W, value share, pick share, top-3 concentration, core age.
6. Score the retool gate, 0 to 4.
7. Assign the phase from the REACHABLE number:
   - reachable >= 1.5x OR rank <= 2 -> CONTEND.
   - reachable 0.8x to 1.5x -> **WIN-NOW CAPABLE**. The lineup is weak and the
     ammunition is not. This is a conversion problem, not a phase problem.
   - reachable 0.6x to 0.8x AND retool gate 4 of 4, or young-core shortcut -> RETOOL.
   - reachable < 0.6x AND rank >= 0.7N -> REBUILD (< 0.4x is DEEP REBUILD).
   - Otherwise -> DEAD ZONE. Print CTE(8) for committed contend and committed
     rebuild, and force the choice.
8. Output: phase, both odds figures, the conversion gap, W, the measurements, VPP,
   and the single first move.

### The conversion gap, and why classifying on current odds is a bug

```
conversion gap = titleOdds_reachable / titleOdds_now
```

Picks contribute **exactly zero** to a current lineup, by construction. So a roster
holding heavy pick capital posts artificially low current odds, and a rule that reads
current odds alone will label it REBUILD when the picks are the very thing that would
make it contend. The measured error on this roster was a factor of seven.

**Gap above 3x means the diagnosis is CONVERSION, not phase.** Say "unconverted", not
"weak". A team told to rebuild when it was already holding the ammunition to contend
loses years to a wait it never needed. This exact misclassification shipped once.

## Failure modes

1. **Treating middle as a phase.** Dead zone is what happens when nobody chooses. Outputting "stay the course" from the 0.6x to 1.0x band is the single most expensive mistake in the taxonomy, worth roughly 0.56 expected titles per 8 years against 0.85 for committing.
2. **Anchoring on record or last season's finish.** Both are lagging by one to two seasons and carry no information about phase health. Use simulated title odds and projected starter-point rank.
3. **Confusing total roster value with starting strength.** A roster can lead the league in KTC sum and rank 8th in points it can actually field. Value share above 12.4% with bottom-third starter points is misdeployment, and the fix is lineup shape or consolidation, never a teardown.
4. **Using "retool" as a euphemism for doing nothing.** The gate exists to stop this. Score it 0 to 4 and name the missing gate. If VPP rose year over year, the retool claim is false.
5. **Importing 12-team, 4-playoff-spot orthodoxy into a 10-team, 6-playoff league.** Fair share here is 10.0%, not 8.33%. Playoff entry is cheap at a 60% berth rate, the top-2 bye is the only regular-season prize worth paying for, and the format ceiling for the best roster is roughly 25-30% per season. Any single-season model output above ~30% in this format is suspect.
6. **Projecting only your own roster forward.** Rivals age and convert picks too. A one-sided projection inflates your future rank and can turn a rebuild call into a false fringe call.
7. **Selling youth during a rebuild.** The sell list is generated by the intersection of high current value and steep forward decay. Young producers at premium positions are the payoff arriving early.

## References

- `references/value_share_and_pv_fv.md`: load when comparing present-value rank to 3-year future-value rank or checking value share bands
- `references/convexity_vpp_league.md`: load when explaining why half-measures fail, reporting VPP, or projecting the league forward
- `references/worked_example.md`: load for a full phase call in the required output format and the earlier-misclassification audit
