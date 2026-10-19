---
name: ingest
description: When you paste raw human input â€” a call transcript (Grain, Zoom, Granola, Fathom), a text or email from a client/partner/friend, a voice-memo dump, or meeting notes â€” and want it converted into structured work. Extracts decisions, action items (yours vs theirs), bugs/feature requests, and facts worth keeping; files GitHub issues in the right repo, captures to the second-brain vault, and drafts (never sends) the reply. Triggers on "/ingest", "ingest this", "here's my call with X," "here's the transcript," "this is from [person]," "[person] asked me this," "from [person]:", a pasted transcript with speaker labels, or a forwarded client message that clearly expects processing. Personâ†’project routing lives in a private config; unknown senders get asked about once, then remembered.
metadata:
  version: 0.1.0
---

# /ingest â€” Raw human input â†’ structured work

You are a relay hub: clients text you, partners email you, calls get transcribed. Each of these carries decisions, action items, bugs, and facts â€” and processing one by hand means re-explaining the same routine every time. This skill is that routine, written down.

**The contract:** internal, reversible outputs (vault captures, filed issues) happen without ceremony. Outward-facing outputs (replies) are always **drafted, never sent**.

## Files

| Path | What |
|---|---|
| `${MAKERSKILLS_CONFIG:-$HOME/.config/makerskills}/ingest/people.yaml` | Person â†’ project/repo/vault-page/reply-channel routing (private, gitignored) |
| `<vault>/raw/call-<slug>.md` / `<vault>/raw/message-<slug>.md` | Captures, in second-brain's schema |
| `references/people.yaml.example` | Config schema with a worked example |

`<vault>` is `${SECOND_BRAIN_VAULT:-$HOME/Documents/SecondBrain}`.

## Step 0 â€” Get the input and classify it

In order: content in the prompt â†’ clipboard (`pbpaste`) â†’ ask.

Classify by shape, not by what the user called it:

| Shape | Type |
|---|---|
| Speaker labels + timestamps, or a Grain/Zoom/Granola/Fathom URL or header | **call** |
| "from X:" / forwarded text or DM, first-person, short | **message** |
| Email headers or greeting/sign-off structure | **email** (treat as message with formal tone) |
| Unstructured first-person stream ("okay so I was thinkingâ€¦") | **voice-note** (no reply draft; capture + actions only) |

Long transcripts arrive truncated in chat sometimes â€” if the content visibly cuts off mid-sentence, say so and ask for the file (or a path) rather than processing a fragment.

## Step 1 â€” Identify who and which project

Read `people.yaml`. Match participants/senders against `name` and `aliases`.

- **Matched** â†’ you now have the repo, vault page, reply channel, and tone notes. Say which routing you're using in one line ("Routing: Jane â†’ acme-app").
- **Unmatched** â†’ ask once: "Who is this and what project does it belong to?" Then offer to append them to `people.yaml` so the question never repeats. If the user declines to add them, process the input with explicit destinations instead of routed defaults.
- **Multiple projects in one call** (common on partner calls) â†’ split extraction by project; route each piece separately.

## Step 2 â€” Extract

Read the whole input first. Then pull out, with a short verbatim quote or paraphrase anchoring each:

1. **Decisions made** â€” anything settled, including "we're NOT doing X."
2. **Action items â€” mine** â€” things the user owes someone. Include any stated deadline.
3. **Action items â€” theirs** â€” things owed to the user (these become the follow-up section of the reply, not issues).
4. **Bugs & feature requests** â€” anything that should become a GitHub issue. One issue per item, never a grab-bag.
5. **Questions to answer** â€” asked but unanswered in the input.
6. **Facts worth keeping** â€” durable context (pricing mentioned, a person's situation, a tool they use) â†’ vault; a genuinely reusable reference â†’ Keep note (only if the `keep` CLI is authed; skip silently otherwise).

**Name verification rule:** transcripts mishear proper nouns constantly (brand names, people, tools). Before a name lands in an issue title, vault page, or reply, verify the spelling against the routing config, the repo, or a quick search â€” never trust the transcript's spelling of a name you can check.

## Step 3 â€” Show the routing plan

One compact table before acting:

| # | Item | Destination |
|---|---|---|
| 1 | "Bulk-export button on the reports page" | Issue â†’ `myorg/acme-app` |
| 2 | Decision: monthly billing default | vault `Projects/Acme.md` |
| 3 | Reply to Jane | draft below |

Then **proceed without waiting** â€” everything in the table is internal or a draft. Pause for confirmation only when routing is ambiguous (two plausible repos, an unmatched person) or the input includes something sensitive (credentials, legal/financial commitments).

## Step 4 â€” Execute

**Issues** â€” search for duplicates first (`gh issue list --search`), then file with `gh issue create` in the mapped repo. Title = imperative summary; body = context quote from the source, what was asked, and who asked. Apply `issue_labels` from config if set. Never assign anyone but the user.

**Vault capture** â€” one file per ingest, second-brain raw schema:

```markdown
# message-jane-bulk-export (2026-09-04)
source: text message from Jane
project: Acme App

## Summary
â€¦

## Decisions
â€¦

## Action items
- [ ] mine: â€¦
- [ ] theirs: Jane to â€¦

## Filed
- myorg/acme-app#123 â€” Bulk-export button on the reports page
```

Slug: `call-` or `message-` + person + topic. Follow the vault's auto-commit convention (semantic commit per session).

**Todos** â€” action items of "mine" also land wherever the person's `vault_page` tracks tasks, if one is configured.

**Reply draft** â€” in the user's voice for that channel (config `tone` + channel norms: text = brief and casual; email = fuller). Structure when it fits: acknowledge â†’ what I'm doing about it â†’ what I need from you â†’ when they'll hear back. End with the draft in a paste-ready block (compose with `/paste` rules for the channel â€” e.g. no URLs in an X post body). **Never send it.**

## Step 5 â€” Report

Close with a compact recap: TLDR of the input (2â€“3 sentences), decisions, both action-item lists, links to filed issues, the vault file path, and the reply draft. This recap is the deliverable â€” someone who never saw the input should understand what happened and what's next.

## Composes with

- `second-brain` â€” captures land in its `raw/` schema for later compile
- `paste` â€” channel formatting for the reply draft
- `deep-research` â€” when an extracted question needs real research before it's answerable
- `pm` â€” when a call produces enough work to deserve a project card, not just issues

## Notes on quality

- The most common failure is **flattening**: summarizing the input instead of extracting work from it. The test: could the user act on your output without rereading the source?
- Second most common: **issue grab-bags**. "Improvements from call with Jane" is not an issue. One item, one issue, one clear title.
- "Theirs" action items are as valuable as "mine" â€” they're the follow-up ledger. Don't drop them because no tool call captures them.
- A voice-note ingest with zero action items is fine: capture it, say so, stop. Not every input contains work.
