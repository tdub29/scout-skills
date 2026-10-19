---
name: chainlink-latency-arb
description: Detect and exploit the ~60-second latency gap between Chainlink oracle updates and Polymarket's UI/resolution display on 5-minute and 15-minute crypto Up/Down markets (BTC, ETH, SOL, XRP). Use this skill whenever the user mentions Chainlink oracle reads, Polymarket 5m/15m crypto markets, oracle latency, terminal lag, "reading resolution before the UI", direct RPC subscriptions, or wants to build infrastructure that sees price/resolution data before the crowd. Also trigger if the user references gabagool22, PBbot1, the 0x1d00... wallet, Clawdbot 5m/15m strategies, or asks about why "skilled traders can print" on these short-duration markets â€” the answer is almost always oracle-vs-UI latency, not directional skill.
---

# Chainlink Oracle Latency Arb (Polymarket 5m/15m)

The edge on Polymarket's 5m/15m crypto Up/Down contracts isn't directional analysis â€” it's **infrastructure**. Polymarket settles via Chainlink, and the terminal lags the oracle by roughly 60 seconds. Anyone reading Chainlink directly sees resolution data before the UI updates, which means they can place or cancel orders into a window where the rest of the market is still pricing as if the outcome were uncertain.

This skill teaches Claude how to set up that direct-read pipeline, normalize timestamps, identify the exact feed Polymarket uses, and structure the trading logic that monetizes the gap. It complements `polymarket-api` (which covers CLOB/Gamma) and `grimoire-polymarket` (CLI execution).

## When the edge applies

- BTC/ETH/SOL/XRP 5-minute and 15-minute Up/Down markets on Polymarket
- The market hasn't already resolved on-chain when you start
- Liquidity is deep enough that your order won't single-handedly close the spread
- The ~60s delay still holds â€” verify empirically each session, the gap compresses as more participants run similar pipelines

## Core build

The pipeline has four pieces. Keep them decoupled so you can swap any one without rewriting the rest.

### 1. Identify the exact Chainlink feed Polymarket uses

Polymarket settles 5m crypto markets via Chainlink Data Feeds on Polygon. For BTC/USD, the canonical Polygon mainnet aggregator is `0xc907E116054Ad103354f2D350FD2514433D57F6f`. **Always verify the current feed address** before relying on it â€” Polymarket has changed feeds before, and the proxy/aggregator distinction matters:

- The **proxy** is stable but adds one hop of read latency
- The **aggregator** behind the proxy updates first; subscribing here shaves milliseconds

To verify which feed a given market uses, read the Polymarket market metadata via the Gamma API and look at the `resolutionSource` or oracle reference. If unclear, cross-check by replaying a recent resolution and confirming the round timestamp matches.

### 2. Subscribe to round updates (don't poll)

Polling adds latency equal to your poll interval. Subscribe to `AnswerUpdated` events on the aggregator via WebSocket RPC. Recommended providers:

- **Alchemy Polygon** â€” generous free tier, low jitter
- **QuickNode** â€” paid but consistent sub-100ms event delivery
- **Self-hosted Polygon node** â€” lowest latency, highest ops cost

Capture three timestamps per round so you can measure the gap and validate the edge still exists:

```
oracle_round_id, oracle_answer, oracle_block_time, oracle_received_at, polymarket_ui_observed_at
```

The delta `polymarket_ui_observed_at âˆ’ oracle_received_at` is your edge window. If it shrinks below ~10s, the play is dead â€” pivot or stop.

### 3. Map oracle rounds to Polymarket market IDs

5m markets on Polymarket are time-bucketed (`btc-updown-5m-<unix-ts>`). The resolution rule is "BTC price at the bucket's close as reported by Chainlink." Build a lookup that, given a fresh oracle round at time T, identifies the Polymarket market that closes at T (or just after) and is therefore about to be resolved.

This mapping is mechanical â€” write it as a pure function so it's testable:

```python
def market_id_for_round(round_close_ts: int, asset: str = "BTC") -> str:
    bucket = round_close_ts - (round_close_ts % 300)  # 5m
    return f"{asset.lower()}-updown-5m-{bucket}"
```

### 4. Execution layer

Once you know the resolution before the UI does, the trade is mechanical: take or cancel into the side that's about to win.

- **Use `post_only=true`** by default â€” you don't want to cross the spread and pay the taker fee on info that's about to be public. See `bot-ops-review` skill for the full ops-checklist.
- **Cancel stale resting orders the instant the oracle prints**, before the rest of the book repositions.
- **Cap size at a fraction of order book depth** (research suggests â‰¤50%) so you don't move the price against yourself before all legs fill.
- **Submit via direct RPC**, not the Polymarket REST API â€” REST adds ~50-150ms.

Reference the local notes in [latency-arb-notes.md](../../../latency-arb-notes.md) for the strategic framing and [ops-checklist-polymarket-bots.md](../../../ops-checklist-polymarket-bots.md) for the risk controls that must be in place before this goes live.

## Cross-venue extension

The same idea generalizes: same underlying event, different oracles.

| Venue | Oracle |
|-------|--------|
| Polymarket | Chainlink |
| Kalshi | Internal pipeline |
| Drift | Pyth |

Pyth and Chainlink update on different cadences with different latencies. A unified pipeline that ingests all three lets you spot structural cross-venue mispricings that don't compress in 60 seconds because they aren't a single-venue race â€” they're a feed-divergence trade.

The `kalshi` skill covers Kalshi reads. For Pyth, the reference docs are at https://docs.pyth.network â€” fetch with `microsoft_docs_fetch` only if needed; the public Pyth docs have the price service URL and the schema directly.

## Sanity checks before going live

Before risking real capital, prove the edge to yourself:

1. **Run the pipeline read-only for 24 hours.** Log the gap distribution. Median should be 30-90s; if it's already <10s, infra alone won't carry you.
2. **Replay one resolution.** Take an oracle round you observed and verify the Polymarket UI confirmation timestamp lagged it by what your logs say. Don't trust your own measurements until you've sanity-checked them this way.
3. **Paper trade for at least one day.** Simulate fills against the historical book. The research shows ~13% of mathematically-valid arb fails on execution due to liquidity or competition â€” your simulator should reproduce this.

## Failure modes to expect

- **Edge compression.** The more wallets running this, the smaller the gap. The trade decays as it gets more popular. Track the gap and pull back when it shrinks.
- **Feed change.** If Polymarket switches the aggregator without notice, your pipeline reads stale data. Add a circuit-breaker that pauses trading if oracle freshness exceeds an SLA (e.g., no update in 90s when you expect one every 60s).
- **Reorg risk.** Polygon reorgs are rare but real. Don't act on a single block â€” wait for confirmation depth proportional to your position size.
- **You become exit liquidity.** If you're copying a faster wallet rather than reading the oracle yourself, you're trading on stale info â€” see [article-5-15-min-bots-strategies.md](../../../article-5-15-min-bots-strategies.md) for why naive copytrading on these markets loses money.

## What this skill is NOT

- Not directional analysis. It does not predict BTC. It races on data delivery.
- Not a copytrading skill (use `polymarket-copy-trading-bot` for that â€” and read the failure modes above first).
- Not a generic Polymarket SDK guide (use `polymarket-api`).
- Not Chainlink contract development (use `smartcontractkit/chainlink-agent-skills` for protocol work).
