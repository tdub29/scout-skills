# Ogilvy: Print Ad Audit

## When to Use

Use this when reviewing or planning a print advertisement, magazine ad, newspaper ad, poster, subway card, or print-style landing creative where layout, copy, image, and readability determine selling power.

Trigger when the user asks to audit a print ad, improve an ad layout, check headline/image/body copy fit, make long copy readable, choose editorial vs ad-like design, or diagnose why a print ad is beautiful but not selling.

Do not trigger for selective headline strategy alone; route to `hopkins-headline-audit`. Do not trigger for specific claim proof alone; route to `hopkins-scientific-claim-check`. Do not trigger for writing the finished ad; route execution to `copywriting` or `ad-creative`. Do not trigger for broad brand platform work; route to `brand-positioning`.

## Framework

Ogilvy's print discipline is a readership-and-sales checklist.

1. Headlines: five times as many people read headlines as body copy. Promise a benefit, announce news, offer helpful information, include the brand, flag narrow buyers, avoid blind or tricky headlines, and use specifics.
2. Illustrations: make the subject work. Favor curiosity and story appeal, product/package focus when no story exists, end-result and before/after images, photographs over drawings when reproduction allows, simple focus, and finished dishes for food.
3. Body copy: write to one person, in everyday language, with short sentences, specifics, story form, testimonials, price when possible, and enough facts to sell. Long copy can sell when well written.
4. Layout: readers scan illustration, headline, copy. Put elements in that order, use captions under every image, make captions mini-ads, and prefer editorial graphics over ad-like clutter.
5. Typography: black on white, serif faces, readable columns, lower case, no headline periods, drop initials, cross-heads, bold or italic key paragraphs, and no reverse type except rare use cases.

## How to Apply

1. Identify the ad's job: awareness, inquiry, sale, coupon, store visit, donation, or brand image.
2. Audit the headline for promise, news, information, brand, buyer flag, specificity, and clarity.
3. Audit the image for story appeal, relevance, product role, simplicity, end-result proof, and likely misinterpretation.
4. Audit the copy for one-to-one voice, facts, specifics, credibility, story, testimonials, price, and length fit.
5. Audit layout order, captions, editorial feel, spread usage, and response devices.
6. Audit typography for readability at real reading distance.
7. Return prioritized fixes, not a full rewrite unless the user explicitly asks for execution through another skill.

## Output Format

Return a print ad audit:

- Selling job: what the ad must cause the reader to do or believe.
- Headline score: benefit, news, information, brand, buyer flag, specificity, clarity.
- Image score: story appeal, product relevance, simplicity, end-result, misread risk.
- Copy score: facts, specificity, credibility, one-to-one tone, length, opening paragraph.
- Layout and typography score: scan order, captions, editorial style, legibility, reverse type, columns.
- Highest-leverage fixes: ordered list of changes.
- Routing note: headline-only, claim-proof, or execution tasks routed to the appropriate sibling or overlap skill.

## Common Failure Modes

- Treating the ad as a poster when readers will encounter it at reading distance.
- Making the layout impressive to art directors instead of readable to buyers.
- Running a headless wonder or a blind headline.
- Using a beautiful image with no story appeal or selling role.
- Omitting captions even though captions are heavily read.
- Setting copy in reverse, all caps, sans serif sheets, strange shapes, or unreadable widths.
- Letting this audit become final copywriting; route execution to `copywriting` or `ad-creative`.

## References

- David Ogilvy, *Ogilvy on Advertising* (1983), Chapter 7, "Wanted: a renaissance in print advertising".
- Sibling skills: `ogilvy-advertising-homework`, `ogilvy-positioning-image`, `ogilvy-big-idea-gate`, `ogilvy-direct-response-lens`, `ogilvy-tv-commercial-formats`, `ogilvy-b2b-advertising`.
- Overlap routes: `copywriting`, `ad-creative`, `brand-positioning`, `hopkins-headline-audit`, `hopkins-scientific-claim-check`, `hopkins-test-campaign`.
