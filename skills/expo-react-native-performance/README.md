# Expo React Native Performance Best Practices

A comprehensive performance optimization guide for Expo React Native applications, designed for AI agents and LLMs.

## Overview

This skill contains 42 rules across 8 categories, covering everything from app startup optimization to platform-specific performance tuning. Rules are prioritized by impact to guide automated refactoring and code generation.

## Structure

```
expo-react-native-performance/
â”œâ”€â”€ SKILL.md              # Entry point with quick reference
â”œâ”€â”€ AGENTS.md             # Compiled comprehensive guide
â”œâ”€â”€ metadata.json         # Version, org, references
â”œâ”€â”€ README.md             # This file
â”œâ”€â”€ references/
â”‚   â”œâ”€â”€ _sections.md      # Category definitions
â”‚   â”œâ”€â”€ startup-*.md      # App startup rules (6)
â”‚   â”œâ”€â”€ list-*.md         # List virtualization rules (6)
â”‚   â”œâ”€â”€ rerender-*.md     # Re-render optimization rules (6)
â”‚   â”œâ”€â”€ anim-*.md         # Animation performance rules (5)
â”‚   â”œâ”€â”€ asset-*.md        # Image & asset loading rules (5)
â”‚   â”œâ”€â”€ mem-*.md          # Memory management rules (5)
â”‚   â”œâ”€â”€ async-*.md        # Async & data fetching rules (5)
â”‚   â””â”€â”€ platform-*.md     # Platform-specific rules (4)
â””â”€â”€ assets/
    â””â”€â”€ templates/
        â””â”€â”€ _template.md  # Rule template
```

## Getting Started

```bash
# Install dependencies
pnpm install

# Build AGENTS.md from references
pnpm build

# Validate skill structure
pnpm validate
```

## Creating a New Rule

1. Choose the appropriate category prefix from `references/_sections.md`
2. Create a new file: `references/{prefix}-{slug}.md`
3. Use the template from `assets/templates/_template.md`
4. Rebuild AGENTS.md: `pnpm build`

### Prefix Reference

| Category | Prefix | Impact |
|----------|--------|--------|
| App Startup & Bundle Size | `startup-` | CRITICAL |
| List Virtualization | `list-` | CRITICAL |
| Re-render Optimization | `rerender-` | HIGH |
| Animation Performance | `anim-` | HIGH |
| Image & Asset Loading | `asset-` | MEDIUM-HIGH |
| Memory Management | `mem-` | MEDIUM |
| Async & Data Fetching | `async-` | MEDIUM |
| Platform Optimizations | `platform-` | LOW-MEDIUM |

## Rule File Structure

```markdown
---
title: Rule Title Here
impact: CRITICAL|HIGH|MEDIUM-HIGH|MEDIUM|LOW-MEDIUM|LOW
impactDescription: Brief quantified impact (e.g., "2-10Ã— improvement")
tags: prefix, technique, related-concepts
---

## Rule Title Here

Brief explanation of WHY this matters (1-3 sentences).

**Incorrect (what's wrong):**

\`\`\`typescript
// Bad code example
\`\`\`

**Correct (what's right):**

\`\`\`typescript
// Good code example
\`\`\`

Reference: [Link](url)
```

## File Naming Convention

Rule files follow the pattern: `{prefix}-{description}.md`

- `prefix`: Category prefix (e.g., `startup`, `list`, `anim`)
- `description`: Kebab-case description of the rule

Examples:
- `startup-enable-hermes.md`
- `list-use-flashlist.md`
- `anim-use-native-driver.md`

## Impact Levels

| Level | Description |
|-------|-------------|
| CRITICAL | Fundamental issues affecting all users, multiplicative impact |
| HIGH | Significant impact on user experience and performance |
| MEDIUM-HIGH | Important optimizations with measurable impact |
| MEDIUM | Moderate improvements, context-dependent |
| LOW-MEDIUM | Minor optimizations for specific scenarios |
| LOW | Micro-optimizations, advanced patterns |

## Scripts

- `pnpm build` - Compile references into AGENTS.md
- `pnpm validate` - Validate skill structure and content
- `pnpm lint` - Check for common issues

## Contributing

1. Follow the rule file structure exactly
2. Include both incorrect and correct examples
3. Quantify impact where possible
4. Add references to authoritative sources
5. Run validation before submitting

## Acknowledgments

Based on official documentation and best practices from:
- [React Native Performance](https://reactnative.dev/docs/performance)
- [Expo Documentation](https://docs.expo.dev/)
- [FlashList by Shopify](https://shopify.github.io/flash-list/)
- [React Native Reanimated](https://docs.swmansion.com/react-native-reanimated/)
- [Callstack Optimization Guide](https://www.callstack.com/ebooks/the-ultimate-guide-to-react-native-optimization)
