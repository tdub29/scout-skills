## 06 Â· Conversational FAQ

Bold questions, brief answers. The page reads like an honest interview with the product. Often each Q/A is a collapsible accordion.

- **Heading:** each section *is* a question â€” a short, direct phrase ending in `?`.
- **Body:** answer in 2â€“4 short paragraphs immediately below the question.
- **Divider:** thin rule between Q/A pairs, or zero rule and a paper-colour swap.
- **Button:** typographic link inside answers ("Read the full policy â†’"); one outlined CTA at the foot.
- **Image:** sparse â€” maybe one diagram per long answer; mostly text.
- **Reveal:** none on load; accordion expand uses 200 ms `--ease-out` on `grid-template-rows: 0fr â†’ 1fr`.

Reach for it near pricing, for products that meet skepticism, for educational/regulated industries.

Avoid as the *primary* page. FAQ usually pairs with another macrostructure that opens the page.

Reference: many SaaS pricing pages, Casper, Substack help pages.

**Sample opening lines** (imitate the *specificity* â€” questions are real questions, answers are short and concrete):
> *"What is this for? â€” A single-binary CLI for parsing log streams from stdin."* â€” names the form factor, names the input
> *"How is this different from X? â€” It's about time."* â€” cron.com â€” answers obliquely, with a phrase that has weight
> *"Who built this? â€” Three of us, in Lisbon, since 2014."* â€” date + place + count, no marketing

```html
<section class="faq">
  <details>
    <summary><h2>How long does setup take?</h2></summary>
    <div class="answer">â€¦</div>
  </details>
  <details>â€¦</details>
</section>
```

---
