# Ogilvy: Big Idea Gate

## When to Use

Use this when the user has one or more campaign ideas and needs to decide whether any of them are big enough to build around.

Trigger when someone asks whether an ad idea is big, whether a campaign concept can last, how to choose among concepts, why a concept feels small, or whether the product itself should be made the hero.

Do not trigger for creating finished copy, headlines, or ad variants; route execution to `copywriting` or `ad-creative`. Do not trigger for selective headline audits; route to `hopkins-headline-audit`. Do not trigger for claim substantiation; route to `hopkins-scientific-claim-check`. Do not trigger for market tests or rollout pilots; route to `hopkins-test-campaign`.

## Framework

Ogilvy says homework is necessary but not sufficient. Advertising needs a big idea, or it passes "like a ship in the night."

Use his five recognition questions:

1. Did it make me gasp when I first saw it?
2. Do I wish I had thought of it myself?
3. Is it unique?
4. Does it fit the strategy to perfection?
5. Could it be used for 30 years?

Add two Ogilvy constraints:

- The unconscious can produce big ideas only when it has been fed with product and consumer information.
- Whenever possible, make the product itself the hero. There are no dull products, only dull writers.

## How to Apply

1. Restate the strategy and main promise before looking at ideas.
2. For each candidate idea, score the five questions from 0 to 2.
3. Penalize ideas that are clever but not strategy-fit, visual but not ownable, or exciting but short-lived.
4. Check whether the product is the hero, or whether the execution is using borrowed interest.
5. Mark whether the idea could survive repetition, personnel changes, and competitive pressure.
6. Choose: build, revise, hold for later, or kill.

## Output Format

Return a big idea gate:

- Strategy anchor: the promise and audience the idea must serve.
- Candidate scores: one row per idea with the five Ogilvy questions scored.
- Product-hero check: whether the product, not the creative flourish, carries the idea.
- Durability verdict: likely campaign life and risks.
- Decision: build, revise, hold, or kill.
- Next route: execution to `copywriting` or `ad-creative`; formal pilot design to `hopkins-test-campaign`.

## Common Failure Modes

- Mistaking novelty for a big idea.
- Approving an idea that makes people gasp but does not fit the strategy.
- Killing a durable idea because it feels too simple.
- Using research to predict cumulative long-term value when the issue is strategic judgment.
- Letting a borrowed-interest gag, celebrity, or visual trick replace the product.
- Turning the gate into copy execution; this skill decides whether to proceed.

## References

- David Ogilvy, *Ogilvy on Advertising* (1983), Chapter 2, "What's the big idea?" and "Make the product the hero".
- Sibling skills: `ogilvy-advertising-homework`, `ogilvy-positioning-image`, `ogilvy-direct-response-lens`, `ogilvy-print-ad-audit`, `ogilvy-tv-commercial-formats`, `ogilvy-b2b-advertising`.
- Overlap routes: `copywriting`, `ad-creative`, `hopkins-headline-audit`, `hopkins-scientific-claim-check`, `hopkins-test-campaign`.
