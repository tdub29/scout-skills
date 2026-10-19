# TASTE.md â€” the shipped taste profile

Confirmed-by: Louise (2026-06-11)

> A sourcing skill is only as good as its taste. This file is the curation layer [SKILL.md](SKILL.md) loads before sourcing anything: which kinds of b-roll to reach for, how fast to cut, and which sources are trusted. It ships with **my** taste (Louise's â€” I make fast-cut tech/marketing video) so the skill makes good calls out of the box. Fork it and make it yours â€” see [Make it yours](#make-it-yours) at the bottom.

## Where this taste comes from

Two signals, in order of strength:

1. **Revealed taste** â€” extracted from my actual published videos, not from what I *say* I like. Method: scene-cut detection on the final cut (`ffmpeg select='gt(scene,0.3)'` â†’ frame montage â†’ catalog every cutaway by type, count the cuts). What you ship beats what you follow.
2. **Curated sources** â€” my YouTube subscriptions, auto-imported then pruned to the b-roll-worthy ~10%, tagged by topic so a tech video never gets scoped to my surf vlogs.

## The fingerprint (revealed from real videos)

**B-roll types I actually use, in rough order of frequency:**

1. **Screenshots / receipts** â€” tweets, social posts, forum threads, documents, search results. Heavy. â†’ the **Receipts** route.
2. **Text / title cards** â€” dark navy (or bold color) background, short punchy text. The motion-graphic look. â†’ pairs with **Concept**.
3. **Full-frame cutaways, green-screen composited** â€” b-roll fills the frame, often with the speaker keyed in.
4. **Memes / face reactions** â€” occasional, anchored on a punchline. â†’ the **Meme** library loop.
5. **Products** â€” clean full-frame product shots. â†’ **Entity/Product**.
6. **Historical / vintage imagery** â€” sepia portraits, archival moments. â†’ **Entity/Historical**.

**Pacing (measured across two published videos â€” a 69s fast-cut explainer with 33 shots, and a 123s storytelling video with 54 shots):** **~26â€“28 cuts/min**, **median shot ~1.6â€“1.9s**. Sub-second insert bursts are a signature move â€” e.g. four receipt screenshots fired in 1.2 seconds (a "receipt montage"). The longest holds (6â€“14s) go to the one explainer beat per video. So: cut roughly every 2 seconds; b-roll coverage ranges **~20% (talky explainer) â†’ ~50% (dense storytelling)**.

**Compositing:** talking head on green-screen / bold colored backgrounds, alternating fast with full-bleed cutaways.

**Notably ABSENT â€” and this is the load-bearing insight:** random "creator clip from a channel I follow" b-roll. I do not pull vibe clips off other YouTubers. The taste-risky **Cultural** route is almost never needed; real b-roll here is Receipts + Entity + Memes + on-brand text cards â€” mostly the OBJECTIVE routes, where there's a checkably *correct* clip. **That's why an agent can source for me at all: my taste rarely asks it to guess.** When you fork this profile, check your own published videos for the same property before letting the agent near vibe-based sourcing.

## Trusted sources (YouTube, tagged by topic)

Searches stay INSIDE this list (plus any source the script itself references). Topic tags scope each video: a `tech` video only searches `tech`-tagged sources.

### Tech / AI
- @anthropic-ai [tech] â€” Anthropic official â€” AUTHORITATIVE for "how AI/LLMs work" credibility flex (interpretability, "Tracing the thoughts of an LLM")
- @OpenAI [tech] â€” OpenAI official â€” model launches / demos (product-flavored)
- @3blue1brown [tech] â€” best "how LLMs work" visual explainers
- WIRED [tech] â€” explainers, "X explained in N levels", product breakdowns
- Silicon Mania [tech] â€” tech/startup commentary
- KRAZAM [tech, comedy] â€” tech satire skits â€” GREAT meme/reaction b-roll for tech beats
- Mark Rober [tech] â€” engineering spectacle, gadget moments
- Hannah Fry [tech] â€” math/AI/data explainers, credibility flex
- CGP Grey [tech, explainer] â€” concept explainers (animated â€” often a style reference for motion-graphics, not a clip)
- Bryan Johnson [tech] â€” longevity/biohacking, "future" energy
- Alex Finn [tech] â€” AI / build-in-public takes
- Chatbase [tech] â€” AI tooling

### Business / GTM / Marketing
- Lenny's Podcast [business] â€” product & growth
- Andrew Capland [business] â€” growth/SaaS marketing
- 20VC with Harry Stebbings [business] â€” VC/startup
- All-In Podcast [business] â€” tech/business panel
- David Perell [business] â€” writing/content/audience
- Colin and Samir [business, creator] â€” creator economy, YouTube-about-YouTube
- Leila Hormozi [business] â€” operator/business
- The prospecteur (Eddy Snoussi) [business] â€” sales/prospecting

### Creator / video / filmmaking
- CaseyNeistat [creator] â€” vlog/storytelling, iconic moments
- Matti Haapoja [creator] â€” video/filmmaking
- Matthew Encina [creator] â€” design/creative process
- Dan Mace [creator] â€” filmmaking energy
- Oscar Boyson [creator] â€” doc/filmmaking

### Comedy / interview (reaction + meme beats)
- Amelia Dimoldenberg [comedy] â€” Chicken Shop Date â€” deadpan reaction gold
- LoeWhaley [comedy] â€” workplace/corporate skits â€” perfect for marketer content
- The Adam Friedland Show [comedy] â€” deadpan interview
- Matt Rife [comedy] â€” standup crowd work
- Louis Theroux [comedy, interview] â€” awkward-pause documentary moments
- JRE Clips [interview] â€” podcast moments / clip culture

## Guardrails
- **MEMES: OFF â€” never source, never propose** (Louise, 2026-06-11, stated explicitly mid-run). The meme fingerprint above is historical; this guardrail wins.

- **Audio: ALWAYS SILENT** â€” I talk over all b-roll. Every sourced clip gets its audio stripped (`ffmpeg -an`). Never hand back a clip with sound. (Confirmed at onboarding 2026-06-11.)
- **Stills motion: subtle sub-pixel zoom-in by default** â€” ~1.5%/sec, centered, rendered sub-pixel (PIL float-box Lanczos). ffmpeg `zoompan`/crop-pans stay banned at any speed (integer-stepped = shaky); no pans, nothing faster than ~2%/sec. (Confirmed at onboarding 2026-06-11.)
- **Source attribution: AUTO (contrast-pick)** â€” small credit per clip, canonical source name + platform ("WIRED / YouTube"), bottom-right at ~70% opacity, white or black auto-picked per clip for contrast; moves bottom-left when the footage carries its own badge bottom-right. Never a URL. Etiquette, not a license â€” official/authoritative sourcing stays the real copyright posture. (Confirmed at onboarding 2026-06-11.)
- **Motion graphics: ON** â€” Remotion project at `~/Downloads/prompt-overlay` (dark #0b0f17 + indigo #6366f1, grid + spring; existing comps: BellCurve, GrowthChart, BrollConcepts, Ep2Concepts â€” reuse/extend these). Use for concept/stat/chart beats. (Louise, 2026-06-11.)
- **AI-generated b-roll: OFF** â€” never generate AI footage. Real footage, receipts, or on-brand Remotion graphics only; a beat with nothing real gets dropped or flagged, never AI-filled. (Confirmed at onboarding 2026-06-11.)
- **Scoping: no random videos** â€” searches stay inside the trusted list + script-referenced sources; for "how X works", go to the authoritative source (AI â†’ Anthropic/OpenAI/3Blue1Brown). Open YouTube search only as a flagged last resort.
- **On-brand:** tech-literate, a bit irreverent â€” I market a screen recorder ([Tella](https://tella.tv)), so Loom-bashing is welcome.
- **Off-limits:** _(fill in yours â€” e.g. nothing political? clip length cap? minimum resolution?)_

## Defaults

- **Default video topic:** tech
- **Default output format (sourcing only):** silent Â· 9:16 1080Ã—1920 Â· ~3s Â· anchored after the punchline

## Template sections (fill in as they come up)

- **Accounts I quote (X / LinkedIn):** the people whose takes/moments you reference â€” add them as the agent asks.
- **Reference bank (movies / shows / comedians / running jokes):** specific bits you reach for.
- **Recurring targets:** the meme/clip you keep wanting.

---

## Make it yours

This profile is the template â€” the structure transfers even if my channels don't. Three steps:

1. **Import-then-prune, not a blank interview.** Pull your YouTube subscriptions with no API key by reading your logged-in browser cookies:
   ```bash
   yt-dlp --cookies-from-browser chrome --flat-playlist \
     --print "%(uploader)s ||| %(channel_url)s" \
     "https://www.youtube.com/feed/channels"
   ```
   Then have the agent categorize them with you and prune hard â€” of my ~280 subscriptions, only ~25 were b-roll-worthy. Bench the rest with a topic tag (`lifestyle`, dormant) instead of deleting; you'll want them the day you make a video on that topic.

2. **Reveal your fingerprint from your own published videos** (strongest signal â€” do this if you've shipped anything): scene-cut detect your best video, montage the frames, catalog every cutaway by type, count cuts/min. Replace my fingerprint section with what you actually use.

3. **Answer the guardrails** â€” audio, stills motion, off-limits, on-brand voice â€” and set your default topic.

No published videos yet? Seed taste from **exemplars** instead: give the agent 3â€“5 b-roll moments you loved in other people's videos and let it extract the pattern.
