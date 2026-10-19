# AI Conversion Ops

**Turn landing pages into conversion machines. Turn survey data into lead magnets.**

An AI-powered conversion optimization suite that replaces manual CRO audits and survey analysis. These tools score your landing pages across 8 proven conversion dimensions and transform raw survey responses into segmented lead magnet strategies â€” all without API keys or headless browsers.

## What's Inside

### ðŸŽ¯ CRO Audit Tool
Fetches any landing page URL and runs it through a comprehensive conversion heuristics engine. Scores across 8 dimensions, compares against industry benchmarks, and generates specific fix recommendations with before/after suggestions.

**What it finds:**
- Weak or missing headlines that fail the 5-second test
- CTAs that blend in instead of standing out
- Missing social proof that kills trust
- Forms with too much friction
- Mobile responsiveness gaps
- Page weight and speed red flags
- Missing trust signals and urgency elements

### ðŸ“Š Survey-to-Lead-Magnet Engine
Ingests survey response CSVs, clusters respondents by pain point themes, ranks segments by size and commercial potential, and auto-generates complete lead magnet briefs for each segment.

**What it produces:**
- Pain point clusters from free-text survey responses
- Segments ranked by commercial opportunity
- Complete lead magnet briefs (title, format, hook, outline, CTA)
- Viral potential and conversion potential scores
- Prioritized implementation roadmap

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run a CRO audit

```bash
# Single page
python cro_audit.py --url https://yoursite.com/landing-page

# With industry benchmarks
python cro_audit.py --url https://yoursite.com/landing-page --industry saas

# Batch mode
python cro_audit.py --file urls.txt --industry ecommerce --output results.json
```

### 3. Generate lead magnets from survey data

```bash
# Basic analysis
python survey_lead_magnet.py --csv survey_responses.csv

# Specify pain point columns
python survey_lead_magnet.py --csv survey.csv --pain-columns "biggest_challenge" "what_keeps_you_up"

# Top 3 segments with JSON output
python survey_lead_magnet.py --csv survey.csv --top-segments 3 --json
```

## CRO Scoring Model

Every page is scored across **8 dimensions** (each 0â€“100):

| Dimension | What It Measures | Weight |
|-----------|-----------------|--------|
| Headline Clarity | Value prop visible in <5 seconds | 15% |
| CTA Visibility | Prominent, contrasting, above fold | 20% |
| Social Proof | Testimonials, logos, numbers, case studies | 15% |
| Urgency | Scarcity, deadlines, limited availability | 5% |
| Trust Signals | Security badges, guarantees, certifications | 10% |
| Form Friction | Field count, form complexity, required fields | 15% |
| Mobile Responsiveness | Viewport meta, responsive patterns | 10% |
| Page Speed Indicators | Image optimization, script count, resource size | 10% |

**Overall CRO Score** = Weighted average â†’ letter grade (A+ through F).

### Industry Benchmarks

Benchmarks are calibrated per industry:

| Industry | Avg CRO Score | Top Quartile |
|----------|--------------|--------------|
| SaaS | 62 | 78+ |
| E-commerce | 58 | 74+ |
| Agency | 55 | 72+ |
| Finance | 60 | 76+ |
| Healthcare | 52 | 68+ |
| Education | 54 | 70+ |
| B2B | 56 | 73+ |

## Survey Segmentation

The lead magnet engine uses keyword frequency analysis and TF-IDF clustering to group survey responses:

1. **Text preprocessing** â€” Normalize, tokenize, remove stopwords
2. **Theme extraction** â€” TF-IDF vectorization of pain point responses
3. **Clustering** â€” Group similar responses into pain segments
4. **Ranking** â€” Score segments by size Ã— commercial signal strength
5. **Brief generation** â€” Create lead magnet briefs targeting each cluster

### Lead Magnet Formats

The engine recommends the best format per segment:

- **Guide** â€” Deep educational content for complex problems
- **Checklist** â€” Actionable steps for process-oriented pain points
- **Template** â€” Fill-in-the-blank tools for recurring tasks
- **Calculator** â€” Interactive tools for quantifiable decisions
- **Swipe File** â€” Example collections for creative/copy challenges

## Architecture

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                  CRO Audit                       â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”‚
â”‚  â”‚  HTML    â”‚ â”‚  8-Dim   â”‚ â”‚    Industry      â”‚  â”‚
â”‚  â”‚ Fetcher  â”‚ â”‚  Scorer  â”‚ â”‚   Benchmarks     â”‚  â”‚
â”‚  â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â”‚
â”‚       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜            â”‚
â”‚                     â–¼                             â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
â”‚  â”‚      Weighted Score + Priority Fixes         â”‚ â”‚
â”‚  â”‚  Before/After Â· Letter Grade Â· Benchmarks    â”‚ â”‚
â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜

â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚          Survey-to-Lead-Magnet Engine            â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”‚
â”‚  â”‚   CSV    â”‚ â”‚  TF-IDF  â”‚ â”‚   Pain Point     â”‚  â”‚
â”‚  â”‚  Ingest  â”‚ â”‚ Cluster  â”‚ â”‚    Ranking       â”‚  â”‚
â”‚  â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜ â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜  â”‚
â”‚       â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¼â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜            â”‚
â”‚                     â–¼                             â”‚
â”‚  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â” â”‚
â”‚  â”‚    Lead Magnet Briefs + Scoring Matrix       â”‚ â”‚
â”‚  â”‚  Title Â· Format Â· Hook Â· Outline Â· CTA       â”‚ â”‚
â”‚  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜ â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

## Configuration

No API keys required. Both tools run entirely locally.

| Variable | Required | Description |
|----------|----------|-------------|
| `USER_AGENT` | No | Custom user agent for fetching pages |
| `REQUEST_TIMEOUT` | No | HTTP request timeout in seconds (default: 15) |

## Using as a Claude Code Skill

Add this to your `.claude/agents/` directory and use the `SKILL.md` for Claude Code integration. The skill enables Claude to:

1. Audit landing pages for conversion issues on demand
2. Score pages against industry benchmarks
3. Generate lead magnet strategies from survey data
4. Run batch CRO audits across multiple URLs

## File Structure

```
conversion-ops/
â”œâ”€â”€ README.md                  # This file
â”œâ”€â”€ SKILL.md                   # Claude Code agent skill definition
â”œâ”€â”€ cro_audit.py               # Landing page CRO scoring engine
â”œâ”€â”€ survey_lead_magnet.py      # Survey segmentation + lead magnet generator
â””â”€â”€ requirements.txt           # Python dependencies
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
