# Company Brain schema (fallback)

**Authoritative source: `<vault>/CLAUDE.md`.** This file is a fallback used only when the vault's CLAUDE.md is missing.

Use this as a starter kit when seeding a new team's vault.

---

## Folder structure

```
people/                â†’ Contacts with context (CRM-lite)
companies/             â†’ Org profiles (prospects, clients, partners)
meetings/              â†’ Call/meeting transcripts + notes
sops/                  â†’ Standard operating procedures
decisions/             â†’ Decision records (narrative form)
customer-language/     â†’ Verbatim phrases from customers/prospects
recurring-questions/   â†’ Questions asked 3+ times â†’ pre-answered
sales-objections/      â†’ Objection library + best responses
raw/                   â†’ Uncategorized fallback (minimize use)
wiki/                  â†’ AI-compiled knowledge base
  INDEX.md             â†’ Master index
outputs/               â†’ Saved Q&A results, briefs, deliverables
Projects/              â†’ Team task management (DO NOT modify â€” pm owns it)
Team/                  â†’ Internal team-only files (DO NOT modify)
Templates/             â†’ Note templates (DO NOT modify)
Drafts/                â†’ In-progress private drafts (DO NOT modify)
```

## File naming conventions

### `people/`
- Filename: `<first-name-last-name>.md` (kebab-case, unambiguous per person)
- If two people share a name: `<name>-<company>.md` or `<name>-<role>.md`

### `companies/`
- Filename: `<company-slug>.md` (short, memorable)

### `meetings/`
- Filename: `YYYY-MM-DD-<company-or-topic>-<slug>.md`
- Examples: `2026-06-15-acme-discovery.md`, `2026-06-30-q3-planning.md`

### `sops/`
- Filename: `<team>-<process>.md`
- Examples: `sales-outbound-cadence.md`, `ops-client-onboarding.md`, `content-blog-review.md`

### `decisions/`
- Filename: `YYYY-MM-DD-<decision-slug>.md`
- Example: `2026-06-30-pricing-restructure.md`

### `customer-language/`
- Filename: `<theme-slug>.md` (grouped by theme, not per customer)
- Examples: `pricing-anchoring.md`, `willingness-to-pay.md`, `decision-triggers.md`
- Append new verbatims to existing themed files; only create new files for new themes

### `recurring-questions/`
- Filename: `<question-slug>.md`
- Example: `how-do-you-handle-migration.md`
- Include a counter at the top: `asked_count: 7`

### `sales-objections/`
- Filename: `<objection-slug>.md`
- Examples: `too-expensive.md`, `we-already-have-a-tool.md`, `no-budget-this-quarter.md`

## File front-matter (all structured dirs)

Every file starts with:

```markdown
source: <URL / call with X on YYYY-MM-DD / email from Y / manual entry>
author: <who captured this â€” email or handle>
captured: YYYY-MM-DD
trust: unreviewed       # unreviewed / verified / deprecated / superseded
sensitivity: internal   # or leadership / confidential
```

**`trust` is deliberately not named `status`** â€” `companies/` and `decisions/` already use `status:` for lifecycle (prospect/customer, decided/reversed). The two fields coexist and must not collide. Files with no `trust:` field (pre-trust-levels vaults) are treated as `unreviewed`.

Every `/cb review` disposition except skip stamps:
```markdown
reviewed: YYYY-MM-DD
reviewed_by: <handle>
```

Verified files: `trust: verified`. Deprecated/superseded files additionally carry:
```markdown
trust: deprecated       # or superseded
superseded_by: [[replacement-page-or-file]]   # superseded only
```

For `people/` files, extend with:
```markdown
role: <current role>
company: <current company>
last_touch: YYYY-MM-DD
tags: [customer, prospect, partner, investor, alumni, ...]
```

For `companies/` files, extend with:
```markdown
industry: <industry>
size: <headcount range>
status: [prospect, customer, churned, partner, competitor]
opportunity_size: <ARR / TCV range>
last_touch: YYYY-MM-DD
account_owner: <team member>
```

For `meetings/` files, extend with:
```markdown
attendees: [name1, name2, name3]
company: <company slug if external>
duration_min: <int>
recording_url: <if available>
```

For `sops/` files, extend with:
```markdown
owner: <team member responsible>
last_reviewed: YYYY-MM-DD
review_cadence: <quarterly | annually | ad-hoc>
```

For `decisions/` files, extend with:
```markdown
deciders: [name1, name2]
review_by: YYYY-MM-DD  # scheduled re-evaluation
status: [decided, in-effect, reversed, superseded]
```

## wiki/ page format

Same as `second-brain`:

```markdown
# Topic Name

Brief summary (2â€“3 sentences).

## Key Concepts
- Concept with explanation

## Details
Main content organized by subtopic.

## Connections
- [[Related Topic]] â€” how it connects

## Sources
- `people/jane-doe.md` (added by @alex, 2026-06-30) â€” role + context
- `meetings/2026-06-15-acme-discovery.md` (added by @sam) â€” objection notes
- `companies/acme.md` (added by @alex, updated by @sam) â€” deal state
```

**Cite by source file + author + optional date.** Multi-author attribution is the discipline that makes the vault trustworthy at team scale.

## wiki/INDEX.md format

```markdown
# Wiki Index

## Sales
- [[Acme Corp Deal]] â€” Active Q3 opportunity, $180K TCV
- [[Pricing Objections]] â€” Standard responses to price pushback

## Customers
- [[Beta Customer Feedback Themes]] â€” Aggregated themes from Q2 feedback

## Ops
- [[Client Onboarding Flow]] â€” 6-step process

## Product
- [[Roadmap Q3]] â€” Prioritized initiatives

## Team & People
- [[Team Directory]] â€” Who does what
- [[Key Contacts at Partners]] â€” Named POCs at partner orgs

## Decisions
- [[Pricing Restructure June 2026]] â€” Rationale + expected outcome + review date

## Playbooks
- [[Sales Outbound Playbook]] â€” Cadence, templates, escalation
```

Extend categories as the team's brain matures.

## Sensitivity levels

| Level | Access |
|---|---|
| `internal` | Any team member (default) |
| `leadership` | Named leadership list only (list in `Team/leadership.md`) |
| `confidential` | Named list per file (list in file front-matter or `Team/confidential-access.md`) |

Wiki pages inherit the *highest* sensitivity of any source. If a wiki page cites 4 `internal` sources and 1 `confidential`, the wiki page is `confidential`.

## Trust levels (`trust:`)

| Trust | Meaning | Query treatment | Compile treatment |
|---|---|---|---|
| `unreviewed` | No human has confirmed it (default for new captures; also how files with no `trust:` field are treated) | Usable but flagged â€” answers note lower confidence | Included; pages mostly built on it get a warning callout |
| `verified` | Human-reviewed and confirmed | Full weight | Included |
| `deprecated` | Wrong or obsolete | Never used as context | Excluded; noted in Sources with `reviewed` date + `reviewed_by` |
| `superseded` | Replaced (`superseded_by: [[target]]`) | Never used; queries point to the replacement | Excluded; Sources link to replacement |

Trust is orthogonal to sensitivity. Trust changes happen through `/cb review` (the human triage pass, which respects sensitivity â€” reviewers only see files at or below their level) â€” capture always starts at `unreviewed`.

## Rules

- **One page per concept** â€” not per source. Multiple raw files about the same customer merge into one wiki page.
- **Use `[[wikilinks]]`** for all internal references
- **Keep pages focused** â€” split if >500 words
- **INDEX.md is the root** â€” keep current
- **Connections section is mandatory** â€” every page links to â‰¥1 other page
- **No orphan pages**
- **Preserve nuance** â€” don't flatten contradictions between authors' captures; note the disagreement
- **Multi-author attribution required** in Sources sections
- **Sensitivity respected** in query mode
- **Deprecate, don't delete** â€” wrong/stale info gets `trust: deprecated` (or `superseded` + pointer), never removed
- **Trust respected end-to-end** â€” deprecated/superseded content never used as context in query or compile

## Publishing (same as second-brain)

Use pandoc + shared stylesheet at `~/.local/share/makerskills/render.css`:

```bash
pandoc "outputs/<file>.md" \
  --css ~/.local/share/makerskills/render.css \
  --metadata title="<title>" \
  --pdf-engine=xelatex \
  -o "outputs/<file>.pdf"
```

Company brain outputs commonly leave the vault as: client-facing briefs, quarterly reviews, sales enablement PDFs, onboarding docs. Same rendering pattern as second-brain.
