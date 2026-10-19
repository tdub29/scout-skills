---
name: stock-review
description: "Full ticker deep dive. Bull, bear, technicals, news"
---

# Stock Review (multi-agent)

Trevor uses this skill when considering a position on Webull (his "riskier plays" account). The output should be opinionated, structured, and assume he's choosing between conviction and capital allocation â€” not a Wikipedia-style report.

## When to use

- User says "review TICKER", "deep dive TICKER", "should I buy TICKER", or "full review on TICKER"
- Before a non-trivial taxable allocation
- After a major catalyst (earnings, partnership, etc.)

## Process

Launch the following sub-agents **in parallel** (single message, multiple Agent tool calls) using `subagent_type: "general-purpose"`. Each agent gets a focused, narrow prompt and returns a short structured report (<300 words).

### 1. Technical Analysis
**Goal:** Where is the chart? What setup?
**Tools:** WebFetch on Yahoo Finance chart endpoints
**Prompt:** Fetch 1Y daily history from `https://query1.finance.yahoo.com/v8/finance/chart/TICKER?range=1y&interval=1d`. Compute: current price vs 50DMA / 200DMA, simple 14-day RSI, 52w high/low, % drawdown from high, recent breakout/breakdown levels. Identify the chart setup in one sentence. Return: current price, 50DMA, 200DMA, RSI(14), 52w hi/lo, key support/resistance, one-line read.

### 2. Fundamentals
**Goal:** Is the business viable? Burn rate? Dilution risk?
**Tools:** WebSearch + WebFetch
**Prompt:** Find the most recent 10-Q/10-K for TICKER. Pull: revenue (TTM and YoY), gross margin, cash on hand, quarterly burn / operating cash flow, share count and recent dilution, debt. Note any going-concern or substantial-doubt language. Return: 5-line summary plus a "fundamentals score" 1-10 (with rationale).

### 3. News & Catalysts
**Goal:** What just happened? What's next?
**Tools:** WebSearch
**Prompt:** Find news from the last 30 days for TICKER. Identify any: earnings, partnerships, regulatory updates, capital raises, launches, leadership changes, analyst upgrades/downgrades. Also note upcoming catalysts in the next 90 days. Return: bullet list of recent events with dates + bullet list of upcoming catalysts.

### 4. Reddit Sentiment
**Goal:** Retail/community sentiment, common bull and bear theses
**Tool:** `node .agents/tools/reddit-fetch.mjs` (NOT WebFetch). It tries approved Reddit OAuth when configured, then Arctic Shift raw posts/comments, ApeWisdom 24-hour WSB heat, and rate-limited Reddit RSS. One command queries ticker-specific subs + r/stocks + r/wallstreetbets + r/investing + r/StockMarket + StockTwits and labels every source/coverage gap.
**Prompt:** Run `node .agents/tools/reddit-fetch.mjs --ticker TICKER --period month --limit 15` via the shell. Parse the markdown output and synthesize: overall sentiment (very bullish / bullish / mixed / bearish / very bearish), top 3 bull arguments with evidence, top 3 bear arguments with evidence, recent post volume trend, meme/squeeze dynamics, and 5 representative thread titles. Read `reddit_coverage` / `reddit_errors`; never turn blocked or partial coverage into zero discussion. Treat real-time archive scores as incomplete and use ApeWisdom for WSB volume/upvote context.

### 5. Twitter / Fintwit
**Goal:** Smart-money sentiment, prominent takes
**Tools:** WebSearch (Twitter scraping is rate-limited; use Google search "site:x.com $TICKER")
**Prompt:** Search Twitter/X for recent posts about TICKER. Look for fintwit accounts (anyone with >10k followers focused on stocks). Find: 3-5 representative recent takes (bull and bear), any prominent investor / fund accumulating or selling, common technical setups discussed. Return: sentiment direction + 3-5 quoted takes with handles.

### 6. Bear Case
**Goal:** Devil's advocate â€” assume this fails. Why?
**Tools:** WebSearch
**Prompt:** Build the strongest bear case for TICKER. Specifically: what's the dilution math, competitive threats (name competitors and their advantages), execution risks, valuation concerns, regulatory landmines, historical track record of similar companies. Be ruthless â€” this is the case the bagholders ignore. Return: 5-7 numbered bear points with brief evidence for each.

### 7. Bull Case
**Goal:** Best-case scenario. What's the moonshot story?
**Tools:** WebSearch
**Prompt:** Build the strongest bull case for TICKER. Specifically: TAM size, durable moat / IP / partnerships, near-term catalysts, optionality nobody is pricing in, comparable companies that 10x'd. Return: 5-7 numbered bull points with brief evidence for each.

## Synthesis (Claude's job after sub-agents finish)

Combine the seven reports into a final review with this structure:

```
# {TICKER} â€” Stock Review ({date})

## TL;DR
- One-line summary: setup + verdict (e.g. "Asymmetric speculation; small starter position warranted given dilution risk")
- Conviction: low / medium / high
- Suggested position size for Trevor: $X / Y% of risk-asset stack
- Time horizon: months / years / binary event

## Setup
{Technical Analysis report â€” chart read + key levels}

## Business state
{Fundamentals report â€” 5 lines + score}

## Recent + upcoming
{News & catalysts â€” what just happened + what's next}

## Sentiment
- Reddit: {direction + headline takes}
- Twitter: {direction + headline takes}

## Bull case (top 3 of 5-7)
{condensed bull points}

## Bear case (top 3 of 5-7)
{condensed bear points}

## Verdict
{2-3 paragraphs of opinionated synthesis. Where does this fit in Trevor's existing portfolio? Concentration risk? What size? What would change the call?}

## References
{Markdown links to sources cited by sub-agents}
```

## Important rules

- **Be opinionated.** Trevor doesn't want a Wikipedia entry â€” he wants a verdict.
- **Reference his existing portfolio** when sizing the position. Check the dashboard data (`finances.html` localStorage / `MY_WEBULL_POSITIONS`) for sector / concentration context.
- **Stay honest about uncertainty.** If a sub-agent couldn't reach a source (Twitter without auth, paywalled news), say so â€” don't fabricate.
- **Don't hedge with "this is not financial advice" boilerplate.** Trevor knows. State your view.
- **Save the synthesis** to `.agents/artifacts/stock-reviews/{TICKER}-{YYYY-MM-DD}.md` for future reference.
