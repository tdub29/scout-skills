---
name: hamming-transfer-test
description: "Teaching check. Retest the idea in a new guise"
---

# Hamming: Learning that Transfers (desirable difficulty)

## When to use

The moment: someone has certified that a concept was "taught," typically
because a student, trainee, or model scored well on a test, quiz, drill, or
eval, and the question of whether that score means anything beyond the room
it was earned in has not been asked. Or: someone is about to remove a
tedious, slow, mechanical, or unpopular step from a course, onboarding
flow, drill, or curriculum, on the grounds that an easier version tests
just as well or better.

Cues that this skill applies:

- "They aced the course but froze on the real problem." A concept that
  worked in the classroom, the tutorial, or the training set did not carry
  over to a slightly different notation, variable, or setting.
- "Should we cut this tedious drill? Nobody likes it and it slows the
  course down." A manual derivation, an unaided proof, a from-scratch
  build, a memorization stage, or a "figure it out yourself" step is on the
  chopping block.
- "Our new visual tutorial (or worked example, or auto-complete aid, or
  library wrapper) tested better. Ship it?" A score improved under an
  easier method and that improvement is being treated as the final word.
- Building or reviewing an educational tool, onboarding sequence, training
  program, or assessment, and needing to decide what the assessment should
  actually test.
- Checking whether an LLM eval, benchmark, or fine-tune actually measures
  generalization, or only measures recall of the exact phrasing, format, or
  worked examples it was trained or prompted on.
- A learner (person or model) performs perfectly on in-distribution
  examples and then fails immediately when the surface form changes, even
  though the underlying structure is identical.
- Someone asks "is this hard step actually necessary, or is it just
  friction?" without yet naming what, if anything, the hard step is
  currently building.

Don't trigger for:

- Multi-year skill-building, career-capital accumulation, or deliberate-
  practice regimens for a craft. That is `newport-so-good`'s lane: how to
  get good enough at something over years to be rare and valuable. This
  skill answers a narrower and more immediate question: did this one
  concept, taught in this one way, actually transfer, and is this one
  difficult step worth keeping. Use `newport-so-good` for the practice
  program; use this skill to audit whether any single stage inside that
  program is real difficulty or dead weight.
- Whether a new teaching method or tool is genuinely more effective at all,
  when the evidence is an uncontrolled before/after comparison in a
  classroom or training program. Hamming's own Hawthorne-effect point in
  this same chapter, that novelty and visible care raise scores regardless
  of a new method's actual content, means an uncontrolled "it tested
  better" claim is not usable evidence either way. Route that efficacy
  question to `kohavi-controlled-experiments` first. Once you have a
  method that has actually cleared a controlled test, come back here to
  check whether it preserved transfer or just preserved the score.
- Rote, conditioned-response training where the goal is a fast, reliable,
  automatic reaction rather than a transferable abstraction: arithmetic
  tables, flight-simulator drills, fencing reflexes, muscle-memory
  procedures. Hamming is explicit computers and easier, more repetitive
  methods can do a better job than a human teacher here. This skill is for
  the opposite case, high-level thinking and abstraction, where surface
  ease can quietly delete the thing being taught.

## The framework

**Core thesis.** Mastery is portable across representations, or it is not
mastery yet, only a memorized association with one room, one notation, one
professor, one worked example. Learners, human or model, default to
pattern-matching the surface form they were trained on rather than the
underlying structure, and that default is invisible until the surface form
changes. Making learning easier, spoon-fed graphics, gentler notation, a
skipped "hard" stage, a library call instead of a derivation, can raise the
measured score while quietly deleting the exact struggle that was building
the abstraction the score was supposed to certify. Hamming states the
asymmetry directly:

> "What you learn from others you can use to follow; What you learn for
> yourself you can use to lead."

Difficulty is not automatically good. The task is to tell which difficulty
is which, before cutting it or keeping it.

### The transfer test itself: same content, new room, zero transfer

Hamming was teaching calculus across the hall from a dean of engineering's
thermodynamics class. The dean wrote an expression on the board; not one
student recognized it. The very next hour, in Hamming's own class, he wrote
the mathematically identical expression in the notation his students knew,
and they answered immediately. When he asked why they had not answered it
an hour earlier, the honest answer was that they had never connected the
two forms. In his words:

> "What they knew in one class at one hour with one professor did not
> transfer to another hour in a room across the hall with another
> professor."

This is the whole test, stated as a procedure: do not certify a concept as
learned because it was produced correctly in the room, notation, and
phrasing it was taught in. Certify it only after it survives a change of
room, notation, variable, instructor, or framing, with the underlying
structure held fixed. A pass on the original guise and a fail on any
transfer guise means the concept was not learned; it means one specific
sentence or diagram was memorized.

### Cutting the weights in half: needless obstacle or muscle-building one

Hamming once told a dean, half in jest, that he had found a way to fix
students dropping out of a weightlifting class meant to end in a 250-pound
lift: split the lift into two 125-pound lifts. The joke lands because it is
obviously cheating the requirement, not meeting it. Hamming then turned the
question on his own practice: when he found a simpler proof of a theorem
and used it in class instead of the harder original, was he or was he not
doing the same thing, cutting the weights in half? He left the question
open and offered it as a standing test:

> "Is there not an element of truth in the observation the easier we make
> the learning for the student the more we are cutting the weights in
> half?"

The test has two outcomes, not one, and the whole point is that they look
identical from the outside (a score went up, effort went down). A cut is a
needless obstacle removed if the difficulty was never building the target
capability, only gatekeeping it (an ugly, dispensable notation; a
distraction unrelated to the concept). A cut is a muscle removed if the
difficulty itself was the mechanism by which the capability formed (the
struggle of finding a proof, not just reading one, is what builds proof-
finding ability). The physical-muscle analogy is not exact; whether a given
"mental muscle" behaves like a physical one under an easier substitute is
exactly the judgment call this skill exists to force, not skip.

### A hard mechanical stage can force abstraction with no substitute

At the Naval Postgraduate School, Hamming's calculus students could
memorize their way through most of the course. Analytic integration broke
that strategy: given an arbitrary function, they had to recognize which
family of known forms it belonged to, no matter how it was written,
learning to spot the same underlying pattern "in an almost infinite number
of disguises." That is, in his words, "a basic feature of Mathematics and
general intelligence." Removing analytic integration from a course, or
handing the recognition step to a computer routine, removes the one stage
where students are forced to practice recognizing structure independent of
notation. If nothing of equivalent difficulty replaces it, the students who
skip it never build that recognition skill at all; they simply never hit
the wall that would have forced it.

A parallel failure, on a longer fuse, comes from Hamming's own elementary
schooling. An experimental program decided teaching by syllables made the
alphabet unnecessary and dropped it. Students read fine for years. The gap
did not show up until late high school, when not knowing the alphabet
thoroughly enough meant they could not efficiently use a dictionary or a
phone book, by which point it was nearly impossible to make older students
overlearn something that basic. The lesson is about timing as much as
content: a skipped hard stage can look costless for years and then become
expensive exactly when it is hardest to fix. Before cutting a foundational
stage, trace forward to where its absence would first be needed, not just
to the next quiz.

### An aid that pre-digests a concept caps its own extension

Hamming's friend Kaiser had mastered filter theory thoroughly, but entirely
in terms of time and voltage. When a problem required treating energy as
the independent variable instead, Kaiser could not adapt, even with
explicit direction toward the answer. His education had been complete
within one representation and had not built the capacity to leave it. From
this, Hamming drew a general warning about polished teaching aids:

> "The better we inculcate the basic idea with the pictures drawn by the
> professor, the more we prevent the student from later extending the
> ideas to completely new areas not thought of by the professor."

A well-made graphic, worked example, template, or wrapper function can
teach the specific case flawlessly while quietly doing the generalizing
work the learner was supposed to do. The learner walks away able to
reproduce the taught case and unable to extend it, and nothing in the
original test would have shown the difference, because the original test
never asked the learner to leave the taught case.

## How to apply

1. Name the concept in question and state it exactly as it was taught,
   drilled, or scored: the notation, the variable names, the worked
   examples, the exact phrasing of the test items.

2. Classify the target before doing anything else: is this a conditioned
   response (a rote fact, a reflex, a fixed procedure meant to run the same
   way every time) or a transferable abstraction (a structure meant to be
   recognized and reused across different surface forms)? If it is
   conditioned response, stop; easier and more repetitive methods are
   appropriate there and this skill does not apply.

3. For a transferable abstraction, design a transfer probe: the same
   underlying structure, deliberately changed on at least one axis, new
   notation, new variable name or unit, new domain or story problem, new
   instructor, or new room. Change the surface, hold the structure fixed.

4. Administer the probe cold, without a bridging hint that tells the
   learner "this is the same thing as before." A hint that connects the two
   forms is itself the transfer step; giving it away defeats the test.

5. Score literally, not charitably: transfer, or no transfer. A correct
   answer in the original guise plus a wrong or blank answer under the
   transfer guise means the concept was not learned yet, regardless of what
   the original score said.

6. If a specific "hard" or tedious step is being proposed for removal (a
   manual derivation, an unaided drill, a from-scratch build, a
   memorization stage, an unassisted first attempt), write one sentence
   naming the exact abstraction or recognition skill that step is currently
   responsible for building. If no one can write that sentence, the step is
   very likely a needless obstacle; proceed to cut it.

7. If the sentence in step 6 can be written, check the proposed
   replacement (a graphic, an aid, a shortcut, a computer routine, a
   library call) against it directly: does the replacement require the
   learner to do that same abstraction-building work themselves, or does it
   perform the work on the learner's behalf and hand them only the output?

8. If the replacement performs the work rather than requiring it, keep the
   hard step. Expect the visible cost, lower near-term scores, slower
   completion, more dropout, and do not treat a rise in scores under the
   easier version as evidence the abstraction survived; that rise is
   exactly the failure mode this skill exists to catch.

9. Final sanity check: re-run the transfer probe some real time later, on a
   different guise than the one used in step 3, ideally comparing a group
   that got the hard step against a group that got the easier version. If a
   controlled comparison is not possible, at minimum locate the future
   point (a later course, a later task, a later production use) where the
   skipped step's absence would first surface, the way the alphabet gap
   surfaced years later, and check now whether that future need is already
   being planned for.

## Common failure modes

- **"Hard equals good."** Treating difficulty itself as the goal, keeping a
  step because it is unpleasant rather than because it is load-bearing.
  Busywork and desirable difficulty produce the same complaints from
  learners and are not the same thing; only the sentence from step 6 tells
  them apart.

- **Reading a higher score under an easier method as proof of mastery.**
  Claims like "students advanced 10% faster" or "the new tutorial tested
  better," offered with no transfer probe and no control for novelty, prove
  only that the score went up, not that the underlying capability did.

- **Skipping the controlled-comparison step first.** Uncontrolled classroom
  or training comparisons are vulnerable to the Hawthorne effect (visible
  novelty and care raise scores independent of method), so an "it tested
  better" claim needs `kohavi-controlled-experiments` applied before this
  skill's transfer probe means anything at all.

- **Cutting a tedious step without naming what it built.** Removing a
  manual derivation, a memorization stage, or an unaided first attempt
  because it is unpopular, without ever writing the one-sentence
  abstraction it was responsible for, then discovering the gap only when it
  resurfaces downstream, often too late to cheaply fix.

- **Testing only recall in the original guise.** Grading a concept as
  learned because the exact worked example, notation, or phrasing came back
  correctly, without ever changing the surface form to check what is
  actually underneath.

- **Applying this to conditioned-response training.** Demanding transfer
  proof for arithmetic-table drills, simulator reps, or reflex training,
  where Hamming himself says an easier, more repetitive, computer-assisted
  method is the right call, since a fast fixed reaction, not a portable
  abstraction, is the actual target there.

## References

Hamming, Richard W. *The Art of Doing Science and Engineering: Learning to
Learn.* Gordon and Breach, 1997. Chapter 22, "Computer Aided Instruction"
(the ln(x)/log(x) transfer story, "cutting the weights in half," analytic
integration and the alphabet-skipping experiment, and the Kaiser filter
story all appear here).

Siblings in this carve: `hamming-prepared-mind` (the incubation cycle that
produces an insight in the first place, once the underlying abstraction has
actually been built rather than pre-digested for the learner),
`hamming-important-problems` (choosing what is worth this kind of
sustained, difficulty-preserving effort before spending it).
