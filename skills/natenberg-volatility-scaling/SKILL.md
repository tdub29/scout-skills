---
name: natenberg-volatility-scaling
description: Convert an annual volatility into the daily and weekly price moves it actually predicts (divide by 16 for daily, by 7.2 for weekly), then use observed settlement-to-settlement changes to audit whether the volatility input is right. That audit is the only feedback loop available, since volatility is never posted. Includes the one-in-three / one-in-twenty frequency test and the indexed-from-100 transformation that stops interest-rate products (Eurodollars, T-Bills, Short Sterling) from producing absurd answers. Use when asked "what daily move does X% vol imply," "is my vol assumption right," "convert annual vol to daily," "how big a move should I expect today," "why does my vol calc blow up on Eurodollar options," or "how do I sanity-check implied vol against what the market is doing." From Sheldon Natenberg, Option Volatility and Pricing, Chapter 4.
---

# Natenberg Volatility Scaling

## What this decides

Whether the volatility number you are feeding a pricing model is consistent with
what the market is actually doing. Volatility is **the one input into a
theoretical pricing model that cannot be directly observed**. A directional bet
has its success visible in posted prices, but **there is no posting of
volatilities.** You have to audit it yourself. This is how.

## The scaling rule

Scale an annual volatility to a shorter period by **dividing by the square root
of the number of those periods in a year.**

- **Daily.** Only trading days count, which leaves about **256** per year.
  Natenberg uses 256 rather than the true 250-255 precisely because its square
  root is a whole number: **16**. So
  **one standard deviation daily move â‰ˆ (annual vol / 16) Ã— price.**
- **Weekly.** There are no holiday *weeks*, so use all **52**. sqrt(52) â‰ˆ 7.2, so
  **one standard deviation weekly move â‰ˆ (annual vol / 7.2) Ã— price.**

Worked: underlying at 40, volatility 30%.
One-SD daily move = 30%/16 Ã— 40 = **0.75**.

## The frequency test (this is the actual audit)

A one-standard-deviation move is not a limit, it is a frequency claim. Under the
normal approximation:

| Move size | Expected frequency |
|---|---|
| â‰¤ 1 SD | about **2 trading days out of every 3** |
| > 1 SD | about **1 day in 3** |
| â‰¤ 2 SD | about **19 days out of 20** |
| > 2 SD | about **1 day in 20** |

So the audit is: compute the one-SD daily move, then count how often the actual
**settlement-to-settlement** changes exceed it. (Settlement to settlement is the
measurement, not high/low or open/close, which may be larger or smaller.)

### Worked example 1: volatility too high

Underlying at 40, assumed vol 30%, one-SD daily = 0.75. Five days of changes:

```
+0.43, -0.06, -0.61, +0.50, -0.28
```

Expected: a move bigger than 0.75 on roughly one day in three, so **once or twice
in five days**. Observed: **not once.** These five changes are *not* consistent
with 30% volatility. (The volatility actually implied by them is about **18.8%**.)

### Worked example 2: volatility too low

Underlying at 332 1/2, assumed vol 18%, one-SD daily = 18%/16 Ã— 332.5 â‰ˆ **3 3/4**.
Observed changes include -5, +2 1/2, -7 3/4, -4 1/4.

Expected: exceed 3 3/4 once or twice in five days. Observed: **three days out of
five**, and one move of 7 3/4, more than two standard deviations, which should
appear about **one day in twenty**.

## The judgment call, stated honestly

When observed moves contradict the input, there are exactly two readings:

1. **This was an unusual period** (a holiday week, a lull) and normal behavior
   will resume. Keep the volatility input.
2. **The input is simply wrong.** Change it to match the observed changes.

Choosing (1) with no specific reason is the failure mode. Continuing to use 30%
in the face of persistently smaller moves means **assigning the wrong
probabilities to the possible price outcomes**, which generates incorrect
theoretical values and defeats the entire purpose of using a pricing model.

Five days is admittedly a very small sample. The method and the reasoning still
hold; just do not over-conclude from one week.

## Interest rate products: the indexed-from-100 transformation

Apply the naive rule to Eurodollars at 93.00 with 16% volatility and you get
16%/16 Ã— 93.00 = **0.93** as a one-SD daily move, which any Eurodollar trader
knows is wildly impossible. The 16% is not wrong; the *price* is.

Eurodollars, T-Bills, Short Sterling, Euromarks and Euroyen are **indexed from
100**: the interest rate is 100 minus the contract value, so barring negative
rates the contract cannot exceed 100. That makes **100 a limiting value in
exactly the way zero is for a stock.**

The fix, which a correctly configured model does automatically:

1. **Use 100 minus the listed price** as the contract value. At 93.00, evaluate
   with **7.00**. One-SD daily move = 16%/16 Ã— 7.00 = **0.07**. Realistic.
2. **Index the exercise price from 100 too.** A 93.50 strike is really 6.50.
3. **Flip the option type: calls become puts and puts become calls.** A 93.50
   call needs the contract above 93.50, which requires rates *below* 6.50, so a
   93.50 call in listed terms is a **6.50 put** in rate terms.

**This transformation is NOT needed for most bonds and notes.** Depending on the
coupon, their prices range freely and often exceed 100, so a traditional model
applies (though rate products raise other issues that may need specialized
models).

**Yield volatility versus price volatility.** For a bond you can compute
volatility from the price series or from the derived yield series. They are
different numbers. If you use yield volatility, you must also specify the
exercise price in yield terms. Interest-rate traders name the distinction
explicitly; carry it through consistently or the model is inconsistent with
itself.

## Working checklist

```
[ ] one-SD daily = (annual vol / 16) x price
[ ] one-SD weekly = (annual vol / 7.2) x price
[ ] Measure SETTLEMENT-to-settlement changes, not high/low or open/close
[ ] Count exceedances: >1SD should be ~1 day in 3; >2SD ~1 day in 20
[ ] Mismatch? Name which explanation you are choosing and why
[ ] Indexed-from-100 product? Use (100 - price), index strikes, swap calls/puts
[ ] Bond/note? Do NOT index; decide yield-vol vs price-vol and stay consistent
```

## Related

- [[natenberg-volatility-types]] for which volatility (future, historical,
  forecast, implied) you are even auditing.
- [[natenberg-volatility-forecast]] when the audit says the input is wrong and
  you need a defensible replacement number rather than a nudge.
- [[natenberg-break-even-volatility]] to turn the scaled move into the
  volatility a position has to realize before it pays.
- [[natenberg-greeks-risk-profile]] for what a one-SD move actually does to the
  position once you have sized it.
