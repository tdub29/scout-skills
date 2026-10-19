# AI SEO Ops

**Find the keywords your competitors missed. Automatically.**

An AI-powered SEO operations suite that replaces the manual grind of keyword research, competitor analysis, content briefing, and trend detection. These tools pull data from Google Search Console, Ahrefs, and the open web to surface the exact opportunities your team should act on â€” ranked by impact, scored by confidence, and ready to execute.

## What's Inside

### ðŸŽ¯ Content Attack Brief Generator
Synthesizes your content footprint, Ahrefs keyword data, GSC performance, and competitor gaps into a weekly prioritized keyword brief. Scores every keyword on Impact Ã— Confidence and assigns an execution path (fully automated â†’ team-assisted â†’ expert-only).

**What it finds:**
- BOFU money keywords your competitors rank for but you don't
- Trending keywords surging before the competition notices
- Decaying pages losing traffic that need a refresh
- Outside-the-box content angles where you have unique authority

### ðŸ“Š GSC Keyword Optimizer
Pulls Google Search Console data and identifies "striking distance" keywords â€” queries where you rank positions 4â€“20 with decent impressions. These are your quick wins: small optimizations that can push you onto page one.

**What it does:**
- Finds keywords on the cusp of page one
- Calculates potential traffic gains from position improvements
- Identifies CTR underperformers (you rank well but nobody clicks)
- Groups related keywords for efficient optimization

### ðŸ”‘ GSC Client & Auth
A reusable Google Search Console API client with OAuth flow. Use it standalone or import it as a library in your own scripts.

**Features:**
- Top queries, pages, device splits, country splits
- Striking distance finder (positions 4â€“20)
- Query + page matrix for cannibalization analysis
- Daily trend tracking
- CLI and library modes

### ðŸ”¥ Trend Scout
Scans Google Trends, Hacker News, Reddit, and X/Twitter to find trending topics in your niche before they peak. Scores each trend for relevance to your content verticals and suggests content angles.

**Sources monitored:**
- Google Trends RSS (US)
- Hacker News (filtered for your niche)
- Reddit (configurable subreddits)
- X/Twitter (via Brave Search)
- YouTube competitor outlier detection

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env with your API keys and site configuration
```

### 3. Authenticate with Google Search Console

```bash
python gsc_auth.py
```

This opens a browser for OAuth consent. Your token is saved locally for subsequent use.

### 4. Run the tools

```bash
# Content Attack Brief â€” full keyword intelligence report
python content_attack_brief.py

# GSC Keyword Optimizer â€” find striking distance keywords
python gsc_client.py --striking --days 28

# GSC top queries
python gsc_client.py --queries 50 --days 28

# Trend Scout â€” find what's trending in your niche
python trend_scout.py
```

## Architecture

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚              Content Attack Brief                 â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”‚
â”‚  â”‚ Content  â”‚ â”‚  Ahrefs  â”‚ â”‚  Competitor Gap   â”‚  â”‚
â”‚  â”‚Fingerprintâ”‚ â”‚ Keywords â”‚ â”‚    Analysis       â”‚  â”‚
â”‚  â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â”‚
â”‚       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜            â”‚
â”‚                     â–¼                             â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
â”‚  â”‚       Impact Ã— Confidence Scoring            â”‚ â”‚
â”‚  â”‚  Volume Â· KD Â· CPC Â· Trend Â· Funnel Stage    â”‚ â”‚
â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
â”‚                     â”‚                             â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
â”‚  â”‚   GSC    â”‚ â”‚ Execution â”‚ â”‚   Trend Scout    â”‚ â”‚
â”‚  â”‚  Client  â”‚ â”‚  Pipeline â”‚ â”‚  (Google Trends  â”‚ â”‚
â”‚  â”‚          â”‚ â”‚           â”‚ â”‚   HN Â· Reddit)   â”‚ â”‚
â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

## Scoring Algorithm

Every keyword gets an **Impact** score (0â€“10) and a **Confidence** score (0â€“10). Priority = Impact Ã— Confidence.

### Impact factors:
| Signal | Score |
|--------|-------|
| Volume â‰¥ 10K | +3 |
| Volume â‰¥ 2K | +2 |
| Volume â‰¥ 500 | +1 |
| CPC â‰¥ $15 | +3 |
| CPC â‰¥ $5 | +2 |
| CPC â‰¥ $1 | +1 |
| BOFU intent | +2 |
| MOFU intent | +1 |
| Trend surging (>50%) | +2 |
| Trend rising (>20%) | +1 |

### Confidence factors:
| Signal | Score |
|--------|-------|
| KD â‰¤ 10 | +4 |
| KD â‰¤ 20 | +3 |
| KD â‰¤ 35 | +2 |
| KD â‰¤ 50 | +1 |
| Already ranking top 10 | +3 |
| Ranking 11â€“30 | +2 |
| Ranking 31â€“50 | +1 |
| Topic authority match | +2 |

## Funnel Classification

Keywords are auto-classified into funnel stages:

- **BOFU** (Bottom of Funnel): "agency", "services", "pricing", "best", "vs", "alternative", "hire"
- **MOFU** (Middle of Funnel): "how to", "guide", "strategy", "case study", "roi", "tutorial"
- **TOFU** (Top of Funnel): Everything else

Commercial/transactional intent from Ahrefs automatically promotes to BOFU.

## Trend Detection

The Trend Scout scores each trending topic against your configured content verticals:

- **High relevance (25pts each):** Exact matches to your core topics
- **Medium relevance (10pts each):** Related industry terms
- **Low relevance (5pts each):** Tangential business terms

Trends scoring â‰¥20 get surfaced with content angle suggestions and recommended platforms.

## Configuration

All configuration is via environment variables (see `.env.example`):

| Variable | Required | Description |
|----------|----------|-------------|
| `GSC_SITE_URL` | Yes | Your GSC property (e.g., `https://www.example.com/`) |
| `GSC_TOKEN_FILE` | No | Path to GSC OAuth token (default: `.gsc-token.json`) |
| `GOOGLE_CLIENT_ID` | Yes | Google OAuth client ID |
| `GOOGLE_CLIENT_SECRET` | Yes | Google OAuth client secret |
| `AHREFS_TOKEN` | No | Ahrefs API token (enables keyword data + competitor analysis) |
| `YOUR_DOMAIN` | Yes | Your root domain for organic keyword tracking |
| `COMPETITORS` | No | Comma-separated competitor domains |
| `CONTENT_VERTICALS` | No | Comma-separated topic verticals for trend scoring |
| `TREND_SUBREDDITS` | No | Comma-separated subreddit names to monitor |
| `BRAVE_API_KEY` | No | Brave Search API key (enables X/Twitter trend scanning) |
| `OUTPUT_DIR` | No | Where to save output files (default: `./output`) |

## Using as a Claude Code Skill

Add this to your `.claude/agents/` directory and use the `SKILL.md` for Claude Code integration. The skill enables Claude to:

1. Run keyword analysis on demand
2. Generate weekly content attack briefs
3. Find and prioritize quick-win keywords from GSC
4. Monitor trending topics and suggest content

## File Structure

```
seo-ops/
â”œâ”€â”€ README.md                  # This file
â”œâ”€â”€ SKILL.md                   # Claude Code agent skill definition
â”œâ”€â”€ content_attack_brief.py    # Full keyword intelligence pipeline
â”œâ”€â”€ gsc_client.py              # GSC API client (library + CLI)
â”œâ”€â”€ gsc_auth.py                # GSC OAuth setup flow
â”œâ”€â”€ trend_scout.py             # Multi-source trend detection
â”œâ”€â”€ requirements.txt           # Python dependencies
â””â”€â”€ .env.example               # Environment variable template
```

## License

MIT


---

<div align="center">

**ðŸ§  [Want these built and managed for you? â†’](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills)**

*This is how we build agents at [Single Brain](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) for our clients.*

[Single Grain](https://www.singlegrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) Â· our marketing agency

ðŸ“¬ **[Level up your marketing with 14,000+ marketers and founders â†’](https://levelingup.beehiiv.com/subscribe)** *(free)*

</div>
