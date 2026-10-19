# Withdrawal Tax Optimization â€” Exploiting low-income early-retirement years

## The framework

> The years between leaving work and starting Social Security / RMDs are often a **low-taxable-income window.** That window is a once-in-a-lifetime opportunity to move money out of tax-deferred accounts and realize gains **at very low or zero tax rates** â€” but it collides with the ACA MAGI cliff and, eventually, with RMDs.

Two complementary tools dominate decumulation tax strategy in this window: **Roth conversions that fill up low tax brackets**, and **0% long-term capital-gains harvesting.** Both work because your *other* income is low after you stop earning a salary.

*(All figures, brackets, and thresholds as of 2026 â€” verify current-year values; the IRS adjusts brackets, the standard deduction, and the 0% LTCG ceiling annually.)*

## Roth conversions filling low brackets

> In a low-income year, **convert just enough traditional â†’ Roth to "fill up" the low tax brackets** without spilling into a higher one.

- You voluntarily realize ordinary income by converting, paying tax now at a low marginal rate, in exchange for tax-free growth and no future RMDs on that money.
- The point is **bracket arbitrage:** if you were in a high bracket while working and your early-retirement bracket is low, converting now at the low rate beats withdrawing later at a higher rate (or being forced out by RMDs).
- **Standard-deduction interaction:** the first slice of income is sheltered by the standard deduction, so a portion of each conversion is effectively tax-free before the brackets even start. Always fill the standard deduction first.
- This is the same engine as the **Roth conversion ladder** bridge (see `fire-early-access-bridge.md`) â€” here the focus is *sizing* the conversion to the bracket rather than the 5-year seasoning.

## 0% long-term capital-gains harvesting

> When your taxable income is low enough, **long-term capital gains are taxed at 0%** up to a ceiling. **Realize gains on purpose** in those years â€” sell appreciated lots and immediately rebuy â€” to **reset your cost basis higher at no tax cost.**

- Selling and rebuying steps up your basis for free (there's **no wash-sale rule on gains** â€” wash-sale rules only apply to *losses*; cross-reference `wash-sale-detection`). Future sales then have smaller taxable gains.
- The 0% bracket is stacked *on top of* ordinary income, so ordinary income (including Roth conversions) "uses up" the room first â€” which is exactly why conversions and gain-harvesting compete for the same low-income space.

## The competition between the two (and with ACA)

Roth conversions are **ordinary income** and capital-gain harvesting needs **room in the 0% LTCG band** â€” and both raise **MAGI**, which can breach the **400% FPL ACA subsidy cliff** (see `fire-healthcare-bridge-aca.md`). In any given year you are juggling three ceilings that draw on the same income headroom:

1. The top of the low ordinary bracket you want conversions to fill.
2. The top of the 0% LTCG band you want gains to fill.
3. The 400% FPL MAGI line you may want to stay under to keep ACA subsidies.

You usually **cannot max all three in the same year.** Plan a multi-year calendar: some years emphasize conversions, some emphasize gain-harvesting, some stay low to grab ACA subsidies.

## Withdrawal sequencing

The classic default order for *which account to spend from*:

> **Taxable first â†’ tax-deferred (traditional) next â†’ Roth last.**

- Spending **taxable** first lets tax-deferred and Roth keep compounding and gives you control over realized gains (harvest at 0% when possible).
- **Roth last** because it grows tax-free and has no RMDs â€” it's the most valuable space to preserve, and a flexible reserve for years you must avoid raising MAGI.
- **The refinement â€” bracket filling / blended sequencing:** rather than purely emptying one account before the next, *blend* â€” each year pull from taxable for cash flow **and** convert/withdraw enough traditional to fill low brackets. Pure "taxable-first" can leave the traditional balance so large that later RMDs force high-bracket withdrawals. Proactive conversions in the low-income window defuse that future **RMD** problem (RMDs begin at the statutory age and force taxable withdrawals whether you need the money or not).

## How to apply

1. **Map the low-income window** â€” from FIRE age until Social Security and RMDs begin. This is the optimization zone.
2. **Fill the standard deduction first**, then decide how much room to allocate between Roth conversions (ordinary bracket) and 0% LTCG harvesting (capital-gains band).
3. **Subtract the ACA constraint.** If you want subsidies that year, the 400% FPL MAGI line caps total income â€” reconcile against `fire-healthcare-bridge-aca.md` before sizing conversions or gains.
4. **Sequence withdrawals taxable â†’ tax-deferred â†’ Roth**, but **blend in bracket-filling conversions** every year to shrink the future traditional balance and the RMD that follows.
5. **Plan multi-year, not single-year.** Alternate emphasis (conversion-heavy years vs. subsidy-preserving low-MAGI years) to optimize across the whole window.
6. **Use the tax-lot skills for execution:** `tax-loss-harvesting` for realizing losses, `wash-sale-detection` to avoid disallowed losses (and note gains aren't subject to wash-sale), and `kanchi-dividend-us-tax-accounting` for dividend/lot accounting â€” cross-reference, do not modify them.

## Common failure modes

- **Leaving the standard deduction and low brackets unused.** Every low-income year of unused bracket space is a permanent lost chance to convert/harvest cheaply.
- **Maxing conversions without checking the ACA cliff.** A bracket-filling conversion can cost more in lost ACA subsidies than it saves in tax (see `fire-healthcare-bridge-aca.md`).
- **Forgetting conversions consume the 0% LTCG room.** Ordinary income (including conversions) stacks under capital gains; a big conversion can push your gains out of the 0% band.
- **Pure taxable-first sequencing.** Emptying taxable while never touching traditional lets the tax-deferred balance balloon, producing large forced RMDs at high rates later.
- **Triggering a wash sale on a *loss* while harvesting.** Wash-sale rules disallow the loss if you rebuy within 30 days; they do *not* apply to gain-harvesting â€” keep the two straight (`wash-sale-detection`).
- **Using stale brackets / 0% LTCG ceiling.** These adjust annually; re-verify the current-year figures.

## References

- IRS ordinary-income brackets, the standard deduction, the 0% long-term capital-gains rate band, and RMD rules (2026 figures); the FIRE-community decumulation literature on Roth conversions and gain-harvesting in low-income years.
- Related: [fire-healthcare-bridge-aca.md](fire-healthcare-bridge-aca.md) (the MAGI cliff that constrains all of this), [fire-early-access-bridge.md](fire-early-access-bridge.md) (the conversion-ladder mechanics), [fire-accumulation-account-order.md](fire-accumulation-account-order.md) (the Roth-vs-traditional setup that creates the conversion opportunity). For execution: `tax-loss-harvesting`, `wash-sale-detection`, `kanchi-dividend-us-tax-accounting` (cross-referenced, not modified).
- All figures and brackets as of 2026 â€” verify current-year values; the IRS adjusts them annually.
