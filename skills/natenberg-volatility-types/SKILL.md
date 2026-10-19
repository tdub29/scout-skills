---
name: natenberg-volatility-types
description: Disambiguate the four things traders mean by "volatility": future (the unknowable right answer), historical/realized (backward-looking, calculation-method dependent), forecast (a service's estimate, an inexact science), and implied (backed out of an option's market price, a property of the OPTION not the underlying). Then price options in volatility terms rather than dollar terms. Use when asked "is this option expensive," "what does implied volatility actually mean," "IV vs historical vol," "are premium levels high," "how do I compare two options on the same underlying," or whenever a conversation about "the volatility of X" is ambiguous about which volatility. From Sheldon Natenberg, Option Volatility and Pricing, Chapter 4.
---

# Natenberg Volatility Types

## Why this matters

> When traders discuss volatility, even experienced traders may find that they
> are not always talking about the same thing.

"The volatility of XYZ is 25%" has at least four meanings. Three describe the
**underlying contract**; one describes an **option**. Confusing them is how
people end up comparing incomparable numbers.

## The four

**1. Future volatility.** The volatility that best describes the *actual* future
distribution of prices. This is what "the volatility input" in a pricing model
theoretically means. Know it and you know the right odds; feed it in and the
theoretical values are correct, like the casino. **Nobody knows it.** Traders
rarely even discuss it because it is unobservable.

**2. Historical (realized) volatility.** Computed from past price data. Two
things to hold onto:

- **The calculation method varies.** There are several ways to compute it
  (settlement-to-settlement is standard; Parkinson, Garman-Klass and Beckers
  give extreme-value estimators from high/low/close). Services that supply
  historical volatility generally base it on settlement prices.
- **Historical and future volatility together are sometimes called *realized*
  volatility.** Ask which is meant.

Whatever the source, the annual number only becomes checkable once scaled to a
daily or weekly move. That arithmetic lives in [[natenberg-volatility-scaling]].

**3. Forecast volatility.** A service's estimate of future volatility, usually
published over horizons matching the remaining life of the listed options (for
quarterly expirations, three/six/nine months; for monthlies, one/two/three).
Natenberg is blunt: volatility forecasting is **an inexact science at best**. It
is an input to a trader's own guess, not a substitute for it.

**4. Implied volatility.** The odd one out. Future, historical, and forecast
volatility all belong to the **underlying**. Implied volatility belongs to an
**option**.

## How implied volatility is derived, and what it actually is

Worked example from the source. A futures contract at 98.50, interest rates 8%, a
105 call with three months to expiry, and your best volatility guess of 16%.
Black-Scholes gives a theoretical value of **0.96**. The market is trading it at
**1.34**.

Assume everyone is using the same model. Then the disagreement must live in one
of the inputs. Walk the list:

- **Time to expiration and exercise price.** Fixed in the contract, cannot be
  the source.
- **Underlying price.** Always double-check it, but suppose it really is 98.50.
- **Interest rates.** Knowable.
- **Volatility.** The only input left that is genuinely a matter of opinion.

Solve for the volatility that makes the model return 1.34 instead of 0.96. That
number, here about **18.5%**, is the **implied volatility of the 105 call**: the
volatility the marketplace is implying, given its price.

**The consensus framing.** Implied volatility changes constantly because prices
and conditions do. It is *as if* the market were continuously polling every
participant for a consensus volatility. Not a literal vote: as bids and offers
are made, the traded price is the **equilibrium between supply and demand**, and
that equilibrium translates into an implied volatility.

**A single number for a contract.** When one implied volatility is quoted for an
underlying, it is usually a weighted average of the individual options' implieds,
weighted by volume, open interest, or, most commonly, **by giving the greatest
weight to the at-the-money options.**

**Premium level.** Strictly, "premium" means an option's price, but traders
routinely use it for the implied volatility. *Premium levels are high* means
implied volatility is high by historical standards, or high relative to the
underlying's recent historical volatility. Low implied vol means low premium
levels.

## The practical payoff: compare in volatility terms, not dollars

With a reliable model and a known future volatility, you would simply sell every
option priced above theoretical value and buy every one priced below, and if
choosing between two overpriced options, sell whichever is most overpriced **in
total dollars**.

A trader with implied volatilities has a better yardstick. Compare an option's
implied volatility either to a **volatility forecast** or to the **implied
volatility of other options on the same underlying.**

Same 105 call: at a theoretical value of 0.96 and a price of 1.34 it is
**0.38 overpriced in dollars**, but **2.5 volatility points** rich (18.5% versus
your 16%). The volatility-point figure is the one that is comparable across
strikes, expirations and contracts. Dollar richness is not. A deep in-the-money
option and a far out-of-the-money one can be equally rich in vol terms and wildly
different in dollars.

## Disambiguation checklist

```
[ ] Which volatility is being discussed? (future / historical / forecast / implied)
[ ] Underlying-level or option-level? (implied is the only option-level one)
[ ] Historical: computed how? settlement-to-settlement, or an extreme-value estimator?
[ ] Historical: over what window? (a 30-day and a 250-day number are different claims)
[ ] Implied: for WHICH option, or a weighted average? weighted by what?
[ ] Comparing richness: in volatility points, not dollars
[ ] "Premium is high" = implied vol high vs history or vs recent realized. Say which
```

## Related

- [[natenberg-volatility-scaling]] to audit whichever volatility number you land
  on against actual observed price changes.
- [[natenberg-volatility-forecast]] when the number you need is forward-looking
  and you have to build it rather than read it off a screen.
- [[natenberg-volatility-skew]] because a single implied volatility per contract
  hides the fact that strikes trade at different implieds.
- [[natenberg-theoretical-edge]] to turn "implied is 2.5 points rich" into a
  sized, quantified edge.
