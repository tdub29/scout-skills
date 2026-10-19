---
name: hamming-heroic-task-first
description: Apply Richard Hamming's rule, from The Art of Doing Science and Engineering: Learning to Learn (1997), that a new method earns the right to do routine, economical work only after it first proves itself on the hardest available problem using the crudest available resources. Hamming solved atomic-bomb partial differential equations on relay computers before numerical analysis matured for routine use. Use this the moment the user is introducing a new method, tool, or process against skepticism, leadership will not trust it beyond toy problems, the approach already nails the hard case but people still default to the old way, the user is wondering whether to keep pushing against stout resistance (or has been ground down by it), or the user is choosing which demo will earn credibility for something unproven. It routes the user to pick the single hardest instance as the proof (not the easiest, not the most convenient), build the reusable, generalizable method alongside that proof so it actually scales, expect stout resistance as the structural default rather than a verdict on the idea, and still size that resistance honestly against the remaining payoff as a real go/no-go checkpoint, not open-ended persistence. Do not use this for the communication and marketing discipline of getting an already-proven result adopted and presented (that is hamming-sell-your-work); this skill governs the sequencing of the proof itself, upstream of any pitch. Output is a demonstration plan (hardest case first, reusable method built alongside) plus a resistance-sizing go/no-go checkpoint.
---

# Hamming: Prove It on the Heroic Task First

## When to use

Reach for this at the moment a new method, tool, or process is real enough to test, and the open question is what to test it on first, and how to read the pushback that follows. This is not a persuasion or presentation skill. It is about the order of proof itself, before there is anything finished worth presenting.

The sequencing matters because it is reversible in only one direction. A method proven on the hard case can then be simplified, documented, and rolled out to routine use. A method that has only ever been shown on an easy, convenient case cannot retroactively claim it would also survive the hard one; it has to actually be run there first, and until it is, every routine-use pitch is standing on an unproven claim.

Trigger on:

- The user is introducing a new method, tool, or process and meeting real skepticism about whether it works at scale, not just in principle.
  For example: a new modeling approach, automation script, or workflow change is being pitched, and the response is "sounds fine for a demo, but will it hold up on our real data."
- Leadership or stakeholders will not extend trust past a toy problem or a small supervised pilot, no matter how the pitch is worded.
  For example: repeated requests for "just one more pilot" that never converts into a decision to actually adopt the thing.
- The method already nails the hardest case available, yet people still default to the old way because the old way is "proven."
  For example: the new approach outperforms on the messiest dataset in the building, and the team still runs the manual process "to be safe."
- The user is wondering whether to keep pushing against resistance to adoption, or is already worn down and ready to quit.
  For example: months of pushback with no clear signal on whether the resistance is normal friction or a real dead end.
- The user is choosing which demo, pilot, or case study to lead with in order to earn credibility for something unproven.
  For example: deciding between showing off the new method on a convenient, well-behaved example versus the ugliest one in the backlog.
- The user is scoping the first real test of a new capability and is tempted to pick an easy, convenient, "let's start small" case instead of the hardest one available.
  For example: choosing a friendly internal team as the first pilot instead of the team with the gnarliest edge cases.
- Resistance is being read as a verdict on the idea's quality ("if it were any good, people would already be using it") instead of being examined for its actual size.
  For example: treating three skeptical stakeholders as proof of failure rather than as the expected starting condition for any new method.
- A one-off "we made it work" success exists, but no generalizable method or theory has been built alongside it yet.
  For example: a single hero engineer solved the hard case once, and nobody else on the team could repeat what they did.

Don't trigger for:

- Presenting or marketing a result that has already been proven. That is hamming-sell-your-work, which governs formal talks, written reports, and informal pitches for something that already exists and works.
  This skill ends where that one begins: once the heroic-task proof exists, hamming-sell-your-work takes over getting it adopted and known.
- Generic change-management or org-politics coaching with no new method, tool, or technique at the center of the disagreement.
  If nothing new is actually being proven, there is no heroic task to sequence, and the disagreement is a different kind of problem.
- Deciding which problem is worth working on in the first place. That is hamming-important-problems.
  This skill assumes the method already exists and needs proving, not that a problem still needs choosing.
- A one-off situational obstacle where the move is inverting a fixed constraint into direction (hamming-defect-into-asset), rather than proving new capability against doubt.
  A missing resource being turned into a design direction is a different move than proving a method works at all.

## The framework

### Core thesis: heroic tasks earn the right to become routine

Hamming states the rule directly: "It is first necessary to prove beyond any doubt the new thing, device, method, or whatever it is, can cope with heroic tasks before it can get into the system to do the more routine, and in the long run, more useful tasks."

His own case: at Los Alamos, computing solutions to atomic-bomb partial differential equations on primitive equipment. At Bell Telephone Laboratories, solving partial differential equations (and even a partial differential-integral equation) on relay computers, before progressing down to ordinary differential equations (missile trajectories), then simple integration, then function evaluation, then finally the arithmetic of how numbers combine. He states the sequence in his own words: "we did some of the hardest problems on the most primitive equipment. It was necessary to do this in order to prove machines could do things which could not be done otherwise. Then, and only then, could we turn to the economical solutions of problems which could be done only laboriously by hand."

The order does not reverse. Proof on the hardest case is what removes doubt that the new thing works at all. Only once that doubt is removed does routine, economical, everyday use become available to argue for. Leading with the easy case instead invites the obvious rebuttal, that the old method already handles the easy case just fine, so why switch.

Hamming names this pattern explicitly as general, not a story confined to 1940s and 1950s computing: "This is typical of many situations." He offers the computing history as the illustration because it is the one he lived through directly, not because the rule is limited to machines, numerical analysis, or that era; any new method, in any field, faces the same sequencing requirement before it is granted routine use.

### Prove on crude resources, for doubt removal, not for efficiency

The equipment behind Hamming's proofs was primitive even by the standards of his own moment (relay computers, improvised setups). The point of a heroic-task demonstration is never that the crude setup is an efficient way to solve the problem. It usually is not.

The point is to remove doubt that the method can do it at all. Confusing "prove it can be done" with "prove it is currently efficient to do it this way" leads people to reject the proof as impractical, missing that practicality was never the claim under test. A heroic-task proof that runs slow, ugly, and by hand in places has still done its job if it removed the doubt; polishing it into an efficient tool is a separate, later task.

Watch for the specific rebuttal this invites: "sure, but nobody would actually do it this way." That objection is true and irrelevant. Nobody was supposed to run the crude proof in production; the crude proof exists to establish that the capability is real, so the efficient, production-grade version can then be built with confidence instead of built on faith.

### Routine adoption follows the proof; it does not precede it or substitute for it

Only after machines had proven themselves against heroic partial-differential-equation work did the field turn to developing the basic theories of numerical analysis and practical computing suitable for machines, for routine, everyday use. The routine, economical case is the destination, not the opening move.

It is reached by first clearing the heroic-task bar, not by skipping ahead to it and hoping people extend trust on faith. A pitch that opens with "and this will save everyone time on the routine cases" before the hard case has ever been run is asking for adoption the proof has not yet earned.

### Build the reusable method alongside the proof, or it will not scale

Hamming did not treat his heroic PDE work as an isolated stunt. Solving the hardest instance and developing the basic theories of numerical analysis happened together, deliberately, because a single successful demonstration that cannot be repeated, taught, or handed to someone else is a curiosity, not an adoptable method.

A proof with no reusable method inside it dead-ends at "one person did one hard thing once." Build the general method, whether that is a written theory, a checklist, a template, or a piece of reusable code, in parallel with the heroic case, not as a follow-up project scoped later once the excitement from the demo has already faded and the original prover has moved on to something else.

### Expect stout resistance as a structural default, not a signal about the idea

"Any innovation is always against such a barrier, so do not get discouraged when you find your new idea is stoutly, and perhaps foolishly, resisted." Resistance to a new method is the ordinary condition new methods encounter, structurally, independent of whether the new method is any good.

Treating friction and pushback as proof the idea is flawed is a category error. The barrier is there for every innovation, including the ones that later become standard practice; the presence of resistance says nothing by itself about which category a given method falls into.

### But size the resistance honestly; it is a go/no-go gate, not license to persist indefinitely

Hamming does not romanticize persistence for its own sake: "By realizing the magnitude of the actual task you can then decide if it is worth your efforts to continue, or if you should go do something else you can accomplish and not fritter away your efforts needlessly against the forces of inertia and stupidity."

Expecting resistance is not the same thing as absorbing unlimited resistance. Once the heroic-task proof exists (or once it is clear it will not, on any resources available), size the actual remaining barrier honestly against the payoff, and use that sizing as a real checkpoint to continue or walk away, not as a license to grind forever on the theory that all resistance is noise.

This is the piece most easily lost once the previous sub-concept is taken to heart. "Expect resistance, do not be discouraged by it" is a statement about not overreacting to the first signs of friction. It is not a statement that friction should be tolerated indefinitely regardless of how it evolves; the two sub-concepts are meant to be applied together, in sequence, not the first one alone forever.

## How to apply

These steps assume a new method or capability already exists in working form, even a rough one, and the open question is how to sequence its first real test and its rollout. Do not wait until the method feels finished to start step 1; the proof target should be chosen while the method is still rough, not after it has already been polished for an easy case.

1. Name the new method, tool, or process plainly, and state exactly what capability it claims that the old way cannot match, or cannot match as well.
   Write this as one sentence before doing anything else; if it cannot be written in one sentence, the claim itself is not yet clear enough to prove.

2. Find the single hardest, most doubted instance of the problem currently available. Not the easiest. Not the most convenient. Not the one closest to what a skeptical stakeholder already believes possible.
   Resist the pull toward a soft, safe pilot; a soft pilot proves nothing that the old method could not already claim to handle.

3. Run the proof on whatever resources are on hand, even crude or improvised ones. The resources do not need to be efficient or production-ready.
   They only need to be sufficient to remove doubt that the method works on the hard case; polish comes later, after doubt is gone.

4. In parallel with running that proof, start building the reusable, generalizable version, whatever form fits: the underlying theory, the process documentation, the reusable script or template, anything that lets someone besides the original prover repeat the result.
   Do not defer this to "after the demo goes well"; by then the details of what actually worked are already starting to fade.

5. When presenting or rolling out the proof, lead with the hardest case, not the easiest one.
   Leading with an easy case invites "the old way already handles that" and spends the credibility of a result before it has actually landed.

6. Expect resistance to follow regardless of how convincing the proof looks.
   Do not treat the mere appearance of resistance as new information about the method's quality; treat it as the default weather every innovation moves through.

7. Separately, size the actual resistance. Is it a normal adoption barrier that time, repetition, and the reusable method will wear down, or is it a wall backed by a real constraint (budget, regulation, a fatal flaw the heroic-task proof did not actually address)?
   Get specific about which one it is; the two require completely different responses.

8. Set a checkpoint on that sizing. Name what continued effort would need to show, and by when, to be worth continuing.
   If the barrier's magnitude outweighs the payoff on honest inspection, redirect effort instead of continuing to grind against it.

Final sanity check: state, in one sentence each, the heroic case the method was proven on, the reusable method that now exists because of that proof, and the condition that would tell you to stop pushing if resistance does not yield. If any of the three comes back blank, the demonstration plan is not ready yet.

A blank on the first sentence means there is no proof yet, only a plan. A blank on the second means the proof is a one-off stunt that will not scale past the person who ran it. A blank on the third means there is no honest go/no-go gate, only an open-ended commitment to keep pushing regardless of what happens next.

### Worked example

A data team has built a new pipeline validation approach and wants it adopted org-wide, replacing manual spot-checks.

- Step 1 to 2: instead of piloting it on a small, well-behaved dataset the team already trusts, they pick the org's worst dataset, the one with the most historical corruption incidents and the least standardized schema, as the proof target.
- Step 3: they run the new approach against that dataset using whatever scripts and compute are already lying around, not a clean production deployment, because the goal is proving the method catches what manual checks miss, not proving it is fast yet.
- Step 4: while running that proof, they simultaneously write up the general validation rules as a reusable checklist and a small library function, so the result is not locked inside one person's one-off script.
- Step 5: they present the worst-dataset result first, not a tidy example, when pitching adoption.
- Step 6 to 7: three teams push back anyway, citing workflow disruption. The team checks whether this is ordinary adoption friction (it mostly is, for two of the three teams) or a real blocker (the third team has a genuine compliance constraint the new method has not yet addressed).
- Step 8: they set a checkpoint, revisit adoption with the two ordinary-friction teams in one quarter, and treat the third team's compliance gap as a real scope item to solve, not resistance to wait out.

Contrast the failure variant: the same team pilots the approach on a friendly team's clean dataset first, gets a smooth result, and then hears "fine for that data, but our data is different" from everyone else. Nothing about the underlying method was worse in this version; only the order of proof was wrong, and it cost the team its best evidence.

## Common failure modes

- **Leading with an efficient, routine, easy case to "ease people in."** This invites direct comparison against the old method on its own best ground and produces exactly the "why not the old way" response the heroic-task-first sequence exists to avoid.
- **Treating normal adoption friction as proof the idea is bad.** Abandoning a sound method the first time someone pushes back, mistaking the structural default for a verdict on the work itself.
- **Running the heroic-task proof once, as a one-off stunt, with no reusable method built alongside it.** The result cannot be repeated, taught, or handed off, and stalls permanently at "it worked that one time."
- **Persisting indefinitely against resistance on the theory that all resistance is just the expected barrier.** Never re-checking whether the actual remaining barrier still justifies the effort against the payoff turns healthy persistence into frittering away effort against inertia.
- **Picking the proof case for stakeholder comfort instead of maximum doubt removal.** Choosing something close to what people already believe possible defeats the purpose of the demonstration before it even starts.
- **Skipping straight to selling or presenting the result before the heroic-task proof and the reusable method both actually exist.** This borrows credibility the work has not yet earned, and it is the wrong skill to reach for until the proof is real.

## References

Hamming, R. W. (1997). *The Art of Doing Science and Engineering: Learning to Learn*, Chapter 5, "History of Computer Applications" (Gordon and Breach).

Siblings: hamming-sell-your-work (once the heroic-task proof and reusable method exist, that skill governs presenting the result and getting it adopted; this skill governs the sequencing of the proof itself, upstream of any pitch), hamming-equivalent-job (once a method is adopted, it reshapes the task itself rather than replacing it unchanged, a natural next question once the heroic-task proof lands), hamming-defect-into-asset (inverting a fixed constraint into direction, for situational limitations rather than proving new capability against doubt).

Chapter 5 sits between Hamming's chapters on hardware and software limits and his chapters on Artificial Intelligence; he frames it as the chapter where "the economics, the applications" of computing take over as the dominant force shaping what actually gets built. The heroic-task-first sequence is offered there as the general lesson underneath his own career of solving harder and harder problems on ever-cruder machines, before the field's routine, economical applications became possible at all.
