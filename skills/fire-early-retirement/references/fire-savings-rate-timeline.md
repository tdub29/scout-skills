# Savings Rate & Timeline â€” The "shockingly simple math" of early retirement

## The framework

> **Your time to financial independence depends almost entirely on your SAVINGS RATE â€” not your income.**

This is Mr. Money Mustache's "shockingly simple math of early retirement." Given an assumed investment return and a safe withdrawal rate, the number of years until you can retire is a function of **the percentage of your take-home pay you save** â€” and almost nothing else. Two people with wildly different incomes who save the same *percentage* reach FI in the same number of years.

The reason is a closed feedback loop:

- Your **savings rate** determines how fast the portfolio grows.
- Your **spending** determines both how much you have left to save *and* how big a portfolio you ultimately need (the FIRE number = expenses Ã· SWR; see `fire-number-and-variants.md`).

So a high earner who spends most of what they make can take *longer* to reach FI than a modest earner who saves aggressively â€” because the big spender needs a far larger portfolio and is feeding it more slowly.

## The canonical table

Assuming a ~5% real return on investments and a 4% safe withdrawal rate, starting from a net worth of zero, years until you have enough to retire by savings rate:

| Savings rate (% of take-home) | Approx. years to FI |
|---|---|
| 10% | ~51 years |
| 15% | ~43 years |
| 20% | ~37 years |
| 25% | ~32 years |
| 30% | ~28 years |
| 40% | ~22 years |
| 50% | ~17 years |
| 65% | ~10.5 years |
| 75% | ~7 years |
| 80% | ~5.5 years |

*(Illustrative, as of 2026 â€” verify current-year assumptions. The exact years shift with the assumed real return and chosen SWR; the SHAPE â€” savings rate dominates â€” is the durable insight, not the precise cell values.)*

The curve is steep at the top: moving from a 10% to a 25% savings rate cuts ~19 years; moving from 50% to 65% cuts another ~6.5. Each incremental percentage point saved is worth more than the last because it works on both levers at once.

## The double-lever insight

Cutting your spending is uniquely powerful because **one dollar of spending reduction does two things**:

1. **Raises the savings rate** â€” that dollar is now saved instead of spent, accelerating accumulation.
2. **Lowers the FIRE number** â€” every recurring dollar of spending you eliminate reduces the target by `1 Ã· SWR` dollars (at 4%, by **$25**; at 3.5%, by ~$28.60). A $1,000/yr recurring expense you cut shrinks your required portfolio by ~$25,000.

A raise that you spend has almost no effect on your FI date. A raise that you bank â€” or a recurring expense you eliminate â€” moves the date dramatically. This is why the FIRE community fixates on the *big three* recurring costs (housing, transportation, food) rather than small one-off frugality wins.

## How to apply

1. **Compute the savings rate as a percentage of take-home pay** = (income âˆ’ spending) Ã· income (using after-tax take-home as the base). Be honest about gross-up: employer 401(k) match and pre-tax contributions count as savings.
2. **Read the timeline off the relationship**, stating the assumed return and SWR explicitly so the user knows the estimate's sensitivity.
3. **Show the two levers.** When the user asks "should I earn more or spend less," show that spending cuts move both the numerator (savings rate) and the FIRE number, while raises only help if banked.
4. **Quantify a specific cut.** Translate a recurring expense into portfolio terms: "dropping this $300/mo ($3,600/yr) cost lowers your target by ~$90k at 4% and raises your savings rate."
5. **Chain to the number.** Once the savings rate sets the timeline, confirm the destination with `fire-number-and-variants.md` and the withdrawal assumptions in `fire-safe-withdrawal-rate.md`.
6. For *why* lifestyle inflation eats raises and how to resist it, hand off to `behavioral-economics` (mental accounting, hedonic adaptation) and `marketing-psychology` â€” do not duplicate them here.

## Common failure modes

- **Optimizing income while ignoring spending.** A higher salary that's fully spent leaves the FI date roughly unchanged because it inflates the required portfolio in lockstep.
- **Using gross income as the savings-rate base inconsistently.** Pick a convention (take-home, or gross including pre-tax savings) and apply it consistently; mixing them distorts the rate.
- **Treating the table cells as precise.** They depend on the return and SWR assumptions; present them as the shape of a relationship, not a guarantee.
- **Chasing tiny frugality wins while ignoring the big three.** Skipping lattes barely moves the savings rate; housing/transport/food restructuring moves it a lot.
- **Forgetting starting net worth and one-time windfalls.** The canonical table starts at zero; existing assets, an inheritance, or home equity shift the timeline.

## References

- "The Shockingly Simple Math Behind Early Retirement," Mr. Money Mustache (2012), as the canonical source of the savings-rate-to-timeline relationship.
- Related: [fire-number-and-variants.md](fire-number-and-variants.md) (the destination the savings rate is racing toward), [fire-safe-withdrawal-rate.md](fire-safe-withdrawal-rate.md) (the SWR that sets the multiple). For the psychology of lifestyle inflation use `behavioral-economics` and `marketing-psychology`.
- Figures as of 2026 â€” verify current-year values; the timeline cells depend on the assumed real return and SWR.
