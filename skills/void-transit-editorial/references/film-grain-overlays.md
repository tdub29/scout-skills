# Film Grain and Scanline Overlays

```css
/* fixed fractal-noise grain, multiply blend, very low opacity */
.noise{position:fixed;z-index:300;inset:0;pointer-events:none;opacity:.08;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 160 160' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.5'/%3E%3C/svg%3E")}

/* animated scanline band over media stages */
.slide-stage:after{content:'';position:absolute;inset:0;pointer-events:none;opacity:.28;
  background:linear-gradient(transparent 49.7%,rgba(0,0,0,.12) 50%,transparent 50.3%);
  background-size:100% 8px;animation:scan 8s linear infinite}
@keyframes scan{to{background-position:0 100px}}
```
