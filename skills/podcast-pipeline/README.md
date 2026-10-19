# AI Podcast Ops

**One podcast episode in, 15-20 content pieces out. Scored, deduplicated, and scheduled.**

Most podcast teams publish an episode and maybe pull one audiogram. This pipeline treats every episode as a content mine â€” extracting narrative arcs, quotable moments, controversial takes, data points, and stories, then generating platform-native content for every channel with viral scoring and deduplication.

## What's Inside

### ðŸŽ™ï¸ Podcast-to-Everything Pipeline (`podcast_pipeline.py`)
End-to-end pipeline that ingests podcast episodes (via RSS feed or raw transcript) and produces a full cross-platform content calendar.

**Ingest modes:**
- RSS feed â†’ auto-download + Whisper transcription
- Raw transcript file (text, SRT, VTT)
- Batch mode: process last N episodes from a feed

**Content generated per episode:**
- 3-5 short-form video clip suggestions (with timestamps + hooks)
- 2-3 Twitter/X thread outlines
- 1 LinkedIn article draft
- 1 newsletter section
- 3-5 quote cards (text overlays for social)
- 1 blog post outline with SEO keywords
- 1 YouTube Shorts/TikTok script

**Intelligence layer:**
- Editorial Brain: LLM-powered extraction of 7 content atom types
- Viral scoring: Novelty Ã— Controversy Ã— Utility (0-100)
- Dedup engine: semantic similarity check against last N days of output
- Calendar generator: auto-schedules by platform best practices

### ðŸ“‹ SKILL.md
Claude Code skill file. Drop into your project and ask: *"Turn this podcast episode into a content calendar"* â€” it handles the rest.

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up environment
cp .env.example .env
# Edit .env with your API keys (OPENAI_API_KEY, ANTHROPIC_API_KEY)

# 3. Process latest episode from your podcast RSS
python podcast_pipeline.py --rss "https://feeds.example.com/podcast.xml"

# 4. Or process a local transcript
python podcast_pipeline.py --transcript episode-42.txt

# 5. Batch process last 5 episodes
python podcast_pipeline.py --batch "https://feeds.example.com/podcast.xml" --episodes 5

# 6. Generate weekly content calendar
python podcast_pipeline.py --calendar

# 7. Only keep high-scoring content
python podcast_pipeline.py --rss "https://feeds.example.com/podcast.xml" --min-score 80
```

## Configuration

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | OpenAI API key (Whisper transcription) |
| `ANTHROPIC_API_KEY` | Yes | Anthropic API key (content generation) |
| `OPENAI_LLM_KEY` | Optional | Separate OpenAI key for GPT-based generation |

### CLI Options

| Flag | Description | Default |
|------|-------------|---------|
| `--rss <url>` | Process latest episode from RSS feed | â€” |
| `--transcript <file>` | Process a local transcript file | â€” |
| `--batch <url>` | Batch process from RSS feed | â€” |
| `--episodes <n>` | Number of episodes for batch mode | 5 |
| `--calendar` | Generate weekly calendar from outputs | â€” |
| `--dedup-days <n>` | Days of history for dedup check | 30 |
| `--min-score <n>` | Minimum viral score to include | 0 |
| `--output-dir <path>` | Output directory | `./output` |

## Output Structure

```
output/
â”œâ”€â”€ episodes/
â”‚   â”œâ”€â”€ 2024-01-15-episode-title/
â”‚   â”‚   â”œâ”€â”€ transcript.txt         # Clean transcript
â”‚   â”‚   â”œâ”€â”€ atoms.json             # Extracted content atoms
â”‚   â”‚   â”œâ”€â”€ content_pieces.json    # All generated content
â”‚   â”‚   â””â”€â”€ calendar.json          # Scheduled calendar
â”‚   â””â”€â”€ ...
â”œâ”€â”€ calendar/
â”‚   â””â”€â”€ week-2024-W03.json        # Aggregated weekly calendar
â”œâ”€â”€ content_history.json           # Dedup tracking (hashes + embeddings)
â””â”€â”€ pipeline_log.json              # Run history and performance stats
```

## How It Works

```
RSS Feed / Transcript
        â”‚
        â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  1. INGEST       â”‚  Download audio â†’ Whisper â†’ clean transcript
â”‚                  â”‚  OR read transcript file directly
â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”˜
         â”‚
         â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  2. EXTRACT      â”‚  Editorial Brain: find narrative arcs, quotes,
â”‚                  â”‚  controversial takes, data points, stories,
â”‚                  â”‚  frameworks, predictions
â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”˜
         â”‚
         â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  3. GENERATE     â”‚  For each atom â†’ platform-native content:
â”‚                  â”‚  clips, threads, articles, newsletter,
â”‚                  â”‚  quote cards, blog outlines, short scripts
â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”˜
         â”‚
         â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  4. SCORE        â”‚  Viral potential: novelty Ã— controversy Ã— utility
â”‚                  â”‚  Filter below threshold
â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”˜
         â”‚
         â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  5. DEDUP        â”‚  Semantic similarity vs last N days
â”‚                  â”‚  Remove overlaps, flag near-dupes
â””â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”˜
         â”‚
         â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  6. SCHEDULE     â”‚  Calendar generation with platform-specific
â”‚                  â”‚  timing rules and content mix optimization
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

## Viral Scoring

Every generated piece is scored on three dimensions:

| Dimension | Weight | What It Measures |
|-----------|--------|-----------------|
| Novelty | 40% | Is this new or surprising? |
| Controversy | 30% | Will people argue about this? |
| Utility | 30% | Can someone use this immediately? |

**Thresholds:** 80+ = priority publish, 60-79 = solid fill, 40-59 = gap filler, <40 = cut

## Integration with Other Skills

- **Content Ops / Expert Panel** â€” Run generated content through the expert panel for quality gating before publish
- **SEO Ops** â€” Feed blog outlines to the SEO pipeline for keyword validation
- **Outbound Engine** â€” Use podcast insights as personalization hooks in outbound sequences
- **Growth Engine** â€” A/B test different content formats from the same episode atoms
