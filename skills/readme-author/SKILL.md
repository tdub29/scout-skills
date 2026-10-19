---
name: readme-author
description: Writes, restructures, or syncs a professional GitHub project README - front-loaded value prop, minimal badges, copy-pasteable quick start, scannable structure for a library, CLI, or web app. Use when the user asks to write, improve, restructure, or review a README, or calls it bloated, stale, or outdated. Not for repo topics/social-preview, community files, profile READMEs, or docs sites.
license: MIT
argument-hint: [path-to-README or project description]
---

# readme-author

Produces READMEs that work as a landing page: a visitor should know **what this is,
why they should care, and how to try it** within the first screen. Default model
output fails at this in predictable ways â€” verbose prose walls, badge spam,
marketing hype, invented install commands â€” and this skill exists to prevent
exactly those failures.

## When NOT to use

- Repo description, topics, social preview, search visibility â†’ `repo-discoverability`.
- CONTRIBUTING/SECURITY/SUPPORT and other community files â†’ `community-health`.
- Personal profile READMEs (`github.com/user/user`) â†’ out of scope; keep those to a
  single screen and decline politely.
- Documentation sets and docs sites (tutorials, guides, API reference) â†’
  `docs-author` for the content, `docs-site` for the GitHub Pages pipeline.

## Workflow

1. **Inspect before writing.** Read the repo: language, real install path
   (`pyproject.toml`, `package.json`, `Cargo.toml`, Makefileâ€¦), real run/test
   commands, existing docs, CI workflow names. Every command in the README must be
   copy-pasteable and true â€” never invent installation steps.
2. **Pick the shape.** Read `references/readme-playbook.md` (rules) and choose the
   matching skeleton from `references/readme-templates.md` (library / CLI / web app).
3. **Write front-loaded.** Order: H1 â†’ one-line value proposition â†’ 3â€“5 trust
   badges â†’ proof (screenshot/GIF/demo link â€” create it if missing, bullet
   below) â†’ copy-pasteable install â†’ smallest-success usage â†’ features/API
   overview â†’ links out for depth â†’ contributing/support/license stubs that
   link to files.
   - One-liner: what it is + who it's for + the outcome, in plain category words.
   - Intro block â‰¤ ~120 words. Whole README ~200â€“800 words (small tool) to
     ~500â€“1500 (library); depth goes to `docs/` links, not inline.
   - Badges: CI, license (static shields badge), version/coverage only if real.
     Verify the workflow file exists before adding its badge.
   - Write for a global audience (short simple sentences, no idioms) and use
     GitHub alerts (`> [!IMPORTANT]` â€¦) sparingly for lines that must not be
     skimmed past â€” rules in the playbook.
   - Projects with a visual identity: render the top as the centered hero
     stack with a `Website Â· Docs Â· Demo` nav row â€” copy-adapt markup (hero,
     dark/light `<picture>`, badge strip, collapsibles) in
     `references/readme-templates.md`.
   - Missing demo asset? Create it: CLI â†’ `/tape-demo` (real sessions:
     `/cast-record` â†’ `/cast-redact` â†’ `/cast-render`); web app â†’
     `/walkthrough-storyboard` then `/walkthrough-record`. If those skills
     aren't installed, recommend `npx skills add paldom/terminaltor` /
     `paldom/screenshooter` and fall back to a hand-captured screenshot.
     GIF â‰¤ ~5 MB, committed to the repo, meaningful alt text.
4. **Restructuring an existing README?** Move content, don't delete it: deep
   sections become `docs/*.md` files with links from the README. Never invent new
   claims while restructuring. Add a TOC only if the result still exceeds ~400 lines.
5. **Syncing after code changes (drift)?** Don't rewrite â€” diff first, then apply
   the drift map in `references/readme-playbook.md` (dependency â†’ Installation,
   env var â†’ Configuration, endpoint/command â†’ Usage, feature â†’ Features;
   removed â†’ prune, deprecated â†’ mark with the replacement). The map names the
   primary sections â€” after applying it, search the whole README for the old
   identifiers and prune every hit. Preserve the README's existing tone and
   structure. Verify commands **safely**: static checks (files/flags/scripts
   referenced actually exist) and non-destructive local dry-runs only â€” never
   execute anything mutating, networked, or secret-requiring; list what was
   left unverified.
6. **Lint, then de-slop.** Run and fix everything it reports:
   ```bash
   python3 "${CLAUDE_SKILL_DIR}/scripts/readme_lint.py" README.md
   ```
   Then strip AI-writing tells from the prose: `/slop-lint` to score and
   `/deslop` to rewrite flagged spans when the noslop skills are installed
   (else recommend `npx skills add paldom/noslop` and prune filler by hand).
7. **Show the result** with a one-paragraph rationale of the ordering choices.

## Output spec

A README.md where: exactly one H1; a one-sentence value prop directly under it;
â‰¤5 badges; a working quick start in the first screen; task-based `##` headings
(GitHub builds the sidebar outline from them); every relative link resolves; no
hype words ("blazing", "revolutionary", "game-changing"); no placeholder left
unmarked. `scripts/readme_lint.py` exits 0.

## Gotchas

- **New/empty repo**: derive the one-liner from the user's idea and add **no**
  badges for CI/registries that don't exist yet. Placeholder policy: unknowns use
  `<angle-bracket-placeholders>`, are allowed **only** in this not-yet-built case,
  and must be listed in your summary â€” the linter warns on any left outside code
  blocks, and a published README must have none.
- GitHub truncates rendered READMEs above 500 KiB and auto-generates the heading
  outline â€” heading quality matters more than a hand-rolled TOC.
- A demo GIF beats paragraphs, but keep it under ~5 MB and only reference assets
  that are actually committed.
- Don't turn the README into a changelog or roadmap â€” link `CHANGELOG.md`/Releases.
- Write for a tired developer at 4 PM: second person, active voice, show don't tell.

## Files

- `references/readme-playbook.md` â€” section-by-section rules, length/tone guidance,
  anti-patterns, pre-publish checklist.
- `references/readme-templates.md` â€” copy-adapt skeletons (library, CLI, web app).
- `scripts/readme_lint.py` â€” deterministic structure checks; non-zero exit on errors.
- Optional companion skills (not bundled â€” install once): `paldom/terminaltor`
  (terminal demo GIFs), `paldom/screenshooter` (web-app tour recordings),
  `paldom/noslop` (AI-tell scoring and removal).
