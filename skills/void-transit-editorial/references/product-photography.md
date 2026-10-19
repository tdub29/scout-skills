# Product-Photography Moves

The imagery is what sells the aesthetic. Full method + prompts in `image-prompts.md`; the moves:
- **Consistent subject via an invariants paragraph** pasted into every image prompt (same model/garment/details) so a shot series reads as one campaign.
- **Ghost-mannequin** product shot (garment worn by an invisible form) for the commerce section.
- **Exploded top-down flat-lay** (equipment-diagram layout) for a full-width "system laboratory" section.
- **Green-screen then cutout:** generate on one flat chroma-green background â†’ remove it â†’ transparent PNG â†’ verify all four corners are transparent.
- **Offset flat-color drop-shadow "sticker" look** â€” hard shadow, zero blur, so the cutout reads as a pasted sticker floating over the grid:

```css
.cutout{filter:drop-shadow(22px 28px 0 rgba(16,16,16,.14))}  /* note: 0 blur radius */
```
Cutouts on colored slides can use `mix-blend-mode:multiply` to fuse into the accent field.
