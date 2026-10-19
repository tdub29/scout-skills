# Blueprints (the proven shapes)

> Entry point to the blueprint layer. Read this to find the shape for a frame; read `blueprints/<id>.md` to instantiate it. The Step-4 method (Reproduce / Adapt / Compose, what to write per frame) lives in `visual-design.md` â€” this file is the menu + the picker.

A **blueprint** is a product-agnostic, **time-coded shot template** â€” `Scene N (aâ€“b s): â€¦` with `[slots]` and one named **signature move** â€” reverse-engineered from 178 golden product-launch clips across two mining rounds (plus 13 legacy blueprints reverse-translated to the same brief format). It encodes a whole shot across its full duration â€” reveals paced to the spoken line, not dumped at t=0 â€” so instantiating one structurally keeps content arriving instead of freezing. The full template lives in `blueprints/<id>.md`. **Step 4 (visual design) instantiates one blueprint per frame** (or composes from the motion vocabulary when none fits).

## The 22 blueprints

<blueprints>
<blueprint id="kinetic-type-beats" roles="Hook, Problem, Product_Intro, Benefits, CTA, Brand_Outro" duration="3.0â€“12.9s">
Flat, centered, bold-type shot where the **motion IS the words changing** â€” a fixed line swaps tokens in place by hard cut, or a statement builds across full-screen beats (each its own move) onto a spring-pop payoff. The workhorse (6 roles). Reach for it whenever the words carry the shot and there's no set, surface, or click.
</blueprint>

<blueprint id="typewriter-reveal" roles="Hook, Brand_Outro" duration="3.6â€“7s">
A live text caret **types (and edits) a line as a human would**, then collapses it and pops a brand payoff, or holds it under a persistent mark while a sub-line types into the final CTA. Reach for it when "someone is typing this" should be the engine â€” a relatable typed pain â†’ brand, or a standing logo + a typed CTA rail.
</blueprint>

<blueprint id="spatial-pan-stations" roles="Hook, Problem, Product_Intro" duration="7â€“10s">
Pre-placed labeled **stations on one oversized canvas, traversed by a single virtual camera** â€” repeated lateral/diagonal pans centering each station and revealing a callout, landing held on the last. Reach for it for a milestone timeline panned to "us," a connected web of pain stations ending in a tangled knot, or a two-shot concept-decode strip bridged by one lateral pan into a live demo.
</blueprint>

<blueprint id="camera-journey" roles="Benefits, Key_Feature" duration="5.6â€“11.1s">
The real viewport camera is the STORYTELLER â€” a **multi-leg motivated journey** (dive in â†’ a beat fires â†’ travel to the consequence / reposition â†’ landing push) across one continuous world. Two sub-shapes: **(A) action roundtrip** â€” dive to a panel, a click/send fires, the camera swoops to where the consequence renders as element motion; **(B) cursorless flight** â€” pure cinematic 3D flight (motion blur, DoF, tilt-to-flatten), no cursor anywhere. Reach for it when the camera's travel itself tells the causeâ†’effect (or spectacle) story â€” not when it chases a cursor (cursor-ui-demo) or presents one hero device (device-surface-showcase).
</blueprint>

<blueprint id="zoom-out-workspace-reveal" roles="Hook, Benefits" duration="6.8â€“11s">
Open TIGHT on one full-bleed detail â€” a graphic macro or a small UI region â€” let micro-action play in close-up, then **ONE continuous decelerating zoom-out reveals the containing whole** (design-tool workspace / multi-pane agent workspace); the frame locks and element-level payoff carries on. The zoom-out IS the engine â€” the structural inverse of the push-in shapes; no zoom-in anywhere. Reach for it to open on a mystery detail that re-scopes into "this is where it lives," or to land a scale/breadth payoff ("that was one corner of everything it did").
</blueprint>

<blueprint id="constellation-hub" roles="Hook, Social_Proof, CTA" duration="5â€“8s (scatter-drift end card ~2.5s)">
Iconned **nodes spring into a ring around a center**, then resolve on the core â€” a camera push-IN (depth-of-field collapsing onto it), a held hub mark with satellites orbiting it, or a cursor click that COLLAPSES the orbit and springs the product demo out of it (CTA). Reach for it for "it connects everything / one hub" or "sits at the center of your stack." Third finisher (scatter-drift end card): no ring, no camera â€” ~20 icons pop in scattered frame-wide around a serif headline and drift slowly outward under a fully static frame.
</blueprint>

<blueprint id="grid-card-assemble" roles="Key_Feature, Benefits, Social_Proof" duration="3.0â€“10.5s">
N items (tiles / cards / logos / list-lines) **self-assemble in a staggered cascade** into a grid or vertical list and hold; an optional camera zoom-OUT reveals the array inside a vaster whole. Reach for it to enumerate breadth at once â€” a feature grid, an accumulating benefit list, a logo wall, a self-populating live data board, or a streaming field that clears to a payoff line.
</blueprint>

<blueprint id="logo-assemble-lockup" roles="Product_Intro, CTA, Brand_Outro" duration="4.4â€“11s">
A brand mark / wordmark **comes to exist on screen** â€” built from parts (elements assemble/orbit, letters cascade, an outline draws on, a camera pushes through negative space), spring-bloomed whole from zero on a cleared stage, morphed in one unbroken chain out of the preceding phrase, absorbed from a pixel streak, or already assembled and settling as satellites clear â€” and resolves into a centered lockup, optionally extended to a URL/CTA/end card. Reach for it for a wordless premium brand sting, a logo build leading into the final ask, or any brand-outro lockup beat.
</blueprint>

<blueprint id="cursor-ui-demo" roles="Product_Intro, Key_Feature, Hook, Benefits" duration="4.0â€“12.9s">
A visible custom **cursor drives a reconstructed app UI** through clicks/hovers/drags so the screen changes state shot-to-shot, while the camera chases each interaction (or holds a locked static stage while element swaps do the "camera work"). Reach for it for a first cursor-led look at the surface (Product_Intro), one workflow demonstrated end-to-end onto the action button (Key_Feature), an ambient multi-cursor canvas hook, or a demo|text|demo Benefits sandwich.
</blueprint>

<blueprint id="device-surface-showcase" roles="Key_Feature, Product_Intro" duration="5â€“11.3s">
A **device mockup or floating window held as hero** while its screens cycle through a real flow, presented by a camera ranging from a static hold to a continuous 3D push. Mechanic-rich (static tour Â· floating-window push-scroll Â· 3D-hand demo Â· cursorless stepwise-flow Â· showcase-carousel); the stepwise-flow variant widens it to Product_Intro. Reach for it to show a feature experienced *inside its real interface*, or a product introduced by *completing its core loop*.
</blueprint>

<blueprint id="prompt-type-submit-generate" roles="Hook, Product_Intro, Key_Feature, CTA" duration="5.2â€“12s">
The AI-era demo shot: a **prompt/query/command types into a real product input and the machine answers** â€” status theater into a streaming answer / action log / diff cards / chart / generated artifact (full loop), an instant result surface that gets re-queried (search / generated page / preview flip), or the clip cuts at the submit and the ask itself is the show (incl. the install-command CTA end card). Reach for it whenever the beat is "watch me ask, watch it answer" â€” the keyboard drives, not a clicked-through UI (that's cursor-ui-demo) and not bare typed typography (that's typewriter-reveal).
</blueprint>

<blueprint id="agent-progress-theater" roles="Key_Feature" duration="4.2â€“11.6s">
Agent work performed as **working-state theater** â€” a single trigger beat (menu pick, modal click, a scan already running) hands the frame to the machine: loaders spin and status phrases swap while it visibly works, then the receipt cascades in â€” a checklist/findings card whose rows arrive and CHECK OFF (badge flips, strikethroughs, severity pills), or a conversation thread building message-by-message to a camera push-in on the confirmation. Reach for it to dramatize an agent doing multi-step work where the state mutation IS the demo â€” no typed prompt, no cursor-driven workflow, no static enumeration.
</blueprint>

<blueprint id="panel-edit-live-sync" roles="Key_Feature" duration="5.3â€“11.9s">
A bipartite stage â€” an inspector/editor **panel bound to a target surface** â€” where a cursor (or caret) continuously manipulates a control (value scrub, unit/codegen dropdown, easing-handle drag, inline retype) and the coupled surface **updates live in the same beat**; the camera holds or punch-and-returns but never loses the couple. Reach for it when the feature IS live editing/inspection â€” "change this, watch it change" â€” not a click-through workflow (that's `cursor-ui-demo`).
</blueprint>

<blueprint id="transcript-scroll-artifact-reveal" roles="Key_Feature" duration="5â€“11.8s">
The frame travels vertically along one LONG full-bleed content surface â€” an agent transcript, task feed, or analysis document (no device frame) â€” by camera pan or element scroll, **reading the generated work as evidence**; then ONE focal interaction (file-chip click, quote highlight, row expand) pivots into an artifact reveal (workspace zoom-out, spreadsheet scale-up onto highlighted cells, inline panel). Reach for it when "the AI did a lot of work â†’ here's the deliverable" is the beat â€” the traversal is the proof, the artifact is the payoff.
</blueprint>

<blueprint id="dataviz-countup" roles="Hook, Problem, Product_Intro, Key_Feature, Social_Proof" duration="4â€“12s">
Numbers and charts are the hero â€” a **count-up ring/number, trend chart, tilted stat grid** â€” traversed by a camera that pushes THROUGH (or scrolls across) them to land on one hero metric. Reach for it when the data carries the argument: quantify a worsening problem, open confidently on "look at the result," cold-open on one exploding statistic, prove a feature with a dark cursor-scrubbed stat montage, or guest-star a single gauge count-up as one beat inside a type relay.
</blueprint>

<blueprint id="titlecard-reveal" roles="Benefits, Social_Proof, CTA, Product_Intro" duration="3â€“5s">
The calm **breather/landing beat** â€” one clean title or single brand/proof card revealed with exactly ONE restrained move (slide-up crossfade, or wipe-away-to-reveal), then a still hold. Low motion is the payload, not a deficiency. Reach for it for a two-line value title, or a busy open wiped to a clean lockup + a "loved by N+ teams" stat. Also runs as a card CHAIN â€” 2â€“3 near-still monochrome cards seamed by instant hard cuts (CTA end-card stack) or blur-snap handoffs (Product_Intro title prelude), terminating on the held logo; chains run 2â€“3s per card, ~5.5â€“9.5s total.
</blueprint>

<blueprint id="comparison-split" roles="Key_Feature" duration="4â€“6s">
Two paired items of equal weight enter from opposite wings with **mirrored 3D "book-open" tilts** and hold side-by-side, then an inner-edge pill badge spring-pops on each to punctuate. Reach for it for an A/B or "X + Y together" â€” two complementary capabilities weighed at once (not >2 items, not sequential steps).
</blueprint>

<blueprint id="overwhelm-surround" roles="Problem" duration="6â€“9s (clutter-shove variant ~10s)">
Overwhelm by accumulation â€” recognizable surfaces assemble, density-marker icons scatter in, the center one **morphs into the viewer's own avatar**, then elements close in from all sides (surrounded, not zoomed-into). Reach for it when the pain is "you're buried in tools," ending on a claustrophobic crowd. Second resolution (clutter-shove-to-question): the accumulation runs under a slow zoom-out, then a push-in shoves the clutter to the frame edges and a two-part serif question builds in the opened center â€” camera-driven, no avatar.
</blueprint>

<blueprint id="ticker-takeover" roles="Hook, Brand_Outro" duration="5â€“7s">
A typed lead-in + an accent word cycling through options, then a hero **crashes in from off-screen and physically shoves the text aside** â€” a collision, not a fade â€” settling alone. Reach for it when a "could be many things" build should be violently replaced by "this is it."
</blueprint>

<blueprint id="fixed-anchor-cycle" roles="Hook, Benefits, Brand_Outro" duration="6.6â€“11.1s">
One element stays PINNED â€” a wordmark, composer box, or anchor line that enters once and **never moves** â€” while the adjacent region (or the entire surrounding theme) cycles through many discrete states: hard-cut label swaps, a vertical carousel, per-word highlight stepping, or in-place theme morphs, cadence often manipulated (steady stepping or a slowâ†’accelerating flurry), resolving on an emphasis beat into a completed lockup. Reach for it to assert breadth around one fixed identity â€” "everyone says / works everywhere / calling all X" â€” where the anchor's stillness IS the claim.
</blueprint>

<blueprint id="video-text-pivot" roles="Product_Intro, Key_Feature" duration="6â€“8s">
A product video holds center and breathes, then **slides aside to hand its weight to a hero stat**, then both clear and kinetic text types into the vacated center, sealed by a gradient pill. Reach for it for "see the feature â†’ see the impact" where the video must stay visible (slides, never cuts).
</blueprint>

<blueprint id="cta-morph-press" roles="CTA, Hook" duration="4â€“6s (Hook opener 5â€“7.5s)">
A resting brand mark **condenses at the same center into a brighter CTA**, then a cursor arrives and lands a human-aimed click with feedback. Reach for it for a focused "click here" sign-off that walks the eye from identity to action â€” no spatial set, no multi-step UI. Role-widened to Hook: the same machinery as an OPENER â€” a lone widget (pill/chip) on a flat field morphs in place (pillâ†’menu, chipâ†’prompt card), performs its payload, then vanishes to a typed closing title.
</blueprint>
</blueprints>

## Role â†’ blueprint menu

A **SOFT** menu: story truth comes first. Story-design reaches in **when the product's own beat calls for that shape** â€” it suggests a proven shape, it never dictates which beats exist. Each role has 4â€“11 options; if none fits the beat, compose freely (the menu is not a checklist). Each line is the **trigger** that should make you reach for that blueprint.

Roles here map 1:1 to the storyboard frame `type` enum: **Hook**=`hook` Â· **Problem**=`pain_point` Â· **Product_Intro**=`product_intro` Â· **Key_Feature**=`feature_showcase` Â· **Benefits**=`benefit_highlight` Â· **Social_Proof**=`social_proof` Â· **CTA**=`cta` Â· **Brand_Outro**=`branding`.

**Hook**

- `kinetic-type-beats` â€” a punchy rhetorical line / "you keep doing X" callout where the in-place word-swap is the joke, an escalating multi-beat statement landing a spring-pop payoff, word beats resolving into a logo reveal, or a centered beat triptych (a beat may be a non-text element).
- `typewriter-reveal` â€” type a relatable line, collapse it, pop the brand (logo or product-UI) â€” "here's the everyday pain, now here's us."
- `spatial-pan-stations` â€” a timeline of milestones panned to the present ("evolution leading up to us").
- `constellation-hub` â€” a constellation of tools/nodes + a camera push-in ("it connects everything").
- `cta-morph-press` â€” a lone widget on a flat field morphs in place (pillâ†’menu, chipâ†’prompt card), performs, then vanishes to a typed title ("one widget doing one thing" opener).
- `ticker-takeover` â€” a cycling accent word ("could be X, or Yâ€¦") violently replaced by a hero crashing in from off-screen.
- `fixed-anchor-cycle` â€” a static lead line holds while an accent line carousels through an audience/option roll-call beneath it, then clears into statement beats landing the brand line.
- `prompt-type-submit-generate` â€” "watch me ask": a typed headline â†’ one push-in onto the product's input â†’ the prompt types and the clip ends at the submit; or the whole demo loop runs and a second command starts before the cut.
- `cursor-ui-demo` â€” an ambient multi-cursor workshop: labeled teammate cursors work a design canvas live (grab-drag-drop, recolor on drop) while a headline builds over the demo â€” the live workshop itself is the hook.
- `dataviz-countup` â€” a cold-open counter burst: icons puncture in clustered at center, one dramatic statistic explodes upward in size as the icons fling outward to their marks, closed by a slow lean-in.
- `zoom-out-workspace-reveal` â€” a full-bleed graphic mystery (blob / blossom / macro) resolved by one unbroken decelerating pull-back through nesting levels into the design-tool workspace that made it; canvas keeps animating after the lock.

**Problem**

- `kinetic-type-beats` â€” 3â€“5 short pain statements each landing alone on a bare canvas, or a question/hook phrase relay scale-popping through center (optionally resolving on a product surface as an element move).
- `spatial-pan-stations` â€” pan a connected web of pain "stations" ending in a tangled knot.
- `dataviz-countup` â€” a count-up ring / chart / stat grid pushed-through to dramatize a worsening or large problem.
- `overwhelm-surround` â€” recognizable tools that morph into the viewer, then task bubbles close in from all sides ("you're buried").

**Product_Intro**

- `kinetic-type-beats` â€” "Introducingâ€¦" hard-cut name-drop resolving on the brand name/logo; also a fixed headline with one swapping word-slot, a word-by-word run with per-hero-word effect payoffs, or an anchored wordmark that transforms out.
- `logo-assemble-lockup` â€” a wordless premium brand sting (elements pulse/orbit and assemble around the mark).
- `cursor-ui-demo` â€” first look at the product surface; a cursor sweeps in to introduce the app.
- `dataviz-countup` â€” hard-cut into a data-viz card grid, camera scrolls to a glowing hero metric + a kinetic tagline.
- `video-text-pivot` â€” a product video that slides aside to hand its weight to a hero stat, then yields the center to kinetic impact text.
- `spatial-pan-stations` â€” a two-shot strip bridged by ONE lateral pan: a static phrase's accent word 3D-flap-decodes (the concept lands), then the camera pans with parallax into a live cursor-typing demo.
- `prompt-type-submit-generate` â€” the first look at the product is its composer or search bar â€” a long prompt (or short query) types with attachments / dropdown picks / live autocomplete, steering to the confirming control.
- `device-surface-showcase` â€” a cursorless end-to-end flow (setup/auth â†’ action â†’ success) completed inside the held surface, bookended by title cards.
- `titlecard-reveal` â€” a three-beat dark title prelude (logo pop â†’ name+version append â†’ tagline card) chained by blur-snap handoffs before any product UI.

**Key_Feature**

- `grid-card-assemble` â€” a labeled feature tile/pill grid that self-assembles (or glass cards revealed by a camera zoom-out; or a live-populating data board â€” skeleton fills, tethered cards, post-assembly status flips).
- `cursor-ui-demo` â€” a specific multi-step workflow demonstrated end-to-end, landing on the action button/result.
- `device-surface-showcase` â€” a device/window hero whose screens cycle (static tour Â· floating-window push-scroll Â· 3D-hand demo).
- `comparison-split` â€” two paired capabilities side-by-side with mirrored book-open tilts (an A/B / "X + Y together").
- `video-text-pivot` â€” a feature clip that slides aside to a frame-filling metric, then a typographic impact line.
- `dataviz-countup` â€” dark-scrub-montage: kinetic headline beats cut-stitched with self-drawing charts and a cursor-scrubbed dashboard (`chart-scrub-readout`).
- `prompt-type-submit-generate` â€” the capability as one promptâ†’response round trip: submit into thinking states, then a streaming answer, action log, diff cards, chart, or instant generated artifact.
- `agent-progress-theater` â€” the feature is the agent WORKING (plan / scan / fix / automation): loader + status theater resolving into a checklist that checks off, or a thread that builds to a confirmation payoff.
- `panel-edit-live-sync` â€” an inspector/editor panel edit-syncs a bound target live (scrub â†’ it rotates, retype â†’ it resizes, pick â†’ it converts); for features whose value prop is the live coupling itself.
- `camera-journey` â€” a cursorless cinematic 3D flight over the product surface â€” motion blur, depth-of-field, tilt-to-flatten â€” landing violently on the CTA / hero card (sub-shape B).
- `transcript-scroll-artifact-reveal` â€” a long transcript/feed/document traversed vertically as evidence of generated work, then one interaction pivots into the artifact ("it did all this â†’ here's the deliverable").

**Benefits**

- `kinetic-type-beats` â€” a rapid-fire staccato montage of 8â€“12 short value phrases, or a slow 2â€“4-statement relay each held ~1.5s+.
- `grid-card-assemble` â€” a vertical benefit list that accumulates, steps, or streams past a focal slot, optionally clearing to a payoff line.
- `titlecard-reveal` â€” a calm two-line value title card (a breather/stillness beat).
- `camera-journey` â€” a small action in one panel pays off in another region, and a real camera swoop physically connects cause to effect (sub-shape A).
- `zoom-out-workspace-reveal` â€” micro-actions in extreme close-up on one small UI region, then one fast decelerating zoom-out reveals the huge multi-pane agent workspace; the wide holds while the deliverable payoff completes.
- `fixed-anchor-cycle` â€” one product surface pinned dead-center while its whole theme re-skins per beat ("the same prompt, in every tool").
- `cursor-ui-demo` â€” the demo|text|demo sandwich: two static-stage demo beats bridged through a full-screen kinetic/title interlude and back.

**Social_Proof**

- `constellation-hub` â€” product mark as the hub, partner logos orbiting it ("works with your stack").
- `grid-card-assemble` â€” a logo wall that builds then pulls back to reveal a vast ecosystem.
- `titlecard-reveal` â€” wipe a busy open away to a clean brand lockup + a "loved by N+ teams" stat.
- `constellation-hub` â€” scatter-drift end card: ~20 app icons pop in frame-wide around a serif headline and drift outward under a static frame ("connects to thousands of apps").
- `dataviz-countup` â€” one radial-gauge count-up instrument embedded as a single beat inside a kinetic-type relay.

**CTA**

- `kinetic-type-beats` â€” a punchy closing line (or short value stack) snapping beat-by-beat onto the logo/URL, or a 3â€“5-beat chain where each beat carries its own kinetic gag before the logo forms.
- `logo-assemble-lockup` â€” a logo build â†’ camera push-through into the final URL/CTA verb.
- `cta-morph-press` â€” a brand mark that condenses into the CTA at one center, then a cursor lands a human-aimed click.
- `titlecard-reveal` â€” a monochrome end-card chain (statement â†’ CTA line â†’ wordmark/logo) seamed by instant hard cuts, ending on the logo held to the final frame.
- `constellation-hub` â€” orbit-collapse: category icons drift around an empty central CTA, a cursor click implodes the orbit toward the click point, and the product demo springs OUT of the collapse.
- `prompt-type-submit-generate` â€” the install-command end card: headline demotes, a terminal pill springs in, the command types and holds with a blinking cursor.

**Brand_Outro**

- `kinetic-type-beats` â€” a rapid verb barrage resolving on the brand's one defining word, or a relaxed full-frame beat relay terminating in a long-held URL end card.
- `typewriter-reveal` â€” a persistent brand mark with a typed/swapping CTA rail beneath it.
- `logo-assemble-lockup` â€” feature/UI elements clear the stage and the lockup draws itself in.
- `ticker-takeover` â€” options cycle, then the brand mark crashes in and owns the frame.
- `fixed-anchor-cycle` â€” the wordmark pins while praise quotes / tagline highlights cycle beside it (optionally accelerating), resolving into the finished lockup.

> Coverage: every role has â‰¥2 options; every blueprint serves â‰¥1 role. `kinetic-type-beats` is the workhorse (6 roles); `dataviz-countup` now spans 5; `device-surface-showcase` (once role-narrow) now also serves Product_Intro via the mined stepwise-flow variant. Five shapes â€” `comparison-split`, `overwhelm-surround`, `ticker-takeover`, `video-text-pivot`, `cta-morph-press` â€” were added from the hyperframes-animation blueprints; seven more â€” `prompt-type-submit-generate`, `agent-progress-theater`, `panel-edit-live-sync`, `camera-journey`, `transcript-scroll-artifact-reveal`, `zoom-out-workspace-reveal`, `fixed-anchor-cycle` â€” were mined from the golden-clip corpus.

## Picking guidance

1. Find the frame's **role** in the menu above; pick the blueprint whose **shape fits this beat** (story may already have named a candidate id â€” confirm or override). If two fit, prefer the one whose motions are closer to your plan.
2. Open `blueprints/<id>.md` â€” read its time-coded template, `[slots]`, and named **signature move**.
3. Choose a posture â€” **Reproduce** (slots map cleanly), **Adapt** (structure fits, content/surface differs; keep the signature move), or **Compose** (nothing fits â†’ build from the motion vocabulary). The _how_ of writing each â€” what to keep/change, the per-frame fields â€” is `visual-design.md`'s job; defer to it.
4. If nothing in the menu fits the beat, **compose** from the motion vocabulary in `motion-language.md` â€” still pace the reveals to the VO across the shot. Don't force a wrong blueprint.

## Motion coverage

Every recurring move in the golden vocabulary is backed by this skill's local `rules/` â€” including five added to round out the corpus: `depth-of-field-blur`, `motion-blur-streak`, `depth-scatter-assemble`, `spring-pop-entrance` (the canonical entrance pop, distinct from the click/press `press-release-spring`), and `ambient-glow-bloom`. Each blueprint's `rule mapping` cites the real rule.

Variant provenance (`from <shape-name>`) names the mined golden shape a variant was reverse-engineered from; the case-level golden map lives with the c2v-bench mining reports (maintainers only â€” consuming agents need only the shape names).

One genuine out-of-scope special remains: `device-surface-showcase`'s **3D-hand gesture-input + WebGL bloom/portal** needs R3F/Three.js + WebGL â€” a heavier capability than the rule library. Use it sparingly, or pick a simpler `device-surface-showcase` variant.
