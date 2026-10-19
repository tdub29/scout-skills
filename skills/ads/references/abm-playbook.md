# ABM Playbook (Paid)

Account-based marketing with ads: targeting named accounts on LinkedIn and Meta, accelerating open pipeline, and stitching channels together. ABM ads are a *pipeline influence* motion, not a lead-gen motion â€” measure accordingly.

## Contents

- When ABM (go/no-go)
- LinkedIn ABM
- ABM on Meta
- Acceleration campaigns (ads against open pipeline)
- Cross-channel orchestration
- Cross-channel UTM remarketing
- Sales orchestration
- Measuring ABM

## When ABM (go/no-go)

Run paid ABM when: target account list â‰¥ ~1,000 companies (or you accept 1:1/1:few economics), deal size ~$25K+, sales cycle 60+ days, sales and marketing actually aligned on the list, and (for Meta) contact enrichment available.

Skip it when: TAL under ~500 with no enrichment, no first-party data, budget under ~$3K/month, or a short transactional cycle â€” standard ICP targeting will outperform.

## LinkedIn ABM

Three motions, by list size:

- **1:1** â€” add the company by name; fully personalized creative for one account.
- **1:few** â€” up to ~10â€“20 accounts per campaign, shared pain/industry angle.
- **1:many** â€” uploaded list (or native targeting), scaled creative.

**List mechanics:**
- LinkedIn needs **300 matched members minimum** to serve; aim for 1,000+ rows (duplicating company names to pad the upload is fine â€” it dedupes on match). Contact lists match best at scale (LinkedIn suggests ~10K emails); **company lists beat contact lists** for most teams â€” easier to source, better match rates, less maintenance.
- Cold ABM audiences need ~15K members to deliver reliably.
- **Segment mixed lists.** Left as one audience, LinkedIn over-serves the largest enterprises in the list â€” accounts have sat at 15% list coverage because the algorithm parked on a few big companies. Split into homogeneous bands (e.g., enterprise / mid-market / SMB) with separate campaigns and budgets.
- List-based targeting typically buys reach materially cheaper than native firmographic targeting, with stronger decision-maker engagement.
- Use the per-company engagement report (Audiences â†’ click into the list) to find under-served priority accounts, then break them into a dedicated campaign.

**Personalized 1:1 creative:** putting the target account's name/logo in the creative can lift CTR ~5â€“10Ã— over generic ads. **Legal exception: do not run company-name/logo-personalized ads into Germany** â€” privacy law, not platform policy.

**Frequency capping:** target ~3 impressions/person/week in priority accounts. Mechanic: build a company-engagement audience of accounts that crossed ~500 impressions in the last 7 days and add it as an *exclusion* â€” it self-rotates accounts out as they cool down. Tune the threshold (300 if fatigue shows, 750 for more pressure).

## ABM on Meta

Meta has no native company targeting â€” the play is **bring your own matched audience**:

- **The match-rate problem:** raw CRM exports of work emails match under ~5% on Meta. Enrichment providers (identity-graph tools that resolve work identities to personal profiles â€” e.g., Primer, Metadata, ZoomInfo, Clearbit) raise matches to ~40â€“85%. Workflow: firmographic criteria â†’ identity-graph match â†’ upload as Custom Audience â†’ target directly or seed a 1% lookalike.
- **Minimum sizes:** account-list audiences ~1,000 companies (5â€“10K optimal); retargeting slices work down to ~100 accounts; lookalike seeds want 500+.
- Advantage+ **conflicts with strict ABM** â€” it won't stay locked to your list. Run ABM campaigns manual (or hybrid: manual for the list, Advantage+ for the broad layer).
- Meta's ABM role is cheap **air cover and multi-threading** (reaching the buying committee beyond your champion) while LinkedIn does precision â€” see the split below.

## Acceleration campaigns (ads against open pipeline)

Ads aimed at accounts already in your pipeline, to speed deals rather than source them:

- Segment the CRM by stage (evaluation / proposal / negotiation), filter to deals worth the spend, upload as an audience, refresh weekly.
- **Use an awareness/reach objective, not conversions** â€” you're keeping the vendor top-of-mind for the buying committee, not asking in-pipeline accounts to "book a demo" they already booked.
- Creative: case studies, proof, objection-handlers â€” matched to stage. Budget scales with deal value (larger open deals justify $100â€“200/day of air cover; stalled deals get a maintenance dose).

## Cross-channel orchestration

Default split for B2B ABM: **~60% LinkedIn / ~30% Meta / ~10% other**. LinkedIn buys precision (right person, right company) at $40â€“70 CPMs; Meta buys presence and committee reach at $10â€“25. Sequence LinkedIn first to validate the audience, then extend to Meta. Multi-channel ABM consistently and materially outperforms single-channel on engagement and conversion â€” the channels compound, they don't compete.

## Cross-channel UTM remarketing

The cheapest high-quality audience you can build: retarget one platform's validated clickers on another platform.

1. Tag all paid traffic with consistent UTMs (`utm_source=linkedin`, `utm_source=google&utm_medium=cpc`).
2. On Meta, build a website Custom Audience with the rule **"URL contains `utm_source=linkedin`"** (or `utm_source=google`).
3. Retarget that audience on Meta â€” LinkedIn-grade audience quality at Meta-grade CPMs (typically 50â€“70% cheaper reach).

Works in both directions (search clickers â†’ LinkedIn remarketing needs meaningful search volume â€” worth it above roughly $30K/month search spend). Requires enough source-channel traffic to clear minimum audience sizes. Use a consistent account/campaign token in UTMs so attribution survives the hop.

## Sales orchestration

ABM ads without sales follow-up is billboard spend:

- Pipe ad-engagement signals to the CRM (LinkedIn company-engagement exports, or connectors that sync engagement per account) and treat an engagement spike as a sales trigger â€” **outreach within ~48 hours** of the spike.
- Route new leads to a shared channel (Slack webhook) with a per-campaign quality reaction (ðŸ‘/ðŸ‘Ž) â€” the cheapest lead-quality feedback loop that exists.
- Hold a monthly sales-marketing session on the list itself: who's engaging, who's dark, who closed â€” and re-cut the list.
- Expect ~7â€“10 cross-channel touches before a sales conversation is normal at ABM deal sizes.

## Measuring ABM

Judge ABM on account movement, not CPL:

- **Account penetration** (% of list reached): target ~40â€“60%.
- **Cost per engaged account** (not per click): ~$100â€“300 is a workable band.
- **Account â†’ opportunity rate:** ~10â€“20%.
- **Pipeline influenced:** aim for 3â€“5Ã— spend; expect win-rate and velocity improvements on engaged vs. non-engaged accounts.
- **Incrementality:** hold out ~20% of the list from ads and compare pipeline formation after 21+ days â€” the only honest answer to "did the ads do anything?"

---

*Framework lineage: adapted (re-expressed and restructured) from practitioner playbooks, notably Ivan Falco's ads-skills. Thresholds are practitioner-reported starting points â€” recalibrate against your own accounts.*
