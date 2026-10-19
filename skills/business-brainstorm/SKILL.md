---
name: business-brainstorm
description: "When you want to pressure-test a potential new business, product, or side project against the serial-founder filter. Not \"marketing ideas for a product\" (that's marketing-skills:marketing-ideas) â€” this is \"should this business exist + can you win it.\" Runs the idea through a structured framework (problem, audience, wedge, monetization, moat, portfolio fit, distribution, energy fit, opportunity cost), checks domain availability via /domain, optionally triggers /deep-research for market validation, and outputs a viability brief: build / sleep on it / pass. Archives every idea to ~/.config/makerskills/business-brainstorm/archive/ so past work is searchable. Triggers on \"/business-brainstorm,\" \"/brainstorm,\" \"new business idea,\" \"should I build X,\" \"pressure test this idea,\" \"validate this idea,\" \"is X a good business,\" \"what about a [type] for [audience].\""
metadata:
  version: 0.2.0
---

# /business-brainstorm â€” Pressure-test a business idea

Takes a vague idea, runs it through the user's filter, and outputs a structured viability brief. Composes with `deep-research` (for market) and `/domain` (for naming).

## Step 1 â€” Capture the idea

Get from the user:
- The idea in 1â€“2 sentences (the *what*)
- The reason it's on their mind (the *why now*)
- Any starting context (a chat where this came up, a tweet that inspired it, a problem they've hit)

If they point at a past chat / doc, load it first. Memory has `project_*.md` files for in-flight projects â€” check there before assuming the idea is brand-new.

If the idea is too vague to score, ask 1â€“2 clarifying questions and stop. Don't pad the brief with assumptions.

## Step 2 â€” Load the framework + personal overlay

Read `references/framework.md` â€” the user's filter. Apply each dimension in order.

Also try to load `${MAKERSKILLS_CONFIG:-$HOME/.config/makerskills}/business-brainstorm/portfolio.local.md` if it exists â€” this is where the user lists their real in-flight businesses, properties, audiences, and partners. When present, use it for the "portfolio fit," "distribution," and "opportunity cost" dimensions instead of asking the user to name each one.

## Step 3 â€” Score each dimension

For each of the 9 dimensions in `framework.md`, give a 1-line take + a verdict (âœ… strong / ðŸŸ¡ OK / âŒ weak / â“ unknown â€” needs research).

Don't BS the unknowns. Mark them â“ and route to deep-research in Step 4.

## Step 4 â€” Trigger research where needed (optional)

If 2+ dimensions are â“ unknown, offer the user: *"Want me to run `/deep-research` on [topic] before scoring?"*

Useful research targets:
- Market size / who pays signal â†’ `/last30days <space>` + `WebSearch`
- Competitive landscape â†’ search for "alternatives to X", "X vs Y" pages
- ICP signal â†’ forums / Reddit / X where the audience hangs out
- Pricing benchmarks â†’ look at competitor pricing pages

If the user says yes, run `Skill({skill: "deep-research", args: "<topic>"})` and incorporate the brief.

## Step 5 â€” Check the .com

Always run `/domain` on the working name(s). A perfect idea with a $50k domain is a worse idea than a B+ idea with a free .com.

If naming is wide open, brainstorm 5â€“10 candidate names through `/domain` and report which are available.

## Step 6 â€” Output the brief

Use this template:

```markdown
# Business brainstorm: <name or idea slug>

**Date:** <YYYY-MM-DD>
**Idea:** <1â€“2 sentences>
**Why now:** <1 sentence>

## Verdict
**Build** / **Sleep on it** / **Pass** / **Steal an angle for [existing property]**

<2â€“3 sentence rationale>

## Score

| Dimension | Take | Verdict |
|---|---|---|
| 1. Problem | â€¦ | âœ… |
| 2. Audience | â€¦ | ðŸŸ¡ |
| 3. Wedge | â€¦ | â“ |
| 4. Monetization | â€¦ | âœ… |
| 5. Moat | â€¦ | âŒ |
| 6. Portfolio fit | â€¦ | âœ… |
| 7. Distribution | â€¦ | âœ… |
| 8. Energy fit | â€¦ | ðŸŸ¡ |
| 9. Opportunity cost | â€¦ | âŒ |

## Domain
- <name>.com â€” available / taken / aftermarket $<price>
- (other candidates if relevant)

## Research applied
- <link to deep-research brief in ~/.config/makerskills/deep-research/archive/, if run>

## Open questions
- <what would change the verdict>

## If you build it (sketch)
- **First 100 customers:** <how>
- **Wedge offer:** <what>
- **Price:** <range>
- **MVP scope:** <1â€“3 features>

## If you don't build it
- **Angle to steal for existing properties:**
  - Property A: â€¦
  - Property B: â€¦
  - Property C: â€¦
  - (etc., only where relevant)
```

## Step 7 â€” Archive

Archives live in `${MAKERSKILLS_CONFIG:-$HOME/.config/makerskills}/business-brainstorm/archive/` (create the directory if missing). Never write archives inside the skill's own folder â€” skill installs and upgrades re-sync from source and wipe anything saved there. **Migration:** if this skill's folder contains an old `references/ideas-archive/` with user entries, move those files into the archive directory first.

Write to `<archive dir>/<YYYY-MM-DD>-<slug>.md`. Append to `<archive dir>/INDEX.md` (create if missing):

```markdown
- 2026-06-16 â€” [<idea>](./<filename>.md) â€” **<verdict>** â€” <one-line rationale>
```

## Step 8 â€” Surface

Show the brief in chat. Tell the user the archive path. Offer:
- *"Want to push to Notion as a positioning canvas?"*
- *"Want me to scaffold a project repo / landing page?"* (if verdict = Build)
- *"Want me to revisit in 30 days?"* (if verdict = Sleep on it)

## Composes with

- `deep-research` â€” for market validation when dimensions are â“
- `/domain` â€” for .com availability and naming brainstorm
- `/last30days` â€” for audience/market recency signal (via deep-research)
- Memory (`project_*.md`) â€” for portfolio context (don't pitch an idea that already exists)

## Notes on quality

- **Nine dimensions, not one hero metric.** Ideas fail because one dimension quietly rots even when the rest score high. Force each dimension to be scored â€” no "we'll figure that out later" cop-outs.
- **Verdict discipline: Ship / Sleep on it / Kill.** Not "maybe." Ambiguity in the verdict compounds into ambiguity in the commit; the brief exists to prevent that.
- **Portfolio-context check is non-negotiable.** Before writing, grep memory + wiki for existing property overlap. If the new idea is 80% one of your existing properties, propose extending the existing property instead of forking a new one â€” 4x cheaper to compound.
- **Archive every brief, even Kills.** Killed ideas resurface â€” the brief with rationale prevents re-litigating. The archive dir + INDEX.md makes revisit trivial.
- **"Angle to steal" section forces value from Kills.** Even ideas you won't build often have an angle that improves an existing property. Don't skip this section â€” it's the highest-leverage output of a Kill verdict.
- **30-day revisit for "Sleep on it."** Set the calendar reminder. Sleep-on-it ideas that never get revisited become dead weight in the archive; ideas that get revisited resurface with better context.
