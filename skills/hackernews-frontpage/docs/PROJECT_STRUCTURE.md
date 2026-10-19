# Project structure

Moved verbatim from CLAUDE.md (token-load reduction).

## Directory tree

```
gstack/
â”œâ”€â”€ browse/          # /browse skill + gstack's own headless browser engine (Playwright) â€” the fallback when Aside is absent
â”‚   â”œâ”€â”€ SKILL.md.tmpl  # /browse: Aside first ({{ASIDE_SETUP}} + cookbook), $B fallback
â”‚   â”œâ”€â”€ src/         # CLI + server + commands
â”‚   â”‚   â”œâ”€â”€ commands.ts  # Command registry (single source of truth)
â”‚   â”‚   â””â”€â”€ snapshot.ts  # SNAPSHOT_FLAGS metadata array
â”‚   â”œâ”€â”€ test/        # Integration tests + fixtures
â”‚   â””â”€â”€ dist/        # Compiled binary
â”œâ”€â”€ hosts/           # Typed host configs (one per AI agent)
â”‚   â”œâ”€â”€ claude.ts    # Primary host config
â”‚   â”œâ”€â”€ claude/hooks/  # Claude Code lifecycle hooks (AUQ capture + enforcement, spawned-session directive, timeline stop, Memorable recall bridge (opt-in))
â”‚   â”œâ”€â”€ codex.ts, factory.ts, kiro.ts  # Existing hosts
â”‚   â”œâ”€â”€ opencode.ts, slate.ts, cursor.ts, openclaw.ts  # IDE hosts
â”‚   â”œâ”€â”€ hermes.ts, gbrain.ts  # Agent runtime hosts
â”‚   â””â”€â”€ index.ts     # Registry: exports all, derives Host type
â”œâ”€â”€ scripts/         # Build + DX tooling
â”‚   â”œâ”€â”€ gen-skill-docs.ts  # Template â†’ SKILL.md generator (config-driven)
â”‚   â”œâ”€â”€ gen-agents-digest.ts  # Generates the budget-capped instruction-tier digest (agents-digest/)
â”‚   â”œâ”€â”€ host-config.ts     # HostConfig interface + validator
â”‚   â”œâ”€â”€ host-config-export.ts  # Shell bridge for setup script
â”‚   â”œâ”€â”€ resolvers/   # Template resolver modules (preamble, aside = the Aside driver contract + research, browse = $B fallback setup + command reference, design, design-checklist = renders review/design-checklist.md from lib/design-catalog.ts, review, gbrain, etc.)
â”‚   â”œâ”€â”€ skill-check.ts     # Health dashboard
â”‚   â”œâ”€â”€ test-free-shards.ts  # Strict parallel free-suite runner (GSTACK_FREE_JOBS, opt-in flaky retry)
â”‚   â”œâ”€â”€ test-paid-shards.ts  # Sharded paid-tier runner (one Bun process per shard)
â”‚   â”œâ”€â”€ eval-flake-rank.ts  # Flake-telemetry dial: ranks tests by retried passes across eval runs + the free-lane ledger
â”‚   â”œâ”€â”€ sandbox-doctor.sh  # One-command cloud-sandbox fixer: makes the free suite run green
â”‚   â””â”€â”€ dev-skill.ts       # Watch mode
â”œâ”€â”€ test/            # Skill validation + eval tests
â”‚   â”œâ”€â”€ helpers/     # skill-parser.ts, session-runner.ts, llm-judge.ts, eval-store.ts, aside-available.ts (Aside self-skip probe)
â”‚   â”œâ”€â”€ fixtures/    # Ground truth JSON, planted-bug fixtures, eval baselines, impeccable engine captures (impeccable-*.json, the dumped slop page, fake-impeccable.ts shim)
â”‚   â”œâ”€â”€ aside-driver.test.ts      # Tier 1: pins the {{ASIDE_SETUP}} contract sentences + the fallback hand-off
â”‚   â”œâ”€â”€ aside-render.test.ts      # Tier 1 pins + fake-executable runs on both engines + a live Aside render (self-skips without Aside)
â”‚   â”œâ”€â”€ gstack-render-cli.test.ts # Tier 1: bin/gstack-render.ts argv guards + output contract against a fake daemon
â”‚   â”œâ”€â”€ skill-validation.test.ts  # Tier 1: static validation (free, <1s)
â”‚   â”œâ”€â”€ gen-skill-docs.test.ts    # Tier 1: generator quality (free, <1s)
â”‚   â”œâ”€â”€ setup-*.test.ts, relink.test.ts, hook-scripts.test.ts  # Tier 1: setup linker ownership, retired-skill prune, browser hint, rebuild check + Chromium bootstrap (anchor-sliced from setup), gstack-relink, PreToolUse hooks (free)
â”‚   â”œâ”€â”€ skill-llm-eval.test.ts   # Tier 3: LLM-as-judge (~$0.15/run)
â”‚   â””â”€â”€ skill-e2e-*.test.ts       # Tier 2: E2E via claude -p (~$3.85/run, split by category)
â”œâ”€â”€ qa-only/         # /qa-only skill (report-only QA, no fixes)
â”œâ”€â”€ plan-design-review/  # /plan-design-review skill (report-only design audit)
â”œâ”€â”€ design-review/    # /design-review skill (design audit + fix loop)
â”œâ”€â”€ ship/            # Ship workflow skill
â”œâ”€â”€ review/          # PR review skill (checklist.md is hand-written; design-checklist.md is GENERATED from lib/design-catalog.ts)
â”œâ”€â”€ plan-ceo-review/ # /plan-ceo-review skill
â”œâ”€â”€ plan-eng-review/ # /plan-eng-review skill
â”œâ”€â”€ autoplan/        # /autoplan skill (auto-review pipeline: CEO â†’ design â†’ DX â†’ eng, eng always last)
â”œâ”€â”€ benchmark/       # /benchmark skill (performance regression detection)
â”œâ”€â”€ canary/          # /canary skill (post-deploy monitoring loop)
â”œâ”€â”€ codex/           # /codex skill (multi-AI second opinion via OpenAI Codex CLI)
â”œâ”€â”€ land-and-deploy/ # /land-and-deploy skill (merge â†’ deploy â†’ canary verify)
â”œâ”€â”€ office-hours/    # /office-hours skill (YC Office Hours â€” startup diagnostic + builder brainstorm)
â”œâ”€â”€ investigate/     # /investigate skill (systematic root-cause debugging)
â”œâ”€â”€ spec/            # /spec skill (five-phase spec â†’ GitHub issue, optional agent spawn, /ship auto-closes)
â”œâ”€â”€ retro/           # Retrospective skill (includes /retro global cross-project mode)
â”œâ”€â”€ careful/         # /careful skill; bin/check-careful.sh (PreToolUse destructive-command hook) + bin/hook-extract.sh (shared hook helpers: payload extraction, deny JSON, gstack_hook_state_root)
â”œâ”€â”€ freeze/          # /freeze skill; bin/check-freeze.sh (PreToolUse edit-boundary hook; sources careful/bin/hook-extract.sh, fails closed)
â”œâ”€â”€ guard/, unfreeze/  # /guard (careful + freeze in one), /unfreeze
â”œâ”€â”€ gstack-upgrade/  # /gstack-upgrade skill + migrations/ (run after ./setup during an upgrade)
â”œâ”€â”€ bin/             # CLI utilities (gstack-render.ts = render a local HTML file through Aside or the engine, gstack-design-detect.ts = probe/scan through a user-installed impeccable engine; gstack-design-md.ts = open DESIGN.md check/convert/tokens/mark; gstack-repo-mode, gstack-slug, gstack-config, gstack-wtree, gstack-evidence, gstack-issue-guard, gstack-relink, gstack-memorable, etc.)
â”œâ”€â”€ document-release/ # /document-release skill (post-ship doc updates + Diataxis coverage map)
â”œâ”€â”€ document-generate/ # /document-generate skill (Diataxis doc generator: tutorial/how-to/reference/explanation)
â”œâ”€â”€ cso/             # /cso skill (OWASP Top 10 + STRIDE security audit)
â”œâ”€â”€ design-consultation/ # /design-consultation skill (design system from scratch)
â”œâ”€â”€ design-shotgun/  # /design-shotgun skill (visual design exploration)
â”œâ”€â”€ open-gstack-browser/  # /open-gstack-browser skill (launch GStack Browser)
â”œâ”€â”€ connect-chrome/  # symlink â†’ open-gstack-browser (backwards compat)
â”œâ”€â”€ setup-browser-cookies/, pair-agent/, skillify/  # Fallback-engine skills (cookie import, shared-browser tunnel, codify a /scrape)
â”œâ”€â”€ qa/, qa-only/, scrape/  # Browser skills (with design-review/, canary/, benchmark/) â€” Aside first via {{ASIDE_SETUP}}, $B when Aside is absent
â”œâ”€â”€ make-pdf/        # /make-pdf skill + compiled `pdf` binary (embeds lib/aside-render.ts); test/ = unit tests (cli-exit-codes, setup-smoke, render) + e2e/*-gate.test.ts on whichever engine resolves
â”œâ”€â”€ diagram/         # /diagram skill (mermaid â†’ SVG/PNG/.excalidraw through bin/gstack-render.ts + lib/diagram-render)
â”œâ”€â”€ design/          # Design binary CLI (GPT Image API)
â”‚   â”œâ”€â”€ src/         # CLI + commands (generate, variants, compare, serve, etc.)
â”‚   â”œâ”€â”€ test/        # Integration tests
â”‚   â””â”€â”€ dist/        # Compiled binary
â”œâ”€â”€ agents-digest/   # Committed 2KB instruction-tier rules digest (gstack-AGENTS.md) for rules-reading hosts
â”œâ”€â”€ extension/       # Chrome extension (side panel + activity feed + CSS inspector)
â”œâ”€â”€ lib/             # Shared libraries (aside-render.ts = local-HTML rendering, Aside first, engine fallback; design-catalog.ts = the typed design anti-pattern catalog every design skill renders from; design-detect-contract.ts = detector sentinel vocabulary; design-md.ts = open DESIGN.md reader/writer; dom-dump-script.ts + generated dom-dump.js = rendered-DOM dump for the detector; review-evidence.ts = review-start receipt binding and computed freshness; frontend-scope.ts; claude-bin.ts, error-handling.ts, worktree.ts, egress-receipt.ts, context-bill.ts, redact-engine.ts, tracker-guard.ts, version-source.ts, code-intelligence/)
â”‚   â””â”€â”€ diagram-render/  # Vendored mermaid + excalidraw runtimes, built into one offline bundle the renderer loads
â”œâ”€â”€ patches/         # bun `patchedDependencies` patches (playwright-core windowsHide)
â”œâ”€â”€ docs/designs/    # Design documents (incl. IMPECCABLE_INTEROP.md = the design detector / catalog / open DESIGN.md record, and fork-port-residual-2026-09/ evaluation evidence)
â”œâ”€â”€ setup-deploy/    # /setup-deploy skill (one-time deploy config)
â”œâ”€â”€ .github/         # CI workflows + shared composite actions (.github/actions/) + Docker image (claude CLI pinned)
â”‚   â”œâ”€â”€ workflows/   # evals.yml (E2E on Ubicloud), quality-gate.yml (secret scan), dependency-review.yml, osv-scanner.yml, skill-docs.yml, actionlint.yml, and 8 more (windows, periodic evals, release gates, ci-image)
â”‚   â””â”€â”€ docker/      # Dockerfile.ci (pre-baked toolchain + Playwright/Chromium)
â”œâ”€â”€ contrib/         # Contributor-only tools (never installed for users)
â”‚   â””â”€â”€ add-host/    # /gstack-contrib-add-host skill
â”œâ”€â”€ setup            # One-time setup: build the browse, design + make-pdf binaries (rebuilds when any is missing or browse/make-pdf/design/lib sources changed) + best-effort Chromium bootstrap + link skills + prune retired-skill renders (both ownership-gated)
â”œâ”€â”€ SKILL.md         # Generated from SKILL.md.tmpl (don't edit directly)
â”œâ”€â”€ SKILL.md.tmpl    # Template: edit this, run gen:skill-docs
â”œâ”€â”€ ETHOS.md         # Builder philosophy (Boil the Ocean, Search Before Building)
â”œâ”€â”€ NOTICE.md        # Third-party notices: material derived from impeccable and the DESIGN.md spec (both Apache-2.0)
â”œâ”€â”€ licenses/        # Verbatim license texts for the notices above (Apache-2.0.txt)
â””â”€â”€ package.json     # Build scripts for browse
```
