# Early-Access Bridge â€” Reaching retirement money before 59Â½ without the 10% penalty

## The framework

> Most tax-advantaged accounts impose a **10% early-withdrawal penalty** (on top of ordinary income tax) if you take money out before **age 59Â½**. An early retiree who stops working at, say, 45 needs a **bridge**: a way to fund 14+ years of spending without triggering that penalty.

There are four-plus mechanisms. A real plan usually **combines** them â€” a taxable account and Roth contributions cover the near years while a conversion ladder seasons for the later ones.

## The mechanisms

### 1. Roth conversion ladder
> Convert money from a **traditional IRA/401(k) to a Roth IRA**; each conversion **"seasons" for 5 tax years**, after which that converted **principal** can be withdrawn **penalty-free** (and tax-free, since the conversion was already taxed).

- You pay ordinary income tax on each conversion in the year you convert (this is the cost), then wait 5 tax years (the clock starts Jan 1 of the conversion year), after which the converted amount is reachable without the 10% penalty.
- Because each conversion has its own 5-year clock, you build a **ladder**: convert an amount every year, and each rung becomes available 5 years later, creating a rolling stream of penalty-free income.
- The catch: you need **5 years of spending from other sources** to live on while the first rungs season. That's where the taxable account and Roth contributions come in.
- Conversions are taxable income, so they raise MAGI â€” directly colliding with the ACA 400% FPL subsidy cliff (see `fire-healthcare-bridge-aca.md`) and best sized to fill low brackets (see `fire-withdrawal-tax-optimization.md`).

### 2. Rule 72(t) / SEPP (Substantially Equal Periodic Payments)
> Take a stream of **substantially equal periodic payments** from an IRA (or, in some cases, a former employer's 401(k)) under IRS Section 72(t), and the 10% penalty is waived â€” but the payments are **locked**.

- Three IRS-approved calculation methods: **Required Minimum Distribution (RMD) method**, **Fixed Amortization method**, and **Fixed Annuitization method**. The amortization and annuitization methods produce larger, level payments; the RMD method recalculates yearly and produces a variable (usually smaller) payment.
- **Lock-in:** once started, you must continue the SEPP unchanged until the **later of 5 years or reaching age 59Â½.** Breaking or modifying the schedule retroactively triggers the 10% penalty (plus interest) on all prior payments. This rigidity is the main drawback â€” it's hard to dial spending up or down, which conflicts with flexible withdrawal (`fire-flexible-withdrawal-guardrails.md`).
- Best for someone who wants a predictable penalty-free stream and doesn't have enough taxable/Roth runway for a conversion ladder.

### 3. Rule of 55
> If you **separate from your employer in or after the year you turn 55**, you can take penalty-free withdrawals **from that employer's 401(k)/403(b)** (not from IRAs, and not from prior employers' plans).

- Applies only to the plan at the job you left at 55+; rolling that 401(k) into an IRA forfeits the Rule-of-55 access. So if you might use it, **leave the money in the 401(k).**
- Useful for retirees leaving work between 55 and 59Â½ who want immediate access without a SEPP or a seasoned ladder.

### 4. Roth contributions (always withdrawable)
> Your **direct Roth IRA contributions** (not earnings, not converted amounts) can be withdrawn **anytime, tax- and penalty-free**, because you already paid tax on them.

- This is the most flexible bridge dollar available â€” no seasoning, no lock-in. It's a natural first source for the early years while the conversion ladder seasons.
- Note the ordering rules: contributions come out first, then conversions (oldest first, subject to their 5-year clocks), then earnings (which can be penalized before 59Â½).

### 5. Taxable brokerage bridge
> A regular **taxable brokerage account** has **no age restriction** â€” you can sell and spend anytime. You only owe capital-gains tax on the *gains*, often at favorable long-term rates (and potentially **0%** in low-income years; see `fire-withdrawal-tax-optimization.md`).

- This is usually the primary funding source for the first 5 years (the seasoning gap of the conversion ladder) and a flexible source throughout. Build it during accumulation (step 6 of `fire-accumulation-account-order.md`).

## Sequencing a bridge from FIRE age to 59Â½

A common early-retiree sequence (retire well before 55):

1. **Years 1â€“5:** live on the **taxable brokerage** + **Roth contributions** (both immediately accessible, low/no tax). Simultaneously, **start the Roth conversion ladder** in year 1 â€” convert an amount each year sized to fill low tax brackets without breaching the ACA MAGI ceiling.
2. **Years 6+:** the first conversion ladder rungs have now seasoned 5 years â†’ withdraw converted **principal** penalty-free; keep converting each year so the ladder keeps feeding itself.
3. **If you left work at 55+:** the **Rule of 55** can replace or supplement the above for that employer's 401(k).
4. **If you lack taxable/Roth runway:** a **72(t)/SEPP** can provide a penalty-free stream, accepting the lock-in.
5. **At 59Â½:** all the penalty restrictions fall away; you can draw from any account directly, and the bridge is no longer needed.

## How to apply

1. **Calculate the gap:** spending Ã— years from FIRE age to 59Â½ = total bridge funding needed.
2. **Inventory accessible sources first:** taxable brokerage balance + Roth contribution basis. These fund the near years with the least friction.
3. **Start the conversion ladder early** (year 1 of retirement) so rungs season in time, sizing conversions against both bracket-filling (`fire-withdrawal-tax-optimization.md`) and the ACA MAGI cliff (`fire-healthcare-bridge-aca.md`).
4. **Decide on Rule of 55 vs. rollover before leaving the job** â€” don't roll the 401(k) to an IRA if you'll want Rule-of-55 access.
5. **Use 72(t)/SEPP only if necessary**, and respect the until-59Â½-or-5-years lock-in; pick the calculation method that matches the income you need.
6. **Coordinate with healthcare and taxes:** every conversion and gain realization raises MAGI â€” reconcile the bridge against `fire-healthcare-bridge-aca.md` and `fire-withdrawal-tax-optimization.md` each year.

## Common failure modes

- **Starting the conversion ladder too late.** The 5-year seasoning means rungs converted in year 1 aren't usable until year 6 â€” you must have other money for the gap.
- **Rolling a Rule-of-55 401(k) into an IRA.** That forfeits penalty-free access from that plan; leave it in the 401(k) if you want the option.
- **Breaking a 72(t)/SEPP.** Modifying the schedule before the 5-year/59Â½ mark retroactively applies the 10% penalty plus interest to all payments.
- **Withdrawing Roth *earnings* (not contributions) early.** Contributions are free; earnings can be taxed and penalized before 59Â½ and before the account's own 5-year rule is met.
- **Ignoring MAGI when converting.** A large conversion can blow past the 400% FPL line and cost the entire ACA subsidy that year (see `fire-healthcare-bridge-aca.md`).
- **Confusing the 5-year conversion clock with the 5-year Roth-account clock.** They're distinct rules; both can apply.

## References

- IRS Section 72(t) (SEPP) and the three approved calculation methods; the Rule of 55; Roth IRA ordering rules; the Mad Fientist's "Roth IRA Conversion Ladder" writing.
- Related: [fire-accumulation-account-order.md](fire-accumulation-account-order.md) (building the taxable/Roth space that funds the bridge), [fire-withdrawal-tax-optimization.md](fire-withdrawal-tax-optimization.md) (sizing conversions to fill brackets), [fire-healthcare-bridge-aca.md](fire-healthcare-bridge-aca.md) (the MAGI ceiling that caps conversions), [fire-flexible-withdrawal-guardrails.md](fire-flexible-withdrawal-guardrails.md) (why SEPP's rigidity is a drawback).
- All rules and ages as of 2026 â€” verify current-year values and IRS guidance before acting.
