# Procedural Story Grammar, Check-ins and Measured Proof

Read when planning a short story-driven or explainer video (any renderer: HyperFrames, a single canvas `frame(t)`, Remotion), before the storyboard, and again before calling it done. The doctrine (SKILL.md) governs seams and in-scene performance; this file adds what neither it nor `hyperframes-creative` (`story-spine.md`, `beat-direction.md`, `narration.md`) covers: pace per beat type, a named reason for every cut, the sound arc, three cheap approval gates, and the numbers that prove "done".

Source: distilled from `cth9191/animate` (MIT, pushed 2026-10-05; `craft.md`, `grammar/STORY.md`, `grammar/FRAME.md`, `kit/core.js`) as shown in the Chase AI "a video is a function" video, reviewed 2026-10-11 in `.agents/artifacts/animation-reference-2026-10-11/review.md`. Third-party and unproven here: the rules are its author's, learned on its pieces, not measured by us. Paraphrased, not copied.

**Where it conflicts with the doctrine, the doctrine wins for HyperFrames work:**

- Idle life (a blink, a cursor, steam in held frames) is for hand-drawn character pieces whose boil on 2s is the medium. In HyperFrames, a hold is owned by a sustained-motion route; idle wobble stays banned.
- Hard cuts on the beat and shape-morph bridges are this grammar's transitions. In HyperFrames, the default seam is still cut-the-curve in the current's direction, checked by the Seam Gate.
- Silence before the payoff (sound, 0.5 to 4 s) pairs with the doctrine's stillness before climax (picture, 0.3 to 0.75 s); use both.
- Springs here overshoot a hair on UI and not at all on big type, which sits inside the doctrine's ban on `bounce.out` / `elastic.out`.

## 1. Three cheap check-ins before any build

A wrong story or look costs a full build, so approve in this order and do not animate before gate 3.

| gate | what the user sees | what they decide |
| --- | --- | --- |
| Story (text) | one-line idea, a device sayable in one sentence, format, length, BPM, numbered beat table: time, what happens, bridge into the next beat, sound role (where the silence is, where the loudest hit is) | approve / change beats / different angle |
| Look | 2 to 4 full-size style frames of the most different beats, side by side | thumbs up per frame / change look |
| Storyboard | every beat as a key frame with its sound and its transition into the next, numbered | thumbs up or down **by panel number** |

The approved frames' drawing code becomes the video's scene code, so nothing is redrawn later.

## 2. Pace per beat type

| beat | job | cuts/s | loudness | length |
| --- | --- | --- | --- | --- |
| start | hero at rest, held | 0 | quiet | 1 to 1.5 s |
| build | one framing, detail accrues | 0 to 1 | rising | 3 to 6 s |
| change | hero changes form | 1 to 5, on 8ths | a hit on the change | 2 to 3 s |
| journey | many places, speeding up on a fixed tempo | 3 to 8 | flat groove, within ~3 dB | 5 to 9 s |
| turn | builds slowly, then changes in 1 to 3 frames | 0 then 2 | a drop, then the loudest hit | 1 to 3 s |
| quiet | alone, still | 0 | lowest | 1 to 1.5 s |
| ending | back to the opening image, changed by the story | 0 | fading or held | 2 to 4 s |

Speed mostly comes from steps of one move on 2s, not from more shots.

## 3. Every cut has a reason you can say out loud

next-step (the process continues) Â· match-position (hero holds its spot, world changes) Â· shape morph (this becomes that: close in on one object, morph on a blank sheet, open out of its counterpart) Â· iris in/out (a circle on the hero over 2 to 4 frames) Â· scale in/out (5 to 20 times) Â· pov Â· cause-effect Â· time-cut (light changes on the same framing) Â· callback (reuse an earlier framing exactly, changed). Chronologies transition from the scene (morphs); catalogue and character pieces cut hard on the beat. At most one hard cut in a morph-joined piece: the slam on the payoff.

## 4. The sound arc

- **Silence before the payoff, loudest on the payoff.** Drop to near silence for 0.5 to 4 s on a held image, then the single loudest hit. The busiest moment goes just before the silence and is not the loudest.
- **With a voice-over, the voice is the clock.** Each beat starts ~0.3 s after a sentence ends (word times from faster-whisper; `.agents/scripts/transcribe-media.py` does this locally). Land the payoff hit in the pause before the line that names it: under speech the duck swallows it. Judge the arc on the score without the voice.
- **With the user's track, the song is the arc.** Put the turn on its drop and the payoff on its loudest hit; cut on its beats.
- **Grid that lands on whole frames:** 24 fps at 120 BPM gives an 8th = 6 frames, a 16th = 3. (30 fps pairs with 112.5 BPM.) Cuts and morph centres sit on the 8th grid, proven by a script, not by eye.
- Balance by removing energy (cut the sustained pad), not boosting the hit.

## 5. Frame rules that read as "not generic AI video"

- Banned defaults: centred title on a gradient, everything fading in, corner labels, glow on UI chrome, generic particle bursts, a logo sting as the only ending.
- One constant the eye can hold in every frame; one colour reserved for the thing the story follows.
- Something new every 2 to 4 s; held frames keep small idle life (a blink, a cursor, steam).
- Act the idea out literally; caption at most one short line per beat.
- Phone scale: anything that matters is at least ~100 px on a 1080-wide frame, captions at least 50 px, 9:16 content inside x 60 to 940, y 250 to 1500. Captions hold at least 1.25 s and at most 3.5 words/s.
- What existed before a step is on screen from frame 0; only the step's own effects animate in. Hard cuts land on finished frames.

## 6. Determinism and motion

- Every frame starts from a clean canvas and is a pure function of `t`: seeded RNG keyed by name (mulberry32 over an FNV hash), never `Math.random()` or `Date`. Check it: render the same `t` twice and compare pixel hashes.
- Hand-drawn looks move "on 2s": one boil index `B = floor(F / 2)` drives the wobble, the camera and every move.
- Springs for anything with mass, in closed form so frames stay deterministic:

```js
// step response of a damped spring, 0 to 1 over time t >= 0 (k stiffness, d damping)
function springEase(t, k = 170, d = 26) {
  if (t <= 0) return 0;
  const w0 = Math.sqrt(k), z = d / (2 * w0);
  if (z < 1) { const wd = w0 * Math.sqrt(1 - z * z);
    return 1 - Math.exp(-z * w0 * t) * (Math.cos(wd * t) + (z * w0 / wd) * Math.sin(wd * t)); }
  return 1 - Math.exp(-w0 * t) * (1 + w0 * t);
}
// presets: snappy {320,30} UI, smooth {170,26} cards/camera, heavy {90,19} big type, playful {260,14} visible overshoot
// many targets: sum one springEase per change, so a mid-move retarget stays continuous
```

- Cameras put a world point on a screen point; never "zoom about a point" (it drops the subject under the caption). In the fastest stretch, pin the hero by centring zoom bumps on it.

## 7. "Done" is measured, then looked at

Three layers every time: test tiles while building (look at them), script numbers, then contact sheets per shot with a written PASS table. Numbers worth checking:

- cuts and morph centres on the beat grid
- dead stretches longer than ~4 s with nothing new (silence acts exempt)
- hero anchor drift in the fastest section
- text cut off, overlapping, or under the phone UI (trust the check over your eye: a cropped label looks fine on a sheet)
- loudest 100 ms window lands in the payoff act, after the silence; integrated loudness (target about -14 LUFS with voice)
- frame count rendered equals frames expected (stale frames from a previous longer render get stitched onto the end otherwise)
- determinism: the same `t` renders an identical picture

Name the weakest shot and what would fix it; say what was not verified (the agent cannot hear the score).
