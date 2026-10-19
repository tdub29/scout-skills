---
name: one-person-ai-business
description: >-
  Design and run a one-person business as five bounded agent lanes - each agent
  one job, all reading one shared business brain, with bounded memory, schedules,
  spend caps, and money/outside-world actions held behind human approval. Use for
  a one-person business, a solo AI business system, agent lane design, building a
  business brain, or scaling a solo business with agents.
metadata:
  version: 1.0.0
  source: "EXM7777/one-person-ai-business (X article, 2026-07-25, sponsored)"
---

# One-person AI business: five bounded agent lanes

Run a solo business as five agent lanes that produce on autopilot while a human
only decides. This skill is the vendor-neutral operating system extracted from
the source below, plus a concrete lane design for the PRTL repo (Expo/RN +
Express digital art-frame product, personal). It defines its own brain, memory,
gate, and cap machinery inline - PRTL does not yet ship dedicated skills for
those (see "PRTL capability map").

## Attribution and sponsorship disclosure (preserve verbatim)

- Source: Machina (@EXM7777), "How to build and scale a one-person business with
  AI", X (twitter), published 2026-07-25 (~498.6K views). Author bio: "running
  ai-powered agencies | weeklyaiops.com".
- **This piece is SPONSORED.** The author's closing line: "thank you Viktor for
  sponsoring this piece, get $100 in free credits at viktor.com".
- Therefore every claim about **Viktor** specifically (that it is an "AI
  employee", joins Slack/Teams, has thousands of connectors, starts free, $100
  free credits) is **promotional / vendor claim, NOT evidence.** Do not adopt any
  Viktor claim as fact and do not treat the vendor as recommended. Adopt only the
  vendor-neutral practices below, which stand on their own.

## The reusable system (vendor-neutral)

1. **Two assets, wired together.** (a) Software that already wins at its job
   (billing, CRM, scheduling, ad delivery) - the job left there is *operating*.
   (b) Your business knowledge (who the client is, what you charge, what a good
   lead looks like, what gets escalated, how delivery works). An AI worker is the
   operator in the middle that used to be a hire.
2. **Five work lanes:** content, projects, outreach, finance, ads. Each lane is
   isolated (one channel or one agent per lane) - never one giant assistant for
   everything.
3. **One agent, one job.** A researcher only researches; a writer only writes; a
   reviewer is *never* the author (an agent grading its own work approves it every
   time). Each specialist = four parts: identity file (who it is + hard "never"s,
   durable) / its slice of the brain / its bounded memory / a schedule + a gate.
   Keep identity separate from memory so a passing fact can never rewrite who the
   agent is.
4. **One shared business brain.** A folder of linked markdown files every
   specialist reads. Notes, one per fact cluster: **offer** (what you sell,
   pricing, scope) / **client** (who buys, verticals, qualified-lead definition) /
   **voice** (how you write, banned words, best-work examples) / **playbooks**
   (how work runs, stage by stage, with checklists) / **rulings** (every decision
   that must never be re-argued). The rulings note is the one everyone skips and
   everyone needs: every correction becomes one line there, read before work - so
   a correction is permanent, not repeated.
5. **Bounded memory, three levels - stop at the lowest that solves your problem.**
   L1 files (markdown loaded at startup); L2 a memory product (meaning-based
   retrieval, e.g. when material outgrows context); L3 a graph (entities + facts
   with time windows, for "what changed when"). Most solo businesses never leave
   L1. Cap always-loaded core small (working agents cap memory files ~a few
   hundred lines, load the rest on demand). The hard half is forgetting.
6. **Schedules before prompts.** A recurring job ("every workday 08:00 post a
   standup") is one sentence in the brief, not a manual poke.
7. **Approval gates by blast radius.** Routine internal work runs unattended;
   anything that sends or spends waits for a human yes.
8. **Spend caps on day one.** Set a hard monthly cap before the first brief;
   put quote-before-execute in every context message.
9. **Reviewer separation.** The reviewer is a different agent than the author.
10. **Scale criterion (one question, asked before every addition):** *did the
    last lane produce this morning without a prompt from me?* Only then add the
    next lane. Start with the one lane where you lose the most hours.

### Operating rules (the management counterweight)

A staff that never pushes back and never flags its own doubt needs the operator
to supply the doubt. (a) The brief carries the context - name the deliverable
and what "done" means; a lazy brief produces confident work in the wrong
direction. (b) Permissions by blast radius. (c) You review on a schedule - two
windows a day to clear the drafts/approvals queue. (d) Cap the bill before it
teaches you. Skip the cap and you edit forever; skip the scale gate and the bill
teaches you instead.

## Vendor-neutral vs vendor-specific (keep separate)

| Vendor-neutral practice (adopt) | Vendor-specific claim (promotional - do NOT adopt as fact) |
|---|---|
| One channel/agent per lane; pinned context message per lane | "Viktor is an AI employee that joins Slack/Teams" |
| Managed connectors to existing software | "thousands of tools through managed connectors" (Viktor) |
| Scheduled jobs from a plain-language brief | "$100 in free credits at viktor.com", "starts free" |
| Approval gates, spend caps, reviewer separation, bounded memory | Any implication a specific vendor is required or recommended |

The practices are tool-agnostic. Implement them on whatever stack PRTL already
uses; a vendor is neither required nor endorsed here.

## PRTL lane design

PRTL is a solo, personal Expo/RN + Express digital art-frame product. Same
pattern as the source (context first, named deliverables, a cadence, a gate on
money/outside-world) adapted to a solo app maker. Every lane below is
**least-privilege**: it may run only its listed scope unattended; every gated
action waits for Trevor. Budget caps are per-lane monthly ceilings under a single
hard account cap; set the real numbers before the first brief (placeholders here).

### Lane 1 - Content / marketing
- **Inputs:** brain notes (offer, voice, client); what performed on X/app stores in the last 14 days for the art-frame niche.
- **Deliverables:** 5 drafted posts + 1 thread on the week's topic; ASO/store-listing copy drafts; strongest draft flagged with a reason. Status = `draft` only.
- **Cadence:** weekly research + draft batch.
- **Permissions (least privilege):** research, draft. No publish, no send.
- **Escalation:** anything off-voice or making a product claim -> Trevor.
- **Budget cap:** e.g. $X/mo.
- **Readiness gate (measurable):** the week the drafts ship with zero rewrites for two consecutive weeks.
- **PRTL skills to lean on:** `content-strategy`, `copywriting`, `social`, `app-store-optimization`/`aso`, `ai-writing-detection` + `no-ai-slop` + `de-slop` on every draft.

### Lane 2 - Projects / build
- **Inputs:** repo state, roadmap, this lane's context note.
- **Deliverables:** weekly plan (each workstream, stage, what ships, biggest blocker); a daily standup under 8 lines (moved / due / blocked). Read-and-track only.
- **Cadence:** weekly plan + workday-08:00 standup.
- **Permissions:** read, plan, standup, track. No code push, no deploy.
- **Escalation:** a blocker unmoved 2 days, or any change to mode-build code / `_/docs` -> Trevor.
- **Budget cap:** e.g. $X/mo.
- **Readiness gate:** standups post correctly for a full week with no manual correction. (This lane passes first, by design.)
- **PRTL skills:** `react-native-dev`, `react-native-best-practices`, `react-native-architecture`, `react-doctor`, `systematic-debugging`; lean output governed by `.agents/rules/lean-token-and-yagni.md` (caveman/ponytail).

### Lane 3 - Outreach / growth
- **Inputs:** client/ICP note; a list target ("N real fits for the art-frame buyer").
- **Deliverables:** research on N real prospects (what they do, the visible need, a confidence note) + a first-touch draft for the top few. **Drafts only - nothing ever sends.**
- **Cadence:** weekly.
- **Permissions:** research, draft. **No send. No external outreach.** (The lane deliberately holds no send-capable tool.)
- **Escalation:** every send is Trevor's decision; a low-confidence prospect -> flag, don't draft.
- **Budget cap:** e.g. $X/mo.
- **Readiness gate:** the confidence column stays honest without Trevor re-checking the sources.
- **PRTL skills:** `cold-email`, `prospecting`, `community-marketing`, `customer-research` (availability varies by tree); `ai-writing-detection` on drafts.

### Lane 4 - Finance
- **Inputs:** billing/subscription state, milestone list.
- **Deliverables:** draft invoice for [client, milestone, amount] posted for review, never finalized; a weekly summary (issued / paid / overdue with days outstanding, MTD) under 10 lines.
- **Cadence:** on-demand drafts + Friday-16:00 summary.
- **Permissions:** invoice_draft, report. **No invoice finalize. No purchase.**
- **Escalation:** any finalize, refund, or spend -> Trevor.
- **Budget cap:** e.g. $X/mo.
- **Readiness gate:** summaries reconcile to source for two cycles with no correction.
- **PRTL skills:** `monetization-strategy`, `pricing`, `paywalls`.

### Lane 5 - Ads / user acquisition
- **Inputs:** the offer (restate in two lines to prove understanding), daily cap.
- **Deliverables:** a proposed test media plan (2 audiences, 2 angles each written for AI-skeptical readers, a proposed split of the daily cap); after plan approval, a campaign **built with everything PAUSED**.
- **Cadence:** on-demand, plan -> approval -> build-paused.
- **Permissions:** plan, build_paused. **No ad activation.** Nothing goes live without an explicit go.
- **Escalation:** plan approval and go-live are both Trevor's calls.
- **Budget cap:** e.g. $X/mo hard cap, quote-before-execute in the context note.
- **Readiness gate:** a paused campaign is built to spec (targeting, angles, budget split) with no rework, twice.
- **PRTL skills:** `ads`, `ad-creative`, `creative-strategy`, `app-store-optimization` (availability varies by tree).

## Memory guidance for PRTL

- **Lowest useful tier.** Start and stay at **L1 files** (markdown in the brain).
  PRTL ships no memory product or graph skill; do not reach for L2/L3 unless the
  material provably outgrows what fits in context.
- **Bounded.** Cap each lane's memory note at a few hundred lines; load
  everything else on demand. Memory that grows without a ceiling crowds out work.
- **Review dates.** Every memory entry carries a `review:<date>`; sweep on the
  review date and delete what did not earn its place.
- **Superseded-fact traceability.** When a fact changes, write the new version and
  keep the old one marked `superseded-by:<new>` / `superseded:<date>` so a bad
  belief can be traced to its source. Never silently overwrite.
- **Identity stays out of memory.** Each agent's identity file is durable; memory
  is the only place churn lives.

## Safeguards (non-negotiable)

Keep **sends, publishing, purchases, ad activation, invoice finalization, and
external outreach BEHIND explicit human approval** - every lane, always,
regardless of how routine it feels. Least privilege per lane: an outreach agent
holds no send tool; a finance agent cannot finalize; an ads agent cannot
activate. Routine internal work (research, drafting, planning, standups,
reporting) runs unattended; anything that touches money or the outside world
waits for Trevor's yes. Set a hard monthly spend cap and quote-before-execute
before the first brief. Sponsored/vendor claims are promotional - never adopt a
vendor claim as fact or a recommendation.

## Independent review / eval

Reviewer is a different agent than the author. Ship nothing money/outside-facing
without an independent pass that checks **both** the output *and* the permission
boundary. One runnable check enforces the boundary invariants:

- File: [`./check-permissions.mjs`](./check-permissions.mjs)
- Run: `node check-permissions.mjs` (exit 0 = pass; it throws on any breach).
- It asserts: (1) every gated verb (send/publish/purchase/ad_activate/
  invoice_finalize/external_outreach) requires human approval from *every* lane;
  (2) no lane can act outside its least-privilege scope; (3) a deliverable
  already marked sent/live/finalized fails the output gate. If someone widens a
  lane's grant or lets a gated action auto-run, the check fails.

Pair it with a human read of the actual deliverable against the brief's
definition of "done" before any approval.

## PRTL capability map (what actually exists - do not invent)

The source names "company-brain", "loopify", "skillify", "orchestration",
"memory", "permissions", and "checkpointing" as building blocks. **None of these
exist as skills or rules in PRTL's `.claude` / `.agents` / `.cursor` trees**
(verified 2026-07-30). So this skill defines the brain, bounded-memory, approval-
gate, spend-cap, and checkpoint discipline inline rather than delegating to
skills that are not present. What PRTL *does* have and this skill leans on:

- **Lean runtime rule:** `.agents/rules/lean-token-and-yagni.md` (caveman +
  ponytail) - the closest existing governance anchor; keeps briefs and memory terse.
- **Writing quality:** `ai-writing-detection`, `no-ai-slop`, `de-slop`/`deslop` (all three trees).
- **Marketing / outreach family:** `content-strategy`, `copywriting`,
  `social`, `cold-email`, `prospecting`, `community-marketing`,
  `ads`, `ad-creative`, `monetization-strategy`, `pricing`,
  `paywalls`, `app-store-optimization`/`aso` (some vary by tree).
- **Build family:** `react-native-dev`, `react-native-best-practices`,
  `react-native-architecture`, `react-doctor`, `systematic-debugging`.

If a real company-brain / memory / orchestration skill is later added to PRTL,
update the lane mappings above to point at it.
