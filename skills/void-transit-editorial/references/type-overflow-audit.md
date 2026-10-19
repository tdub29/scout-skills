# Display-Type Overflow Audit

Tight tracking + huge sizes make painted glyph ink spill past the line box and clip. For every large title, log `clientWidth` vs `scrollWidth` and `clientHeight` vs `scrollHeight` at rest, at mid-animation, and at max pointer offset; fix until each reports zero. Fixes: protective cap-height padding (`padding-top:.14em;padding-bottom:.21em`), safer `line-height`, gentler negative tracking, `clamp()` container-aware sizes, and safe zones for vertical titles. The full audit prompt is step 7 of `Void03-PROMPTS.md`.
