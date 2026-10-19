# Accumulation Account Order â€” Where each dollar of savings should go first

## The framework

> When you have a dollar to invest, **the account it lands in matters as much as what it buys.** The tax-advantaged "investment order" prioritizes free money and tax shelter before taxable accounts.

This is the Bogleheads "prioritizing investments" order, adapted for FIRE. It maximizes after-tax growth by capturing the employer match and tax-advantaged space before falling back to a taxable brokerage. The exact order can shift for a given person's tax situation, but the default sequence is:

1. **401(k)/403(b)/457(b) up to the full employer match** â€” this is an instant, guaranteed return (often 50â€“100% on the matched portion). Never leave it on the table.
2. **HSA (if on an HSA-eligible high-deductible plan)** â€” the **triple tax advantage**: contributions are pre-tax, growth is tax-free, and qualified medical withdrawals are tax-free. After age 65 it behaves like a traditional IRA for non-medical withdrawals (taxed, no penalty), which is why FIRE folks call it a **"stealth IRA."** Especially powerful pre-65 when health costs are a major line item (see `fire-healthcare-bridge-aca.md`).
3. **Max IRA or Roth IRA** â€” fund the IRA to the annual limit. Roth contributions are also uniquely useful for the bridge because contributions (not earnings) are always withdrawable penalty- and tax-free (see `fire-early-access-bridge.md`).
4. **Max the 401(k)/403(b)/457(b)** to the employee deferral limit.
5. **Mega-backdoor Roth, if your plan allows it** â€” after-tax 401(k) contributions converted to Roth, on top of the regular limit. Only available if the plan permits after-tax contributions and in-plan conversion or in-service distribution.
6. **Taxable brokerage account** â€” no contribution limit; this is the workhorse for early-retirement spending before 59Â½ because it has no age restrictions (see `fire-early-access-bridge.md`). Hold tax-efficient funds and harvest losses/gains here (cross-reference `tax-loss-harvesting`, `wash-sale-detection`, `kanchi-dividend-us-tax-accounting`).

## 2026 contribution limits

*(All figures as of 2026 â€” verify current-year values; the IRS adjusts limits annually.)*

| Account | 2026 employee limit | Catch-up (age 50+) | Enhanced catch-up (ages 60â€“63) |
|---|---|---|---|
| 401(k) / 403(b) / 457(b) | **$24,500** | **$8,000** | **$11,250** (replaces the $8,000 in these ages) |
| Traditional / Roth IRA | **$7,500** | **$1,100** (total $8,600) | â€” |
| HSA â€” self-only | **$4,400** | $1,000 (age 55+) | â€” |
| HSA â€” family | **$8,750** | $1,000 each spouse (age 55+) | â€” |

**SECURE 2.0 Roth catch-up rule (effective 2026):** if your prior-year wages from the employer exceeded **$150,000**, your catch-up contributions to a workplace plan **must be made as Roth** (after-tax) â€” you can no longer make pre-tax catch-up contributions above that wage threshold. Plan for the catch-up to be Roth (and to lose the upfront deduction on it) if you're a high earner age 50+.

## Roth-vs-traditional logic for early retirees

The choice hinges on **marginal tax rate now vs. in retirement**:

- **Traditional (pre-tax)** wins when your rate *now* is higher than it will be when you withdraw. Many FIRE savers are high earners during accumulation and will have **low taxable income in early retirement** â€” so they favor **traditional now**, then **convert traditional â†’ Roth later** during low-income years to fill up low brackets cheaply (the Roth conversion ladder; see `fire-early-access-bridge.md` and `fire-withdrawal-tax-optimization.md`).
- **Roth (after-tax)** wins when your rate now is lower than later, or for the strategic benefits: no RMDs, tax-free growth, and contributions withdrawable anytime â€” making Roth space valuable for the bridge.
- **The early-retiree synthesis:** load traditional during peak-earning years to get the deduction, then exploit the low-income gap after you stop working to convert and harvest at low rates â€” but watch the ACA MAGI cliff, since conversions raise MAGI (`fire-healthcare-bridge-aca.md`).

## How to apply

1. **Capture the match first, always.** Confirm the employer match and contribute at least enough to get all of it before anything else.
2. **Use the HSA aggressively if eligible.** Treat it as a stealth retirement account â€” invest it, pay current medical costs out of pocket if you can, and let it compound.
3. **Decide Roth vs. traditional by comparing today's marginal rate to your expected early-retirement rate**, leaning traditional for high earners who plan to convert later.
4. **Build the taxable bridge deliberately.** Because steps 1â€“5 are mostly locked until 59Â½, the taxable account (step 6) and Roth contributions are what fund the years before 59Â½ â€” size them with `fire-early-access-bridge.md` in mind.
5. **Apply the 2026 limits and the SECURE 2.0 Roth-catch-up rule**, flagging that all figures are as-of-2026 and must be re-checked for the current year.
6. For tax-lot management inside the taxable account, cross-reference `tax-loss-harvesting`, `wash-sale-detection`, and `kanchi-dividend-us-tax-accounting` â€” do not modify them. For a holistic view of the whole portfolio, use the Sure skill `whole-wealth-audit`.

## Common failure modes

- **Skipping the match to fund a Roth IRA.** A 50â€“100% match beats any tax arbitrage; get the match first.
- **Ignoring the HSA's triple advantage.** Spending the HSA on current bills instead of investing it forfeits decades of tax-free growth.
- **Front-loading all Roth as a high earner.** If your current marginal rate is high and your early-retirement rate will be low, all-Roth overpays tax now; traditional + later conversions usually wins.
- **Forgetting the SECURE 2.0 Roth-catch-up requirement.** High earners (prior-year wages > $150k) can't make pre-tax catch-up contributions in 2026; budget for the lost deduction.
- **No taxable bridge.** Maxing only locked accounts leaves nothing accessible before 59Â½ without special maneuvers (see `fire-early-access-bridge.md`).
- **Using stale limits.** The figures change annually; re-verify the current-year numbers.

## References

- Bogleheads "Prioritizing investments"; the Mad Fientist on HSA-as-stealth-IRA and account sequencing; IRS contribution-limit notices and SECURE 2.0 Act provisions (2026 figures).
- Related: [fire-early-access-bridge.md](fire-early-access-bridge.md) (how the taxable/Roth space funds pre-59Â½), [fire-withdrawal-tax-optimization.md](fire-withdrawal-tax-optimization.md) (converting traditional later), [fire-healthcare-bridge-aca.md](fire-healthcare-bridge-aca.md) (HSA + the MAGI constraint on conversions). For tax lots use `tax-loss-harvesting`, `wash-sale-detection`, `kanchi-dividend-us-tax-accounting`; for the whole portfolio use the Sure skill `whole-wealth-audit`.
- All figures as of 2026 â€” verify current-year values; the IRS adjusts limits annually.
