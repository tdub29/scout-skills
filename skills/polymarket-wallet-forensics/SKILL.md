---
name: polymarket-wallet-forensics
description: Decode and analyze Polymarket trader wallets via Polygon on-chain data â€” pull tx history, decode CTF Exchange calldata, reconstruct positions, compute bias and sizing patterns, and identify what makes a "Clawdbot-style" or top-bot wallet profitable. Use this skill whenever the user wants to study, decode, reverse-engineer, or replicate a specific Polymarket wallet's behavior, mentions wallet addresses (e.g., gabagool22, PBbot1, 0x1d00..., k9Q2mX4L8A7ZP3R), asks "how does this trader make money", wants to extract a strategy from on-chain data, or needs to extend the local `decode_polymarket_wallet.py` script. Also trigger for forensic questions about Polymarket: "is this wallet a bot", "what's their bias", "what size do they trade", "when do they enter/exit". This is forensic and historical â€” for live mirroring use `polymarket-copy-trading-bot` instead.
---

# Polymarket Wallet Forensics

This skill is for **understanding** a wallet, not mirroring it. The goal is to reconstruct what a profitable Polymarket trader is actually doing â€” asset mix, sizing, bias, entry timing, win/loss distribution â€” so the user can either learn from the strategy or build their own variant. The article on top 5m/15m bots ([article-5-15-min-bots-strategies.md](../../../article-5-15-min-bots-strategies.md)) is the strategic frame; this skill is the technical pipeline.

There's already a starter script at [decode_polymarket_wallet.py](../../../decode_polymarket_wallet.py) â€” extend it rather than rewriting.

## Why forensics, not copytrading

Copying a fast wallet on 5m/15m markets loses money. By the time the trade is on-chain and your bot sees it, the price has moved â€” you provide exit liquidity. Forensics is different: you're trying to extract the *rules* the wallet follows so you can replicate the strategy with your own infra and timing. See [latency-arb-notes.md](../../../latency-arb-notes.md) and the "Why Copytrading Fast Wallets Fails" section in [math.md](../../../math.md) for why this distinction matters.

## The pipeline

Five stages. Each stage's output is the next stage's input â€” keep them as separate scripts so you can re-run any stage independently.

### Stage 1 â€” Pull raw transactions

For any Polymarket wallet, pull the full Polygon transaction history. Two sources, in order of preference:

1. **Alchemy Polygon API** â€” better rate limits, supports `getAssetTransfers` with paging, returns decoded events. Free tier handles a few hundred wallets/day.
2. **PolygonScan API** â€” simpler but rate-limited. Good for spot-checks.

Filter to transactions involving Polymarket contracts:

| Contract | Address | Purpose |
|----------|---------|---------|
| CTF Exchange | `0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E` | Order matching for binary outcomes |
| Negative Risk CTF Exchange | `0xC5d563A36AE78145C45a50134d48A1215220f80a` | Multi-outcome markets |
| Conditional Tokens Framework | `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045` | Position split/merge/redeem |
| USDC.e (Polygon) | `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` | Settlement currency |

**Verify these addresses before relying on them.** Polymarket has migrated contracts; cross-reference against the Polymarket docs or a recent block explorer view of the wallet.

### Stage 2 â€” Decode calldata

Each `OrderFilled` event on the CTF Exchange carries the market token ID, the outcome (YES/NO), the side (maker/taker), the price, and the size. Decode using the contract ABI (fetch from PolygonScan, cache locally).

For the Conditional Tokens Framework, watch:

- `PositionSplit` â€” wallet minted positions (deployed capital)
- `PositionsMerge` â€” wallet collapsed positions (closed before resolution)
- `PayoutRedemption` â€” wallet collected on a winning resolution

A "Clawdbot-style" trader will show many small `OrderFilled` events at the same timestamp range â€” that's order splitting (see [polymarket-clawdbot-model.md](../../../polymarket-clawdbot-model.md)).

### Stage 3 â€” Map fills to markets

Token IDs in CTF Exchange events are opaque ERC-1155 IDs. Map them to human-readable Polymarket markets via the **Gamma API**:

```
GET https://gamma-api.polymarket.com/markets?clob_token_ids=<id1>,<id2>
```

Cache aggressively â€” token IDs are stable and there can be tens of thousands per active wallet.

This is where the `polymarket-api` skill is useful: use its CLOB/Gamma documentation to get the right endpoint and pagination behavior.

### Stage 4 â€” Reconstruct positions and P/L

Build a per-market ledger:

```
market_id, side (YES/NO), entry_avg_price, exit_avg_price, size, entry_block, exit_block, realized_pnl, status
```

For 5m/15m markets, "exit" usually means resolution â€” the wallet doesn't actively close, it just collects on the winning leg. For longer-dated markets, look for `PositionsMerge` events (closing both legs to lock in P/L).

Key derived stats per wallet:

- **Asset mix** â€” % of volume in BTC vs ETH vs SOL vs XRP, and crypto vs politics vs sports
- **Bias** â€” fraction of trades on Down vs Up; `0x1d00...` and `gabagool22` lean Down (they're betting on volatility revealing)
- **Size distribution** â€” median, p90, p99 per-trade size; bots are often clustered at fixed values (`PBbot1` â‰ˆ $5.8k per fill)
- **Time bucket density** â€” trades per hour-of-day; pure bots show flat 24h distributions, semi-discretionary traders peak around US/EU/Asia overlap
- **Win rate vs profit factor** â€” bots can run at <50% win rate if the average win exceeds the average loss; `PBbot1`'s "low variance" profile suggests tight risk caps

### Stage 5 â€” Identify the strategy signature

Once you have the per-wallet ledger, the strategy reveals itself. Common signatures:

| Signature | Indicator | Likely strategy |
|-----------|-----------|-----------------|
| Many sub-second fills on the same market | Order splitting | Clawdbot-style execution |
| Trades concentrated at oracle-update timestamps | Latency arb | See `chainlink-latency-arb` skill |
| Both YES and NO in same market within seconds | Combinatorial arb | See `combinatorial-arb-detector` skill |
| Constant fill size across 1000s of trades | Fixed sizing rule | Bot, not human |
| Win rate ~52-55% with high turnover | Probability farming | Compounded micro-edge |
| Large position then immediate hedge on related market | Cross-market arb | Multi-condition exposure |

For deeper math (Bregman/Frank-Wolfe arbitrage), see [math.md](../../../math.md). The top traders in that paper (extracting $40M/year) all show signatures 3 and 6.

## Practical guidance

### Start with one wallet, one week

Don't try to ingest all of Polymarket history. Pick one wallet (e.g., `0x1d0034134e339...` from the article), pull one week of activity, and walk through the pipeline end-to-end. Volume there is small enough to verify by hand against the Polymarket UI.

### Watch for proxies and helper contracts

Some bots route through smart-contract wallets or Gnosis Safes. Pulled transfers will show the safe as the source/destination. Trace inwards to find the EOA(s) that own the safe â€” that's the human (or at least the signer).

### Privacy and ToS

On-chain data is public. But aggregating it into a public profile of a trader and posting it could violate Polymarket's ToS or be considered harassment. Keep this work for personal study, paper-test variants of strategies you derive, and don't dox individuals.

### When to escalate to indexers

If you're analyzing > 10 wallets or want streaming queries, switch to **Dune**, **The Graph**, or **Subsquid** instead of repeated RPC calls. The `SII-WANGZJ/Polymarket_data` repo (1.1B records) referenced in [github-resources.md](../../../github-resources.md) is the bulk-data starting point.

## Output formats Claude should produce

When the user asks Claude to analyze a wallet, default to a structured report:

```
# Wallet Forensic Report â€” <address or alias>

## Identity
- Polymarket profile URL
- Joined date / first activity
- Total realized P/L (from on-chain data)

## Volume & Activity
- Total trades
- Total volume
- Markets touched
- Active hours per day

## Strategy Signature
- Asset mix (% BTC / ETH / SOL / XRP / other)
- Bias (Up/Down split)
- Median fill size, p90, p99
- Order splitting? (yes/no, evidence)
- Same-market hedge pattern? (yes/no, evidence)

## Likely Playbook
<one paragraph describing the inferred strategy, citing the table above>

## What to Replicate vs Avoid
<bullet list â€” what the user could realistically build, what's infra-dependent (latency, capital), what's risky to copy>
```

Never claim the trader is "definitely" running strategy X â€” call it a "likely signature" and back it with the evidence. Many wallets look like one thing on the surface and turn out to be running multiple sub-strategies.

## What this skill is NOT

- Not live copytrading â€” see `polymarket-copy-trading-bot`
- Not generic Polymarket SDK â€” see `polymarket-api`
- Not a Nansen replacement â€” for cross-chain wallet clustering and labeling, that's a separate (paid) tool
- Not legal/financial advice â€” forensics is for learning; trading decisions are the user's
