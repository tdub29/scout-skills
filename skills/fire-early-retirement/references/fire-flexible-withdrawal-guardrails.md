# Flexible Withdrawal & Guardrails â€” Spend more by adjusting to the market

## The framework

> A **fixed** inflation-adjusted withdrawal (the 4%-rule style) ignores how the portfolio is actually doing. **Dynamic / flexible** withdrawal rules adjust spending up or down based on portfolio performance â€” and because they cut spending in bad years, they let you start at a **higher** withdrawal rate than a fixed rule.

The trade-off is explicit: **a higher sustainable starting rate (~5%+, up to ~5.7% in Morningstar's 2026 flexible case) in exchange for variable annual spending.** You give up a perfectly smooth, predictable income for a larger average withdrawal and a much lower chance of ruin. This is the single biggest lever for raising the safe rate (see `fire-safe-withdrawal-rate.md`) without changing the portfolio.

*(All figures as of 2026 â€” verify current-year values; flexible-withdrawal research is revised annually.)*

## Guyton-Klinger decision rules

Jonathan Guyton and William Klinger's "decision rules" are the canonical guardrail system. You set an **initial withdrawal rate**, then apply rules each year:

- **Withdrawal Rule (inflation adjustment):** normally raise the dollar withdrawal by inflation each year â€” *but* freeze it (skip the inflation raise) in any year the portfolio's total return was negative AND the current withdrawal rate is above the initial rate. (The "freeze rule.")
- **Capital Preservation guardrail (the lower rail):** if a market drop pushes your *current* withdrawal rate **more than 20% above** the initial rate, **cut** spending by 10%. (Current rate = this year's dollar withdrawal Ã· current portfolio value. A falling portfolio raises the current rate; if it breaches the +20% rail you trim.)
- **Prosperity guardrail (the upper rail):** if a strong market pushes your current withdrawal rate **more than 20% below** the initial rate, you may **raise** spending by 10%. (A rising portfolio lowers the current rate; if it breaches the âˆ’20% rail you get a raise.)

So with a 5% initial rate, the guardrails sit at roughly **6.0%** (capital-preservation, cut) and **4.0%** (prosperity, raise). The system is symmetric: you give back some spending after crashes and take more after booms, which is exactly what keeps a higher starting rate solvent. Empirically Guyton-Klinger supports initial rates well above the fixed-rule base case for the same success probability.

## Variable Percentage Withdrawal (VPW)

> **VPW:** withdraw a **percentage of the *current* balance** that *increases with age*, rather than a fixed real dollar amount.

- The withdrawal each year = current portfolio Ã— an age-based percentage (the percentage rises as remaining horizon shrinks, drawing the balance toward zero by end of plan).
- **Pro:** mathematically can never fully deplete the portfolio (you're always taking a fraction of what's left), and it self-adjusts to markets.
- **Con:** spending is highly variable â€” a big drawdown directly cuts the dollar amount that year, which can fall below a livable floor. VPW is usually paired with a spending floor (e.g., Social Security, a bond/cash buffer, or part-time income).

## The "ratchet"

> The **ratchet** raises your spending floor when the portfolio has grown substantially, and (in the spending-only version) never lowers it.

A common ratchet rule (Kitces): if the portfolio rises ~50% above its starting value, increase the inflation-adjusted withdrawal by ~10%, no more often than every few years. The ratchet captures upside (most retirees historically end with far more than they started) while keeping a stable floor â€” at the cost of not cutting in downturns, so it's less protective than Guyton-Klinger on the downside.

## CAPE-based rules

> Set the **initial** withdrawal rate as a function of market **valuation** â€” high CAPE (expensive market) â†’ lower starting rate; low CAPE â†’ higher starting rate.

A typical CAPE rule: withdrawal % = a constant + a multiplier Ã— (1 Ã· CAPE), i.e., the withdrawal rate scales with the earnings yield. This directly addresses the valuation-dependence noted in `fire-safe-withdrawal-rate.md` and the danger of retiring at a market peak (`fire-sequence-of-returns-risk.md`).

## How to apply

1. **Confirm the user can tolerate variable spending.** Flexible rules only work if discretionary spending can flex; a Lean-FIRE budget with no slack can't absorb a 10% cut (see `fire-number-and-variants.md`).
2. **Separate the floor from the flex.** Identify the non-negotiable spending floor (housing, food, insurance) and fund it conservatively; apply guardrails to the discretionary layer above it.
3. **Pick a system:** Guyton-Klinger for explicit symmetric guardrails; VPW for a never-deplete percentage approach (with a floor); the ratchet for upside capture with a stable floor; CAPE rules to set the *starting* rate by valuation.
4. **State the trade-off plainly:** higher sustainable rate (~5%+, up to ~5.7% flexible per Morningstar 2026) for variable annual income. Show the rough guardrail dollar bands so the user sees how big a cut a crash could force.
5. **Tie to sequence-of-returns mitigation** (`fire-sequence-of-returns-risk.md`) â€” flexible spending is itself one of the strongest sequence-risk defenses, because it stops you from selling a fixed amount into a crash.

## Common failure modes

- **Adopting a high flexible rate but having no flexibility.** If the entire budget is essential, you can't cut 10% after a crash, so the higher starting rate isn't actually safe.
- **Computing the current withdrawal rate wrong.** Guardrails compare the *current* rate (this year's withdrawal Ã· *current* balance) to the *initial* rate â€” not the initial rate to itself.
- **Forgetting the freeze rule.** Guyton-Klinger's no-inflation-raise-after-a-down-year is part of why it works; skipping it overstates safety.
- **VPW without a floor.** A pure percentage-of-balance rule can drop below a livable income in a deep drawdown.
- **Ratchet treated as fully protective.** The spending-only ratchet raises but doesn't cut, so it offers less downside protection than guardrails.
- **Ignoring taxes and the ACA cliff.** A "raise" year that pushes income over the 400% FPL line can cost more in lost ACA subsidies than the raise is worth â€” reconcile with `fire-healthcare-bridge-aca.md` and `fire-withdrawal-tax-optimization.md`.

## References

- Jonathan Guyton & William Klinger, "Decision Rules and Maximum Initial Withdrawal Rates" (2006); Bogleheads VPW methodology; Michael Kitces on the ratchet and CAPE-based rules; Morningstar, *The State of Retirement Income* (2026) for the ~5.7% flexible case.
- Related: [fire-safe-withdrawal-rate.md](fire-safe-withdrawal-rate.md) (the fixed-rule base this improves on), [fire-sequence-of-returns-risk.md](fire-sequence-of-returns-risk.md) (flexible spending as a sequence-risk defense), [fire-number-and-variants.md](fire-number-and-variants.md) (need for slack), [fire-healthcare-bridge-aca.md](fire-healthcare-bridge-aca.md) and [fire-withdrawal-tax-optimization.md](fire-withdrawal-tax-optimization.md) (income-spike constraints).
- All figures as of 2026 â€” verify current-year values; flexible-withdrawal research is revised annually.
