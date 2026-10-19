
### F1 Â· Bento grid
Asymmetric grid of 8â€“15 tiles in mixed spans (1Ã—1, 2Ã—1, 1Ã—2, 2Ã—2). Visual rhythm via size.
*Use when:* multiple equally-valid entry points; SaaS feature page.
*Don't confuse with:* F2 Sticky-scroll (which stacks vertically with sticky pacing).

```html
<section class="bento">
  <article class="cell span-2x2">â€¦</article>
  <article class="cell span-1x1">â€¦</article>
  <article class="cell span-2x1">â€¦</article>
</section>
```
```css
.bento { display: grid; grid-template-columns: repeat(4, 1fr); grid-auto-rows: 12rem; gap: var(--space-md); }
.span-2x2 { grid-column: span 2; grid-row: span 2; }
.span-2x1 { grid-column: span 2; }
.span-1x2 { grid-row: span 2; }
@media (max-width: 56rem) { .bento { grid-template-columns: repeat(2, 1fr); } }
```
