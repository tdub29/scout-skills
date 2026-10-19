# Category Signal Mapping

```json
// references/manifest.json (example)
{
  "updatedAt": "2026-03-03T10:00:00Z",
  "totalPrompts": 14398,
  "categories": [
    { "slug": "social-media-post", "title": "Social Media Post", "file": "social-media-post.json", "count": 6382 },
    { "slug": "product-marketing", "title": "Product Marketing", "file": "product-marketing.json", "count": 3709 }
    // ... more categories
  ]
}
```

## Category Signal Mapping

**Do NOT rely on a hardcoded table** â€” categories change over time.

Instead, after loading `manifest.json`, match user intent to categories dynamically:

1. Read `references/manifest.json` â†’ get `categories[]` with `slug` + `title`
2. Infer the best-matching category from the `title` (e.g. "Social Media Post" â†’ social content requests)
3. Search the corresponding `file` (e.g. `social-media-post.json`)

**Matching heuristic** (use category `title` as semantic anchor):
- User says "avatar / profile / headshot / selfie" â†’ find category with title containing "Avatar" or "Profile"
- User says "infographic / diagram / chart" â†’ find category with title containing "Infographic"
- User says "youtube / thumbnail / video cover" â†’ find category with title containing "YouTube" or "Thumbnail"
- User says "product / marketing / ad / promo" â†’ find category with title containing "Product" or "Marketing"
- User says "poster / flyer / banner / event" â†’ find category with title containing "Poster" or "Flyer"
- User says "e-commerce / product photo / listing" â†’ find category with title containing "E-commerce" or "Ecommerce"
- User says "game / sprite / character / asset" â†’ find category with title containing "Game"
- User says "comic / manga / storyboard" â†’ find category with title containing "Comic" or "Storyboard"
- User says "app / UI / web / interface" â†’ find category with title containing "App" or "Web"
- User says "instagram / twitter / social / post" â†’ find category with title containing "Social"
- No clear match â†’ try `others.json` or search multiple categories in parallel
