### S4 Â· Inline (no break)
The heading is a small caps phrase that emerges *inside* the body flow; no spatial break.
*Use when:* the page is prose-led; reading should be continuous.
*Don't confuse with:* S2 Hanging (which separates with negative space).

```html
<p>â€¦ <span class="head-inline">A small heading.</span> â€¦</p>
```
```css
.head-inline { font-variant-caps: all-small-caps; letter-spacing: 0.06em; font-weight: 500; }
```
