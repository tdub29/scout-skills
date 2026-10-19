---
name: social-fetch
description: "When you or another skill needs to fetch the content of a social media post by URL â€” tweet, X thread, LinkedIn post, Instagram post, TikTok video, Bluesky post, Reddit thread, Mastodon status, Threads post, Hacker News thread. Returns normalized structured data (author, posted_at, text, engagement counts, media URLs, replies if requested) regardless of platform. Tries strategies in order: agent-reach (the purpose-built platform CLI), direct public API or oEmbed (Bluesky, Mastodon, HN, X, TikTok), the key-free local headless browser web-get.mjs, Wayback Machine (older posts), paid APIs (ScrapeCreators / Apify â€” only if env keys present). Reports a platform as locked rather than inventing a scrape. Triggers on \"/social-fetch <url>,\" \"fetch this tweet,\" \"fetch this post,\" \"what does this LinkedIn say,\" \"read this thread,\" \"pull this post.\" Used by deep-research (citing specific posts), jab-hook (inspiration account analysis), business-brainstorm (competitor / operator commentary)."
metadata:
  version: 0.1.1
---

# /social-fetch â€” Pull any social post by URL

Normalized fetcher for social posts across platforms. Detects platform from URL, tries strategies in order, returns the same JSON shape regardless of source.

## Step 1 â€” Detect platform

| URL pattern | Platform |
|---|---|
| `x.com/<user>/status/<id>` or `twitter.com/<user>/status/<id>` | **x** (Twitter) |
| `linkedin.com/posts/<slug>` or `linkedin.com/feed/update/urn:li:activity:<id>` | **linkedin** |
| `linkedin.com/in/<handle>` (profile, recent activity) | **linkedin-profile** |
| `instagram.com/p/<id>` or `instagram.com/reel/<id>` | **instagram** |
| `tiktok.com/@<user>/video/<id>` | **tiktok** |
| `bsky.app/profile/<handle>/post/<rkey>` | **bluesky** |
| `reddit.com/r/<sub>/comments/<id>/...` | **reddit** |
| `<mastodon-instance>/@<user>/<id>` (e.g. mastodon.social, hachyderm.io) | **mastodon** |
| `threads.net/@<user>/post/<id>` | **threads** |
| `news.ycombinator.com/item?id=<id>` | **hn** |
| `youtube.com/watch?v=<id>` or `youtu.be/<id>` | â†’ defer to `watch-video` |

If the URL doesn't match any pattern, ask the user what platform it is.

## Step 2 â€” Pick strategy chain

Read `references/strategies.md` for the per-platform strategy chain. Every command there was run
against this machine and is marked with what it actually returned. **Do not improvise a command that
is not on that page** â€” if the ladder runs out, the answer is "locked", not a guess.

The tool ladder, in preference order (governing rule: `.agents/rules/web-browsing-setup.md`):

| Rung | Tool | Use for |
|---|---|---|
| 0 | `agent-reach` (on PATH) | Purpose-built platform reads. **`agent-reach doctor --json` is the authority on what is live** â€” read it, don't guess. |
| 1 | `WebFetch` / `curl` | Public JSON APIs and oEmbed endpoints |
| 2 | `node .agents/scripts/web-get.mjs "<url>" --text` | JS-rendered public pages, key-free, no daemon |
| 3 | `browser-use` (`.agents/browser-use-tooling/.venv/Scripts/browser-use.exe`, not on PATH) | Genuine logged-in multi-step interaction only. Flaky background daemon, last resort, say so when you use it. |
| â€” | cloud `browse` / Browserbase | **Never.** Needs keys Trevor will not set. |

`agent-browser` and `dev-browser` are **not installed on this machine** and never were. Any
instruction naming them is wrong.

Key principles:
- **Free strategies first** (agent-reach, direct APIs, oEmbed, `web-get.mjs`)
- **Paid only as fallback** (ScrapeCreators / Apify) â€” and only if the env key is *already* set; Trevor does not set keys for tooling, so never prompt him to sign up
- **Bluesky / Mastodon / HN are free + reliable** (public APIs)
- **X / TikTok** get metadata only from oEmbed: text, author, date. No engagement, no replies, no thread
- **Reddit / LinkedIn / Instagram / Threads have no working free path today.** `agent-reach` is the right tool for all four and all four channels are LOCKED pending a per-channel decision from Trevor (each needs a logged-in session or a token he has not set). Report the lock and name the unblock; do not scrape around it

## Step 3 â€” Execute strategy

For each strategy in the chain:
1. Try it
2. If success: parse â†’ normalize â†’ return
3. If failure (404, 402, auth wall, empty response): note the failure and try the next strategy

After exhausting the chain, return a clear error: which strategies were tried, which rung each sat on,
why each failed, and what's needed to unlock. Name the *specific* unblock from the table at the bottom
of `references/strategies.md` (e.g., "Reddit is locked: `.json` returns 403 and `web-get.mjs` hits the
bot challenge. Unblock = OpenCLI plus a logged-in Chrome, which is Trevor's call"). Never present a
partial or empty result as a successful fetch.

## Step 4 â€” Normalize output

Return this shape regardless of platform (see `references/output-schema.md` for the full spec + platform-specific examples):

```json
{
  "platform": "x",
  "url": "https://x.com/example/status/1234567890",
  "fetched_at": "2026-06-17T14:35:00Z",
  "raw_source": "scrapecreators",
  "author": {
    "handle": "@example",
    "name": "the user Ganim",
    "verified": true
  },
  "posted_at": "2026-06-17T16:53:00Z",
  "text": "The 80/20 of a useful AI second brain: ...",
  "media": [],
  "engagement": {
    "likes": 51,
    "reposts": 13,
    "replies": 9,
    "bookmarks": 7,
    "views": 32700
  },
  "is_thread": true,
  "thread": [],
  "replies": []
}
```

Fields with no equivalent on a platform (e.g., `bookmarks` on Mastodon) get `null`, not `0`. Missing data is different from zero data.

## Step 5 â€” Optional enrichments

Based on flags / asks:

| Flag | Behavior |
|---|---|
| `--with-replies` | Fetch top-level replies (1 hop). Costs extra API quota. |
| `--thread` | If the post is part of a thread by the same author, fetch the whole thread. |
| `--raw` | Include the raw API/scrape response in the output (for debugging) |
| `--media` | Download media files (images/videos) to `~/Documents/social-fetches/<platform>-<id>/` |

Default: just the post itself, no replies, no media download (just URLs).

## Step 6 â€” Cache (optional)

If `~/Documents/social-fetches/_cache/` exists, cache successful fetches there by `{platform}-{id}.json` for 24h. Saves API quota when the same post is referenced repeatedly across skills.

Skip cache if `--no-cache` flag is set or for `--with-replies` / `--thread` (likely-stale).

## Composes with

- `deep-research` â€” cite specific posts in research briefs. When research surfaces a relevant tweet/post URL, fetch and include in the brief.
- `jab-hook` â€” pull recent posts from inspiration accounts for deeper format analysis.
- `business-brainstorm` â€” pull competitor / operator commentary as evidence during scoring.
- `second-brain` â€” capture a post into `raw/` with the `tweet-` / `bookmark-` prefix; the structured output makes for cleaner raw files than a screenshot or copy-paste.
- `watch-video` â€” for YouTube URLs (or any video â€” Loom, Vimeo, Riverside, MP4), route there instead.

## Known limits

Verified against this machine on 2026-08-23. Re-check `agent-reach doctor --json` before trusting it.

- **X**: oEmbed returns text + author + date only. **No engagement counts, no replies, no thread** â€” those fields are `null`, not `0`. `web-get.mjs` on an x.com post returns 403.
- **LinkedIn**: no reliable path. `web-get.mjs` on a fully public post sometimes returns the body, usually a sign-in wall. **Any authenticated read (the logged-in feed, feed scrolling, gated posts, search) has no working path today.**
- **Reddit**: the `.json` suffix is **dead** (403 on `www` and `old`), and `web-get.mjs` hits a bot challenge. Only Wayback, and only if a snapshot happens to exist.
- **Instagram / Threads**: no working free path. Instagram serves no `og:` tags and its oEmbed needs a Facebook app token; Threads returns nothing but the word "Threads".
- **TikTok**: oEmbed returns caption + author + thumbnail. No engagement.
- **Bluesky / Mastodon / HN**: free + reliable. Mastodon is instance-dependent â€” some instances now require auth on public endpoints.
- **Private / deleted posts**: nothing helps. Try Wayback Machine for deleted content.

For every locked platform, `references/strategies.md` names the specific unblock (a logged-in session
or a token). Each is **Trevor's decision to make**, so surface it and stop â€” do not set it up, and do
not prompt him to sign up for a paid key.

## Notes on quality

- **Strategy chain, not single-source.** Every platform has a fallback ladder (agent-reach â†’ native API/oEmbed â†’ `web-get.mjs` â†’ Wayback â†’ paid, if a key is already set). If one step fails, degrade to the next and **say which rung produced the answer**. Never fail hard on the first attempt, and never silently drop the task when one backend errors.
- **A locked platform is a result, not a failure to hide.** When the ladder runs out, name the platform, the rung that failed, and the specific unblock. An invented command that looks plausible is worse than "locked" â€” it sends the next agent down a path that cannot work.
- **Structured output over screenshots.** Downstream skills (jab-hook, deep-research, second-brain) need JSON with author + text + engagement fields, not an image. Even when the underlying strategy is a screenshot, extract text before returning.
- **Cache aggressively, invalidate honestly.** 24h TTL on `~/Documents/social-fetches/_cache/` prevents API burn when the same post is referenced across multiple skills in a session. `--with-replies` / `--thread` skip cache because replies age fast.
- **Respect paid-key economics.** ScrapeCreators / Apify calls cost real money, and Trevor's standing position is that he does not set API keys or create accounts to make tooling work. Use a paid strategy only if the key is *already* in the environment. Never suggest signing up for one.
- **Media download is opt-in.** Default is post text only; `--media` downloads images/videos. Silent media downloads eat disk quickly.
- **Private / deleted content is a hard stop.** No strategy chain rescues private accounts or deleted posts. Suggest Wayback Machine for deleted content and stop.
- **Rate-limits are per-platform.** oEmbed endpoints throttle under a tight loop, and repeated `web-get.mjs` hits on a walled site (LinkedIn, Reddit) train the anti-bot rather than defeating it. Space out calls in loops or the workflow degrades to worse-than-manual.
