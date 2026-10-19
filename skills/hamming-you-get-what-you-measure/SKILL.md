---
name: hamming-you-get-what-you-measure
description: Fires the moment someone proposes, changes, or defends a metric, rating, grade, KPI, quota, or incentive, before it goes live. Richard Hamming, in The Art of Doing Science and Engineering, Learning to Learn (1997), names the mechanism directly, you get what you measure. The instrument chosen (a fishing net, a log scale, a lines-of-code counter) determines what becomes visible, independent of the truth underneath it, and once a measure is announced people optimize the number, not the goal it stood in for, often within days. Trigger on: a proposed or changed metric, rating scale, grade, KPI, quota, or bonus incentive; worry that a metric will be gamed; setting a rating scale's starting point (95 percent vs 50 percent vs 20 percent) or its dynamic range; choosing an easy, hard-edged proxy over the soft, relevant target it substitutes for; designing hiring, admissions, or promotion criteria that will filter people over repeated cycles; deciding whether to trust a self-reported number moving up a chain of command. This is the behavioral consequence of choosing a measure, an organizational-design act, not dashboard layout (route to kpi-dashboard-design or build-dashboard), not post-hoc analysis of data already collected (route to analytics), not the individual cognitive-bias catalog (route to behavioral-economics), and not online-experiment methodology (route to kohavi-controlled-experiments). Output is a pre-adoption metric audit (what people will actually optimize, relevance vs measurability, anchor and range, adaptation speed, selection effects, verification) plus a go/no-go and redesign moves.
---

# Hamming: You Get What You Measure

## When to use

The moment: right before a metric, rating, grade, KPI, quota, or incentive is proposed, changed, or defended, and while it can still be redesigned. Also the moment someone voices the worry that an existing measure is being gamed.

Hamming's framing of why this matters: "the way you choose to measure things controls to a large extent what happens." Not "if you measure accurately you get an accurate measurement." A different, harder claim, the instrument itself reshapes the behavior of everyone standing under it.

Cues:

1. A team is switching or adding a headline metric and asks what to watch for.
   - Example situation: support reps move from "tickets closed" to CSAT as the main rating.
2. Someone is setting the baseline or starting point of a rating scale.
   - Example situation: a manager review scale where everyone starts at 90 out of 100.
3. A scale's dynamic range comes up, ratings cluster at the middle, or letter grades vs rank-in-class surfaces as a defense against grade inflation.
4. An easy, hard-edged proxy is being chosen over a soft, relevant goal because the proxy is easier to compute or defend in a meeting.
   - Example situation: exam scores standing in for education, uptime percentage standing in for real reliability.
5. Someone proposes a bonus, quota, or incentive tied to a specific number and asks whether it is a good metric.
   - Example situation: engineers get bonuses on lines of code shipped per sprint.
6. Hiring, admissions, or promotion criteria are being set or reviewed, with the potential to filter for or against a trait over many repeated cycles.
7. A worry surfaces that people will game a metric once it is published or enforced.
8. Leadership wants to trust a number reported up several levels of an organization without an independent check on the ground.

Don't trigger for (route elsewhere):

- **kpi-dashboard-design**, **build-dashboard**: laying out a dashboard, choosing chart types, arranging tiles.
  - Contrast: "what should this metric be, and how will people react to it" is this skill; "how should this metric be displayed" is not.
- **analytics**: post-hoc analysis of data already collected, answering "what happened."
  - Contrast: "what will people do once this measure exists" is this skill; "what does the existing data show" is not.
- **behavioral-economics**: the general catalog of individual cognitive biases (anchoring, framing, loss aversion) inside one person's private choices.
  - Contrast: "how will a population collectively game this installed measure" is this skill; "why did I anchor on the first number I saw" is not.
- **kohavi-controlled-experiments**: online experiment design and statistical validity for testing a change.
  - Contrast: "is this the right thing to put on the scoreboard" is this skill; "is this experiment's methodology valid" is not.

## The framework

Core thesis: the measure you choose reshapes behavior toward the measure, often perversely, because measurement changes the system being measured. People optimize what gets counted, not the goal behind it. "You get what you measure" is not a warning about sloppy measurement, it is a warning about accurate measurement of the wrong or badly calibrated thing.

### 1. Instrument bias

"The instrument you use clearly affects what you see." Hamming retells Eddington's fishermen, who examine their catch and conclude fish have a minimum size, because their net cannot catch anything smaller, not because the sea actually works that way. The Richter scale is a log scale, so the record it produces guarantees few large earthquakes and many small ones, regardless of the true underlying distribution of energy. A lines-of-code counter rewards bloat, not clean code, because the tool counts lines, not quality.

Before trusting what a measure shows, ask what the instrument structurally cannot see, and whether the shape of the result, a minimum size, a normal distribution, a productivity score, is a fact about the world or an artifact of the tool.

Apply when: a measure's output looks like a law of nature (a distribution, a floor, a ceiling) and nobody has asked whether the tool itself manufactured that shape.

### 2. Accuracy or relevance confusion

"There is always a tendency to grab the hard, firm measurement... though it may be quite irrelevant." Height and weight are hard and firm; social attitudes are soft. Hamming's own example, school exams measure training, which is easy to grade, and neglect education, which is hard to grade but is the actual goal. "That a measurement is accurate, reproducible, and easy to make does not mean it should be done."

A softer measure that sits closer to the real goal can beat a harder measure that is merely easier to defend in a meeting or a report.

Apply when: the proposed metric is being defended on the grounds that it is easy, cheap, or precise to compute, rather than on the grounds that it is close to the actual goal.

### 3. Scale calibration, anchor and dynamic range

"If in a rating system every one starts out at 95%, then there is clearly little a person can do to raise their rating but much which will lower it." Where a scale starts sets the incentive: start everyone at 95 and the rational move is to play it safe, so the pool that eventually reaches the top is mainly conservative, exactly when the organization may need risk-takers there. Start at 50, or at 20, and there is real room to gain by taking chances, so risk-taking gets rewarded rather than punished from the outset.

Separately, range usage sets how much information a scale communicates. Most raters bunch near the middle (4, 5, 6 on a 1 to 10 scale) and rarely touch the extremes. A rater willing to use the full range (a 2 for dislike against someone else's timid 6) swings a blind average more than the timid rater's opinion, even if the two people disagree by an equal amount in the other direction. Coding theory backs the deeper point, entropy, the average surprise, is maximum when a distribution is uniform, so a grading scheme that mostly hands out the top two grades communicates less information than one that spreads scores across the full alphabet. Rank-in-class is one structural defense against this collapse, at the cost of guaranteeing someone finishes last even inside an unusually strong cohort.

Apply when: a scale's starting point or its actual usage pattern is being set or debated, and nobody has named the behavior that specific calibration will reward.

### 4. Rapid behavioral adaptation

"Any change in the rating system... is apt to not work out well unless you have thought through the response of the individuals to the change, they will certainly change their behavior." People do not wait years to adapt; they adapt almost immediately, and the adaptation runs toward the letter of the measure, not its spirit.

Hamming lived this as a running contest between himself, trying to optimize a shared computer's performance for the system as a whole, and its users, each optimizing their own individual use of it. Navy ships pass inspections one system at a time, in sequence, the skipper polishing whatever is currently up for review and neglecting the rest, so the reported readiness of the fleet is not its true readiness in an actual engagement. War games and business games get trained on idealized numbers instead of real ones, because, in Hamming's words, "we would not be believed if we used other data."

Apply when: a measure is about to be published or enforced and nobody has modeled how fast, or in which direction, the measured group will change its behavior.

### 5. Selection and inbreeding feedback loops

"The recruiting of one generation determines the organization's next generation." Evaluation criteria filter who enters a field and who rises inside it, often for reasons nobody consciously chose. Grades in early calculus and early programming reward the ability to carry out a lot of detail with high reliability, a trait that tends to run negatively correlated with the big-picture, whole-field thinking a discipline needs from its senior people later.

A personnel department screening for research talent tends to reject exactly the original, unconventional people research needs, because originality in the work correlates with originality in dress and behavior that reads as unhireable to a conventional screener. Self-selecting promotion boards pick successors who resemble themselves, producing a comfortable, harmonious, but increasingly inbred organization that innovates less with each generation. None of this shows up inside a single review cycle; it compounds across hiring and promotion cycles until the pipeline has quietly filtered out the people the next stage actually needs.

Apply when: hiring, admissions, grading, or promotion criteria are being set or reviewed, and the effect on who gets filtered out has not been examined.

### 6. Verification against ground truth

"All up and down the organization each person is bending things so they themselves will look good." Every level of a reporting chain has an incentive to make its own numbers look good, so leadership cannot treat reported figures as reality; it has to independently check.

Hamming, on a board of directors, would arrive a day early or stay a day late and simply walk the floor, into the supply crib to eyeball inventory against the reported count, out to the loading dock to see whether the machines marked "shipped" that quarter were actually there or scavenged back off the next batch the moment the quarter closed. Scheduled inspections get gamed on a fixed timetable; an inspector who arrives with less advance notice than the calendar allows gets a reading closer to the truth. The fix is not more paperwork, it is unscheduled, independent contact with the underlying reality.

Apply when: a decision will rely on a number that has passed up through more than one level of reporting, with no independent spot check planned.

## How to apply

Run this before adopting, changing, or defending any metric, rating, grade, KPI, quota, or incentive. Answer every question in writing. Do not skip ahead to the go/no-go call.

1. Write down the exact instrument: what gets counted, on what scale, computed how, reported to whom, and how often.
   - Vague instruments hide the audit; if you cannot write the computation down precisely, you cannot answer the next seven questions.
2. Name what a fully rational person, subject only to this exact instrument, would actually do to raise their score, not what you intend for them to do.
   - Assume the least charitable, most literal-minded response the instrument allows, not the good-faith response you are hoping for.
3. Ask whether this is the closest available measure to the real goal, or just the hardest-edged, easiest-to-defend proxy in the room.
   - Name the soft, more relevant alternative you are passing over, and why.
4. Locate the scale's anchor (where an average performer starts) and its dynamic range (whether raters actually use the extremes).
   - Name the specific behavior, risk-seeking, risk-averse, bunching at the middle, grade inflation, that this calibration rewards.
5. Estimate how fast behavior will adapt once the measure is known, and whether that adaptation will be visible to you or hidden behind an idealized report.
   - Assume days, not years, and assume the report you get may look like a ship polished for the one week it is due to be checked.
6. Ask who this measure will select for or against over repeated cycles, hiring rounds, promotion boards, admissions cycles.
   - Check whether that filter matches who the organization will need several cycles from now, not just today.
7. Ask how the reported number will be independently checked against reality.
   - Name specifically who will make an unscheduled, informal check rather than relying on the scheduled report alone.
8. Check whether a different instrument or scale, linear vs log, raw count vs percentage, absolute score vs rank, would show a materially different picture of the identical underlying reality.
   - If so, name which one is actually closer to what you want to know.

Final sanity check: say out loud, in one sentence, exactly what the measured group will do differently on day one after this metric goes live. If that sentence describes gaming the number while doing less of the actual goal, the metric fails the audit regardless of how accurate, cheap, or easy to compute it is.

Close the audit with:

- A **go/no-go** call.
- **Redesign moves** if the call is no-go or conditional: move the anchor, widen the enforced range, swap in a closer proxy, add an unscheduled independent check, change the underlying scale (log to linear, count to percentage), or pair the hard measure with a second, harder-to-game one.

**Worked example 1: lines-of-code bonus.** A team proposes paying engineers a bonus keyed to lines of code shipped per sprint, because it is easy to pull from source control.

- Instrument (question 1): a raw line count from source-control diffs, reported per engineer per sprint.
- Rational response (question 2): no incentive to delete a line, refactor toward brevity, or reuse an existing function; every incentive to leave excess code in place and add a few extra features if possible.
- Relevance (question 3): the real goal is working, maintainable software; a raw line count is the hardest-edged, easiest-to-pull proxy available, not the closest one. A review-approved diff quality or defect-rate measure sits nearer the actual goal.
- Calibration (question 4): not a rating-scale case, skip.
- Adaptation speed (question 5): immediate, engineers learn within one sprint that verbose code pays better than clean code.
- Selection effect (question 6): over several cycles this rewards engineers who write more code to solve the same problem, and quietly disadvantages engineers who solve it in fewer lines.
- Verification (question 7): none exists beyond the same line count being measured again.
- Instrument swap (question 8): a defect-rate or review-based instrument would show a materially different, and more relevant, picture.
- Decision: no-go on line count as the sole driver. Redesign: replace it with a defect-rate or review-approved-quality measure, and drop raw line count as a bonus input entirely.

**Worked example 2: manager rating scale anchored at 90.** A performance-review scale starts every manager at 90 out of 100, with room to move up or down from there.

- Instrument (question 1): a 0 to 100 annual score, anchored at 90, adjusted by a committee.
- Rational response (question 2): protect the 90 by avoiding visible risk; a failed bet costs more points than a safe non-decision costs.
- Relevance (question 3): the real goal is effective, adaptive management, not a defensible starting number; the anchor itself is the hard-edged, easy-to-administer choice.
- Calibration (question 4): a 90 start point rewards risk-aversion; nearly all the usable range sits below the anchor, so the only visible moves are downward.
- Adaptation speed (question 5): fast; managers learn within one review cycle that safe, low-variance choices protect the score better than ambitious ones.
- Selection effect (question 6): over several promotion cycles this filters for conservative managers, exactly when a later stage may need risk-tolerant leadership.
- Verification (question 7): scores are self-reported up through each manager's own chain, with no independent behavioral sample.
- Instrument swap (question 8): anchoring at 50, with real room to rise on demonstrated risk-taking, would reward a different and more relevant behavior.
- Decision: no-go on the 90 anchor as-is. Redesign: move the anchor to 50, and pair it with an unscheduled review of a small sample of actual decisions rather than relying on the self-reported score alone.

## Common failure modes

- **Treating the score as the reality.** IQ becomes "intelligence" by definition once a calibrated exam is built to define it; the normal distribution reported is an artifact of the calibration method, not evidence about the underlying trait.
  - Example: reporting a customer health score as if it were customer health, instead of a proxy the score was built to approximate.
  - Fix: ask what the instrument structurally cannot see before treating its output as fact.
- **Optimizing for measurability over relevance.** Grabbing the hard, firm, easy-to-defend number over the soft, harder-to-measure one that is actually closer to the goal.
  - Example: grading a final exam on training-style questions because they are easy to score, while the course's actual goal, education, goes unmeasured.
  - Fix: name the soft alternative explicitly in writing, and record why it was passed over.
- **Setting anchor or range with no model of the behavior it rewards.** Starting everyone at 95 percent, then being surprised that only conservative people rise to the top; letting raters bunch at the center, then being surprised that whoever is willing to use the extremes dominates the average.
  - Example: a 1 to 10 review scale where every score lands on 4, 5, or 6, so one extreme rater quietly controls the outcome.
  - Fix: work through question 4 of the audit before publishing any scale.
- **Assuming a new metric is neutral.** Publishing a measure does not just describe behavior, it changes it, usually within days, and always toward the metric's letter rather than its spirit.
  - Example: a support team learns within a week that closing tickets fast, rather than resolving them well, is what "tickets closed" actually rewards.
  - Fix: assume gaming starts on day one, and design the verification check before launch, not after the first complaint.
- **Trusting the reporting chain end to end.** Every level "bends things so they themselves will look good," so a number that has passed through several reporting layers is not the same thing as the truth on the ground.
  - Example: a quarter's reported shipments turn out to be machines scavenged back off the production line the moment the quarter closes.
  - Fix: build an unscheduled, independent check, the walk to the supply crib, the loading dock, the inspection with less notice than the calendar allows, into any process where a big decision will rely on a reported number.
- **Running years of unexamined selection criteria.** Grading or hiring criteria that reward one kind of mind quietly filter out the people a field or organization will need at a later stage, and the effect only becomes visible generations later.
  - Example: early calculus and programming grades reward detail-carrying reliability, a trait negatively correlated with the big-picture thinking the same field needs from its senior people.
  - Fix: periodically ask who a criterion is filtering out, not only who it is selecting for.

## References

- Richard W. Hamming, *The Art of Doing Science and Engineering, Learning to Learn* (Gordon and Breach, 1997), Chapter 29, "You Get What You Measure."
- Siblings in the Hamming carve: `hamming-unreliable-data` (auditing whether an already-reported number can be trusted before it drives a decision), `hamming-question-experts` (auditing an authority's impossibility claim before deferring to it). Cross-reference by name only; do not duplicate their content here.
- `kpi-dashboard-design` and `build-dashboard` own the presentation and layout of a metric once it has already been chosen. This skill governs the choice of the metric and its behavioral fallout, not how it is displayed.
- `analytics` owns post-hoc analysis of data already collected, answering what happened. This skill fires before adoption, on what will happen to behavior once a measure is known to exist.
- `behavioral-economics` owns the general catalog of individual cognitive biases (anchoring, framing, prospect theory) inside one person's private choices. This skill's mechanism is organizational, how a population of people collectively adapts, games, and gets selected by an installed measure over time.
- `kohavi-controlled-experiments` owns online experiment design and statistical validity for testing a change. This skill governs what goes into the scoreboard the experiment reads, not the experiment's methodology.
