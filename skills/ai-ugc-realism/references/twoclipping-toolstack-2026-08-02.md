# twoclipping tool stack + workflow (net-new to SKILL.md)

Source: @twoclipping, "How to turn Claude into your entire video ad department (Full Course)," X article, Jul 31 2026 (21.4K views).

SKILL.md governs the *prompt method* (name the imperfections, stop describing the face, hold the character across cuts) and deliberately abstracts the tooling ("Catalog live tools in the workspace resources doc rather than hardcoding vendors here"). This file IS that catalog: the concrete, chat-native tool stack that turns the method into a pipeline â€” spy on a competitor -> read the ads frame-by-frame -> rebuild at full realism -> schedule out, all from sentences in a Claude chat.

## The thesis: borrow a working format, the product is the punchline

The article's framing, and the reason the tooling matters: **you do not need an original idea to go viral. You need a format that is already working, with your product put inside it.** Originality is remix, not invention from nothing (Picasso studied African masks; hip hop is built on other people's records; the printing press was a wine press with the screw pointed at paper). What separates people is *what* they borrow from and *whether it was already working*.

Author's receipts (use as evidence the method scales, not as claims to repeat as fact):
- 15B+ views generated for apps, "almost none from an original idea we invented."
- Rizz app scaled to $400k/month by inserting the app into an already-viral format. Same playbook on Cantina AI (AI meme trends) and Looksmax AI (looksmaxing trend). Later clients: Kalshi, Polymarket, Pumpfun.
- The reusable format example (from @timdanilovhi): **"every level of X, explained"** â€” original did 6.4M views, then bent into gaming, wealth, banned books, drywall. Same skeleton, almost every version prints.

**The one non-negotiable step:** pick one competitor, one teardown, and read it *properly* before deciding anything â€” write down what happens at second 4 and second 20 of each ad. It is boring (nobody does 300 videos by hand), which is exactly why it is edge. "Ten minutes and it's the only part I'd actually insist on."

## Tool stack (concrete)

| Piece | What it is | URL | Trigger / install |
|---|---|---|---|
| **tiktok-ad-spy** | Competitor ad scraper. Finds a brand's top ads, downloads the mp4s, and reads each one: verbatim transcript with timestamps, a per-second frame log, every on-screen text overlay, and where the product actually appears. | `tiktok-ad-spy.twoclipping.workers.dev` | Add as a skill, then say once: `set up tiktok ad spy`. Run with one sentence: `spy on duolingo`. |
| **ugc-lab** | The realism creator skill â€” both halves, image AND video. Bakes the imperfection list + negatives + character-consistency rules that SKILL.md teaches. | `ugc-lab.twoclipping.workers.dev` | Add as a skill. |
| **Higgsfield MCP** | Live connection so Claude *runs* the generation in-chat instead of handing you a prompt to paste elsewhere. No API key, no config file, ~30 sec. | connector: `mcp.higgsfield.ai/mcp` Â· setup: `higgsfield.ai/mcp` | Claude desktop/claude.ai -> Customize -> Connectors -> add new -> name it `higgsfield` -> paste connector url -> sign in. |
| **Postiz** | The scheduler Claude can actually talk to (by @wickedguro). Connect accounts once (TikTok/IG/YouTube/etc.), Claude sees every connected channel and schedules straight to them â€” 1 account or 40, same work. | `postiz.com` | Connect accounts in Postiz, grab key from Settings, hook it to Claude. |
| **Gemini API key (free)** | The ONLY credential in the whole stack. Gives Claude *eyes* â€” vision to watch the mp4s the spy skill downloads. The one thing Claude genuinely can't do on its own. | `aistudio.google.com/apikey` | Create API key -> let it make a project when asked -> copy. No card, no trial, no billing screen. |

A skill = instructions Claude follows (fires when it recognizes the job, you never invoke it). An MCP = a live connection Claude can *call*. You need both: skills to know what to do, the Higgsfield MCP to actually generate, Postiz to actually post.

## One-time machine setup

- **Prereqs:** Python and curl. curl ships with Windows 10+/macOS/Linux, so realistically it's just Python. **ffmpeg optional but wanted** â€” it shrinks oversized videos down to something the vision model will accept. Don't check versions by hand; the skills check their own environment and install what's missing.
- **Add a skill:** Customize (top-left) -> Skills -> add. Verify by asking Claude what skills it has â€” it should read the description back.
- Everything runs on your own machine and IP: no server between you and the data, no subscription, no shared rate limit.

## End-to-end flow (one sentence each)

1. `spy on <brand>` -> top ads downloaded + read frame-by-frame with transcript, frame log, overlays, product placement.
2. Rank by what actually performed; Claude tells you what happens in each. Do the second-4 / second-20 teardown here.
3. Rebuild the winning format at full realism (ugc-lab prompt method) with a creator who doesn't exist.
4. Generate in-chat via the Higgsfield MCP â€” no leaving the conversation.
5. Schedule + post across every connected social via Postiz.

## Failure modes the author actually hit (net-new war stories)

These are concrete bugs behind the abstract "honest limits" in SKILL.md â€” useful because they show *what a naive competitor-scrape gets wrong*:

- **Pagination lie:** early version only read the first page of results â€” 17 ads instead of 61, and the "top" ad was 32k views instead of the real 390k. Fixed to paginate fully. (Takeaway: verify your scraper isn't silently truncating.)
- **Caption confusion:** searching `stalkie` returned 119 results that were mostly `talkie`. Fix: stop trusting captions â€” pull wide, then have Claude confirm from the actual frames which product is really on screen, and drop the wrong ones. (Takeaway: identify the product by vision, not by text metadata.)
- **Readable phone screen inside the shot garbles every time** â€” a real problem when the product IS the app. (Matches SKILL.md's text/UI limit; composite real screens in post.)
- **Some natural movements don't land.** The models are good, not perfect; they don't carry every format on their own.

## Economics context (for sizing the DIY-vs-buy call)

- Competitors charge $100+/month for *one slice* of this (ad research alone is a paid product; so is the generation). The whole twoclipping skill stack above is free.
- Their paid creator network (if you'd rather not DIY): 150,000+ creators (manual, manual-AI, real human UGC), performance-based ~$1 per 1k views vs. Meta tier-1 CPM $15-40. No base fee/retainer. (`link.affiliatenetwork.com/two`) â€” context only; the free stack is the point.

## Honest framing (repeat to the user)

Not a switch-on-and-walk-away machine. It doesn't replace human creators, manual AI, or real UGC â€” it's a workflow tool, and it won't fit every format, because of AI-video-model limits, not skill weakness. Best version available right now, and it beats guessing at a blank page and paying to find out the ad didn't land.
