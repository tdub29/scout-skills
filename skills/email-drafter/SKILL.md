---
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
# CLAUDE OFFICE SKILL - Enhanced Metadata v2.0
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

# Basic Information
name: email-drafter
description: Draft short, senior-ready work emails the way corporate America actually reads them. Use whenever drafting, replying to, or tightening a one-to-one or team email at work â€” flagging points ahead of a meeting, sending an analysis/attachment, a quick ask, a status flag, a follow-up, a polite decline. Triggers on "draft an email", "reply to this", "write a note to my boss/the team", "send this over", "follow up", "how do I word this email". NOT for multi-email drip/nurture campaigns (use `emails`), cold outreach to strangers (use `cold-email`), or structured status reports/newsletters/incident reports (use `internal-comms`).
version: "2.0.0"
author: Claude Office Skills Contributors
license: MIT

# Categorization
category: productivity
tags:
  - email
  - writing
  - communication
  - work
department: All

# AI Model Compatibility
models:
  recommended:
    - claude-opus-4
    - claude-sonnet-4
  compatible:
    - claude-3-5-sonnet
    - gpt-4o

# MCP Tools Integration
mcp:
  server: office-mcp
  tools:
    - create_docx

# Skill Capabilities
capabilities:
  - email_writing
  - professional_tone
  - template_usage

# Language Support
languages:
  - en
---

# Email Drafter â€” work emails that get read

Draft everyday emails to colleagues, managers, and execs the way they're actually
consumed: on a phone, in about 30 seconds, scanning for what they need before the
next meeting. The job is to be **short, clear, and easy to act on** â€” not polished,
not formal, not complete-sentence-perfect.

Distilled from "Complete Guide to Writing An Email at Work" (Your Finance Brother /
Jonathan, 2026) plus standard corporate email conventions. These are conventions,
not laws â€” adapt to the recipient and culture.

## When to use vs. when not to

| Use this skill for | Use a different skill |
|---|---|
| A note to your boss / a team / an exec | Drip / nurture / lifecycle sequences â†’ `emails` |
| Flagging points ahead of a meeting | Cold outreach to people who don't know you â†’ `cold-email` |
| Sending an analysis or attachment | Status reports, 3P updates, newsletters, incident reports â†’ `internal-comms` |
| A quick ask, follow-up, or polite decline | |

## The playbook (read this first)

1. **Write to the most senior person; CC the rest in descending seniority.**
   Greeting goes to whoever owns the decision. Everyone else is CC'd 2nd, 3rd, 4th
   by rank. If it's a group with no single owner, address "Team".

2. **First names only. Always. Including the CEO.** Never address anyone by last
   name in a work email. "Hi Bob" or just "Bob,". "Team," for a group.

3. **Subject = short and specific.** A few words, to the point.
   *"XYZ analysis â€” ahead of tomorrow's meeting"*, not a sentence.

4. **No monologues.** The reader has ~30 seconds on a phone. A few lines beats four
   paragraphs every time. If you wrote a paragraph, try to make it two bullets.

5. **Lead with the point.** Open with *why this email exists* and any deadline:
   *"Ahead of tomorrow's meeting, please see attachedâ€¦"* Don't bury it under
   "I hope this message finds you well."

6. **Incomplete sentences are fine.** *"Wanted to flag a few points as you review:"*
   reads better than a grammatically complete windup. Throw out the English-teacher
   rules here.

7. **Bullet the things they need to act on.** One scannable item per line.

8. **Offer a live path to close.** End with an easy out:
   *"Let me know if you have questions â€” or if it's easier to catch up live before
   the meeting."* ("Catch up live" = stop by / call / actually talk, vs. more email
   ping-pong.)

9. **Go easy on emojis and acronyms.** A stray acronym the reader doesn't know, or a
   wall of emojis, makes you read as junior. Spell it out the first time.

10. **Sign off simply.** `Best,` then your first name. `Thanks,` works too. Skip
    "Sincerely" / "Warm regards" for routine internal mail.

## Model template

The skeleton that fits most senior-facing work emails:

```
Subject: [3â€“6 words, specific]

[First name / Team],

[One line: why this email + any deadline.] Please see attached for [the thing].

Wanted to flag a few points as you review:
â€¢ [Point one]
â€¢ [Point two]
â€¢ [Point three]

Let me know if you have any questions â€” or if it's easier to catch up live before [the meeting].

Best,
[First name]
```

## Quick scenario variants (kept short on purpose)

**Quick ask**
```
[Name],

Quick one â€” could you [specific ask] by [day]? Need it for [one-line why].

Thanks,
[First name]
```

**Follow-up / nudge**
```
[Name],

Circling back on [thing] from [when]. No rush, just keeping it on your radar â€” anything you need from me to move it forward?

Best,
[First name]
```

**Polite decline**
```
[Name],

Thanks for thinking of me on [thing]. I can't take it on right now â€” [one honest line]. [Optional: alternative / better time.]

Best,
[First name]
```

## Pre-send checklist (the mechanics)

- [ ] **Attachment actually attached.** If the email says "please see attached,"
      confirm the file is on the email *before* you hit send. (The #1 embarrassing miss.)
- [ ] **Recipients ordered by seniority** â€” most senior in To:, rest CC'd in rank order.
- [ ] **First names only** in the greeting.
- [ ] **Subject** short and specific.
- [ ] **Body scans in ~30 seconds** â€” bullets over paragraphs.
- [ ] **No stray acronyms/emojis** that read as junior.

### Outlook "accidental-send" guard

Before composing a draft you might fumble-send half-finished: drop a few junk
characters into the **BCC** line. Outlook treats it as an invalid address and
**blocks Send**, so an itchy trigger finger can't fire off an incomplete email.
Clear the BCC line as the final step before actually sending.

## Output format

When drafting, return:

```
## Email Draft

**Subject:** [short, specific]
**To:** [most senior]   **CC:** [others, descending seniority]

---
[Body â€” first-name greeting, point-first, bulleted, live-path close, simple sign-off]
---

## Notes
- [Attachment to include, if any]
- [Anything to confirm: names, dates, the actual file]
```

## Limitations

- Draft only â€” does not send.
- May not know your org's specific norms (some teams are more formal); adjust.
- Always verify names, dates, figures, and that the attachment is real before sending.
- Not for legal/HR-sensitive messages without review.
