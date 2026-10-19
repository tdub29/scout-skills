# Per-platform strategies

Each platform has 1-4 strategies tried in order. Free first, paid only if a key happens to be set.

**Every command below was run against this machine on 2026-08-23** and is marked with what it
actually returned. Anything that failed is marked LOCKED or DEAD with the reason, not rewritten into
a plausible-looking command. If you find yourself improvising a command that is not on this page,
stop and report the gap instead.

## The tool ladder this file is built on

| Rung | Tool | Where it is | Use for |
|---|---|---|---|
| 0 | `agent-reach` | on PATH (global pip install) | Purpose-built platform reads. **Run `agent-reach doctor --json` first â€” it is the authority on what is live.** |
| 1 | `WebFetch` / `curl` | built in | Public JSON APIs and oEmbed endpoints |
| 2 | `node .agents/scripts/web-get.mjs "<url>" --text` | workspace script, key-free | JS-rendered public pages (headless system Chrome) |
| 3 | `browser-use` | `.agents/browser-use-tooling/.venv/Scripts/browser-use.exe`, **not on PATH** | Genuine logged-in multi-step interaction only. Background daemon, flaky, last resort. |
| â€” | cloud `browse` / Browserbase | **never** | Needs API keys Trevor will not set. Do not reach for it. |

`agent-browser` and `dev-browser` are **not installed on this machine** â€” not on PATH, not in any
skill tree, not as an npm global, not as an MCP server. Any older instruction naming them was wrong.

Governing rule: [`.agents/rules/web-browsing-setup.md`](../../../rules/web-browsing-setup.md).

## agent-reach channel status (2026-08-23)

`agent-reach doctor --json` reported **5 of 15 channels live**. Re-run it; do not trust this snapshot
past the date on it.

| Channel | Status | Meaning for this skill |
|---|---|---|
| `web`, `rss`, `youtube`, `v2ex`, `bilibili` | ok | live |
| `twitter` | **LOCKED** | `twitter-cli` not installed; needs a manual Cookie-Editor export |
| `reddit` | **LOCKED** | no backend installed; anonymous `.json` is blocked platform-side |
| `linkedin` | **LOCKED** | no LinkedIn MCP configured |
| `instagram`, `facebook` | **LOCKED** | need OpenCLI plus a logged-in Chrome |
| `github`, `exa_search`, `xueqiu`, `xiaohongshu`, `xiaoyuzhou` | warn/off | not used by this skill |

**The locked channels are the exact platforms this skill is worst at.** They are locked pending a
per-channel decision from Trevor, because each needs a logged-in session or a token he has not set.
Unlocking one is a decision, not a workaround â€” see "What would unblock each locked platform" at the
bottom of this file. Do not route around a locked channel by inventing a scrape.

**Caveat on `web`:** doctor reports `web: ok` via Jina Reader, but a plain
`curl -s "https://r.jina.ai/<url>"` from this network returns **401 AuthenticationRequiredError**
("blocked from performing anonymous queries due to bad network reputation (AS7922)"). Jina Reader is
not a working key-free path from this box. Use rung 2 (`web-get.mjs`) instead.

---

## bluesky

**Reliability: high.** Public API, free, no auth. Verified 200 on 2026-08-23.

### Strategy 1 â€” Public AppView API (DEFAULT)

URL: `https://bsky.app/profile/<handle>/post/<rkey>`

```bash
# Resolve handle to DID
DID=$(curl -s "https://public.api.bsky.app/xrpc/com.atproto.identity.resolveHandle?handle=<handle>" | jq -r .did)

# Build AT-URI and fetch the post + thread
URI="at://${DID}/app.bsky.feed.post/<rkey>"
curl -s "https://public.api.bsky.app/xrpc/app.bsky.feed.getPostThread?uri=${URI}" | jq .
```

Returns the post + immediate parent + first-level replies in one call. Perfect for `--with-replies`.
A malformed rkey returns 400, not an empty result â€” treat 400 as "bad URL parse", not "post gone".

---

## mastodon

**Reliability: high, but instance-dependent.** Free, no auth on most instances.

### Strategy 1 â€” Status endpoint

URL pattern: `https://<instance>/@<user>/<status-id>`

```bash
# Single status
curl -s -H "Accept: application/json" "https://<instance>/api/v1/statuses/<status-id>"

# With replies
curl -s -H "Accept: application/json" "https://<instance>/api/v1/statuses/<status-id>/context"
```

Note: instance and ID parsed from URL. Web URL `https://hachyderm.io/@user/123456` maps to API
`https://hachyderm.io/api/v1/statuses/123456`. Both endpoints verified 200 on hachyderm.io, 2026-08-23.

**Instance caveat:** some instances now require auth on public endpoints. `mastodon.social` returns
`{"error":"This method requires an authenticated user"}` on its public timeline. If a status endpoint
401s, that is the instance's policy, not a broken URL â€” say so and stop. There is no key-free
workaround for an instance that has closed its public API.

---

## hn

**Reliability: high.** Free public Algolia API. Verified 200 on 2026-08-23.

### Strategy 1 â€” Algolia items API

URL pattern: `https://news.ycombinator.com/item?id=<id>`

```bash
curl -s "https://hn.algolia.com/api/v1/items/<id>" | jq .
```

Returns the item + full nested comment tree. Comments are recursive â€” flatten or limit depth per the
`--with-replies` flag.

---

## reddit

**Reliability: LOCKED. There is no working free path as of 2026-08-23.**

The `.json` suffix trick is **dead**: `https://www.reddit.com/r/<sub>/comments/<id>/.json` returns
**403** with a real browser User-Agent, and `old.reddit.com` returns **403** too. `web-get.mjs`
against a thread URL returns Reddit's "Prove your humanity" bot challenge, not the post.
`agent-reach doctor` reports reddit `off` and states the anonymous `.json` endpoints are blocked
platform-side and that the official API's manual review approves almost nothing since 2025-11.

### Strategy 1 â€” Wayback Machine (the only path that ever returns content, and rarely)

```bash
curl -s "https://archive.org/wayback/available?url=<encoded-url>" | jq -r '.archived_snapshots.closest.url'
```

Returns a Wayback URL if a snapshot exists, then re-fetch from there with `WebFetch`. Most threads
have no snapshot and `archived_snapshots` comes back `{}`. This is a coin flip, not a strategy.

### If that fails

Stop and report Reddit as locked. Do not scrape around the bot challenge. See "What would unblock"
below.

---

## x (twitter)

**Reliability: low. Text + author + date only. No engagement, no replies, no thread.**

### Strategy 1 â€” oEmbed (DEFAULT, verified working)

The only key-free X path that returns real content from this machine. Verified 200 on 2026-08-23.

```bash
curl -sL "https://publish.twitter.com/oembed?url=<encoded-tweet-url>"
# 301-redirects to publish.x.com/oembed; -L is required
```

Returns JSON with `author_name`, `author_url`, `url` (canonical), and `html` â€” a blockquote
containing the **full post text** and the posted date. Parse the text out of the blockquote.

Gives you: `author.handle`, `author.name`, `text`, `posted_at`, `url`.
Does **not** give you: any engagement count, replies, thread siblings, media metadata, `verified`.
Set every one of those to `null`, never `0`.

### Strategy 2 â€” Wayback Machine

```bash
curl -s "https://archive.org/wayback/available?url=https://twitter.com/<user>/status/<id>" | jq -r '.archived_snapshots.closest.url'
```

Older tweets are sometimes cached, recent ones almost never. Worth one call when oEmbed 404s
(deleted or protected post).

### What does NOT work â€” do not try these

- **`web-get.mjs` against an x.com post URL returns HTTP 403** ("Access to x.com was denied"). Verified 2026-08-23.
- **Jina Reader** (`r.jina.ai`) returns 401 from this network. Verified 2026-08-23.
- **Nitter** â€” the public instance network is effectively gone. Do not build a rotation loop against it.
- **agent-reach's twitter channel** â€” LOCKED, `twitter-cli` is not installed.

### Strategy 3 â€” ScrapeCreators / Apify (PAID, only if the env key is already set)

See `auth-keys.md`. Trevor's standing position is that he does not set API keys for tooling, so treat
these as unavailable unless `$SCRAPECREATORS_API_KEY` / `$APIFY_API_TOKEN` is already populated in the
environment. Do not prompt him to sign up.

---

## linkedin

**Reliability: LOCKED for posts and for any authenticated read.**

`agent-reach doctor` reports linkedin `warn`: no LinkedIn MCP is configured. Jina Reader, its listed
fallback, returns 401 from this network.

### Strategy 1 â€” `web-get.mjs` on a public post URL (LOW yield, try once)

```bash
node .agents/scripts/web-get.mjs "<url>" --text
```

Sometimes returns the post body for a fully public `linkedin.com/posts/...` URL before the auth wall
engages. Usually returns a sign-in interstitial. If the output is a login page, that is a locked
result â€” report it, do not retry with a different user agent.

### There is no working path for

- **Any authenticated LinkedIn read**: the logged-in feed, feed scrolling, connection-gated posts,
  `linkedin.com/in/<handle>` recent-activity behind the sign-in wall, people or job search.
- **Reliable single-post fetch** with author, date and engagement together.

Say this plainly to the user rather than producing a partial result that looks like a fetch. See
"What would unblock" below.

### Strategy 2 â€” ScrapeCreators / Apify (PAID, only if the key is already set)

Same caveat as X. See `auth-keys.md`.

---

## instagram

**Reliability: LOCKED. No working free path as of 2026-08-23.**

- `agent-reach` instagram channel is `off` (needs OpenCLI plus a logged-in Chrome; OpenCLI is not installed).
- **Open Graph scraping is dead**: `curl -A "Mozilla/5.0" "https://www.instagram.com/p/<id>/"` returns no `og:` tags.
- Instagram's oEmbed endpoint 301s to the Facebook Graph API, which requires an app access token.

Report Instagram as locked. Do not invent a scrape. Paid fallback (`auth-keys.md`) only if a key is
already set.

---

## tiktok

**Reliability: medium. Metadata only, no engagement.**

### Strategy 1 â€” oEmbed (verified working)

Verified 200 on 2026-08-23.

```bash
curl -s "https://www.tiktok.com/oembed?url=<encoded-video-url>"
```

Returns `title` (the caption, including hashtags), `author_name`, `author_url`, `thumbnail_url`, and
an embed `html`. No like/comment/share/view counts â€” set those `null`.

Note: scraping the video page HTML directly returns **no** `og:` tags (verified 2026-08-23), so oEmbed
is the whole free path, not a first step toward one.

### Strategy 2 â€” ScrapeCreators / Apify (PAID, only if the key is already set)

See `auth-keys.md`.

---

## threads

**Reliability: LOCKED. No working free path as of 2026-08-23.**

`web-get.mjs` against a Threads post URL returns the bare string `Threads` and nothing else (verified
2026-08-23) â€” the content is behind Meta's anti-bot. There is no public Threads oEmbed. `agent-reach`
has no Threads channel at all.

Report Threads as locked. Paid fallback (`auth-keys.md`) only if a key is already set.

---

## Strategy chain summary

| Platform | Working free path (verified 2026-08-23) | Paid fallback (only if key already set) |
|---|---|---|
| bluesky | Public AppView API | â€” |
| mastodon | Instance API, if that instance allows anonymous reads | â€” |
| hn | Algolia API | â€” |
| tiktok | oEmbed (caption + author only) | ScrapeCreators â†’ Apify |
| x | oEmbed (text + author + date only) â†’ Wayback | ScrapeCreators â†’ Apify |
| linkedin | `web-get.mjs`, low yield, public posts only | ScrapeCreators â†’ Apify |
| reddit | **none** (Wayback coin flip) | â€” |
| instagram | **none** | ScrapeCreators â†’ Apify |
| threads | **none** | ScrapeCreators â†’ Apify |

## What would unblock each locked platform

Each of these is a **decision for Trevor**, not something to run unprompted. Every one costs either a
logged-in browser session or a credential. Name the specific unblock when you report a locked fetch,
and stop there.

| Platform | What would unblock it | Cost |
|---|---|---|
| **X â€” engagement, replies, threads** | `pipx install twitter-cli` (v0.8.5+), then a manual Cookie-Editor export of `TWITTER_AUTH_TOKEN` + `TWITTER_CT0`, exported in the calling shell. Documented in `.agents/skills/agent-reach/references/social.md`. | A logged-in X session's cookies on disk |
| **Reddit** | `agent-reach install --system --channels opencli` plus staying logged in to reddit.com in Chrome (OpenCLI reuses the session the user already controls; it never logs in for you). Server fallback is `rdt-cli`. | OpenCLI Chrome extension + a live login |
| **LinkedIn â€” authenticated feed scroll, gated posts, search** | `uvx mcp-server-linkedin@latest --login` to save a logged-in session, then `mcporter call linkedin.*` (`mcporter` **is** installed). Alternatives under consideration: `SawyerHood/dev-browser` and `remorses/playwriter`, both flagged as install candidates in `.agents/artifacts/github/star-intake-gap-audit-2026-08-22.md`. Neither is installed today. | A saved LinkedIn login session |
| **Instagram / Facebook** | `agent-reach install --system --channels opencli` plus a logged-in Chrome on that site. | OpenCLI extension + a live login |
| **Threads** | Nothing available. No agent-reach channel, no public API, no oEmbed. | Genuinely unsolved |

`browser-use` (rung 3) can in principle drive a logged-in session for any of these, but it carries a
background daemon that regularly fails its own `browser-use doctor` check. It is the last resort and
must be named as such when proposed, never presented as a working path.
