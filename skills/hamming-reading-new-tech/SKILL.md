---
name: hamming-reading-new-tech
description: "Size up an emerging technology from outside it"
---

# Hamming: Reading a New Technology Before It Matures

You do not need to become an expert to read a nascent technology's path correctly. Hamming tracked fiber optics for over a decade at Bell Labs, attending a single seminar and never contributing a technical result to the field, and still called the trajectory right: bandwidth would win, splicing would get solved, optical amplification was coming, satellites would lose ground to cable. This skill is that method. Watch structure, not detail, from outside the specialty.

The five signals below are transferable across any nascent technology (a new battery chemistry, a sensor class, a materials process, a software paradigm), not specific to fiber optics itself; fiber optics is simply the worked example Hamming gave in real time, as it happened.

## When to use

Use this the moment you must decide how much attention an unfamiliar, fast-moving technology deserves, without spending the years it would take to become a specialist in it.

Cues:

1. Someone asks whether an emerging technology, outside your own field, deserves to be taken seriously.
2. A lab result, demo, or pilot is being cited as proof the technology is close to real-world deployment.
3. A durability, reliability, or scaling failure is reported, and you must decide if it is a dealbreaker or an ordinary engineering problem in progress.
4. A vendor, analyst, or excited colleague calls something "new," and you must judge whether it is genuinely new or the old thing with extra steps.
5. Several competing approaches to the same sub-problem are showing up in the trade press or research literature at once.
6. A visibly ugly, stopgap-looking piece of a shipped system exists, and you want to know where the next wave of engineering effort is about to land.
7. You have limited attention and several emerging technologies competing for it, and need a cheap way to triage them.
8. You are asked to forecast the trajectory of something you have no intention of becoming an expert in.

Don't trigger for:

- A request for a probability, confidence interval, or "how likely is this to happen by year X." That is calibration work; route to tetlock-superforecasting. This skill produces a structural read; the forecasting skill turns that read into an actual number.
- A question purely about legal, regulatory, political, or economic adoption barriers once the technical read is already done. Hamming treats this as a separate question on purpose (see Common failure modes and References below).
- A request to actually build depth or expertise in the field. This skill is explicitly for staying a well-informed outsider. The moment the technology becomes central to your own work, go get the depth instead of continuing to read structure from a distance.
- A plain fact-check with no emerging-technology judgment involved, such as a spec lookup or a released product's documented feature.

These fences matter because the three questions look similar from a distance (is this technology worth caring about) but are answered by three different disciplines: structural reading (here), calibrated probability (tetlock-superforecasting), and legal/economic/political analysis (out of scope for any of these skills). Answering the wrong one convincingly is worse than admitting you have not answered the right one at all.

## The framework

Core thesis: you can anticipate a technology's path, and decide where to place your attention, from outside the specialty, by watching structure rather than absorbing every detail. The structure has five recurring signals.

This framework has a narrow job. It reads structure and produces a qualitative attention decision. It does not produce a probability or a date (that is tetlock-superforecasting's job, once the structural read is in hand), and it does not answer whether a technologically solved problem will actually be adopted (that turns on legal, regulatory, and economic conditions Hamming treats as a separate question entirely, see Common failure modes). Keep the three jobs separate rather than folding them into one paragraph.

| Sub-concept | One-line cue |
|---|---|
| Fundamental advantage | one sentence, the structural mechanism, not the quotable line |
| Near-term bottleneck | name it early, count who is attacking it |
| Lab versus field | expert-in-controlled-conditions is not technician-in-a-hurry |
| Worst possible design | today's ugly stopgap names tomorrow's engineering wave |
| Order-of-magnitude shifts | a factor of ten is a new thing, not an old thing sped up |

The five signals are cumulative, not a checklist to satisfy one at a time. A technology can have a real fundamental advantage and still deserve low attention if its bottleneck has no active attackers; it can have an actively attacked bottleneck and still deserve low attention if the advantage turns out to be secondary, not fundamental. Read all five before writing the one-paragraph output.

### The one-sentence fundamental advantage

Name the one single-sentence advantage that is structurally true, and set aside surface novelty and quotable color. For fiber optics it was bandwidth: "optical frequencies were very much higher than the electrical ones in use at the time, and hence the fiber optics would have much greater bandwidth... bandwidth is the name of the game for the telephone company." The talk's memorable line, "God loved sand, He made so much of it," pointed at a real but secondary advantage (material supply). The fundamental one was bandwidth, stated once, in one sentence.

Apply when: a pitch arrives with several benefits listed, and you need to find the one claim that would matter on its own, regardless of the rest.

### The near-term bottleneck and who is attacking it

Identify the practical problem that will decide near-term deployment, then count the independent groups or approaches working on it. Hamming spotted fiber splicing as the likely sticking point on his own, from having soldered Heathkits: "how did they propose to splice these fine, hair sized, glass fibers and still have good transmission?" Years later, once "a number of quite clever ways [had been] proposed and tested," the sheer count itself became the signal: "the very number of alternates made me decide probably that feature... would be handled fairly easily." Many independent attempts at a fix is evidence the bottleneck is ordinary solvable engineering, not a wall.

Apply when: a single named obstacle is being used to argue an entire technology will not work.

### Lab feasibility versus field reliability

Treat "it works" as two separate claims with two separate confidence levels: works in the lab, done by experts, under controlled conditions; and works in the field, done by technicians in a hurry, under adverse conditions. Hamming had watched other companies' projects "come to grief on the miserable fact what can be done reliably in the lab by experts is not always the same as what can be done in the field by technicians who are in a hurry." The real proof for fiber splicing was not a lab demonstration, it was the multi-year field trial connecting central offices in Atlanta.

Apply when: a lab result, pilot program, or polished demo is being extrapolated straight to deployment at scale.

### "Worst possible design" stopgaps as a signal

When a working, shipped system contains a step so awkward you would call it "hard to imagine a worse system design," treat that ugliness as a map of where effort is about to concentrate, not as an embarrassment to ignore. Hamming saw the detect, convert to electronic, amplify, convert back to optical relay chain in early fiber systems, and immediately knew where the coming engineering wave would land: optical amplification, eventually solitons. The uglier the tolerated stopgap, the more certain, and the more valuable, the coming fix.

Apply when: a shipped system has an obviously clunky workaround that everyone tolerates, and you want to predict where research investment is about to concentrate.

### Order-of-magnitude shifts are not the old thing with extra steps

Do not dismiss a step-change as incremental just because it superficially resembles a familiar category. "Typically a single order of magnitude change (a factor of 10) produces fundamentally new effects." People who insisted computers were "nothing more than large, fast desk calculators," and that "anything you can do by a machine you can do by hand," made no significant contributions to computing; those who treated computers as something new, to be studied on their own merits, did. The identical reflex, at first, kept digital filters "viewed merely as a variant of the classical analog filters."

Apply when: someone, possibly you, is mapping a new technology onto an old, familiar category to make it feel less unfamiliar, without checking the actual multiplier.

## How to apply

Work the five signals into a single one-paragraph read and an explicit attention decision. Do not stop at the signals themselves; an unfinished list of observations is not the deliverable.

1. State the one-sentence fundamental advantage.
   - Write it as a single mechanism-level claim (frequency, scale, or cost is an order of magnitude different, which changes this specific downstream thing), not a list of nice-to-haves.
   - If it will not compress to one sentence, you do not understand it well enough yet to have an opinion worth acting on.
2. Identify the near-term bottleneck the technology must clear before wide deployment.
   - Ask specifically what would stop this from shipping in the next product or research cycle, not what could theoretically go wrong someday.
3. Count how many independent groups, companies, or distinct approaches are attacking that bottleneck right now.
   - Zero or one active attempt is a real warning sign. Several independent, differently shaped attempts is a signal, not a guarantee, that the bottleneck is solvable engineering.
4. Sort every "it works" claim into lab-under-experts or field-under-technicians, and require field evidence before treating the bottleneck as closed.
   - A trial run for years under real operating conditions outweighs any number of polished demonstrations.
5. Scan the current production system, or its closest existing analog, for a visibly ugly, tolerated stopgap.
   - If a "worst possible design" step is in production anyway, that is where the next concentrated engineering effort, and the next real news, will come from.
6. Check your own reaction to the technology for the desk-calculator reflex.
   - Are you calling it "just X with extra steps" because it resembles something familiar, or because you actually checked the order of magnitude on bandwidth, cost, speed, or scale? If unchecked, go verify the number before concluding either way.
7. Write the one-paragraph read: the fundamental advantage, the bottleneck plus who is attacking it, any worst-possible-design stopgap currently in production, and a decision on where to place your attention.
   - Use the decision table below to pick the attention level; do not leave it as a vague "keep an eye on it."
8. Sanity check: could you deliver this read to someone in five minutes without leaning on a single piece of the field's own jargon?
   - If not, you have drifted from outside observer into partial specialist, and should step back to the structural signals above before writing the paragraph.

Final sanity check on the whole exercise: Hamming never became a fiber-optics expert and never produced a technical result in the field, yet he read its shape correctly for over a decade using exactly these five signals. If your one-paragraph read requires expertise you do not actually have to defend it, you have built it correctly. If defending it requires that expertise, you have quietly become a domain participant rather than an outside reader, and the honest move is to say so and reclassify the task.

Attention-placement decision table:

| Condition found in steps 1 to 6 | Attention decision |
|---|---|
| Clear fundamental advantage, bottleneck has several independent attackers, no field evidence yet | Watch closely; recheck at the next field trial or production milestone |
| Clear fundamental advantage, bottleneck has zero or one attacker, or field evidence keeps failing | Check back on a fixed schedule (a year, a product cycle); do not chase every incremental announcement |
| No clear one-sentence advantage, or the "advantage" is really a secondary benefit | Set aside for now; revisit only if a genuine fundamental advantage surfaces |
| Fundamental advantage is a real order-of-magnitude shift and a visibly ugly stopgap is already in production | Watch closely; this is where the next wave of engineering, and the next real news, is about to land |

### Worked example

Claim under review: an outside observer hears about early fiber optics and must decide how much attention it deserves, without joining the field.

- Fundamental advantage (step 1): optical frequencies are orders of magnitude higher than the electrical frequencies then in use, which directly increases bandwidth, the metric that mattered most to the telephone company.
- Bottleneck and attackers (steps 2 to 3): splicing hair-thin glass fiber with acceptable transmission loss. Over time, multiple independent splicing techniques were proposed and tested; the growing count of alternates was itself the signal the problem was tractable engineering, not a wall.
- Lab versus field (step 4): splicing worked in supervised lab settings well before it was proven in the field. The real evidence arrived only with the multi-year Atlanta central-office trial, run under real operating conditions.
- Worst possible design (step 5): the detect, convert to electronic, amplify, convert back to optical relay chain was visibly the worst possible way to build the system, and correctly flagged optical amplification as the next major wave of engineering investment.
- Order-of-magnitude check (step 6): the bandwidth jump was a genuine structural shift, not a marginal improvement on copper, so it did not fall into the "old thing with extra steps" trap.
- Decision (step 7, using the table): clear fundamental advantage, an actively attacked bottleneck, and a visibly ugly stopgap already in production. Watch closely.
- What this read deliberately excludes: no probability was assigned to when optical amplification would ship, and no claim was made about whether regulators or competing carriers would allow universal fiber rollout. Both questions are real; neither belongs to this skill.

The same six moves (name the advantage, find the bottleneck, count the attackers, demand field evidence, read the ugly stopgap, check the order of magnitude) apply whether the technology in front of you is fiber optics, a battery chemistry, a new class of sensor, or a machine-learning technique you have no intention of specializing in.

## Common failure modes

Each of these is a way the method degrades back into either premature expertise-chasing or lazy dismissal, the two failure poles this skill sits between.

- Becoming a dilettante: treating structural reading as a permanent substitute for ever doing real depth work anywhere. This skill is for technologies outside your actual job. Once a technology becomes central to your work, reading it from outside is no longer sufficient, and this skill has done its job by telling you it is time to go deeper.
- Treating "many independent groups are attacking the bottleneck" as a guarantee rather than a signal. Some bottlenecks resist every attempt for a decade or longer. A high attempt count raises your confidence; it does not settle the question.
- Skipping the separate legal, economic, and political adoption question, and treating "technologically solved" as "will happen." Hamming closes the fiber optics chapter on exactly this point: fiber to every house was technically clear, but "it is necessary to examine political, economic, and social conditions before saying what is technologically possible will in fact happen."
- Dismissing an order-of-magnitude shift as incremental because it resembles a familiar category (the desk-calculator mistake, the "just a variant of the classical analog filter" mistake). Check the actual multiplier before deciding "nothing new here."
- Confusing an impressive lab demo with field readiness because it was well funded, well credentialed, or visually striking. Impressiveness and technician-in-a-hurry robustness are different axes entirely.
- Misidentifying the fundamental advantage: letting a real but secondary benefit (material supply, weight, a quotable line from a talk) get promoted to "the" advantage, while the true structural one goes unstated and unchecked.

## References

- Hamming, Richard W. *The Art of Doing Science and Engineering: Learning to Learn* (1997, Gordon & Breach), Chapter 21, "Fiber Optics."
- The order-of-magnitude, "fast desk calculators" material is drawn from the same book's Chapter 15, "Digital Filters, II," and is folded in here because Hamming applies it as the same generalizable heuristic to a different technology.
- Siblings: hamming-equivalent-job, hamming-question-experts, hamming-heroic-task-first (other frameworks carved from this book).
- Route probability, confidence, or "how likely is adoption" questions to tetlock-superforecasting. This skill supplies the structural read a probability estimate would then be built on, not the estimate itself.
- The legal, economic, and political adoption question Hamming raises at the end of the chapter is deliberately out of scope here; it is a separate analysis, not a structural-signal problem.
- Chapter 1's possible, likely, desirable "vision" trichotomy is a distinct, already-carved framework folded into tetlock-superforecasting. Do not re-derive it here.
- Hamming frames this chapter explicitly as a demonstration of method over a specific result: "I have told you as best I can, how I approached a new technology, what I looked for, what I watched for, what I ignored, what I kept abreast of, and what I pondered." Treat the fiber optics detail as the worked example, not the point.

Bottom line: name the one-sentence advantage, find the bottleneck and who is attacking it, demand field evidence before lab evidence counts, read the ugliest stopgap as tomorrow's project list, and never call a factor of ten "nothing new."
