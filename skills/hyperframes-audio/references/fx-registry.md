# Effect registry

Every effect, its parameters and the usable range of each. Values outside a range
are clamped on read, so anything that parses is safe to realise. **AUTO** marks a
parameter an automation lane can drive; anything unmarked cannot move over time
(see the note at the bottom).

Generated from `HF_AUDIO_FX` in `@hyperframes/core/audio-fx`, which is the source
of truth â€” if this table and the code disagree, the code is right.

## Filter â€” which frequencies a track may occupy

| Effect      | Parameter                                                                                                   |
| ----------- | ----------------------------------------------------------------------------------------------------------- |
| `highpass`  | `frequency` 20â€“20000 Hz (300, log) **AUTO** Â· `q` 0.1â€“20 (0.707, log) **AUTO** Â· `poles` `1`\|`2` (2)       |
| `lowpass`   | `frequency` 100â€“20000 Hz (8000, log) **AUTO** Â· `q` 0.1â€“20 (0.707, log) **AUTO** Â· `poles` `1`\|`2` (2)     |
| `peaking`   | `frequency` 20â€“20000 Hz (1000, log) **AUTO** Â· `gain` âˆ’40â€“40 dB (0) **AUTO** Â· `q` 0.1â€“20 (1, log) **AUTO** |
| `lowshelf`  | `frequency` 20â€“2000 Hz (200, log) **AUTO** Â· `gain` âˆ’40â€“40 dB (0) **AUTO**                                  |
| `highshelf` | `frequency` 500â€“20000 Hz (4000, log) **AUTO** Â· `gain` âˆ’40â€“40 dB (0) **AUTO**                               |

`q` is bandwidth â€” higher is narrower. `poles` is the slope: `2` is the usual
biquad (12 dB/oct), `1` is gentler (6 dB/oct). Shelving filters have no `q`: the
Web Audio spec leaves it unused for them, so a control would have moved nothing.

## Dynamics â€” how level behaves over time

| Effect       | Parameter                                                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `gain`       | `gain` âˆ’60â€“12 dB (0) **AUTO**                                                                                                                                                  |
| `compressor` | `threshold` âˆ’60â€“0 dB (âˆ’24) Â· `ratio` 1â€“20 (4) Â· `attack` 0.01â€“2000 ms (20, log) Â· `release` 0.01â€“9000 ms (250, log) Â· `knee` 1â€“8 (2.83) Â· `makeup` 0â€“36 dB (0) Â· `mix` 0â€“1 (1) |
| `limiter`    | `limit` âˆ’24â€“0 dB (âˆ’1) Â· `attack` 0.1â€“80 ms (5) Â· `release` 1â€“8000 ms (50, log) Â· `level_out` âˆ’24â€“24 dB (0)                                                                     |
| `gate`       | `threshold` âˆ’80â€“0 dB (âˆ’35) Â· `range` âˆ’80â€“0 dB (âˆ’24) Â· `ratio` 1â€“20 (10) Â· `attack` 0.01â€“9000 ms (1, log) Â· `release` 0.01â€“9000 ms (100, log) Â· `knee` 1â€“8 (2.83)               |

Cuts on `gain` go to âˆ’60 dB, boosts stop at +12: it is a level stage for making
room, and a chain that could add 40 dB would clip long before that was useful.
`knee` of 1 is a hard corner, higher eases into it. `mix` below 1 blends the dry
signal back in (parallel compression). `range` is how far down the gate pulls
when closed â€” a gate that pulls all the way to silence sounds like a switch.

## Nonlinear â€” changes the waveform's shape

| Effect     | Parameter                                                                                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `saturate` | `type` `tanh`\|`atan`\|`cubic`\|`exp`\|`alg`\|`quintic`\|`sin`\|`erf`\|`hard` (tanh) Â· `threshold` âˆ’40â€“0 dB (âˆ’6) Â· `output` âˆ’24â€“24 dB (0) **AUTO** Â· `oversample` 1â€“8Ã— (4) |
| `bitcrush` | `bits` 1â€“32 (8) Â· `samples` 1â€“250Ã— (1) Â· `mix` 0â€“1 (1)                                                                                                                     |

`tanh` is the gentlest curve and `hard` is outright clipping. Higher `oversample`
costs more CPU and keeps aliasing down. `samples` repeats each sample N times â€” a
crude downsample, which is where the lo-fi character comes from.

## Time â€” space and width

| Effect   | Parameter                                                                                                                                                           |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `delay`  | `time` 1â€“5000 ms (250, log) **AUTO** Â· `feedback` 0.01â€“0.95 (0.35) **AUTO** Â· `mix` 0â€“1 (0.4) **AUTO**                                                              |
| `reverb` | `size` 0.05â€“1 (0.7) Â· `damping` 0â€“1 (0.5) Â· `wet` 0â€“1 (0.35) **AUTO** Â· `dry` 0â€“1 (0.7) **AUTO**                                                                    |
| `chorus` | `delay` 1â€“100 ms (7) **AUTO** Â· `depth` 0â€“10 ms (2) **AUTO** Â· `speed` 0.01â€“10 Hz (1) **AUTO** Â· `mix` 0â€“1 (0.5) **AUTO**                                           |
| `phaser` | `in_gain` 0â€“1 (0.4) **AUTO** Â· `out_gain` 0â€“2 (0.74) **AUTO** Â· `delay` 0.1â€“5 ms (3) Â· `decay` 0â€“0.99 (0.4) Â· `speed` 0.1â€“2 Hz (0.5) **AUTO** Â· `type` `0`\|`1` (0) |

Reverb convolves a _generated_ impulse, and both preview and render generate the
same one â€” so a room is reproducible without shipping an impulse file. Higher
`damping` rolls the top off the tail faster, which is what makes a large room
sound like a soft one. `feedback` near the top of its range is a very long tail;
it is bounded below 1 because at 1 it never decays.

## Why some parameters cannot be automated

Automation is handed to the audio thread once, as native `AudioParam` ramps and
curves, which is what keeps it sample-accurate and identical between preview and
render. A parameter can therefore only be automated if an `AudioParam` backs it.
Three kinds do not:

- **worklet processor options** â€” `compressor`, `limiter`, `gate` and `bitcrush`
  are AudioWorklets configured wholesale, so **none of their parameters are
  automatable at all**.
- **a WaveShaper curve** â€” `saturate`'s `type`, `threshold` and `oversample`
  rebuild the curve; only its `output` stage is a real param.
- **a convolution impulse** â€” `reverb`'s `size` and `damping` regenerate the
  impulse; `wet`/`dry` are gain stages and automate fine.

To make one of those behave differently over time, automate a `gain` stage
around it instead: a lane on a `gain` before a compressor changes how hard the
compressor is driven, which is most of what automating its threshold would have
done.
