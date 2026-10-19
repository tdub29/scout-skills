---
name: hamming-unreliable-data
description: "Trust audit on a reported number before acting"
---

# Hamming: The Unreliable-Data Trust Audit

## When to use

The moment: right before a reported number is allowed to drive a decision, a sign-off, a contract term, or a plan. Not after the decision is made, and not as a retrospective postmortem.

Hamming's framing of why this matters: "You need reliable data to make reliable decisions, but you will seldom have it with any reliability!" The audit exists to close the gap between how confident a number sounds and how confident you actually have grounds to be.

Trigger cues:

- A vendor, lab, or spec sheet states a precise accuracy or confidence figure ("99.99% uptime," "3-sigma reliability," "accurate to within 0.1%") and someone wants to bake it into an SLA, a contract term, or an engineering sign-off.
  - Example situation: a procurement lead asks whether to accept a vendor's tight uptime number as the SLA baseline.
- An economic or institutional statistic is revised or updated (GDP, inflation, unemployment, a poverty line, a trade or gold-flow figure) and someone wants to replan around the new number.
  - Example situation: a headline GDP print moves from 2.1% to 3.4% and a planning meeting is about to reset budgets around it.
- A survey, questionnaire, or poll result is being cited as if it represents a population, rather than the specific people who happened to answer.
- An average or mean is being quoted for a group you suspect is not actually homogeneous (income, family size, defect rates pooled across very different product lines).
- An automated system, sensor, or piece of equipment reports data about its own operation, and nobody has asked whether it can misreport itself.
  - Example situation: a monitoring dashboard reports its own five-nines uptime with no independent observer in the loop.
- A cost, budget, or sales estimate blends a carefully computed component with a rough guess, and the combined figure is quoted with a single confidence level.
- A dataset is about to be processed, aggregated, summarized, or fed into further analysis before anyone has looked at it for internal impossibilities.
- The user directly asks "can I trust this number," "how good is this data," "is this estimate solid," or "should we believe this."
- A definition behind a headline metric appears to have changed, or two sources report the same underlying quantity with materially different numbers.
- Someone proposes a large-scale data collection effort (a full census, a company-wide survey) when a smaller, carefully controlled sample might answer the same question more reliably.

Don't trigger for (explicit fence, route elsewhere):

- Scoping or running an enterprise data-quality program: dimensions, root-cause analysis, improvement projects, ongoing governance across systems. That is an organizational process sustained over time, not a one-off judgment call before a single decision. Route to `mcgilvray-data-quality-project`.
  - Contrast: "audit whether this vendor number is trustworthy right now" is this skill; "stand up a data-quality program across our systems" is not.
- Framing a modeling task, checking for leakage, or designing a target or label for a model you are building. Nothing is being modeled here; a number that already exists is being distrusted. Route to `provost-data-science-for-business`.
  - Contrast: "is this reported accuracy real" is this skill; "will this label leak information from the future" is not.
- Calibrating your own forward-looking probability judgments, scoring forecasts, or running postmortems on predictions you made. This audit distrusts an already-reported historical or measured figure; it does not calibrate a forecast about the future. Route to `tetlock-superforecasting`.
  - Contrast: "how much should I trust this already-reported figure" is this skill; "what probability should I assign to next quarter's outcome" is not.
- Diagnosing an individual decision-maker's own cognitive bias (anchoring, framing, prospect theory, loss aversion) in how they are choosing. This audit's mechanisms are institutional and instrumental data-reporting failures, not the chooser's own heuristics. Route to `behavioral-economics`.
  - Contrast: "why is this vendor's number wrong" is this skill; "why did I anchor on the first number I saw" is not.

## The framework

**Core thesis.** Data is, in Hamming's words, "generally much less accurate than it is advertised to be," across science, engineering, economics, and social science alike, for reasons that recur and can be checked for rather than shrugged off as bad luck. The instrument that produced a measurement is trusted without anyone asking whether the instrument itself is reliable. A reported low variance often reflects equipment tuned for consistency rather than a true picture of variability. Careful estimates get diluted by wild guesses while inheriting the careful estimate's apparent reliability. Definitions, incentives, and survey conditions quietly bias what gets reported. None of this is random noise; it is a short, learnable list of failure patterns. A decision-maker's job is to actively audit a number's provenance, not to accept its stated confidence at face value.

The eight checks below cover Hamming's chapter in full: instrument circularity, tuning-driven low variance, self-measuring machines, reliability contamination in combined estimates, definitional drift and incentive bias, survey distortion, averages versus medians for mixed groups, and pretesting paired with small careful samples and the gatherability gut-check. None of the eight substitutes for another; a number can pass one check and still fail the next.

### 1. Instrument circularity

Before trusting a measurement, ask whether the measuring or test equipment is itself known to be as reliable as the thing it is testing. Hamming's example: a department head trusted vacuum-tube life-test data because the test equipment carried "brass labels," not because anyone had validated the test equipment against something more reliable. A trusted-looking instrument is not the same thing as a validated one.

Ask directly: "Why do you believe the test equipment is as reliable as what is being tested?" If nobody in the room can answer that question with an actual validation story, the number is unaudited, regardless of how official the instrument looks.

Why it matters: a chain of trust that starts with an unvalidated instrument produces confident-looking numbers at every downstream step, and none of those downstream checks will catch the original gap.

### 2. The low-variance-tuning illusion

Experimenters routinely "fine tune the equipment ... by adjusting it so you get consistent runs," then hand the statistician artificially low-variance data. The statistician, working only from the numbers handed over, reports back exactly the high reliability the experimenter wanted to see in the first place.

This is the mechanism behind Hamming's rule of thumb on confidence limits: "90% of the time the next independent measurement will fall outside the previous 90% confidence limits!" A tight published confidence interval is itself a claim that needs auditing, not a stopping point for the analysis. Ask what the equipment or process was tuned for before the numbers were collected, and whether "consistent runs" was itself a design goal.

Why it matters: the statistician downstream of the tuning has no way to see it in the numbers alone, so a mathematically correct confidence interval can still describe the wrong thing.

### 3. The self-measuring-machine trap

A system that records data about its own operation is not automatically trustworthy just because it is automated. Hamming's example: central-office telephone equipment that both placed and billed calls, and that had logged connections to nonexistent offices, undetected, because nobody was independently checking the machine's account of itself.

Automation removes one kind of human error and quietly introduces its own. A machine can miscount, mislabel, or fabricate its own output with no human noticing, precisely because the usual check (an independent observer) is the thing that got removed when the process was automated. Ask what, if anything, checks this system's report against a source outside the system itself.

Why it matters: a self-measuring system's failure mode is silent by construction, there is no outside party positioned to notice the drift until something else breaks.

### 4. Reliability contamination when hard numbers meet guesses

When a precise, defensible estimate is merged with a rough, unvalidated guess, the combined figure inherits the precise component's apparent reliability in how it gets used and quoted. Hamming's example: careful engineering cost estimates combined with a salesman's guess at future sales volume, reported to a Board of Directors as a single number.

"Much of the reliability of the engineering guesses was transferred to the sum, and the uncertainty of the salesman's guesses was ignored." Hamming calls this "wide spread practice in many fields," not a rare lapse, precisely because it is so easy to miss: nobody lied, the precise part really is precise, but the composite is only as reliable as its weakest input. Ask which specific components of any combined number were actually measured carefully, and which were guessed, before accepting the composite's stated confidence.

Why it matters: refusing to combine hard numbers with guesses at all is not realistic in most organizations, so the useful move is naming the seam between them, not pretending the seam does not exist.

### 5. Definitional drift and incentive bias

Official figures shift meaning without notice, or are shaped by who benefits from the number landing on one side rather than the other. Hamming's examples: a poverty-line redefinition that changes who counts as poor without changing anyone's actual circumstances, GNP double-counting DuPont's GM stake, gold-flow figures differing two-to-one between the countries reporting the same flow, inventory reporting practices changed specifically to exploit new tax rules, and hidden discounts biasing cost figures differently during booms than during busts.

Ask whether the definition behind a metric has changed recently, whether two sources reporting "the same" quantity actually mean the same thing by it, and whether the party doing the reporting benefits from the number coming out high, low, or stable.

Why it matters: a definitional change can move a headline number as much as a real underlying shift, and the two are easy to conflate if nobody checks the fine print.

### 6. Survey and questionnaire distortion

Wording, question order, the presence of a rating or grading authority, and deadline pressure all change what people report, sometimes producing outright fabricated answers. Hamming cites the American Mathematical Society and Literary Digest cases, and the blunt instruction "send in what you can," which openly invites people to submit numbers they never actually measured.

Any survey-derived figure needs its collection conditions examined before it gets treated as a measurement rather than as a social artifact of how the question was asked. Ask who was asked, how the question was worded, whether a deadline or an authority figure was hovering over the response, and what incentive respondents had to answer accurately versus conveniently.

Why it matters: a survey number looks identical in a spreadsheet whether it was measured carefully or dashed off under deadline pressure, so the collection conditions have to be reconstructed by asking, not read off the result.

### 7. Averages versus the median for non-homogeneous groups

"Averages are meaningful for homogeneous groups... but for diverse groups averages are often meaningless." Hamming's classic tells: the average family with 2.3 children, and the grim joke about the average person having one breast and one testicle. An average silently assumes the population is one thing; when it is actually several distinct subpopulations mixed together, the average ends up describing nobody in particular.

Ask whether the group behind this average is genuinely homogeneous. If it is a mixture, prefer the median, or ask for the figure broken out by actual subclass, before treating the single average as informative.

Why it matters: an average computed correctly from a mixed population is not a wrong number, it is a number that answers a question nobody asked.

### 8. Pretest for outliers, then trust small careful samples over large sloppy ones

Never process a dataset before checking it for internal impossibilities. Hamming's example is a Western Electric inventory study that had negative-stock withdrawals sitting uncaught in the raw data until someone actually looked. "I have learned never to process any data until I had first examined it carefully for errors."

Related and just as load-bearing: "small samples carefully taken are better than large samples poorly done," both cheaper and more accurate than a sloppy full census or a rushed company-wide survey. And before trusting any figure at all, run the gatherability gut-check: ask yourself how anyone could actually have gathered this number accurately in the first place. Hamming's examples are an "adultery per year" statistic nobody could have measured directly, and a coin-flip method built specifically to survey something respondents would otherwise lie about. If no plausible collection mechanism comes to mind, the number is suspect no matter how confidently it is reported.

## How to apply

Run this as a standing checklist on any reported number before it is allowed to drive a decision. Work through the questions in order. Do not skip ahead to the rating before answering them.

1. Identify what measured or produced this number, and ask directly whether that instrument, system, or process is itself known to be reliable, independent of the claim it is now producing.
   - If nobody can point to a validation event separate from the claim itself, mark this question unanswered, not passed.
2. Ask whether the reported precision came from tuning the setup for consistent runs rather than from capturing the quantity's true variability.
   - Treat an unusually tight confidence interval as a claim to be tested, not as a fact already established.
3. If the number comes from an automated or self-reporting system, ask whether that system could be miscounting, misclassifying, or fabricating its own output without anyone noticing.
   - Look specifically for an independent cross-check outside the system that produced the number.
4. Check whether this is a composite of a carefully measured component and a rough guess.
   - If so, name which part is which in your notes, and do not let the composite inherit the careful part's confidence level.
5. Ask whether the definition behind this metric has changed recently, differs between the parties reporting it, or is shaped by an incentive on the part of whoever produced it.
   - Compare the current definition against how the same metric was defined a year or a reporting cycle ago.
6. If the number is survey- or questionnaire-derived, ask what wording, ordering, authority figure, or deadline pressure shaped the responses, and whether respondents could plausibly have fabricated an answer to comply.
   - Ask specifically who declined to respond, and whether the non-responders differ systematically from the responders.
7. Ask whether an average is being quoted for a population that is actually a mixture of distinct subgroups.
   - If so, ask for the median, or for the number broken out by subgroup, before using the average.
8. Ask whether the raw data has been checked for internal consistency and outliers yet.
   - If it has not been pretested, stop and do not process it further until it has.
9. Ask whether a small, carefully designed sample would have produced a more trustworthy figure than the large, loosely controlled collection that actually produced this one.
   - Weigh the cost of collecting the large sample against what a smaller, better-controlled one would have cost, not just against doing nothing.
10. Run the gatherability gut-check: picture the actual mechanism by which this number could have been collected accurately.
    - If no plausible mechanism comes to mind, treat the number as unproven regardless of its stated precision.

Final sanity check: state out loud, in one sentence, why you believe this number is as accurate as claimed. If that sentence leans on the source's authority, brand, or the fact that it was automated, rather than on an answer to one of the ten questions above, the number has not actually been audited yet.

Close the audit by producing:

- A **trust rating**: high, medium, or low, with the specific question(s) above that drove the rating.
- A **recommendation**: discount the stated accuracy and use a wider margin, request the raw data or an independent remeasurement, or explicitly flag the residual uncertainty in the decision record rather than passing the number through silently.

**Worked example 1: vendor SLA.** A vendor's SLA proposal states "99.99% uptime, tight confidence interval." Run the checklist: (1) the uptime monitor is the vendor's own tool, no independent validation offered, unanswered; (2) the tight interval may reflect a monitoring window tuned to exclude scheduled maintenance, unanswered; (3) the figure is self-reported by the vendor's own infrastructure, self-measuring-machine trap applies; (4) not a blended estimate, not applicable; (5) "uptime" may be defined to exclude certain outage classes, ask for the definition in writing; (8) no raw incident log has been reviewed yet, pretest required; (10) a precise four-nines figure for a system you have never independently observed is hard to picture as gathered rather than asserted. Rating: low. Recommendation: request the raw incident log and the monitoring definition before signing the SLA at face value, and write the residual uncertainty into the contract's remedy clause rather than into the headline number.

**Worked example 2: revised economic figure.** A GDP print is revised from 2.1% to 3.4% and a planning meeting wants to reset budget targets around the new number. Run the checklist: (1) the instrument here is a national statistical agency's estimation methodology, not a single sensor, so ask what changed in the methodology between the two prints, not just what changed in the economy; (5) definitional drift is the leading suspect, ask whether the revision reflects a component reclassification (a GNP-style double-count, a change in what counts as investment versus consumption) rather than new underlying activity; (7) a national aggregate is itself an average across a wildly non-homogeneous economy, ask which sectors actually drove the revision instead of replanning off the headline number alone; (10) picture how a 1.3-point swing could have been gathered accurately in the time between prints, and treat a swing that large as a signal to read the methodology note before acting. Rating: medium. Recommendation: flag the residual uncertainty in the planning document, replan off a range rather than the point estimate, and revisit once the next revision confirms or reverses the move.

## Common failure modes

- **Trusting brass labels.** Accepting a claimed accuracy because the instrument carries vendor documentation, a certification, or a trusted brand name, without ever asking whether that instrument was validated against something more reliable than itself.
  - Example: signing off on a part because "the lab said so," with no question asked about the lab's own calibration history.
  - Fix: ask for the instrument's own validation record before accepting what it reports.
- **Trusting a machine because it is a machine.** Treating a system's self-reported data about its own operation as automatically correct. "You cannot even trust a machine to gather data about itself correctly."
  - Example: accepting a server's self-reported uptime log with no independent monitoring cross-check.
  - Fix: require at least one data point from outside the self-reporting system before trusting its account of itself.
- **Letting one precise number launder the whole decision.** Allowing a single defensible, carefully computed component (an engineering estimate) to carry its reliability over onto a composite figure that also depends on undefended guesses.
  - Example: a project budget that is "accurate" only because the materials line item was costed carefully, while the labor and timeline guesses next to it were never examined.
  - Fix: report the composite as a range driven by its weakest input, not as a single number driven by its strongest one.
- **Quoting an average for a population you already suspect is mixed.** Using a single mean to describe a "collection of quite different subclasses" instead of breaking it apart or using the median.
  - Example: reporting "average customer lifetime value" across free-tier and enterprise customers as if they were one population.
  - Fix: split the figure by the actual subclass, or lead with the median, before it goes into a decision.
- **Processing before pretesting.** Running analysis, aggregation, or a model on a dataset before checking it for internal impossibilities, on the theory that there is no time, when "no matter how sacred the data and urgent the answer" the check has to come first.
  - Example: computing summary statistics on an inventory table that contains negative stock withdrawals nobody has flagged.
  - Fix: run a pass for internal impossibilities and outliers before any aggregation, no matter the deadline.
- **Confusing a tight confidence interval with a validated one.** Treating a small stated error bar as evidence of accuracy rather than as a claim that may reflect tuning for consistent runs, per Hamming's rule that repeat measurements routinely fall outside the previous "90% confidence" limits.
  - Example: baking a vendor's narrow SLA interval directly into a contract remedy clause with no independent remeasurement.
  - Fix: treat the stated interval as a hypothesis to test with one independent remeasurement, not as a settled fact.

## References

- Richard W. Hamming, *The Art of Doing Science and Engineering: Learning to Learn* (Gordon and Breach, 1997), Chapter 27, "Unreliable Data."
- Siblings in the Hamming carve: `hamming-you-get-what-you-measure`, `hamming-question-experts`. Cross-reference by name only; do not duplicate their content here.
- `mcgilvray-data-quality-project` owns enterprise data-quality governance programs (dimensions, root-cause remediation, ongoing improvement projects). This skill is a one-off judgment call an individual makes before a single decision, not an organizational program sustained over time.
- `provost-data-science-for-business` owns problem-to-mining-task framing, expected value, leakage audits, and label design for a model being built. This skill fires on trusting a number already reported to you, not on framing a modeling task.
- `tetlock-superforecasting` owns calibration of the decision-maker's own forward-looking probability judgments and forecast scorekeeping. This skill audits the trustworthiness of an already-reported historical or measured figure, not the accuracy of your own forecast.
- `behavioral-economics` owns the general catalog of individual cognitive biases (anchoring, framing, prospect theory). This skill's mechanisms are institutional and instrumental data-reporting failures (instrument circularity, tuning, definitional drift, incentive bias, survey distortion), not the chooser's own heuristics.
