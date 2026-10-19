---
name: behavior-design
description: "Habits, not UI. Fogg, Eyal, Clear frameworks."
---

# behavior-design

This hub collapses three foundational behavior-design books into one router plus eighteen references. Route by user cue, read the referenced file(s) in full, and apply that framework exactly â€” including its detection cues and ethical guardrail.

Book provenance: **BJ Fogg, *Tiny Habits: The Small Changes That Change Everything* (Houghton Mifflin Harcourt, 2020)** for the `fogg-*` references, **Nir Eyal with Ryan Hoover, *Hooked: How to Build Habit-Forming Products* (Portfolio/Penguin, 2014)** for the `eyal-*` references, and **James Clear, *Atomic Habits* (Avery, 2018)** for the `clear-*` references.

## When to use

Use this hub when the user wants to **engineer a habit on purpose** â€” for themselves, for another person, or built into a product. Typical intents:

- **Personal behavior change** â€” start, scale, or troubleshoot a personal habit; stop an unwanted one. Lead with the `fogg-*` references (B=MAP, anchored tiny recipe, celebration) and the `clear-*` references (the Four Laws, identity, habit tracking/accountability). Fogg and Clear are complementary lenses on the same personal layer â€” see the guardrail below.
- **Product habit design** â€” make a product, app, or service something users return to without external prompting; design retention/engagement loops. Lead with the `eyal-*` references.
- **Diagnosis** â€” "this habit isn't sticking / this feature isn't retaining," "why do I keep doing X," "why won't users come back." Use the models to locate the broken element.
- **Ethics audit** â€” "is this product manipulative / exploitative," "should we even build this hook." Go to `references/eyal-manipulation-matrix.md`.

## Guardrails

- **Design literacy, not coercion.** These frameworks are powerful precisely because they work below conscious deliberation. The same models that build a flossing habit can build a compulsion. For every habit-forming move, run the ethics check: **identify** the move, ask whether it **materially improves the user's life**, ask whether **the maker would use it themselves**, and prefer the **ethical alternative**.
- **Manipulation Matrix gate for product work.** Before designing a product hook, route through `references/eyal-manipulation-matrix.md`: Facilitator (uses it + improves life â€” proceed), Peddler (improves-life claim without using it â€” beware self-deception), Entertainer (uses it, no life-improvement claim â€” fine but fleeting), Dealer (neither â€” exploitation; stop).
- **Match the lens to the layer.** Fogg and Clear are personal-scale behavior design (one person, their habits); Eyal is product-scale (many users, repeated loops). Don't apply product-retention tactics to a personal habit, or personal celebration mechanics to a retention metric, without translating. Within the personal layer, **Fogg = B=MAP + emotion/celebration wiring** (one anchored tiny recipe, wired in by immediate positive emotion), while **Clear = the Four Laws + tracking/accountability/identity** (cue/craving/response/reward tuned by make-it-obvious/attractive/easy/satisfying, sustained by streaks, contracts, and "votes" for an identity). Where they overlap (habit stacking, starting tiny), cross-reference rather than duplicate; pick the lens that matches the user's framing.
- **Don't answer from router memory alone.** Load the selected reference file(s) first and follow their process, demonstrations, and guardrail.
- **Stay in scope.** For general consumer-psychology and persuasion framing use `marketing-psychology`; for conversion-rate optimization and retention/churn metrics and dashboards use `cro` / `churn-prevention`. Cross-reference; do not duplicate.

## Quick routing table

| User cue (examples) | Route to reference |
|---|---|
| why a behavior happens or doesn't, B=MAP, Fogg Behavior Model, motivation/ability/prompt, the action line, "no prompt no behavior," disrupt an unwanted habit | `references/fogg-behavior-model.md` |
| how to phrase a new habit, "After I [anchor] I will [tiny behavior]," recipe card, anchor to an existing routine, start absurdly small, Starter Step | `references/fogg-tiny-habits-recipe.md` |
| make a behavior easier, "what's making this hard to do," Ability Chain, five ability factors (time/money/physical effort/mental effort/routine), shrink the behavior, scale back | `references/fogg-ability-simplify.md` |
| habits don't stick despite repetition, "emotions create habits," celebrate, Shine, wire it in immediately, feel successful, reward prediction error | `references/fogg-celebration-emotion.md` |
| turn an aspiration into specific behaviors, what should I actually do, Magic Wanding, Swarm of Behaviors, Focus Mapping, golden behaviors, impact vs feasibility, "help people do what they already want to do" | `references/fogg-behavior-matching.md` |
| overview of the product habit loop, four phases Triggerâ†’Actionâ†’Variable Rewardâ†’Investment, Habit Zone, frequency Ã— perceived utility, build a habit-forming product | `references/eyal-hook-model.md` |
| what brings users back, external vs internal triggers, paid/earned/relationship/owned triggers, attach to boredom/loneliness/uncertainty, the 5 Whys for internal triggers | `references/eyal-triggers-external-internal.md` |
| reward design, why a feature stops being engaging, rewards of the Tribe/Hunt/Self, variability, slot-machine effect, finite vs infinite variability | `references/eyal-variable-rewards.md` |
| why effort makes users return, stored value, data/content/followers/reputation/skill, loading the next trigger, IKEA effect, escalation of commitment, little investments | `references/eyal-investment-stored-value.md` |
| is this manipulation/exploitation, should we build this hook, ethics of habit-forming design, Facilitator/Peddler/Entertainer/Dealer | `references/eyal-manipulation-matrix.md` |
| 1% better / marginal gains, why small habits compound, Plateau of Latent Potential / valley of disappointment, systems vs. goals, "you fall to the level of your systems," focus on the trajectory not the result | `references/clear-atomic-habits-systems.md` |
| identity-based habits, three layers (outcomes/processes/identity), change who you are not just what you get, habits as votes for the person you wish to become, "become a runner not run a marathon" | `references/clear-identity-based-habits.md` |
| the habit loop (cue â†’ craving â†’ response â†’ reward), the Four Laws of Behavior Change + inversions overview, which stage is broken, make it obvious/attractive/easy/satisfying | `references/clear-habit-loop-four-laws.md` |
| make a cue obvious, Habits Scorecard, implementation intentions ("I will [behavior] at [time] in [location]"), habit stacking ("After [current habit], I will [new habit]"), environment design, make a bad cue invisible | `references/clear-make-it-obvious.md` |
| make a habit attractive, temptation bundling, social imitation (the close / the many / the powerful), join a culture where it's normal, "get to" vs "have to" reframing, motivation ritual, make it unattractive | `references/clear-make-it-attractive.md` |
| make a habit easy, Law of Least Effort, reduce friction / prime the environment, the Two-Minute Rule / gateway habit, habit shaping, commitment devices & automation, make a bad habit difficult | `references/clear-make-it-easy.md` |
| make a habit satisfying, immediate reward / reinforcement, habit tracking / "don't break the chain," never miss twice, accountability partner & habit contract, make a bad habit unsatisfying | `references/clear-make-it-satisfying.md` |
| keep a habit from stalling, Goldilocks Rule / just-manageable difficulty / flow, falling in love with boredom, perpetual improvement, reflection & review (Annual Review / Integrity Report), keep identity flexible | `references/clear-advanced-goldilocks-review.md` |

## Workflow

1. **Identify the layer.** Personal behavior (Fogg / Clear) or product habit (Eyal)? Diagnosis or design or ethics audit? On the personal layer, pick Fogg for B=MAP + celebration framing or Clear for Four Laws + tracking/identity framing.
2. **Pick the closest row(s)** in the routing table. Start with 1â€“2 references; expand only when the user asks for a combined method (e.g., Fogg B=MAP to diagnose, then Hook Model to redesign a product moment).
3. **Read those `references/*.md` files completely.**
4. **Apply the framework's steps, demonstrations, and detection cues** from those references. Name the specific element in play (e.g., "your prompt is missing," "this is a Reward of the Tribe," "you're a Peddler here").
5. **Run the ethics check** whenever you are designing a hook for other people: identify the move â†’ does it materially improve the user's life â†’ would the maker use it â†’ what is the ethical alternative.

## Common failure modes (hub-level)

- **Skipping the ethics gate** â€” designing a product hook without routing through the Manipulation Matrix, so a Dealer move gets shipped as if it were a Facilitator move.
- **Wrong layer** â€” applying product-retention variability to a personal flossing habit, or treating a single person's habit as a frequency Ã— perceived-utility retention problem.
- **Blaming willpower** â€” diagnosing a missing-prompt or too-hard behavior as a motivation/character failure (the exact mistake Fogg's model exists to prevent).
- **Router-only answer** â€” summarizing a model without loading the reference's full framework, demonstrations, and guardrail.
- **Bolting motivation on later** â€” picking a behavior the person "should" do and trying to manufacture motivation, instead of matching to a golden behavior they already want.

## References

- [references/clear-advanced-goldilocks-review.md](references/clear-advanced-goldilocks-review.md)
- [references/clear-atomic-habits-systems.md](references/clear-atomic-habits-systems.md)
- [references/clear-habit-loop-four-laws.md](references/clear-habit-loop-four-laws.md)
- [references/clear-identity-based-habits.md](references/clear-identity-based-habits.md)
- [references/clear-make-it-attractive.md](references/clear-make-it-attractive.md)
- [references/clear-make-it-easy.md](references/clear-make-it-easy.md)
- [references/clear-make-it-obvious.md](references/clear-make-it-obvious.md)
- [references/clear-make-it-satisfying.md](references/clear-make-it-satisfying.md)
- [references/eyal-hook-model.md](references/eyal-hook-model.md)
- [references/eyal-investment-stored-value.md](references/eyal-investment-stored-value.md)
- [references/eyal-manipulation-matrix.md](references/eyal-manipulation-matrix.md)
- [references/eyal-triggers-external-internal.md](references/eyal-triggers-external-internal.md)
- [references/eyal-variable-rewards.md](references/eyal-variable-rewards.md)
- [references/fogg-ability-simplify.md](references/fogg-ability-simplify.md)
- [references/fogg-behavior-matching.md](references/fogg-behavior-matching.md)
- [references/fogg-behavior-model.md](references/fogg-behavior-model.md)
- [references/fogg-celebration-emotion.md](references/fogg-celebration-emotion.md)
- [references/fogg-tiny-habits-recipe.md](references/fogg-tiny-habits-recipe.md)

- **Book (Fogg references):** BJ Fogg, *Tiny Habits: The Small Changes That Change Everything* (Houghton Mifflin Harcourt, 2020)
- **Book (Eyal references):** Nir Eyal with Ryan Hoover, *Hooked: How to Build Habit-Forming Products* (Portfolio/Penguin, 2014)
- **Book (Clear references):** James Clear, *Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones* (Avery, 2018)
