# Social Media & Communities

xiaohongshu, Twitter/X, bilibili, V2EX, Reddit, Facebook, Instagram.

## xiaohongshu / XiaoHongShu (multiple backends)

xiaohongshu has three backends. **First run `agent-reach doctor --json` to see which `active_backend` xiaohongshu is on**, then use the matching command group.

### Backend A: OpenCLI (preferred on desktop)

```bash
# Search notes
opencli xiaohongshu search "query" -f yaml

# Read a note's body + engagement data (use the full URL from the search results, including xsec_token)
opencli xiaohongshu note "NOTE_URL" -f yaml

# Comments (nested reply threads supported)
opencli xiaohongshu comments NOTE_ID -f yaml

# Home recommendation feed
opencli xiaohongshu feed -f yaml

# A user's public notes on their profile page
opencli xiaohongshu user USER_ID -f yaml
```

> Requires Chrome to be open with the OpenCLI extension installed. OpenCLI only uses a
> Chrome session the user already has and explicitly controls; Agent Reach never logs in
> for the user, and never reads browser cookies.
> `agent-reach configure xhs-cookies` does not inject cookies into OpenCLI.
> If there is no existing session, do not log in automatically; switch to backend B/C and
> configure it through the matching manual Cookie-Editor export flow.

### Backend B: xiaohongshu-mcp (server scenarios)

```bash
# Before authenticating, have the user export manually with Cookie-Editor, then import explicitly
agent-reach configure xhs-cookies

# Read-only check of the current status
mcporter call xiaohongshu.check_login_status --timeout 120000

# Search
mcporter call xiaohongshu.search_feeds keyword="query" --timeout 120000

# Note detail + comments (take feed_id and xsec_token from the search results)
mcporter call xiaohongshu.get_feed_detail feed_id="..." xsec_token="..." --timeout 120000
```

> The first call automatically downloads a roughly 150MB headless browser, so always pass
> `--timeout 120000`.
> Authentication goes only through a manual Cookie-Editor export; after importing, run
> `check_login_status` first.
> That explicit command saves/imports the same-domain xiaohongshu.com cookie set the user
> supplies, and the user should confirm the scope; cookies from domains other than
> xiaohongshu.com are ignored.

### Backend C: xhs-cli (legacy fallback, upstream unmaintained since 2026-03)

```bash
xhs search "query"          # Search
xhs read NOTE_ID_OR_URL     # Read a note (must use the URL/ID from the search results, not a bare note_id)
xhs comments NOTE_ID_OR_URL # Comments
xhs hot                     # Trending
xhs feed                    # Recommendations
```

> Known to be unstable: `xhs user` / `xhs user-posts` / `xhs favorites` may return an API error (upstream is unmaintained and nobody is fixing it). New users should go straight to backend A/B.

### General notes

> **Authentication boundary**: Agent Reach must not log in to xiaohongshu on the user's
> behalf, and must not read browser cookies. OpenCLI may only use a Chrome session the user
> already has and explicitly controls; xiaohongshu-mcp and the legacy tools use a manual
> Cookie-Editor export.
>
> **xsec_token restriction**: xiaohongshu enforces an xsec_token mechanism, so **you cannot read a note with a bare note_id**. The correct flow: search or pull the feed first, then read using the full URL/ID from the results. This is the same on all three backends.
>
> **Rate control**: high-frequency requests (bulk searches, deep comment paging) trigger a captcha, and that platform limit cannot be bypassed. Leave 2-3 seconds between operations.
>
> **Write operations (posting/commenting/liking)**: read-only is recommended. xhs-cli v0.6.x write operations may return 406 because of signature problems.

## Twitter/X (twitter-cli)

> **LOCAL OVERRIDE:** on this machine every `twitter ...` command below runs as `powershell -NoProfile -ExecutionPolicy Bypass -File "C:/Users/TrevorWhite/Downloads/Big Projects/.agents/scripts/x.ps1" <same args>`, which exports the saved cookies and repairs search. Bare `twitter` is blocked by a hook. Skip the auth setup, retry chain and OpenCLI fallback below; x.ps1 search works.

### Authentication prerequisites

The cookies `agent-reach configure twitter-cookies` saves through hidden input are only
used by `agent-reach doctor` to check whether the explicit credentials are complete.
`doctor` does not run the upstream `twitter status`, and does not configure the current
shell. Before running any `twitter` command below, you must supply these explicitly in the
same shell or subprocess environment:

```bash
export TWITTER_AUTH_TOKEN="..."
export TWITTER_CT0="..."
```

### Stable commands

```bash
# Home timeline (the most stable)
twitter feed -n 20

# Read a single tweet (with replies)
twitter tweet URL_OR_ID

# Read a long-form post / X Article
twitter article URL_OR_ID

# User timeline
twitter user-posts @username -n 20

# User profile
twitter user @username
```

### Commands that may be unstable

```bash
# Search tweets (Twitter changes its GraphQL endpoints often, so this may 404)
twitter search "query" -n 10

# likes (since 2024 you can only see your own, a platform limit)
twitter likes
```

### Retry chain when search fails (run in order, stop as soon as one works)

1. Just retry once (intermittent failures are common): `twitter search "query" -n 10`
2. Upgrade, then try again: `pipx upgrade twitter-cli && twitter search "query" -n 10`
3. Switch to the OpenCLI fallback (desktop, reuses the browser login session): `opencli twitter search "query" -f yaml`
4. If none of that works, route around it with stable commands such as `twitter feed` / `twitter user-posts @somebody`

### Important notes

> **Install**: `pipx install twitter-cli` (make sure it is v0.8.5+)
>
> **Authentication**: use only a manual Cookie-Editor export, then set the environment
> variables `TWITTER_AUTH_TOKEN` + `TWITTER_CT0` explicitly; do not rely on automatic
> browser reads.
>
> **IP risk control**: do not call frequently from a VPS or data-center IP, especially followers/following, which risks a ban. Use a residential proxy or a local environment.
>
> **OpenCLI fallback**: if OpenCLI is installed on the desktop, the whole `opencli twitter search/article/user-posts -f yaml` set is available (browser login session, no cookie environment variables needed).
>
> **Output format**: prefer `--yaml` or `--json` for structured output, which is friendlier to AI agents.

## bilibili

> âš ï¸ **Do not use yt-dlp to read bilibili** (its anti-abuse system blocks everything with 412, confirmed in testing with no workaround). Use bili-cli / OpenCLI.

```bash
# Search / trending / video detail (bili-cli, read-only, no login needed)
bili search "query" --type video -n 5
bili hot -n 10
bili video BVxxx

# Subtitles (OpenCLI, needs desktop Chrome)
opencli bilibili subtitle BVxxx
```

> For the detailed commands (audio transcription, direct API fallback) see [references/video.md](video.md).

## V2EX (public API)

No authentication needed; call the public API directly.

### Hot topics

```bash
curl -s "https://www.v2ex.com/api/topics/hot.json" -H "User-Agent: agent-reach/1.0"
```

### Node topics

```bash
# node_name examples: python, tech, jobs, qna, programmers
curl -s "https://www.v2ex.com/api/topics/show.json?node_name=python&page=1" -H "User-Agent: agent-reach/1.0"
```

### Topic detail

```bash
# topic_id comes from the URL, e.g. https://www.v2ex.com/t/1234567
curl -s "https://www.v2ex.com/api/topics/show.json?id=TOPIC_ID" -H "User-Agent: agent-reach/1.0"
```

### Topic replies

```bash
curl -s "https://www.v2ex.com/api/replies/show.json?topic_id=TOPIC_ID&page=1" -H "User-Agent: agent-reach/1.0"
```

### User info

```bash
curl -s "https://www.v2ex.com/api/members/show.json?username=USERNAME" -H "User-Agent: agent-reach/1.0"
```

### Python usage example

```python
from agent_reach.channels.v2ex import V2EXChannel

ch = V2EXChannel()

# Get the hot topics
topics = ch.get_hot_topics(limit=10)
for t in topics:
    print(f"[{t['node_title']}] {t['title']} ({t['replies']} replies)")

# Get the topics for a node
node_topics = ch.get_node_topics("python", limit=5)

# Get a topic's detail + replies
topic = ch.get_topic(1234567)
print(topic["title"], "â€”", topic["author"])

# Get a user's info
user = ch.get_user("Livid")
```

> **Node list**: https://www.v2ex.com/planes

## Reddit (multiple backends, login session required)

> **LOCAL OVERRIDE:** no login is needed here and the backends below are not used. Reddit is read key-free through `.rss`: `python -X utf8 "C:/Users/TrevorWhite/Downloads/Big Projects/sure/tools/social_pulse.py" --topic "<query>" --days 1`, or `--feed "<any reddit .rss url>"`. Reddit allows one anonymous request per ~60s; the script paces and retries. For one thread use the `reddit-thread-analyzer` skill.

**Reddit has no zero-config path**: the anonymous `.json` endpoints are blocked (403), and since 2025-11 the official API's manual review approves almost nothing. Both backends depend on a login session, so first run `agent-reach doctor --json` to see reddit's `active_backend`. Access from mainland China needs a proxy.

### Backend A: OpenCLI (preferred on desktop, reuses the browser login session)

```bash
# Search posts
opencli reddit search "query" -f yaml

# Read the full post + comments
opencli reddit read POST_ID -f yaml

# Browse a subreddit / hot / Popular
opencli reddit subreddit LocalLLaMA -f yaml
opencli reddit hot -f yaml
opencli reddit popular -f yaml

# subreddit metadata (subscriber count, description)
opencli reddit subreddit-info LocalLLaMA -f yaml
```

> Requires Chrome to be open and already logged in to reddit.com in the browser.

### Backend B: rdt-cli (legacy/server fallback, upstream unmaintained since 2026-03)

```bash
rdt search "query" --limit 10   # Search posts
rdt read POST_ID                # Read the full post + comments
rdt sub python --limit 20       # Browse a subreddit
rdt popular --limit 10          # Browse hot posts
rdt all --limit 10              # Browse /r/all
```

> **Install**: `pipx install 'git+https://github.com/public-clis/rdt-cli.git'` (the PyPI release lags, so install v0.4.2+ from GitHub). Run `rdt login` first before you can search and read (on a server with no browser, write the cookies manually, see the doctor hints).
> Prefer `--yaml` output, which is friendlier to AI agents.

### Advanced option: official API + PRAW (only for users who already have credentials)

Users who registered a Reddit script app before 2025-11 (and hold a client_id/client_secret) can use PRAW against the official API (100 QPM free). New applications need manual review and personal projects are almost never approved, so **do not recommend this path to new users**.

## Facebook (OpenCLI, login session required)

Facebook goes through OpenCLI, reusing the facebook.com login session in the user's Chrome. First run `agent-reach doctor --json` to see facebook's `active_backend`, which should normally be `OpenCLI`. Do not recommend Jina/Exa/Graph API as the default path.

```bash
# Search users / pages / posts
opencli facebook search "query" -f yaml

# User or page info
opencli facebook profile zuck -f yaml

# News Feed for the current account
opencli facebook feed --limit 10 -f yaml

# Group list / recent activity visible to the current account
opencli facebook groups --limit 20 -f yaml
```

> Requires Chrome to be open with the OpenCLI extension installed and logged in to facebook.com. Facebook Groups currently only promises the group list and recent activity visible to the current account; it does not promise an API for arbitrary group posts and comments.

## Instagram (OpenCLI, login session required)

Instagram goes through OpenCLI, reusing the instagram.com login session in the user's Chrome. First run `agent-reach doctor --json` to see instagram's `active_backend`, which should normally be `OpenCLI`. Do not fall back to instaloader by default; historically it has been unstable with cookies/401/429.

```bash
# Search users (not a site-wide keyword search over posts)
opencli instagram search "query" -f yaml

# User profile
opencli instagram profile nasa -f yaml

# A user's recent posts
opencli instagram user nasa --limit 12 -f yaml

# Explore / Discover
opencli instagram explore --limit 20 -f yaml

# Saved items for the current account
opencli instagram saved --limit 20 -f yaml
```

> Requires Chrome to be open with the OpenCLI extension installed and logged in to instagram.com. `instagram search` is a user search; to read posts, determine the username first, then use `instagram user USERNAME`. If you hit 429 / login required, have the user log in again in Chrome and lower the request rate.
