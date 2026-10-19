# ðŸ“Š AI Revenue Intelligence

> **Prove content ROI, extract call intelligence, and generate client reports â€” automatically.**

An AI-powered revenue intelligence suite that connects the dots between sales calls, content performance, and closed deals. These tools pull from Gong, GA4, HubSpot, and Ahrefs to answer the questions every marketing team hates: "What content actually drove revenue?" and "What are prospects really saying on calls?"

Built in production at [Single Grain](https://www.singlegrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills). Now open-sourced for any revenue-focused marketing team.

---

## Architecture

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                        DATA SOURCES                                 â”‚
â”‚                                                                     â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”‚
â”‚  â”‚   Gong    â”‚  â”‚   GA4    â”‚  â”‚ HubSpot  â”‚  â”‚     Ahrefs       â”‚   â”‚
â”‚  â”‚  (calls)  â”‚  â”‚(traffic) â”‚  â”‚ (deals)  â”‚  â”‚    (SEO)         â”‚   â”‚
â”‚  â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
         â”‚              â”‚             â”‚                â”‚
         â–¼              â”‚             â”‚                â”‚
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”‚             â”‚                â”‚
â”‚  Gong-to-Insight â”‚    â”‚             â”‚                â”‚
â”‚    Pipeline      â”‚    â”‚             â”‚                â”‚
â”‚                  â”‚    â”‚             â”‚                â”‚
â”‚ â€¢ Objections     â”‚    â”‚             â”‚                â”‚
â”‚ â€¢ Buying signals â”‚    â”‚             â”‚                â”‚
â”‚ â€¢ Competitors    â”‚    â”‚             â”‚                â”‚
â”‚ â€¢ Content topics â”‚    â”‚             â”‚                â”‚
â”‚ â€¢ Follow-ups     â”‚    â”‚             â”‚                â”‚
â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â”‚             â”‚                â”‚
       â”‚                â–¼             â–¼                â”‚
       â”‚      â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”            â”‚
       â”‚      â”‚   Revenue Attribution     â”‚            â”‚
       â”‚      â”‚       Mapper              â”‚            â”‚
       â”‚      â”‚                           â”‚            â”‚
       â”‚      â”‚ â€¢ First-touch / linear /  â”‚            â”‚
       â”‚      â”‚   time-decay attribution  â”‚            â”‚
       â”‚      â”‚ â€¢ Content ROI by type     â”‚            â”‚
       â”‚      â”‚ â€¢ CPA calculations        â”‚            â”‚
       â”‚      â”‚ â€¢ Content gap analysis    â”‚            â”‚
       â”‚      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜            â”‚
       â”‚                  â”‚                            â”‚
       â–¼                  â–¼                            â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚              Client Report Generator                         â”‚
â”‚                                                              â”‚
â”‚  Executive Summary + Traffic + Pipeline + SEO + Call Quality â”‚
â”‚  Anomaly Detection + Period-over-Period Comparison           â”‚
â”‚  â†’ Markdown or JSON output                                   â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## Tools

### 1. ðŸŽ™ï¸ Gong-to-Insight Pipeline (`gong_insight_pipeline.py`)

Turns sales call transcripts into structured intelligence. Works with the Gong API or plain `.txt` transcript files.

**What it extracts:**
- **Objections** â€” categorized as pricing, timing, competition, authority, or need
- **Buying signals** â€” budget confirmed, timeline mentioned, decision maker engaged, champion identified
- **Competitive mentions** â€” which competitors were named and in what sentiment (positive/negative/neutral)
- **Pricing discussions** â€” dollar amounts, pricing model questions, ROI concerns
- **Content topics** â€” recurring objection patterns that should become blog posts, case studies, or battle cards
- **Follow-up drafts** â€” personalized outbound suggestions based on what happened on the call

```bash
# Analyze a transcript file
python gong_insight_pipeline.py --file transcript.txt

# Analyze a directory of transcripts
python gong_insight_pipeline.py --dir ./transcripts/ --content-topics

# Pull from Gong API (last 7 days)
python gong_insight_pipeline.py --gong --days 7

# Full output with follow-ups
python gong_insight_pipeline.py --file call.txt --follow-ups --output insights.json

# Example output:
# ============================================================
#   Call: discovery-call-acme
#   Temperature: WARM
# ============================================================
#
#   ðŸš« Objections (3):
#      pricing: 2
#      timing: 1
#      â†’ [pricing] "That's a bit more than we budgeted for this quarter"
#      â†’ [pricing] "Can you do a smaller pilot first?"
#      â†’ [timing] "We're in the middle of a platform migration"
#
#   âœ… Buying Signals (2):
#      budget_confirmed: 1
#      champion_identified: 1
#
#   âš”ï¸  Competitors: HubSpot, Drift
#
#   ðŸ’° Pricing discussed: Yes (3 mentions)
```

### 2. ðŸ’° Revenue Attribution Mapper (`revenue_attribution.py`)

The "prove content ROI" tool. Maps blog posts, videos, podcasts, and webinars to actual closed deals using first-touch, linear, or time-decay attribution models.

**What it produces:**
- Content-to-revenue mapping showing exactly which pieces drove pipeline
- Attribution across three models (pick the one that fits your sales motion)
- Cost-per-acquisition by content type (blog vs. video vs. webinar vs. podcast)
- Content gap analysis (which funnel stages have no content working?)
- Top performers ranked by attributed revenue

```bash
# Full attribution report (linear model)
python revenue_attribution.py --report

# Time-decay model (more credit to recent touchpoints)
python revenue_attribution.py --report --model time-decay

# Content gaps (which funnel stages are uncovered?)
python revenue_attribution.py --gaps

# CPA by content type
python revenue_attribution.py --cpa --costs content_costs.json

# Example output:
# ======================================================================
#   CONTENT REVENUE ATTRIBUTION REPORT
#   Model: linear
# ======================================================================
#
#   ðŸ“Š Summary
#      Total Revenue:          $984,000
#      Total Deals:            5
#      Avg Deal Size:          $196,800
#      Content w/ Attribution: 13
#      Avg Touchpoints/Deal:   4.4
#
#   ðŸ“ˆ Revenue by Content Type
#   Type             Revenue    Sessions   Pieces   Avg/Piece
#   --------------------------------------------------------
#   landing_page    $211,200     1,800        1    $211,200
#   blog            $298,560    17,000        6     $49,760
#   case_study      $156,000     2,090        2     $78,000
#   ...
```

### 3. ðŸ“‹ Multi-Source Client Report Generator (`client_report_generator.py`)

Pulls from all four data sources (GA4, HubSpot, Ahrefs, Gong) and generates a unified, client-ready BI report with an auto-generated executive summary and optional anomaly detection.

**What it includes:**
- **Executive summary** â€” auto-generated highlights, concerns, and recommendations
- **Traffic** â€” sessions, users, conversions, channel breakdown, top pages (GA4)
- **Pipeline** â€” deals created/won/lost, revenue, win rate, avg cycle (HubSpot)
- **SEO** â€” domain rating, rankings, backlinks, organic traffic (Ahrefs)
- **Call quality** â€” talk ratio, call duration, next-steps rate, top topics (Gong)
- **Anomaly detection** â€” flags unusual changes with severity levels
- **Period comparison** â€” month-over-month, quarter-over-quarter, or year-over-year

```bash
# Console summary
python client_report_generator.py --client "Acme Corp"

# Full markdown report
python client_report_generator.py --client "Acme Corp" --format markdown --output report.md

# JSON for dashboards/slides
python client_report_generator.py --client "Acme Corp" --format json --anomalies

# Skip sources you don't use
python client_report_generator.py --client "Acme Corp" --skip gong,ahrefs

# Example output:
# ======================================================================
#   Acme Corp - Performance Report
#   2025-03-01 to 2025-03-31
# ======================================================================
#
#   ðŸŸ¢ Overall: Strong
#
#   âœ… Highlights:
#      â€¢ Traffic up 8.1% (45,200 sessions)
#      â€¢ Conversions up 14.8% (342 total)
#      â€¢ Win rate at 60.0% (12 won)
#      â€¢ $1,440,000 revenue closed
#
#   âš ï¸  Concerns:
#      â€¢ Reps talking too much (54.2% talk ratio)
```

---

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Test with sample data

All tools ship with built-in sample data and fall back gracefully when API keys aren't configured. Try them out of the box:

```bash
# Analyze a transcript
echo "Prospect: That's more than we budgeted for this quarter.
Rep: I understand. What range were you expecting?
Prospect: We were looking at HubSpot too, they quoted us around 50k.
Rep: Makes sense. Our ROI calculator shows 3x return in year one." > sample.txt

python gong_insight_pipeline.py --file sample.txt --follow-ups

# Run attribution report (uses sample data without API keys)
python revenue_attribution.py --report --gaps

# Generate client report (uses sample data without API keys)
python client_report_generator.py --client "Demo Corp" --anomalies
```

### 4. Connect real APIs

Set these environment variables to connect live data:

```bash
# Gong
export GONG_API_KEY="your-gong-api-key"

# GA4
export GA4_PROPERTY_ID="123456789"
export GA4_CREDENTIALS_JSON="/path/to/service-account.json"

# HubSpot
export HUBSPOT_API_KEY="your-hubspot-private-app-token"

# Ahrefs
export AHREFS_TOKEN="your-ahrefs-api-token"
```

---

## Configuration

| Variable | Required By | Description |
|----------|-------------|-------------|
| `GONG_API_KEY` | Gong Pipeline, Client Report | Gong API access key |
| `GONG_API_BASE_URL` | Gong Pipeline, Client Report | Gong API URL (default: `https://api.gong.io/v2`) |
| `GA4_PROPERTY_ID` | Attribution, Client Report | GA4 property ID |
| `GA4_CREDENTIALS_JSON` | Attribution, Client Report | Path to GA4 service account JSON |
| `HUBSPOT_API_KEY` | Attribution, Client Report | HubSpot private app token |
| `AHREFS_TOKEN` | Client Report | Ahrefs API token |
| `YOUR_DOMAIN` | Client Report | Your root domain for Ahrefs data |
| `OUTPUT_DIR` | All | Output directory (default: `./output`) |

---

## Customization

### Objection Patterns
Edit `OBJECTION_PATTERNS` in `gong_insight_pipeline.py` to match your industry's objection language.

### Competitor List
Edit `KNOWN_COMPETITORS` in `gong_insight_pipeline.py` with your actual competitive landscape.

### Content Type Classification
Edit `CONTENT_TYPE_PATTERNS` in `revenue_attribution.py` to match your site's URL structure.

### Anomaly Thresholds
Pass custom thresholds to `detect_anomalies()` in `client_report_generator.py`:
```python
thresholds = {"warning": 0.15, "critical": 0.30}  # 15% = warning, 30% = critical
```

---

## How They Work Together

1. **Weekly**: Run `gong_insight_pipeline.py` on recent calls â†’ extract objections and buying signals
2. **Monthly**: Run `revenue_attribution.py` â†’ see which content drove deals
3. **Monthly**: Run `client_report_generator.py` â†’ deliver unified report to clients or leadership
4. **Quarterly**: Use Gong content topics + attribution gaps to plan next quarter's content

The insight loop:
- Gong reveals what prospects ask about â†’ creates content topics
- Content gets published â†’ drives traffic (GA4)
- Traffic converts to pipeline â†’ deals close (HubSpot)
- Attribution mapper proves which content worked â†’ invest more in winners
- Repeat

---

## File Structure

```
revenue-intelligence/
â”œâ”€â”€ README.md                       # This file
â”œâ”€â”€ SKILL.md                        # Claude Code agent skill definition
â”œâ”€â”€ requirements.txt                # Python dependencies
â”œâ”€â”€ gong_insight_pipeline.py        # Call transcript â†’ structured insights
â”œâ”€â”€ revenue_attribution.py          # Content â†’ revenue mapping
â””â”€â”€ client_report_generator.py      # Multi-source client BI reports
```

---

<div align="center">

**ðŸ§  [Want these built and managed for you? â†’](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills)**

*This is how we build agents at [Single Brain](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) for our clients.*

[Single Grain](https://www.singlegrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) Â· our marketing agency

ðŸ“¬ **[Level up your marketing with 14,000+ marketers and founders â†’](https://levelingup.beehiiv.com/subscribe)** *(free)*

</div>
