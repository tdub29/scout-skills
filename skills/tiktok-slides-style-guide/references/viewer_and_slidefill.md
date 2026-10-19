# Viewer Integration and SlideFill Helper

## Viewer Integration

All decks must be added to `tiktok-slideshow-viewer.html`.

Each deck is defined in the `decks` array:

```javascript
{
  label: "Deck Name",
  folder: "exports/tiktok/{name}",
  // Option A: sequential numbered files
  count: 7,
  filePrefix: "slide-",
  pad: 2,
  // Option B: explicit file names (for renamed/descriptive files)
  files: ["descriptive-name-01.png", "descriptive-name-02.png"],
}
```

Use `files` array when slides have descriptive names. Use `count`/`filePrefix`/`pad` for sequentially numbered slides.

---

## SlideFill Helper

Use `SlideFill` for content that should fill the remaining vertical space:

```tsx
function SlideFill({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <div className={`flex min-h-0 w-full flex-1 flex-col ${className ?? "justify-center"}`}>
      {children}
    </div>
  );
}
```
