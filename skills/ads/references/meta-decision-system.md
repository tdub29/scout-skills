# Meta Decision System (B2B)

A quantified kill/keep/scale engine for Meta ads. Every threshold derives from one anchor number, so decisions become arithmetic instead of vibes. Pairs with the strategy-level Meta playbook in SKILL.md (creative-as-targeting, creative volume) â€” this file is the *operating* layer.

## Contents

- TCPL: the anchor variable
- The ad-count ceiling
- Two-campaign structure (Scaling / Testing)
- Destination testing (CBO per persona, one ad set per destination)
- Stage 1: delivery check (day 7)
- Stage 2: quality evaluation (weekly)
- Graduation criteria
- Fatigue detection
- Swap rules
- Creative production math
- Scaling protocol
- Weekly cadence
- Lead forms and social amnesia
- Advantage+ transition
- Benchmarks and seasonality

## TCPL: the anchor variable

TCPL = **Target Cost Per Qualified Lead** (qualified = meets your ICP bar, not just a form-fill). Set it one of three ways:

1. **From deal math (best):** TCPL = target cost per demo Ã— qualified-lead-to-demo rate. ($2,000/demo Ã— 0.28 = $560.)
2. **From history:** TCPL = trailing 30-day CPL(qualified) Ã— 0.80 â€” a 20% improvement is achievable through operational cleanup alone (killing zero-QL ads, graduating winners). Once you have both, use whichever is tighter.
3. **New account:** target CAC Ã— qualified-lead-to-customer rate, or a placeholder from your ACV tier; replace with method 2 after 30 days.

Every rule below is expressed in multiples of TCPL. Review TCPL monthly.

## The ad-count ceiling

More active ads than your budget can feed = every ad starves and nothing gets a fair read.

**Ceiling = (daily budget Ã— 14) / (2 Ã— TCPL)** â€” i.e., over a 14-day evaluation window, each ad needs at least 2Ã— TCPL of spend to be judged.

$1,000/day at $500 TCPL â†’ ceiling of 14 ads; run **6â€“10** (winners + 2â€“3 test slots). At the ceiling, launching a new test requires killing something first.

## Two-campaign structure (Scaling / Testing)

Run two CBO campaigns over the **same audience**:

- **Scaling campaign (~80% of budget)** â€” holds only graduated, proven ads.
- **Testing campaign (~20%)** â€” holds new concepts and iterations, with its own protected budget.

Why: inside a single CBO, proven ads always starve new ads â€” tests never get enough spend to be judged. Why not ABO for testing: equal forced distribution keeps spending on ads Meta has already deprioritized. The separation is *budget protection*, not audience segmentation.

**Image-first validation:** launch new concepts as statics first; only produce the video/carousel/UGC version after the image passes the checks below. Exception: concepts that are inherently video (testimonial, demo, UGC).

## Destination testing (CBO per persona, one ad set per destination)

A complementary structure for when the **lander, not the creative, is the biggest unknown**: one CBO per persona; inside it, one ad set per destination type â€” PDP, listicle/advertorial, quiz, demo page â€” with the **same creatives in every ad set**. Holding creative constant makes the read clean: any CPM or performance divergence between ad sets is the destination.

Why it works: the destination is a test axis of the same rank as creative â€” a losing funnel can hide winning creative, and different personas convert through different funnel shapes. CBO allocates budget across destinations the way it allocates across ads, and practitioners running this report wide CPM/performance spreads between destinations plus meaningful new-reach gains (~30%) from the added variety.

Fit with the two-campaign structure: treat a destination test like a concept test â€” run it in the Testing campaign with a protected budget, judge each ad set against TCPL at the usual spend gates, then graduate the winning creative Ã— destination pair. *Practitioner-reported pattern (Alexander Pauwelyn, 2026), not a platform-documented mechanic â€” validate against your own account data.*

## Stage 1: delivery check (day 7)

CBO's spend allocation is itself a signal â€” Meta pre-screens your ads. At day 7 for each test ad:

- **Fair share test:** minimum expected spend = (campaign daily budget Ã· active ads) Ã— 7 Ã— 0.5. Below that â†’ **kill** (Meta actively deprioritized it). Zero spend â†’ kill immediately.
- **Ongoing:** if an ad has spent â‰¥ 1Ã— TCPL lifetime AND averaged under ~$10/day over the last 7 days â†’ kill. (The lifetime-spend gate stops you from killing ads CBO simply hasn't explored yet.)

When iterating on a delivery-killed ad, change the **hook/visual/format only** â€” the audience never got far enough for copy or CTA to matter.

## Stage 2: quality evaluation (weekly, rolling 14-day data)

Run in order; stop at the first triggered action:

1. **Data gate:** spend < 3Ã— TCPL â†’ **wait** (not enough signal). At true cost-per-QL = target, 3Ã— TCPL of spend should produce ~3 qualified leads; zero QLs at that spend is ~5% probability â€” so judging at 3Ã— gives ~95% confidence without wasting budget (2Ã— has a 13% false-negative rate; 5Ã— overpays for certainty).
2. **Zero pixel leads** at â‰¥3Ã— TCPL â†’ **swap and abandon the concept** (don't iterate a dead concept).
3. **Quality check** (the layer Meta can't see â€” requires your CRM):
   - Pixel leads but zero qualified â†’ swap; keep the format, change the angle.
   - Qualified rate <40% â†’ swap; the ad attracts the wrong people. Add ICP-filtering language. (At 40% QL rate, true cost per QL is 2.5Ã— the pixel CPL you see in Ads Manager â€” two ads identical in-platform can differ 60%+ in real cost.)
   - 40â€“60% â†’ monitor one more week. â‰¥60% â†’ proceed.
4. **Cost check:** cost per QL â‰¤ TCPL â†’ candidate winner. 1â€“1.5Ã— TCPL â†’ monitor (normal variance). >1.5Ã— TCPL â†’ swap (structural underperformance, not noise).

## Graduation criteria (Testing â†’ Scaling)

Graduate only when **all** are true: â‰¥5 qualified leads Â· qualified rate â‰¥60% Â· cost per QL â‰¤ TCPL Â· running â‰¥14 days Â· â‰¥1 QL in the last 7 days.

## Fatigue detection

Frequency bands by campaign type (safe / warning / critical):

| Campaign type | Safe | Warning | Critical |
|---|---|---|---|
| Cold prospecting | 1.0â€“2.5 | 2.5â€“4.0 | >4.0 |
| Retargeting | 2.0â€“4.0 | 4.0â€“6.0 | >6.0 |
| ABM (small audiences) | 2.0â€“5.0 | 5.0â€“8.0 | >8.0 |

Other signals, in urgency order: CTR down 20%+ from baseline over 7 days; CPM up 30%+ over 2 weeks (leading indicator â€” moves before CTR); ad relevance rankings "below average"; CPA up with stable targeting.

For **scaling-campaign ads**, apply a deliberately stricter bar than the general bands â€” these ads carry ~80% of spend, so fatigue there costs the most: warning at frequency 3.0â€“3.5 or cost +20% â†’ start 2 iterations now (they take ~14 days to be ready); swap at >3.5, cost +40%, or >1.5Ã— TCPL for 2 weeks.

**Lifespan expectations (B2B):** statics 14â€“28 days; short video and carousels 21â€“35; UGC/testimonial 28â€“42. Small B2B audiences build frequency fast â€” plan refresh every 14â€“21 days.

**Retire (don't iterate)** when CTR drops 30%+ from peak or frequency crosses the campaign type's critical band above â€” the concept is exhausted, not the execution.

**Rotation without resetting learning:** never edit creative inside a performing ad â€” that resets the learning phase. Launch new ads alongside existing ones, or spin up a new ad set with the same targeting. Pausing doesn't reset; editing does.

## Swap rules

**Never pause without a replacement.** Keep 2â€“3 iterations staged; replacement live within 7 days, immediately for critical fatigue. If the pipeline is empty, redirect the budget to proven ads rather than leaving a zombie running. What to change depends on why it died: delivery kill â†’ hook/visual; quality kill â†’ angle and ICP language; cost kill â†’ offer and audience; fatigue â†’ fresh execution of the same proven concept.

## Creative production math

- **Test throughput** â‰ˆ (monthly budget Ã— 0.20) Ã· (3 Ã— TCPL), per month. Delivery kills free budget early, so actual throughput runs ~1.5â€“2Ã— the base rate.
- **Win rates:** iterations on winners ~25%; brand-new concepts ~10%; blended ~1 in 6. To get N winners, plan ~6Ã— N tests.
- **Minimum proven-ad inventory** â‰ˆ monthly budget Ã· $5,000 â€” each proven B2B ad absorbs roughly $5K/month before fatiguing. **You cannot scale budget ahead of creative supply**; if proven ads < minimum, fix the creative deficit before raising budget.
- **Iteration priority** when refreshing a winner (ranked by impact): 1. hook (changes who stops) â†’ 2. visual treatment â†’ 3. format â†’ 4. body copy/CTA.

## Scaling protocol

Scale only when all: proven-ad count meets the next budget level's minimum; account frequency <3.0; cost per QL â‰¤ TCPL for 2+ consecutive weeks; 3+ replacements staged.

- **Rate:** +20% every 5 days. Never +30% or more in one move â€” that resets learning.
- **Rollback trigger:** cost per QL >1.5Ã— TCPL after a scale step â†’ cut budget 20â€“30% immediately, stabilize 2 weeks, resume at +10% per week.
- **Hitting the wall** (account-wide average frequency >3.5 â€” an account-level *scale* guardrail, distinct from the per-ad fatigue bands above): expand lookalikes 1% â†’ 2â€“3%, add new seed audiences, test broad, activate cross-channel UTM audiences (see [ABM playbook](abm-playbook.md)), re-open remarketing.

## Weekly cadence

- **Monday â€” decision day:** pull rolling 14-day data; run Stage 2 on every test ad; run the fatigue check on every scaling ad.
- **Wednesday â€” launch day:** launch new tests into freed slots; run Stage 1 on ads that hit day 7.
- **Friday â€” scaling day:** apply scale steps or rollbacks.
- **Monthly:** creative library audit + TCPL review.

## Lead forms and social amnesia

The #1 B2B Meta lead-quality problem: frictionless auto-filled forms produce leads who don't remember converting ("social amnesia"). **Intentional friction = awareness = quality:**

- Use **Higher Intent** form type (adds a review step), not More Volume.
- **Require work email** â€” it can't auto-fill from the Facebook profile, forcing a conscious act. This is the single biggest quality lever.
- Add 1â€“3 multiple-choice qualification questions (4+ spikes abandonment), ordered easiest â†’ hardest.
- Confirmation message sets expectations for what happens next (combats amnesia at the follow-up stage).

Lead form vs. landing page: LP converting â‰¥5% â†’ use the LP; LP under ~2% â†’ lead form; demo/trial offers â†’ LP; content/webinar â†’ form.

## Advantage+ transition

Manual is where you learn; Advantage+ is where you earn. Transition a campaign to Advantage+ only after: a proven offer, a validated audience, and **~50 conversions/week** on the optimization event (the learning-phase exit bar â€” budget needed â‰ˆ target CPA Ã— 50 Ã· 7 per day). If you can't hit 50/week on the target event, optimize a higher-volume event up-funnel and retarget converters. Advantage+ conflicts with strict ABM (you can't lock it to a list) â€” see the [ABM playbook](abm-playbook.md). Watch Campaign Score directionally (70+ healthy, <50 = fighting the algorithm) but never trade lead quality for score.

## Benchmarks and seasonality

B2B SaaS Meta ranges (practitioner-reported; recalibrate on your own first 30 days): CTR 1.0â€“1.5% (red flag <0.8%); CPM $10â€“20 (red flag >$25); CPL (form) $20â€“50 (red flag >$75); landing page CVR 8â€“12%. Seasonality: Q1 CPMs are the year's lowest (scale aggressively); Q4 runs +60â€“80% (consider reducing B2B spend and banking budget for January).

---

*Framework lineage: this decision system is adapted (re-expressed, reconciled, and restructured) from practitioner operating systems, notably Ivan Falco's ads-skills. All thresholds are starting points â€” recalibrate against your own account.*
