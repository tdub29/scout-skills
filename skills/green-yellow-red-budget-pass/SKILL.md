---
name: green-yellow-red-budget-pass
description: Categorize transactions into green (income), yellow (wants/discretionary), and red (needs + investments + non-negotiables), then compute available margin, invest ammo, and surface yellow drift â€” yellow spending that has quietly become recurring. Pulls from Sure (the Rails finance app Trevor uses) or from a CSV export. Saves a markdown report to .agents/artifacts/budget-passes/. Use this whenever the user says "categorize my spending", "budget pass", "where is my money going", "green yellow red", "highlight my transactions", "find subscription drift", or otherwise wants a structured look at where cash is going over the last quarter. Also trigger when the user is preparing for the Wallet pillar of [[whole-wealth-audit]] or before a big financial decision (mortgage signing, offer evaluation).
---

# Green / Yellow / Red Budget Pass

A clean cut on the last 90 days of spending. The point isn't accounting â€” it's catching the yellow that has drifted into red-by-habit, and computing the real number Trevor can deploy into the asset class.

## When to use

- "Budget pass" / "categorize my spending" / "where is my money going"
- "Find subscription drift" / "what should I cancel"
- During the Wallet pillar of [[whole-wealth-audit]]
- Before signing the dual-residence mortgage or accepting an offer (need a clean read on real outflows)

## The model

Every transaction gets one color. Transfers between Trevor's own accounts are excluded (Sure already auto-matches these â€” see `Transfer` model in the codebase if needed).

| Color | What it is | Examples |
|---|---|---|
| ðŸŸ¢ Green | Income â€” money landing in the household | Salary, side income, refunds, interest, dividends |
| ðŸŸ¡ Yellow | Wants â€” discretionary, can be cut without pain | Restaurants, bars, streaming, gear, hobby stuff, travel-for-fun |
| ðŸ”´ Red | Needs + non-negotiables + scheduled investments | Rent/mortgage, utilities, insurance, debt service, tax, scheduled Roth/taxable contributions, groceries (real groceries), childcare-equivalent, medical |

**Edge calls â€” be explicit about which bucket they go in:**
- Groceries: red (food is a need), but flag if monthly grocery spend looks abnormally high â€” could be hiding yellow (Whole Foods specialty stuff)
- Subscriptions: default yellow, *unless* the subscription is genuinely load-bearing for income (e.g. a CRM that runs the side income â†’ red)
- Travel: yellow if for fun, red if for family/funeral/required work
- Gym: red (it's the Body pillar from [[whole-wealth-audit]])
- Therapy / coaching: red (Brain pillar)
- "Investments": *only* count as red if they're scheduled/automatic. Discretionary stock buys go in their own bucket (see below) â€” they're not yellow but they're also not a fixed cost.

**A fourth implicit bucket:** discretionary investments (buying a position on Webull, opportunistic crypto). Track these separately as "blue" in the report so the math stays clean. They're not consumption and they're not a fixed obligation.

## Getting the data

Try these in order:

### Option A: Sure database (preferred â€” Trevor's data lives here)

If the working directory is the Sure repo and Postgres is running:

```bash
bin/rails runner '
  start = 90.days.ago.to_date
  family = Family.first  # adjust if multiple families
  txns = family.transactions
               .joins(:entry)
               .where("entries.date >= ?", start)
               .includes(:category, :merchant, entry: :account)
  data = txns.map do |t|
    {
      date: t.entry.date,
      amount: t.entry.amount.to_f,
      account: t.entry.account.name,
      category: t.category&.name,
      merchant: t.merchant&.name,
      name: t.entry.name,
    }
  end
  require "csv"
  CSV.open("/tmp/budget_pass.csv", "w") do |csv|
    csv << data.first.keys
    data.each { |row| csv << row.values }
  end
  puts "Wrote #{data.size} rows to /tmp/budget_pass.csv"
'
```

Adjust `Family.first` if the install has multiple families. Sign convention reminder from `CLAUDE.md`: negative `amount` on a depository account = inflow (income); positive on credit card = a charge (outflow). Handle the sign per account classification when bucketing.

### Option B: CSV the user already exported

If the user hands you a CSV path, use it directly. Expect columns roughly like: `date, amount, account, category, merchant, name`. Don't assume sign convention â€” confirm with the user before treating positive vs. negative as income vs. expense.

### Option C: Ask

If neither works, ask the user to either run the Rails command or export a CSV from Sure. Don't fabricate a budget pass off of memory or guesses.

## The categorization pass

For each transaction, assign green / yellow / red / blue. Default mapping from Sure category names (case-insensitive, partial match OK):

```
GREEN:    "income", "salary", "paycheck", "refund", "interest", "dividend", "freelance", "consulting", "1099"
RED:      "rent", "mortgage", "utilities", "insurance", "loan", "debt", "tax", "irs",
          "grocery", "groceries", "gas", "fuel", "medical", "doctor", "dentist", "therapy",
          "gym", "fitness", "childcare", "tuition", "phone bill", "internet"
YELLOW:   "dining", "restaurants", "bars", "coffee", "entertainment", "streaming", "subscription",
          "shopping", "amazon", "clothing", "hobbies", "games", "travel" (and "vacation"),
          "gifts" (unless tagged "family")
BLUE:     "investment", "brokerage", "webull", "vanguard", "fidelity", "crypto" â€” only when the transaction
          is a buy/transfer-out from a cash account to a brokerage; exclude reinvested dividends
```

For transactions with no category or an ambiguous one, ask Trevor for a one-time call â€” don't silently default. Track those decisions and propose updating Sure's category mapping if the same merchant comes up repeatedly.

## Yellow drift detection

Yellow that has become habitual is the most valuable insight from this pass. A subscription Trevor signed up for in 2023 and hasn't thought about since is yellow by category but red by behavior.

After bucketing, run drift detection on yellow:
- Group yellow transactions by `merchant` (or `name` if merchant is null)
- For each merchant: count occurrences in the 90-day window
- Flag as "drifted" if: count â‰¥3 (i.e. monthly or more) **and** total â‰¥ $50 over the period

Sort drifted items by total spend, descending. These are the cancel-or-promote decisions: either acknowledge it's actually a red (load-bearing tool), or cancel it.

## The math

After bucketing:

```
green        = sum of green
red          = sum of red
yellow       = sum of yellow
blue         = sum of blue (discretionary investments)

available_margin    = green - red             # what's left after needs are covered
invest_ammo         = green - red - yellow    # what's actually being saved/invested
yellow_share        = yellow / green          # % of income going to wants
margin_consumption  = yellow / available_margin   # % of available margin eaten by wants
```

Annualize the 90-day figures (Ã—4) when reporting so the numbers map to mental models like "savings rate" and "annual deployable cash".

## Output format

Save to `.agents/artifacts/budget-passes/YYYY-MM-DD.md`:

```markdown
# Budget Pass â€” YYYY-MM-DD (last 90 days)

## Headline
- Income: $X (annualized $4X)
- Available margin (green âˆ’ red): $X
- Invest ammo (green âˆ’ red âˆ’ yellow): $X
- Yellow share of income: X%
- Margin consumption: X%
- Discretionary investments (blue): $X

**One-line read:** {e.g. "Margin is healthy at $X but 38% of it is being eaten by yellow â€” drift list below has $Y of obvious cuts."}

## Bucket totals
| Bucket | Total | Annualized | % of income |
|---|---|---|---|
| ðŸŸ¢ Green | $X | $4X | 100% |
| ðŸ”´ Red | $X | $4X | X% |
| ðŸŸ¡ Yellow | $X | $4X | X% |
| ðŸ”µ Blue (disc. invest) | $X | $4X | X% |

## Yellow drift â€” recurring wants that look habitual
| Merchant | Count | Total (90d) | Avg/mo | Action |
|---|---|---|---|---|
| ... | ... | $X | $X | cancel / keep / promote-to-red |

## Top 10 yellow line items (by spend)
| Date | Merchant | Amount | Category |
|---|---|---|---|

## Top 10 red line items (sanity check â€” is anything in here actually yellow?)
| Date | Merchant | Amount | Category |
|---|---|---|---|

## Ambiguous / asked Trevor
| Transaction | Resolved as | Note |
|---|---|---|

## Recommended actions
1. ...
2. ...
3. ...

## Delta vs. last pass
{If a previous file exists in `.agents/artifacts/budget-passes/`, compare invest_ammo, yellow_share, and the drift list.}
```

## Notes

- **Don't moralize.** Yellow isn't bad. Yellow that drifted into recurring is what we're hunting. A high invest_ammo with healthy yellow > a starvation budget with zero yellow.
- **Honor the Sure model.** Don't double-count Transfers (Sure already excludes them from income/expense rollups via the `Transfer` model). Don't classify a debt-payment transfer as red unless the destination is a Loan account.
- **One pass, not perfect.** First-pass categorization will have errors. Surface ambiguous items, ask, and propose a Sure category-rule update so the next pass is cleaner. Don't try to ship a "100% accurate" report â€” the action is more valuable than the polish.
- **Tie back to other skills.** When invoked as part of [[whole-wealth-audit]], feed the headline numbers into the Wallet pillar's data section rather than producing a standalone file.
