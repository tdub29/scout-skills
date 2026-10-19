# Eyal â€” The Manipulation Matrix (Facilitator / Peddler / Entertainer / Dealer)

## The framework

> "The matrix seeks to help you answer not, 'Can I hook my users?' but instead, 'Should I attempt to?'" (*Hooked*, Chapter 6)

This is the **ethics tool of the Hook Model** â€” the gate you run *before* writing code or shipping a product. Eyal starts from an uncomfortable admission: "We are all in the persuasion business." Manipulation is "an experience crafted to change behavior," and not all of it is bad â€” Weight Watchers is mass manipulation few people question, while addictive games feel distasteful. Habit-forming technology has been called "the cigarette of this century"; with greater access, data, and speed, the world is getting more addictive faster than society develops "antibodies." So makers need a decision tool.

The Manipulation Matrix asks the maker **two questions**:

1. **"Would I use the product myself?"** (Do *you* use it?)
2. **"Will the product materially improve users' lives?"** (Does it genuinely help them?)

Crossing these two yes/no axes gives four quadrants â€” four kinds of maker:

| | **Materially improves life: YES** | **Materially improves life: NO** |
|---|---|---|
| **Maker uses it: YES** | **Facilitator** | **Entertainer** |
| **Maker uses it: NO** | **Peddler** | **Dealer** |

## The four quadrants

- **Facilitator** (uses it + improves life). You build something you use and believe makes users' lives better â€” you're "facilitating a healthy habit." Highest chance of success because you understand the user's need first-hand. Critical honesty test: "If you find yourself squirming as you ask yourself these questions or needing to qualify or justify your answers, STOP! You failed." You must *actually* want to use it and *actually* believe it benefits you. (Exception: you'd have used it in your younger years â€” e.g. education products â€” but the further from your former self, the lower your odds.) Facilitators "build the change they want to see in the world."

- **Peddler** (improves life claim + does NOT use it). You believe your product helps people but wouldn't use it yourself. This is the danger zone of self-deception â€” "reality distortion fields" let makers twist their thinking until they imagine a user who'd find value. Fitness apps, charity sites, and especially advertising often live here, gamifying tasks no one wants with hollow points/badges. Not inherently immoral, but the odds of building something users actually want are "depressingly low" because the maker lacks empathy and first-hand insight.

- **Entertainer** (uses it + does NOT claim to improve life). You make something you enjoy but can't in good conscience say improves lives â€” that's **entertainment**, and entertainment is legitimate art for its own sake. The caveat: it's fleeting and hits-driven (the brain always wants the next novelty), so entertainer products "tend to fade quickly" and need a strong distribution engine and a full pipeline of fresh releases to be sustainable.

- **Dealer** (does NOT use it + does NOT improve life). Building something you wouldn't use and don't believe helps anyone is **exploitation** â€” the only remaining motive is "to make a buck." Casinos and drug dealers offer a good time until the addiction takes hold and "the fun stops." Lowest chance of long-term success and a morally precarious position. (Ian Bogost's Cow Clicker was meant to *satirize* Dealer mechanics â€” and accidentally hooked people anyway, so he shut it down: "The Cowpocalypse.")

## Manipulation-literacy: the four-step check

Use this both to *audit your own design* and to *recognize when a product is exploiting you*:

1. **Identify the move.** Name the specific habit-forming mechanism in play (which trigger, which variable reward, which investment / lock-in).
2. **Does it materially improve the user's life?** Honestly â€” not after rationalizing.
3. **Would the maker use it themselves?** (Or, as a user: would the maker accept being hooked this way?)
4. **Choose the ethical alternative.** If the answers place the design in Peddler or Dealer territory, redesign toward Facilitator â€” or don't build it.

Two yeses = Facilitator (proceed, with safeguards for the small fraction who form unhealthy dependencies). Uses-but-doesn't-help = Entertainer (fine, but expect it to be fleeting). Helps-but-won't-use = Peddler (beware self-deception; you probably don't understand the user). Neither = Dealer (stop â€” this is exploitation).

## How to apply

1. **Run the matrix before building any hook**, not after. It's a pre-ship decision support tool for entrepreneurs, employees, and investors.
2. **Answer the two questions honestly.** Squirming, qualifying, or justifying = a failed Facilitator claim. Don't manufacture a hypothetical user who'd value something you wouldn't.
3. **If you land in Peddler or Dealer, redesign or walk away.** For Peddler, get close enough to the user to honestly answer "would I use this?"; for Dealer, recognize there's no ethical version of the current design.
4. **Build safeguards for Facilitators.** Even a genuinely beneficial product will form unhealthy dependencies in a small fraction (~1%); makers have a "moral obligation" to use their data to identify and help over-users.
5. **As a user / for manipulation-literacy:** when a product feels compulsively sticky, run steps 1â€“4 from the *outside* â€” name the mechanism, ask if it actually improves your life, and ask whether its makers would accept being hooked this way. That diagnosis is the defense.

## Common failure modes

- **Self-deception in the Peddler quadrant.** The "reality distortion field" that invents a user who'd value what you wouldn't â€” the single most common ethical failure in habit design.
- **Skipping the matrix entirely.** Asking only "can I hook them?" and never "should I?" â€” shipping a Dealer move because it drives metrics.
- **Mistaking Entertainer for Facilitator.** Claiming life-improvement for what is really (legitimate) entertainment, then being surprised it fades.
- **Dismissing the addicted minority.** Treating the ~1% who form harmful dependencies as too small to matter instead of building safeguards.
- **Rationalizing lock-in as benefit.** Using stored value and escalation of commitment (see `eyal-investment-stored-value.md`) to trap users in a product that no longer helps them.

## Ethical guardrail

This *is* the ethical guardrail of the entire `behavior-design` hub. Every habit-forming move from the other references â€” engineered prompts (`fogg-behavior-model.md`), attaching to negative internal triggers (`eyal-triggers-external-internal.md`), engineered craving via variable rewards (`eyal-variable-rewards.md`), and lock-in via investment (`eyal-investment-stored-value.md`) â€” should be run through this matrix before it's deployed on other people. Identify the move â†’ does it materially improve the user's life â†’ would the maker use it â†’ choose the ethical alternative. Build as a Facilitator; refuse the Dealer move.

## References

- Nir Eyal with Ryan Hoover, *Hooked: How to Build Habit-Forming Products* (Portfolio/Penguin, 2014), Chapter 6 ("What Are You Going to Do With This?"): the morality of manipulation, the two diagnostic questions, and the Facilitator / Peddler / Entertainer / Dealer quadrants.
- Related: [eyal-hook-model.md](eyal-hook-model.md) (the design this gates), [eyal-triggers-external-internal.md](eyal-triggers-external-internal.md), [eyal-variable-rewards.md](eyal-variable-rewards.md), [eyal-investment-stored-value.md](eyal-investment-stored-value.md), [fogg-behavior-model.md](fogg-behavior-model.md) (B=MAP is value-neutral and needs this ethics gate). Sibling manipulation-literacy hub: `greene-48-laws` (recognizing power tactics).
