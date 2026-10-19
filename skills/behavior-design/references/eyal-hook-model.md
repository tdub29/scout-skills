# Eyal â€” The Hook Model (Trigger â†’ Action â†’ Variable Reward â†’ Investment)

## The framework

> "The Hook Model: a four-phase process companies use to form habits." (*Hooked*, Introduction)

The Hook is the product-design analogue of a habit loop. Through **consecutive cycles** of four phases, a product moves users from needing external prompting to returning **on their own** â€” "unprompted user engagement" â€” without relying on costly advertising. Each pass through the hook strengthens the association between the user's internal trigger and your product.

The four phases:

1. **Trigger** â€” the actuator of behavior, "the spark plug in the engine." Triggers come in two types: **external** (an email, a notification, an app icon â€” they tell the user what to do next) and **internal** (an emotion, thought, or routine that cues the action without any visible prompt). Successful products start with external triggers and, over repeated cycles, attach to an internal trigger. (Detailed in `eyal-triggers-external-internal.md`.)
2. **Action** â€” "the behavior done in anticipation of a reward." This is the simplest action the user takes toward the reward (clicking, scrolling, searching). The Action phase **explicitly incorporates Fogg's model**: the likelihood of an action is driven by **ease of doing it** Ã— **motivation to do it** (B=MAP â€” see `fogg-behavior-model.md`). Reduce effort and align motivation, and the action happens.
3. **Variable Reward** â€” what separates a Hook from a plain feedback loop: it **creates a craving** through *variability*. Predictable feedback (the fridge light) creates no desire; an unpredictable reward (a different treat each time) creates intrigue. Dopamine surges in *anticipation* of a variable reward. Eyal's three reward types: Tribe, Hunt, Self. (Detailed in `eyal-variable-rewards.md`.)
4. **Investment** â€” the user "does a bit of work," putting something into the product (time, data, effort, social capital, content, money). The investment isn't a payment â€” it's an action that **improves the product for the next go-around** and **loads the next trigger**, increasing the odds of another cycle. (Detailed in `eyal-investment-stored-value.md`.)

Barbra's worked example runs the loop: a Facebook photo (external **trigger**) â†’ she clicks through to Pinterest (**action**) â†’ she's served a cornucopia of relevant + surprising images (**variable reward**), scrolling 45 minutes â†’ she pins and collects, giving the site preference data (**investment**) that primes the next loop. Over many cycles, she associates the product with her need for social connection â€” an **internal trigger** now fires unprompted.

## The Habit Zone: frequency Ã— perceived utility

Before designing a hook, ask whether the behavior *can* become a habit. Plot two axes:

- **Frequency** â€” how often the behavior occurs.
- **Perceived utility** â€” how useful/rewarding the behavior is in the user's mind versus alternatives.

A behavior enters the **Habit Zone** (becomes a default, automatic behavior) only when it has **enough frequency and enough perceived utility**. The threshold line slopes down but never touches the perceived-utility axis:

- **High frequency** can carry **low perceived utility** into habit (Google: any single search is barely better than Bing, but it happens many times a day â†’ habit).
- **High perceived utility** can offset **lower frequency**, but only to a point â€” an infrequent behavior may *never* habituate no matter how useful (Amazon: less frequent than Google, but high perceived utility as the "everything store" keeps it the default).
- A behavior that's both infrequent and low-utility won't habituate; reposition the product so it's used more often or made more clearly valuable.

This is why the Hook Model is for **habit-forming** (repeated-use) products â€” not one-time-use goods.

## How to apply

**To design a habit-forming product:**
1. **Check the Habit Zone first.** Is the target behavior frequent enough and useful enough to habituate? If not, increase frequency (find a more frequent use occasion) or perceived utility before building hooks.
2. **Map each phase deliberately:** What external trigger starts it, and what internal trigger will it graduate to? What is the simplest action? What variable reward solves the user's problem? What investment loads the next trigger?
3. **Design the loop to compound** â€” each investment should make the next trigger more engaging, the action easier, and the reward richer.
4. **Cycle, don't single-shot.** A habit forms over *successive* hooks; one good experience isn't a habit.

**To diagnose a product that isn't retaining:** walk the four phases and find the broken link â€” no internal trigger (users only come when you push notifications), action too hard, reward too predictable (finite variability â€” see `eyal-variable-rewards.md`), or no investment (nothing stored, so nothing loads the next trigger).

## Common failure modes

- **Building hooks for a non-habit behavior.** If the behavior fails the Habit Zone test (too infrequent and low-utility), no amount of hook design makes it a habit.
- **Stopping at external triggers.** A product that only returns users via paid/owned notifications never graduates to an internal trigger and bleeds engagement when prompting stops.
- **A predictable reward.** Without variability, the reward is a plain feedback loop and creates no craving.
- **No investment phase.** Without stored value loading the next trigger, each session starts cold and the loop doesn't compound.
- **Treating the Hook as a one-time funnel.** Habits come from repeated cycles, not a single conversion.

## Ethical guardrail

The Hook Model is explicitly "a superpower" that "can be used for evil." Building it obligates a route through the **Manipulation Matrix** (`eyal-manipulation-matrix.md`) *before* you ship: identify the hook, ask whether it materially improves the user's life, ask whether you'd use it yourself, and choose the ethical alternative if the answer is no. A hook that habituates a behavior the user would not endorse on reflection is exploitation, not facilitation.

## References

- Nir Eyal with Ryan Hoover, *Hooked: How to Build Habit-Forming Products* (Portfolio/Penguin, 2014): Introduction ("The Hook Model") and Chapter 1 ("The Habit Zone," frequency Ã— perceived utility).
- Related: [eyal-triggers-external-internal.md](eyal-triggers-external-internal.md), [eyal-variable-rewards.md](eyal-variable-rewards.md), [eyal-investment-stored-value.md](eyal-investment-stored-value.md), [eyal-manipulation-matrix.md](eyal-manipulation-matrix.md), [fogg-behavior-model.md](fogg-behavior-model.md) (the Action phase is B=MAP applied to a product moment).
