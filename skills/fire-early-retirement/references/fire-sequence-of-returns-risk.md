# Sequence-of-Returns Risk â€” Why the first decade of retirement decides everything

## The framework

> **Sequence-of-returns risk** is the danger that *poor returns early in retirement* â€” while you're withdrawing â€” permanently damage a portfolio, even if average returns over the full retirement are fine.

During accumulation, the *order* of returns doesn't matter: a dollar invested compounds the same regardless of which years were good or bad, because you're not selling. During *withdrawal*, order matters enormously. Pulling a fixed amount during an early drawdown forces you to **sell more shares at low prices**, shrinking the share count that needs to recover. The portfolio can be so depleted by the time the market rebounds that it never catches up.

This is why **the first ~5â€“10 years of withdrawals dominate a long retirement's survival.** Two retirees with identical *average* returns over 30 years can have opposite outcomes: the one who hit a crash in years 1â€“5 may run out, while the one who hit the same crash in years 25â€“30 dies with a surplus. The safe withdrawal rate (`fire-safe-withdrawal-rate.md`) is essentially calibrated to survive the worst early sequences in the historical record â€” and for FIRE's 40â€“60 year horizons, there are more early years exposed and more time for damage to compound.

**"Retiring into a crash"** is the worst case: you stop contributing, start withdrawing, and the market drops 30â€“50% in your first year or two. The combination of no new contributions, forced selling at lows, and a long remaining horizon is what sequence risk is really about.

## Mitigations

### 1. Rising-equity glidepath / bond tent
> Hold a **higher bond (lower equity) allocation right around the retirement date**, then **increase equity exposure over the first decade** of retirement.

Plotted over time the bond allocation looks like a **tent** â€” it peaks at retirement and tapers down afterward. The logic: the danger window is the first 5â€“10 years (when sequence risk is highest), so you carry more bonds *then* to avoid selling stocks into an early crash, and you let equities drift back up once the danger window has passed. Counterintuitively, this means getting *more* aggressive as you age through early retirement â€” the opposite of the traditional "glide down to bonds" advice â€” because the sequence-risk window is front-loaded.

### 2. Cash buffer (1â€“3 years of spending)
> Keep **1â€“3 years of living expenses in cash or short-term instruments** so you can fund spending from cash during a downturn instead of selling equities at a loss.

When the market is down, you draw from the buffer and let the equity portion recover; you refill the buffer in up years. This directly breaks the "sell low" mechanism that drives sequence risk. The cost is cash drag (lower expected return on the buffer), so keep it sized to the danger window, not the whole retirement.

### 3. Flexible spending
> **Cut spending in down years.** Variable withdrawal (Guyton-Klinger guardrails, VPW â€” see `fire-flexible-withdrawal-guardrails.md`) reduces the dollar amount you pull during a drawdown, which is the single most effective sequence-risk defense.

Because flexible spending takes out less when prices are low, it preserves shares for the recovery â€” the mirror image of what sinks fixed-withdrawal retirees. This ties directly to keeping discretionary slack in the budget (`fire-number-and-variants.md`).

### 4. Part-time income in the early years
> Earning even modest income in the first few years (Barista-style; see `fire-number-and-variants.md`) reduces or eliminates withdrawals during the danger window, letting the portfolio ride out an early downturn untouched.

### 5. Avoid selling equities in a drawdown
The unifying principle behind all of the above: **do not be a forced seller of stocks during the early-retirement danger window.** The glidepath/bond tent, cash buffer, flexible spending, and part-time income are four different ways to avoid that single failure mode.

## How to apply

1. **Identify the danger window.** It's roughly the first 5â€“10 years post-retirement and, critically, *valuation at the start* â€” retiring at a high CAPE (expensive market) raises the risk (see `fire-safe-withdrawal-rate.md`).
2. **Layer mitigations, don't pick just one.** A typical robust plan combines a bond tent *into* the retirement date, a 1â€“3 year cash buffer, and flexible spending rules. Part-time income further de-risks the first years.
3. **Size the cash buffer to the window, not the whole plan.** 1â€“3 years balances protection against cash drag.
4. **Plan to taper equity back up** over the first decade if using a rising-equity glidepath, and define the refill rule for the cash buffer.
5. **Connect to withdrawal strategy.** Flexible/guardrail withdrawal (`fire-flexible-withdrawal-guardrails.md`) is both a way to raise the safe rate *and* a sequence-risk defense â€” treat them as the same lever.
6. For whether the portfolio's actual risk metrics (drawdown, volatility) support the plan, cross-reference the Sure skill `risk-metrics-calculation` â€” do not modify it.

## Common failure modes

- **Assuming average returns are enough.** A perfectly fine *average* return can still ruin a retirement if the bad years land first.
- **Holding a fixed real withdrawal through a crash.** Selling the same dollar amount at low prices is exactly the behavior sequence risk punishes.
- **Over-sizing the cash buffer.** Holding 5+ years in cash creates large drag that itself reduces sustainability over a 40â€“60 year horizon.
- **Gliding *down* to bonds at retirement and staying there.** A static high-bond allocation forever sacrifices the growth a long horizon needs; the bond tent is meant to *taper back up*.
- **Ignoring starting valuation.** Treating a high-CAPE retirement date the same as a cheap one understates the early-sequence danger.
- **No flexibility in the budget.** If spending can't flex, the strongest sequence defense (cutting in down years) is unavailable.

## References

- Michael Kitces & Wade Pfau on rising-equity glidepaths and the "bond tent"; the broad sequence-of-returns literature underlying the Trinity/Bengen SWR results.
- Related: [fire-safe-withdrawal-rate.md](fire-safe-withdrawal-rate.md) (the SWR is calibrated to survive bad sequences), [fire-flexible-withdrawal-guardrails.md](fire-flexible-withdrawal-guardrails.md) (flexible spending as the top defense), [fire-number-and-variants.md](fire-number-and-variants.md) (slack and Barista income). For portfolio risk metrics use the Sure skill `risk-metrics-calculation`.
- Figures and rules as of 2026 â€” verify current-year values.
