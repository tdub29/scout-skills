---
name: control-target-sync
description: The live-sync couple â€” a scrubbed/typed/picked control drives a second element's property in the SAME beat. Readout tween + target transform tween share one timeline label (continuous scrub), or one threshold state array carries both sides (discrete steps). Makes "change this, watch it change" read as causality.
metadata:
  tags: control, scrub, live-sync, mirror, panel, editor, couple, readout, ui
---

# Control-Target Sync

THE live-editing move: an inspector/editor control is manipulated â€” a value scrubbed, a field retyped, a dropdown picked â€” and a **bound second element answers in the same frame**. The button rotates WHILE the rotation value scrubs; icons resize PER KEYSTROKE. The persuasion is causality â€” one gesture, two surfaces changing together â€” and this rule is the coupling contract that produces it.

Nearest precedent is [reactive-displacement.md](reactive-displacement.md): that rule also derives two elements' motion from one source, but it is **collision physics** â€” an entering intruder displaces an exiting victim, once, as a transition, and the victim leaves. This rule is a **live editing mirror**: the control is manipulated repeatedly across several beats, the target answers every time, and both sides hold the stage throughout. The numeric readout rides [counting-dynamic-scale.md](counting-dynamic-scale.md)'s proxy pattern; discrete steps ride [discrete-text-sequence.md](discrete-text-sequence.md)'s threshold pattern â€” what this rule adds is the law that binds either of them to the target.

## How It Works

An **edit beat** is a set of concurrent tweens at ONE timeline label: `tl.addLabel("edit1", â€¦)`, then the **readout tween** (numeric proxy + `onUpdate` writing `textContent` only) and the **target transform tween** (`rotation` / `x` / `y` / `scale` to the same endpoint), both placed at the label with the same **duration** and **ease**. The two motions are two projections of one gesture â€” value at 40% â‡’ target at 40%, on every frame, under any seek. That mathematical lockstep reads as "the panel is editing the page," not "two animations happen to overlap."

For **discrete edits** (per-keystroke retypes, dropdown picks, unit snaps) the couple steps instead of glides: a single threshold state array carries BOTH sides â€” each state holds the readout text AND the target's property value â€” and one driver applies whichever state is active. Both sides read from the same state object, so they cannot desync.

Chain 2â€“4 edit beats with short holds between, and end on a **landed** edit â€” the last value applied and holding, never a tooltip with the dropdown unopened.

## Recipe

```html
<!-- Bipartite by construction: target surface + inspector panel share the frame.
     Every scrubbed readout gets `font-variant-numeric: tabular-nums` and a fixed
     min-width (â‰¥ the longest value) or the panel edge jitters as digits change. -->
<div class="target-surface">
  <div class="target-button" id="target-button">{buttonLabel}</div>
  <div class="preview-row">
    <div class="preview-icon">{iconA}</div>
    â€¦
  </div>
</div>
<div class="panel">
  <div class="field-row">
    <span>Rotation</span><span class="field-value" id="rotation-readout">0Â°</span>
  </div>
  <div class="field-row">
    <span>Class</span><span class="field-value mono" id="class-readout">text-1xl</span>
  </div>
</div>
```

```js
// ---- Continuous couple: ONE label; both tweens share duration AND ease ----
tl.addLabel("edit1", EDIT1_AT);
const rotState = { v: 0 };
const rotReadout = document.getElementById("rotation-readout");
tl.to(
  rotState,
  {
    v: ROT_TARGET,
    duration: SCRUB_DUR,
    ease: SCRUB_EASE,
    onUpdate: () => {
      rotReadout.textContent = `${Math.round(rotState.v)}Â°`;
    },
  },
  "edit1",
);
tl.to(
  "#target-button",
  { rotation: ROT_TARGET, duration: SCRUB_DUR, ease: SCRUB_EASE },
  "edit1", // same label â€” the mirror answers in the same frame
);

// ---- Discrete couple: ONE state array carries BOTH sides ----
const STEPS = [
  { t: 0.0, text: "text-1xl", scale: 1.0 }, // must equal the initial state
  { t: 0.4, text: "text-4xl", scale: 1.9 },
  { t: 1.0, text: "text-xl", scale: 0.85 }, // backspace
  { t: 1.35, text: "text-2xl", scale: 1.3 }, // lands
];
const stepAt = (time) => [...STEPS].reverse().find((s) => time >= s.t) ?? STEPS[0];

tl.addLabel("edit3", EDIT3_AT);
const classReadout = document.getElementById("class-readout");
const stepDriver = { t: 0 };
let lastStep = null;
tl.to(
  stepDriver,
  {
    t: STEPS_TOTAL,
    duration: STEPS_TOTAL,
    ease: "none",
    onUpdate: () => {
      const s = stepAt(stepDriver.t);
      if (s !== lastStep) {
        classReadout.textContent = s.text; // control steps
        gsap.set(".preview-icon", { scale: s.scale }); // target steps â€” same state object
        lastStep = s;
      }
    },
  },
  "edit3",
);
```

## Variations

- **Dropdown pick â†’ instant conversion (self-conversion)** â€” the pick converts the panel's own readout in place (`tl.set("#padding-readout", { textContent: "6 px" }, "pick")`); control and target collapse into one element. Compose the dropdown from neighbors: menu pops via [spring-pop-entrance.md](spring-pop-entrance.md), row hover-stepping via [dynamic-content-sequencing.md](dynamic-content-sequencing.md). The conversion must be an INSTANT snap â€” tweening between unit strings reads as broken, and instantness is the feature being sold.
- **Easing-handle drag â†’ target re-animates (deferred mirror)** â€” the edit authors a _behavior_, so the mirror is a **replay**, not a concurrent transform: beat 1 drags the handle (handle tween + coords readout), then at a later label the target performs its motion with the newly-authored curve (`tl.fromTo("#toggle-knob", { x: 0 }, { x: KNOB_TRAVEL, duration: REPLAY_DUR, ease: AUTHORED_EASE }, "replay")`), often under a zoom-out ([viewport-change.md](viewport-change.md)). The one sanctioned case where the response is not in the gesture's beat; the replay must still be unmistakably the edited parameter.
- **Read-sync mirror (reverse direction)** â€” the gesture happens ON the target (hovering swatches, selecting an element) and the PANEL readout is the bound side. Same discrete contract â€” one state array of `{ t, hoverTarget, readout }` drives both the highlight and the text.
- **Color couple** â€” the readout counts (`0 â†’ 80`) while the target's `backgroundColor` tweens between two palette stops at the same label. Keep it two fixed stops (GSAP interpolates); never derive per-frame hex strings by hand.

## Values

| token                | range                           | notes                                                                                                                                 |
| -------------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| SCRUB_DUR            | 0.8â€“1.6 s                       | the viewer must see BOTH sides move â€” under ~0.6 s the mirror registers subconsciously at best                                        |
| SCRUB_EASE           | `power1.inOut` / `power2.inOut` | shared verbatim by both tweens. Never `back.out` / `elastic.out` â€” an overshooting value reads as a broken hinge; the readout is data |
| edit endpoints       | visible but plausible           | âˆ’10Â° tilt, 38 px shift, 1xl â†’ 4xl â†’ 2xl; a 2Â° rotation doesn't demo anything                                                          |
| HOLD_BETWEEN         | 0.3â€“0.8 s                       | each landed value gets a breath; below 0.3 s the beats smear into one gesture                                                         |
| BEAT_COUNT           | 2â€“4                             | one edit is a moment, not a demo; past 4 the shot reads as a settings tour                                                            |
| STEP gaps (discrete) | 0.15â€“0.5 s                      | keystroke pacing per discrete-text-sequence; first state must equal the on-load state                                                 |
| VALUE_MIN_WIDTH      | â‰¥ longest value's width         | without it the panel edge jitters as digit counts change                                                                              |

## Critical Constraints

- **One label, one gesture** â€” readout tween and target tween share position, duration, AND ease; never sequence readout-then-target, and never stagger the target behind the readout even by 0.1 s â€” a delayed response reads as an animation following an edit, not a bound surface. A mismatched ease desyncs the mirror mid-tween even when endpoints agree.
- **Discrete steps share one state object** â€” both sides read the same array entry, so desync is impossible by construction; first entry mirrors the initial DOM state.
- **The readout is data** â€” no overshoot, no bounce on the settle; the target may carry the gesture's ease but lands exactly on the edited value.
- **Co-visibility is load-bearing** â€” control and target share the frame for every edit beat; a camera move must never crop the mirror out (punch-and-return around the beats, not through them).
- **`tabular-nums` + fixed `min-width`** on every scrubbed readout; `onUpdate` is O(1) â€” text writes only, discrete drivers guard writes with a last-state check.
- **End on a landed edit** â€” the final beat resolves with the value applied and holding (or the deferred-mirror replay); never mid-gesture or on an unopened menu.
- **The gesture's actor is a separate rule** â€” cursor glide, grab-cursor flip, and click feedback come from the cursor rules; this rule owns only the couple.

## See also

`cursor-click-ripple` / `context-sensitive-cursor` (the hand performing the gesture) Â· `counting-dynamic-scale` (the readout half alone, when there is no bound target) Â· `discrete-text-sequence` (retypes inside the control field) Â· `spring-pop-entrance` (dropdowns/chrome around the couple) Â· `multi-phase-camera` (punch-and-return framing) Â· `chart-scrub-readout` (the sibling READ direction â€” a scrub interrogates a chart instead of editing a target).
