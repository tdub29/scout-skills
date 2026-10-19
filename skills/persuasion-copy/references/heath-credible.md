# Heath: Credible

## When to use

Trigger when the question is "the claim is true but the audience doesn't believe it." Concrete cues:

- A pitch / proposal / claim is being received with skepticism that the user thinks is unwarranted
- A statistic the user thinks is striking but the audience treats as noise
- A competitive comparison where the user IS measurably better but the comparison doesn't land
- A technical or scientific claim that a lay audience doesn't trust on authority
- A startup / underdog has to prove competence to an audience that defaults to skepticism
- "How do I make this credible without sounding defensive / arrogant / overclaiming"
- A claim that requires the audience to act, and the audience is hesitating because they don't believe the claim
- A safety statistic, financial number, or risk assessment that the audience needs to internalize, not just nod at

Don't trigger for: pure source-citation work (use `hopkins-scientific-claim-check` â€” that skill focuses on backing claims with verifiable sources; this skill focuses on the credibility-engineering moves once you have the substantive case), generic prose editing (`copy-editing`), or commercial conversion (`cro`). This skill operates at the *believability* layer â€” making true claims feel true to a skeptical audience.

## The framework

### Core thesis

Heath's claim: credibility doesn't come from authority alone. Authority is passive trust ("she has a PhD, she must be right"). Modern audiences are skeptical of authority by default. The reliable moves are *active*: structures that let the audience verify the claim themselves, or that compress the broader competence into one definitive case the audience can grasp.

Heath identifies three sub-techniques that work across contexts. They share trigger surface â€” "make this claim credible" â€” and operate as a single skill, not three separate ones, because a single credibility problem usually calls for one or two of the three depending on the type of claim.

### Sub-technique 1: The Sinatra Test

**Premise.** "If I can make it there, I'll make it anywhere." Rather than proving competence broadly, identify one case where success was so hard / so visible / so on-the-skeptic's-turf that winning there implicitly proves competence across the whole domain.

**Heath's canonical example:** Safexpress, an Indian logistics startup competing against UPS. Safexpress claimed they could outperform UPS on reliability. UPS scoffed. Safexpress's move: deliver a critical shipment in UPS's own service area, on a deadline UPS couldn't meet. They did. The Sinatra-test win in UPS's backyard proved competence everywhere else by implication â€” "if we can beat UPS on UPS's home turf, of course we can do simpler routes elsewhere."

**The structure.** The Sinatra-test case has to be:
1. **On the skeptic's turf.** The case should test the claim in conditions the audience considers hardest. Winning in easy conditions doesn't transfer; winning in hard conditions does.
2. **Measurable and objective.** "We outperformed UPS" needs a number: delivery time, cost, reliability rate. Subjective wins don't transfer credibility.
3. **Counterintuitive.** The audience expected the user to lose this specific case. Their surprise at the win is the transfer mechanism.

**When to use:** comparative claims, underdog positioning, claims about capabilities that the audience doubts.

### Sub-technique 2: Sticky Statistics

**Premise.** Raw numbers don't stick. "1 in 10,000 chance of being killed by a shark" is abstract â€” it sits in analytical mode and doesn't trigger gut understanding. The reframe: anchor the statistic to a human-scale comparison that *does* trigger gut understanding.

**Heath's example:** "You're more likely to be killed by a vending machine than a shark." The statistic itself is unchanged; the comparison changes how it's processed. The audience now has an intuitive grip on the magnitude.

**The structure.** Sticky-statistic moves:
1. **Human-scale denominator.** "1 in 10,000" â†’ "in a stadium of 50,000, only 5 people." The denominator should be something the audience can picture as a population.
2. **Surprising comparison.** Compare to a thing the audience considers very different â€” sharks vs. vending machines, lottery odds vs. lightning strikes, COVID fatality rates vs. driving fatality rates. The unexpected pairing creates the stick.
3. **Mathematical fidelity.** The reframe must preserve the actual ratio. Manipulating the denominator to create a misleading impression is statistical malpractice.

**When to use:** statistics in risk communication, financial claims, scientific findings, public health, fundraising metrics, audience-impact numbers.

### Sub-technique 3: Testable Credentials

**Premise.** The strongest credibility is *internal* â€” credibility the audience produces for themselves by verifying the claim. External credentials ("trust me, I'm an authority") work only as far as the audience trusts the authority. Internal credentials (testable claims, demos, live verification) bypass the trust question entirely.

**Heath's canonical example:** Wendy's "Where's the beef?" The campaign claimed Wendy's burgers had more meat than competitors. The ad invited diners to literally lift the bun and check. Audiences didn't have to trust Wendy's; they could verify. The move worked because the claim was true and verifying was easy.

**The structure.** Testable credentials require:
1. **A claim that's actually true.** Testable credentials backfire spectacularly if the claim fails the test.
2. **A verification mechanism the audience can use.** "Lift the bun." "Visit our office." "Run this query." "Try the demo for 30 days." "Read the source code." "Check the public records."
3. **Low friction to verify.** If the verification requires expert knowledge or a lot of work, the audience won't do it, and the testable credential degrades to a regular authority claim.

**When to use:** claims that competitors are likely making too (verification breaks ties); claims where the user's reputation is unknown or contested; technical claims to non-technical audiences.

### Which sub-technique when

- **Sinatra test:** comparative claims, underdog positioning, "we're better than [established player]"
- **Sticky statistics:** numerical claims that need to be internalized, not just noted
- **Testable credentials:** any claim where the audience could plausibly verify, and where the user is confident the verification will go their way

Most credibility problems benefit from one or two of these. Stacking all three risks looking like a sales pitch.

### Manipulation risk

Each sub-technique can be weaponized:

- **Sinatra test misuse.** Picking a single case that's exceptional rather than representative. "We delivered for one Fortune 500 client" â†’ audience assumes we deliver for all clients. If the case is unrepresentative, disclose it. Don't let one win imply a competence the user doesn't actually have at scale.
- **Statistical manipulation.** Sticky statistics are easy to twist. Cherry-picking denominators, comparing across non-comparable categories, omitting confounding variables. The reframe must preserve actual mathematical fidelity, not just rhetorical punch.
- **Rigged tests.** A "testable credential" where the verification mechanism is designed to always confirm. The audience eventually catches on, and trust collapses harder than if no test had been offered. The verification must be capable of disconfirming.
- **Concealing unfavorable comparisons.** Using sticky statistics for the favorable comparison ("we're 10Ã— faster than X") while staying abstract about the unfavorable one ("our reliability is in line with industry standards"). Be sticky on both sides or admit you're not going to be on either.

The honest version: the case is representative or labeled as not, the statistical reframe preserves math, and the test could honestly fail.

## How to apply (step-by-step)

1. **Diagnose the credibility problem.** What specifically is the audience doubting? The user's capability? A specific number? A comparison? Be precise â€” different credibility problems need different sub-techniques.

2. **Pick the sub-technique that fits the claim type.**
   - Comparative / capability claim â†’ Sinatra test
   - Numerical claim â†’ Sticky statistics
   - Verifiable factual claim â†’ Testable credentials
   - (Multiple sub-techniques are fine if the credibility problem has multiple layers.)

3. **For Sinatra test:**
   - Identify the audience's hardest expected case ("the toughest test you could imagine us facing")
   - Find or create a case where the user won that specific test
   - Verify it's measurable and objective (numbers, not feelings)
   - Verify it's representative or label it as exceptional

4. **For Sticky statistics:**
   - Identify the abstract number that isn't landing
   - Convert to a human-scale denominator the audience can picture
   - Pair with a surprising comparison from a different domain
   - Run the math: is the comparison actually mathematically fair?
   - Add the context the audience needs (last year's number, base rate, confidence interval) so the sticky version isn't misleadingly precise

5. **For Testable credentials:**
   - Identify what the audience could verify
   - Design a verification mechanism with low friction (a demo, a public record, an open-source repo, a trial period, a published metric)
   - Stress-test the verification: could it disconfirm? If not, redesign â€” a rigged test is worse than no test
   - Make the verification easy to take action on (one click, one phone call, one observable behavior)

6. **Run the manipulation-risk check.**
   - Is the Sinatra-test case representative of typical performance, or exceptional?
   - Does the sticky-statistic reframe preserve mathematical fidelity?
   - Could the testable credential honestly fail?
   - Are you being sticky/specific on favorable claims and abstract on unfavorable ones?

7. **Produce the credibility plan.** A three-section document: (a) the credibility problem diagnosed in one sentence; (b) the chosen sub-technique(s) with the specific Sinatra case / statistic reframe / verification mechanism; (c) the manipulation-risk audit showing the plan survives honest scrutiny.

8. **Sanity-check by reading aloud.** "Here's what we claim. Here's why you should believe it. You can check by [verification]." If any part of that sentence feels overstated, scale back.

## Common failure modes

- **Authority signaling without backing.** "I have 20 years of experience" used as a credibility move without any of the three sub-techniques. Audiences increasingly discount authority-only claims. Add a Sinatra case, a sticky statistic, or a testable credential.

- **Cherry-picked Sinatra cases.** A single exceptional win used to imply ongoing competence. Audiences eventually encounter the typical case and feel deceived. The fix: either pick a representative win, or disclose that the example is your best case.

- **Statistical sleight-of-hand.** "Our customers see 10Ã— improvement" â€” true for the customer who improved the most, false for the typical customer. The sticky-statistic frame must reflect the typical case, not the outlier.

- **Rigged tests.** Demos that always go perfectly; trials that quietly downgrade if the user tries to leave; "verification mechanisms" that can't actually disconfirm. The credibility loss when the rigging is discovered is larger than the credibility gain from the test in the first place.

- **Three-sub-technique stacking when one would do.** Using Sinatra + sticky stats + testable credentials for a low-stakes claim makes the user look defensive ("doth protest too much"). Match the credibility-firepower to the actual skepticism.

- **Forgetting the truth-preservation check.** Every credibility move depends on the underlying claim being true. The credibility moves *transmit* truth more effectively; they don't *manufacture* truth. If the claim is false, no amount of Sinatra-testing will save it long-term.

- **Stickiness on the favorable side only.** "We're 10Ã— faster than X" (sticky comparison) / "Our pricing is competitive" (abstract). Audiences notice asymmetry. If you're going to be sticky on one side, be sticky on the other.

- **Confusing this skill with `hopkins-scientific-claim-check`.** Hopkins focuses on whether claims are backed by verifiable specific evidence (drug X tested on Y subjects with Z outcome). Heath-credible focuses on how to *deliver* a credible claim to a skeptical audience. Compose: Hopkins ensures the claim is rigorously backed; Heath ensures the rigorous backing is communicated stickily.

- **Treating credibility as a one-time fix.** Credibility is built (and lost) across many touchpoints. A single credible moment can fail to compensate for a track record of overclaiming. The skill works at the message level; the broader credibility battle is fought at the relationship level.

- **Skipping the manipulation-risk check because "it's just marketing."** Audiences detect manipulation faster than ever. The propaganda version of credibility moves backfires within one cycle. Honest credibility-engineering is also long-term-sustainable credibility.

## References

- Chip Heath and Dan Heath, *Made to Stick* (Random House, 2007), Chapter 4 â€” Credible. The Sinatra Test / Safexpress vs. UPS passage; the sharks-vs-vending-machines statistic; the Wendy's "Where's the beef?" testable-credential example.

- Sibling carved Heath skills:
  - `heath-curse-of-knowledge` â€” the curse often manifests as the expert assuming the audience trusts them; credibility moves work against this assumption
  - `heath-finding-the-core` â€” credibility moves are most effective when applied to the singular core claim, not to every supporting point
  - `heath-concrete` â€” the sticky-statistic and testable-credential moves are concrete by construction; the concreteness skill is the foundation
  - `heath-unexpected`, `heath-emotional`, `heath-stories` â€” credibility composes with all of them

- Related skills:
  - `hopkins-scientific-claim-check` â€” orthogonal sibling: that skill verifies the claim is backed; this skill delivers the backed claim credibly
  - `aristotle-three-modes-of-persuasion` â€” credibility is the ethos mode of Aristotle's framework; this skill is the operational layer
  - `marketing-psychology` â€” touches social proof and authority biases; this skill is the actionable structural moves underneath
