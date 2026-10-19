# AI Image Prompts â€” 10,000+ Curated Prompts for Any Model

## Contents

- [What Is This?](#what-is-this)
- [Why Use This Skill?](#why-use-this-skill)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Categories](#categories)
- [Data Source](#data-source)
- [Keep Prompts Fresh](#keep-prompts-fresh)
- [License](#license)


[![Prompts](https://img.shields.io/badge/Prompts-10000%2B-brightgreen)](https://youmind.com/nano-banana-pro-prompts)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://clawhub.com/skill/ai-image-prompts)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-orange)](https://github.com/YouMind-OpenLab/ai-image-prompts-skill)
[![Daily Updates](https://img.shields.io/badge/Updates-Twice%20Daily-purple)]()
[![Multi-language](https://img.shields.io/badge/Language-Multi--lingual-yellow)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

> **Stop spending hours hunting for the right AI image prompt.** Tell your AI assistant what you need in one sentence â€” it searches 10,000+ curated prompts and returns the top 3 matches with sample images, ready to use with any model.
>
> ðŸ–¼ï¸ [Browse the Prompt Gallery â†’](https://youmind.com/nano-banana-pro-prompts)

## What Is This?

An **AI agent skill** that gives Claude, OpenClaw, Cursor, and other AI assistants the ability to intelligently search a curated library of **10,000+ image generation prompts**, recommend the best matches for your use case, and even customize prompts based on your content.

These prompts are **model-agnostic** â€” they work with:

- ðŸŒ **Nano Banana Pro** & **Nano Banana 2** (Google Gemini image generation)
- ðŸŽ¨ **Seedream 5.0** (ByteDance's latest image model)
- ðŸ–¼ï¸ **GPT Image 1.5** (OpenAI's newest image model)
- âœ¨ **Midjourney**, **DALL-E 3**, **Flux**, **Stable Diffusion**, and more

High-quality prompts are the key to great results â€” regardless of which model you use.

## Why Use This Skill?

- âœ… **10,000+ prompts, organized by use case** â€” not a random dump, but professionally categorized
- âœ… **Every prompt includes sample images** â€” see the result before you copy
- âœ… **Smart semantic search** â€” describe what you need, the AI finds the match
- âœ… **Content remix mode** â€” paste your article or video script, get a custom prompt
- âœ… **Updated twice daily** â€” always reflects the latest viral prompts from the community
- âœ… **Multi-language** â€” responds in your language, always provides English prompt for generation

---

## Installation

### OpenClaw (Recommended)

```bash
clawhub install ai-image-prompts
```

Or search inside OpenClaw chat:

> "Install the ai image prompts skill from clawhub"

### Claude Code

```bash
npx skills i YouMind-OpenLab/ai-image-prompts-skill
```

### Other AI Assistants (Cursor, Codex, Gemini CLI, Windsurf)

```bash
# Universal installer â€” auto-detects your AI assistant
npx skills i YouMind-OpenLab/ai-image-prompts-skill
```

### Manual / openskills

```bash
npx openskills install YouMind-OpenLab/ai-image-prompts-skill
```

---

## How to Use

### Mode 1: Direct Search

Just describe what you need:

```
"Find me a cyberpunk-style avatar prompt"
"I need prompts for travel blog article covers"
"Looking for a product photo on white background"
"Help me find a YouTube thumbnail for a tech review video"
```

You'll get up to 3 recommendations with:
- Translated title & description (in your language)
- Truncated prompt preview + link to full prompt
- Sample image showing the result
- One-click customization option

### Mode 2: Content Illustration

Provide your content and let the AI find matching visual styles:

```
"Here's my article about remote work productivity. Find me a good cover image prompt."
[paste article text]
```

The skill will:
1. Analyze your content's theme, tone, and audience
2. Search for matching prompt templates
3. Let you pick a style
4. Remix the prompt with your specific content details

---

## Categories

Prompts are organized into 11 use-case categories:

| Category | Count | Use For |
|----------|-------|---------|
| Social Media Post | 6,382 | Twitter, Instagram, LinkedIn visuals |
| Product Marketing | 3,709 | Ads, promo banners, marketing materials |
| Profile / Avatar | 1,064 | Profile pictures, AI portraits, headshots |
| Poster / Flyer | 485 | Event posters, flyers, announcements |
| Infographic / Edu Visual | 458 | Data visualizations, educational graphics |
| E-commerce Main Image | 382 | Product photos, listing images |
| Game Asset | 378 | Game sprites, characters, environments |
| Comic / Storyboard | 290 | Comics, manga, visual storytelling |
| YouTube Thumbnail | 173 | Video thumbnails, channel art |
| App / Web Design | 167 | UI mockups, app screenshots, web design |
| Uncategorized | 910+ | Everything else â€” landscapes, abstract, experimental |

---

## Data Source

All prompts are curated from the open community by [YouMind.com](https://youmind.com) â€” sourced from real creators sharing their best image generation results on social media. Each prompt includes the actual generated image as a sample.

The library is updated **twice daily** via GitHub Actions, syncing with the latest community contributions.

---

## Keep Prompts Fresh

The skill auto-checks for updates on each use. To manually sync:

```bash
# Check if update needed (silent if fresh)
node scripts/setup.js --check

# Force update all references
pnpm run sync
```

---

## License

MIT â€” prompts are community-sourced and free to use.

---

<p align="center">
  <sub>Curated with â¤ï¸ by <a href="https://youmind.com">YouMind.com</a></sub>
</p>
