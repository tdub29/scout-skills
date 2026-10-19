# overwhelm-surround â€” Overwhelm / Close-In

**intent**: Convey overwhelm by accumulation. Recognizable subjects assemble, density markers scatter in to amplify "look how much," then the central subject morphs into the viewer's own avatar and elements close in from ALL sides â€” the frame feels surrounded, not zoomed-into. The emotional arc is recognition â†’ claustrophobia.

**roles served**

- Problem (from `problem-mockup-overwhelm`): when the problem beat must first show "too many tools / too much surface area" and then put **the viewer inside it** â€” a literal swap of subject (product â†’ person) followed by a closing-in that feels invasive. Reach for it when the pain is "you're buried," not "this metric is bad" (that's `dataviz-countup`).
- Problem (from `desktop-clutter-accumulation`): when the overwhelm is a **workspace**, not a tool
  count â€” live windows, stickies, and alert toasts pile up until the frame is chaotically full, and
  the beat resolves not by closing in but by shoving the clutter aside and asking the question.
  Reach for this variant when the pain lands on words ("how can you Xâ€¦ when you spend months on
  Y?"), not on a surrounded avatar.

**duration**: 6â€“9s (clutter-shove-to-question variant ~10s)

**shot structure** (a `[bg]` canvas; recognizable surfaces first, the viewer's avatar revealed underneath, then a radial crowd)

- **Scene 1 (0.0â€“~1.6s) â€” recognizable assembly.** Three `[product mockups / surfaces]` assemble into something the viewer knows â€” staggered scale-in, the **center** one full-size, the two flanks smaller (~0.86). Each rides a low-amplitude float so they feel like live context, not a static collage. Camera static.
- **Scene 2 (~1.6â€“3.0s) â€” density amplifies.** `[platform icons / logos]` scatter in around the mockups (staggered), used purely as **density markers** â€” "look how much surface area," not animated dials.
- **Scene 3 (~3.0â€“4.6s) â€” the morph (signature move).** The CENTER mockup MORPHS: its content fades out, the container reshapes, and the viewer's `[avatar]` is revealed **underneath** â€” a literal swap of subject, product â†’ person.
- **Scene 4 (~4.6â€“end) â€” close-in.** `[task bubbles / demands]` close in from ALL sides toward the avatar (radial staggered entry). The avatar **stays put** while the bubbles invade â€” the claustrophobia comes from being surrounded, never from a camera push. Holds on the crowded state.
- **Variant â€” clutter-shove-to-question** (replaces Scenes 3â€“4 and
  inverts the camera contract â€” see modifier): accumulation runs under a **slow steady zoom-out** â€”
  `[sticky notes]` bounce in springy, `[dashboard / editor windows]` pop and slide up, a stack of
  `[alert toasts]` slides in at one edge, inner content keeps typing / log-scrolling as live density,
  windows overlap until the frame is chaotically full. The camera then REVERSES into a quick
  push-in that **shoves the clutter to the frame edges**, opening central negative space where a
  `[two-part serif question]` builds word-by-word (line 1 swaps in place to line 2); a `[cursor]`
  glides in from off-frame and comes to rest under the text; a very slow forward creep and hold.
  No morph, no avatar â€” the question is the payoff.

**motion vocabulary**: staggered scale-in assembly; resting-scale-preserving low float; density-marker icon scatter; content-fade â†’ container-reshape â†’ reveal-anchor-beneath morph; radial close-in entry from all compass points; held crowded end-state. Clutter-shove variant: slow steady zoom-out under accumulation; reverse quick push-in; clutter
shoved to frame edges opening center negative space; continuous live typing / log scroll inside
windows as ambient density; toast-stack slide-in; word-by-word serif build with in-place line swap;
cursor glide-to-rest; very slow forward creep + hold.

**rule mapping**

- staggered mockup + icon entries (smooth settle onto their resting scale) â†’ `spring-pop-entrance` (smooth-settle register) backed by `gsap-effects`
- platform icons as density markers (positions pre-baked, scale/opacity only â€” NOT internal-parts animation) â†’ `svg-icon-enrichment` (its DOM contract only)
- center mockup â†’ avatar morph (HF forbids `width`/`height` tweens â†’ drive the reshape on `scaleX`/`scaleY`, anchor = the avatar layer rendered beneath) â†’ `card-morph-anchor`
- radial bubble close-in (positions baked once via `cos`/`sin`, staggered entry) â†’ `gsap-effects` (radial layout) + `spring-pop-entrance` (per-bubble arrival)
- low-amplitude float on background mockups/icons â†’ `sine-wave-loop` (low-amplitude register â€” subtle jitter that composes onto each element's resting scale, never a `fromTo` yoyo that re-tweens to its start)
- (variant) zoom-out under accumulation â†’ quick push-in â†’ slow forward creep â†’ `multi-phase-camera`
  (pull-back / push / drift as sequential phases on one world wrapper; counter-translate math in
  `viewport-change`)
- (variant) clutter shoved to the edges as the push-in lands â†’ `center-outward-expansion` (outward
  vectors to edge resting positions), fired at the same timeline position as the camera push so the
  shove reads as CAUSED by it (`reactive-displacement` register)
- (variant) word-by-word serif question build â†’ `gsap-effects` (staggered word reveal); the
  in-place line-1 â†’ line-2 swap â†’ `discrete-text-sequence`
- (variant) live typing inside windows â†’ `gsap-effects` (typewriter); the continuous inner
  log-scroll â€” composition: looping content translateY via `gsap-effects` (masked)
- (variant) cursor glide-in coming to rest â†’ `cursor-click-ripple` (approach portion only â€” no click)

**camera modifier**: camera-static â€” the close-in must read as the world crowding the subject, so the frame holds; a push-in would convert "surrounded" into "zoomed-into" and kill the claustrophobia. The clutter-shove-to-question variant is the sanctioned exception: there the camera IS the
storyteller (zoom-out â†” push-in via `multi-phase-camera`), and the claustrophobia comes from
accumulation, not surround â€” never mix the two resolutions in one shot.
