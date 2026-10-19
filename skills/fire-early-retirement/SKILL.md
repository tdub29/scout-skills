---
name: fire-early-retirement
description: Router hub for FIRE (Financial Independence / Retire Early) planning â€” a synthesized, US-centric methodology (NOT from a single book) covering the FIRE number and variants (Lean/Fat/Coast/Barista/Flamingo FIRE, 25x rule), the savings-rate-to-timeline math ("shockingly simple math"), safe withdrawal rate (Bengen 4% â†’ 4.7%, Trinity study, Morningstar 2026 ~3.9%, long-horizon ~3.25â€“3.5%), flexible/guardrail withdrawal (Guyton-Klinger, VPW, CAPE rules), sequence-of-returns risk and mitigations (bond tent / rising-equity glidepath, cash buffer), the tax-advantaged accumulation account order (401(k) match â†’ HSA â†’ IRA â†’ max 401(k) â†’ mega-backdoor Roth â†’ taxable), pre-59Â½ early-access bridges (Roth conversion ladder, Rule 72(t)/SEPP, Rule of 55, taxable brokerage), the pre-65 healthcare/ACA bridge with MAGI management (the 400% FPL subsidy cliff returned Jan 1 2026), and decumulation tax optimization (Roth conversions filling low brackets, 0% LTCG harvesting, withdrawal sequencing). Use when the user asks about FIRE, financial independence, retire early, "how much do I need to retire," "when can I retire," FIRE number, 25x rule, 4% rule, safe withdrawal rate, Coast/Barista/Lean/Fat FIRE, savings rate, Roth conversion ladder, 72(t)/SEPP, Rule of 55, sequence of returns risk, bond tent, ACA subsidy / healthcare before 65, or early-retirement withdrawal/tax strategy. GUARDRAILS: this is an educational planning framework, US-centric, NOT personalized financial/tax/legal/investment advice â€” recommend verifying current-year limits and consulting a fiduciary/CPA; all figures are as of 2026 and change annually (tell the reader to check the current year). For the PSYCHOLOGY of the retire/keep-working decision, the one-more-year trap, and spending behavior hand off to `behavioral-economics`, `difficult-conversation`, and `marketing-psychology`; for portfolio allocation/health checks cross-reference the Sure skills `whole-wealth-audit` and `risk-metrics-calculation`; for tax-lot mechanics cross-reference `tax-loss-harvesting`, `wash-sale-detection`, and `kanchi-dividend-us-tax-accounting` â€” do NOT modify any of them. Load the matching references/<name>.md file and apply that framework exactly.
---

# fire-early-retirement

This hub collapses a synthesized FIRE / early-retirement methodology into one router plus references. Route by user cue, read the referenced file(s) in full, and apply that framework exactly â€” including its figures (all as-of-2026), its math, and its guardrails.

This is a **synthesized methodology hub, not a single book** â€” it draws on the FIRE community canon (Bengen's safe-withdrawal research and the Trinity study, Mr. Money Mustache's savings-rate math, the Bogleheads/Mad Fientist account-order and bridge strategies, Guyton-Klinger flexible withdrawal, and Morningstar's annual *State of Retirement Income* updates).

## When to use

Use this hub when the user wants to:

- Compute a **FIRE number** ("how much do I need to retire," "when can I retire") and pick the variant (Lean/Fat/Coast/Barista/Flamingo) that fits.
- Translate a **savings rate** into a years-to-financial-independence timeline.
- Choose a **safe withdrawal rate** for a long (40â€“60 year) early-retirement horizon, or layer on a **flexible/guardrail** strategy to raise it.
- Defend against **sequence-of-returns risk** â€” "retiring into a crash," bond tents, cash buffers.
- Order **accumulation** contributions across tax-advantaged accounts using current-year limits.
- Build a **pre-59Â½ bridge** to reach tax-deferred money without the 10% penalty (Roth conversion ladder, 72(t)/SEPP, Rule of 55, taxable brokerage).
- Solve the **pre-65 healthcare gap** with ACA coverage and MAGI management (the 400% FPL subsidy cliff returned in 2026).
- **Tax-optimize decumulation** â€” Roth conversions filling low brackets, 0% capital-gains harvesting, withdrawal sequencing.

## Guardrails

- **Educational planning framework, US-centric â€” not advice.** This hub does not give personalized financial, tax, legal, or investment advice. Always recommend the user verify current-year limits/rules and consult a fiduciary advisor and/or CPA for personal decisions.
- **Every figure is as of 2026 and changes annually.** Contribution limits, the FPL thresholds, ACA rules, and SWR base cases all move year to year. Each reference that cites a number says "as of 2026 â€” verify current-year values"; carry that caveat into any answer.
- Do **not** answer from router memory alone; load the selected reference file(s) before applying a framework. Do not invent numbers â€” use the figures in the references verbatim and flag them as as-of-2026.
- **Hand off the psychology.** For the emotional retire/keep-working decision, the one-more-year trap, lifestyle-inflation behavior, and spending psychology, route to `behavioral-economics`, `difficult-conversation`, and `marketing-psychology` (a partner conversation about retiring lives in `difficult-conversation`). Do not modify those hubs.
- **Cross-reference, don't duplicate.** For portfolio allocation and a holistic financial health check use the Sure skills `whole-wealth-audit` and `risk-metrics-calculation`; for tax-lot mechanics use `tax-loss-harvesting`, `wash-sale-detection`, and `kanchi-dividend-us-tax-accounting`. Reference them via code-spans; never edit them.
- The two big constraints interact: a year spent **under the 400% FPL ceiling** for ACA subsidies (ref #8) directly conflicts with **large Roth conversions or gain-harvesting** (ref #9) in that same year. Always check both before recommending either.

## Quick routing table

| User cue (examples) | Route to reference |
|---|---|
| "how much do I need to retire," FIRE number, 25x rule, expenses Ã· SWR, Lean/Fat/Coast/Barista/Flamingo FIRE, which variant fits | `references/fire-number-and-variants.md` |
| savings rate, "when can I retire," years-to-FI, shockingly simple math, how saving more shortens the timeline two ways | `references/fire-savings-rate-timeline.md` |
| 4% rule, safe withdrawal rate, Trinity study, Bengen, Morningstar base case, why a 40â€“60yr horizon needs a lower rate, CAPE | `references/fire-safe-withdrawal-rate.md` |
| dynamic/flexible withdrawal, Guyton-Klinger guardrails, VPW, the ratchet, "can I spend more if I'm flexible," CAPE-based rules | `references/fire-flexible-withdrawal-guardrails.md` |
| sequence of returns risk, retiring into a crash, bond tent, rising-equity glidepath, cash buffer, why the first 5â€“10 years matter most | `references/fire-sequence-of-returns-risk.md` |
| where to put savings, investment order, 401(k) match vs HSA vs IRA vs Roth, mega-backdoor Roth, Roth-vs-traditional, 2026 limits | `references/fire-accumulation-account-order.md` |
| accessing retirement money before 59Â½, 10% penalty, Roth conversion ladder, 72(t)/SEPP, Rule of 55, sequencing the bridge | `references/fire-early-access-bridge.md` |
| health insurance before 65 / before Medicare, ACA marketplace, premium tax credits, MAGI management, 400% FPL cliff, COBRA | `references/fire-healthcare-bridge-aca.md` |
| decumulation tax strategy, Roth conversions in low-income years, 0% LTCG harvesting, withdrawal order, bracket filling, RMD concerns | `references/fire-withdrawal-tax-optimization.md` |

## Workflow

Run the numbers as a pass, in this order â€” each step feeds the next:

1. **Compute the FIRE number.** Annual expenses Ã· safe withdrawal rate. Pick the variant that fits the user's life (Lean/Fat/Coast/Barista/Flamingo). â†’ `references/fire-number-and-variants.md`
2. **Check the savings rate and years-to-FI.** Convert the user's savings rate into a timeline; note that cutting spending shortens it on both ends. â†’ `references/fire-savings-rate-timeline.md`
3. **Choose the SWR and withdrawal strategy.** Set a base rate for the long horizon (`references/fire-safe-withdrawal-rate.md`); decide whether to layer on flexible/guardrail spending to lift it (`references/fire-flexible-withdrawal-guardrails.md`).
4. **Assess sequence-of-returns risk** and pick mitigations (glidepath/bond tent, cash buffer, flexible spending). â†’ `references/fire-sequence-of-returns-risk.md`
5. **Plan the pre-59Â½ bridge** so money is reachable without the 10% penalty. â†’ `references/fire-early-access-bridge.md`
6. **Plan the pre-65 healthcare / MAGI bridge** for the coverage gap before Medicare. â†’ `references/fire-healthcare-bridge-aca.md`
7. **Tax-optimize decumulation** across the low-income early-retirement years â€” but reconcile it against the ACA MAGI ceiling from step 6. â†’ `references/fire-withdrawal-tax-optimization.md`

If the user asks a single targeted question, jump straight to the matching row in the routing table and read that reference in full before answering.

## References

- [references/fire-number-and-variants.md](references/fire-number-and-variants.md)
- [references/fire-savings-rate-timeline.md](references/fire-savings-rate-timeline.md)
- [references/fire-safe-withdrawal-rate.md](references/fire-safe-withdrawal-rate.md)
- [references/fire-flexible-withdrawal-guardrails.md](references/fire-flexible-withdrawal-guardrails.md)
- [references/fire-sequence-of-returns-risk.md](references/fire-sequence-of-returns-risk.md)
- [references/fire-accumulation-account-order.md](references/fire-accumulation-account-order.md)
- [references/fire-early-access-bridge.md](references/fire-early-access-bridge.md)
- [references/fire-healthcare-bridge-aca.md](references/fire-healthcare-bridge-aca.md)
- [references/fire-withdrawal-tax-optimization.md](references/fire-withdrawal-tax-optimization.md)

## Basis / provenance

Synthesized methodology hub (not a single book). Draws on: William Bengen's 1994 safe-withdrawal research and the Trinity study lineage; Morningstar's *State of Retirement Income* (2026 edition) for the current base-case withdrawal rate; Mr. Money Mustache's "shockingly simple math of early retirement" for the savings-rate-to-timeline relationship; the Bogleheads investment-order and the Mad Fientist's Roth-conversion-ladder / 72(t) bridge writing; Jonathan Guyton & William Klinger's decision-rule (guardrail) withdrawal research; and the Kitces body of work on rising-equity glidepaths and sequence-of-returns risk. All figures are as of 2026 and must be re-verified against current-year IRS limits, Federal Poverty Level tables, and ACA rules.
