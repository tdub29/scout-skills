# TikTok Slide Common Patterns

## Common Patterns

### Section Header (above a table)

```tsx
<p className="text-[3rem] font-black uppercase tracking-[0.2em] text-[#a4d944]">
  SECTION LABEL
</p>
<h2 className="text-[6.5rem] font-bold leading-[1.02] tracking-tight drop-shadow-[0_10px_36px_rgba(0,0,0,0.55)]"
    style={{ fontFamily: '"Edosz", sans-serif' }}>
  Tournament Title
</h2>
<p className="text-[3rem] font-medium tracking-tight text-[#c7d8cf]">
  Subtitle description
</p>
```

### Table Header Row

```tsx
<div className="grid border-b-[3px] border-[#4d6b5c]/50 px-5 pb-3 pt-2 text-[2rem] font-black uppercase tracking-[0.14em] text-[#aabeb4]"
     style={{ gridTemplateColumns: "minmax(0,1fr) 110px 148px 102px" }}>
  <span>Player</span>
  <span className="text-right">OWGR</span>
  <span className="text-right">Odds</span>
  <span className="text-right">Price</span>
</div>
```

### Table Data Row

```tsx
<div className="grid items-center border-b border-[#4d6b5c]/30 px-5 py-[13px] text-[3.2rem] leading-[1.15]"
     style={{ gridTemplateColumns: "minmax(0,1fr) 110px 148px 102px" }}>
  <span className="truncate font-semibold text-[#f5f2e8]">{name}</span>
  <span className="text-right font-medium text-[#aabeb4]">{owgr}</span>
  <span className="text-right font-bold text-[#a4d944]">{odds}</span>
  <span className="text-right font-bold text-[#f5f2e8]">${price}</span>
</div>
```

### Lime Footer URL

```tsx
<p className="text-[3.5rem] font-semibold leading-tight tracking-tight text-[#a4d944] drop-shadow-[0_4px_20px_rgba(0,0,0,0.45)]">
  underparfantasy.com
</p>
```
