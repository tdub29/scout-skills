---
name: pre-launch-site-check
description: "Run the 25-item readiness gate on a website before it goes live, then fix what is missing. Use when the user says the site is 'about to launch', 'ready to ship', 'going live', 'before I deploy', 'is my site ready', 'pre-launch checklist', 'what am I missing on the site', 'launch checklist for the website', or hands over a finished-looking site for a final pass. Audits conversion, SEO/crawl, trust, local, accessibility, and analytics items against the actual codebase; implements the mechanical ones; refuses to fabricate trust content (reviews, case studies, team photos, response-time promises) and collects those as one ask. For go-to-market and announcement planning see launch. For diagnosing a live site that already lost rankings see seo-audit. For structured data depth see schema."
metadata:
  version: 0.1.0
---

# Pre-Launch Site Check

A finished-looking site is not a launchable site. This is the last gate before deploy: 25 concrete artifacts that are cheap to add before launch and expensive to retrofit after. Source: a 27-second "20 things to tell Claude to add to your site before launching" clip (Yates | AI Content, TikTok) â€” the list is the seed; the checks, the detection commands, and the fabrication rule are this skill's work.

## Step 0 â€” Classify the site

Five items only apply to a business with a physical location or a service area. Ask once (or infer from the code) and record the answer:

| Site type | Skip |
|---|---|
| Local service business (plumber, clinic, gym, restaurant) | nothing â€” all 20 apply |
| SaaS / product / web app | #14 maps, #17 local schema |
| Portfolio / personal | #6 case studies stays, #8 response promise stays, #14, #17 skip |
| Content / blog | #2, #9, #14, #17 skip; #11â€“13 are the priority |

Also confirm the framework (Next.js, Astro, plain HTML, Rails, â€¦) â€” every "fix" below lands in a framework-specific file, so read one existing page before writing.

## Step 1 â€” Audit before touching anything

Run every check first and produce one table: `#`, item, `PASS` / `MISSING` / `NEEDS-HUMAN`. Do not fix as you go â€” the report is what tells the user how far from launch they are.

| # | Item | How to check | Fix |
|---|---|---|---|
| 1 | Custom 404 page | look for `404.*` / `not-found.*` / server error route | branded page with nav back to home + top 3 links + search if one exists. Must return HTTP 404, not 200. |
| 2 | CTA above the fold | read the homepage template; is a primary action in the first viewport without scroll? | one primary CTA, verb-first, above the fold, repeated at page end |
| 3 | Internal links | count `href="/â€¦"` per page; any orphan page with 0 inbound links? | link every page from at least one other page; add contextual in-body links, not just nav |
| 4 | Thank-you page | is there a distinct URL after form submit, or just an inline "thanks"? | real URL (`/thank-you`) so it can be a conversion goal + retarget trigger; state what happens next |
| 5 | Breadcrumbs | any breadcrumb component/markup on nested pages | breadcrumb trail on every page â‰¥2 levels deep, with `BreadcrumbList` JSON-LD |
| 6 | Case studies | search for case-study / portfolio / results content | **NEEDS-HUMAN.** Scaffold the template + placeholders, never invent the client, numbers, or quote |
| 7 | 5 FAQs | count Q&A blocks | 5 real objections answered in the buyer's words, plus `FAQPage` JSON-LD |
| 8 | Response-time promise | grep for "within", "hours", "respond" near contact form | **NEEDS-HUMAN.** Ask what they can actually honor, then state it next to every form and phone number |
| 9 | Sticky mobile CTA | any fixed/sticky element in a mobile breakpoint | persistent call/book/quote bar on mobile only; keep clear of the iOS home indicator (`env(safe-area-inset-bottom)`) |
| 10 | robots.txt | file exists, and does it still say `Disallow: /`? | real robots.txt + `Sitemap:` line. **Staging blocks are the #1 launch-day bug â€” check this twice.** Also check for a stray `noindex` meta left over from staging |
| 11 | Unique page titles | list every `<title>`; duplicates? | unique, â‰¤60 chars, primary term first, brand last |
| 12 | Meta descriptions | list every description tag; missing or duplicated? | unique, 140â€“160 chars, written as ad copy not a summary |
| 13 | Social share image | `og:image` + `twitter:card` present and absolute URL? | 1200Ã—630 image, absolute URL, per-page where it matters; verify it isn't a broken relative path |
| 14 | Maps + directions | embedded map or directions link on contact page | embed or link to the real listing; the address must match Google Business Profile exactly (NAP consistency) |
| 15 | Real reviews | search for testimonial content | **NEEDS-HUMAN.** Pull from Google/Yelp/email with attribution. Never write a testimonial. `Review` schema only on reviews that genuinely exist |
| 16 | Alt text on images | list every `<img>` / `Image` without `alt` | describe the function, not the filename; decorative images get `alt=""` |
| 17 | Local schema | `LocalBusiness` JSON-LD present? | name, address, phone, hours, geo, URL â€” matching the site and the GBP listing |
| 18 | Privacy policy page | `/privacy` route exists and is linked in the footer | real policy naming what is collected (analytics counts), plus terms if money changes hands. Required by ad platforms and by GA4's own terms |
| 19 | Analytics | tracking snippet present and firing | GA4 (or Plausible/Fathom) on every page + the thank-you page as a conversion event. Verify it fires, not just that the tag is pasted |
| 20 | Real photo of the team | any human faces, or all stock? | **NEEDS-HUMAN.** One real photo beats ten stock ones. Ask for it; leave a marked placeholder, never source a stock face and present it as the team |

### Five more the original 20 left out

Added 2026-09-13 from a second public checklist (@Manixh02, "your vibe coded website looks finished, but it's not"). These five appear on that list and on no line of the 20 above. Same audit treatment: `PASS` / `MISSING`, fixed in the mechanical pass.

| # | Item | How to check | Fix |
|---|---|---|---|
| 21 | Favicon set | `favicon.ico` + `apple-touch-icon` + `<link rel="icon">` in head; open a tab and look | full set (ico, 180Ã—180 apple-touch, 512 PNG for the manifest). A default framework globe is the single loudest "unfinished" tell |
| 22 | Loading states | every fetch/submit path: is there a state between click and result? | skeleton or spinner on any action over ~300ms, and a disabled button on submit so it cannot double-fire |
| 23 | Form error states | submit every form empty and with bad input; what renders? | inline per-field message naming what to fix, tied to the input with `aria-describedby`, plus one summary for screen readers. A form that fails silently reads as a broken site |
| 24 | Compressed images | list image byte sizes; anything over ~200 KB, or a 4000px source in a 600px slot? | WebP/AVIF with a fallback, sized to the slot, `loading="lazy"` below the fold. This is usually the whole LCP problem |
| 25 | Cookie banner | is one needed at all? Only if non-essential cookies (ads, GA4 in EU/UK scope) are set | consent gate BEFORE the tag fires, not a decorative bar over a tag that already fired. A US-only site with cookieless analytics correctly has none â€” mark `N/A`, do not add one for decoration |

## Step 2 â€” The fabrication rule (non-negotiable)

Items 6, 8, 15, 20 â€” and the address in 14/17 â€” are **trust claims**. An agent filling them in invents a company that does not exist and exposes the user to an FTC endorsement-guide problem and, for reviews, platform bans.

For every `NEEDS-HUMAN` item:

1. Build the component, template, and schema so the slot is ready.
2. Fill it with an obvious placeholder â€” `[REVIEW: paste from Google, with reviewer first name + last initial]` â€” that is visibly wrong if shipped, never plausible filler.
3. Collect all of them into **one** batch ask at the end. Do not interrupt the audit item by item.

If the user says "just make something up," build it clearly labeled as sample content and say plainly that it must be replaced before the site is public.

## Step 3 â€” Fix in dependency order

1. **Crawl blockers first** â€” #10 robots.txt, stray `noindex`, canonical tags. A perfect site nobody can index is a dead site.
2. **Mechanical, agent-only** â€” #1, #3, #4, #5, #11, #12, #13, #16, #18, #19, #21, #22, #23, #24. No user input needed; do them all.
3. **Conversion** â€” #2, #9, #7. Needs the user's actual offer; ask once, then build.
4. **Local** â€” #14, #17. Needs the verified NAP.
5. **Trust batch** â€” #6, #8, #15, #20. The single ask from Step 2.

## Step 4 â€” Verify, don't assert

Launch-blocking items get an actual check, not a claim:

```bash
curl -sI https://<site>/no-such-page | head -1     # must be 404, not 200
curl -s  https://<site>/robots.txt                  # must not Disallow: /
curl -s  https://<site>/ | grep -oE '<title>[^<]*|og:image[^>]*|name="description"[^>]*'
```

Then: load the homepage on a 390px viewport (sticky CTA visible? CTA above fold?), run the URL through a rich-results validator for the JSON-LD, and confirm analytics registers a realtime hit. Report the last three as done or as not-yet-verified â€” never as assumed.

## Step 5 â€” Ship report

Output: the Step 1 table updated to final state, the trust-batch ask, and anything left unverified. Then hand over the deploy command â€” for Trevor's Cloudflare Pages apps, editing the source does not update the live page (`.agents/rules/deploy-cloudflare-pages-apps.md`).

## Composes with

- `seo-audit` â€” deeper technical SEO on a site that is already live and underperforming
- `schema` â€” full structured-data implementation beyond #5/#7/#15/#17
- `launch` â€” the go-to-market plan that runs *after* this gate passes
- `impeccable` / `web-design-guidelines` â€” visual and UX quality, which this checklist deliberately does not judge
- `mobile-accessibility` / `wcag-audit-patterns` â€” #16 is the floor, not the ceiling
- `ai-writing-detection` â€” any copy written for #2, #7, #12 gets the tells cut
