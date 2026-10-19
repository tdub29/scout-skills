# ðŸŽ¨ AI Image Prompt Optimizer

## Contents

- [âœ¨ Features](#-features)
- [ðŸ“¦ Installation](#-installation)
- [ðŸš€ Usage](#-usage)
- [ðŸ“š What You Get](#-what-you-get)
- [ðŸŽ“ Reference Materials](#-reference-materials)
- [ðŸŒŸ Platform Priority](#-platform-priority)
- [ðŸ“– Example Output](#-example-output)
- [ðŸ› ï¸ Technical Details](#-technical-details)
- [ðŸ¤ Contributing](#-contributing)
- [ðŸ“„ License](#-license)
- [ðŸ”— Links](#-links)
- [ðŸ“® Author](#-author)


A Claude Code skill for generating and optimizing AI image generation prompts with **primary support for Google Gemini (Nano Banana)**, plus Midjourney, Stable Diffusion, DALL-E, Leonardo.ai, and other text-to-image tools.

## âœ¨ Features

- **Google Gemini Optimized**: Primary focus on conversational, natural language prompts for Google Gemini (Nano Banana)
- **Multi-Platform Support**: Secondary support for Midjourney, Stable Diffusion, DALL-E, Leonardo.ai
- **Bilingual Output**: English and Chinese prompt variations
- **Educational**: Explains prompt components and optimization strategies
- **Comprehensive Templates**: Pre-built templates for portraits, landscapes, products, and more
- **Reference Library**: Extensive keyword and platform-specific reference materials

## ðŸ“¦ Installation

### Using npx (Recommended)

```bash
npx skills add manzxiao/text-to-image-prompt-optimizer
```

### Manual Installation

1. Clone this repository to your Claude Code skills directory:
```bash
cd ~/.claude/skills
git clone https://github.com/manzxiao/text-to-image-prompt-optimizer.git
```

2. Restart Claude Code or reload skills

## ðŸš€ Usage

The skill activates automatically when you:

1. Request prompt generation: "Generate a prompt for..."
2. Optimize existing prompts: "Optimize this prompt: ..."
3. Ask for variations: "Create variations of this image idea"
4. Mention keywords: Gemini, Nano Banana, Midjourney, AIç»˜å›¾, text-to-image
5. Use command patterns: "/imagine", "æç¤ºè¯"

### Example Requests

```
Generate a prompt for a sunset over mountains

ä¼˜åŒ–è¿™ä¸ªæç¤ºè¯: a cat sitting on a table

Create variations for a cyberpunk street scene

å¸®æˆ‘ç”Ÿæˆä¸€ä¸ªé€‚åˆ Nano Banana çš„äººç‰©è‚–åƒæç¤ºè¯
```

## ðŸ“š What You Get

Each prompt generation includes:

- â­ **Google Gemini version** (Primary, conversational style)
- ðŸŽ¯ **Alternative platform versions** (Midjourney, SD, etc.)
- ðŸ“ **Prompt breakdown** explaining each component
- âš™ï¸ **Platform-specific guidance** and parameters
- ðŸ’¡ **Optimization tips** for refinement
- ðŸŽ¯ **Next steps** for implementation

## ðŸŽ“ Reference Materials

The skill includes comprehensive reference documentation:

- **prompt-library.md** - Template library organized by category (portraits, landscapes, products, etc.)
- **keywords-reference.md** - Quick keyword lookup by type
- **platform-specific.md** - Platform-specific parameters and advanced techniques

## ðŸŒŸ Platform Priority

**Primary (Default):**
- Google Gemini (Nano Banana) - Conversational, natural language prompts

**Secondary (On Request):**
- Midjourney
- Stable Diffusion
- DALL-E
- Leonardo.ai

## ðŸ“– Example Output

When you ask for a prompt, you'll receive:

```
## ðŸŽ¨ Generated Prompts

### â­ Variation 1: Google Gemini (Nano Banana) - RECOMMENDED
English (Conversational):
Create a professional portrait of a young woman in her late 20s with warm,
natural lighting. She should have confident, friendly expression...

ä¸­æ–‡ç‰ˆæœ¬:
ç”Ÿæˆä¸€å¼ ä¸“ä¸šäººåƒç…§ç‰‡ï¼Œä¸»è§’æ˜¯ä¸€ä½20å¤šå²çš„å¹´è½»å¥³æ€§ï¼Œé‡‡ç”¨æ¸©æš–è‡ªç„¶çš„å…‰çº¿...

é€‚ç”¨å¹³å°: Google Gemini (Nano Banana / Nano Banana Pro)
æŽ¨èæ¨¡åž‹: Nano Banana for testing / Nano Banana Pro for professional output

---

### Variation 2: Midjourney Style
professional portrait, young woman, late 20s, warm lighting,
confident expression, natural beauty...

[Plus detailed breakdowns, tips, and next steps]
```

## ðŸ› ï¸ Technical Details

- **Skill Type**: Claude Code Agent Skill
- **Format**: SKILL.md with YAML frontmatter
- **Compatibility**: Claude Code CLI, skills.sh
- **Language**: English & Chinese

## ðŸ¤ Contributing

Contributions are welcome! Feel free to:

- Report issues
- Suggest improvements
- Add new templates or keywords
- Expand platform support

## ðŸ“„ License

MIT License - Feel free to use and modify for your projects.

## ðŸ”— Links

- [Skills.sh Directory](https://skills.sh/)
- [Claude Code Documentation](https://code.claude.com/docs)
- [Google Gemini](https://gemini.google.com/)

## ðŸ“® Author

**manzxiao**

If you find this skill useful, please â­ star the repository!

---

**Installation:**
```bash
npx skills add manzxiao/text-to-image-prompt-optimizer
```
