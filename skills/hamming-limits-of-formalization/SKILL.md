---
name: hamming-limits-of-formalization
description: Apply Hamming's limits-of-discrete-symbol-systems argument, from "The Art of Doing Science and Engineering: Learning to Learn" (1997), before anyone tries to make a policy, rubric, contract, or classifier fully unambiguous. Godel's theorem shows any sufficiently rich discrete symbol system has truths it cannot prove within itself, and adding axioms only pushes the gap higher, never closes it. Natural language stays fuzzy (multiple meanings, tone, context) on purpose to escape that ceiling. Some content (music, beauty, justice) apparently cannot be put into words or symbols at all. Trigger on a request to write zero-ambiguity rules for an AI content-moderation policy, a grading rubric or scoring scheme meant to remove all teacher or grader judgment, a contract, style guide, or classifier that tries to define every case in advance, a compliance policy chasing false completeness, or any attempt to fully encode "fairness," "quality," "justice," or "good writing" in rules. Fence hard against model-thinking, which is about choosing or combining models of a system already agreed to be formalizable; this skill answers the prior question of whether, and how much, to formalize a domain at all, and applies specifically where the content is judgment, value, or context-bound. Relevant to AI policy design, EdTech rubrics, legal contracts, and compliance work. Output is a formalize-vs-discretion decision: which parts of the domain are genuinely mechanizable (make them rigorous) and which are Godel-limited or judgment-bound (give them a documented, bounded discretion clause).
---

# Hamming: The Limits of Discrete Symbol Systems

Provenance: Hamming, *The Art of Doing Science and Engineering: Learning to Learn* (Gordon and Breach, 1997), Chapter 23, "Mathematics." This is the chapter's closing argument, the "disturbing thought" Hamming leaves the reader with after walking through the five schools of what mathematics is.

## When to use

Trigger the moment someone is about to write a rule system meant to cover every case in advance, before the first draft locks in, not after a gap in the finished policy has already caused a bad outcome. This is a pre-formalization check: does the domain in front of you actually admit the completeness you are about to promise it.

Concrete cues:

- Someone wants zero ambiguity in an AI content-moderation policy, and is asking whether every borderline post can be resolved by the rule text alone.
  - Example situation: a trust-and-safety team asks for a rule list that removes the need for any human reviewer to ever make a judgment call on satire, reclaimed slurs, or newsworthy exceptions.
- A grading rubric or scoring scheme is being built to remove the need for teacher or grader judgment entirely, "so any grader gets the same score."
  - Example situation: a district asks for an essay rubric where "originality" and "voice" are broken into point values precise enough that two graders can never disagree.
- A style guide is being asked to fully define "good writing," "clarity," or "brand voice" with no room left for editorial discretion.
- A contract, terms-of-service, or compliance policy is being drafted to anticipate and rule on every future case, with the stated goal of never needing a human judgment call again.
  - Example situation: a vendor contract's "reasonable efforts" clause is being rewritten as a numbered list intended to make "reasonable" fully self-executing, with no room for a case-by-case read.
- A classifier or scoring model is being specified with the assumption that enough categories and enough training examples will eventually make every edge case fall cleanly on one side of a line.
- Someone frames a disagreement as "we just need a clearer definition" for a term that is actually a values term (fairness, quality, harm, justice, beauty), not a factual one.
- A law, regulation, or internal policy is being praised or criticized for "finally closing the loophole," when the pattern in front of you is the same gap reappearing one level up.
- The user directly asks whether a domain can be "fully specified," "made deterministic," or "automated away from human judgment."
- A prior policy or rubric has already been patched several times to cover cases it missed, and the request is now to "get it right this time" so no further patching is ever needed.
- An AI evaluation or scoring harness is being asked to judge something inherently subjective (writing quality, helpfulness, tone) with a rubric that assumes a single, fully specified ground truth exists for every case.
  - Example situation: an LLM-as-judge prompt is being written to score "helpfulness" on a 1 to 10 scale with the stated goal that any two runs of the judge should always agree exactly.

Don't trigger for:

- Choosing, combining, or validating models of a system already agreed to be formalizable (financial models, physical simulations, statistical models). That is `model-thinking`, which operates inside a domain everyone accepts can be captured by some formal structure; the open question there is which structure fits, not whether formalization is possible at all.
- Calibrating confidence in an already-reached conclusion, or assigning a probability to an uncertain but well-defined claim. That is `tetlock-superforecasting`.
- Auditing whether a reported number can be trusted. That is `hamming-unreliable-data`.
- Designing a target variable or label for a model you are actively building (choosing what to predict, checking for leakage). That is `provost-data-science-for-business`; this skill fires on whether the underlying concept can be captured by rules at all, not on the mechanics of turning an already-accepted concept into a training label.
- A domain where more precision is simply undelivered, not impossible, and the fix is writing a better definition (see Common failure modes, "premature surrender"). Only trigger this skill once you suspect the gap is structural, not merely under-specified.

The dividing line: if the argument in the room is about which formal model best fits an already-agreed-formalizable system, route to model-thinking. If the argument is whether a domain can be fully captured by rules or symbols at all, and the content in question is judgment, value, or context dependent, this skill applies.

A useful one-question test: ask "if two competent, well-intentioned people applied this rule to the same case, could they reach different answers for a reason other than a mistake." If yes, on inspection, that item belongs in this skill's judgment-bound category, not in a model-thinking discussion about which formalism fits best.

## The framework

**Core thesis.** Godel's theorem, loosely stated, says that a sufficiently rich system of discrete symbols will contain statements whose truth or falsity cannot be proved within that system. Add new axioms to settle those statements, and the enlarged system generates new unsettleable statements of its own. Formalization is never complete; closing one gap opens another one level up. Natural language looks, at first glance, like just another discrete symbol system, but it is not: words carry multiple and graded meanings, and tone, gesture, and context shift what is being said. Hamming's suggestion is that this fuzziness is not a defect language happens to have, it may be exactly how language escapes the trap Godel describes for cleaner formal systems. And some content, Hamming says explicitly, apparently cannot be put into words or symbols at all: what a piece of music communicates, and (to a lesser extent) what a painting communicates, plus truth, beauty, and justice, the three things "of Classic Greece" that everyone thinks they understand and nobody can fully define. The oldest attempt to force one of these into words, justice into law, is Hamming's standing example that the encoding is never the thing itself.

### 1. Formalization is never complete

Godel's result is specifically about "a reasonably rich system of discrete symbols," not mathematics alone. Adding axioms to resolve one unprovable statement produces "new theorems which you cannot settle within the new enlarged system." Treat any claim that a rule system has "finally closed the loophole" as a claim to be checked, not accepted: the pattern to expect is not zero remaining gaps, it is the gap reappearing one level higher, in a form nobody wrote a rule for yet. A policy that has been patched ten times and still needs an eleventh patch is not failing, it is behaving exactly as Godel's argument predicts a discrete rule system will behave.

Why it matters: a team that expects the eleventh patch to be the last one will keep being surprised by the twelfth, and will keep treating each new gap as an isolated bug instead of budgeting time and process for the next one, which is exactly what step 6 of How to apply exists to fix.

### 2. Ambiguity and context-sensitivity are a feature, not a defect

Godel's theorem assumes "a set of definite symbols with unchanging meaning." Natural language violates that assumption constantly: the word "tall" means something different in "a tall building," "a tall person," and "a tall tale," and a tone of voice, a raised eyebrow, or a smile can change what a sentence means without changing a single word in it. Hamming's speculation is that this is not sloppiness that evolution failed to fix, it may be exactly the escape valve that lets natural language say things a fully formal system cannot say at all. When someone proposes replacing a fuzzy, context-sensitive term in a policy with a precise one, ask what the fuzziness was doing for the system before treating its removal as pure gain.

Why it matters: a policy author who reads every remaining fuzzy term as an unfinished job, rather than as a load-bearing design choice, will keep trying to legislate it away and keep being surprised that the replacement rule creates new, worse edge cases of its own.

### 3. Some domains resist symbolic capture altogether

Hamming's direct claim: "it is not evident... that all things, whatsoever they may be, can be put into words." What a piece of music transmits to an audience "cannot be put into words," or the composer would have used words instead of music. Painting resists capture "to a lesser extent." And truth, beauty, and justice, though everyone believes they know what the words mean, apparently cannot be put into words either. The law is the standing example: from Hammurabi forward, "the attempt to put justice into words has produced the law, and often the law is not your conception of justice." The law is a discrete symbol system's best attempt at justice, not justice itself, and the persistent gap between the two is not a bug in any particular legal code, it is what you should expect whenever a value term gets forced into rule form.

Why it matters: mistaking the rule (the law, the rubric, the moderation policy) for the value it is trying to encode (justice, quality, safety) leads to defending the rule's letter in cases where the rule has visibly drifted from the value it exists to serve.

### 4. Discrete computers inherit the same ceiling

Standard computers handle discrete symbols, so "apparently, there may be many things they cannot handle." An AI classifier, a content-moderation model, or an automated grading system is a discrete symbol system running on a machine built to process discrete symbols; it inherits Godel's ceiling along with every other feature of that architecture. Treat "the model will eventually learn the edge cases" as an empirical bet on how far formalization can be pushed, not as a guarantee that the gap closes to zero.

Why it matters: procurement and product decisions that assume a big enough model or a large enough training set eventually eliminates all judgment calls are making an unstated bet against a structural ceiling, not just an engineering estimate, and should carry a fallback plan for the cases the model will keep getting wrong.

### A quick check for whether the mechanizable/judgment-bound sort is honest

Before treating the sort as done, confirm the following are all true, not just asserted:

- Every item marked judgment-bound survived the premature-surrender test in step 3 below; nothing was labeled judgment-bound purely because writing the precise rule would have taken more time.
- Every item marked mechanizable can actually be stated as a rule someone could apply without knowing anything about the specific case beyond the stated facts. If applying the "rule" still requires the applier to weigh context, it is not actually mechanizable yet.
- The discretion clause being planned for the judgment-bound items names a specific decision-maker and a specific record they must leave, not just "human review" as an unstructured placeholder.
- Nobody has quietly moved a value-laden term (fairness, quality, harm, justice) into the mechanizable column just because a numeric score got attached to it. A number is not the same thing as a mechanized definition; it can just be a judgment call wearing a decimal point.

## How to apply

1. **Name the domain and state the completeness claim being made.** Write down, in one sentence, what the policy, rubric, contract, or classifier is claiming to do: cover every case, remove the need for judgment, eliminate ambiguity. If nobody can state the claim plainly, the gap between intention and draft is already hiding somewhere.
   Example claim: "no content reviewer should ever need to exercise discretion" is a testable completeness claim; "make moderation better" is not, and needs to be sharpened before this process can run.

2. **Sort the domain's content into mechanizable and judgment-bound.** Go through the actual cases the system needs to handle and mark each one: does resolving it require only facts and a fixed rule (mechanizable), or does it require weighing values, reading context, or making a call reasonable people could disagree on (judgment-bound). Example split for a content-moderation policy: "does this post contain a slur from list X" is mechanizable; "is this post satire or genuine harassment" is judgment-bound.

3. **Test each judgment-bound item against the premature-surrender check.** For every item marked judgment-bound, ask: would a sharper definition actually close this gap, or does the ambiguity survive any definition you can write. If a better definition would close it, it was under-specified, not Godel-limited; move it back to mechanizable and go write the definition. If disagreement persists no matter how the definition is sharpened, because the disagreement is about values, weighting, or context rather than facts, it stays judgment-bound.

4. **Make the mechanizable parts fully rigorous.** Where the sort in step 2 holds, do not leave slack. Hamming's caution here runs both directions: he is not arguing for vagueness everywhere, only for reserving vagueness for the parts that actually need it. A rule that can be made precise and enforced consistently should be.
   Example: a word-count minimum, a required-citation-count rule, or a banned-terms list should be exact, automatically checkable, and applied the same way every time, with no discretion clause attached to it at all.

5. **Design a bounded discretion clause for the judgment-bound parts.** Do not leave judgment-bound cases as silent gaps or as items quietly folded into the "mechanizable" bucket to make the policy look complete. Write an explicit clause: who exercises the judgment, what factors they must weigh, what record they must leave, and what review or appeal exists. "Bounded" is the operative word: the clause states the scope of discretion and the accountability trail, it does not hand over unlimited, unreviewable authority under the banner of "human judgment."
   Example clause skeleton: "A tier-two reviewer decides satire/harassment-in-context cases, must record the three factors weighed and the specific evidence for each, and the poster may appeal to a second reviewer within seven days."

6. **Expect and schedule the next gap.** Because closing one gap with a new rule tends to open another one level up, build a revisit cadence into the policy itself (a review date, a triggering volume of appealed cases, a scheduled audit) rather than treating the current draft as the final one. Treat the first hard case that slips through both the mechanizable rules and the discretion clause as expected behavior of a discrete rule system, not as a one-off failure to patch and forget.
   Example cadence: a quarterly audit of every case routed to the discretion clause, specifically looking for a cluster of similar cases that suggests a new mechanizable rule could now be carved out of what used to be pure judgment.

7. **Write the artifact.** Produce the actual policy, rubric, contract, or classifier spec with two visible parts: the rigorous rules, and a clearly labeled, bounded discretion section covering the judgment-bound cases identified in step 2, including who decides and what they must document.
   Keep the two parts visibly distinct in the document itself, a separate heading or a separate column, rather than interleaving them so a reader cannot tell rule from judgment call at a glance.

8. **Sanity-check before finalizing.** Reread the draft and ask: did every judgment-bound item from step 2 survive into the discretion clause, or did any get quietly converted into a rigid rule just to make the document look complete. Did any mechanizable item from step 4 get left loose out of misplaced deference to "judgment." If either has happened, the formalize-vs-discretion line has drifted and steps 2 through 5 need to be rerun on the affected items.
   Final gate: state out loud, in one sentence, which specific value or judgment call the discretion clause exists to protect. If no one can name it, the clause is decoration, not a real bounded-discretion mechanism, and step 5 needs to be redone.

**Worked example 1: AI content-moderation policy.** A team wants zero-ambiguity rules for banning content. Step 1: the completeness claim is "no reviewer should ever need to make a judgment call." Step 2: sort cases; "contains a slur from list X," "contains a phone number in a spam pattern," and "posted more than N times in an hour" are mechanizable; "is this satire," "is this newsworthy documentation of violence rather than glorification of it," and "does this cross the line into harassment given the relationship between the parties" are judgment-bound. Step 3: sharper definitions can shrink the satire case somewhat (a stated-intent field, a account-history check) but cannot make it fully mechanical, since satire is defined partly by audience uptake, not just speaker intent; it stays judgment-bound. Step 4: the slur list, spam pattern, and rate limit get made precise and automatically enforced. Step 5: the discretion clause names a human review tier for satire/newsworthiness/harassment-in-context calls, requires the reviewer to log the specific factors weighed, and routes contested calls to a second reviewer on appeal. Step 6: the policy commits to a quarterly review of the appeal log to catch the next gap. Output: an enforcement engine for the mechanizable list, plus a documented, bounded human-review tier for the rest, instead of a single rule table pretending to cover both.

**Worked example 2: essay grading rubric.** A school wants a rubric precise enough that any two graders reach the identical score, eliminating "grader variance." Step 1: the completeness claim is "remove all teacher judgment from scoring." Step 2: sort criteria; "contains a thesis statement in the first paragraph," "uses at least three cited sources," and "meets the word count" are mechanizable; "the argument is original," "the prose has voice," and "the essay demonstrates genuine insight rather than competent restatement" are judgment-bound. Step 3: originality and voice do not close under a sharper definition, since two graders reading the same well-defined criterion can still reasonably disagree on whether a particular essay meets it; they stay judgment-bound, while "insight vs. restatement" partially closes if the rubric adds a required comparison-to-source-material step, so that piece moves toward mechanizable. Step 5: the discretion clause specifies a scored band (not a single point value) for originality and voice, requires a one-sentence written justification from the grader, and routes any essay within one band-width of a grade boundary to a second reader. Output: a rubric with hard-mechanized criteria for structural requirements and a bounded, documented judgment band for the parts grading has never actually been able to fully mechanize, honest about which is which instead of forcing both into identical-looking point values.

**Worked example 3: "reasonable efforts" contract clause.** A vendor contract's "reasonable efforts" clause is being rewritten to remove the phrase entirely and replace it with a numbered checklist meant to be self-executing. Step 1: the completeness claim is "no future dispute over what counts as reasonable effort should ever require interpretation." Step 2: "delivered by the stated date," "used the named subcontractor," and "spent at least the budgeted hours" are mechanizable; "responded appropriately to an unforeseen supply disruption" and "prioritized this client's work fairly relative to other clients" are judgment-bound, since "appropriately" and "fairly" are exactly the kind of value terms Hamming's justice-into-law example warns will not fully close under any checklist. Step 3: some of the checklist items thought to require judgment (did they notify the client within 48 hours of a known disruption) actually close under a sharper, purely factual definition and move to mechanizable. Step 5: the surviving judgment-bound terms get an arbitration clause naming a specific decision process and the factors an arbitrator must weigh, rather than a checklist item pretending "reasonable" has been fully defined away. Output: a contract with hard deadlines and factual triggers stated as checklist items, and a named dispute-resolution mechanism, rather than a false promise that "reasonable" no longer requires anyone to interpret anything.

## Common failure modes

- **Premature surrender.** Calling something "impossible to formalize" and reaching for a discretion clause when a better, sharper definition would actually close the gap. Hilbert closed real gaps in Euclid by adding postulates Euclid had never stated; not every ambiguity is Godel-limited, some are just under-specified.
  - Example: labeling "spam" judgment-bound and routing every case to human review, when a rate-and-pattern rule would mechanize most of it.
  - Fix: run step 3's premature-surrender check before accepting any "judgment-bound" label; write the sharper definition first and see what is actually left over.

- **False completeness.** Writing a policy, rubric, or classifier as if it covers every case, with no discretion clause at all, then patching it forever as edge cases surface one at a time. This is the failure Godel's argument predicts directly: each patch closes one gap and opens another.
  - Example: a content policy with no review tier at all, amended for the tenth time this year after the tenth new edge case went viral.
  - Fix: build the bounded discretion clause and the scheduled-review cadence (steps 5 and 6) into the first version, not as damage control after the fact.

- **Skipping achievable precision.** Using "some things resist formalization" as an excuse to leave vague what could and should be made rigorous, including cases where regulation or law requires a precise rule. The framework is a sorting tool, not a blanket license for vagueness.
  - Example: leaving a data-retention deadline "up to reasonable judgment" when the applicable regulation actually specifies a fixed number of days.
  - Fix: re-run step 2 on any item currently left loose; if it is genuinely mechanizable, it belongs in step 4, not folded into the discretion clause for convenience.

- **Over-mysticizing to dodge accountability.** Labeling a domain "impossible to fully define, it's just judgment" as a way to avoid ever being held to a standard, rather than as an honest description of where values genuinely diverge.
  - Example: a manager waves off every complaint about inconsistent performance ratings with "quality is subjective," with no rubric, no documented factors, and no appeal path behind the claim.
  - Fix: a bounded discretion clause has a named decision-maker, stated factors, and a review path (step 5); "it's just judgment" with none of those attached is not this skill's output, it is the failure this skill exists to prevent.

- **Unbounded discretion dressed as a clause.** Writing a discretion section that names no decision-maker, no factors, no record, and no appeal, then calling that a "bounded" clause because it has a heading.
  - Example: a rubric's "holistic judgment" section that is one sentence long and grants a single grader unreviewable final say.
  - Fix: bounded means scoped and accountable; add the who, the factors, the required record, and the appeal path, or the section is not actually a discretion clause yet.

- **Treating the law-as-justice gap as an argument against having law.** Hamming's point about justice resisting full encoding into law is not an argument for abandoning legal codes, it is an argument for expecting the gap and building review mechanisms into the system on purpose.
  - Example: concluding that because no rule set can fully capture "fairness," a fairness policy is not worth writing at all.
  - Fix: write the rule set for what it can mechanize, and build the appeal, judicial-discretion, or case-law-style review mechanism for the remainder, exactly as steps 4 through 6 describe.

- **Writing the discretion clause on paper, then building enforcement that bypasses it.** Shipping a policy document with a well-designed bounded discretion clause, while the actual enforcement system (an automated classifier, an auto-moderation pipeline) is wired to act unilaterally without ever routing the judgment-bound cases to the named human reviewer.
  - Example: a moderation policy's documented appeal path never actually fires because the automated system auto-removes content before any reviewer sees it, regardless of confidence score.
  - Fix: verify the enforcement mechanism actually routes judgment-bound cases to the named decision-maker from step 5, not just that the policy document describes a clause that exists in principle.

## References

- Hamming, Richard W. *The Art of Doing Science and Engineering: Learning to Learn* (Gordon and Breach, 1997), Chapter 23, "Mathematics." Key passages: "Language at first glance is just a discrete symbol system... it just might be the reason language has such peculiar features is in life it is necessary to escape the limitations of Godel's theorem." "It is not evident... that all things, whatsoever they may be, can be put into words... what is transmitted to the audience [by music] cannot be put into words." "There will be new theorems which you cannot settle within the new enlarged system."

- This is the chapter's closing move, arriving after Hamming walks through the five schools of mathematical philosophy (Platonic, formalist, logicist, intuitionist, constructivist) and argues none of them fully accounts for how mathematics actually works. The limits-of-discrete-symbol-systems argument generalizes past mathematics specifically to any discrete symbol system, which is why it reaches language, law, and (by direct extension) computers.

- Sibling carved skills from the same book: `hamming-high-dimensional-intuition`, `hamming-you-get-what-you-measure`. Cross-reference by name only; do not duplicate their content here.

- `model-thinking` owns choosing and combining models of a system already agreed to be formalizable. This skill owns the prior question, whether and how much to formalize a domain at all, and applies specifically to the judgment-bound remainder model-thinking does not address.

- `hamming-unreliable-data` owns auditing whether an already-reported number or measurement can be trusted. This skill is about whether a domain admits full rule-based capture at all; the two combine when a bounded discretion clause itself depends on numbers (a confidence score, a rate threshold) that also need their own trust audit.
