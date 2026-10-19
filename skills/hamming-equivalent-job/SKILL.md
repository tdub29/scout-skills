---
name: hamming-equivalent-job
description: Apply before scoping any automation, tool rollout, or AI integration. Hamming's rule, from The Art of Doing Science and Engineering: Learning to Learn (1997): when you successfully use a machine you do an equivalent job, not the same old one. A tool that "just speeds up" the current task is a myth; the task gets reshaped, so name the new job, not the old one it meant to replace. Trigger this when someone automates a manual workflow (reconciliation spreadsheet, review queue, data entry) and frames the goal as pure speed-up with every human step around it unchanged; when they bolt an LLM or agent onto an existing process assuming upstream and downstream steps stay identical; when they scope a "lift and shift" as complete once behavior matches the old system; when the design assumes one live, shared, mutating source of truth that multiple people or processes read and write while wanting controlled before/after comparisons against it; when a tool is built to mimic the human method instead of exploiting what the machine does well; or when a rollout plan freezes scope as if the tool's role will never shift again. Fence against generic project scoping, which asks cost and timeline; this asks what job will actually exist once the tool lands. Timely for AI automation, where "point the model at the existing process" is the default and usually wrong framing. Output is a redefinition of the equivalent job the tool will actually create, plus flags on 1:1-replacement and shared-mutable-state assumptions.
---

# Hamming: An Equivalent Job, Not the Same Job

## When to use

Reach for this skill at the moment someone is scoping what a tool, script, model, or automated system will do to an existing task, not after it has already shipped and the surprises have already landed. Concrete cues:

- Someone is automating a manual workflow (spreadsheet reconciliation, a manual QA pass, data entry, a review queue) and describes the payoff purely as "faster," with every human step around it assumed to stay exactly as it is today.
- Someone is adding an AI model, LLM agent, or new tool into an existing pipeline and assumes the steps before and after it are unaffected by its presence.
- Someone is scoping a "lift and shift" migration, or a straight port of a process onto new infrastructure, and treats the port as finished once outputs match the old system bit for bit.
- The design calls for one live, continuously updated shared source of truth (a shared plan, shared dataset, shared model, shared tape) that multiple people or processes will read and write concurrently, while someone also wants to run a controlled before/after comparison against it.
- A robot, script, or model is being built to replicate the human method step by step, instead of being asked what shape actually exploits the machine's own strengths and constraints.
- A rollout plan freezes the tool's scope at launch and treats any later reshaping of its role as scope creep or failure rather than the expected next phase.
- A retro or postmortem is asking why an automation project technically works (outputs match) but the workflow around it still feels wrong, underused, or fought by the people who have to live with it.
- Someone credits a tool purely with a speed multiplier and has not asked what new option or decision point that speed actually opened up.

- A team is debating whether a new tool's rollout "failed" purely because it did not reduce headcount or hours the way the business case promised, without checking whether it changed the nature of the work those hours were spent on instead.

Do not trigger for:

- Plain cost, timeline, or resourcing scoping questions where nothing about the task itself is being reshaped. That is generic project management, and this skill has nothing to add to it.

- A true like-for-like infrastructure move (moving a static file to a new server, upgrading a library version) where the artifact is genuinely meant to stay identical and no workflow sits around it waiting to be reorganized.

- Pure feasibility questions ("can this even be done at all, on the hardest case we have"). That is hamming-heroic-task-first's lane, proving a method can be trusted before it earns routine use, a question that logically comes before this one.

- General AI safety, bias, or ethics review. That is a different discipline, and treating it as a scope-reshaping question would dilute both skills.

## The framework

Hamming states the rule three separate times, in three different domains (lab instrumentation, enterprise data management, shipboard robotics), which is why it survives as a general law and not a one-off anecdote. Apply all four sub-concepts together. Naming the new job without checking the shared-baseline trap, or redesigning around the tool's strengths without leaving room for further drift, only catches part of the failure.

### Core thesis

> "When you successfully use a computer you usually do an equivalent job, not the same old one."

> "Realize, as a general rule, it is not the same job you should do with a machine, but rather an equivalent one, and do it so then future, flexible, expansion can be easily added (if you do succeed)."

A tool introduced into a workflow does not leave the workflow's shape intact and merely run it quicker. Once the tool is actually in use, the task reorganizes itself around what the tool makes newly possible, or newly hard, and a plan that only budgeted for speed-up gets surprised, usually late, by a task that has quietly become a different task. The thesis has two working parts:

- The tool changes what the task fundamentally is, not just its throughput. Treat "how much faster" as the wrong first question and "what can we now do that we couldn't before" as the right one.
- The redesign has to leave room for continued reshaping, since a tool that succeeds keeps drifting away from the exact shape first imagined for it, not settling into it.

Both parts matter together. A plan that names the new job but locks it down at launch will still be blindsided a few months in, once the tool's real use has moved past the spec that described it on day one.

### Automation changes the task's nature, not just its speed

Hamming's own case is the small SDS-910 computer wired to the Brookhaven cyclotron. It was proposed, under the pretext of "gathering, reducing, and displaying" data faster, and it did do that. But its real effect was different in kind: researchers could now watch the data appear mid-run and abort or redesign an experiment on the spot (the specimen off-center, a strange edge effect, something worth stopping for), instead of running to completion and only discovering the problem afterward.

> "We got the machine in under one pretext, but its presence in the long run changed both the problem and what the computer was actually used for."

Hamming's own estimate was that the cheap, small machine "at least doubled the effective productivity of the huge, expensive cyclotron," not by doing the old job faster but by turning a fixed batch process into a live, steerable one. Ask, for every step slated for a tool:

- Does the tool change what decision is available at this step (steer mid-run, catch an error earlier, skip a step entirely, batch it differently), or does it only perform the same fixed decision faster?
- If the honest answer is "only faster," look harder. A tool rarely earns its adoption cost on speed alone, and the qualitative change, once found, is usually where the real value and the real scope surprise both live.

### A moving shared baseline defeats controlled comparison (the Boeing tape story)

Boeing's plan was a single master tape holding the current status of a plane design, so every part of the company would stay in sync automatically. It did not work out as planned. If the shared data changes while you are studying, say, wing shape and profile, an apparent improvement you find might actually be someone else's silent edit landing in the same window, not your change at all, and might even be masking a change that made things worse.

> "You simply cannot use a constantly changing data base for an optimization study."

Engineers worked around it in practice by forking a private snapshot of the tape for the duration of a study, and reconciling with the shared master only once their own design was finalized. The same trap reappears today as:

- A "single shared knowledge base" an AI agent reads and writes concurrently with the humans it is supposed to be helping.
- A shared live model being retrained or fine-tuned while someone is trying to A/B test a prompt or feature change against it.
- A shared planning document or dataset being edited by other stakeholders during the exact window of a before/after study.

Anywhere a design calls for one continuously mutating source of truth, read and written by multiple parties, and someone also wants attributable, controlled comparisons run against it, the two goals are in direct conflict. Resolve it explicitly: either freeze a snapshot baseline for the duration of any comparison, or drop controlled comparison as a design goal and say so out loud instead of quietly producing numbers nobody can trust.

### Reengineer around the tool's strengths, not the human method (ceiling-rail robots)

Hamming's Navy example: a mobile robot on a ship does not need legs. Running the robot on rails from the ceiling sidesteps the actual problem (things fall to the deck, the ship pitches violently in combat or heavy seas, a walking gait built for a stable floor is the wrong transfer) rather than solving it by better mimicking human locomotion.

> "That is another example of what I have been repeatedly saying, when you go to machines you do an equivalent job, not the same one."

The design question is never "how do we get the machine to do it the way a person does it." It is "what shape of solution actually fits this machine's strengths and this environment's constraints." Two modern instances of the same mistake:

- An agent that clicks through a graphical interface exactly as a human would, screen by screen, when it already has direct API access to the same data and actions.
- A model forced to "read" a formatted report the way an analyst skims it, when it could ingest the underlying table or database directly and skip the formatting layer entirely.

Both are the ceiling-rail problem solved with legs. Look for the equivalent of rails: the path that only makes sense once you stop asking the machine to imitate the person.

- Before locking a design, ask specifically what a solution would look like if no human had ever done this task by hand. If the honest answer looks nothing like your current draft, your draft is probably still walking on legs.

### Leave room for the job to keep drifting

Hamming brought the SDS-910 in "under one pretext," and its presence went on to change both the problem and what the computer ended up being used for, well past the original ask. He generalizes this into a design habit for anyone building a tool meant to handle more than one fixed case: organize the tool so it can cope with next year's range of problems, not only the one instance sitting in front of you today, since you will not know in detail what will come next but you can know the tool needs room to take it.

- Treat the first rollout's scope as the starting shape, not the final spec.
- Build explicit extension points into the design rather than hard-coding today's exact process.
- Put a review checkpoint on the calendar after real usage starts, since the tool's actual equivalent job is discovered in production, not fully knowable at design time.
- Expect resistance to this framing from anyone who signed off on a fixed-scope spec; a plan that admits it will keep reshaping itself reads, to a budget owner, like an admission the estimate is soft. Hold the line anyway; the alternative is a spec that quietly goes stale the first month it is in production.

## How to apply

1. Write down the literal current task exactly as it is done today: every manual step, check, correction, and escalation included, before writing a single line about the tool.
   - Include the steps nobody put in the official process doc: the workaround someone quietly does every Friday, the judgment call that never got written down.
2. Separately, write down what the tool is actually good at (raw speed, tirelessness, ability to inspect state mid-process, bandwidth, parallelism, direct data access) rather than what would make it a drop-in replacement for a step in list 1.
   - If you cannot name a strength beyond "faster than a person," treat that as a warning sign, not a green light; keep digging before scoping the build.
3. For every step slated for automation, ask whether the tool opens a qualitatively new option there (steer mid-run, catch it earlier, skip it, batch it differently), rather than only performing the same fixed step faster. Name that new option explicitly; it is the equivalent job.
4. If the design assumes one live, shared, continuously updated source of truth read and written by multiple people or processes, run the Boeing test: could two different, unrelated changes both plausibly explain the same apparent improvement or regression? If yes, either freeze a snapshot baseline for any comparison study, or drop controlled comparison as a design goal and say so out loud.
5. Check whether the current design was produced by copying the human method onto the machine (mimicking manual steps one for one), or by asking what shape best exploits the machine's real constraints and strengths. If it is the former, redesign around the latter, ceiling rails rather than legs.
6. Write the redefinition of the equivalent job in one paragraph: what task will actually exist after rollout, who or what performs each part of it, and exactly how it differs from the task it is replacing. This paragraph is the artifact this skill produces.
   - Circulate that paragraph to whoever owns the steps immediately upstream and downstream of the tool; their steps are the ones most likely to quietly change shape once the tool lands.
7. Build explicit checkpoints into the rollout plan for renegotiating scope after real usage starts, since the tool's actual role will keep drifting from the launch spec if the rollout is succeeding at all.
8. Sanity check: describe the redefined job to someone who has not seen the plan, and ask them what job the tool actually does. If their answer matches your original "does the same thing, just faster" framing word for word, the equivalent job has not been found yet; return to step 3.

Worked example, compressed from Hamming's own cyclotron story: a team plans to "automate the manual data review step" with a small script that gathers and displays incoming results. Scoped as 1:1 replacement, the project ships, matches the manual review's output, and looks done. Applying step 3, someone asks what new option the live display actually creates: the reviewer can now watch results arrive mid-run and stop a flawed run early instead of only reviewing after the fact. That is the equivalent job, catching bad runs before they finish, not reviewing the same fixed batch faster, and it changes what the reviewer's role even is going forward.

Six months later the same team, applying step 7's checkpoint, notices reviewers have started asking the tool to flag borderline cases automatically rather than watching every run themselves. Nobody scoped that. It is the job continuing to drift, exactly as expected, and the checkpoint exists so the team notices and redesigns around it instead of being the last to find out.

## Common failure modes

- Scoping as literal 1:1 replacement ("same steps, automated") and being blindsided when the workflow reorganizes itself around the tool anyway, on its own timeline instead of yours.

- Building a shared mutable-state system (one live database, model, or plan multiple parties edit concurrently) when a frozen baseline is what a controlled comparison actually requires; results become unattributable even though the numbers look fine.

- Copying the human method onto the machine instead of designing for the machine's own strengths and constraints (a walking robot instead of a ceiling rail, an agent driving a GUI like a person instead of calling the API it already has).

- Freezing scope at launch and treating any later reshaping of the tool's role as scope creep or a broken plan, instead of the expected next phase of an adoption that is actually working.

- Declaring success once outputs match the old system bit for bit, without ever asking what new decision points or capabilities the tool actually opened up; a mid-run abort capability, for instance, is easy to miss if throughput was the only thing being measured.

- Assuming a shared "single source of truth" is unambiguously good without checking who reads it, who writes it, and whether any comparison or attribution work depends on it holding still while the study runs.

- Measuring the rollout only against the old task's success metric, when the equivalent job may have made that metric the wrong one to track; a faster batch report is a poor grade for a tool whose real contribution was enabling a mid-run abort nobody previously had.

## References

Hamming, Richard W. The Art of Doing Science and Engineering: Learning to Learn. Gordon and Breach, 1997. Chapter 5, "History of Computer Applications" (the SDS-910/Brookhaven cyclotron story and the Boeing shared-tape story, both stated as the explicit "equivalent job" rule, pp. 36 to 38). Chapter 7 (the shipboard ceiling-rail robot example, the same rule restated a third time in a different domain, p. 50).

Read Chapter 5 in full before applying this skill to a high-stakes rollout; the cyclotron and Boeing stories sit inside a larger argument about the economics of computer applications that gives the rule its full weight.

Sibling skills, same source:

- hamming-heroic-task-first: covers the prior question of whether a new method can be trusted at all, proving it on the hardest available case with the crudest resources before it earns the right to do routine, economical work. Use before this skill when feasibility itself, not scope, is still in doubt.
- hamming-reading-new-tech: covers how to evaluate and absorb an unfamiliar technology or method before committing to it, so the "what the tool is actually good at" half of this skill's analysis rests on real understanding rather than a vendor's pitch.
- hamming-transfer-test: covers checking whether a lesson or method that worked in one context actually transfers to a new one before relying on it a second time, a useful check on any assumption that the redefined job here will generalize automatically to the next use case.

Use this skill at the scoping stage, before build starts, not as a retrospective explanation for why an already-shipped tool behaves strangely. The redefinition of the equivalent job is meant to change the plan while it can still be changed.

If a tool has already shipped and only now is behaving strangely, this skill still applies retroactively: write the redefinition paragraph for the job it is actually doing today, compare it to the job it was scoped to do, and use the gap to explain the strangeness rather than treating the tool as broken.

The rule generalizes past computers, past robots, past any single decade of technology. Any time a new capability enters a workflow that used to run on older constraints, expect the workflow itself, not just its speed, to be up for renegotiation.

That holds for a spreadsheet macro, a fine-tuned model, or a fully autonomous agent alike: the size of the tool changes, the rule does not.
