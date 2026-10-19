# Auth keys â€” unlocking paid fallback strategies

The free strategies (Bluesky API, Mastodon API, HN Algolia, X and TikTok oEmbed, `web-get.mjs`) work
for some cases. For X engagement/threads, LinkedIn posts, Instagram and Threads, paid keys would
unlock reliable + complete data.

> **Read this first.** Trevor's standing position is that he does **not** set API keys or create
> accounts to make tooling work. This page documents a road not taken. Use a paid strategy only if
> the environment variable is *already* populated; never prompt him to sign up, and never present a
> paid key as the recommended fix for a locked platform. The unblocks in `strategies.md` (a
> logged-in session via agent-reach's backends) are the paths that fit how he actually works, and
> even those are his decision to make.

## Which key unlocks what

| Key | Unlocks | Cost (approx, 2026) |
|---|---|---|
| `$SCRAPECREATORS_API_KEY` | X (tweets + threads + replies), LinkedIn posts, Instagram, TikTok, possibly Threads | Pay-as-you-go, ~$0.005â€“$0.02/post depending on endpoint |
| `$APIFY_API_TOKEN` | Nearly any platform via "Actors" (X, IG, TikTok, LinkedIn, Threads, even niche ones) | Per-actor pricing, often $1â€“$5 / 1K results |

## Checking whether a key is already set

This is a **Windows** box with no zsh, so there is no `~/.zshenv` to source. Check the environment
for an existing value and stop there:

```powershell
# PowerShell 5.1 (the only PowerShell on this machine)
if ($env:SCRAPECREATORS_API_KEY) { "scrapecreators: set" } else { "scrapecreators: not set" }
if ($env:APIFY_API_TOKEN)        { "apify: set" }          else { "apify: not set" }
```

If either is unset, the paid strategies for that provider are unavailable. That is the end of the
branch â€” do not walk the user through a signup. Fall back to reporting the platform as locked and
naming the session-based unblock from `strategies.md`.

## Free-only mode

Neither key is set, so free-only mode is the normal mode. Verified 2026-08-23:

- **Bluesky / Mastodon / HN** â€” fully functional (Mastodon is instance-dependent)
- **X** â€” oEmbed only: text, author, date. No engagement, no replies, no thread
- **TikTok** â€” oEmbed only: caption, author, thumbnail. No engagement
- **LinkedIn** â€” public posts sometimes readable via `web-get.mjs`; no authenticated read at all
- **Reddit / Instagram / Threads** â€” nothing. No working free path

Paid fallback would mostly help with:
- Building corpus (deep-research running many fetches)
- Analyzing thread structure or reply trees on X
- Inspiration-account analysis on Instagram (where free fails entirely)

None of that justifies asking Trevor for a key. Where a platform is locked, the honest answer is to
say so and name the session-based unblock.

## Cost discipline

When using paid strategies:
- Always check the cache first (`~/Documents/social-fetches/_cache/` if it exists)
- Default to 24h cache TTL
- Don't auto-enrich with `--with-replies` or `--thread` unless requested â€” these multiply quota use
- For high-volume work (e.g., fetching last 50 posts from an inspiration account), batch via Apify actors (cheaper per item) instead of ScrapeCreators per-call

## When to raise paid at all

Effectively never, unaided. Trevor has said he will not set keys or create accounts for tooling, so
"add a key" is not a fix this skill may propose. If a real workflow (deep-research, inspiration
analysis, competitor monitoring) is genuinely blocked on the same platform repeatedly, report the
blockage once with the concrete cost of each option, and let him decide:

1. The **session-based unblock** for that platform in `strategies.md` (free, no account, but needs a
   logged-in browser and his approval)
2. A paid key (money, an account, and ongoing cost)

Present option 1 first. Do not act on either without him saying so.
