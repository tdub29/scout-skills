# AI Outbound Engine

From ICP definition to emails in inbox â€” fully automated cold outbound.

This skill category handles the complete cold outbound pipeline: defining your ideal customer profile, writing expert-scored email sequences, sourcing and verifying leads, deduplicating against existing campaigns, uploading to your email platform, and monitoring the competitive landscape.

## What's Inside

### ðŸŽ¯ Cold Outbound Optimizer (`SKILL.md`)
Full campaign design workflow:
- **ICP Definition** â€” structured template to define exactly who you're targeting
- **Infrastructure Audit** â€” pulls sending account inventory, warmup scores, and capacity math from Instantly
- **Expert Panel Scoring** â€” 10 simulated outbound experts score your copy (recursive until 90+/100)
- **Sequence Copywriting** â€” subject lines, body copy, follow-ups, breakup emails â€” all Instantly-ready
- **Capacity Planning** â€” accounts Ã— daily limits = pipeline projections
- **Implementation Docs** â€” step-by-step launch plan

Supports both "start from scratch" and "optimize existing campaigns" modes.

### ðŸ“¥ Lead Pipeline (`scripts/lead-pipeline.py`)
End-to-end lead sourcing:
1. **Apollo People Search** â€” pull leads matching your ICP criteria
2. **LeadMagic Verification** â€” validate every email before sending
3. **Deduplication** â€” check against existing Instantly leads + exclusion lists
4. **Upload to Instantly** â€” batch upload with rate limiting and retry logic

### ðŸ” Competitive Monitor (`scripts/competitive-monitor.py`)
Track competitors automatically:
- Pricing page change detection (diff-based)
- Blog post monitoring for recent content
- Generates weekly competitive intelligence reports
- Configurable competitor list â€” add any company you want to track

### ðŸ”— Cross-Signal Detector (`scripts/cross-signal-detector.py`)
Find overlapping signals across multiple data sources:
- Company overlap across SEO, sales, and outbound data
- Vertical alignment detection
- Keyword cluster correlation
- Confidence-scored recommendations for coordinated action

### ðŸ“§ Cold Outbound Sender (`scripts/cold-outbound-sender.py`)
Sends approved outbound emails:
- Reads from an approved prospects JSON file
- Daily send limits (configurable)
- Full send history tracking
- Dry-run mode for testing

### ðŸ”§ Instantly Audit (`scripts/instantly-audit.py`)
Pull campaign health data from the Instantly v2 API:
- Sending account inventory and warmup scores
- Campaign performance (open rate, reply rate, positive reply rate)
- Capacity math (conservative vs aggressive projections)
- Flags: low warmup scores, underperforming campaigns, blockers

## Quick Start

### 1. Set Up Environment Variables

```bash
cp .env.example .env
# Fill in your API keys
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Lead Pipeline

```bash
python3 scripts/lead-pipeline.py \
  --titles "VP Marketing,CMO,Head of Growth" \
  --industries "SaaS,Marketing" \
  --company-size "11,50" \
  --locations "United States" \
  --campaign-id "YOUR_CAMPAIGN_UUID" \
  --volume 500 \
  --dry-run
```

### 4. Audit Your Instantly Account

```bash
python3 scripts/instantly-audit.py --output report.md
```

### 5. Monitor Competitors

```bash
python3 scripts/competitive-monitor.py --output report.md
```

### 6. Detect Cross-Signals

```bash
python3 scripts/cross-signal-detector.py \
  --data-dir ./data/agent-outputs \
  --output cross-signals.json
```

## Architecture

```
ICP Definition
     â”‚
     â–¼
Expert Panel Scoring (recursive â†’ 90+)
     â”‚
     â–¼
Apollo Search â†’ LeadMagic Verify â†’ Dedupe â†’ Instantly Upload
     â”‚                                            â”‚
     â–¼                                            â–¼
Competitive Monitor â—„â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â–º Cross-Signal Detector
     â”‚
     â–¼
Weekly Intelligence Report
```

## File Structure

```
outbound-engine/
â”œâ”€â”€ README.md                           # This file
â”œâ”€â”€ SKILL.md                            # Claude Code skill definition
â”œâ”€â”€ .env.example                        # Environment variable template
â”œâ”€â”€ requirements.txt                    # Python dependencies
â”œâ”€â”€ scripts/
â”‚   â”œâ”€â”€ lead-pipeline.py                # Apollo â†’ LeadMagic â†’ Dedupe â†’ Instantly
â”‚   â”œâ”€â”€ instantly-audit.py              # Instantly account health check
â”‚   â”œâ”€â”€ competitive-monitor.py          # Competitor tracking
â”‚   â”œâ”€â”€ cross-signal-detector.py        # Multi-source signal detection
â”‚   â””â”€â”€ cold-outbound-sender.py         # Send approved outbound emails
â””â”€â”€ references/
    â”œâ”€â”€ expert-panel.md                 # Default 10-expert scoring roster
    â”œâ”€â”€ copy-rules.md                   # Cold email copywriting rules
    â”œâ”€â”€ icp-template.md                 # ICP data collection template
    â””â”€â”€ instantly-rules.md              # Instantly variable syntax & deliverability rules
```

## Requirements

- Python 3.9+
- API keys: Apollo, LeadMagic, Instantly (see `.env.example`)
- For the sender script: a configured email sending tool (e.g., `gog` CLI or SMTP)
- Claude Code or similar AI coding agent (for running the SKILL.md workflow)

## Customization

- **ICP**: Edit `references/icp-template.md` or provide parameters at runtime
- **Expert Panel**: Swap panelists in `references/expert-panel.md` for your industry
- **Competitors**: Configure the `COMPETITORS` dict in `competitive-monitor.py`
- **Send limits**: Adjust `MAX_PER_DAY` in `cold-outbound-sender.py`
- **Data sources**: Point `cross-signal-detector.py` at your own data directories

## License

MIT


---

<div align="center">

**ðŸ§  [Want these built and managed for you? â†’](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills)**

*This is how we build agents at [Single Brain](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) for our clients.*

[Single Grain](https://www.singlegrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) Â· our marketing agency

ðŸ“¬ **[Level up your marketing with 14,000+ marketers and founders â†’](https://levelingup.beehiiv.com/subscribe)** *(free)*

</div>
