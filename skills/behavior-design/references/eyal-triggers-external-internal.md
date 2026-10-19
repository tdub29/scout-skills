# Eyal â€” Triggers: External Graduating into Internal

## The framework

> "New habits are sparked by external triggers, but associations with internal triggers are what keeps users hooked." (*Hooked*, Chapter 2)

The Trigger is the first phase of the Hook and the actuator of behavior. There are two kinds, and the entire strategic arc is moving from one to the other:

- **External triggers** communicate *what to do next* through sensory information in the environment â€” an email, a notification, a "Log-In Now" button, an app icon. The information about the next action is embedded in the trigger itself.
- **Internal triggers** are invisible â€” you can't see, touch, or hear them. They "manifest automatically in your mind": an emotion, a thought, or a pre-existing routine. When a product becomes tightly coupled with an internal trigger, the user cues their own next behavior with no external prompt. This is "the brass ring of consumer technology."

The goal of every external trigger is ultimately to drive the user through enough hook cycles that the product **attaches to a frequent internal trigger** and the user returns on their own.

## The four types of external triggers

1. **Paid triggers** â€” advertising, search/display marketing. Effective but costly; habit-forming companies use them to *acquire* users, not to bring them back (Facebook can't afford to buy an ad every time it wants you to return).
2. **Earned triggers** â€” free attention you can't buy directly: press, viral videos, App Store features. Powerful but short-lived; requires constant effort to stay in the limelight.
3. **Relationship triggers** â€” one person telling another: an invitation, a "Like," word-of-mouth, a referral. These can produce viral hypergrowth (PayPal: "someone just sent you money" was itself the trigger to open an account).
4. **Owned triggers** â€” triggers the company *owns* a place for in the user's environment, with the user's permission: an app icon on the home screen, an email subscription, a notification the user opted into. Owned triggers drive **repeat** engagement and are what bring users back, loop after loop.

Paid, earned, and relationship triggers mostly **acquire** users; **owned** triggers **re-engage** them; and the ultimate destination is the **internal** trigger that needs no owned trigger at all.

## Internal triggers are emotions, especially negative ones

> "Emotions, particularly negative ones, are powerful internal triggers." (Chapter 2)

The strongest internal triggers are uncomfortable feelings that prompt an almost instantaneous, often mindless action to quell the discomfort. Eyal's canonical map of negative emotion â†’ product:

- **Boredom** â†’ dramatic news headlines, feeds, games.
- **Loneliness** â†’ Facebook, Twitter, social destinations for instant connection.
- **Uncertainty** â†’ Google (one click away from an answer).
- **Stress / overwhelm** â†’ calming, escapist destinations like Pinterest.
- **Fear of losing a moment** â†’ Instagram (Yin opens it when she fears a special moment will be lost forever).

These stressors are often **below the threshold of consciousness** â€” tiny, nagging itches we're barely aware of reacting to. Positive emotions can also be internal triggers, but the bonds form most reliably around relieving a frequent pain. Over repeated use, the bond between the internal trigger (the feeling) and the product "cements into a habit," like layers of nacre in an oyster â€” the user "scratches the itch" with your product automatically.

## Finding the internal trigger: the "5 Whys"

To uncover the *real* internal trigger your product should attach to, start from a user need and ask **"why?" repeatedly** (a technique borrowed from the Toyota Production System's Five Whys). Each "why" peels back a layer until you reach an **emotion** rather than a feature. Example arc: a user wants to check email â†’ why? to not miss something â†’ why? to feel connected/avoid anxiety â†’ â€¦ â†’ **fear of being out of the loop** is the internal trigger. You don't design for the surface task; you design for the emotion underneath it.

## How to apply

1. **Identify the internal trigger first.** Use the 5 Whys to drive from the surface need to the underlying emotion (boredom, loneliness, uncertainty, fear, fatigue). That emotion is what your product must reliably relieve.
2. **Frequency matters.** Attach to an internal trigger the user experiences *often* â€” a feeling that recurs many times a day gives you many habit-forming occasions (Habit Zone logic; see `eyal-hook-model.md`).
3. **Sequence your external triggers.** Use paid/earned/relationship triggers to *acquire*; secure an **owned** trigger (permissioned notification, home-screen icon, email) to *re-engage*; design the loop so the product graduates to the internal trigger and needs the owned ones less over time.
4. **To detect it on yourself:** notice which emotion precedes a reflexive app open. "What do you do in response to your internal triggers?" Naming the emotion (and that the app was engineered to attach to it) is the first defense.

## Common failure modes

- **Designing for the task, not the emotion.** Building for the surface action instead of the underlying internal trigger produces a product people use only when externally prompted.
- **Living on paid/earned triggers.** Relying on ads or PR for re-engagement is unsustainable; without owned and then internal triggers, retention collapses when spend stops.
- **Picking a rare internal trigger.** Attaching to an infrequent emotion can't reach the Habit Zone no matter how strong the relief.
- **Over-notifying.** Abusing owned triggers (notification spam) is the manipulation-prone shortcut that erodes trust and permission.

## Ethical guardrail

Attaching a product to a frequent negative emotion is exactly where habit design tips toward exploitation â€” you can relieve loneliness or you can *cultivate and feed* it. Run the Manipulation Matrix (`eyal-manipulation-matrix.md`): does attaching to this internal trigger materially improve the user's life, and would you accept being hooked this way yourself? If the product manufactures or worsens the discomfort it then relieves, that's a Dealer move.

## References

- Nir Eyal with Ryan Hoover, *Hooked: How to Build Habit-Forming Products* (Portfolio/Penguin, 2014), Chapter 2 ("Trigger"): external vs internal triggers, the four external trigger types (paid, earned, relationship, owned), emotions as internal triggers, and finding internal triggers via the "5 Whys."
- Related: [eyal-hook-model.md](eyal-hook-model.md) (Trigger is phase 1), [fogg-tiny-habits-recipe.md](fogg-tiny-habits-recipe.md) (the personal analogue: anchoring to an existing routine), [eyal-manipulation-matrix.md](eyal-manipulation-matrix.md) (ethics of attaching to negative emotions).
