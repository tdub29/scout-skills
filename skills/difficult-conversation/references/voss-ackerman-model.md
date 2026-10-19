---
name: voss-ackerman-model
description: Apply Chris Voss's ACKERMAN MODEL from *Never Split the Difference* (HarperBusiness, 2016, Ch 9) â€” a specific algorithmic bargaining procedure developed by Mike Ackerman (former CIA, founder of Ackerman Group) and Howard Raiffa (Harvard), used by the FBI for hostage ransom negotiation and adapted by Voss for business / real estate / salary / vehicle negotiations. The four-step algorithm: (1) Set your target price (your true goal); (2) Set your first offer at 65% of target (extreme low anchor); (3) Calculate three raises at diminishing increments â€” 85%, 95%, 100% of target; (4) Use empathy + ways to say "No" + calibrated questions between each raise to make the counterpart counter before you raise. Plus two finishing moves: precise non-round final numbers ($37,893 not $38,000 â€” signals deliberate calculation, not arbitrary positioning), and a small non-monetary concession at the final number to signal you've hit your limit. The model wins by exploiting reciprocity (each diminishing raise reads as "I'm giving you more even though it's harder for me"), anchoring (the 65% anchor reshapes the entire negotiation range), and ego (the counterpart feels they "won" by extracting concessions). Use whenever a user is about to enter a PRICE negotiation â€” salary, vendor contract, home purchase, freelance rate, car, equipment, settlement â€” and asks "how do I bargain hard," "what's my opening offer," "how do I avoid splitting the difference," "I always end up meeting in the middle and losing â€” what should I do," or "how do I anchor without seeming insulting." Also trigger for "Ackerman model," "Ackerman bargaining," "65/85/95/100," "haggling algorithm," "negotiation pricing," "anchor low," "precise non-round numbers," or "FBI ransom negotiation." Output is an Ackerman plan: target / first offer (65%) / second (85%) / third (95%) / fourth (100% with precise number) + the empathy + No-saying + calibrated questions between each raise + the small non-monetary item to throw in at the final number + manipulation-risk gate. Do NOT trigger for relationship-based negotiations where price is secondary, low-stakes haggling where the algorithm is overkill, or non-price negotiations (interpersonal conflict, schedule, scope) â€” this is the price-specific algorithm.
---

# Voss: The Ackerman Model

## When to use

Trigger when the user has a PRICE to negotiate and the negotiation is adversarial enough that walking-away pricing matters. Concrete cues:

- Salary negotiation â€” new job, raise, promotion
- Buying a car, house, or major equipment
- Negotiating with a vendor / supplier on a contract
- Quoting a freelance / consulting rate
- Settling a dispute that comes down to a dollar figure
- The user is about to "split the difference" and senses they're losing money to politeness
- "What should my opening offer be?"
- "How low can I anchor without seeming insulting?"
- "I always end up at the midpoint â€” how do I get more?"
- A vendor or competitor has anchored their price and the user wants to counter

Don't trigger for: relationship-based negotiations where price is secondary, casual haggling at the farmer's market (the algorithm is overkill), non-price negotiations (use `voss-calibrated-questions` and `voss-no-framework` for those), or contexts where preserving the relationship matters more than the dollar figure (the Ackerman model is bargaining-hard territory â€” it works against counterparts who expect adversarial price negotiation; deploying it in a collaborative context damages trust).

## The framework

### Core thesis

The conventional bargaining failure mode: both parties "meet in the middle" or "split the difference." Voss (citing Mike Ackerman) calls this lazy and predictable, and shows that it consistently produces *worse* deals for the more competent negotiator than the algorithmic alternative. The Ackerman model is the specific algorithm Voss endorses â€” developed at the Ackerman Group for kidnapping ransom negotiations, validated by Howard Raiffa at Harvard, and adapted for business.

The mechanism: the algorithm exploits three psychological effects simultaneously â€” **anchoring** (the first offer reshapes the entire range), **reciprocity** (each diminishing raise reads as "I'm giving you more even though it's harder for me," triggering the counterpart's obligation to make a concession in return), and **ego** (the counterpart feels they're winning by extracting concessions, even when the final price is at the user's target).

The user reaches their target price by *appearing to fight against giving it*. The counterpart feels they've succeeded by extracting concessions; the user has actually gotten what they wanted.

### The four-step algorithm

**Step 1: Set your target price.** Your actual goal. The number you'd be genuinely satisfied with. Not your "stretch" number or your "minimum acceptable" â€” your *target*. This number is private; you never say it.

**Step 2: First offer at 65% of target.** This is the extreme anchor. For a target of $100, you open at $65. For a salary target of $120K, you open at $78K (if buying) or $156K (if selling labor â€” invert the percentages for which side you're on).

The 65% feels uncomfortably aggressive. That's the point. It anchors the negotiation in a range far below where you'll end. The counterpart's mental model of "what this could cost" shifts toward your number.

**Step 3: Three diminishing raises â€” 85%, 95%, 100%.**

| Round | % of target | Increment from previous |
|---|---|---|
| 1 (open) | 65% | â€” |
| 2 | 85% | +20 percentage points |
| 3 | 95% | +10 percentage points |
| 4 (final) | 100% | +5 percentage points |

The diminishing increments are critical. The first raise is large (+20pp); the second is half (+10pp); the third is half again (+5pp). The pattern signals to the counterpart: "I'm running out of room. Each step is harder for me to give." Reciprocity kicks in â€” they feel they've extracted everything you can give.

**Step 4: Empathy + "No" + calibrated questions between each raise.** This is where most practitioners fail. The algorithm doesn't say "make four offers in a row." Between each raise, the user must:

- Use empathy / labeling (route to `voss-labeling`): "It seems like the price is making this hard for you to commit."
- Use calibrated questions (route to `voss-calibrated-questions`): "How am I supposed to do that?" "What about this isn't working?"
- Use ways to say "No" without saying the word (route to `voss-no-framework`): "Your offer is very generous, but I'm afraid that won't work for me."
- Wait for the counterpart to *counter* before raising â€” if you raise without their counter, you've negotiated against yourself and given up the reciprocity advantage.

**Each raise should feel earned by the counterpart, not given by you.**

### The two finishing moves

**Move 1: Precise non-round numbers.** At the final (100%) offer, use a precise number that doesn't end in zeros or fives. Not $100,000 â€” $98,743. Not $50,000 â€” $51,257. Not $200 â€” $187.

The mechanism: round numbers feel arbitrary ("you just pulled that out of nowhere"). Precise numbers feel calculated ("they actually worked out the math to get to this number"). The counterpart reads precision as evidence that you've considered the offer carefully and can't move further.

This is the same psychological pattern that makes "$9.99" feel meaningfully cheaper than "$10" â€” except deployed at the higher-stakes scale of negotiation, where the precision signals "I'm at my real limit, not just rounding."

**Move 2: Throw in a small non-monetary item at the final number.** "I can't move the price â€” but I can include the warranty extension" / "but I can throw in installation" / "but I can adjust the payment terms." The throw-in must be:

- Genuinely small from your side (you weren't going to charge for it anyway, or it costs you near-zero)
- Visible / valuable from their side (they'd actually like having it)
- Used ONLY at the final number, as a signal that you've hit your floor

The throw-in does two jobs: it gives the counterpart one more "win" to feel they've extracted maximum value, and it makes the final number feel locked. After a throw-in, raising further would signal weakness.

### Why this beats "split the difference"

Splitting the difference is the path of least resistance. Both parties feel they've been fair; the average of opening positions becomes the deal. Voss's diagnostic: if the opening positions weren't *strategically calibrated* in the first place, splitting the difference rewards the party who opened more extremely.

Conventional negotiator: opens reasonably ($95 against target of $100); counterpart anchors high ($120); both split the difference at $107.50. User loses $7.50 against target.

Ackerman negotiator: opens at $65; counterpart anchors at $120; user raises through 85/95/100 with empathy and questions; lands at $100. User hits target exactly.

The discomfort of the 65% opening is the price of avoiding the splitting-the-difference trap.

### When the Ackerman model doesn't fit

The algorithm assumes:
- The negotiation is genuinely about price
- Both parties expect adversarial price-bargaining
- The relationship can survive (or doesn't matter beyond) hard bargaining
- The user has time to run the 4-round protocol (it can't be done in 30 seconds)

Don't deploy when:
- Price is secondary to relationship (collaborative vendor partnerships, family transactions)
- The counterpart is naive and an aggressive 65% anchor will damage rather than calibrate
- The negotiation is fundamentally about something other than dollars (scope, time, autonomy)
- You only have one chance to make an offer (the model requires iterative back-and-forth)

### Manipulation risk

The Ackerman model is *aggressive* bargaining. It works by triggering psychological mechanisms (anchoring, reciprocity, ego) in the counterpart. The ethical position:

1. **Consent.** The counterpart should expect adversarial price-bargaining. Deploying the model on someone who came in expecting collaborative negotiation (a family member, a friend, an unsophisticated counterparty) is a betrayal of the implicit relationship contract.
2. **Truth.** The target price you set should be your honest target â€” not a sandbagged number where "hitting target" means extracting maximum from the counterpart. The throw-in at the end should be a genuine small concession, not theater.
3. **Beneficiary.** If you hit target via the model, is the deal one the counterpart can live with? Or are you using algorithmic precision to extract a price they'll later regret? The model works ethically when both parties can live with the result; it manipulates when it produces a deal one side will eventually unwind.

The Ackerman model is the most overtly tactical Voss technique â€” and the one most often deployed against counterparties who aren't using the same tools. Use with calibration to context.

## How to apply (step-by-step)

1. **Confirm this is a price negotiation that warrants the model.** Adversarial expectations? Iterative back-and-forth available? Price is the dominant variable? If yes, proceed.

2. **Set your target price.** Honest target â€” what would actually satisfy you. Write it down privately. Don't share.

3. **Calculate the four offers:**
   - Open: 65% of target
   - Second: 85% of target
   - Third: 95% of target
   - Final: 100% of target, expressed as a precise non-round number

   (If you're the seller, invert: 135%/115%/105%/100%.)

4. **Identify the throw-in for the final number.** Something genuinely small from your side, visible from theirs. Warranty, accessory, flexibility on terms, etc.

5. **Compose the labels and calibrated questions for between rounds.**
   - For when they reject your opening: a label ("It seems like the price is challenging") + a calibrated question ("How would you suggest we structure this?")
   - For when they make a counter that's far from yours: another label + "How am I supposed to do that?"
   - For when they're pressing you to raise faster: empathy ("I hear you") + a way to say No ("I'm afraid that won't work for me yet")

6. **Open with the 65% offer.** Calmly. Don't apologize or explain. State the number. Let it land. The counterpart will likely react negatively â€” that's expected.

7. **Wait for them to counter before raising.** If they don't counter and just stonewall, deploy empathy + calibrated questions to draw them into engagement. Do NOT raise without a counter â€” that's negotiating against yourself.

8. **Raise to 85%.** Verbally frame this as "I can get to X" â€” implying effort, not generosity. Wait for their counter.

9. **Raise to 95%.** Smaller increment; signal strain. "I'm pushing my limits, but I can move to Y."

10. **Raise to 100% with the precise number.** "After running the numbers carefully, I can do $98,743." Pause.

11. **Deploy the throw-in.** "I can't move on the price â€” but I can include X." Watch for the counterpart's relief / win signal.

12. **Close.** They accept; deal locked at your target. Or they push for more; you have a decision: hold firm (most often), walk away (sometimes), or revise target (rarely â€” only if their counter reveals new information).

13. **Run the manipulation-risk gate.**
    - Was the counterpart expecting adversarial bargaining?
    - Was the target honest?
    - Can both sides live with the deal?

14. **Produce the Ackerman plan** (artifact):
    - Target
    - Four-offer ladder with precise final number
    - Throw-in
    - Labels + calibrated questions for between rounds
    - The manipulation-risk audit

## Common failure modes

- **Raising without a counter from the counterpart.** The single most common failure. The user opens at 65%, the counterpart doesn't counter, the user gets nervous and offers 85% to "show goodwill." Disaster â€” the user has just negotiated against themselves and lost reciprocity advantage. Wait for the counter, no matter how long it takes. Empathy and calibrated questions are your tools while waiting.

- **Equal-increment raises.** Some practitioners hear "four offers" and ladder them evenly (65 â†’ 75 â†’ 90 â†’ 100). The diminishing pattern (65 â†’ 85 â†’ 95 â†’ 100) is what triggers reciprocity. Equal increments feel arbitrary.

- **Round-number final.** "I can do $100,000" loses to "I can do $98,743." The precision signals real calculation, not bluff. Always use a precise non-round final number.

- **Throw-in that's actually expensive for you.** Defeats the purpose. The throw-in should be near-zero cost to you, real value to them. If you're tossing in something that meaningfully impacts your bottom line, you're not at your floor.

- **65% opening that's so low the counterpart walks.** Calibrate to context. In some contexts (real estate in tight markets, salary in a hot field), 65% might be insulting enough to break the deal entirely. Test with the empathy-and-question protocol â€” if the opening produces shutdown rather than counter, you may need to recalibrate to 70% or 75%.

- **Deploying on a relationship-based counterpart.** A family member, a long-term collaborator, a vendor you want to keep close â€” running Ackerman on them damages the relationship. The model is for adversarial price bargaining; for relationship contexts, use empathy + collaborative pricing.

- **Forgetting empathy and calibrated questions between rounds.** The algorithm without the relational glue feels mechanical and hostile. The counterpart should feel heard between rounds, even as the user holds the line. Empathy + No-saying + calibrated questions are non-optional.

- **Treating the target as the minimum.** The target is the honest goal. If you set it artificially low to "easily exceed" it, you're sandbagging and the algorithm's psychology breaks down.

- **Using rounding for the final number.** $99,999 reads as gimmicky. $98,743 reads as calculated. The precision signals consideration; round-ish numbers signal anchoring.

- **Skipping the throw-in.** The throw-in is what locks the final number. Without it, you've just stated a number and waited; the counterpart may push for more. With it, the counterpart has a "win" and the deal closes.

- **Skipping the manipulation-risk gate.** The model can extract advantage from naive counterparties. Calibrate to context â€” if the counterparty isn't sophisticated, the result may be a deal they regret. That's manipulation, not negotiation.

## References

- Chris Voss and Tahl Raz, *Never Split the Difference: Negotiating As If Your Life Depended On It* (HarperBusiness, 2016), Chapter 9 â€” "Bargain Hard." The Ackerman algorithm is laid out at lines 6724â€“6734 of the extracted text. The Mishary rent case (worked example) at lines 6809â€“6894. Mike Ackerman's bio and Harvard endorsement (Howard Raiffa) referenced throughout the chapter.

- Parent skill: `voss-tactical-empathy` â€” the empathy/No/calibrated-question moves between Ackerman rounds depend on this mindset.

- Sibling carved Voss skills:
  - `voss-labeling` â€” used between rounds to acknowledge the counterpart's reaction
  - `voss-no-framework` â€” provides the "ways to say No" between rounds
  - `voss-calibrated-questions` â€” provides the questions ("How am I supposed to do that?") between rounds
  - `voss-mirroring` â€” different domain; rarely used inside Ackerman protocol
  - `voss-accusation-audit` â€” pre-conversation prep that complements Ackerman if the counterpart is hostile
  - `voss-black-swans` â€” orthogonal but composable; finding hidden constraints can move the target itself

- The Ackerman Group (Mike Ackerman's firm) and Howard Raiffa's *The Art and Science of Negotiation* (Harvard, 1982) are the underlying intellectual sources Voss cites.
