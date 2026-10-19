---
name: reddit-thread-analyzer
description: "Sentiment and consensus in a Reddit thread"
---

# Reddit Thread Analyzer

Extract deep insights from Reddit discussions including sentiment, key arguments, and community consensus.

When a user provides a Reddit thread URL or asks about Reddit opinions, analyze the discussion comprehensively to surface meaningful patterns and insights.

## Instructions

### 1. Fetch and Parse Thread Data

**Do not use WebFetch on a Reddit URL from this machine. It returns an ~8 KB stub with
zero comments and looks like a success.** Verified 2026-08-25 against a live r/stocks
thread: the HTML answers 200 at 8,435 bytes with no `<shreddit-comment>` element,
`.json` answers 403 (a 189 KB block page), and only `.rss` returns the real thread at
26 KB with 33 comment entries.

Append `.rss` to the permalink and parse the Atom:

```python
import re, time, urllib.request, urllib.error
from xml.etree import ElementTree as ET

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
A = "{http://www.w3.org/2005/Atom}"

def thread(permalink, tries=4):
    url = permalink.rstrip("/") + "/.rss"
    for i in range(tries):
        try:
            raw = urllib.request.urlopen(
                urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30).read()
            break
        except urllib.error.HTTPError as e:
            if e.code != 429 or i == tries - 1:
                raise
            time.sleep(20 * (i + 1))          # a 429 here is our own throttling
    for e in ET.fromstring(raw).findall(A + "entry"):
        yield {
            "author": e.findtext(A + "author/" + A + "name"),
            "text": re.sub(r"<[^>]+>", " ", e.findtext(A + "content") or ""),
            "updated": e.findtext(A + "updated"),
            "url": (e.find(A + "link") or {}).get("href"),
        }
```

Two traps that make a working setup look broken:

1. **Send a browser User-Agent.** With none, or with a tool-shaped one, you get sporadic
   429s. **A 429 here is your own rate limiting, not a block** - the same URL returns 200
   on retry. Space calls ~15 s apart and retry before concluding anything.
2. **Windows consoles are cp1252 and Reddit text is not.** Printing a comment can raise
   `UnicodeEncodeError` after the fetch already succeeded. Reconfigure stdout to UTF-8.

What you get: post title and body, author handles, all comments including nested ones,
and timestamps.

**What Atom does not carry: scores, awards, and flair.** Steps below that rank by comment
score cannot be satisfied from this route. Rank by recency and by how often an argument
recurs across comments, and say plainly in the output that vote counts were unavailable
rather than estimating them. Never invent a score.

For a ticker-level pulse across many threads plus X, use `tools/social_pulse.py` instead of
analyzing one thread at a time.

### 2. Analyze Overall Sentiment

Determine the dominant sentiment and emotional tone:
- **Overall sentiment**: Positive, negative, neutral, or mixed
- **Sentiment distribution**: Approximate percentages
- **Emotional tone**: Excited, frustrated, skeptical, supportive, angry, enthusiastic
- **Shift over time**: Note if sentiment changes throughout discussion

### 3. Extract Key Arguments

Identify the most impactful points:

**Top Arguments in Favor** (3-5 points):
- Quote the argument
- Note comment score
- Identify supporting evidence or reasoning

**Top Arguments Against** (3-5 points):
- Quote the argument
- Note comment score
- Identify counter-points and rebuttals

**Expert or Verified Opinions**:
- Highlight comments from verified experts
- Note OP responses and clarifications

### 4. Find Consensus Points

Determine what the community agrees on:
- Points with broad agreement (high scores, no controversy)
- Emerging patterns across multiple comments
- Common ground between opposing viewpoints

### 5. Identify Controversial Topics

Flag heavily debated points:
- Topics with mixed upvotes/downvotes
- Arguments that sparked long comment chains
- Divisive issues where community is split

### 6. Provide Structured Analysis

Format your analysis clearly:

```markdown
# Reddit Analysis: [Thread Title]

## Executive Summary
[2-3 sentence overview of the discussion and main takeaway]

## Overall Sentiment
- **Dominant Sentiment**: Positive/Negative/Neutral/Mixed (X%)
- **Emotional Tone**: [excited/frustrated/skeptical/etc.]
- **Community Alignment**: High/Medium/Low

## Top Arguments

### In Favor
1. **[Main point]** (+XXX score)
   > "[Direct quote from comment]"
   - [Brief explanation of reasoning]

2. **[Main point]** (+XXX score)
   > "[Direct quote]"

### Against
1. **[Main point]** (+XXX score)
   > "[Direct quote]"

## Community Consensus
- âœ… [Point most people agree on]
- âœ… [Another consensus point]

## Controversial Topics
- âš ï¸ [Divisive issue] - Community split roughly 50/50
- âš ï¸ [Another debate point]

## Notable Insights
- **Expert Opinion**: [Quote from verified expert] (+XXX)
- **Surprising Take**: [Unexpected perspective that gained traction]
- **Most Helpful**: [Most practical or actionable advice]

## Key Quotes
> "[Memorable quote]" - u/username (+XXX score)
> "[Another impactful quote]" - u/username (+XXX score)

## Discussion Quality
- Civility: High/Medium/Low
- Depth: Superficial/Moderate/Deep
- Evidence-based: Yes/No/Mixed
```

## Best Practices

- **Focus on highly upvoted comments** for consensus
- **Include exact scores** to show community agreement level
- **Quote directly** rather than paraphrasing
- **Preserve nuance** - avoid oversimplifying complex debates
- **Note OP responses** - original poster often adds important context
- **Distinguish facts from opinions** clearly
- **Highlight constructive vs. unproductive** discussions
- **Consider recency** - early comments may be less informed than later ones

## Example Analysis

**User**: "What does Reddit think about the new iPhone?"

**Your analysis**:
1. Fetch r/apple or r/iPhone thread
2. Analyze 300+ comments
3. Determine sentiment: Mixed (55% positive, 45% negative)
4. Extract top pros: Camera improvements (+450), Performance (+380)
5. Extract top cons: High price (+420), Incremental updates (+390)
6. Note consensus: Good phone, but expensive for what you get
7. Identify controversy: Whether it's worth upgrading from iPhone 14
8. Surface expert opinions from tech reviewers
9. Deliver structured report with quotes and scores

---

**Remember**: Focus on substance over noise. Prioritize well-reasoned arguments over emotional reactions.
