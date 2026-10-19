# FIRE Number & Variants â€” How much you need, and which flavor of FIRE fits

## The framework

> Your **FIRE number** is the portfolio value at which work becomes optional: **annual expenses Ã· safe withdrawal rate (SWR)**.

This single ratio is the spine of every FIRE plan. The SWR you divide by is the percentage of the portfolio you can pull in year one and keep withdrawing (inflation-adjusted) without running out â€” see `fire-safe-withdrawal-rate.md`. The FIRE number is exquisitely sensitive to *both* inputs: lowering expenses shrinks the numerator, and your chosen SWR sets the multiplier.

**The multiplier math** (FIRE number = expenses Ã· SWR = expenses Ã— multiple):

| Safe withdrawal rate | Multiple of annual expenses | $60k/yr expenses â†’ number |
|---|---|---|
| 4.0% | 25Ã— | $1.50M |
| 3.5% | ~28.6Ã— | ~$1.71M |
| 3.25% | ~30.8Ã— | ~$1.85M |

So the famous "**25Ã— rule**" is just the 4%-SWR case: save 25 times your annual spending. Early retirees with 40â€“60 year horizons commonly use a more conservative 3.25â€“3.5% SWR (â‰ˆ28.6â€“30.8Ã—) â€” see `fire-safe-withdrawal-rate.md` for why a longer horizon lowers the safe rate.

*(All figures as of 2026 â€” verify current-year values; SWR research is updated annually.)*

## The variants

FIRE is not one target. The variants differ by **how big the number is** and **whether you fully stop working**.

### Lean FIRE
- **Definition:** Financial independence built on a frugal, minimalist budget â€” typically well below median household spending (often cited around <$40k/yr for a household, but it's relative to a deliberately lean lifestyle).
- **Math:** Small annual expenses â†’ small FIRE number. At 4% SWR, $30k/yr expenses â†’ $750k.
- **Who it fits:** People comfortable with frugality, low-cost-of-living areas, no kids or grown kids, who value time over consumption. Fragile to lifestyle creep, medical shocks, and inflation because there's little slack in the budget.

### Fat FIRE
- **Definition:** Financial independence at a comfortable-to-affluent spending level â€” no meaningful belt-tightening, room for travel, healthcare, and discretionary spending.
- **Math:** Large annual expenses â†’ large FIRE number. At 4% SWR, $150k/yr expenses â†’ $3.75M.
- **Who it fits:** High earners and savers who refuse to downgrade their lifestyle, want a big safety margin, and can tolerate a much longer accumulation phase. The most resilient to shocks because there's discretionary spending to cut if needed (ties to flexible withdrawal â€” see `fire-flexible-withdrawal-guardrails.md`).

### Coast FIRE
- **Definition:** You have *enough already invested* that **compounding alone** will reach your full FIRE number by traditional retirement age â€” **no further contributions required**. You still work to cover current living expenses, but you no longer need to save for retirement.
- **Math:** Solve for the invested balance needed today:
  > **Coast number = target FIRE number Ã· (1 + r)^years**
  where `r` is the assumed real annual return and `years` is time until traditional retirement age. Example: target $1.5M at age 65, you're 35 (30 years), assume 5% real return â†’ $1.5M Ã· (1.05)^30 = $1.5M Ã· 4.322 â‰ˆ **$347k** invested today and you can "coast."
- **Who it fits:** Younger savers who front-loaded investing and now want to reduce career intensity, take a lower-paying-but-fulfilling job, or stop the savings grind without touching the nest egg.

### Barista FIRE
- **Definition:** You retire from full-time career work but take **part-time or partial income** (the canonical "barista" job, often valued for employer **health benefits**) that **bridges the gap** between portfolio withdrawals and total spending.
- **Math:** Portfolio need = (annual expenses âˆ’ part-time income) Ã· SWR. If you spend $60k/yr and earn $20k part-time, you only need to support $40k from the portfolio â†’ at 4%, $1.0M instead of $1.5M. Employer health coverage also removes the ACA-bridge problem (see `fire-healthcare-bridge-aca.md`).
- **Who it fits:** People who want out of the career grind but are fine with light work, especially for benefits, and want to shrink the required number.

### Flamingo FIRE
- **Definition:** A staged path â€” reach **half your FIRE number** ("half-FI"), then **coast** (stop contributing) while compounding doubles the balance to the full target, often while working part-time or a lower-stress job in the interim.
- **Math:** Half the FIRE number, left to compound. At ~7% nominal it roughly doubles in ~10 years (rule of 72); at 5% real, ~14â€“15 years. So reaching half the target and coasting buys you out of full-time saving roughly a decade-plus before full FIRE.
- **Who it fits:** A hybrid of Coast and Barista for people who want a defined two-phase plan: grind to half, then downshift.

## How to apply

1. **Nail down real annual expenses** â€” not gross income, not current spending if it includes savings. Use actual or projected post-retirement spending, including a healthcare line (big pre-65; see `fire-healthcare-bridge-aca.md`).
2. **Pick a SWR for the horizon.** For a 40â€“60 year early retirement, lean toward 3.25â€“3.5% (28.6â€“30.8Ã—) rather than 4% â€” see `fire-safe-withdrawal-rate.md`.
3. **Compute the FIRE number:** expenses Ã· SWR. Show the multiple so the user feels the leverage of each input.
4. **Match the variant to the life, not the other way around.** Ask: Do they want to fully stop working (Lean/Fat) or keep partial income (Barista)? Are they front-loaded and want to downshift now (Coast/Flamingo)? Output the **named variant + the target number**.
5. **Stress the double lever.** Cutting expenses lowers the number *and* (per `fire-savings-rate-timeline.md`) raises the savings rate that gets you there.
6. For the *emotional* "is this enough / can I really stop" question, hand off to `behavioral-economics` (one-more-year trap) and `difficult-conversation` (the partner conversation). For checking whether the underlying portfolio is allocated sensibly, cross-reference the Sure skill `whole-wealth-audit`.

## Common failure modes

- **Using gross income instead of real expenses.** The FIRE number is driven by spending, not earning. A $200k earner who spends $60k needs $60k Ã— multiple, not $200k Ã— multiple.
- **Anchoring on 25Ã— for a 50-year retirement.** 25Ã— (4%) was validated for a 30-year horizon; very long horizons need a lower SWR and thus a larger multiple â€” don't default to 25Ã— for a 35-year-old.
- **Ignoring healthcare and taxes in "expenses."** Pre-65 health premiums and the taxes owed on withdrawals are real spending; omitting them understates the number.
- **Coast-FIRE math with a nominal return where a real (inflation-adjusted) target is used (or vice versa).** Keep the discount rate and the target consistent â€” both real or both nominal.
- **Treating Lean FIRE as risk-free.** A lean budget has no slack to cut in a downturn, which removes the flexibility that makes higher withdrawal rates safe (see `fire-flexible-withdrawal-guardrails.md`).
- **Forgetting the variants are points on a spectrum.** Many real plans are blends (e.g., Coast now, Barista at 50, full at 60).

## References

- William Bengen (1994) and the Trinity study lineage for the 4% / 25Ã— basis; Morningstar *State of Retirement Income* (2026) for current SWR base cases.
- Related: [fire-safe-withdrawal-rate.md](fire-safe-withdrawal-rate.md) (the SWR you divide by), [fire-savings-rate-timeline.md](fire-savings-rate-timeline.md) (how fast you reach the number), [fire-flexible-withdrawal-guardrails.md](fire-flexible-withdrawal-guardrails.md) (flexibility lets you spend more / carry a smaller number), [fire-healthcare-bridge-aca.md](fire-healthcare-bridge-aca.md) (the healthcare line in expenses). For portfolio allocation use the Sure skill `whole-wealth-audit`; for the psychology of "enough" use `behavioral-economics`.
- All figures as of 2026 â€” verify current-year values before relying on them.
