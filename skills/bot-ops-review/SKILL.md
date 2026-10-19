---
name: bot-ops-review
description: "Trading bot risk controls, kill switch, deploy safety"
---

# Bot Ops Review (Polymarket / Prediction-Market Bots)

Trading bots fail two ways: (1) the code does the wrong thing technically, and (2) the code does the right thing but blows up on a corner case nobody thought about â€” outage, oracle stale, network partition, leaked key. This skill is for catching the second failure mode.

The checklist itself lives in [ops-checklist-polymarket-bots.md](../../../ops-checklist-polymarket-bots.md), and the security setup in [shelpid-wi3m-clawdbot-setup.md](../../../shelpid-wi3m-clawdbot-setup.md). This skill operationalizes them: when Claude is reviewing bot code or helping spin one up, walk through each section deliberately and call out gaps.

## When to invoke

- User asks "review my bot code"
- User is about to deploy or go live
- User adds a new feature (new market, new sizing rule, new venue)
- User mentions putting real funds in
- User shares a config file, systemd unit, Dockerfile, VPS setup script
- User references the project's Clawdbot or weather-Clawdbot setup
- Anything that smells like "I'm wiring this to my mainnet wallet"

If in doubt, run the review. The cost of a 60-second checklist scan is trivial; the cost of a missing kill-switch is your bankroll.

## The four pillars

### 1. Trading controls (must-haves, not nice-to-haves)

These are pre-trade and per-trade gates. Each must be a hard cap enforced in code, not a goal in a docstring.

| Control | What it does | Failure if missing |
|---------|-------------|----------------------|
| `max_position_usd` per market | Cap exposure on any single market | One mispriced market drains the bankroll |
| `max_total_exposure_usd` | Cap total open exposure across markets | Many small positions correlate and blow up together |
| `max_open_orders` | Cap unwind complexity | Can't cancel safely if something breaks |
| `max_daily_loss_usd` kill switch | Auto-halt at threshold | Tilted bot trades itself broke |
| `max_drawdown_pct` kill switch | Halt if equity curve craters | Slow-bleed strategies eat capital |
| `post_only=true` default | Don't cross the spread on stale info | Pay taker fee + adverse selection |
| Cancel-on-near-resolution | Don't get picked off in the last seconds | Late-resolution-leak losers |

When reviewing code, grep for these:

- Hard-coded position sizes with no cap variable â†’ flag
- Order placement that doesn't check current exposure â†’ flag
- Daily P&L tracking but no halt action â†’ flag (logging without enforcement is theatre)
- `post_only` not set or `False` without justification â†’ flag

### 2. Monitoring & alerts

Logging is necessary; alerting is what saves you. Every order event and every position change needs a timestamp + price + reason.

The metrics that catch failures earliest:

- **One-sided fill rate** â€” if YES legs fill but NO legs don't, you're systematically exposed and the strategy's broken
- **Time-to-fill distribution** â€” sudden widening means liquidity dropped, slow down or stop
- **Slippage vs expected** â€” if realized prices keep beating or missing your estimates by > 1Â¢, recalibrate or pause
- **API/WebSocket disconnects** â€” every disconnect is a window where state can desync; alert and verify before resuming
- **Drawdown** â€” daily, since-inception, and rolling 7-day; alert at 5%, halt at the configured `max_drawdown_pct`

Alerts should arrive somewhere the user actually sees fast â€” Telegram or SMS, not email. Each alert must include three things:

```
1. WHAT happened: "BTC 5m market 1771350600 â€” YES leg filled, NO leg rejected"
2. WHAT the bot did: "Bot canceled remaining order, flattened position via reverse market order"
3. WHAT it will do next: "Bot is paused; manual resume required"
```

Vague alerts ("error in trading bot") force the user to context-switch into debug mode every time. Specific alerts let them triage in 30 seconds.

### 3. Security (the boring stuff that keeps you solvent)

Bot wallets get drained constantly by leaked keys, exposed dashboards, and reused credentials. The defenses are well-known and cheap:

- **Keys-only SSH**, password auth disabled, root login disabled
- **Default-deny inbound firewall**, allow only what's required (usually just SSH from Tailscale)
- **fail2ban** or equivalent for brute-force protection
- **Tailscale** or another mesh VPN for private-by-default network access â€” your dashboard, RPC nodes, and admin endpoints should not be public
- **Separate trading wallet from main wallet.** The bot key signs trades; it does NOT have access to long-term holdings. Move profits to the main wallet manually or via a scheduled sweep with a separate key.
- **Minimal API key scopes.** Where the venue lets you, restrict by IP and by capability.
- **Sandbox / container isolation** for any agent-driven execution. Command allowlists only â€” never give the bot a free shell.

For the project's specific VPS setup, follow [shelpid-wi3m-clawdbot-setup.md](../../../shelpid-wi3m-clawdbot-setup.md) end-to-end.

### 4. Deployment hygiene

Bots crash. Servers reboot. Power flickers. These need to be *normal* events, not catastrophic ones.

- **Run as a service with auto-restart** (systemd or equivalent) â€” but combine with **safe-mode-on-restart**. On boot, the bot does NOT immediately start trading. It reloads state, verifies positions match the venue's view, and waits for an explicit unpause signal.
- **Single source of truth for state.** Open orders, current positions, bankroll limits â€” one canonical store, queried by everything else. Don't compute "how much am I exposed" by summing across multiple files.
- **Panic button.** A single command (CLI, Telegram bot, hotkey) that:
  1. Cancels all open orders
  2. Optionally flattens positions
  3. Pauses trading (so the auto-restart doesn't undo the panic)

If there's no panic button in the bot, the user has to write one mid-incident. That's the worst possible time to design a feature.

## How Claude should do the review

When invoked, walk through the four pillars in order. For each one:

1. **Cite what's present.** "I see `max_position_usd` is set in `config.py:14` and enforced in `place_order` at line 87."
2. **Flag what's missing.** "I don't see a `max_drawdown_pct` kill-switch â€” drawdown is logged but never triggers a halt action."
3. **Flag what's present-but-broken.** "There's a `kill_switch` flag but it's only checked at startup, not before each order."
4. **Recommend a concrete fix.** Not "add risk controls" â€” instead, the actual code change.

Output structure:

```
# Bot Ops Review â€” <bot name>

## Trading Controls â€” <PASS / GAPS / FAIL>
- [ok] max_position_usd present and enforced
- [gap] max_drawdown_pct logged but no halt action â€” recommend ...
- ...

## Monitoring & Alerts â€” <PASS / GAPS / FAIL>
- ...

## Security â€” <PASS / GAPS / FAIL>
- ...

## Deployment Hygiene â€” <PASS / GAPS / FAIL>
- ...

## Top 3 Things to Fix Before Going Live
1. ...
2. ...
3. ...
```

The "top 3" prioritization matters. A long unsorted list of issues lets the user defer all of them. Three concrete blockers force the conversation about whether the bot is actually ready.

## Pre-deploy gate

Before any deployment that touches real funds, the bot must satisfy at minimum:

- [ ] Hard caps on position, total exposure, and daily loss
- [ ] Kill switch wired to drawdown
- [ ] Post-only default, with justified exceptions
- [ ] Alerts to a fast channel (Telegram/SMS) including what/did/next
- [ ] Trading key separated from main wallet
- [ ] Server behind Tailscale (or equivalent), no public dashboard
- [ ] Panic button command tested at least once
- [ ] Safe-mode-on-restart verified by manually killing and restarting the service

If any of these fail, the user should paper-trade or drop bankroll size before re-attempting. The project's "$1 paper test" guidance ([AGENTS.md](../../../AGENTS.md), Theme #4) applies here: don't deploy at full size on day one.

## Common gaps to check for

These show up across most bot reviews:

- **Drawdown is tracked but not enforced.** A halt action must mutate state (set a `paused` flag in the source-of-truth store) so a restart doesn't immediately resume trading.
- **Disconnect handling silently retries forever.** WebSocket reconnect loops without exponential backoff or an alerting threshold mean you find out about an outage when you check P&L the next day.
- **Configuration is split across env vars, JSON, and constants.** Pick one. Misconfiguration that requires reading three files to diagnose is a time bomb.
- **No reconciliation step between local state and venue state.** Local thinks position is +500 YES, venue thinks +0 (an order failed silently). Bot keeps trading on the false picture. Reconcile on every restart and at a fixed interval (e.g., every 5 minutes).
- **Secrets in `.env` files committed to git.** Audit for `.env` in the repo, `private_key=` in source, hardcoded RPC URLs with auth tokens.
- **Telegram bot tokens in group chats.** Per the ops checklist: bot restricted to a single user, never group chats â€” group chat means anyone in the group can issue commands.

## What this skill is NOT

- Not a substitute for paper trading. Reviews catch what's missing in code; live behavior catches what's missing in the model.
- Not a generic security review (use `security-review` for that on a wider codebase).
- Not strategy review â€” soundness of the strategy is a different question (see `trading-strategies` and `combinatorial-arb-detector`).
- Not an excuse to deploy. The checklist passing means "the obvious failure modes are guarded." It does not mean "this is profitable" or "this is safe at any size."
