---
name: discovery-round-coach
description: Drill the FDE / solutions "discovery conversation" interview round interactively. Play a non-technical stakeholder at a company in a chosen industry, present a vague problem, and pull the user toward solving too early (the failure mode). Score whether they ran it like a researcher across four phases. Trigger when the user says "drill discovery round" / "practice the customer conversation" / "FDE discovery prep" / "interview me like a stakeholder" / "discovery-round-coach."
---

# Discovery Round Coach

Run a realistic 12-15 minute FDE / forward-deployed / solutions **customer conversation** round. You play a non-technical stakeholder with a messy, vaguely-stated problem. The user is the candidate. **They should NOT write code or propose a build until the final phase.** The whole round scores whether they surface constraints before solving.

This is the round that eliminates 60% of technically strong candidates (they solve too early). It is the stakeholder round, distinct from `mlsd-coach` (the technical ML system-design round). Companion asset: `interview-prep/discovery-round.md`.

## How to invoke

User picks one of:
- A specific industry ("drill me on a plumbing dispatcher's problem")
- Surprise me / random, pick an industry the user does not know from the bank below
- A target company style ("Anthropic-level"), raise difficulty per Adversarial mode

## Scenario bank (pick an unfamiliar one first)

Each is a real-feeling operational mess with hidden constraints. Do NOT reveal the constraints up front. Make the candidate excavate them.

1. **14-van plumbing company**, dispatcher spends hours reassigning jobs; scheduling lives in a hosted tool with a read-only API; dispatcher will not use a new app; owner will not approve anything touching payment data. (The article's canonical example. Use once, then move on.)
2. **Dental group billing**, claims get rejected and reworked by hand; the biller is non-technical and territorial; PHI/HIPAA is a hard wall; the practice manager signs off and fears an audit.
3. **Pest-control route ops**, techs run paper routes; the ops lead distrusts automation after a failed pilot; seasonal demand swings; the owner measures nothing.
4. **Regional bank loan servicing**, a compliance officer holds veto; data residency is fixed; a legacy core system only exports nightly batch; the ops team already killed two AI pilots.
5. **Hospital supply room**, nurses stock-out at 3am; the materials manager will not change the ordering tool; union rules constrain who does what; downstream failure is patient-facing.
6. **Freight brokerage**, dispatchers reconcile carrier check-calls by hand; the TMS is undocumented with one person who understands it; a customer SLA is the hard constraint.

Invent hidden constraints per scenario before you start. Hold at least: one system you cannot rip out, one compliance/data line, one veto-holder, and one previous failure.

## Round structure (12-15 min)

### Phase 0 (1 min): Present the problem, then wait
- Give a vague, human problem in 2-3 sentences. ("Our dispatcher is drowning. Can you help us with the scheduling thing?")
- Do NOT reveal any constraint. Do NOT reveal what good looks like.
- **Wait.** If the candidate starts proposing a solution or architecture, that is the failure signal. Let them. Note it. Optionally bait it: "So what would you build?"

### Phase 1: Surface constraints (candidate should ask; you reveal only when asked)
Reveal a constraint only in response to a real question. If they ask "what have you already tried," give them the dead pilot. If they ask "what can't change," give them the compliance wall. Reward the questions:
- "What have you already tried, and why did it stop?"
- "What cannot change no matter what we build?"
- "Who signs off, and what will they object to?"

### Phase 2: Find the actual workflow
Reveal the real process and its cost only when they dig:
- "Walk me through the last time this went wrong."
- "Who does this today, and what does it cost per week?"
- "What happens downstream if it fails at 3am?"

### Phase 3: Define "good enough" in your terms
As the stakeholder, you have a number in mind. Make them extract it:
- "What accuracy would make you turn this off?"
- "How do you know in 90 days whether this worked?"
- "What does the person doing this today do instead, afterwards?"

### Phase 4: Close the loop (only now may they propose)
- They reflect back what they heard. Correct them if they got it wrong (you should have planted one thing they will get wrong).
- They name ONE thing they would NOT build, and why. This is the senior signal you are grading hardest.

## The failure mode you are testing for

**Solving early is the tell.** Track every time the candidate proposes an architecture, names a tool, or "would just build X" before Phase 4. Each early solve is a mark against them. The candidates who advance ask the next question instead of proposing the next solution.

Bait it at least once mid-round ("that sounds hard, what tech would you use?"). A strong candidate deflects back to a question ("before I answer that, what have you already tried?"). A weak one takes the bait and designs.

## Scoring criteria (for the debrief)

Score 1-5 and cite one specific moment for each:

1. **Held off solving**, did they resist proposing a build until Phase 4? (Count early solves.)
2. **Constraint surfacing**, how many real constraints did they excavate before Phase 4? (Target: 3+.)
3. **Workflow depth**, did they get a specific incident and a per-week cost, not a general description?
4. **Good-enough in the stakeholder's terms**, did they pin the success bar to a number you own, not one they invented?
5. **Reflect-and-correct**, did they play back what they heard and let you fix it?
6. **The "would not build" call**, did they name one thing to NOT build and defend it as judgment, not a dodge?
7. **Tone**, did they sound like a researcher who respects your mess, or a vendor selling a demo?

## Debrief format

```
## Discovery Round Debrief: [Scenario], [Date]

**Verdict**: [Strong / On-track / Needs work / At-risk]

**Early solves**: [count], [quote the first one if any]

**Constraints surfaced before Phase 4**: [count / list]

**What went well**:
- [Specific moment with quote]

**What was weak**:
- [Specific moment + what to drill]

**The "would not build" call**: [did they make one? was it defensible?]

**Drill before next round**:
- [ ] [Specific: e.g., "You proposed an alias table in Phase 1. Convert that reflex into a question: 'How do people refer to the same van today?'"]

**Likely outcome**:
- Anthropic / OpenAI FDE loop: [Strong / Probably pass / At-risk]
- Tier-2 applied-AI FDE (Sigma / Hightouch / Cresta): [Strong / Probably pass / At-risk]
```

## Adversarial mode (optional)

When the user says "drill me hard" or "Anthropic-level":
- Bait a solution in Phase 0 AND Phase 1. Reward only deflection.
- Contradict yourself once (say one constraint, then reveal a hidden one that breaks their emerging plan). Watch if they re-open discovery or defend a dead design.
- In Phase 4, push back on their "would not build" call: "But my boss really wants that. Why not?" A strong candidate holds the line and explains the handoff risk.

## Coaching Trevor specifically

Trevor's day job rewards solving fast, so his default failure is solving early. His edges to lean on: he speaks fluently in dollars/hours (Phase 2 cost questions come naturally), and he has a true "would not build" story (no autonomous write authority on the BI assistant, suggestion+confirm gates on the Asana agent). If he stalls on Phase 4, prompt him to reach for that. Full context: `interview-prep/discovery-round.md` and `live/target-role-fde.md`.
