# OrcaLayer Agent Skill

A portable [agent skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) that
teaches any skill-aware agent (Claude Code, Cowork, Claude Desktop) to do **Polymarket
smart-money research** with the [OrcaLayer](https://orcalayer.com) API: farmer-filtered
leaderboards, NegRisk-corrected win rates, per-wallet FIFO P&L, resolved-position backtests, and
an ISW Ukraine frontline overlay.

It is the same capability surface as the [orcalayer-mcp](https://github.com/orcalayer/orcalayer-mcp)
server, delivered as a `SKILL.md` so it works in any tool that loads skills â€” no MCP server to run.

## What's inside

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill itself â€” when to use it, setup, capabilities, worked examples, guardrails. |
| [`reference/api.md`](reference/api.md) | Full endpoint reference, SDK signatures, auth matrix. |
| [`examples/`](examples/) | Runnable snippets: top smart money, farmer check, backtest a wallet. |

## Install

The skill is the `SKILL.md` (plus its `reference/` and `examples/`). Drop the folder into your
agent's skills directory:

**Claude Code**
```bash
git clone https://github.com/orcalayer/orcalayer-skill.git
# personal (all projects):
mkdir -p ~/.claude/skills && cp -r orcalayer-skill ~/.claude/skills/orcalayer-polymarket-research
# or project-scoped:
mkdir -p .claude/skills && cp -r orcalayer-skill .claude/skills/orcalayer-polymarket-research
```

**Claude Desktop / Cowork** â€” add it as a skill from the skills/settings panel (point it at the
cloned folder, or copy it into the app's skills directory). The agent auto-loads `SKILL.md` and
triggers it when you ask about Polymarket whales, smart-money wallets, farmer filtering, market
consensus, or copy-trade backtesting.

## Setup

```bash
pip install orcalayer            # official SDK (v0.2.0)
export ORCALAYER_API_KEY=...     # Premium key â€” get one at https://orcalayer.com/pricing
```

- **The leaderboard is keyless** â€” prefer a keyless client for it and other public reads (a
  non-Premium key still works via the SDK's v0.2 public fallback, but adds a wasted round-trip).
- Public reads (wallet, market, ISW) work without a key; Premium features (whale-alerts,
  backtest, live SSE, batch) need the key.

Try it:
```bash
python examples/top_smart_money.py                 # keyless
python examples/is_wallet_a_farmer.py 0xWALLET     # keyless
ORCALAYER_API_KEY=... python examples/backtest_follow.py 0xWALLET   # Premium
```

## Related

- **API & docs:** https://orcalayer.com/developers Â· https://orcalayer.com/docs Â·
  https://orcalayer.com/docs/api
- **Pricing / API key:** https://orcalayer.com/pricing
- **MCP server:** https://github.com/orcalayer/orcalayer-mcp
- **Backtest cookbook (notebooks):** https://github.com/orcalayer/polymarket-backtest-cookbook

## Safety

Informational only â€” **not financial advice**. OrcaLayer is a data layer, not an execution venue.
Past performance and backtests do not predict future results.

## License

MIT â€” see [LICENSE](LICENSE).
