"""Score a weighted decision matrix so the totals row is computed, never typed.

usage: python score_matrix.py matrix.json
       python score_matrix.py --demo

matrix.json:
{
  "criteria": [{"name": "Cost", "weight": 30}, {"name": "Speed", "weight": 50}, {"name": "Risk", "weight": 20}],
  "options": {"Option 1": [8, 5, 7], "Option 2": [6, 9, 7], "Option 3": [7, 7, 9]}
}

Weights may be percents or fractions; they are normalised to sum to 1. Scores are 1-10, one per
criterion, in criteria order. Prints the markdown matrix with a computed Total row and the ranking.
"""
import json
import sys

DEMO = {
    "criteria": [{"name": "[Factor 1]", "weight": 30}, {"name": "[Factor 2]", "weight": 50},
                 {"name": "[Factor 3]", "weight": 20}],
    "options": {"Option 1": [8, 5, 7], "Option 2": [6, 9, 7], "Option 3": [7, 7, 9]},
}


def score(m):
    weights = [c["weight"] for c in m["criteria"]]
    total_w = sum(weights)
    if total_w <= 0:
        sys.exit("weights must sum to more than 0")
    totals = {}
    for name, scores in m["options"].items():
        if len(scores) != len(weights):
            sys.exit(f"{name}: {len(scores)} scores for {len(weights)} criteria")
        totals[name] = sum(w * s for w, s in zip(weights, scores)) / total_w
    return weights, total_w, totals


def render(m):
    weights, total_w, totals = score(m)
    names = list(m["options"])
    lines = ["| Criteria | Weight | " + " | ".join(names) + " |",
             "|" + "---|" * (len(names) + 2)]
    for i, c in enumerate(m["criteria"]):
        pct = f"{100 * c['weight'] / total_w:g}%"
        lines.append(f"| {c['name']} | {pct} | " + " | ".join(str(m["options"][n][i]) for n in names) + " |")
    lines.append("| **Total** | | " + " | ".join(f"**{totals[n]:.2f}**" for n in names) + " |")
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    lines += ["", "Ranking: " + ", ".join(f"{n} {t:.2f}" for n, t in ranked)]
    if len(ranked) > 1 and round(ranked[0][1] - ranked[1][1], 6) < 0.3:
        lines.append(f"Close call: top two are {ranked[0][1] - ranked[1][1]:.2f} apart; test the weights before deciding.")
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    m = DEMO if sys.argv[1] == "--demo" else json.load(open(sys.argv[1], encoding="utf-8"))
    print(render(m))
