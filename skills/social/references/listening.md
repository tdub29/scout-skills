# Social Listening & Engagement Triage

How to surface the right posts to engage with each day â€” instead of randomly scrolling. The goal is a short, scorable list ("here are your top 10 posts to comment on") rather than an open feed.

## Contents
- When to use this
- The daily triage loop
- Scoring rubric
- Comment quality tiers
- Sources & light tooling (curl recipes)
- Per-platform notes
- Common workflows

---

## When to Use This

Use listening when the goal is **commenting and relationships**, not posting. Typical asks:
- "Give me the top 10 posts I should comment on today"
- "Who's complaining about [competitor] right now?"
- "Find people asking for a tool like mine"
- "Surface posts from my 20 target accounts in the last 24h"
- "What's the conversation around [topic] this week?"

If the user wants to **create** content, use the rest of the social skill. Listening feeds creation (it surfaces angles, language, objections), but the output is different.

---

## The Daily Triage Loop

A repeatable 20-minute loop the user (or you, on their behalf) can run each morning.

1. **Pull** â€” fetch new posts from defined sources (target accounts, keywords, subreddits, hashtags). See [tooling](#sources--light-tooling-curl-recipes).
2. **Filter** â€” drop anything older than 24h, low signal, or off-topic.
3. **Score** â€” apply the [rubric](#scoring-rubric). Keep top 10.
4. **Draft** â€” for each, draft a comment matched to the post's tier.
5. **Post** â€” user reviews, edits, posts. Mark which actually went live.
6. **Log** â€” track what you commented on and what got replies. This is your engagement loop dataset.

Output format Claude should produce:

```
TOP 10 POSTS â€” 2026-06-05

1. [Score 9/10] @author â€” LinkedIn â€” 2h ago
   "We just rolled out X and the team is loving itâ€¦"
   Why: ICP fit (B2B SaaS, 50â€“200 employees), buying-intent signal
   Suggested comment: [draft]
   Link: https://â€¦
```

---

## Scoring Rubric

Score each post 1â€“10 across five dimensions, then sum and rank.

| Dimension | What it measures | Weight |
|-----------|------------------|--------|
| **ICP fit** | Is the author your target customer / influencer? | 2x |
| **Intent signal** | Are they expressing a problem, asking, or shopping? | 2x |
| **Reach potential** | Is the post getting traction (likes/comments rising)? | 1x |
| **Comment opportunity** | Can you say something genuinely useful, not generic? | 2x |
| **Recency** | Posted in last 1â€“4h (early comments win, especially on LinkedIn) | 1x |

**Intent signal examples (high-value):**
- "Looking for a tool that does X"
- "Why is [category] so painful?"
- "We just switched from [competitor] becauseâ€¦"
- "Anyone use [competitor] â€” is it worth it?"
- A complaint about a known competitor

**Drop if any of these are true:**
- Author isn't ICP and isn't an influencer
- Post is >24h old and already has 50+ comments (your comment buries)
- Generic motivational/AI-slop post
- Self-promotion thread where comments don't get reach
- You can't add anything beyond "Great post!"

---

## Comment Quality Tiers

Match the comment to the post. Don't waste a tier-1 draft on a tier-3 opportunity.

**Tier 1 â€” Relationship builder (target accounts, ICP, high intent)**
- Add a specific insight or counter-example
- Reference your own experience with specifics (numbers, names, outcomes)
- Ask a thoughtful follow-up that invites a reply
- Length: 2â€“4 sentences, no link

**Tier 2 â€” Visibility play (high-reach post, adjacent topic)**
- Add one sharp insight in one sentence
- Pattern: "Agreed â€” and the part most miss is [X]"
- Length: 1â€“2 sentences

**Tier 3 â€” Light touch (relationship maintenance)**
- Specific reaction, not "Love this"
- Quote a specific line and react to it
- Length: 1 sentence

**Never:** "Great post!", emoji-only, "+1", LinkedIn-isms like "This is gold ðŸ”¥"

---

## Sources & Light Tooling (curl recipes)

**Fetch ladder. Climb it top-first and say which rung you used.** Governing rule: `.agents/rules/web-browsing-setup.md`.

0. **A platform source, or you don't have a URL yet, use `agent-reach`.** Run `agent-reach doctor --json` first; it names the live backend per channel. See [LinkedIn, X, Reddit](#linkedin-x-reddit-agent-reach).
1. **An open public JSON or RSS endpoint, use `curl` or `feedparser`.** The recipes below. Fastest when the endpoint is actually open.
2. **A static public page or an oEmbed endpoint, use `WebFetch`.**
3. **A JS-rendered public page, use `node .agents/scripts/web-get.mjs "<url>" --text`.** Key-free, no daemon, no account. Add `--shot out.png` for a screenshot.
4. **Genuine logged-in multi-step interaction, use `browser-use`** (`.agents/browser-use-tooling/.venv/Scripts/browser-use.exe`, not on PATH). It has a flaky background daemon. Last resort, and say so when you use it.
5. **Never** cloud `browse` / Browserbase. It needs API keys that will not be set.

**Tooling actually present on this machine (verified 2026-08-23):**

| Tool | State | Use instead |
|---|---|---|
| `jq` | **not installed** | Pipe to `python -c "import sys,json; ..."`. Every `\| jq` below is illustrative, not runnable as written. |
| `xmllint` | **not installed** | `feedparser` (see the RSS recipe). |
| `python` | on PATH | A project venv can hijack it. Check `echo $env:VIRTUAL_ENV`; the system interpreter is `C:\Users\TrevorWhite\AppData\Local\Programs\Python\Python312\python.exe`, which is where `feedparser` lives. |

Worked example, HN with stdlib instead of `jq`:
```bash
SINCE=$(($(date +%s) - 86400))
curl -s "https://hn.algolia.com/api/v1/search_by_date?query=KEYWORD&tags=story&numericFilters=created_at_i>${SINCE}" \
  | python -c "
import sys, json
for h in json.load(sys.stdin)['hits'][:10]:
    print(h['title'], '|', h['author'], '|', 'https://news.ycombinator.com/item?id='+h['objectID'])
"
```

### Reddit (no longer free or scriptable)

**Reddit's anonymous `.json` endpoints are blocked.** Both `https://www.reddit.com/r/SaaS/new.json` and `/search.json` return **403** (verified 2026-08-23), with or without a custom User-Agent. There is no zero-config path left: the official API's manual review has approved almost nothing since 2025-11.

Reddit reads now go through `agent-reach`'s reddit channel, which is **locked** pending a decision from Trevor. See [LinkedIn, X, Reddit](#linkedin-x-reddit-agent-reach) for the state and what unblocks it. Do not paste a `.json` URL and hope.

### Hacker News (Algolia search)

**Recent stories mentioning a keyword (last 24h):**
```bash
SINCE=$(($(date +%s) - 86400))
curl -s "https://hn.algolia.com/api/v1/search_by_date?query=KEYWORD&tags=story&numericFilters=created_at_i>${SINCE}" \
  | jq '.hits[] | {title, url, author, points, num_comments, created_at, story_id: .objectID, hn_url: ("https://news.ycombinator.com/item?id="+.objectID)}'
```

**Recent comments mentioning a keyword:**
```bash
curl -s "https://hn.algolia.com/api/v1/search_by_date?query=KEYWORD&tags=comment&numericFilters=created_at_i>${SINCE}" \
  | jq '.hits[] | {author, comment_text, story_title, hn_url: ("https://news.ycombinator.com/item?id="+.objectID)}'
```

### Bluesky (public API, blocked from this machine)

âš  **Returns 403 from this machine** (verified 2026-08-23, via both `curl` and node `fetch`). The egress IP sits on AS7922, which is also what makes Jina Reader answer `401 bad network reputation`. This is not a broken recipe, it is an IP-reputation block, and the only thing that unblocks it is a different egress. The recipe below is correct and works from a clean network.

**Search posts by keyword:**
```bash
curl -s "https://public.api.bsky.app/xrpc/app.bsky.feed.searchPosts?q=KEYWORD&limit=25&sort=latest" \
  | jq '.posts[] | {author: .author.handle, text: .record.text, likes: .likeCount, replies: .replyCount, url: ("https://bsky.app/profile/"+.author.handle+"/post/"+(.uri | split("/") | last))}'
```

### RSS for blogs, podcasts, YouTube channels

For target accounts that publish to RSS (most blogs, all YouTube channels). This is the highest-yield rung that is fully live here. `xmllint` is not installed, so use `feedparser` on the system python:

```bash
"C:/Users/TrevorWhite/AppData/Local/Programs/Python/Python312/python.exe" -c "
import feedparser
# YouTube channel feed: https://www.youtube.com/feeds/videos.xml?channel_id=CHANNEL_ID
# Generic blog feed:    https://example.com/feed/
for e in feedparser.parse('FEED_URL').entries[:6]:
    print(e.get('published', ''), '|', e.title, '|', e.link)
"
```

### LinkedIn, X, Reddit (agent-reach)

These three expose no usable public API. **`agent-reach` is the right channel for all three** and it is installed on this machine. **As of 2026-08-23 all three are LOCKED** and need a per-channel decision from Trevor before any command here will run. They need a logged-in session, not an API key.

**Check before you reach, every time:**
```bash
agent-reach doctor --json
```
`doctor` is the authority on which backend serves each channel. Note that `agent-reach` is a setup and diagnostics CLI, **not a fetcher**. There is no `agent-reach fetch` or `agent-reach read`. It tells you the live backend, and you then call that backend directly (`opencli`, `twitter`, `mcporter`, `curl`). Its per-channel reference files live in `.agents/skills/agent-reach/references/` (social.md, career.md, web.md, video.md). Read them before writing a command.

Roughly 5 of 15 channels are live today (youtube, rss, web, v2ex, bilibili). The three that matter here are not:

| Channel | State | Backend when live | What unblocks it |
|---|---|---|---|
| **X / Twitter** | LOCKED | `twitter-cli`, or `opencli twitter` | `pipx install twitter-cli` (v0.8.5+), then a manual Cookie-Editor export set as `TWITTER_AUTH_TOKEN` + `TWITTER_CT0` in the same shell. Or `agent-reach install --system --channels opencli` and reuse a Chrome session already logged in to x.com. |
| **Reddit** | LOCKED | `opencli reddit`, or `rdt-cli` | No zero-config path exists. Either OpenCLI over a Chrome already logged in to reddit.com, or `pipx install 'git+https://github.com/public-clis/rdt-cli.git'` followed by `rdt login`. |
| **LinkedIn** | LOCKED | `mcp-server-linkedin` via `mcporter` | `uvx mcp-server-linkedin@latest --login` once, to save a session. The documented Jina Reader fallback (`curl -s "https://r.jina.ai/https://linkedin.com/in/USER"`) answers **401** from this machine, so it is not a fallback here. |

**Say the lock out loud instead of running a command you know will fail.** "LinkedIn is locked in agent-reach; unblocking it is one `uvx mcp-server-linkedin --login`, want me to?" is the correct report. Improvising a browser workaround is not.

**Commands once a channel is unlocked** (taken from the agent-reach reference files, not invented):
```bash
# X / Twitter, after exporting TWITTER_AUTH_TOKEN + TWITTER_CT0
twitter user-posts @handle -n 20          # a target account's recent posts
twitter tweet URL_OR_ID                   # one tweet plus replies
twitter feed -n 20                        # home timeline (the most stable command)
opencli twitter search "query" -f yaml    # OpenCLI fallback, reuses the browser session

# Reddit, via OpenCLI over a logged-in Chrome
opencli reddit search "query" -f yaml
opencli reddit subreddit SaaS -f yaml
opencli reddit read POST_ID -f yaml

# LinkedIn, after `uvx mcp-server-linkedin@latest --login`
mcporter call linkedin.get_person_profile linkedin_username="handle" sections="posts"
mcporter call linkedin.search_people keywords="AI engineer" location="Remote"
```

**No working path today: scrolling an authenticated LinkedIn or X feed.** Nothing installed here can page an algorithmic logged-in feed. `mcp-server-linkedin` reads profiles, companies and jobs, not the feed; `twitter feed` needs the cookie pair that is not set. The only tool that could do it is `browser-use` driving a real logged-in session, which has a flaky background daemon and is the last rung for a reason. **Do not invent a scroll command.** Either get the channel unlocked, work from specific target-account URLs, or ask the user to paste the posts.

**Useful URLs once a channel is live:**

| URL pattern | What it shows |
|-------------|---------------|
| `linkedin.com/in/HANDLE/recent-activity/all/` | A target account's recent posts |
| `linkedin.com/feed/hashtag/TOPIC/` | Hashtag feed |
| `linkedin.com/feed/` | Your main feed (algorithmic, less useful for triage) |
| `x.com/HANDLE` | A target account's profile |
| `x.com/search?q=QUERY&f=live` | Real-time search (use `f=live` for chronological) |
| `x.com/i/lists/LIST_ID` | A curated list, the cleanest source for target accounts |

**Tips:**
- On X, build a private list of target accounts and read the list. Far cleaner than the algorithmic feed.
- LinkedIn's `/recent-activity/all/` URL is the cleanest way to see one person's posts without the algorithm.
- Never auto-post. Draft, hand to the user, let them post. Bot detection is a real risk on both platforms.
- Rate-limit yourself. Leave a couple of seconds between calls; bulk paging trips captchas and, on X, risks a ban.

**Paid alternatives if you don't want to drive a session:**

| Platform | Tools |
|----------|-------|
| LinkedIn | Sales Navigator (saved searches), Taplio (engagement) |
| X | TweetDeck/X Pro (saved columns), Typefully, Taplio, Tweet Hunter |

**Still closed (no good path):**
- Instagram & TikTok â€” closed APIs, browser automation is detectable and risky. Use native saved searches / hashtag follows.

---

## Per-Platform Notes

### LinkedIn
- **Locked today.** Reads go through `agent-reach`'s linkedin channel, see [LinkedIn, X, Reddit](#linkedin-x-reddit-agent-reach). Unblock is one `uvx mcp-server-linkedin@latest --login`.
- **First-hour comments matter most** â€” algorithm weights early engagement heavily. Prioritize posts <2h old from target accounts.
- Comments with 5+ words get more reach than reactions
- Replying to other commenters can put you in front of their network
- Tag the author in your reply only if it adds context

### Twitter/X
- **Locked today.** Reads go through `agent-reach`'s twitter channel, see [LinkedIn, X, Reddit](#linkedin-x-reddit-agent-reach). Once unlocked, build a private list of target accounts and read the list URL rather than the feed.
- Reply within first 30 min for max reach on big accounts
- Quote-tweet > reply when adding substantial value
- Threading your reply (multi-tweet) signals effort
- Don't pile on dunks â€” relationships > clout

### Reddit
- **Locked today.** Anonymous `.json` is 403; reads need `agent-reach`'s reddit channel over a logged-in session. See [LinkedIn, X, Reddit](#linkedin-x-reddit-agent-reach).
- Read the subreddit rules before commenting (some ban self-promotion outright)
- Earn karma in the sub before linking to anything you own
- Long, specific answers win. AMAs and "help me decide" threads are gold
- Never lead with your product â€” answer the question first

### Hacker News
- Comment quality bar is high; low-effort gets downvoted fast
- Founders commenting on threads about their product is welcomed if you're transparent
- Search for past discussions of your category â€” they're often dormant gold mines

### Bluesky
- **403 from this machine** (egress IP reputation, not the recipe). Works from a clean network.
- Smaller volume but high engagement-to-follower ratio
- Tech and indie-hacker communities are active
- Custom feeds (like Bluesky's "Following" + topic feeds) replace algorithmic search

---

## Common Workflows

**What actually runs today:** HN (Algolia), RSS and YouTube feeds, V2EX, and any public page via `WebFetch` or `web-get.mjs`. **The Reddit, X and LinkedIn steps below are blocked** until those agent-reach channels are unlocked, and Bluesky is blocked from this egress IP. Run the live half, name the blocked half, do not substitute a guess.

### "Give me my top 10 posts to comment on today"
1. Pull from: target account RSS/saved searches + Reddit (relevant subs) + HN (last 24h)
2. Score with the [rubric](#scoring-rubric)
3. Output top 10 with suggested comments

### "Find people complaining about [competitor]"
1. Reddit search: `"competitor name" -site:competitor.com` sorted by new
2. HN comment search for competitor name
3. Bluesky search for competitor handle/name
4. Score by intent signal (high if switching language: "moving from", "alternatives to", "frustrated with")

### "Surface brand mentions from the last week"
1. Reddit search for brand name
2. HN search (stories + comments) for brand name
3. Bluesky search for brand name + handle
4. Output as: reply needed (yes/no), tone (positive/negative/neutral), suggested response

### "Find target-account posts I missed"
1. Maintain a list of target accounts with their RSS / Reddit usernames / Bluesky handles
2. Fetch each source's recent posts
3. Filter to last 24h, output sorted by score

---

## Setting Up the Source List

The user should maintain a list of sources somewhere persistent at `.agents/listening-sources.md` (or `.claude/listening-sources.md`). Claude reads it when running the daily loop.

**A ready-to-fill template lives at [listening-sources-template.md](listening-sources-template.md).** Copy it into the project and edit. The source path depends on how the skill was installed:

```bash
# Plugin / marketplace install (most common):
cp .agents/skills/social/references/listening-sources-template.md .agents/listening-sources.md
# .claude/ install:
cp .claude/skills/social/references/listening-sources-template.md .agents/listening-sources.md
# Working inside the marketingskills repo:
cp skills/social/references/listening-sources-template.md .agents/listening-sources.md
```

The template covers: brand/category, ICP (for scoring), target accounts per platform, intent keywords, subreddits, saved-search URLs, and a do-not-engage list.
