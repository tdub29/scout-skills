---
name: team-ops
description: "Team performance audits, meeting transcript actions"
---

# AI Team Ops

## Preamble (runs on skill start)

```bash
# Version check (silent if up to date)
python3 telemetry/version_check.py 2>/dev/null || true

# Telemetry opt-in (first run only, then remembers your choice)
python3 telemetry/telemetry_init.py 2>/dev/null || true
```

> **Privacy:** This skill logs usage locally to `~/.ai-marketing-skills/analytics/`. Remote telemetry is opt-in only. No code, file paths, or repo content is ever collected. See `telemetry/README.md`.

---

AI-powered team performance analysis and meeting intelligence: ruthless performance audits using the "Elon Algorithm" + automatic extraction of action items, decisions, and follow-ups from meeting transcripts.

## When to Use

Use this skill when:
- Evaluating team performance against OKRs/KPIs with a structured framework
- Stack ranking team members to identify A/B/C players
- Finding redundant roles, bottlenecks, and automation opportunities in your org
- Extracting action items and decisions from meeting transcripts
- Processing batch meeting notes into structured follow-up lists
- Pushing meeting action items to CRM (HubSpot) as tasks

## Tools

### Team Performance

| Script | Purpose | Key Command |
|--------|---------|-------------|
| `team_performance_audit.py` | Elon Algorithm: 5-step team audit + stack rank + scorecards | `python3 team_performance_audit.py --input team_data.json --output report.md` |

### Meeting Intelligence

| Script | Purpose | Key Command |
|--------|---------|-------------|
| `meeting_action_extractor.py` | Extract decisions, actions, follow-ups from transcripts | `python3 meeting_action_extractor.py --transcript meeting.txt --format markdown` |

## Configuration

All scripts use environment variables for LLM API access. Copy `.env.example` to `.env` and fill in your values.

### Required Environment Variables

- `ANTHROPIC_API_KEY` â€” Anthropic API key (Claude for analysis)
- `OPENAI_API_KEY` â€” OpenAI API key (alternative LLM provider)

### Optional Environment Variables

- `HUBSPOT_API_KEY` â€” HubSpot private app token (for pushing meeting action items as tasks)
- `LLM_PROVIDER` â€” `anthropic` (default) or `openai`
- `LLM_MODEL` â€” Model name override (default: `claude-sonnet-4-20250514` or `gpt-4o`)

## Data Flow

```
Role Descriptions + OKRs + Output Data (CSV/JSON)
        â”‚
        â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚   team_performance_audit.py      â”‚
â”‚   5-Step Elon Algorithm:         â”‚
â”‚   1. Question requirements       â”‚
â”‚   2. Delete redundancies         â”‚
â”‚   3. Simplify workflows          â”‚
â”‚   4. Accelerate bottlenecks      â”‚
â”‚   5. Automate what's possible    â”‚
â”‚                                  â”‚
â”‚   + Score: velocity, quality,    â”‚
â”‚     independence, initiative     â”‚
â”‚   + Stack rank: A/B/C players    â”‚
â”‚   + Actions: promote/coach/exit  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
        â”‚
        â–¼
Executive Summary + Individual Scorecards + Org Recommendations


Meeting Transcripts (text files or stdin)
        â”‚
        â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚   meeting_action_extractor.py    â”‚
â”‚   Extract:                       â”‚
â”‚   â€¢ Decisions (who + context)    â”‚
â”‚   â€¢ Action items (owner +        â”‚
â”‚     deadline + priority)         â”‚
â”‚   â€¢ Open questions               â”‚
â”‚   â€¢ Key insights / quotes        â”‚
â”‚   â€¢ Follow-up meetings needed    â”‚
â”‚   â€¢ Implicit commitments         â”‚
â”‚   + Confidence scores            â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
        â”‚
        â–¼
Structured JSON / Markdown + Optional CRM Push
```

## Dependencies

- Python 3.9+
- `anthropic` or `openai` (for LLM-powered analysis)
- `requests` (for optional HubSpot integration)
