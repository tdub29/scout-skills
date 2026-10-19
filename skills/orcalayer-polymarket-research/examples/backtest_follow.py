"""Backtest following one wallet â€” what copying it would have returned (Premium).

Run: ORCALAYER_API_KEY=... python examples/backtest_follow.py 0xWALLET
Backtest is a Premium endpoint â€” set ORCALAYER_API_KEY. No SDK method yet, so plain REST.
P&L already encodes OrcaLayer's NegRisk/FIFO/farmer methodology â€” do not reconcile it elsewhere.
"""
import os, sys, httpx

addr = (sys.argv[1] if len(sys.argv) > 1 else "0xc67a7ec12f9982d17ce8063b3c4ad766cc37f0b6").lower()
key = os.environ.get("ORCALAYER_API_KEY")
if not key:
    raise SystemExit("Set ORCALAYER_API_KEY (Premium). Get one at https://orcalayer.com/pricing")

r = httpx.get(f"https://orcalayer.com/api/v2/whale/{addr}/backtest",
              params={"limit": 500}, headers={"X-API-Key": key}, timeout=30.0)
r.raise_for_status()
bt = r.json()

s = bt.get("summary", {})
print(f"Backtest {addr}")
print(f"  resolved positions : {s.get('resolved')}  (wins {s.get('wins')} / losses {s.get('losses')})")
print(f"  win rate           : {s.get('win_rate')}%")
print(f"  total P&L          : ${ (s.get('total_pnl') or 0):,.0f}\n")

# Equity curve: cumulative P&L over resolved positions, time-ordered.
rows = [p for p in bt.get("positions", []) if p.get("won") is not None]
rows.sort(key=lambda p: p.get("last_trade_ts") or 0)
equity = 0.0
print("Resolved positions (chronological):")
for p in rows[:15]:
    pnl = p.get("pnl") or 0
    equity += pnl
    mark = "WON " if p.get("won") else "LOST"
    pnl_s = f"${pnl:+,.0f}"
    print(f'  {mark} {pnl_s:>14}  equity ${equity:>14,.0f}  '
          f'{(p.get("side") or ""):<3} @ {p.get("avg_entry_price")}  {str(p.get("question"))[:48]}')
if len(rows) > 15:
    print(f"  ... and {len(rows) - 15} more")
print("\nInformational only - not financial advice; backtests do not predict future returns.")
