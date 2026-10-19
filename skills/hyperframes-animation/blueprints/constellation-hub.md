# constellation-hub â€” Constellation / Hub + Satellites

**intent**: Labeled/iconned nodes spring into a ring/cluster around a center, then the shot resolves on the core â€” either by pushing the camera INTO the center (depth-of-field collapsing onto it) or by holding a hub mark while the satellites ORBIT it; the "everything connects to / sits around one center" beat.

**roles served**

- Hook (from `hook-cluster-push-in`): a constellation of tool/app nodes springs into a wide ring, then a sustained camera push-in with depth-of-field resolves on the inner core â€” "it connects everything / one hub for all your tools."
- Social_Proof (from `social-proof-orbit-ecosystem`): the product brand mark lands as the center hub and partner logos spring onto a ring and revolve around it â€” "plugs into / sits at the center of your stack."
- CTA (from `cta-orbit-collapse`): the ring resolves by COLLAPSE rather than a push-in â€” category icons drift around an empty central CTA, a cursor click implodes the orbit toward the click point, and the product demo springs OUT of that collapse as the answer (scope â†’ choice â†’ consequence â†’ product).
- Social_Proof (from `proof-logo-chain`): a persistent center logo accrues proofs â€” its wordmark decodes, a claim ticker swaps, the logo glides to center, then avatars cascade into orbit with drawn connectors while partner logos scroll the bottom strip; four claims read as one statement.
- Social_Proof (from `scatter-drift-finisher`): the ecosystem beat as a
  static END CARD â€” a two-line serif `[headline]` is the center (no hub mark, no ring), `[~20 app
icons]` pop in scattered frame-wide in a quick stagger, then keep drifting very slowly OUTWARD
  to the end. "Connects to thousands of apps" said with count and spread, not geometry.

**duration**: 5â€“8s (Hook 5â€“6s Â· Social_Proof 5â€“8s Â· CTA orbit-collapse ~6s Â· Social_Proof
scatter-drift end card ~2.5s as a closing beat)

**shot structure**

Consolidated template â€” nodes ring a center, then one of two finishers resolves on the core.

- Scene 1 (0.0â€“~1.5s): `[bg]` (dark/space field, optionally slow-drifting diffused gradient blobs). `[primary nodes]` (circles carrying `[icon]` + label) SPRING-POP in (scale 0â†’1, ~1.15 elastic overshoot, staggered) arranged in a wide ring/cluster around an empty or marked center `[hub]`.
- Scene 2 (~0.7â€“2.5s, overlapping): smaller `[secondary nodes]` (platform / partner-logo chips) pop in staggered with the same elastic spring, filling the gaps; optional thin `[accent]` connector lines / orbit ring draw from hubâ†’nodes. Camera holds.
- Scene 3 (~2.5â€“Xs, the resolve): see finisher variant below; lands and HOLDS on the magnified / orbited center to the end.

- Variant â€” Hook (push-in finisher): from Scene 3, a continuous smooth CAMERA PUSH-IN toward the center inner cluster â€” inner nodes scale up and stay sharp while outer nodes are pushed toward the edges and progressively BLUR (depth-of-field), background scales up smoothly; holds magnified on the core.
- Variant â€” Social_Proof (orbit finisher): the center `[brand mark]` snaps in via a quick 3D rotate that decelerates and settles; a thin `[accent]` orbit ring draws around it; `[N partner badges]` spring onto the ring (staggered overshoot) and revolve CLOCKWISE while staying upright, under a continuous slow camera ZOOM-OUT (ecosystem reveal).
- Variant â€” Social_Proof (optional type-push-through opener, prepended before Scene 1): centered `[headline]` types/slides in with a huge transparent-fill OUTLINE copy of the same words behind it; the outline text scales up exponentially toward camera (high-speed dolly / push-through), breaches the frame, then HARD-CUTS to the hub bg of Scene 1.
- Variant â€” Social_Proof (scatter-drift finisher, no ring): the center is a two-line serif
  `[headline]` building in place (not a mark); `[~20 app icons]` pop in SCATTERED across the whole
  frame in a quick stagger â€” no ring geometry, no connectors â€” then sustain a very slow outward
  drift to the end. Camera fully static: no push-in, no zoom-out; the "everything around one
  center" reads from the drift vectors pointing away from the headline. Often chained as the end
  card of a preceding UI beat (the prior card dissolves into it).

**motion vocabulary**: staggered elastic spring-pop node entrances (~1.15 overshoot); slow gradient-blob drift; connector-line / orbit-ring draw-on; 3D snap-rotate-settle on the hub mark; continuous camera push-in (inner sharp, outer depth-of-field blur, bg scale-up); clockwise orbital revolve of upright badges; continuous slow camera zoom-out (ecosystem reveal); optional outline-text push-through dolly entry. Scatter-drift finisher: frame-wide scattered icon pop-in (staggered, no ring); sustained slow
outward icon drift; in-place two-line serif headline build; static-frame hold to the end.

**rule mapping** (motion verb â†’ `rules/<id>.md`)

- staggered spring-pop node entrances â†’ `spring-pop-entrance` (elastic overshoot) + `gsap-effects` (stagger recipe); 3D-flip-in flavor â†’ `orbit-3d-entry`
- ring / cluster layout of nodes around a center â†’ `avatar-cloud-network` (nodes on an elliptical ring + SVG lines to a center)
- icons on the nodes â†’ `svg-icon-enrichment`
- connector lines hubâ†’node â†’ `svg-path-draw`
- orbit-ring draw-on â†’ `svg-path-draw`
- slow gradient-blob drift â†’ `sine-wave-loop` (idle looped drift)
- 3D snap-rotate-settle on hub mark â†’ `orbit-3d-entry` (3D-flip entry); technique CSS-3D
- clockwise orbital revolve of upright badges â†’ `orbit-3d-entry` (continuous elliptical orbit); technique MotionPath
- camera push-in toward center â†’ `multi-phase-camera` (PUSH-in) + `coordinate-target-zoom` (target the core)
- background scale-up during push-in â†’ `multi-phase-camera`
- continuous slow zoom-out (ecosystem reveal) â†’ `multi-phase-camera` (pull-back) / `coordinate-target-zoom`
- outline-text push-through dolly opener (Social_Proof) â†’ `3d-text-depth-layers` (outline copy behind) + `multi-phase-camera` (push-through)
- depth-of-field blur on outer nodes during push-in â†’ `depth-of-field-blur` (progressive DOF/focus-falloff blur on the off-center outer nodes while the inner core stays sharp)
- frame-wide scattered icon pop-in (no ring) â†’ `spring-pop-entrance` (staggered group) +
  `gsap-effects` (stagger recipe); positions pre-baked scattered â€” NOT `avatar-cloud-network`'s
  elliptical ring
- sustained slow outward icon drift â†’ `center-outward-expansion` (outward vectors, slow sustained
  register â€” drift targets sit slightly past the pop-in positions)
- in-place serif headline build â†’ `gsap-effects` (staggered line/word reveal)

**camera modifier**: push-in-with-DOF (Hook) â€” `multi-phase-camera` PUSH-in targeted via `coordinate-target-zoom` onto the core; the focus-falloff blur half of it is backed by `depth-of-field-blur`. Orbit finisher (Social_Proof) â€” slow continuous zoom-out via `multi-phase-camera` (pull-back) while satellites revolve. Scatter-drift finisher (Social_Proof end card) â€” none: the frame never moves; the outward drift
is element-level.
