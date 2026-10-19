---
name: ai-ugc-realism
description: "When the user is generating AI UGC-style ad creative (AI actors, talking-head testimonials, AI influencers, faceless spokesperson clips, or product-in-hand shots) and the output looks fake, plastic, glossy, or like a 'stock photo that moves.' Also use when the user mentions 'AI UGC,' 'AI actor,' 'AI avatar looks fake,' 'make this AI video look real,' 'realistic AI person,' 'AI influencer,' 'talking head ad,' 'the face keeps changing between cuts,' 'character consistency,' 'skin looks plastic,' 'too glossy,' 'uncanny,' or 'AI ad that doesn't look AI.' Use to add the specific imperfections that break the AI beauty default, and to keep a generated character consistent across every cut of a video. Pairs with image/video generation skills (nano-banana-pro, flux-image, ai-image-generation, agentic-image-generation, video) and with ad-creative for the faceless/UGC ad formats."
metadata:
  version: 1.0.0
---

# AI UGC Realism

AI image and video models default to a face that reads as fake: glowy skin, a symmetric face, perfect teeth, soft studio light. It looks like a stock photo that learned to move. Real UGC works because the person looks like an actual human filming themselves on a phone, not a model in a commercial. This skill makes AI-generated actors, testimonials, and product shots pass as real by naming the imperfections the model will never add on its own, and by keeping one character consistent across an entire video.

## The problem: the beauty default

Every general image/video model is trained toward flattering, retouched, professionally-lit faces. Left alone it removes exactly the things that signal "real footage." You do not get realism by asking for "realistic" or "photorealistic" (that word pushes toward polished stock). You get it by explicitly restoring the flaws the model stripped out.

## The fix: name the imperfections

State these directly in the prompt. Do not rely on the model to infer them, and do not soften them into "natural looking."

- **Visible pores** on the nose, cheeks, and forehead
- **Peach fuzz** along the jaw and upper lip
- **Shine / oil** on the nose and forehead (not matte, not powdered)
- **Faint under-eye shadow** (mild, not dramatic bags)
- **A single small healing blemish** or a spot, not clear skin
- **Uneven, asymmetric freckles** (not a tidy sprinkle)

Supporting cues that reinforce "phone footage, not a shoot": slightly uneven skin tone, a stray flyaway hair, natural (not whitened) teeth, mixed indoor lighting instead of a soft key light, a phone front-camera focal length. Pick the few that fit the character. The goal is a believable human, not a caricature of flaws, so tune quantity to the look you want.

## Once a reference photo is attached: stop describing the person

The single most common mistake. When you attach a reference image (or several) for the character, **stop writing sentences about the face.** The model is now anchored to the reference. Every extra sentence describing the person ("she has green eyes, high cheekbones, light freckles...") competes with the reference and pulls the output away from it.

After a reference is attached, describe only:

- **Pose** (what the body/head is doing)
- **Camera** (angle, framing, lens feel, phone vs. pro)
- **Setting and light** (where they are, what light hits them)
- **Action** (what happens in the shot)

Let the reference carry the identity. Describe the scene, not the face.

## Keeping a character consistent across a video

A face that looks great in one still still drifts, warps, or becomes a different person on the next cut. Four rules hold a character together across every generation in a multi-shot video:

1. **Restate the character and the negatives in every single video prompt.** Not once at the top of the project. Every generation gets the full character description (or reference) plus the imperfection list, because each generation starts fresh and will re-drift toward the beauty default if you let it.
2. **Run the negatives on every generation.** The "no glossy skin, no symmetric face, no perfect teeth, no studio glam" negatives are per-generation, same as the positives. Dropping them on shot 4 is how shot 4 turns plastic.
3. **Give several reference angles up front.** Front, profile, close-up, and a full-body shot. One frontal headshot is not enough for the model to reconstruct the person from a new angle; it invents the missing sides and they drift. More angles, less drift.
4. **After the reference is attached, describe pose and camera, not the person** (the rule above, applied per shot). Every face sentence you add per shot is another chance to lose the reference.

## Honest limits

State these to the user instead of promising a perfect result:

- **Text and UI inside the shot garble.** A phone screen, an app interface, a label, or any readable text held up in-frame will usually come out as gibberish. Composite real screens in post, or keep screens out of frame / out of focus.
- **Some motion reads unnatural.** Hands, gait, and object interactions can still look slightly off even with a locked character. Cut around the worst frames; keep shots short.

Neither is fully solved by prompting. Plan the edit around them.

## Workflow

1. Lock the character: generate or select 3-4 reference angles (front, profile, close-up, body) with the imperfection list baked in.
2. Build a reusable prompt block: `[character reference] + [imperfection list] + [negatives]`. This block is pasted into every shot.
3. Per shot, append only pose + camera + setting + action. Never re-describe the face.
4. Generate, keep the takes where the character held, cut around drift and garbled screens.
5. For the ad structure around these shots (hooks, faceless/UGC formats, script), hand off to `ad-creative`.

## Tool stack (reference)

The realism prompt method is model-agnostic. Tools people pair with it: a TikTok ad-spy scraper (find a brand's top-performing ads, download them, transcribe with timestamps plus a frame log, on-screen text, and product placement) to reverse-engineer what already converts; a generation model reachable from chat (e.g. a Higgsfield MCP, or the `nano-banana-pro` / `flux-image` scripts); and a scheduler the agent can post through (e.g. Postiz). Catalog live tools in the workspace resources doc rather than hardcoding vendors here.

## Related skills

- **ad-creative**: the faceless/UGC and motion-video ad formats, hooks, and grounded batch production that these realistic shots slot into.
- **nano-banana-pro / flux-image / ai-image-generation / agentic-image-generation**: the actual image generation engines. This skill governs *what to put in the prompt*, they *run* it.
- **video**: video generation and editing mechanics.
- **video-prompting-guide**: general prompt structure for AI video. This skill is the realism-and-continuity layer on top of it.
