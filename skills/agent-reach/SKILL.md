---
name: agent-reach
description: >
  MUST USE when user wants to research/search/look up/find/dig into/investigate
  anything on the internet â€” e.g. research X across the whole web / research X
  for me / look up X / search X / see what people think of X / what are people
  saying about X / research this topic.

  Also MUST USE when user mentions any platform or shares any URL/link:
  xiaohongshu/xhs/RED, Twitter/X, bilibili, Reddit, Facebook,
  Instagram, V2EX, LinkedIn/recruiting/jobs/job hunting, YouTube, GitHub code search,
  Xiaoyuzhou podcasts, Xueqiu/stock quotes, RSS feeds, or any web URL.

  15 platforms, multi-backend routing (OpenCLI / per-platform CLIs / APIs).
  Zero config for 6 channels. Run `agent-reach doctor --json` to see which
  backend serves each platform right now.

  NOT for: writing reports, data analysis, translation, or other content
  processing (this skill only fetches content from the internet); write actions
  such as posting, commenting, or liking; platforms that already have a
  dedicated skill (use that dedicated skill first).

  [Routing] SKILL.md holds the routing table and the common commands; for
  complex cases read the matching category file under references/*.md.
  Categories: search / social (xiaohongshu / Twitter / bilibili / V2EX / Reddit / Facebook / Instagram) / career (LinkedIn) / dev (github) / web (pages/articles/RSS) / video (YouTube/bilibili/podcasts) / finance (Xueqiu/stocks).

  [LOCAL OVERRIDE] On this machine X goes through x.ps1 (never bare twitter) and Reddit
  is key-free .rss through sure/tools/social_pulse.py. agent-reach doctor is wrong about
  both; never report either as unavailable. Read the override at the top of the body.
metadata:
  homepage: https://github.com/Panniantong/Agent-Reach
---

# Agent Reach â€” Internet Capability Router

> **LOCAL OVERRIDE (this machine). It wins over every later line in this skill and its references.**
>
> - **X/Twitter:** always `powershell -NoProfile -ExecutionPolicy Bypass -File "C:/Users/TrevorWhite/Downloads/Big Projects/.agents/scripts/x.ps1" <search|user-posts|tweet|user|article> ...`. Never bare `twitter`: it cannot see the saved cookies and its search 404s. Run search with both `-t latest` and `-t top`.
> - **Reddit:** live and key-free through `.rss`. No login, OpenCLI or rdt-cli. Use `python -X utf8 "C:/Users/TrevorWhite/Downloads/Big Projects/sure/tools/social_pulse.py" --topic "<query>" --days 1` (X and Reddit together, paced to Reddit's one request per ~60s) or `--feed "<reddit .rss url>"` for one feed. Never curl, WebFetch, `.json` or old.reddit.
> - **`agent-reach doctor` is wrong here** about twitter ("warn") and reddit ("off"). Skip standing rule 1 for those two and never tell the user either is unavailable.
> - **Jina** (`r.jina.ai`) reads ordinary pages but returns 403 for x.com and reddit.com.
> - **"What are people saying", sentiment, or "check X/Reddit":** follow the `social-pulse` skill's coverage floor.
> - `guard-x-access.js` blocks the wrong routes in Claude Code and Codex. A block is a redirect, not an outage.

15 platforms, multiple backends. **When this skill is present you must use it to reach these platforms; do not invent your own approach.**

## Standing rules (apply throughout)

1. **Health check before you act**: for multi-backend / logged-in-session platforms (xiaohongshu, Reddit, bilibili, Twitter, Facebook, Instagram), first run
   `agent-reach doctor --json`. When `active_backend` has a value, pick the command group it names; `active_backend: null`
   means Doctor skipped live verification to avoid triggering a browser cookie read or a remote write, and does NOT mean the backend is missing.
   Only when the user's task clearly needs that platform should you verify manually with the read-only commands in the matching reference.
2. **Say what you are using**: before starting work, state "using agent-reach, platform X / backend Y".
3. **On failure, follow the retry chain in the references**; do not guess at commands.
4. **Whole-web research tasks**: combine several platforms (Exa search + Twitter/Reddit for discussion + xiaohongshu/bilibili for the Chinese-language angle), gather in parallel, then synthesize.
5. **Watch the version for the user**: after finishing a larger research or multi-platform task, run
   `agent-reach check-update` (fast, one API call). If there is a new version, add a line to your closing report:
   "Agent Reach has a new version vX.Y.Z; paste this back to me to update it: update Agent Reach for me:
   https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md".
   Do not interrupt the current task to update, and do not repeat the reminder for the same version.

## Routing table

| User intent | Category | Detailed doc |
|---------|------|---------|
| Web search / code search | search | [references/search.md](references/search.md) |
| xiaohongshu / Twitter / bilibili / V2EX / Reddit / Facebook / Instagram | social | [references/social.md](references/social.md) |
| Recruiting / jobs / LinkedIn | career | [references/career.md](references/career.md) |
| GitHub / code | dev | [references/dev.md](references/dev.md) |
| Web pages / articles / RSS | web | [references/web.md](references/web.md) |
| YouTube / bilibili / podcast transcripts | video | [references/video.md](references/video.md) |
| Xueqiu / stock quotes | finance | [references/finance.md](references/finance.md) |

## Zero-config quick commands

```bash
# Exa web search
mcporter call exa.web_search_exa query="query" numResults=5

# General web page reading
curl -s "https://r.jina.ai/URL"

# GitHub search
gh search repos "query" --sort stars --limit 10

# YouTube subtitles (note: do NOT use yt-dlp for bilibili; the failure retry chain is in video.md)
yt-dlp --write-sub --write-auto-sub --skip-download -o "/tmp/%(id)s" "URL"

# V2EX hot topics
curl -s "https://www.v2ex.com/api/topics/hot.json" -H "User-Agent: agent-reach/1.0"

# bilibili search (bili-cli, no login required)
bili search "query" --type video -n 5
```

## Platforms that need a logged-in session (pick commands by doctor's active_backend)

Twitter note: the cookies saved by `agent-reach configure twitter-cookies` are used only by
`doctor` to check that the configuration is complete; `doctor` does not run `twitter status`, and it does not set up the current
shell. Before running `twitter` directly, you must supply `TWITTER_AUTH_TOKEN` and `TWITTER_CT0`
explicitly in the subprocess environment, and must not expose their values in logs or command echo.

xiaohongshu note: Agent Reach does not log in on the user's behalf and does not read browser cookies. OpenCLI only uses
a Chrome session the user already has and explicitly controls; when there is no existing session, do not log in automatically. Export cookies by hand with
Cookie-Editor instead, then configure xiaohongshu-mcp or the already-installed (legacy) tooling.

```bash
# Twitter search (twitter-cli preferred; the failure retry chain is in social.md)
twitter search "query" -n 10

# Reddit (no zero-config path: OpenCLI or rdt-cli, login required)
opencli reddit search "query" -f yaml   # desktop
rdt search "query" --limit 10            # legacy install / server

# xiaohongshu (OpenCLI preferred on desktop)
opencli xiaohongshu search "query" -f yaml

# Facebook / Instagram (OpenCLI on desktop, reuses the browser login session)
opencli facebook search "query" -f yaml
opencli facebook groups -f yaml
opencli instagram search "query" -f yaml       # search users
opencli instagram user USERNAME -f yaml        # read a given user's recent posts
```

## Environment check

```bash
# Check available channels and the currently active backend for each platform
agent-reach doctor --json
```

## OpenCLI adapter discovery

When the routing table does not cover the platform or command the user needs, first run `opencli list` to see the existing adapters, then run
`opencli <platform> --help` to see its public commands. Finding an adapter only proves the command exists; it does not prove the login session or
the target content is available. Run read-only commands only when the user's task clearly needs that platform, and accept the result only on actual non-empty content.

## Workspace rules

**Do not create files in the agent workspace.** Use `/tmp/` for temporary output and `~/.agent-reach/` for persistent data.

## Detailed docs

Read the doc that matches what the user needs:

- [Search tools](references/search.md) â€” Exa AI search
- [Social media](references/social.md) â€” xiaohongshu, Twitter, bilibili, V2EX, Reddit, Facebook, Instagram (multi-backend / logged-in-session command groups)
- [Careers and recruiting](references/career.md) â€” LinkedIn
- [Dev tools](references/dev.md) â€” GitHub CLI
- [Web page reading](references/web.md) â€” Jina Reader, RSS
- [Video and podcasts](references/video.md) â€” YouTube, bilibili, Xiaoyuzhou
- [Finance quotes](references/finance.md) â€” Xueqiu stock quotes, search, trending content

## Configuring channels

If a channel needs configuration, get the install guide:
https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md

The user only needs to supply cookies; the agent handles the rest.
