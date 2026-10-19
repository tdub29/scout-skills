# Ogilvy: Positioning And Image

## When to Use

Use this when a product or campaign needs a sharper advertising position and a more consistent brand personality.

Trigger when the user asks how to position a product in an ad, whether a campaign fits the brand image, how to choose between rational facts and personality, how to make a parity product distinctive, or whether new creative will strengthen or weaken long-term brand equity.

Do not trigger for a full market, ICP, category, or brand-platform project; route that to `brand-positioning`. Do not trigger for final copy or ad variants; route execution to `copywriting` or `ad-creative`. Do not trigger for headline selection, claim proof, or formal test pilots; route those to `hopkins-headline-audit`, `hopkins-scientific-claim-check`, or `hopkins-test-campaign`.

## Framework

Ogilvy separates two decisions that many campaigns blur.

1. Positioning: "what the product does, and who it is for." Dove could have been positioned as a detergent bar for dirty hands; Ogilvy positioned it as a toilet bar for women with dry skin.
2. Image: the brand's personality. It is built from name, packaging, price, advertising style, and the product itself.
3. Consistency: every advertisement contributes to brand image, so the image should be projected consistently year after year.
4. Quality signal: for products people are seen using, cheap-looking advertising rubs off on the product.
5. Image economics: in categories like whiskey, cigarettes, beer, cars, and other social products, people often buy the image as much as the product facts.

## How to Apply

1. Define the current implicit position in one sentence: what the product does and who it appears to be for.
2. Generate alternative positions by changing use case, buyer, occasion, contrast, or enemy.
3. Score each position for buyer relevance, product truth, competitive distinctiveness, and long-term campaign potential.
4. Define the desired image in three to five plain adjectives, then tie each adjective to product, packaging, price, proof, or execution style.
5. Audit the proposed ad against the image: does it look, sound, and behave like the brand you intend to build?
6. Decide whether rational facts or image should carry the burden. Use facts when they are distinctive and believed; use image when category choice is social, emotional, or parity-driven.

## Output Format

Return a positioning and image brief:

- Current position: what the product currently does and who it appears to serve.
- Recommended position: one sentence with rationale.
- Rejected alternatives: why they lose.
- Desired brand image: personality traits and concrete execution signals.
- Consistency check: what the ad must keep repeating over years.
- Risk flags: cheapness, image drift, wrong audience, unsupported personality, or generic parity.

## Common Failure Modes

- Calling a tagline a position when it does not define product role and audience.
- Choosing an image the product, price, packaging, or service cannot support.
- Changing the campaign every time a new manager wants to make a mark.
- Mistaking a rational proof point for a brand personality in image-led categories.
- Treating this as a full positioning platform; use `brand-positioning` for market architecture, ICP, category strategy, and value proposition systems.
- Moving from strategy to copy too early; route execution to `copywriting` or `ad-creative`.

## References

- David Ogilvy, *Ogilvy on Advertising* (1983), Chapter 2, "Positioning" and "Brand image".
- Sibling skills: `ogilvy-advertising-homework`, `ogilvy-big-idea-gate`, `ogilvy-direct-response-lens`, `ogilvy-print-ad-audit`, `ogilvy-tv-commercial-formats`, `ogilvy-b2b-advertising`.
- Overlap routes: `brand-positioning`, `copywriting`, `ad-creative`, `hopkins-headline-audit`, `hopkins-scientific-claim-check`, `hopkins-test-campaign`.
