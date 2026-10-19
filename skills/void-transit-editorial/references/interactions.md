# Signature Interactions

## Contents

- [4.1 Pinned smootherstep hero](#41-pinned-smootherstep-hero)
- [4.2 Horizontal scroll-jacked lookbook (conveyor)](#42-horizontal-scroll-jacked-lookbook-conveyor)
- [4.3 Pointer-parallax lerp follower](#43-pointer-parallax-lerp-follower)
- [4.4 Shared section-entrance engine](#44-shared-section-entrance-engine)

All four run off one `requestAnimationFrame` loop gated by a `ticking` flag and a passive scroll listener; all four are disabled when `reduceMotion` is true.

```js
const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
const clamp = (n,min=0,max=1)=>Math.min(max,Math.max(min,n));
addEventListener('scroll',()=>{ if(!ticking){requestAnimationFrame(update);ticking=true;} },{passive:true});
```

## 4.1 Pinned smootherstep hero
Outer section is taller than the viewport (~170vh); inner panel is `position:sticky;top:65px`. Normalize scroll through the pin to `0..1`, run it through **smootherstep**, and derive three overlapping phases:

```js
const lr = launch.getBoundingClientRect();
const pinRange = Math.max(1, launch.offsetHeight - innerHeight);
const p = clamp(-lr.top / pinRange);                 // 0..1 progress through the pin
const ease = n => n*n*n*(n*(n*6-15)+10);             // smootherstep (Ken Perlin)
const intro   = ease(clamp(p / .3));                 // 0 â†’ .3   : bg + title settle
const build   = ease(clamp((p - .12) / .64));        // .12 â†’ .76: stamps/orbit/number track in
const release = ease(clamp((p - .7) / .3));          // .7 â†’ 1   : layers ease off
```

Drive transforms and CSS custom props (`--hero-progress`, `--hero-num-x/y/scale`) from `intro/build/release`. **Critical:** ancestors of the sticky hero use `overflow:clip`, never `hidden`, or the pin dies.

## 4.2 Horizontal scroll-jacked lookbook (conveyor)
Tall outer + sticky full-screen inner + a flex track of full-screen cards translated on X from vertical progress. A progress meter and the active-card label read from the *same* normalized progress.

```css
.conveyor{height:440vh}                               /* outer = ~cards Ã— screens */
.conveyor-sticky{position:sticky;top:65px;height:calc(100vh - 65px);overflow:hidden}
.track{position:absolute;height:100%;display:flex;width:max-content}
.slide{width:calc(100vw - var(--rail));flex:none}
```
```js
const cr = conveyor.getBoundingClientRect();
const cp = clamp(-cr.top / (cr.height - innerHeight));            // 0..1
const railPx = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--rail'));
const travel = Math.max(0, track.scrollWidth - (innerWidth - railPx));
track.style.transform = `translate3d(${-cp*travel}px,0,0)`;
meter.style.transform = `scaleX(${1 + cp*3})`;                    // meter base 25% â†’ 100%
frameLabel.textContent = labels[Math.min(3, Math.floor(cp*4))];  // synced active label
slides.forEach((s,i)=>{ s._local = cp*3 - i; paintSlide(s, s._local); }); // per-card local progress
```
Each card layers, back-to-front: giant background display word, orbit ring w/ accent dots, transparent subject cutout, outlined foreground word, card title, caption, floating spec chip.

## 4.3 Pointer-parallax lerp follower
Never assign the pointer position directly â€” keep `current` and `target`, update only `target` on move, and ease `current` toward it each frame. One follower serves hero and every card.

```js
const followPointer = (t, draw) => {
  if (t._motionFrame) return;                          // one rAF chain per target
  const step = () => {
    t._px += (t._targetX - t._px) * .18;               // ease ~18% of remaining distance / frame
    t._py += (t._targetY - t._py) * .18;
    draw(t._pointerVelocity);
    const moving = Math.abs(t._targetX-t._px)+Math.abs(t._targetY-t._py) > .001;
    if (moving) t._motionFrame = requestAnimationFrame(step);
    else { t._px=t._targetX; t._py=t._targetY; t._motionFrame=0; draw(t._pointerVelocity); }
  };
  t._motionFrame = requestAnimationFrame(step);
};
stage.addEventListener('pointermove', e => {
  if (reduceMotion || e.pointerType === 'touch') return;         // disabled on touch + reduced motion
  const r = stage.getBoundingClientRect();
  t._targetX = ((e.clientX-r.left)/r.width  - .5) * 2;           // -1..1, only the TARGET moves
  t._targetY = ((e.clientY-r.top )/r.height - .5) * 2;
  followPointer(t, v => paintSlide(s, s._local, v));
});
// pointerleave: set target to 0,0 and let the SAME follower ease home â€” no jump on re-entry
```
Per-depth speed: background type moves least, subject more, foreground type most, orbit ring independent. Keep semantic text inside safe zones at max offset so parallax never pushes it off-screen or under the rail.

## 4.4 Shared section-entrance engine
One timing engine, several gestures. A spec array tags each element with a variant class + staggered `--enter-delay`; an IntersectionObserver activates them; a passed-element fallback catches hash jumps / fast scroll so nothing is ever left invisible.

```js
const entranceSpecs = [ // [selector, variant, baseDelayMs, perElementStepMs]
  ['.lab-header>h2','enter-left',260,0], ['.lab-module','enter-up',120,110], /* â€¦ */ ];
entranceSpecs.forEach(([sel,type,base,step]) =>
  document.querySelectorAll(sel).forEach((el,i)=>{ el.classList.add('enter',type);
    el.style.setProperty('--enter-delay', `${base + i*step}ms`); }));

const activatePassedEntrances = () =>            // fallback: hash jump / fast scroll safety net
  document.querySelectorAll('.enter:not(.active)').forEach(el=>{
    if (el.getBoundingClientRect().top < innerHeight*.92) el.classList.add('active'); });
new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting) e.target.classList.add('active'); }),
  {threshold:.08, rootMargin:'0px 0px -4% 0px'}).observe(/* each .enter/.reveal */);
```
```css
.enter{opacity:0;transition:opacity .85s var(--ease) var(--enter-delay),
  transform 1s var(--ease) var(--enter-delay),clip-path 1.1s var(--ease) var(--enter-delay)}
.enter-left{transform:translate3d(-90px,35px,0) rotate(-5deg);filter:blur(5px)}
.enter-right{transform:translate3d(100px,-25px,0) rotate(5deg);filter:blur(5px)}
.enter-up{transform:translate3d(0,85px,0) rotate(2deg)}
.enter-down{transform:translate3d(0,-70px,0) rotate(-2deg)}
.enter-scale{transform:scale(.72) rotate(-7deg);filter:blur(7px)}
.enter-clip{clip-path:inset(0 100% 0 0)}
.enter-clip-reverse{clip-path:inset(0 0 0 100%)}
.enter.active{opacity:1;transform:none;clip-path:inset(0);filter:none}
```
Give each section its own variant + stagger â€” never one generic fade-up everywhere. The first-load hero entrance is a separate set of `@keyframes`; remove its class after ~1.55s so scroll transforms take over cleanly.
