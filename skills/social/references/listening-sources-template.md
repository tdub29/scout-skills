# Listening Sources â€” Template

Copy this file to `.agents/listening-sources.md` in your project (or `.claude/listening-sources.md`) and fill in the brackets. Claude reads it when running the [listening workflow](listening.md).

Delete sections you don't use. Keep this short and current â€” stale sources are worse than no sources.

---

## What We're Listening For

**Brand / product:** [Your product name]
**Category:** [e.g., "AI writing assistant", "Postgres GUI"]
**Goal:** [e.g., "find people switching from Notion", "engage with B2B SaaS founders 50-200 employees"]

## ICP (for scoring)

Used by the [scoring rubric](listening.md#scoring-rubric) to judge ICP fit.

- **Role:** [e.g., "founder, head of marketing, marketing ops lead"]
- **Company stage:** [e.g., "seed to Series B SaaS, 10-200 employees"]
- **Industry:** [e.g., "B2B SaaS, infra, devtools"]
- **Signals they're a fit:** [e.g., "writes about GTM, runs paid ads, recently raised"]

---

## Target Accounts

Engage with **every** post from these accounts when relevant. Keep this list to 20-50 max.

### LinkedIn (`agent-reach` linkedin channel, currently LOCKED)
- [Name] â€” `linkedin.com/in/handle`
- [Name] â€” `linkedin.com/in/handle`

### X / Twitter (`agent-reach` twitter channel, currently LOCKED)
- [@handle]
- [@handle]

### Reddit (`agent-reach` reddit channel, currently LOCKED)
- u/[username]
- u/[username]

### Bluesky
- [handle.bsky.social]

### Blogs / Newsletters (RSS)
- [Name] â€” `https://example.com/feed/`
- [Name] â€” `https://example.substack.com/feed`

### YouTube channels (RSS)
- [Name] â€” channel ID `UCxxxxxxxx`

---

## Keywords (intent signals)

Search across all platforms. Claude runs these on the [daily loop](listening.md#the-daily-triage-loop). **Only HN runs today**: Reddit needs an unlocked agent-reach channel and Bluesky is 403 from this machine's egress. See [listening.md](listening.md#sources--light-tooling-curl-recipes).

### High-intent (someone shopping or switching)
- `"alternative to [competitor]"`
- `"looking for a [category] tool"`
- `"recommend a [category]"`
- `"switching from [competitor]"`
- `"frustrated with [competitor]"`

### Problem signals (someone in pain)
- `"[category] is so [bad/hard/expensive]"`
- `"why is [category] [problem]"`
- `"hate [pain point]"`

### Brand mentions
- `"[your brand]"`
- `"[your brand misspelling]"`
- `"[your domain]"`

### Competitor mentions (monitor for switching language)
- `"[competitor 1]"`
- `"[competitor 2]"`

---

## Subreddits

Pulled via `agent-reach`'s reddit channel on the daily loop. **Blocked today**: Reddit's anonymous `.json` API returns 403 and the channel needs a logged-in session Trevor has not approved. Keep the list; it becomes live the moment the channel is unlocked.

- r/SaaS
- r/Entrepreneur
- r/[your niche, e.g., "marketing", "devtools"]
- r/[adjacent community]

---

## Saved Searches (manual, or once the channel is unlocked)

URLs to scan. LinkedIn and X reads go through `agent-reach`; both channels are locked today, so these are for the user to open by hand until then.

### LinkedIn Sales Navigator
- [Search name] â€” `https://linkedin.com/sales/search/people?...`

### LinkedIn (regular)
- Posts hashtag â€” `https://linkedin.com/feed/hashtag/yourtopic/`

### X advanced search
- [Search name] â€” `https://x.com/search?q=...&f=live`

---

## Do Not Engage

Save yourself the regret.

- Accounts known for bad-faith dunking: [@handle], [@handle]
- Blocked brands / competitors who'll screenshot: [list]
- Topics to avoid: [politics, [your founder's hot takes], etc.]

---

## Notes for Claude

- When asked for "today's top 10," output in the format defined in [listening.md](listening.md#the-daily-triage-loop)
- For LinkedIn, X and Reddit, check `agent-reach doctor --json` first. All three are locked as of 2026-08-23. Say so rather than improvising a browser workaround, and never invent a feed-scroll command.
- For everything else, use the curl recipes in [listening.md](listening.md#sources--light-tooling-curl-recipes)
- Default lookback: 24h. User can override.
- Always ask before posting â€” output drafts, user approves and posts manually
