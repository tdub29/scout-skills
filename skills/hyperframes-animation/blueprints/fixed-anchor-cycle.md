# fixed-anchor-cycle â€” Fixed Anchor, Cycling World

**intent**: One element is PINNED â€” a wordmark, a composer box, an anchor line that enters once and never moves again â€” while the adjacent region (or the entire surrounding theme) cycles through many discrete states around it, cadence often manipulated (steady stepping, a fast carousel, or a slowâ†’accelerating flurry), resolving on an emphasis beat into a completed lockup or a muted freeze. The stillness of the anchor IS the claim: everything changes, this stays. Distinct from `kinetic-type-beats` sub-shape A, where a word-slot inside a centered line swaps and the sentence itself is the subject â€” there the anchor is a sentence frame on a bare type field; here the anchor is the PRODUCT identity and what cycles around it can be non-text (whole theme skins, chrome/logo swaps, textured label chips, a carousel list), the cycle asserts breadth ("everyone says / works everywhere / calling all X"), and the resolve completes the anchor into a lockup. Distinct from `ticker-takeover`, whose cycle ends in a collision â€” a hero crashes in and shoves the text aside; here nothing ever collides with the anchor: the cycle stops, and a final element quietly joins it.

**roles served**

- Brand_Outro (from `static-anchor-rapid-text-swaps`): when the sign-off is the brand name sitting immovable while praise quotes / tagline words cycle beside or beneath it â€” steady per-word highlight stepping, or a hard-cut chip flurry that accelerates â€” landing on the finished lockup ("bolt.new / prompt, run, edit, deploy / enjoy."; "Opus 4.6 by ANTHROP\C").
- Benefits: when "works everywhere" is shown literally â€” one product surface (a prompt composer with one verbatim string) pinned dead-center while its ENTIRE shell morphs in place through N product themes (background, typography, radii, chrome, logos all crossfading at once), ending in a washed-out freeze.
- Hook: when the opener is a roll-call â€” a static anchor line holds while an accent-colored line beneath it runs as a fast vertical carousel through an audience/option list, then the block clears into follow-up statement beats that land the brand line.

**duration**: 6.6â€“11.1s (Benefits shortest ~6.6s at 4 theme beats; Brand_Outro ~9â€“9.4s; Hook longest ~11s when the anchor-cycle block hands off to follow-up statement beats). The cycle engine itself occupies ~3â€“5s regardless of role.

**shot structure** (flat static frame â€” camera locked in every member; a `[bg]` field, solid or subtly drifting; two folded sub-shapes â€” **(A) adjacent-region cycle**: the anchor holds and a neighboring slot swaps through N states; **(B) whole-context morph**: the anchor holds and everything AROUND it re-skins in place)

- **Scene 1 (0.0â€“~2.0s) â€” the anchor lands and PINS.** The `[anchor: wordmark / product name / composer box / lead line]` enters once â€” fade/scale-in centered, word-by-word build, or already present at frame one â€” at a fixed position it will hold for the entire clip. Zero movement from here on: no drift, no breathe, no re-layout. If the anchor is a UI surface (sub-shape B), it carries a `[verbatim string]` with a blinking cursor.

- **Scene 2 (~2.0sâ€“~70% of runtime) â€” the cycle engine (signature move).** The world changes around the unmoved anchor. Choose by sub-shape:
  - **Sub-shape A (adjacent-region cycle)**: a region beside/beneath the anchor steps through N discrete states â€” pick ONE swap mechanic and ONE cadence:
    - _swap mechanics_: instant hard-cut label replacement (a `[chip / tape label]` slaps over the old one, texture/highlight shifting slightly, chip width re-fitting each `[phrase]` â€” growing away from the anchor, never over it); sequential per-word highlight stepping (one word of the `[tagline]` snaps bright/bold while the rest sits dim grey, the highlight walking the line); or a fast vertical carousel (each `[list item]` slide/fades through the accent slot ~0.5s/phrase).
    - _cadences_: steady stepping (~0.5â€“1s/state), or **slowâ†’accelerating flurry** â€” ~1s beats compressing to ~0.15â€“0.3s per swap, breadth escalating into a blur of states (12â€“16 states read as "everyone"; 3â€“8 read as a roll-call).
    - Geometry law: the cycling region NEVER overlaps, touches, or displaces the anchor; size the layout so the longest state still fits inside the frame with clear margins.
  - **Sub-shape B (whole-context morph)**: at ~1.3s intervals the entire theme â€” `[bg color]`, typography, corner radii, toolbar icons, footer `[brand logos]`, contextual lines â€” morphs in place via quick (~0.3s) crossfades through N `[product skins]`, every property blending simultaneously. No hard cuts, no wipes; the anchor's content string is identical in every skin (chrome details like a `> ` prefix may adapt per skin).

- **Scene 3 (~70â€“85%) â€” the emphasis beat.** The cycle resolves â€” it does not just stop:
  - _Variant â€” Brand_Outro (highlight stepping)_: the whole `[tagline]` snaps solid bright at once â€” full-line illumination after the per-word walk.
  - _Variant â€” Brand_Outro (flurry)_: the flurry halts and HOLDS on the `[longest / weightiest phrase]` â€” a beat of stillness after acceleration.
  - _Variant â€” Benefits (theme morph)_: the final beat mutes â€” a faint `[dot-grid]` fades in across the background while the UI drops to low opacity, a washed-out blueprint freeze.
  - _Variant â€” Hook (carousel)_: the anchor block clears, handing off to 1â€“3 centered word-by-word statement beats (kinetic-type-beats territory) that carry toward the close.

- **Scene 4 (final beat â†’ end) â€” lockup completion and HOLD.** A final element joins the still-unmoved anchor and the finished composition holds static to the end: a `[closing word]` drops in below, aligned to the last cycled state ("enjoy."); the chip vanishes on a hard cut and the `[brand sign-off]` appears beside the anchor on a shared baseline ("by ANTHROP\C"); or the final `[brand line]` builds word-by-word dead-center and holds ("with Copilot."). Long static hold â€” the lockup is the payoff, give it 20â€“30% of the runtime.

**motion vocabulary**: anchor fade/scale-in entrance; permanently pinned anchor (zero movement, no idle breathe); instant hard-cut label/chip replacement (slap-over with subtle texture/highlight shift); chip width resize-to-fit per phrase (grows away from the anchor); sequential per-word highlight stepping through a line; dim-to-grey line state; whole-line illumination snap; fast vertical carousel slide/fade of one line under a static line; cadence acceleration (slow ~1s beats into a ~0.15â€“0.3s flurry); hold-on-longest-phrase emphasis beat; in-place theme morph crossfade (~0.3s) blending background/fonts/radii/icons simultaneously; per-beat chrome/logo swap; blinking text cursor; contextual line appearing/disappearing across beats; dot-grid backdrop fade-in; global opacity washout; end freeze; word-by-word phrase build; block clear between scenes; drop-in entrance of a final word; hard cut to final lockup; long static hold.

**rule mapping**

- instant hard-cut chip/label/phrase swaps at time thresholds; per-word highlight stepping (color/weight state swaps); dim-line â†’ full-line illumination snap; per-state chip width set (a per-state layout property, set discretely â€” never tweened) â†’ `discrete-text-sequence`
- fast vertical carousel of the accent line under the static anchor (slide/fade stepped swaps in a masked slot) â†’ `vertical-spring-ticker` (its footer-reveal step unused â€” Scene 4's lockup takes its place)
- per-phrase state windows computed from a script of N states (praise quotes, audience list, theme beats) â†’ `dynamic-content-sequencing` (Accelerating cadence â€” for the flurry, pre-compute the beat array with shrinking `hold` values, geometric decay over the state list)
- word-by-word phrase builds (anchor line, follow-up statements, final brand line) â†’ `dynamic-content-sequencing` + `waterfall-entry` (or `kinetic-beat-slam` when the statements should land percussively)
- anchor entrance fade/scale-in; drop-in of the final closing word â†’ `spring-pop-entrance` (restrained overshoot â€” the register here is editorial, not bouncy)
- blinking cursor in the pinned composer â†’ `context-sensitive-cursor` (color adapts per theme skin at segment boundaries)
- whole-context theme morph â†’ `theme-crossfade-morph` (N pre-styled full-scene layers stacked at the same geometry, opacity-crossfaded, the shared anchor string rendered once on top); the composer shell's radius/surface component alone â†’ `card-morph-anchor`
- subtly drifting background field beneath the cycle â†’ `sine-wave-loop` (bounded drift; the anchor itself gets none)
- dot-grid fade-in + global opacity washout freeze; long static hold â†’ `gsap-effects` (plain opacity tweens) / static hold (no rule needed)

**camera modifier**: none â€” every member is fully camera-static; the cycle is the only motion, and the pinned anchor's stillness is load-bearing. Do not add a push-in "for energy"; it would break the anchor contract.
