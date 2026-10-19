---
name: x-longform-post
description: Write long-form X (Twitter) posts and threads in a founder/CEO voice. Use when drafting X articles, long tweets, thought leadership threads, or viral content. Produces contrarian, data-backed posts with ASCII diagrams and code block visuals. Includes mandatory AI humanizer pass (24-pattern detector) before finalizing.
---

# X Long-Form Post Writer

Write posts for X in your founder/CEO's authentic voice. Every post should feel like a real person wrote it â€” not a content team, not a bot.

See `references/founder-voice.md` for the founder voice template. Customize it with your founder's real patterns.

---

## Voice Rules

- Simple declarative sentences. Short paragraphs.
- Contrarian angles backed by specific numbers and real examples.
- No corporate speak. No "I'm excited to share." No emoji in body text.
- Open with a hook that stops the scroll â€” contrarian claim, surprising number, or uncomfortable truth.
- End with a payoff: uncomfortable truth â†’ "worth it" resolution.

---

## Structure

1. **Hook** (1-2 lines) â€” Contrarian claim or surprising stat
2. **Setup** (2-3 lines) â€” Establish credibility/context fast
3. **Sections** â€” Each follows: problem â†’ what actually happened â†’ fix/lesson
4. **ASCII diagram** â€” At least one per post (see below)
5. **Uncomfortable truth** â€” The insight most people avoid
6. **Payoff** â€” Was it worth it? Yes, and here's why.

---

## ASCII Diagrams (MANDATORY)

Every post MUST include at least one ASCII diagram in a code block. These break up walls of text and make complex systems visual.

Use box-drawing characters:
```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚  Input  â”‚â”€â”€â”€â–ºâ”‚ Process â”‚â”€â”€â”€â–ºâ”‚ Output  â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

Diagram types to use:
- **System architecture** â€” boxes connected by arrows showing how components relate
- **Before/after** â€” side-by-side comparison of old vs new state
- **Flow diagrams** â€” decision trees, pipelines, sequences
- **Hierarchy** â€” org charts, priority stacks, dependency trees
- **Metrics** â€” simple bar charts using block characters (â–ˆ â–“ â–‘)

Keep diagrams:
- Under 40 chars wide (mobile rendering)
- Simple enough to parse in 3 seconds
- Labeled clearly â€” no ambiguous boxes

Example â€” system flow:
```
Input (60s)
    â”‚
    â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Process  â”‚ step 1
â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜
     â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Dispatch â”‚ step 2
â””â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜
     â–¼
  Output
```

Example â€” metrics visualization:
```
Performance by Category:
Category A   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ 100%
Category B   â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–‘â–‘â–‘â–‘  67%
Category C   â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘   0%
```

---

## Formatting for X

- X articles support markdown-like formatting in long posts
- Use code blocks (```) for ASCII art â€” they render in monospace on X
- Bold with asterisks where supported
- Keep paragraphs to 1-3 sentences max
- Line breaks between every thought

---

## Content Sources

Pull from real data whenever possible:
- Real metrics from your business
- Specific incidents and debugging stories
- Actual decisions made and why

Never fabricate metrics. Use real numbers or don't use numbers.

---

## Analytics Feedback Loop

If X/Twitter analytics are available, use them before drafting and after publishing.

Before drafting:
- Pull recent post performance for similar topics and formats.
- Compare impressions, engagement rate, replies, reposts, bookmarks, profile clicks, follower delta, post length, hook style, proof number, CTA type, and topic bucket.
- Prefer hooks and structures that have actually worked. Do not worship cleverness. Cleverness without distribution is theater with better fonts.

After publishing:
1. Log post URL/id, publish time, hook, title, proof number, structure, CTA, and topic bucket.
2. Pull analytics after the readback window.
3. Compare against a baseline cohort of similar posts.
4. Patch the title formulas, hook patterns, CTA rules, or section structure only if the candidate beats baseline or produces a clearly better audience signal.

Judgment metrics:
- impressions
- engagement rate
- replies
- reposts
- bookmarks
- profile clicks
- follower delta
- quality of replies

Every promoted format change should include a baseline window, candidate window, metric winner, caveats, and rollback rule.

---

## Input Format

User provides:
- **Topic**: What the post is about
- **Angle**: The contrarian or unique framing
- **Source material**: Real examples, data, incidents (optional)

---

## Output

Deliver the complete post ready to paste into X. No preamble, no "here's your post" â€” just the post itself.

If the post would work better as a thread (>1500 chars), split into numbered tweets with each one standalone valuable.

---

## Reference

See `references/founder-voice.md` for extended voice examples and patterns. Customize with your founder's real voice.

---

## Humanizer Checklist (MANDATORY â€” Run Before Finalizing)

Before returning any X article draft, check against ALL 24 humanizer patterns. If any pattern is detected, rewrite that section.

For the full humanizer expert scoring rubric, see: `../content-ops/experts/humanizer.md`

### CRITICAL: No "Not X, It's Y" Constructions
Never write "This is not X. This is Y." or "That is not X, that is Y." or any variant. These are the #1 AI slop tell. Say what something IS directly. Don't define by negation.

### Banned Vocabulary (never use these)
delve, tapestry, landscape (abstract), leverage, multifaceted, nuanced, pivotal, realm, robust, seamless, testament, transformative, underscore (verb), utilize, whilst, keen, embark, comprehensive, intricate, commendable, meticulous, paramount, groundbreaking, innovative, cutting-edge, synergy, holistic, paradigm, ecosystem, Additionally, crucial, enduring, enhance, fostering, garner, highlight (verb), interplay, intricacies, showcase, vibrant, valuable, profound, renowned, breathtaking, nestled, stunning

### Pattern Checklist
1. â˜ No significance inflation ("pivotal moment", "stands as", "is a testament")
2. â˜ No undue notability claims (listing media mentions without context)
3. â˜ No superficial -ing phrases ("highlighting", "showcasing", "underscoring")
4. â˜ No promotional language ("boasts", "vibrant", "profound", "commitment to")
5. â˜ No vague attributions ("Experts believe", "Industry reports suggest")
6. â˜ No formulaic "despite challenges... continues to" structures
7. â˜ No AI vocabulary clustering (multiple banned words in one paragraph)
8. â˜ No copula avoidance ("serves as", "stands as" â€” just use "is")
9. â˜ No negative parallelisms ("It's not just X, it's Y")
10. â˜ No rule-of-three forcing (triple adjectives, triple parallel clauses)
11. â˜ No synonym cycling (varying terms for the same thing unnecessarily)
12. â˜ No false ranges ("from X to Y" on no meaningful scale)
13. â˜ No em dash overuse (max 1 per 200 words)
14. â˜ No mechanical boldface emphasis
15. â˜ No inline-header vertical lists (bolded label + colon pattern)
16. â˜ No Title Case In Every Heading
17. â˜ No emoji decoration on headings/bullets
18. â˜ No curly quotation marks
19. â˜ No collaborative artifacts ("I hope this helps", "Let me know")
20. â˜ No knowledge-cutoff disclaimers
21. â˜ No sycophantic tone ("Great question!")
22. â˜ No filler phrases ("In order to", "It is important to note")
23. â˜ No excessive hedging ("could potentially", "might have some effect")
24. â˜ No generic positive conclusions ("The future looks bright", "Exciting times ahead")

### Humanizer Scoring

Start at 100. Deduct points per the rubric in `../content-ops/experts/humanizer.md`.

- **90-100**: Human-sounding. Clean. Ship it.
- **70-89**: Minor AI tells. Quick fixes needed.
- **50-69**: Obvious AI patterns. Significant rewrite needed.
- **0-49**: Full rewrite.
