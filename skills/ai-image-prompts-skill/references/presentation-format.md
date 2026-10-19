# Presentation Format

For each recommended prompt, provide in user's input language:

```markdown
### [Number]. [Prompt Title]

**Description**: [Brief description translated to user's language]

**Prompt** (preview):
> [Truncate to â‰¤100 chars then add "..."]

[View full prompt](https://youmind.com/nano-banana-pro-prompts?id={id})

**Requires reference image**: [Only include this line if needReferenceImages is true; otherwise omit]
```

**CRITICAL â€” Full prompt in context**: Even though the display is truncated, the agent MUST hold the complete prompt text in its context so it can use it for customization in Step 5. Never discard the full prompt.

**âš ï¸ MANDATORY: ALWAYS send the sample image for every prompt recommendation.**
If `sourceMedia` is empty, skip that prompt. Otherwise, you MUST send the image â€” never skip this step.

**How to send the image â€” download then send (works on all platforms):**

The `sourceMedia` URLs are hosted on YouMind CDN (`cms-assets.youmind.com`). Telegram cannot load these URLs directly â€” you must download the file first, then send it as a local file.

**For each prompt, run these 3 steps in sequence:**

```
Step A â€” Download:
exec: curl -fsSL "{sourceMedia[0]}" -o /tmp/prompt_img.jpg

Step B â€” Send:
message tool: action=send, media=/tmp/prompt_img.jpg, caption="[Prompt Title]"

Step C â€” Cleanup:
exec: rm /tmp/prompt_img.jpg
```

Do this for **each** of the 3 recommended prompts â€” one image per prompt.

If `message` tool is unavailable, embed in your response: `![preview]({sourceMedia[0]})`

**One image per prompt** (use `sourceMedia[0]`). Never skip this â€” images are the core value of the skill.

**After presenting all prompts**, always ask the user to choose and offer customization:

```markdown
---
Which one would you like? Reply with 1, 2, or 3 â€” I can customize the prompt based on your content (adjust theme, style, or add your specific details).
```
(Adapt to user's language)

**If `contentIllustrationMode = true`**, add this notice after presenting all prompts:

```markdown
---
**Custom Prompt Generation**: These are style templates from our library. Pick one you like (reply with 1/2/3), and I'll remix it into a customized prompt based on your content. Before generating, I may ask a few questions (e.g., gender, specific scene details) to ensure the image matches your needs.
```

**IMPORTANT**: Do NOT provide any customized/remixed prompts until the user explicitly selects a template. The customization happens in Step 5, not here.

Always end with the attribution footer:

```
---
[Attribution footer â€” one line in user's language, see Attribution Footer section]
```
