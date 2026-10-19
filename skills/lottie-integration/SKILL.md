---
name: lottie-integration
description: Add or debug Lottie animations on web (Next.js), React Native, or Remotion using the right library and docs.
---

# Lottie integration (Under Par)

## When to use

- User asks for **Lottie**, **Bodymovin JSON**, **`.lottie` files**, or **After Effectsâ€“exported** animations in the app or in Remotion renders.

## Canonical repos

1. **[lottie-web](https://github.com/airbnb/lottie-web)** â€” Renders Lottie JSON in the browser (SVG / canvas / HTML). npm: `lottie-web`. High-level docs: [airbnb.io/lottie](https://airbnb.io/lottie/).
2. **[lottie-react-native](https://github.com/lottie-react-native/lottie-react-native)** â€” Native iOS/Android (and Windows) player for React Native. Read **[MIGRATION-5-TO-6.md](https://github.com/lottie-react-native/lottie-react-native/blob/master/MIGRATION-5-TO-6.md)** when upgrading. Web builds may require **`@lottiefiles/dotlottie-react`** as documented in that README.

## Under Par stack

| Context | Library | Pointer |
|---------|---------|---------|
| **fantasy-golf (Next.js)** | `lottie-web` or a maintained React wrapper that uses it | Use in `"use client"` components; avoid running the player during SSR. Lazy-load JSON from `public/` or import static JSON. |
| **Remotion** (repo root `remotion/`) | `@remotion/lottie` | Follow `.agents/skills/remotion-best-practices/rules/lottie.md` and `delayRender` until `animationData` is ready. |
| **Future React Native app** | `lottie-react-native` | Add `pod install` on iOS; configure Metro for `.lottie` if using dotLottie (see upstream README). |

## Companion skills / rules

- **Rule:** `.cursor/rules/lottie-references/RULE.md`
- **Performance / a11y:** `.cursor/skills/fixing-motion-performance/SKILL.md`, `.cursor/skills/fixing-accessibility/SKILL.md`
- **Motion craft:** `.cursor/skills/12-principles-of-animation/SKILL.md`, `.cursor/skills/interaction-design/SKILL.md`
- **Workspace (parent `Big Projects`):** `.agents/skills/ui-animation/SKILL.md`, `.agents/skills/react-native-animations/SKILL.md`

## Export checklist (design â†’ dev)

- Prefer **shapes from vector layers** in AE so JSON stays small; raster/AI folders bloat assets.
- Test in [Lottie editor / preview](https://lottiefiles.com/) or the target player; not every AE feature is supported.
