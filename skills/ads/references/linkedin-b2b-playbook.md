# LinkedIn B2B Playbook

Operational rules for LinkedIn Ads: bidding, audience sizing, scaling triggers, benchmarks, and format-specific tactics. LinkedIn is the precision channel â€” highest-quality B2B targeting at the highest cost, so the operating discipline is about not wasting that precision.

## Contents

- Bidding progression
- Audience sizing rules
- Job functions vs. job titles
- Audience splitting rules
- Penetration-based scaling
- Benchmarks by funnel stage
- Thought leader ads (TLAs)
- Campaign group build order
- Format notes (document, conversation, CTV)
- Retargeting setup (non-retroactive!)
- Account audit shortlist

## Bidding progression

1. **Week 1:** launch on automated bidding / maximum delivery. Don't touch it â€” you're buying CPC data.
2. **Week 2+:** switch to manual CPC set **~20% below the average CPC** the automated phase produced. This reliably cuts CPC without killing delivery.
3. **Exceptions:** small retargeting/ABM audiences stay on automated (manual underdelivers on small pools); reset to automated for a week whenever you change objective; audiences under ~10K may never spend their full budget at any bid.

Scheduling note: LinkedIn's ad day resets at UTC midnight. Professional activity peaks weekday morningsâ€“early afternoon in the audience's timezone; dayparting there stretches limited budgets.

## Audience sizing rules

- **Cold prospecting:** 50Kâ€“300K members. Minimum ~15K per cold campaign.
- **Too-narrow failure mode:** hyper-narrow audiences spike CPMs several-fold and stall delivery entirely â€” budget won't spend at any bid. If it's not spending, the audience is usually too small, not the bid too low.
- **Tiny TAM (<~30K addressable):** skip the TOF/BOF split â€” run one campaign that saturates the whole audience with all funnel layers.
- **Retargeting:** audiences of roughly 1Kâ€“5K per segment (site visitors, 50%+ video viewers) are workable; below ~300 won't deliver.

## Job functions vs. job titles

Title targeting is precise but small and expensive. **Job function + seniority** targeting typically triples the addressable audience with materially cheaper reach at similar engagement â€” at the cost of a weekly "negative title" exclusion pass for the first ~2 months (like negative keywords: exclude irrelevant titles as they show up in demographics).

Platform gotchas:
- **Job-title targeting and seniority targeting are mutually exclusive** â€” you can't stack them. Entry-level exclusions only work under function/seniority targeting.
- The **Business Development function includes many CEOs, CMOs, and managing directors.** Don't blanket-exclude BD if you sell to the C-suite â€” filter with seniority exclusions instead.
- Leave **Audience Expansion OFF** (it quietly spends a meaningful share of budget on out-of-ICP members) and **Audience Network OFF** for B2B lead gen.

## Audience splitting rules

Split priority: **intent > persona > region/company size > seniority.**

- **Region:** keep the US separate (most expensive market â€” grouped with cheaper regions, it eats the budget). DACH needs localized ads; UK/Canada/Australia group fine; Nordics/Netherlands run fine in English. Never group an expensive market with small ones.
- **Company size:** segment by employee count (not revenue â€” LinkedIn's revenue data is estimated). Start with two bands, not three. Left unsegmented, LinkedIn over-serves the extremes (small companies and very large ones) and underserves mid-market â€” splitting forces fair distribution.

## Penetration-based scaling

Audience penetration (reached Ã· audience size) is the scaling trigger, not spend:

- 30-day penetration **<25%** â†’ room to raise budget on this audience.
- **25â€“35%** â†’ hold; let penetration accumulate before adding spend.
- **~35%+** = healthy saturation â†’ scale horizontally (new audiences), not vertically.
- Expect diminishing returns: doubling budget grows penetration ~50â€“70%, not 100%.
- One campaign at 35%+ penetration beats three campaigns at 12% each â€” consolidate before multiplying.
- **Spend rising but reach flat (frequency climbing)?** Either competitors outbid you or ad quality is dragging your auction price. Strong ads â†’ raise budget/bids; weak ads â†’ fix creative first, more money just buys the same people again.

## Benchmarks by funnel stage

Practitioner-reported B2B SaaS ranges â€” recalibrate on your own account. **Careful:** for engagement-objective and thought-leader campaigns, LinkedIn's reported "CTR" includes social actions; judge traffic on **click-through to landing page (CTRTLP)** specifically.

| Metric | Cold / TOF | MOF | BOF/retargeting |
|---|---|---|---|
| CTRTLP | 0.30â€“0.55% | 0.55â€“0.80% | 0.80â€“1.30% |
| CPM | $33â€“65 typical | â€” | â€” |
| CPC | $8â€“22+ | â€” | lower |
| Cost per lead (Lead Gen Form) | â€” | $50â€“200 | â€” |
| Cost per website form fill | â€” | â€” | $200â€“500 |

Other useful bars: lead-gen form fill rate >8% (below = form too long, offer weak, or audience too cold); cost per SQL should stay under ~$500 (enterprise ACVs tolerate $300â€“500+ CPLs; SMB needs $50â€“150); video view rate >40%, completion 8â€“15% for horizontal; expect return data to lag 3â€“6 months.

## Thought leader ads (TLAs)

Ads promoted from a person's profile rather than the company page â€” currently the platform's biggest efficiency arbitrage:

- TLAs typically deliver **~3â€“6Ã— the CTR of company-page ads** at a fraction of the CPC.
- **Non-employee/creator TLAs often outperform employee TLAs** â€” partnerships with niche creators are worth 30â€“50% of TLA budget if available.
- **Organic-first pipeline:** posts that hit ~2â€“3% organic CTR are your TLA candidates â€” the audience already voted.
- **The 72-hour edit:** organic reach concentrates in a post's first ~3 days. Let it run organic, then edit the post to add the CTA/product mention and promote it as a TLA â€” you capture organic credibility first, then convert it to demand gen.
- Auction insight: single-image ads face the most auction competition. Document, conversation, and TLA formats often buy cheaper reach purely because fewer advertisers use them â€” format diversification is a *bidding* tactic, not just creative variety.

## Campaign group build order

Add groups in ROI order, funding each before the next: **1. Product value** (direct response on your core offer) â†’ **2. Remarketing** â†’ **3. Content** (only content that can't be consumed in-feed â€” it must earn the click) â†’ **4. Social proof** (case studies, testimonials) â†’ **5. Thought leadership** (slowest payback, add last). Group-budget optimization tends to favor cheap audiences and video â€” don't mix enterprise with SMB or static with video in one group.

## Format notes

- **Document ads:** always 1080Ã—1350 portrait (4:5). 5â€“7 slides: hook â†’ pain â†’ shift â†’ solution â†’ differentiators â†’ CTA. The classic mistake is making the "solution" slide generic category requirements and the "differentiator" slide a rehash â€” slide N must add what slide N-1 couldn't. Big standalone stat slides (one number, source small) carry these.
- **Conversation ads:** subject 2â€“4 words; 3â€“5 short lines per message; specific numbers beat vague benefit claims; lead with a soft CTA ("see how it works") over "book a demo"; route the primary CTA to a Lead Gen Form, not a scheduling link. Benchmarks: 35â€“50%+ open rate, 2â€“5% CTR.
- **CTV:** Brand Awareness objective only, auto-bid only, ~$50/day minimum, limited geos. Completion metrics are meaningless (forced view). Only worth it above roughly $15K/month total spend â€” below that it cannibalizes measurable-signal budget.

## Retargeting setup (non-retroactive!)

**LinkedIn retargeting audiences only start collecting from the moment you create them.** Create every retargeting audience you might ever want (site visitors, video viewers, ad engagers, lead-form openers, company page visitors) **before launch** â€” data you didn't capture is gone permanently.

Cross-channel: tag paid-search traffic with UTMs and build LinkedIn (and Meta) retargeting audiences from it â€” see the [ABM playbook](abm-playbook.md) for the mechanic.

## Account audit shortlist

The highest-frequency findings when auditing LinkedIn accounts, in order: Audience Expansion left on Â· Audience Network left on Â· audiences too small to deliver Â· fewer than 4 active ads per campaign Â· campaigns under ~10 results/week (starved â€” consolidate) Â· stale creative (3+ months old) Â· no retargeting audiences created Â· lead quality never reconciled against CRM Â· brand/geo budget mixing Â· everything on automated bidding forever.

---

*Framework lineage: adapted (re-expressed and restructured) from practitioner playbooks, notably Ivan Falco's ads-skills. Benchmarks are practitioner-reported starting points â€” recalibrate against your own account.*
