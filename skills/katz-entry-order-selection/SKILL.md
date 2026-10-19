---
name: katz-entry-order-selection
description: Choose the entry order type (stop, limit, or market) that matches a trading model's theory of market behavior, using Katz and McCormick's tradeoffs â€” stop orders confirm direction but buy high and eat slippage, limit orders get a known price with zero slippage but may never fill and are inherently countertrend, market orders guarantee a fast fill with two-sided slippage. Use when asked "should I enter on a stop or a limit," "what order type suits a breakout system," "why is my entry slipping so badly," "how do I enter a retracement/mean-reversion signal," or when the entry order is being treated as an afterthought rather than as part of the model. From Katz and McCormick, The Encyclopedia of Trading Strategies, Part Two Introduction.
---

# Katz Entry-Order Selection

## What this decides

Which order type executes a given entry signal. The point most traders miss:
**the order type is part of the entry model, not a detail bolted on afterward.**
A stop entry on a breakout system *is* the breakout rule. Pick the order that
matches the model's theory of what the market is about to do.

## The three orders and their real tradeoffs

**Stop order** â€” enters a market already moving in the trade's direction. A buy
triggers above the stop, a sell below it.

- For: the market must be moving favorably at the moment of entry, so the order
  itself acts as a confirming filter on the signal. A genuinely good entry turns
  profitable fast with almost no adverse excursion.
- Against: slippage, worst exactly when the move is fastest. Entry happens
  significantly into the move at a relatively poor price. The nastiest case is a
  fill far past the stop just as the market reverses.
- Natural home: trend-following and breakout models.

**Limit order** â€” enters when the market moves *against* the trade's direction.
Buy limits fill below the limit price, sell limits above.

- For: no slippage. Entry at a good, known price.
- Against: it is countertrend in the short term, and the market may never come
  to the order at all, so signals get missed.
- Natural home: predictive countertrend models, and anything that specifies a
  price rather than only a moment.

**Market order** â€” buy or sell at the prevailing price.

- For: fast, and execution is guaranteed. Stops and limits can sit unfilled;
  many exchanges require market orders to fill within minutes.
- Against: slippage, but two-sided. It can land in the trade's favor or against
  it, depending on movement and execution delay.
- Natural home: models that supply timing only.

## The selection rule

Match the order to what the model claims to know.

| The model predicts | Use | Why |
|---|---|---|
| A turning point slightly ahead, with a price | **Limit** | Fills at or near the level; a bounce turns it profitable fast, and a tight money-management stop caps the failure cheaply |
| A direction, needing confirmation before commitment | **Stop** | The order only fires if the market actually goes there, so no signal, no trade |
| Only timing, with no price and no confirmation available cheaply | **Market** | Confirmation via a stop would cost more in slippage and delay than the expected per-trade profit |

Critical-retracement systems are the clearest case for a limit: the model names
the price, so entry on a limit plus a tight stop produces either a quick winner
or a very small loss.

Breakout systems are the clearest case for a stop: pass the threshold and you
are in automatically; fail to pass it and there was never a trade.

## The decision questions

Ask in this order:

1. **Does the model specify a price, or only a time?** A price supports a limit
   or a stop. Time alone points at a market order.
2. **Is the model trend-following or countertrend?** Trend-following wants
   confirmation, which is a stop. Countertrend wants a better price against the
   move, which is a limit.
3. **Do I need the entry filtered?** If a wrong-direction market should cancel
   the trade entirely, only a stop does that for free.
4. **What is expected profit per trade versus expected slippage?** When per-trade
   profit is thin, a stop's slippage can consume the edge, and a market order or
   a limit is the cheaper execution.
5. **Can I tolerate missed trades?** Limits miss. If the model's edge depends on
   catching every signal, a limit will not deliver it.

## The failure signatures

- Backtest and live results diverge on a breakout system, mostly on the biggest
  winners: slippage on stop entries in fast moves. Test with realistic, larger
  slippage assumptions rather than a fixed small constant.
- A countertrend system underperforms its backtest with unexplained losers:
  entering on stops or market orders, which forces buying high into the very
  move the model wants to fade.
- A limit-based system takes far fewer trades live than in the backtest: the
  simulator is filling limits the real market never traded through. Fills at the
  limit price require the market to trade beyond it, not merely touch it.

## Related

- [[katz-optimization-discipline]] before believing any of the entry test
  results that motivate a choice here.
- [[katz-exit-strategy-taxonomy]] for the paired exit, especially the tight
  money-management stop that makes limit entries at retracement levels work.
