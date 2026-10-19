# Aristotle: The Three Genres of Rhetoric

## When to use

Trigger when the question is "what kind of argument is this supposed to be?" â€” and the answer is non-obvious. Concrete cues:

- The user is starting a persuasive piece and the genre is ambiguous (a pitch that's also a celebration, a memo that's also an accountability moment)
- A draft "feels off" and the user can't name why â€” often because it mixes genres
- "Should I lead with consequences (future), evidence (past), or virtues (present)?"
- A board meeting that mixes deliberation about a future decision with retrospective accountability for past results
- An op-ed that argues policy (deliberative) while taking down a specific opponent (forensic-flavored)
- A eulogy that drifts into "what should we do now" (deliberative drift in an epideictic moment)
- A keynote that's billed as visionary (epideictic) but reads like a sales pitch (deliberative)
- The user is teaching someone else and wants a teachable framework for argument classification

Don't trigger for: pure persuasion-mechanism analysis (use `aristotle-three-modes-of-persuasion`), generic chart/data-viz work, sentence-level prose. This skill answers ONE prior question: what *kind* of argument is appropriate here?

## The framework

### Core thesis

Aristotle's claim: every piece of rhetoric belongs to exactly one of three genres, each defined by what the audience is being asked to *do*. The audience's role determines the time orientation, the proof obligations, the natural emotions, and the topoi (lines of argument) appropriate to the piece. Mixing genres â€” asking the audience to be a deliberator about future action AND a judge of past wrongdoing AND a celebrant of present virtue â€” fragments the rhetorical work.

The three genres are exhaustive: every persuasive artifact (speech, memo, pitch, op-ed, fundraising email, eulogy, court filing, legislative testimony, branding campaign) falls into one. Some artifacts blend two (a policy speech that includes praise for the proposal's supporters is mostly deliberative with epideictic flavoring), but one genre always dominates.

### Deliberative (political / future-oriented)

**Audience role:** deliberator â€” someone who must decide what to do.
**Time orientation:** future.
**Persuasive end:** the *expedient* (advantageous) vs. the *harmful*; what serves the audience's interest.
**Native question:** "Should we do this?"

Examples: a board pitch, a policy speech, a legislative testimony, a fundraising appeal, a strategic memo, a "we should pivot" all-hands. Modern equivalents include sales pitches, investment memos, product proposals, RFPs, and most business writing aimed at a decision.

**Natural argument moves:** cost-benefit comparison; consequences if we act vs. if we don't; risk; precedent (when similar decisions worked / didn't work); the speaker's expertise on the relevant domain; alignment with the audience's values and goals.

**Native pathos:** hope (this will work) and fear (failing to act has consequences) are the dominant emotions; confidence and resolve are common; pride in successful outcomes for epideictic borrowing.

### Forensic (judicial / past-oriented)

**Audience role:** judge â€” someone determining whether something happened and how to weigh it.
**Time orientation:** past.
**Persuasive end:** the *just* vs. the *unjust*; what actually occurred and what should follow from it.
**Native question:** "Did this happen, and was it right?"

Examples: a court case (the original context); a post-mortem; an accountability conversation; an investigation findings report; a regulatory filing about past conduct; a journalism piece exposing wrongdoing. Modern equivalents include incident reviews, audit reports, retrospective performance evaluations, and any piece arguing about who's responsible for a past outcome.

**Natural argument moves:** evidence about facts; arguments about motive (why would someone do this?); arguments about means and opportunity; character of the actor; precedents and norms violated; comparison to similar past cases.

**Native pathos:** indignation at wrongdoing; pity for victims; anger at violation; the cooler emotions of judgment (vs. the urgent emotions of deliberation).

For deep operationalization of forensic-genre proof, see `aristotle-forensic-analysis`.

### Epideictic (ceremonial / present-oriented)

**Audience role:** observer â€” someone witnessing and recognizing virtue or vice.
**Time orientation:** present (though it draws on past actions to demonstrate present worthiness).
**Persuasive end:** the *honorable* / *praiseworthy* vs. the *shameful* / *blameworthy*.
**Native question:** "Is this person / thing / movement worthy?"

Examples: a eulogy, a wedding speech, an award acceptance, an obituary, a brand-purpose manifesto, an inaugural address, a graduation keynote, a "thank you" speech, a movement statement, a victory speech. Modern equivalents include brand mission statements, founders' letters, "company values" docs, hall-of-fame inductions, anniversary celebrations, and most ceremonial speech.

**Natural argument moves:** enumeration of virtues; specific actions that exemplify those virtues; comparison to historical exemplars; identification with shared values; aesthetic intensification (this person / cause is *uncommonly* worthy).

**Native pathos:** admiration, gratitude, pride, awe; the celebratory emotions. For blame: indignation, contempt.

### Why genre mismatch is the most common rhetoric failure

Most "this piece feels off" diagnoses trace to genre confusion:

- **Deliberative dressed as epideictic.** A sales pitch that tries to be a vision speech. The audience expects "should we buy this?" arguments and gets "isn't this amazing?" assertion. The result feels light on substance.
- **Forensic dressed as deliberative.** A "let's talk about the future" memo that's actually about past blame. The audience braced for collaboration encounters accusation. Trust drops.
- **Epideictic dressed as deliberative.** A eulogy that includes "we should all therefore donate to X." The audience came to mourn and feels emotionally bait-and-switched.
- **Deliberative dressed as forensic.** A retrospective that turns into a "and so here's what we should change going forward" â€” fine, but the audience hasn't finished processing past accountability and the forward-look feels rushed.

The diagnostic is always: what is the audience being asked to *do*? Decide a future course (deliberative)? Judge a past action (forensic)? Recognize present worthiness (epideictic)? Once you know, the genre is set, and arguments / emotions / structure follow.

### Manipulation risk â€” by genre

Each genre has its own ethical traps:

- **Deliberative misuse:** false urgency (manufactured future threats), exaggerated benefits, hidden costs, biased precedent selection.
- **Forensic misuse:** prosecuting people for things they didn't do; cherry-picked evidence; using the structure of accusation to discredit while pretending neutrality.
- **Epideictic misuse:** hagiography (false elevation of someone undeserving); blame campaigns that use the structure of "naming vices" to demonize disagreement.

A piece that performs the genre's form (deliberative balance-sheet, forensic evidence-presentation, epideictic virtue-enumeration) without honestly meeting the genre's truth-obligation is the propaganda failure mode. Genre is form; honesty is what makes the form serve the audience rather than exploit it.

### Hybrids and dominant genres

A piece can have flavoring from another genre â€” a deliberative pitch can include brief epideictic praise for the team's track record; a forensic post-mortem can pivot to deliberative recommendations at the end. The rule: one genre *dominates*, the others *flavor*. If the user can't name the dominant genre in one sentence, the piece is fragmented and needs structural rework.

## How to apply (step-by-step)

1. **State the audience's task.** In one sentence: what is the audience being asked to do as a result of this piece? Decide a future action? Judge a past action? Recognize present worthiness?

2. **Identify the dominant genre.** Map the task to deliberative / forensic / epideictic. If you can't pick one, that's the diagnosis â€” the piece is mixed and needs simplification.

3. **List the natural moves for that genre.**
   - Deliberative: consequences, expediency, future precedent
   - Forensic: evidence, motive, means, justice, comparison to similar cases
   - Epideictic: virtues, exemplary actions, identification with shared values

4. **Check the draft against the natural moves.** Is the draft using the genre's appropriate proof modes, or is it borrowing arguments from a different genre? (E.g., a deliberative pitch that's arguing "she's a virtuous person, so the proposal is good" â€” that's epideictic content inside a deliberative frame, and it weakens both.)

5. **Identify flavoring opportunities.** Where would a brief touch of another genre strengthen the piece? Deliberative pieces often benefit from a moment of epideictic recognition (acknowledge the people involved); forensic pieces often need deliberative pivot at the end (so what do we do now). But these are *touches*, not co-dominant genres.

6. **Check for genre-mismatch trouble spots.** Does any section read like it's from a different genre than the rest? Either rewrite to the dominant genre or move it to a sibling piece (e.g., the celebration moment doesn't belong in the post-mortem; it belongs in the separate retrospective email).

7. **Apply the genre's manipulation-risk check.**
   - Deliberative: are consequences honest? Are costs disclosed?
   - Forensic: is evidence representative? Are facts verified?
   - Epideictic: is the virtue real, or being projected onto someone or something undeserving?

8. **Produce the genre diagnosis.** One sentence naming the dominant genre + a list of which moves to add/strengthen + a flag for any genre-mixing that should be either re-genred or split off.

## Common failure modes

- **Refusing to commit to a dominant genre.** "It's both a decision piece AND a celebration." Almost certainly it's primarily one with flavoring from the other; the user just hasn't decided. Forcing the choice usually resolves the structural problem.

- **Confusing audience-task with topic.** A piece *about* a past event can be deliberative if the audience-task is future-oriented (what should we do given what happened). The topic is past; the genre is deliberative. Topic-vs-genre confusion is common.

- **Applying epideictic moves to deliberative artifacts.** "Our team is amazing, our culture is unique, our mission is to change the world." That's all epideictic content. In a deliberative pitch (we want money / approval / a decision), it weakens the argument because the audience expected "here are the consequences if you say yes vs. no." Save the epideictic content for a separate brand / mission piece.

- **Applying deliberative moves to epideictic artifacts.** A eulogy that turns into "we should all therefore live like this" is intrusive; the audience came to mourn, not be exhorted. Let epideictic do its native work: recognize, honor, intensify.

- **Forensic accusation inside a deliberative frame.** A "let's plan the next quarter" meeting that turns into a blame session. If accountability is needed, schedule it separately as its own forensic-genre conversation. Don't smuggle accusation into a forward-looking frame; the genre mismatch destroys trust.

- **Treating the three genres as exhaustive of all writing.** They aren't â€” Aristotle is specifically about persuasive rhetoric. Purely informational writing (a tutorial, a status report, a reference doc) isn't rhetoric and doesn't fit cleanly into the three. Use this skill when persuasion is the goal; use other skills when information transfer is the goal.

- **Skipping the genre step and going straight to tactics.** "How do I write a more persuasive memo?" without first asking "what *kind* of memo is this?" Most rhetoric advice (modes, style, structure) is genre-conditional. Skipping the genre step is why generic persuasion advice often misses.

- **Manipulation via genre disguise.** Writing a deliberative piece (we should do X) disguised as epideictic (here's a vision) â€” the audience doesn't realize they're being asked to commit until later. Or writing forensic accusation disguised as deliberative discussion â€” naming "concerns" that are really accusations. The fix: be honest about the genre at the top of the piece. If you're asking the audience to decide / judge / honor, say so.

## References

- Aristotle, *Rhetoric* (W. Rhys Roberts translation; Megaphone eBooks 2008), Book I, Part 3, lines 621â€“676 â€” the three divisions of rhetoric introduced. The defining passage: "Rhetoric falls into three divisions, determined by the three classes of listeners to speeches."
- Book I, Parts 4â€“9 cover the topoi of each genre in depth (deliberative topoi: ways and means, war/peace, defense, food supply, legislation. Epideictic topoi: virtues and noble actions. Forensic topoi: justice, wrongdoing, motive â€” all available in `aristotle-forensic-analysis`).

- Sibling carved Aristotle skills:
  - `aristotle-three-modes-of-persuasion` â€” once genre is set, this determines the natural ethos/pathos/logos mix
  - `aristotle-forensic-analysis` â€” deep operationalization of the forensic genre (motive, states of mind, victim profiling)
  - `aristotle-emotions` â€” the systematic pathos catalog used across all three genres
  - `aristotle-speech-arrangement` â€” the structural framework (proem/narration/proof/epilogue) that adapts per genre
  - `aristotle-style` â€” sentence-level rhetorical craft, also adapted per genre
