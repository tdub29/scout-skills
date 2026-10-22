# Find a skill, then install the selected bundle

## Agent-assisted setup

Copy the [README's agent prompt](../README.md#paste-this-into-your-agent) into your agent while
working in the target project's root. It asks the agent to install the complete `scout-skills`
bundle, preserve local changes, and verify discovery. Setup is complete when the agent can read
the installed `SKILL.md`, its `references/jev.md`, and its `scripts/jev.py`, and can return a
coverage map for a sample task. A file copy alone does not verify activation.

Keep the library checkout at a reusable location and record its absolute path in your existing
project instructions or agent configuration. The installed bundle uses that checkout's ranker;
it can fall back to direct file search if the ranker is unavailable. No global slash command is
required. Use the skill's name through your agent's supported invocation mechanism, or ask:

```text
Use scout-skills at mid extent for this task. Search descriptions and bodies, read matching references, keep every contributor, and report cited coverage and gaps before proceeding.
```

## Manual setup

Clone the library and search it with Python 3. The ranker uses the standard library; it needs no API key, package install, or network connection after cloning.

```sh
git clone https://github.com/tdub29/scout-skills.git
cd scout-skills
python scripts/find-local-skill.py "browser automation" --top 8
python scripts/find-local-skill.py "review accessibility" --json
```

The script finds this checkout's `skills/` directory relative to its own location, not your current directory. It also examines configured local trees and your home Claude skills tree, so results can include skills outside this checkout. A match means the instructions were found on disk, not that an agent has loaded them.

Browse the [skill catalogue](../skills/README.md) or inspect a result's full `SKILL.md` and supporting files before using it. Check the exact bundle in [PROVENANCE.md](../PROVENANCE.md) and the [third-party notices](../THIRD_PARTY_NOTICES.md). Imported, adapted, claimed-but-unverified local, and unresolved origins are distinct; the repository's MIT license does not cover every bundle.

## Copy one complete bundle into your project

For Claude Code's project skills directory, the following example copies only the `ab-testing` bundle. Replace both absolute paths with your actual checkout and target project paths. Use a new destination; if a bundle already exists, review its differences instead of overwriting local changes.

```sh
cd /absolute/path/to/your-project
mkdir -p .claude/skills
cp -R /absolute/path/to/scout-skills/skills/ab-testing .claude/skills/ab-testing
```

Windows PowerShell equivalent:

```powershell
Set-Location 'C:\path\to\your-project'
New-Item -ItemType Directory -Force -Path '.claude/skills' | Out-Null
Copy-Item -LiteralPath 'C:\path\to\scout-skills\skills\ab-testing' -Destination '.claude/skills/ab-testing' -Recurse
```

Copy the whole selected directory, including references, scripts, templates, and notices. Copying only `SKILL.md` can break relative links. Copying instructions does not install their Python or Node dependencies, configure services, grant permissions, or resolve licensing requirements. Read the selected skill's setup instructions.

Claude Code, Codex, and Cursor have different discovery rules. The example above targets Claude Code only; use the directory and activation procedure documented by your actual agent. Do not assume every agent reads `.claude/skills`, `.agents/skills`, or `.cursor/skills` interchangeably.

For the scouting workflow itself, replace `ab-testing` with `scout-skills` in the examples.
Codex supports project skills in `.agents/skills`; Claude Code uses `.claude/skills`; Cursor
supports `.cursor/skills`. Confirm the path for your installed version and reload or start a
new session when required. See the official [Claude Code](https://code.claude.com/docs/en/skills),
[Codex](https://developers.openai.com/codex/skills), and
[Cursor](https://cursor.com/docs/context/skills) documentation. These paths describe each agent's
discovery, independently of the ranker's Claude-oriented flag below.

## Optional Jev

The complete scout-skills bundle includes a standard-library-only Jev client, so no extra
Python package installation is needed. It requires Python 3.9+. First run from the checkout:

```sh
python skills/scout-skills/scripts/jev.py --state "This excerpt explains keyboard focus." --noul contributes="Does this excerpt give an accessibility rule?" --dry-run
```

This must succeed without a key or network access. To enable live calls, follow
[Jev setup and routing](../skills/scout-skills/references/jev.md). Configure your own key locally,
check current account terms, and authorize the data that may leave your machine. Setup does
not grant API spending permission. With Jev unavailable or disabled, local search and scouting
remain usable. Jev is a separate bounded-decision step, not a hidden network mode of the ranker.

For updates, fetch and review changes in the reusable checkout, then compare and replace only
the selected complete bundle. Preserve local adaptations and notices using
[the upstream update procedure](UPDATING.md). Re-run discovery and the dry run afterward.

## Read the ranker's loaded-tree flag correctly

The current implementation marks only the checkout's `.claude/skills` and your home `~/.claude/skills` trees as invocable. It searches `skills/`, `.agents/skills`, and `.cursor/skills` as description sources but marks them not invocable. It does not inspect Codex's discovery state or verify an active agent session. Treat the flag as the script's Claude-oriented tree classification, not a universal installation check.

An installed bundle in a different project is outside this checkout's scan roots. Run the ranker from this checkout to search the library; verify loading through your target agent separately.

## Search controls and maintenance

```sh
python scripts/find-local-skill.py --rebuild
python scripts/find-local-skill.py "browser automation" --clusters
python scripts/find-local-skill.py --clusters
python scripts/find-local-skill.py --selftest
```

Run these commands from the cloned repository root. `--rebuild` refreshes the local index. `--clusters` shows name-collision groups; supplying a query also highlights clusters touching the search results, followed by the largest clusters across the roster. The cache lives at `scripts/.find-local-skill-cache.json` and is disposable.

For the complete command reference, see [scripts/README.md](../scripts/README.md). To inspect upstream changes or update one bundle while preserving local adaptations, follow [UPDATING.md](UPDATING.md). To propose a change, read [CONTRIBUTING.md](../CONTRIBUTING.md).
