# Aristotle: Speech Arrangement (Taxis)

## When to use

Trigger when the question is "in what order should this persuasive piece go?" â€” for an extended artifact where structure matters. Concrete cues:

- The user is outlining a speech, pitch deck, op-ed, keynote, sermon, debate opening, or court filing
- A draft "doesn't flow right" and the user suspects a structural problem, not a sentence-level one
- "Where do I put the strongest evidence?" / "Should I open with the story or the claim?"
- The user is preparing a 20-minute talk and has 8 things to say but no order
- A pitch deck where the slides are individually fine but the deck as a whole doesn't build to anything
- The user is rewriting an existing piece that has the right content but the wrong arrangement
- A fundraising appeal, manifesto, or persuasive essay that needs to escalate to a clear ask at the end
- Long-form: a video essay, a podcast monologue, a keynote address, a memoir-style persuasive piece

Don't trigger for: sentence-level writing (use `aristotle-style` or `prose-style`), genre classification (use `aristotle-three-genres` first â€” arrangement varies by genre), short-form copy with no room for 4-part structure (a tagline, a single-paragraph ad, a tweet). This skill is for extended persuasive artifacts where the order of arguments actually changes the result.

## The framework

### Core thesis

Aristotle's claim about arrangement: a persuasive piece has at most four functional parts â€” proem, narration, proof, epilogue â€” and the audience experiences them in that order whether the writer designed them deliberately or not. Designing them deliberately means controlling what the audience encounters first (proem), what facts they're handed (narration), how those facts are argued (proof), and what they walk away with (epilogue). Skipping a part or putting them in the wrong order doesn't remove them â€” it just means they happen accidentally.

The four parts adapt to genre:
- **Deliberative** (future-oriented decisions): narration may be brief or absent; proof and epilogue dominate
- **Forensic** (past wrongdoing): narration is critical (the facts of what happened); proof centers on motive and evidence; epilogue often carries the emotional appeal
- **Epideictic** (ceremonial praise/blame): narration may be intermittent (interspersed with proof); proof is the demonstration of virtue or vice; epilogue intensifies

Modern artifacts that don't *look* like classical speeches â€” pitch decks, op-eds, fundraising emails â€” still follow the 4-part pattern. The opening establishes credibility and frames the question (proem). The middle provides context and evidence (narration + proof). The close drives toward action with emotional weight (epilogue). Recognizing the underlying structure lets you diagnose what part is missing or weak in a draft.

### Part 1: Proem (the introduction)

**Function.** Secure the audience's attention and goodwill. Establish the speaker's credibility (ethos). Frame what the speech is about and why the audience should care.

**Moves.**
- Open with a strong line â€” quotable, surprising, or directly relevant. The audience decides whether to listen within the first 30 seconds (in a speech) or the first paragraph (in writing).
- Establish ethos: signal phronesis (you know the topic), arete (you're truthful), eunoia (you care about the audience). This is *built in the speech*, not borrowed from a bio.
- State the thesis or the question, depending on genre. Deliberative: name the decision. Forensic: name the dispute. Epideictic: name the subject of praise/blame.
- Lower defenses if the audience is hostile. Acknowledge their concerns. Demonstrate you've thought about the opposing view.

**Genre variations.**
- *Deliberative:* short proem; state the question and your position quickly. Audiences considering future action want efficiency.
- *Forensic:* longer proem if the case is complex; address audience predispositions about the accused before laying out the evidence. The audience's emotional state at the proem is a barrier or accelerator for everything that follows.
- *Epideictic:* the proem itself often carries praise/blame â€” opening lines can be the most rhetorical of the whole piece (the famous opening of a eulogy that everyone remembers).

**Common failure.** Generic opening â€” "Today I want to talk about..." â€” that wastes the most attention-rich moment of the piece. The proem is rhetorical real estate; treat it as such.

### Part 2: Narration (the statement of facts)

**Function.** Lay out the relevant facts the audience needs to understand the case. Provide the context the proof will build on. Aristotle is clear: narration is about *what happened* (or *what is the case*), told plainly enough to be understood and arranged to support what comes next.

**Moves.**
- Tell the relevant facts in an order that makes the proof's argument easier to follow.
- Include the facts the opposition will use, even briefly â€” better to acknowledge them under your framing than to have them surface in opposition.
- Vary pace: dwell on the facts that matter most; summarize the rest.
- Maintain credibility by being accurate. The audience's trust in the narration affects their willingness to accept the proof.

**Genre variations.**
- *Deliberative:* often brief or absent â€” the audience knows the situation; jump to the decision. Long narrations in deliberative speech feel like the speaker doesn't trust the audience.
- *Forensic:* continuous and detailed â€” the audience needs the facts as a foundation for the proof. The narration is where the case is largely won or lost; the proof confirms what the narration has set up.
- *Epideictic:* intermittent â€” narration is woven through the proof rather than presented as a single block. The audience encounters the facts of the subject's life or actions as they relate to each virtue being demonstrated.

**Common failure.** Burying the proof inside the narration â€” "and here's what actually happened, and by the way here's why that means I'm right" â€” instead of separating them so each does its job cleanly.

### Part 3: Proof (the argument)

**Function.** Establish the case through argument. This is where enthymemes (compressed syllogisms) and examples (rhetorical induction) do their work. Proof is the rhetorical center of gravity in most pieces.

**Moves.**
- Lead with the strongest argument or save it depending on audience disposition. With a hostile or skeptical audience, lead strong; the early skepticism needs the heaviest counter. With a sympathetic audience, you can build (Aristotle's preference in some contexts is to put the strongest argument *in the middle*, framed by adequate openings on each side â€” neither the first thing the audience hears nor the last).
- Use enthymemes to drive logical force. The audience completes the unstated premise, which makes the argument feel like theirs.
- Use examples to support enthymemes â€” pattern recognition reinforcing deductive argument.
- Address the opposing case directly: acknowledge â†’ refute. Hiding the opposition makes the eventual encounter with it more damaging.

**Genre variations.**
- *Deliberative:* proof centers on consequences, expediency, precedent. "If we do X, Y will follow; if we don't, Z will follow."
- *Forensic:* proof centers on motive, means, opportunity, character, victim profile â€” the systematic forensic framework (route to `aristotle-forensic-analysis` for the deep operationalization).
- *Epideictic:* proof centers on enumerated virtues or vices with specific exemplary actions. "She demonstrated courage by doing X; wisdom by doing Y."

**Common failure.** Weak proof structure â€” listing points without an argumentative arc. The audience experiences "and another thing, and another thing" rather than "because of A, B follows; and B implies C; and C is the case." The proof should escalate.

### Part 4: Epilogue (the conclusion)

**Function.** Aristotle identifies four sub-functions of the epilogue:

1. **Dispose the hearer favorably toward yourself and unfavorably toward the opponent** â€” final ethos calibration
2. **Magnify or minimize the facts** â€” frame the stakes
3. **Excite the appropriate emotion** â€” final pathos move
4. **Refresh the memory** â€” recap the main arguments

The epilogue is where the audience's takeaway gets shaped. What the audience remembers from a long piece is heavily weighted toward the close (recency effect). Aristotle recognized this 2,300 years before behavioral psychology did.

**Moves.**
- Recap the strongest 2â€“3 arguments. Don't introduce new evidence (the audience has already exited the proof phase mentally).
- Magnify the stakes â€” what's at risk if the wrong decision is made. (Stakes inflation is a manipulation move when applied to small things; for real stakes, the epilogue is where they get named.)
- Land the emotional moment. The pathos that you've been preparing throughout should hit hardest here. The audience walks out *feeling*, not just thinking.
- Drive to action or judgment, depending on genre. Deliberative: clear ask. Forensic: clear verdict-implication. Epideictic: clear honor-or-blame.

**Genre variations.**
- *Deliberative:* end with the decision the audience is being asked to make, framed by consequences. "Vote yes, and we will... Vote no, and we will..."
- *Forensic:* end with the emotional weight of the case â€” pity for the wronged or indignation at the wrongdoer. The proof was the spine; the epilogue is the gut-punch.
- *Epideictic:* end with intensified praise or blame â€” the most quotable line of the piece is often here. Brand manifestos, eulogies, victory speeches all live or die on their closes.

**Common failure.** Tapering off. The audience expects climax and gets diminuendo. Either no clear final line, or a polite "thank you for your time" that surrenders the most rhetorically powerful moment of the piece.

### How modern artifacts map to the 4-part structure

The classical structure isn't archaic. Modern persuasive artifacts implement it whether their writers know it or not:

- **Pitch deck:** title + problem (proem) â†’ market / customer / situation (narration) â†’ product / traction / business model (proof) â†’ ask / vision / close (epilogue)
- **Op-ed:** hook + thesis (proem) â†’ context (narration) â†’ argument and counter-argument (proof) â†’ call to action or stakes (epilogue)
- **Fundraising email:** opening line that captures attention (proem) â†’ backstory of the cause (narration) â†’ why this works / track record (proof) â†’ the ask + emotional anchor (epilogue)
- **Keynote:** opening story or provocative line (proem) â†’ context / state of the field (narration) â†’ main argument / new framework (proof) â†’ vision / call to action / memorable closing line (epilogue)

When a modern piece feels structurally off, the diagnosis is usually missing or weak proem or epilogue â€” proof and narration take the most page space and get the most attention, while the structurally crucial first-and-last moments get treated as afterthoughts.

### Manipulation risk

Arrangement is the most ethically loaded structural framework because it weaponizes attention. Specific risks:

- **Epilogue manipulation.** The epilogue's emotional move can be used to override the audience's rational evaluation. If the proof is weak but the epilogue hits hard, audiences walk away persuaded by feeling rather than evidence. The guardrail: epilogue's emotion should *amplify* the case the proof has already made, not *substitute* for proof.
- **Prejudice removal in the proem.** Aristotle himself describes techniques for removing audience prejudice against the speaker or the cause â€” useful when prejudice is unjust, but the same techniques can be used to disarm well-founded skepticism. Check whether the audience's resistance is a *prejudice* (unfair predisposition) or a *legitimate concern* (something you should address with evidence, not technique).
- **Narration framing.** "Just the facts" â€” but the *order* and *emphasis* in narration is selective. Selective omission of facts the opposition would highlight is the most common forensic manipulation move.

Run the manipulation-risk check at each structural position: is this part doing legitimate work for the audience, or laundering weakness in another part?

## How to apply (step-by-step)

1. **Confirm the artifact warrants 4-part structure.** Long enough that order matters? If yes, proceed. If no (short copy, single message), the 4-part framework is overkill; lean on `aristotle-style` or `aristotle-three-modes-of-persuasion` instead.

2. **Confirm the genre.** Deliberative, forensic, or epideictic? The genre determines the natural proportions and the specific moves per part. Route to `aristotle-three-genres` if uncertain.

3. **Draft the proem.** What's the strongest opening move available? Quote, story, surprising claim, provocative question? What ethos does the audience need to feel before they'll engage? What thesis or question frames the piece?

4. **Draft the narration.** What facts must the audience have before the proof can land? Order them to support the proof's argumentative arc. For deliberative: minimize narration; jump to the argument. For forensic: develop narration carefully; this is where the case is built. For epideictic: weave narration into proof.

5. **Draft the proof.** What are the 2â€“4 main arguments? Place them in escalating order, or with the strongest in the middle (Aristotle's "Nestor formation"). Acknowledge and refute the opposing case explicitly.

6. **Draft the epilogue.** Recap the main arguments. Name the stakes. Land the emotional move. Drive to the action (deliberative ask) / verdict-implication (forensic) / intensified praise-or-blame (epideictic). The final line should be the most quotable in the piece.

7. **Audit the proportions against genre.**
   - Deliberative: brief proem + brief narration + substantial proof + strong epilogue
   - Forensic: substantial proem (especially for hostile audiences) + detailed narration + structured proof + emotionally weighted epilogue
   - Epideictic: stylistically rich proem + interwoven narration/proof + intensified epilogue

8. **Manipulation-risk check.**
   - Is the proem disarming legitimate skepticism, or removing genuine prejudice?
   - Is the narration honest about the facts the opposition would highlight?
   - Does the proof actually prove the case, or rely on the epilogue's emotional close to compensate?
   - Does the epilogue amplify the proof's case, or substitute for weak proof?

9. **Produce the arrangement plan.** Per part: function, key moves, genre-specific notes, manipulation-risk status, and the specific lines or moments the user has already drafted that should anchor each part.

## Common failure modes

- **Weak proem.** "Today I want to talk about..." or "First let me give you some background..." â€” wasting the most attention-rich moment. The proem should be the strongest opening you can write. If the rest of the piece is solid but no one remembers the opening, fix the proem first.

- **Bloated narration.** Spending two-thirds of the piece on background context, leaving the proof and epilogue rushed. Audiences want to hear *the argument*, not *all the context the argument depends on*. Compress narration ruthlessly; trust the audience.

- **Proof without arc.** Listing arguments rather than building them. The audience experiences "here's one point, here's another point, here's a third" instead of "given A, B; given B, C; therefore D." Arrange proof so each argument builds on the prior.

- **Epilogue as afterthought.** Ending with "thank you" or "I'm happy to take questions" surrenders the most powerful structural position. The epilogue is where audiences form their walk-away â€” design it deliberately.

- **Introducing new evidence in the epilogue.** The audience has mentally exited the proof phase by the time you reach the close. New evidence there feels unfair and is often missed. If a piece of evidence is important, put it in the proof.

- **Mismatched arrangement to genre.** Applying forensic arrangement (long narration + heavy proof + emotional epilogue) to a deliberative pitch (which wants efficient proem + light narration + strong proof + clear-ask epilogue). The audience experiences the wrong-genre arrangement as a mismatch even when each part is individually good.

- **Skipping the manipulation-risk check on the epilogue.** Powerful epilogues can carry weak cases through audience emotional momentum. The ethical version: the epilogue's emotion is *proportional* to the proof's strength. If the epilogue is the only thing holding the piece together, the piece is structurally manipulative.

- **Treating arrangement as optional for short-form.** A 90-second pitch still has a proem (the hook), narration (the situation), proof (why this works), and epilogue (the ask). The parts are compressed but present. Treating short-form as "no structure needed" produces forgettable pitches.

- **Confusing this skill with `aristotle-style`.** Arrangement is *structural* (which part comes when, what each part does). Style is *sentence-level* (how each part is written). Run arrangement first to get the structure right, then style to make each part land.

- **Refusing to commit to a single arrangement.** Some pieces try to be "experimental" â€” non-linear, fragmented, deliberately disordered. This works in some literary and artistic contexts; for *persuasive* artifacts, the 4-part structure works because audiences have predictable attention patterns. Experimental arrangement in a pitch deck or fundraising appeal usually just confuses the audience.

## References

- Aristotle, *Rhetoric* (W. Rhys Roberts translation; Megaphone eBooks 2008), Book III:
  - Parts 13â€“14 (lines ~8200â€“8500): the parts of a speech defined; proem moves
  - Part 16 (lines ~8500â€“8800): narration â€” how to handle the statement of facts per genre
  - Parts 17â€“18 (lines ~8800â€“9000): proof â€” placement, sequencing, acknowledgment of opposition
  - Part 19 (lines ~9000â€“9180): epilogue â€” the four sub-functions (favorable disposition, magnify/minimize, emotion, memory)

- Sibling carved Aristotle skills:
  - `aristotle-three-genres` â€” determines the natural proportions and specific moves per part; run before this skill
  - `aristotle-three-modes-of-persuasion` â€” each part delivers a different mix of ethos/pathos/logos
  - `aristotle-emotions` â€” the epilogue is the prime placement for pathos work
  - `aristotle-forensic-analysis` â€” forensic-genre proof centers on motive/state-of-mind/victim-fit
  - `aristotle-style` â€” sentence-level craft, with style choices that vary by structural position (higher ornament in proem and epilogue than in proof and narration)

- The 4-part structure is the ancestor of every modern essay / pitch / speech template; recognizing the underlying classical pattern makes it easier to diagnose what's missing in any modern persuasive artifact.
