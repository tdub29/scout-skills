# Find a skill, then install the selected bundle

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
