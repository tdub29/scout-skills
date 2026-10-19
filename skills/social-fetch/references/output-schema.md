# Normalized output schema

Same shape returned for every platform. Fields with no equivalent on a platform get `null`, not zero or empty string. Missing â‰  zero.

## Schema

```typescript
{
  "platform": "x" | "linkedin" | "linkedin-profile" | "instagram" | "tiktok"
    | "bluesky" | "reddit" | "mastodon" | "threads" | "hn",
  "url": string,                 // canonical URL of the post
  "fetched_at": ISO8601,
  "raw_source":                   // which strategy succeeded
    "agent-reach" | "direct-api" | "oembed" | "web-get"
    | "browser-use" | "wayback" | "scrapecreators" | "apify",

  "author": {
    "handle": string | null,      // @username
    "name": string | null,        // display name
    "verified": boolean | null,
    "follower_count": number | null,
    "profile_url": string | null,
    "avatar_url": string | null
  },

  "posted_at": ISO8601 | null,
  "edited_at": ISO8601 | null,

  "text": string,                 // post body, plain text. Markdown OK if source supports it.
  "html": string | null,          // original HTML if scraped (Mastodon, etc.)
  "language": string | null,      // ISO 639-1 if detected

  "media": Array<{
    "type": "image" | "video" | "gif" | "audio",
    "url": string,
    "alt": string | null,
    "width": number | null,
    "height": number | null,
    "duration_seconds": number | null    // video/audio only
  }>,

  "engagement": {
    "likes": number | null,         // tweets/posts: likes. Reddit: upvotes.
    "reposts": number | null,       // retweets, shares, reposts, reblogs
    "replies": number | null,
    "bookmarks": number | null,
    "views": number | null,
    "quotes": number | null         // quote-tweets where applicable
  },

  "links": Array<{                  // links cited in the post body
    "url": string,
    "expanded_url": string,         // resolved if t.co or similar shortener
    "title": string | null
  }>,

  "mentions": string[],             // @handles mentioned
  "hashtags": string[],

  "is_reply": boolean,
  "reply_to": {                     // if is_reply = true
    "url": string,
    "author_handle": string
  } | null,

  "is_thread": boolean,             // post is part of a multi-post thread by same author
  "thread": Array<{                 // siblings in the thread (excludes self), in order
    "url": string,
    "text": string,
    "posted_at": ISO8601
  }>,

  "replies": Array<{                // top-level replies (only if --with-replies)
    "url": string,
    "author": { "handle": string, "name": string },
    "text": string,
    "posted_at": ISO8601,
    "engagement": { "likes": number, "replies": number }
  }>,

  "raw": object | null               // raw API/scrape response (only if --raw)
}
```

## Platform field-coverage matrix

What each platform typically provides on a successful free-strategy fetch:

| Field | bluesky | mastodon | hn | reddit (free) | x (free, oEmbed) | x (paid) | linkedin (free) | linkedin (paid) | ig (paid) | tiktok (free, oEmbed) | tiktok (paid) | threads (paid) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| author.handle | âœ… | âœ… | âœ… | ðŸ”’ | âœ… | âœ… | partial | âœ… | âœ… | âœ… | âœ… | âœ… |
| author.verified | â€” | â€” | â€” | ðŸ”’ | â€” | âœ… | â€” | âœ… | âœ… | â€” | âœ… | âœ… |
| author.follower_count | âœ… | âœ… | â€” | ðŸ”’ | â€” | âœ… | â€” | âœ… | âœ… | â€” | âœ… | âœ… |
| posted_at | âœ… | âœ… | âœ… | ðŸ”’ | âœ… | âœ… | partial | âœ… | âœ… | â€” | âœ… | âœ… |
| text | âœ… | âœ… | âœ… | ðŸ”’ | âœ… | âœ… | partial | âœ… | âœ… | âœ… (caption) | âœ… | âœ… |
| media | âœ… | âœ… | â€” | ðŸ”’ | â€” | âœ… | â€” | âœ… | âœ… | thumbnail only | âœ… | âœ… |
| engagement.likes | âœ… | âœ… | âœ… (score) | ðŸ”’ | â€” | âœ… | â€” | âœ… | âœ… | â€” | âœ… | âœ… |
| engagement.reposts | âœ… | âœ… | â€” | ðŸ”’ | â€” | âœ… | â€” | âœ… | â€” | â€” | âœ… | âœ… |
| engagement.views | â€” | â€” | â€” | ðŸ”’ | â€” | âœ… | â€” | partial | partial | â€” | âœ… | partial |
| replies | âœ… | âœ… | âœ… | ðŸ”’ | â€” | âœ… | â€” | partial | â€” | â€” | partial | partial |
| thread (own author) | âœ… | âœ… | n/a | ðŸ”’ | â€” | âœ… | â€” | âœ… | â€” | n/a | â€” | partial |

`partial` = sometimes available depending on the post and whether the auth wall engaged.
`ðŸ”’` = the whole column is locked, not the individual field: Reddit has no working free path at all
(`.json` returns 403, `web-get.mjs` hits a bot challenge). Instagram and Threads have no free column
here for the same reason. See `strategies.md` for what would unblock each.

## Example outputs (abbreviated)

### bluesky â€” full

```json
{
  "platform": "bluesky",
  "url": "https://bsky.app/profile/jay.bsky.team/post/3kphvqpv6xs2t",
  "raw_source": "direct-api",
  "author": {
    "handle": "@jay.bsky.team",
    "name": "Jay Graber",
    "verified": null,
    "follower_count": 500123
  },
  "posted_at": "2026-06-15T14:23:00Z",
  "text": "We're rolling out video posts.",
  "media": [],
  "engagement": {
    "likes": 1245, "reposts": 234, "replies": 89, "bookmarks": null, "views": null
  }
}
```

### x â€” partial (free strategy: oEmbed)

This is what the only working key-free X path actually returns. Everything oEmbed does not carry is
`null`, never `0`.

```json
{
  "platform": "x",
  "url": "https://x.com/example/status/1234567890",
  "raw_source": "oembed",
  "author": {
    "handle": "@example",
    "name": "Example User",
    "verified": null,
    "follower_count": null
  },
  "posted_at": "2026-06-17T00:00:00Z",
  "text": "The 80/20 of a useful AI second brain: ...",
  "engagement": {
    "likes": null, "reposts": null, "replies": null, "bookmarks": null, "views": null
  },
  "is_thread": null,
  "thread": []
}
```

Note every engagement field is `null` and `is_thread` is `null`, not `false` â€” oEmbed gives no signal
either way, and claiming `false` would be inventing data. `posted_at` is date-only (oEmbed's blockquote
carries "March 21, 2006", not a timestamp), so do not fabricate a time-of-day. Full engagement,
replies and thread siblings need the X channel unlocked or a paid key; see `strategies.md`.

### hn â€” full

```json
{
  "platform": "hn",
  "url": "https://news.ycombinator.com/item?id=12345678",
  "raw_source": "direct-api",
  "author": { "handle": "pg" },
  "posted_at": "2026-06-15T18:00:00Z",
  "text": "Title of the submission",
  "links": [{"url": "https://example.com/article", "expanded_url": "https://example.com/article"}],
  "engagement": { "likes": 234, "replies": 89 },
  "replies": [
    {
      "url": "https://news.ycombinator.com/item?id=12345679",
      "author": { "handle": "user1" },
      "text": "Great article becauseâ€¦",
      "engagement": { "likes": 45, "replies": 3 }
    }
  ]
}
```

## Returning to the user

When the skill completes, output:

1. **One-line summary** in chat: `<author> Â· <platform> Â· <date> Â· "<first 80 chars>..."`
2. **Path to the JSON output** if `--save` flag set (saved to `~/Documents/social-fetches/<platform>-<id>.json`)
3. **Inline JSON** in chat for the calling skill / the user to use

Always name the rung that produced the answer ("oEmbed", "web-get.mjs", "agent-reach"), so the next
agent knows how much to trust it.

If only partial data was retrievable, surface it clearly: *"X oEmbed returned author + text + date.
Engagement, replies and thread siblings are unavailable â€” the agent-reach twitter channel is locked
(twitter-cli not installed). See references/strategies.md for what would unblock it."*

If nothing was retrievable, say so and stop: *"Reddit is locked. `.json` returns 403 and web-get.mjs
hits the bot challenge; no Wayback snapshot exists. Unblocking needs OpenCLI plus a logged-in Chrome,
which is your call."* Never pad an empty fetch with recalled or inferred content.
