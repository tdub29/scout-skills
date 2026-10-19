# panel-edit-live-sync â€” Panel Edit, Live Sync

**intent**: A bipartite stage â€” an inspector/editor **panel bound to a target surface** â€” where a cursor (or text caret) continuously manipulates a control (value scrub, unit/codegen dropdown pick, knob or easing-handle drag, inline retype) and the coupled surface updates **live, in the same beat**: the page button rotates as the value scrubs, preview icons resize per keystroke, the hex readout mirrors every hover, the code block converts on the pick. The motion IS the causality â€” one gesture, two surfaces changing in the same frame. The camera's job is co-visibility of the couple, not a chase.

**provenance** (7 mined Key_Feature goldens across 4 products, both dialects â€” three sync modes):

- _Write-sync (control â†’ target)_ â€” the anchor mode: a visual-editor panel scrubs rotation/margin/padding while the live page button rotates and shifts in the same beat (plus unit + font-weight dropdown picks); an inline `className` retype in a glowing code callout resizes the preview icons per keystroke (caret-as-actor, push-in/pull-back roundtrip that must keep BOTH surfaces in frame); a motion editor drags a knob along a dotted motion path and bends easing handles into an S-curve, paying off with a big zoom-out where the finished toggle PERFORMS the edited ease (deferred payoff).
- _Read-sync (target â†’ panel mirror)_: clicking a page button pops a toolbar â†’ "Copy code" â†’ the code editor fills with the element's CSS under one continuous slow zoom-out; hovering palette swatches live-updates a footer hex readout while the grid scrolls.
- _Self-conversion (panel is both control and target)_: unit dropdown conversions inside a 3D-tilted spacing panel snap-convert values in place (remâ†’pxâ†’%, `0,375 rem` â†’ `6 px` â†’ `4,871 %`); a codegen dropdown picks SwiftUI and the CSS block crossfades into SwiftUI under a rapid punch-in.

> **Concentration caveat**: 4 of 7 members are one video (CSS Scan Pro 2.0). The COUPLING engine is independently attested by 3 more products across 3 more videos and both dialects (Figma Dev Mode, Figma motion editor, bolt.new), each on a different surface pair â€” page+inspector, canvas+timeline+easing panel, IDE code+app preview â€” so the shape is real, not one film's house style. What IS CSS-Scan-Pro house style (marked optional below): the dark-slate capability title-card prelude, the oversized black cursor with white outline, the green success-checkmark flip, flash tooltips. Trigger is product-conditional: reach for this shape when the feature itself is live editing/inspection.

**roles served**

- Key_Feature (from `panel-edit-live-sync`, all 7 cases): one capability demonstrated as 2â€“4 edit beats on a single bound element â€” each beat a continuous manipulation the coupled surface answers in real time, resolving on the last edit held, a zoom-out to the finished product performing the edit, or a callout landing on the result. Three sub-shapes fold in:
  - **(A) write-sync** â€” cursor/caret edits a control; the TARGET transforms live (rotate/shift/stretch/resize/re-animate).
  - **(B) read-sync** â€” cursor selects/hovers the target; the PANEL readout mirrors live (CSS streams in, hex footer updates).
  - **(C) self-conversion** â€” the edit transforms the panel's own readout (units snap-convert, CSS crossfades to SwiftUI).

**duration**: 5.3â€“11.9s (read-sync hover demos shortest ~5.3s; multi-beat scrub/edit runs 8.7â€“11.9s)

**shot structure** (a `[target surface â€” webpage / design canvas / IDE + live preview]` sharing the frame with a `[bound panel â€” floating inspector / docked code panel / timeline + easing editor]`; a `[cursor or caret]` is the actor; every beat pairs ONE manipulation gesture with a SIMULTANEOUS response on the coupled surface; selection chrome declares which element is bound; camera ranges locked â†’ active but always preserves the couple)

- **Scene 0 (optional, 0.0â€“2.0s) â€” capability title card.** Solid dark `[slate/charcoal]` card; a single white line names the capability (`"Edit CSS visually"`, `"Auto measurement units conversion"`, `"Check color palettes"`) â€” fades/drifts in, holds, then a HARD CUT or a fast motion-blurred zoom-out that settles the stage. (CSS-Scan-Pro-house-leaning; 071/017/080 open cold on the stage, 071 instead springs a giant lowercase `[verb word]` over the preview.)

- **Scene 1 (~1â€“3s) â€” the couple establishes.** The `[target surface]` arrives with the `[bound panel]` docked, floating in subtle 3D tilt, or SLIDING IN from an edge. Selection chrome pops on to declare the binding: `[bounding box + corner handles / red dashed inspection guides / redline measurement chips popping sequentially / green class-name header]`. The cursor enters and glides to the first control.

- **Scene 2..N (~2s each) â€” edit beats, gesture + mirror in the same frame (the engine).** Each beat is ONE continuous manipulation and its live answer:
  - _Variant â€” write-sync (A)_: the cursor CLICK-AND-DRAGS a numeric field (value counts up/down: `0Â°â†’-10Â°`, `0â†’38 px`) while the target `[button/element]` rotates/shifts/stretches in real time; OR drags a `[knob along a dotted motion path / easing handle bending the curve, coords readout updating]`; OR a caret INLINE-RETYPES a value (`1xlâ†’4xlâ†’2xl`) inside a `[glowing magnifier callout]` while `[preview elements]` resize per keystroke. A flash `[tooltip]` may name the gesture.
  - _Variant â€” read-sync (B)_: the cursor CLICKS/HOVERS the target element â€” a `[floating toolbar]` springs up above it, a menu pick fires (`Copy code` â†’ icon flips to a green checkmark) and the `[code editor]` fills with streaming CSS; or hovered `[swatches]` outline and the `[footer hex]` updates instantly per hover as the grid scrolls.
  - _Variant â€” self-conversion (C)_: the cursor clicks a unit/codegen `[dropdown]` â€” it opens with hover-highlighted rows + checkmark â€” and on the pick the readout SNAP-CONVERTS in place (`remâ†’px`, value recalculates) or the whole `[code block]` crossfades to the new language, heading flipping (`Layout`â†’`HStack`).
  - Camera per beat: LOCKED wide holding both surfaces; or a PUNCH-IN to the acting surface (panel scroll reveals the next section) â€” but during a write-sync edit both gesture and mirror stay co-visible (071's law: the push-in never crops the preview out).

- **Scene N (final beat â†’ end) â€” the edit proves out, HOLD.** Resolution diverges:
  - _Variant â€” last edit held_: the final pick lands (`100 - Thin` selected, `4,871 %` applied) and the state simply HOLDS â€” never end on the tooltip with the dropdown unopened.
  - _Variant â€” payoff zoom-out_: a big zoom-out reveals the finished product PERFORMING the edited parameter â€” the toggle slides with the new ease inside the full phone mockup, confetti drifting; or the pull-back returns to the identical full framing while a `[terminal]` appends an hmr line.
  - _Variant â€” callout lands_: a large `[arrow callout]` slides in pointing at the result / the export menu rests open under the cursor; frame drifts subtly outward.

**signature move**: the **live-sync couple** â€” a scrubbed/typed/dragged control and its bound surface changing simultaneously, in-frame together, every edit beat.

**motion vocabulary**: click-and-drag value scrubbing with live target sync (rotate / shift / stretch); per-keystroke live preview resize; inline retype with backspace + blinking caret; instant value snap-conversion; live hex/readout mirror on hover; unit/codegen dropdown with hover-highlight rows + checkmark, instant open/close; font-weight/dropdown row pick; knob drag along a dotted motion path with waypoints; easing-handle drag bending the curve (coords readout updating); playhead scrub; redline measurement chips popping sequentially; bounding box + corner handles; red dashed inspection guides; floating toolbar springs up above the selected element; code panel slides in from an edge; in-panel scroll to a new section; swatch-grid scroll; syntax-highlighted code streams/pastes in; code crossfade (CSSâ†’SwiftUI) with heading flip; glowing magnifier callout over a code token; icon flips to green success checkmark; flash tooltip naming the gesture; oversized black cursor with white outline; grab-cursor drag; dark title-card prelude + hard cut; fast motion-blurred zoom-out settle; ONE continuous slow zoom-out spanning a demo shot; eased push-in â†’ hold â†’ eased pull-back roundtrip; quick punch-in to panel/timeline/code; subtle 3D tilt drift/parallax on a floating panel; big zoom-out to the product payoff; result element re-animates with the edited ease; confetti drift; terminal log append; large arrow callout slide-in; static hold.

**rule mapping**

- cursor glide to a control, presses, click feedback â†’ `cursor-click-ripple`
- cursor state flips pointerâ†”grab over a scrubbable field / draggable handle â†’ `context-sensitive-cursor`
- scrubbed numeric readout counts up/down under the drag â†’ `counting-dynamic-scale`
- **the live-sync couple itself** (control gesture drives a second element's property in the same beat) â†’ `control-target-sync` (concurrent tweens at the SAME timeline position â€” readout tween + target transform tween sharing one label)
- inline retype with backspace, typos, holds / keystroke thresholds â†’ `discrete-text-sequence` (+ `context-sensitive-cursor` for the caret blink)
- per-keystroke preview resize â†’ `discrete-text-sequence` (keystroke state thresholds) + `control-target-sync` (the coupled scale steps)
- instant value snap-conversion / hex readout swap / heading flip (`Layout`â†’`HStack`) / status text â†’ `discrete-text-sequence`
- syntax-highlighted code streaming/pasting in, terminal log append â†’ `discrete-text-sequence` (bulk additions are explicitly in-scope)
- dropdown/menu pops open; floating toolbar springs up; tooltip flash; redline chips pop sequentially (staggered, â‰¤500ms) â†’ `spring-pop-entrance`
- dropdown row hover-highlight stepping and pick sequencing / which edit beat shows what â†’ `dynamic-content-sequencing`
- dashed inspection guides / selection outline draw on â†’ `svg-path-draw`; dotted motion path with waypoints â†’ `svg-path-draw` (the path display)
- knob TRAVEL along the motion path â†’ path following â€” see `hyperframes-keyframes` (paths)
- easing-handle drag bending the curve (SVG `d` interpolation) â†’ SVG path morph â€” see `hyperframes-keyframes` (morph; `svg-path-draw` only draws strokes, it cannot morph a path); coords readout beside it â†’ `discrete-text-sequence`
- glowing magnifier callout over a code token (incl. the live enlarged duplicate of a UI token) â†’ composition: `ambient-glow-bloom` (the glow) + `spring-pop-entrance` (the callout pop)
- code panel slides in from an edge / panel docks â†’ `card-morph-anchor` / `scale-swap-transition` (per cursor-ui-demo precedent for panel slide-in)
- code block crossfade CSSâ†’SwiftUI; success-icon flip to green checkmark â†’ `scale-swap-transition` (state swap at the same anchor)
- in-panel scroll / swatch-grid scroll (masked internal translate) â†’ `gsap-effects`; on a 3D-tilted panel â†’ `3d-page-scroll` (tilted plane w/ internal scroll)
- subtle 3D tilt drift/parallax on the floating panel; continuous micro-drift on holds â†’ `multi-phase-camera` (micro-drift phase)
- punch-in to panel/timeline/code and settle â†’ `coordinate-target-zoom` + `multi-phase-camera`
- eased push-in â†’ hold â†’ eased pull-back roundtrip (co-visibility preserved) â†’ `multi-phase-camera` (pull-back / focus / push sequencing)
- ONE continuous slow zoom-out spanning the demo shot; big zoom-out to the product payoff â†’ `viewport-change` (single `.world` composite transform)
- fast motion-blurred zoom-out settle transition â†’ `motion-blur-streak` + `viewport-change`
- result element re-animates with the edited ease (toggle slides with the new S-curve) â†’ `gsap-effects` (custom-ease tween on the payoff element)
- confetti drift on the payoff â†’ `particle-burst` (deterministic confetti) + `sine-wave-loop` (bounded drift)
- large arrow callout slide-in + hold â†’ `gsap-effects` (single slide tween)
- dark title-card prelude (capability line fades/drifts in, hard cut out) â†’ cross-blueprint: `titlecard-reveal` territory; the drift/fade itself â†’ `gsap-effects` â€” EXIT-N/A as a mapped rule here
- hard cuts between title and demo; final static hold â†’ EXIT-N/A (transition registry / no rule needed)

**camera modifier**: The camera law is the INVERSE of cursor-ui-demo's chase: it serves **co-visibility of the couple**. Three attested postures â€” (1) LOCKED: fixed framing for the whole demo, panel + target both in frame, all motion element-level (CSS_39.0, CSS_102.8 after settle); (2) ONE CONTINUOUS MOVE: a single slow zoom-out (or drift) spanning the entire demo shot while edits fire inside it (CSS_10.9, CSS_63.5's tilt-drift) â†’ `viewport-change`; (3) PUNCH-AND-RETURN: eased push-in onto the acting surface, tight hold through the edit, eased pull-back to the identical opening framing (071_bolt, 080_figma, 017_figma) â†’ `multi-phase-camera` + `coordinate-target-zoom` â€” with the hard constraint that during a write-sync edit the mirror surface is never cropped out. If the camera is chasing the cursor target-to-target with per-beat state swaps, you're in `cursor-ui-demo`, not here.
