# Local tooling

Run these commands from the repository root with Python 3. The local ranker uses the standard library and sends no network requests.

## find-local-skill.py

```sh
python scripts/find-local-skill.py "browser automation" --top 8
python scripts/find-local-skill.py "options volatility"
python scripts/find-local-skill.py "landing page" --json
python scripts/find-local-skill.py --rebuild
python scripts/find-local-skill.py --clusters
python scripts/find-local-skill.py "browser automation" --clusters
python scripts/find-local-skill.py --selftest
```

The positional query accepts plain words. `--top` controls the maximum number of hits, defaulting to six. `--json` returns the query, hits, and collision groups for matching results. `--clusters` reports name collisions across the roster; a query adds matching-cluster details before the largest roster-wide clusters. `--rebuild` forces a fresh index; `--selftest` runs the built-in regression checks.

The library root is the parent of the script directory. Search roots are `skills/`, `.agents/skills`, `.claude/skills`, and `.cursor/skills` below that root, plus `~/.claude/skills`. The cache is `scripts/.find-local-skill-cache.json`. Moving your shell to another project does not change these roots.

Only the two Claude trees are marked invocable in the implementation. Cursor and library source directories remain searchable but carry a not-invocable flag. Codex discovery is not inspected. The flag does not prove a skill is loaded into your current session, and a rank is a text match rather than a certification of skill quality.

See [Getting started](../docs/GETTING_STARTED.md) to copy a complete selected bundle into the appropriate agent tree.

## build-catalog.py

```sh
python scripts/build-catalog.py
python scripts/build-catalog.py --check
```

Generate the browsing catalogue after changing bundles or provenance metadata, then check that generated output matches the current inputs. This generator does not update upstream skills or resolve missing authorship and licensing information. See [Contributing](../CONTRIBUTING.md) and [Updating](../docs/UPDATING.md).

## Optional Jev client

The portable client is bundled at `skills/scout-skills/scripts/jev.py`, so copying the complete
scout-skills bundle also copies the runtime. It uses Python 3.9+ and the standard library.
See [setup, routing and JSONL contract](../skills/scout-skills/references/jev.md).
The ranker never calls it automatically.

```sh
python skills/scout-skills/scripts/jev.py --help
python skills/scout-skills/scripts/jev.py --state "An example excerpt." --noul relevant="Does it explain testing?" --dry-run
python -m unittest discover -s tests
```

The tests mock HTTP: no keys, API spending or network access are required.
