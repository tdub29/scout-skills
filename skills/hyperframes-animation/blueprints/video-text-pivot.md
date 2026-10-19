# video-text-pivot â€” Video â†’ Text Pivot

**intent**: A product video holds center and claims attention, then slides aside to hand its weight to a hero stat in the space it vacates, then both clear and kinetic text types into the center â€” accent words carrying the meaning the video used to carry â€” sealed by a gradient pill. The arc is "show â†’ yield â†’ pivot â†’ stamp," and each handoff pairs an exit with a same-anchor entrance so two beats read, not four.

**roles served**

- Product_Intro (from `metric-video-text-pivot`): when the open is "see the feature" then "see the impact" and the `[product video]` must stay visible through the stat reveal â€” it slides, it doesn't cut.
- Key_Feature: a feature clip that yields to a frame-filling metric and a typographic impact line.

**duration**: 6â€“8s

**shot structure** (a `[bg]` canvas; one `[product video]` as a real muted `.mp4` clip, a hero stat, then kinetic text â€” each pair shares a screen anchor so the handoff reads as a weight-transfer)

- **Scene 1 (0.0â€“~1.6s) â€” the video shows.** The `[product video]` lands centered on a smooth scale-up and breathes (a small y-bob), claiming full attention. Camera static.
- **Scene 2 (~1.6â€“3.2s) â€” yield + stat (signature move).** The video SLIDES aside (x + scale down) **into the very space** the `[hero stat]` now fills as the stat pops in with 3D-depth type â€” one weight-transfer reading as a single event, not two. The stat breathes within this window.
- **Scene 3 (~3.2â€“5.0s) â€” pivot to text.** Both video and stat clear out and kinetic `[impact text]` TYPES into the vacated center, character by character; its `[accent words]` carry the meaning the video used to carry.
- **Scene 4 (~5.0â€“end) â€” stamp.** A gradient `[pill]` snaps shut around the closing line (`scaleX` 0â†’1), its glow halo resolving a beat behind so the silhouette reads before the bloom â€” sealing the statement as one graphic. Holds.

**motion vocabulary**: video scale-in + small breath; weight-transfer slide (video x + scale-down handing off to the stat at the same anchor); 3D-depth stat type; character-stream typing; gradient pill scaleX-snap; glow-halo bloom trailing the silhouette.

**rule mapping**

- video entrance (smooth) and the weight-transfer slide â†’ `gsap-effects` (scale/opacity then x + scale on a long-tail `power3`); the video itself is a muted `<video class="clip">` direct child of the root
- hero stat's frame-filling 3D type â†’ `3d-text-depth-layers` (static-depth variation â€” layers built at setup, no cascade fighting the entry)
- the same-anchor video-exit â†” stat-entry handoff (if treated as a morph) â†’ `scale-swap-transition` (shared center)
- character-by-character impact typing through segmented spans â†’ `dynamic-content-sequencing` (clean character stream) or `discrete-text-sequence`
- pill `scaleX` snap + trailing glow halo â†’ `gsap-effects` (scaleX) + `ambient-glow-bloom` (the halo, resolving a beat behind)
- video / stat breath within their windows â†’ `sine-wave-loop` (low-amplitude register â€” subtle jitter, gated to each element's window, never a forever loop)

**camera modifier**: camera-static â€” all motion is element-space (the video translates), so the "pivot" is the elements moving, not a camera.
