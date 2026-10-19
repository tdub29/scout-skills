---
name: deep-research
description: "Multi-source web brief with citations and open gaps"
metadata:
  version: 0.2.0
---

# /deep-research â€” Multi-source research with archive

Plans, executes, and synthesizes research from multiple sources. Archives the output so the corpus compounds.

## Step 1 â€” Frame the question

Restate the research question in one tight sentence. If ambiguous, ask the user:
- What's the decision this research will inform?
- What's the minimum useful answer? (Saves over-researching.)
- Any sources to prioritize or avoid?

Output: `**Research question:** <one sentence>`

## Step 2 â€” Plan the sources

Pick from this menu based on the question type. Note which sources you'll hit and why.

**Open with a real search, not recall.** The first discovery action is an actual `agent-reach` or `WebSearch` call. Never cloud `browse`/Browserbase: no keys are set, so it always fails. Anything you already "know" about the topic is a hypothesis to verify against a fetched source, not a finding. Full ladder: `.agents/rules/web-browsing-setup.md`.

| Source | When to use | Tool |
|---|---|---|
| Semantic web search, YouTube, GitHub, RSS | **Rung 0. Start here.** Finding sources, and platforms a plain fetch cannot read | `agent-reach` CLI, key-free (`agent-reach doctor --json` lists live channels) |
| Web search | Authoritative articles, docs, official statements | `WebSearch` |
| Specific URLs | When the user hands over starting URLs | `WebFetch` |
| JS-rendered pages | Pricing pages, product tours, profiles | `node .agents/scripts/web-get.mjs "<url>" --text` from the workspace root (key-free headless Chrome) |
| Memory | Prior research / decisions / context the user already captured | grep `~/.claude/memory/` |
| Notion | If the topic touches a known Notion workspace | Direct Notion API (key in `$NOTION_API_KEY`, see `reference_notion_api.md`) |
| Research archive | Prior `/deep-research` runs that touched this topic | grep `${MAKERSKILLS_CONFIG:-$HOME/.config/makerskills}/deep-research/archive/` |

Run discovery passes **in parallel** where possible. Sequential only when one source needs another's output (e.g., fetching a URL that agent-reach or WebSearch discovered).

## Step 3 â€” Execute discovery

Run each chosen source. For each result, capture:
- The source (URL or system)
- 1â€“3 sentence summary of what was said
- Date / recency
- Confidence in the source (high/medium/low)

Don't synthesize yet â€” just collect.

## Step 4 â€” Synthesize

1. **Group findings** by theme or sub-question
2. **Contradiction check** â€” flag anywhere sources disagree. Don't average them; surface the disagreement.
3. **Confidence**: high (multiple independent sources agree), medium (one strong source or several weak), low (single anecdote or speculation)
4. **Gaps**: what would change the answer? What's NOT in the corpus?

## Step 5 â€” Output the brief

Use this template:

```markdown
# Research: <question>

**Date:** <YYYY-MM-DD>
**Decision this informs:** <one line>
**Confidence overall:** high / medium / low

## TL;DR
<2â€“4 sentences with the answer>

## Key findings

### 1. <Finding>
<2â€“4 sentences>. Sources: [1], [3], [5]

### 2. <Finding>
...

## Contradictions / uncertainty
- <where sources disagree, with each side cited>

## Gaps
- <what's missing from the corpus>
- <what to research next to close the gap>

## Recommended next steps
1. <action>
2. <action>

## Sources
[1] <Title> â€” <URL or system> (<date>) â€” <confidence>
[2] ...
```

## Step 6 â€” Archive

Archives live in `${MAKERSKILLS_CONFIG:-$HOME/.config/makerskills}/deep-research/archive/` (create the directory if missing). Never write archives inside the skill's own folder â€” skill installs and upgrades re-sync from source and wipe anything saved there. **Migration:** if this skill's folder contains an old `references/research-archive/` with user entries, move those files into the archive directory first.

Write the brief to `<archive dir>/<YYYY-MM-DD>-<slug>.md` so it's grep-able forever. Slug = kebab-case of the topic.

Also append a one-line entry to `<archive dir>/INDEX.md` (create if missing):

```markdown
- 2026-06-15 â€” [<topic>](./<filename>.md) â€” <one-line TL;DR>
```

## Step 7 â€” Surface

After archiving:
- Show the full brief in chat
- Tell the user the archive path
- Offer: *"Push to Notion or save to a project's docs?"*

## Composes with

- `business-brainstorm` â€” calls this skill during the market validation step
- `/domain` â€” when research includes "is the .com available"
- `agent-reach` â€” the key-free rung-0 source (web search, YouTube, GitHub, RSS)

## Notes on quality

- **Always cite.** Every claim in the brief needs a source pointer.
- **Recency matters** â€” note dates on each source. For fast-moving topics (AI, startups), de-weight sources >12 months old.
- **Don't trust a single source** for high-stakes claims. Re-search until you have at least 2 independent corroborations or surface the uncertainty.
- **No padding.** If the answer is one paragraph, return one paragraph. The template is a maximum, not a minimum.
