---
name: saliba-butterflies-condors
description: Express a trading-range or big-move view with defined risk using butterflies and condors â€” long when forecasting little movement and seeking time decay or falling implied volatility, short when forecasting a large move either way â€” including the 1-2-1 construction, the max profit formula (wing width minus debit), the two breakevens, and the call/put/iron equivalence. Use when asked "how do I trade a range with limited risk," "butterfly or condor," "what's an iron butterfly," "cheaper alternative to a short straddle," "how do I profit if nothing happens," or "where do I put the body of the fly." From Anthony J. Saliba, Option Spread Strategies, Chapter 5.
---

# Saliba Butterflies and Condors

## What they are

Directionless structures. Like straddles and strangles, the forecast is
**magnitude, not direction** â€” but with **defined risk on both sides**, which is
the whole reason to prefer them.

- **Long butterfly** â€” long 1 lower strike, short 2 middle strikes, long 1 upper
  strike; same class, same expiration, equally spaced strikes.
- **Long condor** â€” the same shape with the body split into two different
  strikes, giving a flat profit plateau instead of a single peak.
- **Iron** variants build the same payoff from a mix of calls and puts. Call, put,
  and iron butterflies at the same strikes and expiration share the same Greeks;
  choose between them on pricing and margin, not on payoff.

## Direction of the magnitude forecast

- **Long butterflies and condors** are used when forecasting **little or no
  directional movement, or a trading range**, seeking to profit from the
  position's value rising via **time decay or falling implied volatility**.
- **Short butterflies and condors** are used when forecasting a **large-magnitude
  move in either direction**, seeking to profit from the position's value falling.

Note the sign convention that trips people up: the **long** butterfly is the
short-volatility trade. It is long the structure, not long volatility.

## The arithmetic

For a long call butterfly at strikes K1 < K2 < K3 with equal spacing, entered
for a debit:

- **Max profit** = (K3 - K1)/2 - debit, realized at K2 at expiration
- **Max loss** = the debit paid
- **Breakevens** = K1 + debit and K3 - debit

Worked from the source: long 1 March 130 call at $7.00, short 2 March 135 calls
at $5.00, long 1 March 140 call at $4.00, for a **$1.00 debit**.

- Max profit = (140 - 130)/2 - 1.00 = **$4.00**
- Max loss = **$1.00**
- Breakevens = **$131.00** and **$139.00**

That 4-to-1 reward-to-risk with a defined loss is the structural appeal, and the
catch is visible in the same numbers: the profit zone is only eight points wide
and the maximum is reached at exactly one price.

## Placement

- **The body (K2) is the forecast.** It should sit where you expect the
  underlying to be at expiration, not where it is now.
- **Wing width** trades probability against payoff: wider wings cost more, widen
  the breakevens, and lower the peak-to-cost ratio; narrower wings are cheap
  lottery tickets on a precise landing.
- **A condor is a butterfly with a tolerance band.** Use it when the range view
  is honest about being a range rather than a point.

## Butterfly versus short straddle

Both express stillness. The butterfly is the short straddle with insurance
attached:

| | Short straddle | Long butterfly |
|---|---|---|
| Max loss | Undefined | The debit |
| Max profit | Full premium | Wing width/2 minus debit |
| Margin | Heavy | Light |
| Best when | Confident and well-capitalized | Right view, limited risk budget |

## Checklist

```
[ ] Am I forecasting a RANGE (long fly) or a BIG MOVE (short fly)?
[ ] Is the body placed at the expected expiration price, not the current price?
[ ] Computed: max profit, max loss, both breakevens
[ ] Wing width chosen deliberately against probability of landing in the zone
[ ] Condor instead of butterfly if the view is a band rather than a point
[ ] Call / put / iron chosen on pricing and margin (Greeks are identical)
[ ] Four legs of commissions checked against a often-small max profit
```

## Related

- [[saliba-straddles-strangles]] for the undefined-risk version of the same view.
- [[saliba-spread-selection]] for routing into this family in the first place.
