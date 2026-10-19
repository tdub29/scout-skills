# Heath: Curse of Knowledge

## When to use

Trigger when the question is "why doesn't my audience get this?" and the user is the expert. Concrete cues:

- An expert / specialist / founder / engineer / scientist / academic / domain insider has a message that isn't landing
- "I keep explaining this but nobody understands" / "Why are they still asking the same questions"
- A pitch deck or board update where the user assumes context the audience doesn't have
- Internal documentation that new hires can't follow
- Customer-facing content written by engineers and now needs to be human-readable
- A teacher / coach realizes students are struggling with what feels obvious to them
- "This should be obvious" or "they should know this" is in the user's vocabulary
- Preparing to communicate cross-functionally (eng â†’ sales, finance â†’ product, etc.)

Don't trigger for: grammar-level fixes (use `prose-style`), routine copy editing (`copy-editing`), pure persuasion-mechanism rebalancing (`aristotle-three-modes-of-persuasion`). This skill operates at the *diagnosis* layer â€” what context is hidden and how to surface it. Once the curse is diagnosed, downstream SUCCESs skills (`heath-finding-the-core`, `heath-concrete`, etc.) do the rewriting.

## The framework

### Core thesis

Heath's central insight: once you know something, you cannot unknow it. Your brain *automatically* fills in the context that surrounds the knowledge â€” the prerequisites, the vocabulary, the unstated "everyone knows" assumptions. To you, the message feels complete; to a non-expert, half the message is missing because you didn't realize you were leaving it out. The Heath brothers call this the *curse of knowledge*, and they argue it is the single biggest reason expert communication fails.

The canonical experiment (Elizabeth Newton, 1990, "Tappers and Listeners"): tappers were asked to tap out a well-known song. Listeners had to guess the song. Tappers predicted listeners would guess correctly ~50% of the time. The actual rate: 2.5%. The tappers heard the song in their head while tapping â€” for them, the rhythm was obvious. The listeners heard only a series of disconnected taps. The tappers couldn't *unfeel* knowing the song.

Every expert-to-novice communication has the same asymmetry. The expert hears the full song. The audience hears taps. The expert wonders why the audience isn't getting it. The audience wonders what the hell the expert is talking about.

### Why the curse can't be uncursed

You cannot un-learn what you know. The curse is irreversible. The only two ways to beat it:

1. **Don't learn the thing** â€” useless, you're the expert
2. **Transform your message** using techniques that *bridge* the gap â€” the six SUCCESs principles (Simple, Unexpected, Concrete, Credible, Emotional, Stories), each of which forces you to use schemas your audience already has, not the ones you have

This is why Heath structures the entire book as "the villain (curse of knowledge) and the six weapons against it (SUCCESs)." Each principle is a forcing function that surfaces hidden context.

### Symptoms of the curse

Recognizable symptoms in a draft message:

- **Jargon dependency** â€” the message uses domain-specific terms without defining them
- **Unstated prerequisites** â€” the message assumes the audience has background they don't have
- **Abstraction inflation** â€” concrete examples are absent because they feel "too elementary" to the expert
- **Bullet-point compression** â€” the expert has packed complex ideas into terse bullets that *they* can decompress, but the audience can't
- **The "everyone knows" trap** â€” "Everyone knows X" is in the message when the audience often doesn't
- **Frustrated rewriting** â€” the expert has rewritten the same explanation 5 times, each time clearer to them but still confusing to the audience
- **Asymmetric Q&A** â€” audience questions feel "off-topic" to the expert because the audience is asking about the unstated context

### Beating the curse â€” the structural moves

Heath identifies the moves that work (operationalized in the per-principle skills):

1. **Find the core** (route to `heath-finding-the-core`) â€” strip to the one essential message. Forces you to admit what's *not* in the core, which exposes what you were assuming the audience already had.

2. **Use unexpected hooks** (route to `heath-unexpected`) â€” break the audience's pattern. Forces you to identify what schema your audience IS working from, which is the schema your message has to bridge.

3. **Use concrete language** (route to `heath-concrete`) â€” sensory specifics + named examples. The opposite of abstraction. The expert's natural mode is abstract; concrete is forced.

4. **Make claims testable** (route to `heath-credible`) â€” let the audience verify rather than trust your expertise. Forces you to design proof that doesn't require expert-level pre-context.

5. **Make it emotional / identity-relevant** (route to `heath-emotional`) â€” translate "this matters because X technical reason" into "this matters because of who you are / what you'll feel." Forces translation from expert frame to audience frame.

6. **Tell stories** (route to `heath-stories`) â€” narrative simulation. Audiences who can't follow an abstract principle CAN follow a story illustrating it; the story does the simulation work the audience's brain needs.

### Manipulation risk

The curse-of-knowledge framework is *defensive* â€” its purpose is to make experts more accessible to non-experts. Manipulation risks are limited but real:

- **False simplification.** Stripping context until the message is no longer true. The audience can act on a clear-but-wrong message faster than they can fail to act on a confused-but-correct one. Honest debridging keeps the message true; manipulation strips truth in the name of clarity. Test: would a domain expert agree the simplified version is still substantively correct?
- **Hidden complexity.** Selling clarity that hides material tradeoffs the audience needs to know about (e.g., "this surgery is safe" without disclosing the 5% complication rate). Curse-bridging should reveal what's relevant, not omit what's inconvenient.
- **Manipulating the expert's apparent confidence.** A confident-sounding bridged message can read as if all complexity is resolved when it isn't. Acknowledge open questions and uncertainty even in the simplified version.

The honest version: bridge the curse to help the audience *act* well; don't bridge it to help yourself *win*.

## How to apply (step-by-step)

1. **Confirm the expert-novice gap exists.** Who is the audience? What do they actually know about this topic vs. what does the user (expert) know? If you can't name 3 specific things the user knows that the audience doesn't, the curse may not be the dominant problem â€” route elsewhere.

2. **Inventory the unstated assumptions.** Walk through the draft message and list every concept, term, prerequisite, or context that the user assumed the audience would supply. Categorize:
   - Jargon (terms not defined)
   - Prerequisites (assumed knowledge the audience may not have)
   - Implied causal chains (the expert sees Aâ†’Bâ†’C; the audience needs to see them spelled out)
   - "Everyone knows" assumptions

3. **Test the message on a non-expert proxy.** Either find a real non-expert and read them the message, OR mentally simulate: a colleague from a different function reading this draft cold. Where do they get lost? What do they ask?

4. **Diagnose which SUCCESs principle is most missing.** Each principle attacks the curse from a different angle. Map the failure mode:
   - If the audience doesn't grasp the priority of the message â†’ `heath-finding-the-core`
   - If the audience tunes out before they start engaging â†’ `heath-unexpected`
   - If the audience nods along but can't recall specifics â†’ `heath-concrete`
   - If the audience doubts the claim â†’ `heath-credible`
   - If the audience understands but doesn't care â†’ `heath-emotional`
   - If the audience needs to internalize a complex behavior â†’ `heath-stories`

5. **Generate the bridging rewrite.** Produce the rewritten message:
   - Define every jargon term on first use (or replace with plain language)
   - Make implicit prerequisites explicit ("This assumes you're familiar with X â€” if not, here's what X is in one sentence")
   - Replace abstractions with concrete examples
   - Use schemas the audience already has (analogies to things they know)
   - Acknowledge what you, the expert, find easy but they may find hard

6. **Run the manipulation-risk check.**
   - Is the simplified version still substantively correct? (Would a fellow expert agree?)
   - Have you hidden complexity that the audience needs to know to make a good decision?
   - Have you projected false confidence that resolves uncertainty the user actually has?

7. **Produce the audit document.** Three sections: (a) what the user knows that the audience doesn't (the inventory), (b) which SUCCESs principle(s) are weakest in the current draft, (c) the rewrite with annotations showing where each bridging move happened.

8. **Sanity-check by reading aloud to a non-expert.** The actual test. Does the non-expert now understand? Can they paraphrase back? Can they ask informed questions? If not, iterate on the weakest principle.

## Common failure modes

- **The expert insists the audience "should know" the assumed context.** Maybe the audience should, but they don't, and "should" doesn't communicate. The curse doesn't care about whose fault the gap is; it only cares whether the message lands. Fix the message, not the audience.

- **Bridging that loses domain accuracy.** Over-simplification in the name of clarity can produce a message a domain expert would call wrong. The fix: bridge with analogies and concrete examples that *preserve* the substance, not strip it.

- **Confusing the curse with general "be clearer" advice.** Clarity in prose is one tool against the curse, but the curse can persist in perfectly clear prose if the prose still assumes context the audience doesn't have. Diagnose the gap, then bridge it; don't just rewrite the sentences.

- **Diagnosing the curse but skipping the SUCCESs follow-up.** Naming the curse is the first step; the bridging happens through the six principles. A curse audit without a follow-on rewrite is just a complaint about communication, not a fix.

- **Treating the curse as the only diagnosis.** Sometimes communication fails for reasons other than the curse â€” wrong genre (use `aristotle-three-genres`), wrong emotion (`aristotle-emotions`), bad prose (`prose-style`). Run the curse diagnosis first because it's foundational; if the curse isn't the problem, route to whatever else is.

- **The "I tested it on my team" trap.** Your team isn't your audience. Your team has been exposed to the same jargon, the same context, the same framing as you. They're cursed too, just in your direction. Test on someone outside the in-group.

- **Bridging too far.** Some technical messages need a technical audience and shouldn't be simplified into uselessness. The "explain it to a fifth-grader" trope is often wrong â€” the right test is "explain it to the *actual* audience," which may be sophisticated professionals from a different domain. Calibrate bridging to the *actual* gap, not to a generic non-expert.

- **Skipping the truth-preservation check.** Simplification that breaks accuracy isn't curse-bridging, it's dumbing down. The fix is bridging that *preserves* the substantive claim, not bridging that swaps a hard truth for an easy lie.

- **Forgetting the curse applies to YOU running this skill.** Reading a curse-of-knowledge audit is also subject to the curse â€” once you understand the framework, you'll assume others do too. Apply the curse-bridging moves to your own communication about the curse.

## References

- Chip Heath and Dan Heath, *Made to Stick: Why Some Ideas Survive and Others Die* (Random House, 2007), Introduction. The "tappers and listeners" experiment (Elizabeth Newton, 1990) is described on pages 19â€“20; the framing of curse-of-knowledge as the villain that the SUCCESs principles fight runs through the entire book.

- Sibling carved Heath skills (the six weapons against the curse):
  - `heath-finding-the-core` â€” Chapter 1 (Simple)
  - `heath-unexpected` â€” Chapter 2 (Unexpected)
  - `heath-concrete` â€” Chapter 3 (Concrete)
  - `heath-credible` â€” Chapter 4 (Credible)
  - `heath-emotional` â€” Chapter 5 (Emotional)
  - `heath-stories` â€” Chapter 6 (Stories)

- Related skills:
  - `prose-style` â€” sentence-level craft (works downstream of curse diagnosis)
  - `aristotle-three-modes-of-persuasion` â€” different layer: which mode (ethos / pathos / logos) needs work, vs. which knowledge gap to bridge
  - `clarify` â€” sentence-level UX copy work, complementary to bridging at the message-design layer
