---
name: agent-design-audit
description: "AI agent or multi-agent system design review"
---

# agent-design-audit

A design and review lens for agent systems, distilled from Eric Xing, Mingkai Deng, and Jinyu Hou, "Critique of Agent Model" (arXiv:2606.23991, 2026). The full mapping onto this workspace lives in [[reference_agent-model-critique]]; this skill is the on-demand procedure you run when you are actually building or reviewing an agent.

Use it when the task is to design, review, critique, or debug an agent, a multi-agent workflow, an orchestration setup, a set of agent operating rules, or the harness itself. It does not build models. It tells you where a design is under-scaffolded and whether the autonomy you are claiming is real.

## Step 1: make the agentic vs agentive call

- **Agentic**: competence lives in external scaffolding. Goals, identity, planning depth, and learning schedule are supplied by prompts, tool wiring, workflow scripts, or rules. Built for prescribed tasks.
- **Agentive**: the same structures are internalized. The system forms its own goals, evolves its own self-model, regulates its own deliberation, and learns continuously with no external intervention. Open-world autonomy.

State which one the system is, plainly. Almost everything anyone builds today, including this workspace's harness, is agentic, and for a prescribed task that is the correct choice, not a shortfall. The failure mode to catch is a design that *claims* agentive autonomy but is really scaffolding with the seams hidden. If you cannot point to where a structure is internalized, it is not.

## Step 2: walk the five dimensions

For each axis, ask: where does this structure live, is it explicit, and is there a gap? A gap is a dimension left implicit or assumed.

1. **Goal.** Is there a persistent objective, and is it decomposed into dependency-ordered subgoals, or is the system fed one step at a time and left to drift? A long-running task with no explicit decomposition (no todo list, no `/goal` hard-stop, no plan held outside the context window) will stop at partial and declare done.
2. **Identity.** What does the system know about its own capabilities and limits, and where is that written? In an agentic system this is the system prompt plus rules plus memory. Check it is current and not contradicted by the actual toolset. Stale identity ("harness engineering" the paper critiques) is the quiet cause of a system attempting what it cannot do.
3. **Decision-making.** How does it choose actions: pure reactive generation, or does it predict consequences before committing? An agentic analog of the paper's world model is: read before you write, dry-run before you execute, simulate on a small slice before a full fan-out. If none of those are present on a risky action, flag it.
4. **Self-regulation.** Does the system decide *when* to plan versus act, matched to difficulty and urgency, or is deliberation depth fixed? This is the paper's System III configurator. In this workspace it is the hand-written "choose the shape" step (solo / subagents / workflow / loop). The most common gap in practice: the routing decision is left implicit, so every task gets the same treatment. Name the configurator and confirm it scales with difficulty.
5. **Learning.** Does a finished run feed anything back, or is every run cold? Agentic learning is out-of-band by design: memory files, skill imports, rule edits, accomplishment logging. The gap to catch is a genuine win or correction that never gets written back anywhere, so the next run repeats the work or the mistake.

## Step 3: the GIC three-system check (for anything that plans)

The paper's architecture splits control into three layers. Use them as roles to confirm a planning system has, even informally:

- **System I (actor)** â€” fast reactive execution once a plan exists.
- **System II (planner)** â€” deliberate multi-step planning that predicts consequences.
- **System III (configurator)** â€” the meta-layer that decides how much to deliberate.

A workflow that fans out with no routing (everything gets the heavyweight path) is missing System III. A single context window doing everything at once has collapsed all three into one, which is exactly where laziness, drift, and self-grading come from. Separate them.

## Step 4: safety, auditability, controllability

Check the design against the paper's four oversight principles. In this workspace these already back the always-on rules; confirm the specific design honors them.

- **Structural transparency (auditability).** Are goals, plans, and progress inspectable as they happen, or is it a black box explained after the fact? Emit progress, never run dark ([[blocker-log-and-escalation]], [[verification-and-evidence]]).
- **Selective planning (controllability).** Does it act on a speculative plan only when the expected gain clears a margin for error, and fall back to the safe baseline otherwise? Analog: confirm hard-to-reverse or outward-facing actions, prefer the smallest safe diff, prepare-don't-execute for anything destructive or outward-facing ([[scope-and-safety]], the `guard-destructive-commands.js` hook).
- **Separation of concerns.** The thing that acts must not be the thing that certifies the act. Doing and judging are different agents (adversarial verification, [[orchestration-and-loops]]).
- **Simulate first, validate in reality.** Prefer a cheap dry-run or small-slice trial over live trial-and-error. Quarantine untrusted input from any high-privilege actor.

## Step 5: quick diagnostics

Three concrete failure shapes to check for directly, each mapped to the dimension it hides in:

- A hidden repair or retry loop that runs a second pass silently (Decision-making / System I collapsing II). If a fix happens without it showing up in the plan or the log, it did not happen transparently.
- Memory admission that lets the agent's own prior output re-enter as fact on a later turn, with no source tag distinguishing "I said this" from "this was verified" (Learning).
- A tool rule that lives only in prompt text, with no code gate enforcing it (Self-regulation / Selective planning). If the only thing stopping a bad call is an instruction, name that as a gap, not a control.

A sound tool contract returns status, a one-line summary, next_actions, and artifacts on success; a failing call returns a root-cause hint, a safe retry, and an explicit stop condition. A tool result missing these is a Step 4 finding, not a footnote.

## Output

Return a short verdict, not a lecture:

1. Agentic or agentive, one line.
2. The five dimensions as a checklist, each marked explicit or gap, with the gap named.
3. If it plans: which of System I / II / III is missing or collapsed.
4. The one or two safety principles most at risk, if any.
5. The smallest change that closes the biggest gap.

Keep it to what you can act on. The point is to make every scaffold explicit and to catch autonomy that is claimed but not built. For the full theory and the workspace mapping, see [[reference_agent-model-critique]].
