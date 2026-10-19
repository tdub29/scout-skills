---
name: reactive-displacement
description: Physical collision where an entering element's spring drives the exiting element's displacement â€” single source of truth makes the motion causally linked.
metadata:
  tags: transition, physics, collision, displacement, spring, causal
---

# Reactive Displacement

Exit animation of element A is mathematically DERIVED from the entry spring of element B â€” a causal link: "A moves _because_ B hit it." Distinct from [scale-swap-transition.md](scale-swap-transition.md) (which overlaps but isn't causal) and [card-morph-anchor.md](card-morph-anchor.md) (one container morphing).

A single 0â†’1 driver tween (the "entry spring") feeds three concurrent derived motions in one `onUpdate`:

- **Intruder** (B, entering): position interpolated off-stage â†’ settled over the full driver, plus tilt settling to 0Â° and a sharp early opacity reveal.
- **Victim** (A, exiting): position interpolated settled â†’ off-stage in the OPPOSITE direction, completing at `VICTIM_FRACTION` (~0.4â€“0.5) of the driver â€” NOT 1.0.

The victim finishing BEFORE the intruder's entry creates the "hit then settle" rhythm; sharing one eased driver makes the impact moment mathematically synchronized.

## Recipe

```js
// Both cards absolutely centered; overflow: hidden on the scene (off-stage travel);
// will-change: transform, opacity on both; intruder z-index ABOVE victim.
const INTRUDER_START_X = STAGE_W; // off-stage right
const VICTIM_END_X = -STAGE_W; // off-stage left â€” SAME axis, opposite direction

gsap.set("#victim", { x: 0, opacity: 1, rotation: 0 });
gsap.set("#intruder", { x: INTRUDER_START_X, opacity: 0, rotation: -INTRUDER_TILT });

const driver = { p: 0 };
tl.to(
  driver,
  {
    p: 1,
    duration: DRIVER_DUR,
    ease: `back.out(${BOUNCE_FACTOR})`, // the intruder spring
    onUpdate: () => {
      // Intruder: full 0â†’1 progress maps enter (off-stage â†’ center)
      const intruderX = INTRUDER_START_X * (1 - driver.p);
      const intruderOpacity = Math.min(1, driver.p * FADE_IN_SHARPNESS);
      const intruderRot = -INTRUDER_TILT * (1 - driver.p); // settles to 0Â°
      const intruder = document.getElementById("intruder");
      intruder.style.transform = `translate(-50%, -50%) translateX(${intruderX}px) rotate(${intruderRot}deg)`;
      intruder.style.opacity = String(intruderOpacity);

      // Victim: completes its exit at VICTIM_FRACTION of the driver â€” by the
      // time the intruder centers, the victim is already off-stage.
      const victimP = Math.min(1, driver.p / VICTIM_FRACTION);
      const victimX = VICTIM_END_X * victimP;
      const victim = document.getElementById("victim");
      victim.style.transform = `translate(-50%, -50%) translateX(${victimX}px)`;
      victim.style.opacity = String(1 - victimP);
    },
  },
  DRIVER_AT,
);
// Climax dwell â€” intruder holds centered for â‰¥ DWELL_MIN before the scene ends.
```

## Variations

- **Impact rotation on victim** â€” the victim also rotates as it slides: `const victimRot = victimP * -VICTIM_KICK_DEG;` appended to its transform. `VICTIM_KICK_DEG` 15â€“25Â°, magnitude matched to the perceived intruder weight.
- **Vertical collision** â€” intruder from top, victim displaced downward; same math on Y. Reads as "weight dropped on it."
- **Wobble after settle** â€” after the intruder centers, a damped sine wobble (`Â±WOBBLE_AMP_DEG` rotation, linearly decaying over `WOBBLE_DUR` via a second `ease: "none"` driver at `DRIVER_AT + DRIVER_DUR`) before stillness â€” "impact aftermath."
- **Multi-victim ripple** â€” the intruder displaces multiple aligned cards, each victim's `victimP` on a slightly offset driver phase (cascade ripple).

## Values

| token             | range                  | notes                                                                                                      |
| ----------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| DRIVER_AT         | phase-dependent        | after the prior reading beat resolves; must leave â‰¥ DWELL_MIN of climax dwell before the scene ends        |
| DRIVER_DUR        | 0.6â€“1.4 s              | short = zippy punch, long = heavy landed impact; higher bounce on long durations reads as floaty           |
| BOUNCE_FACTOR     | 1.2â€“2.0 (typ. 1.4â€“1.6) | stay in the `back.out` family (or `elastic.out` for oscillation) â€” changing family rewrites the feel       |
| VICTIM_FRACTION   | 0.4â€“0.5                | <0.4 the victim disappears before the impact reads; >0.5 feels parallel, not causal; hard cap ~0.6         |
| STAGE_W           | â‰¥ composition width    | smaller leaves the off-stage element partially visible at start                                            |
| INTRUDER_TILT     | 5â€“15Â° (typ. ~10Â°)      | low = clean glide, high = "spin-and-plant"; sign consistent with entry direction (momentum transfer)       |
| FADE_IN_SHARPNESS | 3â€“8                    | intruder reaches opacity 1 at `1/FADE_IN_SHARPNESS` of progress; must be > 1 or it's transparent at center |
| DWELL_MIN         | â‰¥ 1.0 s (typ. 1.0â€“1.5) | post-impact dwell is where the new content gets read â€” do not skip                                         |

## Critical Constraints

- **Single driver = single source of truth** â€” both motions computed inside ONE driver's `onUpdate`, never separate `tl.to()` calls per element; independent tweens destroy the causal link (they'd merely be near each other in time).
- **Victim completes at a fraction of the driver** â€” the "hit" is the overlap moment; after it the victim is just vacating space the intruder will fill.
- **Directional momentum transfer** â€” same axis, opposite directions; different axes read as passing, not colliding.
- **Intruder z-index above victim** â€” explicit, not DOM order; otherwise the victim looks like it tunneled through.
- **Intruder enters tilted, settles flat** â€” small initial tilt â†’ 0Â° reads as "spinning in then planting."
- **Climax dwell after impact** â€” the impact is the headline beat; hold the settled intruder â‰¥ DWELL_MIN.
- **`overflow: hidden` on the scene** â€” off-stage motion exceeds the frame.

## See also

`control-target-sync` (the live-editing mirror â€” repeated coupled edits, nothing exits) Â· `hacker-flip-3d` (intruder text reveal during entry) Â· `sine-wave-loop` (idle breathing during the dwell) Â· `vertical-spring-ticker` (a ticker that "shoves" the previous content out).
