"""Top smart-money wallets in a category (keyless).

Run: python examples/top_smart_money.py
No API key needed â€” the leaderboard is keyless; a keyless client is cleanest here.
"""
from orcalayer import OrcaLayer

CATEGORY = "CRYPTO"   # CRYPTO | POLITICS | SPORTS | GEOPOLITICS | ECONOMICS | TECH

oc = OrcaLayer()  # anonymous on purpose â€” cleanest for the public leaderboard
try:
    board = oc.leaderboard(sort="pnl", category=CATEGORY, filter="smart", limit=10)
finally:
    oc.close()

print(f"Top smart-money wallets in {CATEGORY} (filter=smart):\n")
for i, w in enumerate(board.get("whales", []), 1):
    # Trust win_rate only with a real sample of resolved markets.
    wr = f'{w["win_rate"]}%' if w.get("resolved_markets", 0) >= 10 else "n/a (<10 resolved)"
    print(f'{i:2}. {w.get("name") or w["wallet"][:10]:<18} '
          f'P&L ${w["total_pnl"]:>14,.0f}  WR {wr:<18} '
          f'markets {w.get("resolved_markets")}  cat {w.get("main_category")}')
