# Safe Withdrawal Rate â€” How much you can pull, and why early retirees need less

## The framework

> The **safe withdrawal rate (SWR)** is the percentage of your starting portfolio you withdraw in year one and then keep withdrawing, **adjusted upward for inflation each year**, with a high probability of not running out over your retirement horizon.

The SWR is the multiplier behind the FIRE number (expenses Ã· SWR; see `fire-number-and-variants.md`). It is not a return assumption â€” it's a *spending* rule designed to survive bad return sequences, not just average returns.

### The lineage of the 4% rule

- **Bengen (1994):** William Bengen tested historical 30-year retirement windows (US data) and found that a portfolio of **50â€“75% stocks** with the rest in bonds could sustain an **initial 4% withdrawal, then inflation-adjusted each year**, through even the worst starting years (e.g., retiring just before the 1929, 1937, or 1973â€“74 downturns). 4% was the **worst-case** survivable rate for a **30-year** horizon â€” not the typical or expected one. In most historical periods the retiree died with more money than they started with.
- **Trinity study (1998):** Three Trinity University professors confirmed and popularized Bengen's result using success-probability framing across stock/bond mixes and horizons â€” this is where "the 4% rule" got its name.
- **Bengen's later revision:** Bengen subsequently raised his own recommended maximum to about **4.7%** after adding **small-cap value** to the asset mix, which improved historical survivability.

### Where the base case sits in 2026

- **Morningstar, *State of Retirement Income* (2026):** puts the **fixed (constant, inflation-adjusted) withdrawal** base case at **3.9%** for a 30-year horizon at a 90% success rate â€” **up from 3.7% the prior year** (the increase reflects higher bond yields and revised return forecasts).
- With **flexible / guardrail spending** (adjusting withdrawals to market conditions rather than holding a fixed real amount), Morningstar finds a starting rate as high as **~5.7%** can be sustainable â€” the cost being variable annual spending. See `fire-flexible-withdrawal-guardrails.md`.

*(All figures as of 2026 â€” verify current-year values; Morningstar revises this annually and the base case has moved in recent years.)*

### The key early-retirement caveat â€” horizon

The 4% rule, the Trinity study, and the Morningstar base case were all built for a **30-year** retirement. **FIRE horizons are 40â€“60 years.** Over a longer horizon:

- There are **more years for a bad sequence to compound** and for inflation to erode purchasing power.
- The same starting rate has a **lower success probability** â€” a rate that's "safe" for 30 years can fail over 50.

So the FIRE community commonly uses a more conservative **~3.25â€“3.5% SWR** (â‰ˆ **28â€“31Ã— expenses**) for very long retirements. Put plainly: **the 4% rule understates longevity risk and sequence risk for very long retirements.** A 4% rate that worked historically for a 65-year-old may be too aggressive for a 40-year-old.

### Why sequence and inflation matter more than average return

Two retirees with identical *average* returns can have opposite outcomes if one suffers poor returns early. Withdrawing a fixed real amount during an early drawdown sells more shares at low prices, permanently shrinking the base â€” this is **sequence-of-returns risk**, covered in depth in `fire-sequence-of-returns-risk.md`. The SWR is essentially priced to survive the worst sequences in the historical record.

### CAPE sensitivity (brief)

Safe rates are **valuation-dependent**. When equities are expensive â€” a high **CAPE** (cyclically adjusted price-to-earnings, the Shiller P/E) â€” forward returns have historically been lower and the safe starting rate is lower; when valuations are cheap, a higher starting rate has been safe. This is why some practitioners use **CAPE-based withdrawal rules** that set the initial rate as a function of current valuation (see `fire-flexible-withdrawal-guardrails.md`). Retiring at a market peak (high CAPE) argues for the conservative end of the range.

## How to apply

1. **Start from the horizon.** For a 40â€“60 year early retirement, anchor on **3.25â€“3.5%** as the conservative base, not 4%. Reserve 4%/4.7% framing for ~30-year horizons.
2. **State the assumptions out loud:** stock/bond mix (50â€“75% equities historically), inflation-adjusted withdrawals, and the success probability you're targeting (e.g., 90%).
3. **Offer the flexibility upgrade.** If the user can tolerate variable spending, point to `fire-flexible-withdrawal-guardrails.md`, where dynamic rules push the sustainable starting rate higher (~5%+ in some studies, ~5.7% in Morningstar's flexible case).
4. **Check valuation.** If equities are expensive (high CAPE) or the user is retiring into a hot market, lean conservative and flag sequence risk (`fire-sequence-of-returns-risk.md`).
5. **Convert to the FIRE number** with `fire-number-and-variants.md`: number = expenses Ã· SWR.
6. For the underlying portfolio's risk profile and whether the allocation supports the chosen SWR, cross-reference the Sure skills `risk-metrics-calculation` and `whole-wealth-audit` â€” do not modify them.

## Common failure modes

- **Treating 4% as a law for all horizons.** It was a 30-year worst case; for 50 years it's optimistic. Use ~3.25â€“3.5% for long FIRE horizons.
- **Confusing SWR with expected return.** The SWR is below the expected return precisely to survive bad sequences and inflation; "the market returns 7% so I can withdraw 7%" is the classic ruin error.
- **Forgetting the inflation adjustment.** A "4% withdrawal" means 4% of the *starting* balance, then raised for inflation annually â€” not 4% of the current balance each year (that's a different, variable rule).
- **Ignoring valuation at the start.** Retiring at a high CAPE lowers the safe starting rate; using the historical worst case from a *cheap* market overstates safety.
- **Quoting a single number as certainty.** SWR is probabilistic; always frame it as a success probability over a horizon, not a guarantee.
- **Using a stale base case.** Morningstar's number moves yearly (3.7% â†’ 3.9%); re-verify the current-year figure.

## References

- William Bengen, "Determining Withdrawal Rates Using Historical Data" (1994); Cooley, Hubbard & Walz, the "Trinity study" (1998); Bengen's later ~4.7% revision with small-cap value; Morningstar, *The State of Retirement Income* (2026 edition).
- Related: [fire-number-and-variants.md](fire-number-and-variants.md) (SWR sets the multiple), [fire-flexible-withdrawal-guardrails.md](fire-flexible-withdrawal-guardrails.md) (dynamic rules raise the safe rate), [fire-sequence-of-returns-risk.md](fire-sequence-of-returns-risk.md) (the risk SWR is priced to survive). For portfolio risk use the Sure skills `risk-metrics-calculation` and `whole-wealth-audit`.
- All figures as of 2026 â€” verify current-year values; the base case is revised annually.
