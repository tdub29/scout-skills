# Slate Host Integration â€” Research & Design Doc

**Date:** 2026-04-02
**Branch:** garrytan/slate-agent-support
**Status:** Research complete, blocked on host config refactor
**Supersedes:** None

## What is Slate

Slate is a proprietary coding agent CLI from Random Labs.
Install: `npm i -g @randomlabs/slate` or `brew install anthropic/tap/slate`.
License: Proprietary. 85MB compiled Bun binary (arm64/x64, darwin/linux/windows).
npm package: `@randomlabs/slate@1.0.25` (thin 8.8KB launcher + platform-specific optional deps).

Multi-model: dynamically selects Claude Sonnet/Opus/Haiku, plus other models.
Built for "swarm orchestration" with extended multi-hour sessions.

## Slate is an OpenCode fork

**Confirmed via binary strings analysis** of the 85MB Mach-O arm64 binary:

- Internal name: `name: "opencode"` (literal string in binary)
- All `OPENCODE_*` env vars present alongside `SLATE_*` equivalents
- Shares OpenCode's tool/skill architecture, LSP integration, terminal management
- Own branding, API endpoints (`api.randomlabs.ai`, `agent-worker-prod.randomlabs.workers.dev`), and config paths

This matters for integration: OpenCode conventions mostly apply, but Slate adds
its own paths and env vars on top.

## Skill Discovery (confirmed from binary)

Slate scans ALL four directory families for skills. Error messages in binary confirm:

```
"failed .slate directory scan for skills"
"failed .claude directory scan for skills"
"failed .agents directory scan for skills"
"failed .opencode directory scan for skills"
```

**Discovery paths (priority order from Slate docs):**

1. `.slate/skills/<name>/SKILL.md` â€” project-level, highest priority
2. `~/.slate/skills/<name>/SKILL.md` â€” global
3. `.opencode/skills/`, `.agents/skills/` â€” compatibility fallback
4. `.claude/skills/` â€” Claude Code compatibility fallback (lowest)
5. Custom paths via `slate.json`

**Glob patterns:** `**/SKILL.md` and `{skill,skills}/**/SKILL.md`

**Commands:** Same directory structure but under `commands/` subdirs:
`/.slate/commands/`, `/.claude/commands/`, `/.agents/commands/`, `/.opencode/commands/`

**Skill frontmatter:** YAML with `name` and `description` fields (per Slate docs).
No documented length limits on either field.

## Project Instructions

Slate reads both `CLAUDE.md` and `AGENTS.md` for project instructions.
Both literal strings confirmed in binary. No changes needed to existing
gstack projects... CLAUDE.md works as-is.

## Configuration

**Config file:** `slate.json` / `slate.jsonc` (NOT opencode.json)

**Config options (from Slate docs):**
- `privacy` (boolean) â€” disables telemetry/logging
- Permissions: `allow`, `ask`, `deny` per tool (`read`, `edit`, `bash`, `grep`, `webfetch`, `websearch`, `*`)
- Model slots: `models.main`, `models.subagent`, `models.search`, `models.reasoning`
- MCP servers: local or remote with custom commands and headers
- Custom commands: `/commands` with templates

The setup script should NOT create `slate.json`. Users configure their own permissions.

## CLI Flags (Headless Mode)

```
--stream-json / --output-format stream-json  â€” JSONL output, "compatible with Anthropic Claude Code SDK"
--dangerously-skip-permissions               â€” bypass all permission checks (CI/automation)
--input-format stream-json                   â€” programmatic input
-q                                           â€” non-interactive mode
-w <dir>                                     â€” workspace directory
--output-format text                         â€” plain text output (default)
```

**Stream-JSON format:** Slate docs claim "compatible with Anthropic Claude Code SDK."
Not yet empirically verified. Given OpenCode heritage, likely matches Claude Code's
NDJSON event schema (type: "assistant", type: "tool_result", type: "result").

**Need to verify:** Run `slate -q "hello" --stream-json` with valid credits and
capture actual JSONL events before building the session runner parser.

## Environment Variables (from binary strings)

### Slate-specific
```
SLATE_API_KEY                              â€” API key
SLATE_AGENT                                â€” agent selection
SLATE_AUTO_SHARE                           â€” auto-share setting
SLATE_CLIENT                               â€” client identifier
SLATE_CONFIG                               â€” config override
SLATE_CONFIG_CONTENT                       â€” inline config
SLATE_CONFIG_DIR                           â€” config directory
SLATE_DANGEROUSLY_SKIP_PERMISSIONS         â€” bypass permissions
SLATE_DIR                                  â€” data directory override
SLATE_DISABLE_AUTOUPDATE                   â€” disable auto-update
SLATE_DISABLE_CLAUDE_CODE                  â€” disable Claude Code integration entirely
SLATE_DISABLE_CLAUDE_CODE_PROMPT           â€” disable Claude Code prompt loading
SLATE_DISABLE_CLAUDE_CODE_SKILLS           â€” disable .claude/skills/ loading
SLATE_DISABLE_DEFAULT_PLUGINS              â€” disable default plugins
SLATE_DISABLE_FILETIME_CHECK               â€” disable file time checks
SLATE_DISABLE_LSP_DOWNLOAD                 â€” disable LSP auto-download
SLATE_DISABLE_MODELS_FETCH                 â€” disable models config fetch
SLATE_DISABLE_PROJECT_CONFIG               â€” disable project-level config
SLATE_DISABLE_PRUNE                        â€” disable session pruning
SLATE_DISABLE_TERMINAL_TITLE               â€” disable terminal title updates
SLATE_ENABLE_EXA                           â€” enable Exa search
SLATE_ENABLE_EXPERIMENTAL_MODELS           â€” enable experimental models
SLATE_EXPERIMENTAL                         â€” enable experimental features
SLATE_EXPERIMENTAL_BASH_DEFAULT_TIMEOUT_MS â€” bash timeout override
SLATE_EXPERIMENTAL_DISABLE_COPY_ON_SELECT  â€” disable copy on select
SLATE_EXPERIMENTAL_DISABLE_FILEWATCHER     â€” disable file watcher
SLATE_EXPERIMENTAL_EXA                     â€” Exa search (alt flag)
SLATE_EXPERIMENTAL_FILEWATCHER             â€” enable file watcher
SLATE_EXPERIMENTAL_ICON_DISCOVERY          â€” icon discovery
SLATE_EXPERIMENTAL_LSP_TOOL               â€” LSP tool
SLATE_EXPERIMENTAL_LSP_TY                 â€” LSP type checking
SLATE_EXPERIMENTAL_MARKDOWN               â€” markdown mode
SLATE_EXPERIMENTAL_OUTPUT_TOKEN_MAX       â€” output token limit
SLATE_EXPERIMENTAL_OXFMT                  â€” oxfmt integration
SLATE_EXPERIMENTAL_PLAN_MODE              â€” plan mode
SLATE_FAKE_VCS                            â€” fake VCS for testing
SLATE_GIT_BASH_PATH                       â€” git bash path (Windows)
SLATE_MODELS_URL                          â€” models config URL
SLATE_PERMISSION                          â€” permission override
SLATE_SERVER_PASSWORD                     â€” server auth
SLATE_SERVER_USERNAME                     â€” server auth
SLATE_TELEMETRY_DISABLED                  â€” disable telemetry
SLATE_TEST_HOME                           â€” test home directory
SLATE_TOKEN_DIR                           â€” token storage directory
```

### OpenCode legacy (still functional)
```
OPENCODE_DISABLE_LSP_DOWNLOAD
OPENCODE_EXPERIMENTAL_DISABLE_FILEWATCHER
OPENCODE_EXPERIMENTAL_FILEWATCHER
OPENCODE_EXPERIMENTAL_ICON_DISCOVERY
OPENCODE_EXPERIMENTAL_LSP_TY
OPENCODE_EXPERIMENTAL_OXFMT
OPENCODE_FAKE_VCS
OPENCODE_GIT_BASH_PATH
OPENCODE_LIBC
OPENCODE_TERMINAL
```

### Critical env vars for gstack integration

**`SLATE_DISABLE_CLAUDE_CODE_SKILLS`** â€” When set, `.claude/skills/` loading is disabled.
This makes publishing to `.slate/skills/` load-bearing, not just an optimization.
Without native `.slate/` publishing, gstack skills vanish when this flag is set.

**`SLATE_TEST_HOME`** â€” Useful for E2E tests. Can redirect Slate's home directory
to an isolated temp directory, similar to how Codex tests use a temp HOME.

**`SLATE_DANGEROUSLY_SKIP_PERMISSIONS`** â€” Required for headless E2E tests.

## Model References (from binary)

```
anthropic/claude-sonnet-4.6
anthropic/claude-opus-4
anthropic/claude-haiku-4
anthropic/slate              â€” Slate's own model routing
openai/gpt-5.3-codex
google/nano-banana
randomlabs/fast-default-alpha
```

## API Endpoints (from binary)

```
https://api.randomlabs.ai                          â€” main API
https://api.randomlabs.ai/exaproxy                 â€” Exa search proxy
https://agent-worker-prod.randomlabs.workers.dev   â€” production worker
https://agent-worker-dev.randomlabs.workers.dev    â€” dev worker
https://dashboard.randomlabs.ai                    â€” dashboard
https://docs.randomlabs.ai                         â€” documentation
https://randomlabs.ai/config.json                  â€” remote config
```

Brew tap: `anthropic/tap/slate` (notable: under Anthropic's tap, not Random Labs)

## npm Package Structure

```
@randomlabs/slate (8.8 kB, thin launcher)
â”œâ”€â”€ bin/slate           â€” Node.js launcher (finds platform binary in node_modules)
â”œâ”€â”€ bin/slate1          â€” Bun launcher (same logic, import.meta.filename)
â”œâ”€â”€ postinstall.mjs     â€” Verifies platform binary exists, symlinks if needed
â””â”€â”€ package.json        â€” Declares optionalDependencies for all platforms

Platform packages (85MB each):
â”œâ”€â”€ @randomlabs/slate-darwin-arm64
â”œâ”€â”€ @randomlabs/slate-darwin-x64
â”œâ”€â”€ @randomlabs/slate-linux-arm64
â”œâ”€â”€ @randomlabs/slate-linux-x64
â”œâ”€â”€ @randomlabs/slate-linux-x64-musl
â”œâ”€â”€ @randomlabs/slate-linux-arm64-musl
â”œâ”€â”€ @randomlabs/slate-linux-x64-baseline
â”œâ”€â”€ @randomlabs/slate-linux-x64-baseline-musl
â”œâ”€â”€ @randomlabs/slate-darwin-x64-baseline
â”œâ”€â”€ @randomlabs/slate-windows-x64
â””â”€â”€ @randomlabs/slate-windows-x64-baseline
```

Binary override: `SLATE_BIN_PATH` env var skips all discovery, runs the specified binary directly.

## What Already Works Today

gstack skills already work in Slate via the `.claude/skills/` fallback path.
No changes needed for basic functionality. Users who install gstack for Claude Code
and also use Slate will find their skills available in both agents.

## What First-Class Support Adds

1. **Reliability** â€” `.slate/skills/` is Slate's highest-priority path. Immune to
   `SLATE_DISABLE_CLAUDE_CODE_SKILLS`.
2. **Optimized frontmatter** â€” Strip Claude-specific fields (allowed-tools, hooks, version)
   that Slate doesn't use. Keep only `name` and `description`.
3. **Setup script** â€” Auto-detect `slate` binary, install skills to `~/.slate/skills/`.
4. **E2E tests** â€” Verify skills work when invoked by Slate directly.

## Blocked On: Host Config Refactor

Codex's outside voice review identified that adding Slate as a 4th host (after Claude,
Codex, Factory) is "host explosion for a path alias." The current architecture has:

- Hard-coded host names in `type Host = 'claude' | 'codex' | 'factory'`
- Per-host branches in `transformFrontmatter()` with near-duplicate logic
- Per-host config in `EXTERNAL_HOST_CONFIG` with similar patterns
- Per-host functions in the setup script (`create_codex_runtime_root`, `link_codex_skill_dirs`)
- Host names duplicated in `bin/gstack-platform-detect` (since deleted â€” host
  detection now lives in the `hosts/` registry, exported to shell via
  `scripts/host-config-export.ts`), `bin/gstack-uninstall`, `bin/dev-setup`

Adding Slate means copying all of these patterns again. A refactor to make hosts
data-driven (config objects instead of if/else branches) would make Slate integration
trivial AND make future hosts (any new OpenCode fork, any new agent) zero-effort.

### Missing from the plan (identified by Codex)

- `lib/worktree.ts` only copies `.agents/`, not `.slate/` â€” E2E tests in worktrees won't
  have Slate skills
- `bin/gstack-uninstall` doesn't know about `.slate/`
- `bin/dev-setup` doesn't wire `.slate/` for contributor dev mode
- `bin/gstack-platform-detect` doesn't detect Slate (obsolete: the bin was
  deleted; host detection is now the `hosts/` registry via
  `scripts/host-config-export.ts` â€” `hosts/slate.ts` is where Slate lives)
- E2E tests should set `SLATE_DISABLE_CLAUDE_CODE_SKILLS=1` to prove `.slate/` path
  actually works (not just falling back to `.claude/`)

## Session Runner Design (for later)

When the JSONL format is verified, the session runner should:

- Spawn: `slate -q "<prompt>" --stream-json --dangerously-skip-permissions -w <dir>`
- Parse: Claude Code SDK-compatible NDJSON (assumed, needs verification)
- Skills: Install to `.slate/skills/` in test fixture (not `.claude/skills/`)
- Auth: Use `SLATE_API_KEY` or existing `~/.slate/` credentials
- Isolation: Use `SLATE_TEST_HOME` for home directory isolation
- Timeout: 300s default (same as Codex)

```typescript
export interface SlateResult {
  output: string;
  toolCalls: string[];
  tokens: number;
  exitCode: number;
  durationMs: number;
  sessionId: string | null;
  rawLines: string[];
  stderr: string;
}
```

## Docs References

- Slate docs: https://docs.randomlabs.ai
- Quickstart: https://docs.randomlabs.ai/en/getting-started/quickstart
- Skills: https://docs.randomlabs.ai/en/using-slate/skills
- Configuration: https://docs.randomlabs.ai/en/using-slate/configuration
- Hotkeys: https://docs.randomlabs.ai/en/using-slate/hotkey_reference
