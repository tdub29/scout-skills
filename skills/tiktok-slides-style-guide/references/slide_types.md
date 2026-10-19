# TikTok Slide Types

## Slide Types

### Hook Slides

Big-text attention grabbers. Pattern:

```
[Edosz headline â€” one bold statement]
[Lime green "Under Par / Fantasy golf" Edosz subline]
(body-colored parenthetical quip)

underparfantasy.com  â† footer
```

Each hook is defined as a `HookDef` object:

```typescript
type HookDef = {
  bg: number;          // bgIndex (0-2)
  size: string;        // Tailwind text size + leading
  headline: ReactNode; // The hook text
  sub?: ReactNode;     // Optional subline (usually null for sacrifice hooks)
  quip?: string;       // Parenthetical dismissal
};
```

**Sacrifice hook pattern** (the "I did X to build Under Par" format):
- Headline: `text-[6.95rem] leading-[1.08]` with the situation
- Subline: Edosz "to build" + lime "Under Par / Fantasy golf"
- Quip: Dismissive parenthetical like "(he's fine)" or "(she'll find another one)"
- Always end the headline portion at the natural break before "to build"

**Layout:** Centered flex column with `justify-between` between headline area and footer URL.

### Odds/Table Slides

Data-driven slides showing tournament field info.

**Table container:**
```
rounded-[1.25rem] border-[3px] border-[#4d6b5c] bg-[#183026] shadow-[0_20px_48px_rgba(0,0,0,0.4)]
```

**Two grid modes:**

Default (favorites/sleepers â€” no rank column):
```
grid-cols-[minmax(0,1fr)_110px_148px_102px] gap-x-4
```
Columns: Player | OWGR | Odds | Price

Dense (full field â€” with rank column):
```
grid-cols-[56px_minmax(0,400px)_100px_132px_100px] gap-x-4
```
Columns: # | Player | OWGR | Odds | Price

**Cell colors:**

| Cell | Color | Weight |
|------|-------|--------|
| Rank # | muted | Bold |
| Player name | text (foreground) | Semibold |
| OWGR | muted | Medium |
| Odds | lime | Bold |
| Price | text (foreground) | Bold |

**Row styling:**
- Default: `px-5 py-[13px] text-[3.2rem]`
- Dense: `px-5 py-[10px] text-[2.65rem]`
- Divider: `border-b border-[#4d6b5c]/30` (omit on last row)

**Pagination:** Full field uses `ROWS_PER_FIELD_SLIDE = 20` rows per page.

**Slide footer:** Lime-colored `underparfantasy.com` with drop shadow, right-aligned or centered.
