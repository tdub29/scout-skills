"""Is wallet X smart money, or a farmer / hedger? (keyless)

Run: python examples/is_wallet_a_farmer.py 0xWALLET
Wallet overview + positions are public reads â€” no key required.
"""
import sys
from orcalayer import OrcaLayer, WalletComputingError

addr = sys.argv[1] if len(sys.argv) > 1 else "0xc67a7ec12f9982d17ce8063b3c4ad766cc37f0b6"

oc = OrcaLayer()
try:
    try:
        ov = oc.wallet_overview(addr, poll=True)
    except WalletComputingError as exc:
        print(f"Stats still computing â€” retry in ~{exc.retry_after:.0f}s.")
        raise SystemExit
    pos = oc.wallet_positions(addr, limit=50)
finally:
    oc.close()

stats = ov.get("stats", {})
print(f"Wallet: {ov.get('profile', {}).get('name') or addr}")
print(f"  is_smart      : {stats.get('is_smart')}")
print(f"  win_rate      : {stats.get('win_rate')}%  (over {stats.get('resolved')} resolved markets)")
print(f"  total_pnl     : ${ (stats.get('total_pnl') or 0):,.0f}")
print(f"  profit_factor : {ov.get('overview', {}).get('profit_factor')}")

# Farmer / hedger heuristics (the API's is_smart already applies the real filter):
flags = []
if stats.get("is_smart") is False:
    flags.append("NOT flagged smart money")
if (stats.get("resolved") or 0) < 10:
    flags.append("thin sample (<10 resolved markets) - win rate unreliable")
# Hedger tell: paired opposite-side positions in the same market.
seen = {}
for p in pos.get("positions", []):
    seen.setdefault(p.get("question"), set()).add(p.get("outcome"))
hedged = [q for q, sides in seen.items() if len(sides) > 1]
if hedged:
    flags.append(f"holds both sides in {len(hedged)} market(s) - possible hedger/MM")

print("\nVerdict:", "; ".join(flags) if flags else
      "looks like genuine smart money (passes filter, real sample, no obvious hedge).")
print("Note: a very high win rate with avg entry price ~>0.95 is the farmer fingerprint.")
