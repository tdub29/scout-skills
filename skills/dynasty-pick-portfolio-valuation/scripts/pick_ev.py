"""Price a stack of dynasty picks as a portfolio: EV per pick, expected hits, share band, sell flags.

usage: python pick_ev.py picks.json
       python pick_ev.py --demo

picks.json:
{
  "target_seasons": 4,            # seasons from the rookie draft to the season you want to field them (1 = rookie year)
  "teams": 10,                    # league size, for the stack limit
  "roster_total_value": 60000,    # optional: total roster dynasty value on the same chart, for the share band
  "stance": "rebuild",            # optional: contender | rebuild, for the share target
  "picks": [
    {"label": "2027 1st (early)", "slot": "early1", "chart": 7304, "class_premium": 0.385},
    {"label": "2027 1st (mid)", "slot": "mid1", "chart": 5628, "tier": 56}
  ]
}

slot is one of early1_rb, early1, mid1, late1, 2nd, 3rd. class_premium is the class's premium over the
historical future-first baseline as a fraction (0.385 = +38.5%). tier, when given, adds rookie-year
points from the points formula, reported separately from EV and never added to it.
All constants come from SKILL.md; change them there and here together.
"""
import json
import sys

HIT = {"early1_rb": 0.80, "early1": 0.65, "mid1": 0.50, "late1": 0.35, "2nd": 0.20, "3rd": 0.08}
STARTABILITY = {1: 0.75, 2: 0.85, 3: 0.93}  # 4+ is 1.00
SELL_PREMIUM = 0.25
BANDS = [(0.22, "Green"), (0.35, "Amber"), (float("inf"), "Locked")]
TARGET = {"contender": "< 12%", "rebuild": "25-35%"}
FIRSTS = {"early1_rb", "early1", "mid1", "late1"}

DEMO = {
    "target_seasons": 4, "teams": 10,
    "picks": [
        {"label": "1st (early, non-RB)", "slot": "early1", "chart": 7304, "class_premium": 0.385},
        {"label": "1st (mid)", "slot": "mid1", "chart": 5628, "class_premium": 0.175},
        {"label": "1st (mid)", "slot": "mid1", "chart": 5628, "class_premium": 0.175},
        {"label": "1st (late)", "slot": "late1", "chart": 4905, "class_premium": 0.11},
        {"label": "1st (late)", "slot": "late1", "chart": 4905, "class_premium": 0.11},
    ],
}


def startability(seasons):
    if seasons < 1:
        sys.exit("target_seasons must be 1 or more; a pick has no price without a target year")
    return STARTABILITY.get(seasons, 1.00)


def price(cfg):
    s = startability(cfg["target_seasons"])
    rows, flags = [], []
    for p in cfg["picks"]:
        if p["slot"] not in HIT:
            sys.exit(f"{p['label']}: unknown slot {p['slot']!r}; use one of {', '.join(HIT)}")
        hit = HIT[p["slot"]]
        frac = hit * s
        pts = max(0.0, (-14 + 3.7 * p["tier"]) * 0.75) if "tier" in p else None
        prem = p.get("class_premium")
        if prem is not None and prem > SELL_PREMIUM:
            flags.append(f"SELL candidate: {p['label']} class is +{prem:.1%} over baseline (trigger +{SELL_PREMIUM:.0%})")
        rows.append((p["label"], p["chart"], hit, s, frac, p["chart"] * frac, pts))
    firsts = [p for p in cfg["picks"] if p["slot"] in FIRSTS]
    if cfg.get("teams") == 10 and len(firsts) > 3:
        flags.append(f"Stack limit: {len(firsts)} firsts in a 10-team league; firsts 4+ go on the block")
    return s, rows, flags


def render(cfg):
    s, rows, flags = price(cfg)
    out = [f"Target: season {cfg['target_seasons']} after the draft (startability {s:.2f})", "",
           "| Pick | Chart | Hit rate | Startability | EV / chart | EV | Rookie pts |",
           "|---|---|---|---|---|---|---|"]
    for label, chart, hit, st, frac, ev, pts in rows:
        p = "" if pts is None else f"{pts:.0f}"
        out.append(f"| {label} | {chart:g} | {hit:.2f} | {st:.2f} | {frac:.2f} | {ev:.0f} | {p} |")
    hits = sum(r[2] for r in rows)
    out += ["", f"Expected hits: {hits:.2f} (sum of hit rates, never of chart values)"]
    total = cfg.get("roster_total_value")
    if total:
        share = sum(r[1] for r in rows) / total
        band = next(name for cap, name in BANDS if share < cap)
        tgt = TARGET.get(cfg.get("stance", ""), "contender < 12%, rebuild 25-35%")
        out.append(f"Pick value share: {share:.1%} ({band}); target {tgt}, never above 35%")
    out += [f"- {f}" for f in flags] or ["- No sell flags"]
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    cfg = DEMO if sys.argv[1] == "--demo" else json.load(open(sys.argv[1], encoding="utf-8"))
    print(render(cfg))
