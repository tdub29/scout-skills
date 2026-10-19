# OrcaLayer API reference (for the skill)

Verified against the live `/api/v2` + `/api/public/v1` surface and the OpenAPI spec
(`https://orcalayer.com/api/openapi.json`) on 2026-06-29. Base URL: `https://orcalayer.com`.

## Authentication & surfaces

OrcaLayer exposes two surfaces:

| Surface | Base | Auth | Notes |
|---|---|---|---|
| Public read | `/api/v2/*` | none (key optional) | Cloudflare-throttled per IP (~200 req/min). Wallet, market, leaderboard, ISW reads live here. |
| Premium product | `/api/public/v1/*` | `Authorization: Bearer <key>` **or** `X-API-Key: <key>` | 600 req/min, no daily cap. Proxies to `/api/v2/*` after auth. |

**Key rules (verified):**
- **Leaderboard:** call it **keyless** â€” a keyless call returns 200. Passing a *non-Premium*
  key routes through the Premium surface; the SDK (v0.2+) then automatically retries anonymously
  on `/api/v2`, so the call still succeeds, at the cost of a wasted round-trip and a one-time
  warning. Prefer a keyless client for public reads.
- **Public reads** (`/wallet/*`, `/market/*`, `/markets/search`, `/isw/*`, `/hot-traders`,
  `/wallet-search`) work without a key on `/api/v2`.
- **Premium features** require a key: whale-alerts, recent-trades, whale-flips,
  conviction-clusters, hot/resolved markets, live SSE, batch endpoints, AI analysis.
- **Backtest** requires a Premium key on both surfaces: `GET /api/v2/whale/{addr}/backtest` with
  `X-API-Key`, or `/api/public/v1/whale/{addr}/backtest` with `Bearer`. Without a key it returns **401**.

Every response carries `X-RateLimit-*` headers. Categories: `CRYPTO`, `POLITICS`, `SPORTS`,
`GEOPOLITICS`, `ECONOMICS`, `TECH`.

## Python SDK (v0.2.0)

`pip install orcalayer`. Construct once; it makes no network call until a method is used.

```python
from orcalayer import OrcaLayer
oc = OrcaLayer(api_key=None, base_url="https://orcalayer.com")   # key optional
```

Methods (exact signatures):

| Method | Signature | Auth |
|---|---|---|
| `leaderboard` | `(*, sort='pnl', category=None, filter='smart', limit=50, offset=0, min_markets=None, min_wr=None, min_pnl=None, min_profit_factor=None, max_avg_entry=None, max_sports_pct=None) -> dict` | keyless |
| `markets` | `(q='', *, category=None, limit=50, offset=0, min_volume=None, min_whales=None, price_min=None, price_max=None) -> dict` | keyless |
| `wallet_overview` | `(address, *, poll=True) -> dict` | keyless |
| `wallet_positions` | `(address, *, limit=200, offset=0) -> dict` | keyless |
| `whale_alerts` | `(*, minutes=10, wallet=None, market_id=None, min_usd=10, smart_only=True, limit=50, category=None) -> dict` | **Premium** |
| `close` | `() -> None` | â€” |

`poll=True` blocks (~up to 60s) while a heavy wallet computes, then raises `WalletComputingError`;
`poll=False` raises it immediately so you can retry. Exceptions:
`OrcaLayerError`, `APIError`, `AuthenticationError`, `PremiumRequiredError`, `RateLimitError`,
`ServerError`, `WalletComputingError`.

There is **no SDK method** for backtest, wallet profile/closed/alignment, market detail, ISW,
conviction-clusters, or whale-flips â€” use REST for those.

## Endpoints used by this skill

### Leaderboard & discovery (public)
- `GET /api/v2/whales/leaderboard?sort=&category=&filter=smart&min_markets=10&limit=`
  â†’ `{"whales": [{wallet, name, total_pnl, win_rate, profit_factor, resolved_markets, wins,
  losses, total_volume, total_trades, main_category, avg_entry_price, last_trade_ts}], "total"}`
- `GET /api/v2/hot-traders?limit=` â†’ `{"traders": [{wallet, name, trades_1h}]}`
- `GET /api/v2/wallet-search?q=&limit=` â†’ `{"wallets": [{wallet, name, total_pnl}]}`

### Wallet (public read)
- `GET /api/v2/wallet/{address}` â†’ `{address, name, is_smart, is_farmer, is_bot, primary_category}`
- `GET /api/v2/wallet/{address}/overview` â†’ `{profile:{name, pseudonym, address, proxy_wallet},
  overview:{total_trades, total_markets, total_volume, profit_factor, active_count, closed_count,
  first_trade, last_trade, ...}, stats:{is_smart, win_rate, market_win_rate, total_pnl,
  profit_factor, resolved, wins, losses, unrealized_pnl, pnl_24h, pnl_7d, ...}, categories,
  rankings, degraded, as_of}` â€” the SDK returns this verbatim, no reshaping.
- `GET /api/v2/wallet/{address}/positions` â†’ `{positions:[{question, outcome, side,
  current_value, pnl, pnl_pct, avg_entry, current_price, category}], count}` â€” returns the
  full open-position set; the API ignores `limit`/`offset` and does not guarantee order, so
  page and sort (e.g. by `current_value`) client-side.
- `GET /api/v2/wallet/{address}/closed?limit=&offset=` â†’ `{positions:[{condition_id, question,
  side, outcome, tokens, cost, avg_entry, current_price, pnl, category, closed}], total}`
- `GET /api/v2/wallet/{address}/closed-insights` â†’ best/worst category, biggest win, hedged %
- `GET /api/v2/wallet/{address}/pnl-history?period=1M` â†’ `{points:[{ts, cumulative_pnl}]}`
- `GET /api/v2/wallet/{address}/alignment` â†’ how often the wallet sides with smart-money consensus
- `GET /api/v2/wallet/{address}/hold` Â· `/rankings` Â· `/similar-traders` Â· `/related-markets`
- `GET /api/v2/wallet/{address}/trades?since=&before=&limit=&offset=` â†’ raw on-chain CTF event
  feed (advanced; rows carry `entry_type` MINT/MERGE/COMPLEMENTARY/null â€” see note below)
- `GET /api/v2/wallet/{addr}/market-trades?market=&before=&after=` â†’ per-market trade slice

### Backtest & history (Premium â€” send key)
- `GET /api/v2/whale/{address}/backtest?limit=` â†’
  `{"summary": {total, resolved, wins, losses, win_rate, total_pnl},
    "positions": [{market_id, condition_id, question, category, side, avg_entry_price,
    net_tokens, net_cost, pnl, won, winning_side, resolved_at, last_trade_ts}]}`
  Netted, NegRisk/FIFO-correct, resolved positions. **The copy-trade backtest workhorse.**
- `GET /api/v2/whale/{address}/history` â†’ resolved-market history.

### Markets & consensus
- `GET /api/v2/markets/search?q=&category=&limit=` â†’ `{markets:[{id, question, slug, event_slug,
  category, price_yes, whales_yes, whales_no, volume}]}` (keyless; `whales_yes`/`whales_no` =
  smart-money split)
- `GET /api/v2/market/{id}` â†’ `{market:{id, question, category, price_yes, price_no},
  whales:{yes, no, yes_pct}, yes_team, no_team, event}` (keyless)
- `GET /api/v2/market/{id}/breakdown` Â· `/lookup` Â· `/trades` (keyless)
- `GET /api/v2/conviction-clusters?min_whales=3&limit=` â†’ `{clusters:[{event_slug|market_id,
  side, whale_count, market_count, total_capital_usd, whales:[...]}]}` (**Premium**) â€” markets
  where multiple smart whales hold the same high-conviction side.

### Whale activity (Premium â€” send key)
- `GET /api/public/v1/whale-alerts?minutes=&min_usd=&smart_only=true&limit=` â†’ `{alerts:[{timestamp,
  whale:{wallet,name,win_rate,is_smart}, trade:{action,side,price,usd_amount,shares},
  market:{id,category}}], count}`
- `GET /api/public/v1/whales/recent-trades?hours=&category=&limit=` â†’ per-trade smart-money feed
- `GET /api/public/v1/whale-flips?days=&limit=` â†’ wallets that reversed direction on a market
- `GET /api/public/v1/live/trades` â†’ SSE: one JSON event per smart-money trade (long-lived)

### ISW Ukraine (public read)
- `GET /api/v2/isw/status` â†’ control state of every tracked city/zone (per latest ISW map)
- `GET /api/v2/isw/status-summary` â†’ `{ua, ru, contested, flips_24h}`
- `GET /api/v2/isw/events?hours=&city=&min_severity=&limit=` â†’ historical captures/advances/shifts
- `GET /api/public/v1/live/isw/live` â†’ SSE of territory changes (Premium)

### Batch (Premium, POST)
- `POST /api/public/v1/wallets/overview` â€” up to 50 wallets, body `{"wallets":[...]}`
- `POST /api/public/v1/wallets/positions` â€” up to 20 wallets

## Note: raw `/wallet/{addr}/trades` semantics

The rows are **on-chain CTF events**, not orderbook buys/sells. `entry_type`:
`MINT` (split â†’ position entry), `MERGE` (pair merge â†’ exit), `COMPLEMENTARY` (NegRisk adapter
leg), `null` (legacy V1 orderbook trade before the 2026-04-28 indexer cutover). `side` is the
direction of that CTF operation, not an exchange buy/sell. For backtesting prefer the netted
`/whale/{addr}/backtest` and `/wallet/{addr}/closed` endpoints; reach for the raw feed only when
you need event-level granularity.

## Methodology (canonical)

- **Smart money:** win rate â‰¥55% by resolved market, positive lifetime P&L, not a farmer/bot,
  â‰¥10 resolved markets (~208K of ~1.42M tracked wallets qualify).
- **Farmer filter:** average buy price above ~0.95; bots = very high trade counts at tiny size;
  protocol routers excluded.
- **NegRisk correction:** resolved P&L /2 on linked multi-outcome markets, split/merge attributed.
- **FIFO P&L:** per wallet, per market.
- Full version: https://orcalayer.com/methodology
