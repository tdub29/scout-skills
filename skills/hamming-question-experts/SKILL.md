---
name: hamming-question-experts
description: Fires the instant an authority (an expert, a vendor, a senior engineer, a credentialed specialist, a boss) declares something impossible, shuts down a proposal, or answers a challenge with jargon and irrelevant citation instead of engaging the substance. Trust an expert who says something CAN be done; distrust one who says it CANNOT, until the assumptions behind that claim are inspected. Hamming, in "The Art of Doing Science and Engineering: Learning to Learn" (1997), catalogs the expert's track record on impossibility claims (heavier-than-air flight, supersonic flight, lifting water past 33 feet, continental drift) and shows every one rested on an assumption nobody re-checked. Trigger on: an authority calls something impossible or kills a proposal outright; the user is deferring to credentials, titles, or jargon rather than arguments; a vendor or senior person insists a spec limit or established paradigm cannot be exceeded, especially against a live counter-example; the user IS the senior expert and just rejected a junior's idea (run the self-audit and success-trap check on that rejection); a field, team, or product feels paradigm-locked with nobody questioning the assumptions underneath it. FENCE: this fires on AUTHORITY-BACKED IMPOSSIBILITY claims only; it does not produce a probability estimate (route calibration questions to tetlock-superforecasting) and it is not the general cognitive-bias catalog (route anchoring, framing, prospect theory to behavioral-economics). Output is an assumption-audit ledger (claim -> assumptions -> which still hold -> authority-vs-substance flag -> seek outside view) plus an accept/second-opinion/recuse decision.
---

# Hamming: Question the Experts (impossibility audit)

An expert who says something CAN be done is usually right; an expert who says something CANNOT be done has usually skipped a step. This skill is that missing step: pull the assumptions out from under the impossibility claim, check each one against the actual situation, and decide only after the check, not before it. It applies outward, to the experts and authorities you consult, and inward, to yourself once you are the one being consulted.

## When to use

Use this the moment someone with authority, credentials, seniority, or a title says a thing cannot be done, shuts down a proposal without engaging its specifics, or wins the argument by jargon or citation rather than by addressing the proposal itself. It also applies the moment you notice yourself, as the senior person in the room, about to do the same thing.

Cues:

1. An expert, specialist, or vendor says "that's impossible," "that violates X," "it can't be done," or "the spec forbids it."
2. A senior person shuts down a proposal in a single sentence, using a term of art the room does not fully understand.
3. Someone cites a paper, standard, or specialist result that is not obviously connected to the actual proposal on the table.
4. A live counter-example already exists (a working prototype, a test-rig result, a competitor doing it) and an authority is dismissing it anyway.
5. The user is the senior expert in the room and has just rejected, waved off, or shut down a junior colleague's idea.
6. A team or field has operated the same way for years and cannot give a reason beyond "that's how it's done."
7. Someone outside the field proposes an idea and insiders reflexively dismiss it as amateur or crackpot.
8. A paradigm feels locked: everyone agrees on the constraint, nobody can name why.

Don't trigger for:

- A request to put a probability or confidence level on an uncertain future event. That is calibration work; route to tetlock-superforecasting. This skill produces an assumption ledger, not a percentage.
- A general question about anchoring, framing, loss aversion, or decision heuristics with no authority-backed impossibility claim in play. Route to behavioral-economics.
- A plain fact-check against existing data with no authority tell involved (no expert, no jargon, no shutdown, just a number to verify).
- A stated resource or time constraint offered as a preference, not as an impossibility claim (for example, "we don't have budget this quarter" carries no expert authority tell to audit).

## The framework

Core thesis: experts have a poor record specifically on impossibility claims, because such claims rest on assumptions that confident people rarely re-inspect. Jargon and citation of results irrelevant to the actual proposal are displays of authority, not evidence. The identical blind spot (certainty plus unexamined assumptions) will afflict you once you are the seasoned expert, unless you deliberately interrogate your own beliefs. As Hamming put it: "An expert is one who knows everything about nothing; a generalist knows nothing about everything," and in an argument the expert usually wins "by simply (1) using unintelligible jargon, and (2) citing their specialist results which are often completely irrelevant to the discussion."

Quick map of the six sub-concepts:

| Sub-concept | One-line cue |
|---|---|
| Positive/negative asymmetry | "can" earns trust, "cannot" earns a check |
| Assumption audit | every impossibility proof hides conditions |
| Authority tell vs substance tell | jargon and citation are not arguments |
| Outsider origin | the fix usually crosses a field boundary |
| Self-audit | run the check on your own certainty too |
| Success trap | your winning formula ages out |

### Positive/negative asymmetry

Trust "can be done." Distrust "impossible" until checked. Hamming's rule of thumb: "If an expert says something can be done he is probably correct, but if he says it is impossible then consider getting another opinion." The asymmetry exists because a "can be done" claim only needs one path to work, while an "impossible" claim needs every path to be blocked, which is a much stronger and more fragile claim.

Apply when: an authority states a hard "no" or "never," not a "not yet" or "not with our current approach."

### The assumption audit

"All impossibility proofs must rest on a number of assumptions which may or may not apply in the particular situation." The aviation expert who called heavier-than-air flight impossible, the claim that going too fast in a train would make you lose your breath and die, the assertion that supersonic flight was impossible, the "you cannot lift water more than 33 feet" that a patent-office rejection rested on until a standing-wave column proved otherwise: every one of these was an unstated assumption dressed up as a law of nature. The expert "seldom remembers to carefully inspect the assumptions before making their impossible statements." Your job is to do the inspection they skipped.

Apply when: you need the mechanism behind the claim, not just the claim, before deciding anything.

### Authority tell vs substance tell

An authority tell is jargon, a credential, a title, or a citation that does not connect to the specifics of the proposal on the table. A substance tell is an argument that names an assumption, a mechanism, or a specific failure mode in the proposal. Weight only substance tells. A fluent, confident, jargon-dense "no" carries no more evidentiary weight than a fluent, confident "yes"; both still owe you the assumptions underneath.

Examples of authority tells: "per the spec," "in my twenty years of experience," "that is not how it is done," a citation with no stated link to this situation.
Examples of substance tells: "this fails because it violates invariant X," "we tested this at scale and hit limit Y," "here is the assumption this depends on, and here is why it breaks in your case."

Apply when: you are sorting the pushback you received into what to weigh and what to discount.

### Outsider origin of paradigm shifts

Major innovations disproportionately arrive from outside the field under attack. Carbon dating came from physics, not from any archaeologist. The first automatic telephone exchange came from an undertaker, not a telephone engineer. Einstein wrote his five 1905 papers while working in the Swiss patent office, not inside a university physics department. Continental drift was proposed in 1838 and again by Wegener in the early 1900s, ridiculed by geologists for decades, and accepted only after WWII when oceanographers (an outside specialty relative to geology) found the actual mechanism on the ocean floor. When a field is stuck, deliberately solicit a view from someone outside it before treating the field's own consensus as final.

Apply when: everyone you have asked so far shares the same training, the same incentives, or the same paradigm.

### Self-audit when you are the expert

Once you are the one with seniority, ask regularly: "What would I accept as evidence I am wrong?" and "Why do I believe what I do?" Ask this hardest exactly where you are most sure: your own paradigm, your own area of expertise. Hamming's own confession: he forgot a technological change had invalidated his earlier reasoning, more than once, and told the story "to my embarrassment... in order to get the point vividly across."

Apply when: you catch yourself certain, fast, and unwilling to name a counter-example.

### The success trap

"What you did to become successful is likely to be counterproductive when applied at a later date." The specific skills, instincts, and heuristics that made you an authority are tuned to a paradigm that is now shifting under you; they are exactly what will make you resist the next one. Periodically test whether your winning formula still fits the current terrain, and where your own investment in the old approach is most entrenched, consider recusing yourself from the gatekeeping decision entirely rather than trusting your own judgment there.

Apply when: the proposal you just rejected threatens the approach that built your reputation.

## How to apply

1. Write down the impossibility claim verbatim, in the words the authority actually used.
   - Do not paraphrase it into something weaker ("might be hard") or stronger ("never, under any circumstance"). The exact wording usually contains the assumption.
2. List every assumption the claim depends on.
   - Push past the first one. Most impossibility claims hide two or three assumptions, and the second one is usually the load-bearing one (the first is often just restated jargon).
   - Ask: under what conditions would this statement be true, and are those the conditions here?
3. Mark each assumption: still holds, uncertain, or invalidated by changed context (new tool, new dataset, new competitor, new technology, new scale).
   - Changed context is the single most common way an old impossibility proof quietly stops applying. Look there first.
4. Sort the authority's supporting statements into two piles: jargon, credential, and irrelevant citation on one side; arguments that actually engage the assumptions from step 2 on the other.
   - Weight only the second pile. A citation counts as substance only if it addresses this situation's assumptions, not merely if it exists.
5. If a live counter-example already exists (a prototype, a test-rig result, a working system elsewhere), treat it as stronger evidence than the credential of whoever is dismissing it.
   - A demonstrated exception beats an unverified proof every time; this is Hamming's water-column patent story in miniature.
6. Solicit one outside view, ideally from someone outside the field or discipline making the claim, before treating the impossibility as settled.
   - Paradigm shifts disproportionately arrive from outsiders; an inside second opinion often shares the same blind assumption as the first.
7. If you are the one being consulted (you are the authority here), answer "what would change my mind" before you answer "impossible."
   - If you cannot name anything that would change your mind, you are not reasoning from assumptions, you are reasoning from identity. Flag it.
8. Decide, and record the decision:
   - **Accept** the impossibility: every assumption still holds and no counter-evidence survived step 5.
   - **Second opinion**: one or more assumptions are uncertain, or the outside view disagrees.
   - **Recuse**: you (or the authority) have a personal, financial, or career stake in the old paradigm being right, strong enough to bias the audit itself.

Final sanity check: can you name, in one sentence, the specific assumption this whole impossibility claim rests on? If not, the audit is not finished; you have deferred to authority instead of doing the work.

Decision quick-reference:

| Condition found in the audit | Decision |
|---|---|
| Every assumption checked out, no counter-evidence | Accept |
| One or more assumptions uncertain, or outside view disagrees | Second opinion |
| Personal or career stake strong enough to bias the audit | Recuse |

### Worked example

Claim (verbatim): "You cannot lift water more than 33 feet with this kind of pump." A patent examiner rejected an inventor's claim on this basis.

- Assumptions found: (a) the pump works by suction from the top, which is capped by atmospheric pressure at roughly 33 feet, (b) no other physical mechanism is in play.
- Check on (a): does not hold for the inventor's design; it used a standing-wave column with valves, admitting water at a low-pressure point and expelling it at a high-pressure point higher up.
- Check on (b): simply false as stated; a second mechanism existed and the examiners had not looked for one.
- Authority tell vs substance tell: "the textbooks say it cannot be done" is a jargon/citation tell (an appeal to the textbook, not to this device). No examiner engaged the actual mechanism.
- Outside view: the mechanism came from outside the examiners' own frame of reference; nobody trained on suction pumps had reason to look for a standing-wave alternative.
- Counter-evidence: the inventor demonstrated the pump lifting water to the roof of the patent office building, well past 33 feet.
- Decision: reject the impossibility claim outright; the load-bearing assumption (suction-only lift) was false for this specific design.

The same four moves (state the claim, find the assumption, check it against this situation, weigh demonstrated evidence over cited authority) apply whether the claim concerns a pump, a database's scaling limit, a vendor's spec sheet, or a junior engineer's redesign.

## Common failure modes

- Collapsing "impossible" into a probability estimate ("I'd call it 20% likely") and calling that the audit. That is calibration work; it belongs to tetlock-superforecasting. This framework surfaces assumptions, it does not produce odds.
- Treating the audit as license to entertain every unfounded claim that shows up. Most outsider ideas really are noise, most vendors really are right, most specs really do hold. The audit targets a specific authority blocking a specific proposal, it is not a general policy of doubting everyone.
- Running the audit only outward and never on your own certainty once you are the one with seniority. This is the failure Hamming spends the back half of the chapter on: Bell Labs bosses who considered the computer "beneath the consideration of a real mathematician," Einstein opposing quantum mechanics after his own photoelectric paper helped start it.
- Mistaking fluency or confidence for evidence. A polished, jargon-fluent "no" is not more true than a polished "yes"; both owe you the same assumption list.
- Skipping the outside view because the field's own insiders "obviously know best." The chapter's own examples (carbon dating, the automatic telephone, continental drift) all crossed a field boundary before the correction landed; the fix rarely comes from inside the resisting field.
- Auditing a claim once, at one point in time, and treating the verdict as permanent. Assumptions that held yesterday get invalidated by a new tool, a new dataset, or a new competitor; rerun the audit when context changes, not just once.

A closing check on all six: applying the self-audit only in private reflection, and never letting it change an actual decision, is the same failure as never running it at all. "Why do I believe what I do" is a wasted question if the answer never overturns a rejection you already made.

Two failure extremes bound this whole skill. One is reflexively dismissing every idea that comes from outside the field, guaranteeing you miss the next paradigm shift. The other is chasing down every unsolicited claim as a potential breakthrough, which is a full-time job with almost no payoff. Hamming declines to resolve which extreme a person should lean toward as a general life strategy; that is a values choice, not a procedure. This skill does not resolve it either. It only governs the narrower case actually in front of you: a specific authority is blocking a specific proposal, right now, and the assumptions behind that block need to be named and checked before you accept it.

## References

- Hamming, Richard W. *The Art of Doing Science and Engineering: Learning to Learn* (1997, Gordon & Breach), Chapter 26, "Experts."
- Related but not carved separately: Kuhn's paradigm concept, as Hamming applies it to smaller, non-Nobel-scale field changes; it is background for the outsider-origin sub-concept above, not an independently actionable step.
- Siblings: hamming-unreliable-data, hamming-tolerate-ambiguity, hamming-reading-new-tech (other frameworks carved from this book).
- Route probability and confidence-level questions to tetlock-superforecasting. Route general cognitive-bias questions (anchoring, framing, prospect theory) to behavioral-economics. Do not duplicate either sibling's territory here.

Bottom line: check the assumption before you accept the impossibility, and run the identical check on your own most confident beliefs once you are the one being asked.
