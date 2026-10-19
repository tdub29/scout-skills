# ðŸ§¬ Growth Engine

**What if your marketing experiments ran themselves?**

Autonomous growth experimentation for AI agents. Inspired by [Karpathy's autoresearch](https://x.com/karpathy/status/1886192184808149383) pattern applied to marketing: create experiments with hypotheses, collect data, run statistical analysis, auto-promote winners to a living playbook, and suggest what to test next.

Your AI agents stop guessing and start *knowing* what works.

---

## What You Get

- **ðŸ”¬ Experiment Engine** â€” Create A/B or batch (up to 10 variants) experiments with hypotheses, track them, and let the math decide winners
- **ðŸ“Š Bootstrap CI + Mann-Whitney U** â€” Real statistical rigor, not vibes. Non-parametric tests that work with small samples and non-normal distributions
- **ðŸ“– Auto-Playbook** â€” Winners automatically promote to a living playbook of empirically proven best practices
- **ðŸ’¡ Next-Experiment Suggestions** â€” The system knows what you haven't tested yet and suggests what to run next
- **ðŸ“ˆ Weekly Scorecard** â€” Automated report across all channels: wins, trends, running experiments, discards
- **âš ï¸ Pacing Alerts** â€” Monitor campaign health, lead staging rates, and candidate pipelines against targets

---

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set environment variables

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Run your first experiment

```bash
# Create an experiment
python3 experiment-engine.py create \
  --agent content \
  --hypothesis "Thread posts get 2x impressions vs single posts" \
  --variable "format" \
  --variants '["thread", "single"]' \
  --metric "impressions" \
  --cycle-hours 8

# Log data as it comes in
python3 experiment-engine.py log \
  --agent content \
  --experiment-id EXP-CONTENT-001 \
  --variant "thread" \
  --metrics '{"impressions": 4500, "clicks": 120, "replies": 8}'

# Score when you have enough data
python3 experiment-engine.py score \
  --agent content \
  --experiment-id EXP-CONTENT-001

# Check your playbook of proven winners
python3 experiment-engine.py playbook --agent content

# What should you test next?
python3 experiment-engine.py suggest --agent content
```

---

## Commands

### experiment-engine.py

The core engine. Manages the full experiment lifecycle.

| Command | Description |
|---------|-------------|
| `create` | Create a new A/B or batch experiment with a hypothesis |
| `log` | Log a data point (metrics) for a running experiment variant |
| `score` | Run statistical analysis. Auto-promotes winners to playbook |
| `list` | List experiments by agent, optionally filtered by status |
| `playbook` | Show the living playbook of empirically proven best practices |
| `suggest` | Suggest untested variables to experiment on next |

**Batch mode** â€” test up to 10 variants simultaneously:

```bash
python3 experiment-engine.py create \
  --agent email \
  --hypothesis "Which subject line style drives highest open rate?" \
  --variable "subject_line_style" \
  --variants '["question", "number", "how-to", "curiosity-gap", "personalized"]' \
  --metric "open_rate" \
  --batch-mode
```

### autogrowth-weekly-scorecard.py

Generates a weekly report across all agents/channels.

```bash
# Current week scorecard
python3 autogrowth-weekly-scorecard.py

# Two weeks ago
python3 autogrowth-weekly-scorecard.py --weeks 2

# Save to file
python3 autogrowth-weekly-scorecard.py --output reports/week-12.md
```

### pacing-alert.py

Monitors campaign health and pacing against targets.

```bash
# Formatted text output
python3 pacing-alert.py

# JSON output for integrations
python3 pacing-alert.py --json
```

---

## Example Output

### Experiment Scoring

```
ðŸ† EXP-CONTENT-003: KEEP â€” 'thread' +23.4% lift (p=0.0312, 95% CI [8.2, 41.7]%)
   ðŸ“– Playbook updated: format â†’ 'thread'
```

### Playbook

```
ðŸ“– CONTENT PLAYBOOK â€” Empirically Proven Best Practices

  format: 'thread' (+23.4% on impressions, p=0.0312, 95% CI [8.2, 41.7])
    Source: EXP-CONTENT-003 | Promoted: 2026-03-15

  hook_style: 'contrarian' (+18.7% on clicks, p=0.0421, 95% CI [5.1, 34.2])
    Source: EXP-CONTENT-007 | Promoted: 2026-03-22
```

### Weekly Scorecard

```
# AutoGrowth Weekly Scorecard â€” Week of Mar 17 â€“ Mar 23, 2026

## Summary
- Total experiments active: 4
- New experiments launched: 2
- Experiments completed: 3 (2 kept, 1 discarded)
- Total data points collected: 847

## ðŸ† Big Wins (keep status this week)
### EXP-EMAIL-012 (email)
- Tested: subject_line_style â†’ variant: question
- Metric value: 0.3420 | Sample n: 156
- Lift: 31.2% | p-value: 0.008

## ðŸ“ˆ Trending (watch these)
- EXP-CONTENT-015 (content) â€” variant `data_hook` leading at 0.1250 | 42 samples so far
```

### Pacing Alert

```
âš ï¸ Pacing Alert â€” Thu Mar 27 2:15 PM PDT

ðŸŸ¢ ðŸ“§ Outbound Pipeline:
â€¢ 12 leads staged today | 8 approved | 6 sent
â€¢ Campaigns: ðŸŸ¢ 3/3 sending | 450 emails/day

ðŸŸ¡ ðŸ” Recruiting Pipeline:
â€¢ 5 candidates added today | 187 this week | target: 400/week
â€¢ Campaigns: ðŸŸ¢ 5/5 sending | 200 emails/day
```

---

## How It Works

### The Autoresearch Loop

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                                             â”‚
â”‚   1. HYPOTHESIZE                            â”‚
â”‚      "Thread posts get 2x impressions"      â”‚
â”‚                        â”‚                    â”‚
â”‚                        â–¼                    â”‚
â”‚   2. EXPERIMENT                             â”‚
â”‚      Run variants, collect data points      â”‚
â”‚                        â”‚                    â”‚
â”‚                        â–¼                    â”‚
â”‚   3. ANALYZE                                â”‚
â”‚      Bootstrap CI + Mann-Whitney U          â”‚
â”‚      p < 0.05 + lift â‰¥ 15% = winner        â”‚
â”‚                        â”‚                    â”‚
â”‚                        â–¼                    â”‚
â”‚   4. PROMOTE or DISCARD                     â”‚
â”‚      Winner â†’ playbook (auto)              â”‚
â”‚      Loser â†’ discard pile (learned)        â”‚
â”‚                        â”‚                    â”‚
â”‚                        â–¼                    â”‚
â”‚   5. SUGGEST NEXT                           â”‚
â”‚      System identifies untested variables   â”‚
â”‚      â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ loops back to 1 â”€â”€â”€â”€â”€â”˜  â”‚
â”‚                                             â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### Statistical Methods

- **Mann-Whitney U test** â€” Non-parametric. Works with small samples. No normality assumption needed.
- **Bootstrap confidence intervals** â€” 1,000 resamples to estimate the true lift range.
- **Dual threshold** â€” Both statistical significance (p < 0.05) AND practical significance (â‰¥15% lift) required to declare a winner. No more "statistically significant but useless" results.
- **Trending detection** â€” Early signal detection at p < 0.10 with 15+ samples, so you know what's promising before it's conclusive.

### Configurable Thresholds

| Parameter | Default | What It Controls |
|-----------|---------|-----------------|
| `P_WINNER` | 0.05 | p-value threshold for declaring a winner |
| `P_TREND` | 0.10 | p-value threshold for "trending" status |
| `LIFT_WIN` | 15.0% | Minimum lift required for "keep" decision |
| `BOOTSTRAP_ITERATIONS` | 1000 | Number of bootstrap resamples for CI |

---

## Configuration

All configuration is via environment variables. See `.env.example` for the full list.

### Core Settings

| Variable | Description | Default |
|----------|-------------|---------|
| `GROWTH_ENGINE_DATA_DIR` | Where experiment data is stored | `./data/experiments` |
| `GROWTH_ENGINE_AGENTS` | Comma-separated list of agent names | `content,email,linkedin,seo,blog` |
| `HIGH_VOLUME_AGENTS` | Agents with fast data (fewer samples needed) | `content,email` |
| `LOW_VOLUME_AGENTS` | Agents with slow data (more samples needed) | `seo,linkedin,blog` |

### Pacing Alert Settings

| Variable | Description | Default |
|----------|-------------|---------|
| `PIPELINE_API_URL` | Your pipeline/CRM API endpoint | â€” |
| `PIPELINE_AUTH_TOKEN` | Bearer token for pipeline API | â€” |
| `EMAIL_API_URL` | Email platform API base URL | â€” |
| `EMAIL_AUTH_TOKEN` | Bearer token for email platform | â€” |
| `OUTBOUND_CAMPAIGNS` | JSON map of campaign name â†’ ID | `{}` |
| `DAILY_LEAD_TARGET` | Minimum leads staged per day | `10` |
| `WEEKLY_CANDIDATE_TARGET` | Candidate sourcing weekly target | `400` |

---

## Integrating with Your AI Agents

The growth engine is designed to be called by AI agents (Claude Code, GPT, etc.) as part of their workflow:

```python
# In your agent's post-publishing hook:
import subprocess

# After publishing a social post, log the experiment data
subprocess.run([
    "python3", "experiment-engine.py", "log",
    "--agent", "content",
    "--experiment-id", current_experiment_id,
    "--variant", variant_used,
    "--metrics", json.dumps({"impressions": post_impressions, "clicks": post_clicks})
])

# Periodically score experiments
subprocess.run([
    "python3", "experiment-engine.py", "score",
    "--agent", "content",
    "--experiment-id", current_experiment_id
])

# Before creating new content, check the playbook
result = subprocess.run(
    ["python3", "experiment-engine.py", "playbook", "--agent", "content"],
    capture_output=True, text=True
)
# Parse playbook rules and apply them to new content
```

---

## Project Structure

```
growth-engine/
â”œâ”€â”€ experiment-engine.py          # Core experiment lifecycle engine
â”œâ”€â”€ autogrowth-weekly-scorecard.py # Weekly report generator
â”œâ”€â”€ pacing-alert.py               # Campaign pacing monitor
â”œâ”€â”€ requirements.txt              # Python dependencies
â”œâ”€â”€ .env.example                  # Environment variable template
â”œâ”€â”€ SKILL.md                      # Claude Code skill definition
â”œâ”€â”€ README.md                     # This file
â””â”€â”€ data/                         # Auto-created experiment data
    â””â”€â”€ experiments/
        â”œâ”€â”€ content/
        â”‚   â”œâ”€â”€ experiments.json  # Experiment definitions + data
        â”‚   â”œâ”€â”€ playbook.json    # Proven winners
        â”‚   â””â”€â”€ active.json      # Currently running experiments
        â”œâ”€â”€ email/
        â”œâ”€â”€ seo/
        â””â”€â”€ ...
```

---

## License

MIT

---

<div align="center">

**ðŸ§  [Want these built and managed for you? â†’](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills)**

*This is how we build agents at [Single Brain](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) for our clients.*

[Single Grain](https://www.singlegrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) Â· our marketing agency

ðŸ“¬ **[Level up your marketing with 14,000+ marketers and founders â†’](https://levelingup.beehiiv.com/subscribe)** *(free)*

</div>
