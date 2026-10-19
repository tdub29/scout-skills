# Craft Details Guide

Implementation details that separate polished products from rough ones. Most AI models miss these.

---

## 1. Focus States

Focus states are for keyboard navigation. Get them wrong and your app feels broken.

### The Rule: `:focus-visible`, Not `:focus`

```css
/* âŒ Shows focus ring on mouse click â€” annoying */
.button:focus {
  outline: 2px solid var(--primary);
}

/* âœ… Shows focus ring only on keyboard navigation */
.button:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}
```

**Why:** `:focus` triggers on any focus (including mouse click). `:focus-visible` only triggers when user is navigating with keyboard.

### Never Remove Focus Without Replacement

```css
/* âŒ NEVER â€” breaks keyboard navigation */
.button:focus {
  outline: none;
}

/* âœ… Replace default with custom visible focus */
.button:focus-visible {
  outline: none;
  box-shadow: 0 0 0 2px var(--bg), 0 0 0 4px var(--primary);
}
```

### Compound Controls: `:focus-within`

For groups where focus on any child should highlight the parent:

```css
/* Search input with icon */
.search-wrapper:focus-within {
  border-color: var(--primary);
  box-shadow: 0 0 0 3px var(--primary-tint);
}
```

---

## 2. Forms

Forms are where users struggle most. These details reduce friction.

### Input Types and Attributes

```html
<!-- âœ… Correct types trigger right keyboard on mobile -->
<input type="email" inputmode="email" autocomplete="email">
<input type="tel" inputmode="tel" autocomplete="tel">
<input type="url" inputmode="url">
<input type="number" inputmode="numeric">

<!-- âœ… Meaningful names help password managers -->
<input name="email" type="email" autocomplete="email">
<input name="password" type="password" autocomplete="current-password">
<input name="new-password" type="password" autocomplete="new-password">
```

### Autocomplete Matters

| Field | `autocomplete` value |
|-------|---------------------|
| Email | `email` |
| Password (login) | `current-password` |
| Password (signup) | `new-password` |
| Name | `name` |
| Phone | `tel` |
| Address | `street-address` |
| Credit card | `cc-number`, `cc-exp`, `cc-csc` |
| Non-auth fields | `off` (prevents password manager triggers) |

### Never Block Paste

```jsx
/* âŒ NEVER â€” accessibility violation, user hostile */
<input onPaste={(e) => e.preventDefault()} />

/* âœ… Let users paste */
<input />
```

### Disable Spellcheck Where Appropriate

```html
<!-- Spellcheck off for: emails, codes, usernames, URLs -->
<input type="email" spellcheck="false">
<input name="username" spellcheck="false">
<input name="verification-code" spellcheck="false">
```

### Labels and Hit Targets

```html
<!-- âœ… Clickable label (explicit) -->
<label for="email">Email</label>
<input id="email" type="email">

<!-- âœ… Clickable label (implicit) -->
<label>
  Email
  <input type="email">
</label>

<!-- âœ… Checkbox: label + control share single hit target -->
<label class="checkbox-wrapper">
  <input type="checkbox">
  <span>Accept terms</span>
</label>
```

```css
/* No dead zones between checkbox and label */
.checkbox-wrapper {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}
```

### Placeholder Formatting

```html
<!-- âœ… Placeholders end with â€¦ and show format -->
<input placeholder="name@company.comâ€¦">
<input placeholder="(555) 123-4567â€¦">
<input placeholder="Search productsâ€¦">
```

### Submit Button States

```jsx
/* âœ… Button enabled until request starts, then shows spinner */
<button 
  type="submit" 
  disabled={isSubmitting}
>
  {isSubmitting ? <Spinner /> : 'Save Changes'}
</button>
```

### Error Handling

```jsx
/* âœ… Errors inline, focus first error on submit */
<form onSubmit={handleSubmit}>
  <input 
    ref={emailRef}
    aria-invalid={errors.email ? 'true' : 'false'}
    aria-describedby={errors.email ? 'email-error' : undefined}
  />
  {errors.email && (
    <span id="email-error" role="alert">
      {errors.email}
    </span>
  )}
</form>
```

### Unsaved Changes Warning

```js
// Warn before leaving with unsaved changes
useEffect(() => {
  const handleBeforeUnload = (e) => {
    if (hasUnsavedChanges) {
      e.preventDefault();
      e.returnValue = '';
    }
  };
  window.addEventListener('beforeunload', handleBeforeUnload);
  return () => window.removeEventListener('beforeunload', handleBeforeUnload);
}, [hasUnsavedChanges]);
```

---

## 3. Images

Images are the #1 cause of layout shift (CLS). Fix them.

### Always Set Dimensions

```html
<!-- âŒ Causes layout shift as image loads -->
<img src="photo.jpg" alt="Product">

<!-- âœ… Reserves space, no layout shift -->
<img src="photo.jpg" alt="Product" width="400" height="300">
```

### Loading Strategy

```html
<!-- Above the fold: load immediately -->
<img src="hero.jpg" fetchpriority="high" alt="Hero">

<!-- Below the fold: lazy load -->
<img src="feature.jpg" loading="lazy" alt="Feature">
```

### In React/Next.js

```jsx
// Critical hero image
<Image src="/hero.jpg" priority alt="Hero" />

// Below fold
<Image src="/feature.jpg" loading="lazy" alt="Feature" />
```

---

## 4. Touch & Mobile

Details that make mobile feel native.

### Tap Delay Removal

```css
/* Remove 300ms tap delay on mobile */
* {
  touch-action: manipulation;
}
```

### Tap Highlight

```css
/* Set intentionally, don't just disable */
button, a {
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0.1);
}
```

### Modal Scroll Lock

```css
/* Prevent scroll chaining in modals/drawers */
.modal, .drawer, .sheet {
  overscroll-behavior: contain;
}
```

### AutoFocus Rules

- Desktop only â€” avoid on mobile (opens keyboard unexpectedly)
- Single primary input per page maximum
- Must be justified â€” not "just because"

```jsx
/* âœ… Desktop-only autofocus */
<input autoFocus={!isMobile} />
```

---

## 5. Performance Patterns

Patterns that prevent jank.

### Virtualize Large Lists

Lists with 50+ items should be virtualized:

```jsx
// Use virtua, react-window, or similar
import { VList } from 'virtua';

<VList style={{ height: 400 }}>
  {items.map(item => <Row key={item.id} data={item} />)}
</VList>
```

**Or CSS-only for simpler cases:**

```css
.long-list {
  content-visibility: auto;
  contain-intrinsic-size: 0 50px; /* estimated item height */
}
```

### Avoid Layout Reads in Render

```jsx
/* âŒ Forces synchronous layout recalculation */
function Component() {
  const height = elementRef.current.offsetHeight; // BAD
  return <div style={{ marginTop: height }} />;
}

/* âœ… Use ResizeObserver or CSS */
function Component() {
  const [height, setHeight] = useState(0);
  useLayoutEffect(() => {
    const observer = new ResizeObserver(([entry]) => {
      setHeight(entry.contentRect.height);
    });
    observer.observe(elementRef.current);
    return () => observer.disconnect();
  }, []);
  return <div style={{ marginTop: height }} />;
}
```

### Uncontrolled Inputs When Possible

```jsx
/* âŒ Re-renders on every keystroke */
const [value, setValue] = useState('');
<input value={value} onChange={e => setValue(e.target.value)} />

/* âœ… No re-renders during typing */
<input defaultValue="" ref={inputRef} />

/* Get value on submit */
const handleSubmit = () => {
  const value = inputRef.current.value;
};
```

### Preconnect to CDNs

```html
<head>
  <!-- Preconnect to asset domains -->
  <link rel="preconnect" href="https://cdn.example.com">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  
  <!-- Preload critical fonts -->
  <link 
    rel="preload" 
    href="/fonts/inter.woff2" 
    as="font" 
    type="font/woff2" 
    crossorigin
  >
</head>
```

---

## 6. Accessibility Quick Wins

High-impact, low-effort accessibility fixes.

### Semantic Elements

```html
<!-- âŒ Div with click handler -->
<div onClick={handleClick}>Click me</div>

<!-- âœ… Proper button -->
<button onClick={handleClick}>Click me</button>

<!-- âŒ Span styled as link -->
<span onClick={navigate} className="link">Go here</span>

<!-- âœ… Proper link -->
<a href="/page">Go here</a>
```

### Keyboard Handlers

Interactive custom elements need keyboard support:

```jsx
<div 
  role="button"
  tabIndex={0}
  onClick={handleClick}
  onKeyDown={(e) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleClick();
    }
  }}
>
  Custom button
</div>
```

### Heading Hierarchy

```html
<!-- âœ… Proper heading order -->
<h1>Page Title</h1>
  <h2>Section</h2>
    <h3>Subsection</h3>
  <h2>Another Section</h2>

<!-- âŒ Skipping levels -->
<h1>Page Title</h1>
  <h4>Section</h4> <!-- Wrong: skipped h2, h3 -->
```

### Scroll Margin for Anchors

```css
/* Prevents fixed header from covering anchor targets */
[id] {
  scroll-margin-top: 80px; /* height of fixed header + buffer */
}
```

### Async Updates Need Announcements

```jsx
/* Toast notifications, validation messages */
<div role="status" aria-live="polite">
  {message}
</div>
```

---

## 7. Navigation & State

URL should reflect app state. Users expect to bookmark, share, and use back button.

### URL Reflects State

```jsx
/* âœ… Filters, tabs, pagination in URL */
// /products?category=shoes&sort=price&page=2

/* Use nuqs or similar for easy URL state sync */
import { useQueryState } from 'nuqs';
const [category, setCategory] = useQueryState('category');
```

### Links Support Browser Features

```jsx
/* âŒ onClick navigation â€” breaks Cmd+click, middle-click */
<div onClick={() => navigate('/page')}>Go</div>

/* âœ… Proper link â€” all browser features work */
<Link href="/page">Go</Link>
```

### Destructive Actions Need Confirmation

```jsx
/* âŒ Immediate destructive action */
<button onClick={deleteAccount}>Delete Account</button>

/* âœ… With confirmation */
<button onClick={() => setShowConfirmModal(true)}>Delete Account</button>

/* Or with undo window */
<button onClick={deleteWithUndo}>Delete Account</button>
// Toast: "Account deleted. Undo (10s)"
```

---

## 8. Content Copy Rules

Writing that converts.

| Rule | Example |
|------|---------|
| **Active voice** | "Install the CLI" not "The CLI will be installed" |
| **Title Case for headings/buttons** | "Save Changes" not "Save changes" |
| **Numerals for counts** | "8 deployments" not "eight deployments" |
| **Specific labels** | "Save API Key" not "Continue" |
| **Error messages include fix** | "Email invalid. Use format: name@domain.com" |
| **Second person** | "Your account" not "My account" |
| **& over "and"** (space-constrained) | "Terms & Privacy" |

---

## 9. Anti-Patterns Checklist

Flag these during code review:

- [ ] `user-scalable=no` or `maximum-scale=1` â€” disables zoom, accessibility violation
- [ ] `onPaste` with `preventDefault` â€” blocks paste, user hostile
- [ ] `transition: all` â€” performance killer, unpredictable
- [ ] `outline: none` without `:focus-visible` replacement â€” breaks keyboard nav
- [ ] `<div onClick>` for navigation â€” use `<a>` or `<Link>`
- [ ] `<div>` or `<span>` as buttons â€” use `<button>`
- [ ] Images without `width`/`height` â€” causes CLS
- [ ] Large arrays `.map()` without virtualization (50+ items)
- [ ] Form inputs without labels â€” accessibility fail
- [ ] Icon buttons without `aria-label`
- [ ] Hardcoded date/number formats â€” use `Intl.DateTimeFormat`, `Intl.NumberFormat`
- [ ] `autoFocus` without clear justification

---

## Pre-Ship Checklist

- [ ] **Focus:** `:focus-visible` not `:focus`, never bare `outline: none`
- [ ] **Forms:** Correct `type`, `inputmode`, `autocomplete` attributes
- [ ] **Forms:** Labels on all inputs, no paste blocking
- [ ] **Images:** `width`/`height` set, `loading="lazy"` below fold
- [ ] **Touch:** `touch-action: manipulation`, `overscroll-behavior: contain` in modals
- [ ] **Performance:** Large lists virtualized, no layout reads in render
- [ ] **A11y:** Semantic HTML, keyboard handlers, heading hierarchy
- [ ] **URLs:** State reflected in URL, proper `<a>`/`<Link>` for navigation
- [ ] **Copy:** Active voice, specific labels, errors include fix

---

*Details matter. These patterns are the difference between "works" and "feels right."*
