# ticker-takeover â€” Ticker Displace / Takeover

**intent**: A context phrase types in, an accent word cycles through options like a slot-machine to suggest "this could be many things," then a hero CRASHES in from off-screen and physically shoves the text aside â€” "actually, this is what it is." A collision, not a fade.

**roles served**

- Hook (from `takeover-ticker-displace`): when a static lead-in phrase + a cycling accent word should be **physically replaced** (not cross-dissolved) by a hero arriving with momentum, and the final frame is the hero alone. Reach for it when the takeover should read as an impact.
- Brand_Outro: the same collision used as a sign-off â€” options cycle, the brand mark crashes in and owns the frame.

**duration**: 5â€“7s

**shot structure** (a `[bg]` canvas; one text group on the left/center that gets ejected by an incoming hero)

- **Scene 1 (0.0â€“~1.4s) â€” context build.** A typewriter lays down a `[lead-in phrase]` character-by-character (smooth, no typos â€” selling confidence, not human chaos). Camera static.
- **Scene 2 (~1.4â€“3.0s) â€” the cycling beat.** An `[accent word]` slot inside the line ticks through 2â€“3 `[options]` on a vertical spring-roll (each click a new word), suggesting breadth â€” "many things this could be." (More than ~3 reads as filler.)
- **Scene 3 (~3.0â€“4.2s) â€” the collision (signature move).** A `[hero]` crashes in from off-screen with momentum and physically SHOVES the whole text group aside â€” the text reacts to the impact (gets displaced), it does not fade. The hero lands **heavy** â€” a longer settle, not a zip â€” so it reads as mass, not speed.
- **Scene 4 (~4.2â€“end) â€” the hero alone.** The hero settles dead-center and reads still. Holds.

**motion vocabulary**: smooth character typewriter; vertical spring-ticker word roll (2â€“3 steps); off-screen hero crash-in with momentum; reactive displacement of the struck text group; heavy long-tail landing (not bouncy); dual-axis subtle jitter on the resting hero.

**rule mapping**

- smooth single-phrase typewriter lead-in â†’ `discrete-text-sequence` (smooth-slice / continuous `floor(progress)` form â€” no typo machinery)
- accent word slot-machine cycling through options â†’ `vertical-spring-ticker` (`STEPS` = number of options the hero will replace; the rule's footer-reveal is unused â€” Scene 3 takes its place)
- hero shoves the text group aside on impact â†’ `reactive-displacement` (the text is the displaced mass; express the hero's "heavy land" as a longer `power2` settle, not the rule's default `back.out`)
- hero's fast off-screen crash-in â†’ `motion-blur-streak` (directional velocity blur resolving sharp as it lands)
- resting-hero aliveness â†’ `sine-wave-loop` (low-amplitude dual-frequency register â€” scale + rotation jitter composing onto the hero's final landed scale; never a yoyo around 1)

**camera modifier**: camera-static â€” the displacement happens in element space (the hero moves the text), so there is no real camera move; the impact is the only motion.
