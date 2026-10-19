# Site Type Templates

Full page hierarchy templates with ASCII trees, URL maps, and navigation recommendations for common site types.

---

## SaaS Marketing Site

### Page Hierarchy

```
Homepage (/)
â”œâ”€â”€ Features (/features)
â”‚   â”œâ”€â”€ Feature A (/features/feature-a)
â”‚   â”œâ”€â”€ Feature B (/features/feature-b)
â”‚   â””â”€â”€ Feature C (/features/feature-c)
â”œâ”€â”€ Pricing (/pricing)
â”œâ”€â”€ Customers (/customers)
â”‚   â”œâ”€â”€ Case Study 1 (/customers/company-name)
â”‚   â””â”€â”€ Case Study 2 (/customers/company-name-2)
â”œâ”€â”€ Resources (/resources)
â”‚   â”œâ”€â”€ Blog (/blog)
â”‚   â”‚   â””â”€â”€ [Posts] (/blog/post-slug)
â”‚   â”œâ”€â”€ Templates (/resources/templates)
â”‚   â”‚   â””â”€â”€ [Template] (/resources/templates/template-slug)
â”‚   â””â”€â”€ Guides (/resources/guides)
â”‚       â””â”€â”€ [Guide] (/resources/guides/guide-slug)
â”œâ”€â”€ Integrations (/integrations)
â”‚   â””â”€â”€ [Integration] (/integrations/integration-name)
â”œâ”€â”€ Docs (/docs)
â”‚   â”œâ”€â”€ Getting Started (/docs/getting-started)
â”‚   â”œâ”€â”€ Guides (/docs/guides)
â”‚   â””â”€â”€ API Reference (/docs/api)
â”œâ”€â”€ About (/about)
â”‚   â”œâ”€â”€ Careers (/about/careers)
â”‚   â””â”€â”€ Contact (/contact)
â”œâ”€â”€ Compare (/compare)
â”‚   â””â”€â”€ [Competitor] (/compare/competitor-name)
â”œâ”€â”€ Privacy (/privacy)
â””â”€â”€ Terms (/terms)
```

### URL Map

| Page | URL | Nav Location | Priority |
|------|-----|-------------|----------|
| Homepage | `/` | Header (logo) | Critical |
| Features | `/features` | Header | High |
| Feature pages | `/features/{slug}` | Header dropdown | Medium |
| Pricing | `/pricing` | Header | Critical |
| Customers | `/customers` | Header | Medium |
| Case studies | `/customers/{slug}` | Customers dropdown | Medium |
| Blog | `/blog` | Header (Resources) | High |
| Blog posts | `/blog/{slug}` | â€” | Medium |
| Integrations | `/integrations` | Header | Medium |
| Docs | `/docs` | Header | Medium |
| Compare | `/compare/{slug}` | Footer | High (SEO) |
| About | `/about` | Footer | Low |
| Pricing CTA | `/pricing` | Header (CTA button) | Critical |

### Navigation

**Header (6 items + CTA)**: Features | Pricing | Customers | Resources | Integrations | Docs | [Get Started]

**Footer columns**:
- Product: Features, Pricing, Integrations, Changelog, Security
- Resources: Blog, Templates, Guides, Case Studies
- Company: About, Careers, Contact, Press
- Legal: Privacy, Terms, Security

---

## Content / Blog Site

### Page Hierarchy

```
Homepage (/)
â”œâ”€â”€ Blog (/blog)
â”‚   â”œâ”€â”€ [Category: Topic A] (/blog/category/topic-a)
â”‚   â”œâ”€â”€ [Category: Topic B] (/blog/category/topic-b)
â”‚   â”œâ”€â”€ [Category: Topic C] (/blog/category/topic-c)
â”‚   â””â”€â”€ [Posts] (/blog/post-slug)
â”œâ”€â”€ Newsletter (/newsletter)
â”œâ”€â”€ Resources (/resources)
â”‚   â”œâ”€â”€ Guides (/resources/guides)
â”‚   â”‚   â””â”€â”€ [Guide] (/resources/guides/guide-slug)
â”‚   â””â”€â”€ Tools (/resources/tools)
â”‚       â””â”€â”€ [Tool] (/resources/tools/tool-slug)
â”œâ”€â”€ About (/about)
â”œâ”€â”€ Contact (/contact)
â”œâ”€â”€ Privacy (/privacy)
â””â”€â”€ Terms (/terms)
```

### URL Map

| Page | URL | Nav Location | Priority |
|------|-----|-------------|----------|
| Homepage | `/` | Header (logo) | Critical |
| Blog index | `/blog` | Header | High |
| Categories | `/blog/category/{slug}` | Header dropdown | Medium |
| Posts | `/blog/{slug}` | â€” | Medium |
| Newsletter | `/newsletter` | Header (CTA) | High |
| Guides | `/resources/guides` | Header | Medium |
| About | `/about` | Header | Low |

### Navigation

**Header (4 items + CTA)**: Blog | Resources | About | Contact | [Subscribe]

**Sidebar** (on blog): Categories, Popular Posts, Newsletter signup

---

## E-Commerce

### Page Hierarchy

```
Homepage (/)
â”œâ”€â”€ Shop (/shop)
â”‚   â”œâ”€â”€ Category A (/shop/category-a)
â”‚   â”‚   â”œâ”€â”€ Subcategory (/shop/category-a/subcategory)
â”‚   â”‚   â”‚   â””â”€â”€ [Product] (/shop/category-a/subcategory/product-slug)
â”‚   â”‚   â””â”€â”€ [Product] (/shop/category-a/product-slug)
â”‚   â”œâ”€â”€ Category B (/shop/category-b)
â”‚   â”‚   â””â”€â”€ [Product] (/shop/category-b/product-slug)
â”‚   â””â”€â”€ Category C (/shop/category-c)
â”‚       â””â”€â”€ [Product] (/shop/category-c/product-slug)
â”œâ”€â”€ Collections (/collections)
â”‚   â””â”€â”€ [Collection] (/collections/collection-slug)
â”œâ”€â”€ Sale (/sale)
â”œâ”€â”€ Blog (/blog)
â”‚   â””â”€â”€ [Posts] (/blog/post-slug)
â”œâ”€â”€ About (/about)
â”‚   â””â”€â”€ Our Story (/about/our-story)
â”œâ”€â”€ Help (/help)
â”‚   â”œâ”€â”€ FAQ (/help/faq)
â”‚   â”œâ”€â”€ Shipping (/help/shipping)
â”‚   â”œâ”€â”€ Returns (/help/returns)
â”‚   â””â”€â”€ Contact (/contact)
â”œâ”€â”€ Cart (/cart)
â”œâ”€â”€ Account (/account)
â”œâ”€â”€ Privacy (/privacy)
â””â”€â”€ Terms (/terms)
```

### URL Map

| Page | URL | Nav Location | Priority |
|------|-----|-------------|----------|
| Homepage | `/` | Header (logo) | Critical |
| Shop | `/shop` | Header | Critical |
| Categories | `/shop/{category}` | Header mega menu | High |
| Products | `/shop/{category}/{product}` | â€” | High |
| Collections | `/collections/{slug}` | Header | Medium |
| Sale | `/sale` | Header (highlighted) | High |
| Cart | `/cart` | Header (icon) | Critical |
| Account | `/account` | Header (icon) | Medium |

### Navigation

**Header (5 items + cart/account)**: Shop (mega menu) | Collections | Sale | Blog | Help | [Cart icon] [Account icon]

**Mega menu under Shop**: Category columns with featured products/images

---

## Documentation Site

### Page Hierarchy

```
Docs Home (/docs)
â”œâ”€â”€ Getting Started (/docs/getting-started)
â”‚   â”œâ”€â”€ Installation (/docs/getting-started/installation)
â”‚   â”œâ”€â”€ Quick Start (/docs/getting-started/quick-start)
â”‚   â””â”€â”€ Configuration (/docs/getting-started/configuration)
â”œâ”€â”€ Guides (/docs/guides)
â”‚   â”œâ”€â”€ Guide A (/docs/guides/guide-a)
â”‚   â”œâ”€â”€ Guide B (/docs/guides/guide-b)
â”‚   â””â”€â”€ Guide C (/docs/guides/guide-c)
â”œâ”€â”€ API Reference (/docs/api)
â”‚   â”œâ”€â”€ Authentication (/docs/api/authentication)
â”‚   â”œâ”€â”€ Endpoints (/docs/api/endpoints)
â”‚   â””â”€â”€ Webhooks (/docs/api/webhooks)
â”œâ”€â”€ Examples (/docs/examples)
â”‚   â””â”€â”€ [Example] (/docs/examples/example-slug)
â”œâ”€â”€ Changelog (/docs/changelog)
â””â”€â”€ FAQ (/docs/faq)
```

### URL Map

| Page | URL | Nav Location | Priority |
|------|-----|-------------|----------|
| Docs home | `/docs` | Header | High |
| Getting Started | `/docs/getting-started` | Sidebar (top) | Critical |
| Guides | `/docs/guides` | Sidebar | High |
| API Reference | `/docs/api` | Sidebar | High |
| Changelog | `/docs/changelog` | Sidebar (bottom) | Low |

### Navigation

**Header**: Docs | API | Blog | Community | GitHub | [Dashboard]

**Sidebar** (persistent, left): Getting Started, Guides, API Reference, Examples, Changelog â€” with expandable subsections

**On-page**: Previous/Next navigation at bottom of each doc page

---

## Hybrid SaaS + Content

### Page Hierarchy

```
Homepage (/)
â”œâ”€â”€ Product (/product)
â”‚   â”œâ”€â”€ Feature A (/product/feature-a)
â”‚   â”œâ”€â”€ Feature B (/product/feature-b)
â”‚   â””â”€â”€ Feature C (/product/feature-c)
â”œâ”€â”€ Solutions (/solutions)
â”‚   â”œâ”€â”€ By Use Case (/solutions/use-case-slug)
â”‚   â””â”€â”€ By Industry (/solutions/industry-slug)
â”œâ”€â”€ Pricing (/pricing)
â”œâ”€â”€ Blog (/blog)
â”‚   â”œâ”€â”€ [Category] (/blog/category/slug)
â”‚   â””â”€â”€ [Posts] (/blog/post-slug)
â”œâ”€â”€ Resources (/resources)
â”‚   â”œâ”€â”€ Guides (/resources/guides)
â”‚   â”œâ”€â”€ Templates (/resources/templates)
â”‚   â”œâ”€â”€ Webinars (/resources/webinars)
â”‚   â””â”€â”€ Case Studies (/resources/case-studies)
â”œâ”€â”€ Docs (/docs)
â”‚   â”œâ”€â”€ Getting Started (/docs/getting-started)
â”‚   â””â”€â”€ API (/docs/api)
â”œâ”€â”€ Integrations (/integrations)
â”‚   â””â”€â”€ [Integration] (/integrations/slug)
â”œâ”€â”€ Compare (/compare)
â”‚   â””â”€â”€ [Competitor] (/compare/competitor-slug)
â”œâ”€â”€ About (/about)
â”‚   â”œâ”€â”€ Careers (/about/careers)
â”‚   â””â”€â”€ Contact (/contact)
â”œâ”€â”€ Privacy (/privacy)
â””â”€â”€ Terms (/terms)
```

### Navigation

**Header (7 items + CTA)**: Product | Solutions | Pricing | Resources | Blog | Docs | Integrations | [Start Free Trial]

Use mega menus for Product (features list), Solutions (use cases + industries), and Resources (blog, guides, templates, webinars, case studies).

---

## Small Business / Local

### Page Hierarchy

```
Homepage (/)
â”œâ”€â”€ Services (/services)
â”‚   â”œâ”€â”€ Service A (/services/service-a)
â”‚   â”œâ”€â”€ Service B (/services/service-b)
â”‚   â””â”€â”€ Service C (/services/service-c)
â”œâ”€â”€ About (/about)
â”œâ”€â”€ Testimonials (/testimonials)
â”œâ”€â”€ Blog (/blog)
â”‚   â””â”€â”€ [Posts] (/blog/post-slug)
â”œâ”€â”€ Contact (/contact)
â”œâ”€â”€ Privacy (/privacy)
â””â”€â”€ Terms (/terms)
```

### URL Map

| Page | URL | Nav Location | Priority |
|------|-----|-------------|----------|
| Homepage | `/` | Header (logo) | Critical |
| Services | `/services` | Header | High |
| Service pages | `/services/{slug}` | Header dropdown | High |
| About | `/about` | Header | Medium |
| Testimonials | `/testimonials` | Header | Medium |
| Blog | `/blog` | Header | Medium |
| Contact | `/contact` | Header (CTA) | High |

### Navigation

**Header (5 items + CTA)**: Services | About | Testimonials | Blog | [Contact Us]

Keep it simple. Small business sites should be flat (1-2 levels max). Every page should be reachable from the header.
