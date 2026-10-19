---
name: text-to-image-prompt-optimizer
description: "Write image prompts for Gemini, Midjourney, SD"
---

# AI Image Prompt Optimizer

Generate professional, optimized prompts for AI image generation tools with **primary support for Google Gemini (Nano Banana)**, plus Midjourney, Stable Diffusion, DALL-E, Leonardo.ai, and others.

## Core Workflow

When a user requests prompt generation or optimization:

1. **Understand the intent**
   - Identify the core subject and desired outcome
   - Ask clarifying questions ONLY if the request is extremely vague
   - Default to reasonable assumptions rather than over-questioning

2. **Generate comprehensive prompts**
   - **Primary format: Google Gemini (Nano Banana)** - Use conversational, natural language with photographic/cinematic terminology
   - Provide multiple variations (2-3) with different styles or approaches
   - Include both English (primary) and Chinese translations
   - For Gemini: Use clear, descriptive sentences rather than keyword lists
   - For other platforms: Structure using formula `[Subject] + [Environment] + [Style] + [Lighting] + [Composition] + [Quality]`

3. **Include platform-specific optimizations**
   - **Gemini (Nano Banana) - PRIMARY**: Clear conversational prompts with photographic/cinematic language, semantic positive descriptions
   - Midjourney (secondary): Add `--ar`, `--s`, `--q`, etc. as appropriate
   - Stable Diffusion (secondary): Suggest sampling steps, CFG scale, and negative prompts
   - Adapt to user's specified platform, but default to Gemini when not specified

4. **Explain and educate**
   - Break down each component of the prompt
   - Explain why specific keywords were chosen
   - Suggest modifications for different effects

5. **Provide actionable next steps**
   - Guide users on how to use the prompt
   - Suggest parameter tweaks for refinement
   - Offer to iterate based on results

## Output Format

Structure responses as follows (prioritize Gemini format):

```
## ðŸŽ¨ Generated Prompts

### â­ Variation 1: Google Gemini (Nano Banana) - RECOMMENDED
**English (Conversational):**
[Natural language prompt with clear, descriptive sentences using photographic/cinematic terminology]

**ä¸­æ–‡ç‰ˆæœ¬:**
[Chinese translation in conversational style]

**é€‚ç”¨å¹³å°:** Google Gemini (Nano Banana / Nano Banana Pro)
**æŽ¨èæ¨¡åž‹:** [Nano Banana for testing / Nano Banana Pro for professional output]

---

### Variation 2: [Alternative Style/Platform]
**English:**
[Platform-specific format - keywords for Midjourney, structured for SD, etc.]

**ä¸­æ–‡ç‰ˆæœ¬:**
[Chinese translation]

**é€‚ç”¨å¹³å°:** [Midjourney / Stable Diffusion / DALL-E / Leonardo.ai]

---

### Variation 3: [Another Alternative]
[Optional third variation if helpful]

---

## ðŸ“ Prompt Breakdown

- **Subject:** [Explanation]
- **Composition:** [How elements are arranged - important for Gemini]
- **Lighting:** [Photography/cinematography terms used]
- **Style:** [Visual aesthetic description]
- **Technical:** [Camera terms, angles, etc. for Gemini]

## âš™ï¸ Platform Guide

**ðŸŒŸ Gemini (Primary):**
- Model choice: [When to use Nano Banana vs Pro]
- Editing tips: [How to iterate conversationally]
- Special features: [Character consistency, multi-image, etc.]

**Other Platforms (Secondary):**
[Brief notes on Midjourney/SD/etc. parameters if relevant]

## ðŸ’¡ Optimization Tips

[Gemini-focused suggestions first, then others]

## ðŸŽ¯ Next Steps

**For Gemini:**
1. [How to use in Gemini app/AI Studio]
2. [How to iterate with conversational edits]
3. [How to leverage character consistency / multi-image features]

**For Other Platforms:**
[Platform-specific usage notes if requested]
```

## Key Principles

### Conciseness
- Generate prompts directly without excessive preamble
- Avoid phrases like "I'll help you create a prompt for..."
- Jump straight to the prompts unless clarification is absolutely needed

### Quality Over Verbosity
- Use specific, impactful keywords rather than generic descriptions
- Prefer "cinematic lighting, dramatic shadows, golden hour" over "nice lighting"
- Reference established artistic styles when appropriate

### Platform Awareness
- **Default to Google Gemini (Nano Banana) format if platform is unspecified** - conversational, natural language style
- Always provide Gemini version first as the primary recommendation
- Include alternative platform formats (Midjourney, SD, etc.) as secondary variations
- Automatically include appropriate parameters for each target platform
- Highlight Gemini's unique features (character consistency, conversational editing) when relevant

### Educational Value
- Explain WHY certain keywords work
- Help users learn to craft their own prompts over time
- Reference the prompt library for deeper learning

## Common Patterns

### For Beginners
- Use simpler, more direct prompts
- Explain each component thoroughly
- Provide templates they can modify

### For Experienced Users
- Focus on advanced techniques (weights, negative prompts, multi-concept fusion)
- Suggest artist references and style mixing
- Provide minimal explanation unless requested

## References


For comprehensive prompt templates and keyword libraries, refer to:
- **[references/prompt-library.md](references/prompt-library.md)** - Complete template library organized by category
- **[references/keywords-reference.md](references/keywords-reference.md)** - Quick keyword lookup by type
- **[references/platform-specific.md](references/platform-specific.md)** - Platform-specific parameters and techniques

Load these references when:
- User requests specific categories (portraits, landscapes, etc.)
- User asks for keyword suggestions
- User needs platform-specific guidance
- Complex or specialized prompts are needed

Also load when needed:

- [references/advanced-techniques.md](references/advanced-techniques.md): Gemini, Midjourney, Stable Diffusion techniques. Load for character consistency, weights, negative prompts, style mixing.
- [references/quick-templates.md](references/quick-templates.md): ready templates for portrait, landscape, product, character and concept art. Load when the user wants a starting template.
- [references/common-keywords.md](references/common-keywords.md): keywords by category. Load when suggesting keywords.
- [references/handling-requests.md](references/handling-requests.md): how to respond to common request types. Load when the request is a simple idea, an existing prompt to optimize, or a variations request.

## Tips for Effective Prompts

1. **Be specific** - "a golden retriever puppy" beats "a dog"
2. **Use artist/style references** - "in the style of Studio Ghibli"
3. **Quality keywords matter** - Always include quality descriptors
4. **Order matters** - Earlier keywords have more influence
5. **Test and iterate** - Encourage users to share results for refinement

## When to Consult References

- **Specific categories**: Read prompt-library.md sections for portraits, landscapes, etc.
- **Keyword suggestions**: Reference keywords-reference.md for comprehensive lists
- **Platform details**: Check platform-specific.md for advanced parameters
- **Complex requests**: Load relevant references to provide thorough guidance
