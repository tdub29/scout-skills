# Carved-skill template (schwartz-* anatomy)

Use this when spawning a per-skill drafting subagent in Step 6 of `book-to-skill`. Substitute placeholders. This template mirrors the schwartz-mass-desire and tufte-lie-factor anatomy â€” both are working exemplars.

---

```markdown
---
name: {prefix}-{framework-slug}
description: {Pushy single dense sentence â€” start with the framework's core action ("Apply X's Y framework to do Z") then chain trigger phrases. Include the framework name, the author, the book, AND a long list of non-keyword triggers ("the user is debating which X to lead with," "the user is comparing two approaches"). Description should be 150â€“250 words. Lean toward MORE triggers, not fewer â€” undertrigger is a worse failure than overtrigger. End with the output type ("Output is a ___ + ___ + ___"). Optionally end with a DO NOT TRIGGER FOR sentence to fence against adjacent skills.}
---

# {Author}: {Framework name as the book names it}

## When to use

Trigger when {state the user's *moment* â€” what decision are they making, what's confusing them, what's the next action they're about to take?}. Concrete cues:

- {Bullet list of trigger contexts â€” non-keyword. "The user has a chart with 8+ overlapping series" beats "the user says 'small multiples'."}
- {Continue 4â€“8 bullets}

Don't trigger for: {adjacent skills that overlap on keywords but route elsewhere}. {One-sentence explanation of where the boundary is.}

## The framework

### Core thesis

{One paragraph. The big idea in the author's own logic â€” but in plain English, not paraphrased to death. Why does this framework exist? What's the leverage? What's the cost? What does the author's evidence show?}

### {Sub-concept 1 from the book â€” use the book's own headings if possible}

{...}

### {Sub-concept 2}

{...}

### {Continue for each sub-concept the framework has}

(Most carved skills have 3â€“6 sub-concepts. If you have fewer than 3, the framework probably fails test #3 â€” fold instead.)

## How to apply (step-by-step)

1. **{Imperative verb}.** {Concrete output of this step.}
2. **{Imperative verb}.** {Concrete output.}
3. {Continue. Each step should produce something tangible.}
4. ...

(Most carved skills have 5â€“9 steps. The final step is usually "sanity-check by â€¦" â€” a verification step.)

## Common failure modes

- **{Failure mode name}.** {What it looks like in the wild. Why it happens. What the agent should do instead. Two sentences each is plenty.}
- **{Another failure mode.}** {...}
- {Continue. 4â€“8 failure modes is typical. The schwartz-* family averages 6.}

## References

- *{Book title}*, {edition}, chapter {N} (book pages Xâ€“Y). {Specific page references for the framework's definition.}
- Sibling carved skills:
  - `{prefix}-{other-framework-1}` â€” {one-line relationship}
  - `{prefix}-{other-framework-2}` â€” {one-line relationship}
- Parent reference doc: `references/{prefix}-{parent}.md` ({if applicable})
```

## Template guidance for the drafting subagent

- **Description field.** Treat it as the most important text in the file. Description failures are the #1 reason skills never trigger. Pushy > polite. Many triggers > few triggers. Specific contexts > generic ones. Include the author's name and the book â€” users searching for "Schwartz" or "Tufte" should hit this skill.

- **Don't paraphrase the book.** Read the chapter, then write the SKILL.md in your own structural words while preserving the author's specific terms (Lie Factor, Mass Desire, Data-Ink Ratio). The skill is agent-readable instructions, not a book summary.

- **Output type matters.** Every skill must end the "how to apply" steps with a tangible output: a score, a checklist filled out, a redraw spec, a ranked list, a diagnosis, a layout plan. Name the output type in the description. If you can't name the output, the framework didn't pass test #1 and shouldn't have been carved.

- **Failure modes are the secret sauce.** The schwartz-* family's depth comes from the "common failure modes" section â€” they teach the agent what NOT to do, which is half of agentic decision-making. Lift failure modes from the book where the author warns against something explicitly; add inferred failure modes only if they're clearly implied.

- **Cross-reference siblings.** Every carved skill in a family should link to its 2â€“4 nearest siblings in the References section. This helps the agent route correctly when it hits a borderline trigger.

- **No "as the author would sayâ€¦"** Voice belongs in a separate `<author>-voice` skill (via `voice-analysis`). Framework skills are method, not impersonation.

- **Length.** Target 200â€“400 lines. Under 150 lines suggests the framework is too thin to be its own skill. Over 500 lines means you should be splitting into a SKILL.md + `references/` files.

- **Write to `drafts/{prefix}-{framework-slug}/SKILL.md`.** The orchestrator will move it to `skills/` after the user reviews.
