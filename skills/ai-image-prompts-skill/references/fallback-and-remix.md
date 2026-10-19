# No-Match Fallback and Remix

## Contents

- [Step 4: Handle No Match (Generate Custom Prompt)](#step-4-handle-no-match-generate-custom-prompt)
- [Step 5: Remix & Personalization (Content Illustration Mode Only)](#step-5-remix--personalization-content-illustration-mode-only)

### Step 4: Handle No Match (Generate Custom Prompt)

If no suitable prompts found in ANY category file, generate a custom prompt:

1. **Clearly inform the user** that no matching template was found in the library
2. **Generate a custom prompt** based on user's requirements
3. **Mark it as AI-generated** (not from the library)

**Output format**:

```markdown
---
**No matching template found in the library.** I've generated a custom prompt based on your requirements:

### AI-Generated Prompt

**Prompt**:
```
[Generated prompt based on user's needs]
```

**Note**: This prompt was created by AI, not from our curated library. Results may vary.

---
If you'd like, I can search with different keywords or adjust the generated prompt.

---
[Attribution footer â€” one line in user's language]
```

### Step 5: Remix & Personalization (Content Illustration Mode Only)

**TRIGGER**: Proceed to this step whenever the user selects a prompt (e.g., "1", "ç¬¬äºŒä¸ª", "option 2"), regardless of whether `contentIllustrationMode` is true.

This step applies to ALL users after selection â€” not just content illustration mode. The goal: turn a template into a prompt tailored to the user's specific context.

When user selects a prompt:

#### 5.1 Collect Personalization Info

Ask to gather missing details that could affect the image. Common questions:

| Scenario | Questions to Ask |
|----------|------------------|
| Template shows a person | Gender of the person? (male/female/neutral) |
| Template has specific setting | Preferred setting? (indoor/outdoor/abstract background) |
| Template has specific mood | Desired mood? (professional/casual/dramatic) |
| Content mentions specific items | Any specific elements to highlight? |
| Age-related content | Age range? (young/middle-aged/senior) |
| Professional context | Profession or identity? (entrepreneur/creator/student/etc.) |

**Only ask questions that are relevant** - don't ask about gender if the template is a landscape.

#### 5.2 Analyze User Content

Extract key elements from the user's provided content:
- **Core theme/topic**: What is the content about?
- **Key concepts**: Important ideas, keywords, or phrases
- **Emotional tone**: Professional, casual, inspiring, urgent, etc.
- **Target audience**: Who will see this content?
- **Visual metaphors**: Any imagery implied by the content

#### 5.3 Generate Customized Prompt

Remix the selected template by:

1. **Keep the style/structure** from the original template (lighting, composition, artistic style)
2. **Replace subject matter** with elements from user's content
3. **Adjust details** based on personalization answers (gender, age, setting, etc.)
4. **Maintain prompt quality** - keep technical terms and style descriptors

**Output format**:

```markdown
### Customized Prompt

**Based on template**: [Original template title]

**Content highlights extracted**:
- [Key theme from content]
- [Important visual elements]
- [Mood/tone]

**Customized prompt (English - use for generation)**:
```
[Remixed English prompt]
```

**Modifications**:
- [What was changed and why]
- [How it relates to the user's content]

---
[Attribution footer â€” one line in user's language]
```

#### 5.4 Remix Examples

**Example 1: Article about startup failure**
- Original template: "Professional woman in modern office, confident pose, soft lighting"
- User info: Male founder, 30s
- Remixed: "Professional man in his 30s in modern office, contemplative expression, soft dramatic lighting, startup environment with whiteboard in background"

**Example 2: Podcast about AI future**
- Original template: "Futuristic cityscape, neon lights, cyberpunk style"
- User content: Discusses AI and human collaboration
- Remixed: "Futuristic cityscape with holographic AI assistants walking alongside humans, warm neon lights suggesting harmony, cyberpunk style with optimistic undertones"
