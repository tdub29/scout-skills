# Deck Generator

**AI-generated presentations in minutes, not hours.** Every slide is a custom image in a consistent visual style.

## How It Works

```
Content Spec (JSON/MD)
        â”‚
        â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Style Engine â”‚ prepend style prefix to each prompt
â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜
       â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  Imagen 4.0  â”‚ generate slide images (~4Â¢ each)
â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜
       â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚   Assemble   â”‚ local images or Google Slides
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

You provide the content. The generator creates a consistent, professional deck where every slide is a purpose-built image. No template hunting. No design skills needed.

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your Gemini API key
export GEMINI_API_KEY="your-api-key-here"

# 3. Create a content spec (see examples/)
cat > slides.json << 'EOF'
[
  {"name": "01-title", "prompt": "Title slide: 'AI Marketing in 2025'"},
  {"name": "02-problem", "prompt": "Dashboard showing declining organic reach across platforms"},
  {"name": "03-solution", "prompt": "AI agent workflow: content creation to distribution pipeline"}
]
EOF

# 4. Generate
python3 scripts/generate-deck.py --content slides.json --style whiteboard --title "AI Marketing"
```

## Style Presets

| Style | Look |
|-------|------|
| `whiteboard` | Hand-drawn sketch, black ink, orange accents |
| `corporate` | Navy/white/gold, clean sans-serif |
| `minimalist` | White background, single blue accent, Apple keynote vibe |
| `dark-tech` | Black background, neon green, terminal aesthetic |
| `playful` | Bright pastels, rounded shapes, startup energy |
| `editorial` | B&W with red spot color, magazine layout |

Or describe your own: `--style "Retro 80s neon aesthetic with grid backgrounds"`

## Cost & Speed

- ~4 cents per slide image
- 14-slide deck â‰ˆ 56 cents and ~2 minutes
- Supports parallel generation (rate-limited)

## Output Options

1. **Local images** (default) â€” PNG files in output directory
2. **Google Slides** â€” Automatic presentation creation via Google Slides API

## Requirements

- Python 3.10+
- Gemini API key (`$GEMINI_API_KEY`)
- Google Slides API credentials (optional, for auto-assembly)

---

<div align="center">

**ðŸ§  [Want these built and managed for you? â†’](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills)**

*This is how we build agents at [Single Brain](https://singlebrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) for our clients.*

[Single Grain](https://www.singlegrain.com/?utm_source=github&utm_medium=skill_repo&utm_campaign=ai_marketing_skills) Â· our marketing agency

ðŸ“¬ **[Level up your marketing with 14,000+ marketers and founders â†’](https://levelingup.beehiiv.com/subscribe)** *(free)*

</div>
