# scout-skills

Local skill indexer, ranker, and curated skill library for Claude Code, Codex, and Cursor.

When a skill library grows past a few hundred entries, the in-context `name: description` list exceeds the CLI context budget and gets truncated to bare names (our full roster measured 588,453 characters against a 40,000-character budget at 1M context, a 14.7x overshoot). Once descriptions are dropped, agents guess skills by folder name alone or reach for web registries when the skill is already on disk.

`find-local-skill.py` indexes `SKILL.md` frontmatter on disk across `.agents/skills`, `.claude/skills`, and `.cursor/skills`, ranks matches by name and description coverage, flags whether each hit is invocable in a loaded tree, and reports head-noun collision clusters. It uses Python's standard library only, with no embeddings, API keys, or network calls.

## Authorship and upstream work

I maintain the local search/ranking tooling and this skill collection. The collection includes imported skills, local adaptations, and entries with unresolved origins. I do not claim to have written every skill.

- **Project tooling:** `scripts/find-local-skill.py` provides the local indexer and ranker.
- **Vendored / imported skills:** upstream-based bundles retain their authorship and license evidence. An import label does not imply a pristine upstream copy.
- **Adapted skills:** source-derived or locally modified instructions credit the upstream sources where recorded.
- **Locally created skills:** local-creation claims are labeled as unverified unless original authorship can be established.
- **Unresolved entries:** ambiguous local copies and missing source records are marked explicitly.

See the [per-skill provenance catalogue](PROVENANCE.md), [machine-readable origins](provenance.json), and [third-party notices](THIRD_PARTY_NOTICES.md).

## Usage

```bash
# Search by capability, artifact, or task in plain words
python scripts/find-local-skill.py "browser automation" --top 8
python scripts/find-local-skill.py "options volatility"
python scripts/find-local-skill.py "landing page" --json

# Inspect head-noun collision clusters across the roster
python scripts/find-local-skill.py --clusters

# Force a cache rebuild after adding or editing a skill
python scripts/find-local-skill.py --rebuild

# Run the built-in regression self-test
python scripts/find-local-skill.py --selftest
```

## How ranking works

1. **Name matches outweigh prose mentions.** A query term in the skill name scores higher than an incidental phrase buried in a long description.
2. **Presence over raw frequency.** Description terms score once on presence so verbose descriptions do not outrank concise ones.
3. **Coverage multiplier instead of flat absence penalties.** Partial query matches scale total score proportionally rather than subtracting flat penalties that sink exact-name matches.
4. **Invocability check.** Skills present only in `.agents/skills` are flagged as description-only until mirrored into an active tool tree (`.claude/skills`).

## Repository contents

- `scripts/find-local-skill.py`: Zero-dependency CLI indexer and ranker with built-in self-tests.
- `skills/scout-skills/SKILL.md`: The `scout-skills` agent skill definition that routes skill discovery through the disk ranker first.
- `skills/`: Curated collection of reusable agent skills (`SKILL.md` bundles and reference files).

## License

[MIT](LICENSE) covers project-owned tooling and original contributions. Imported and adapted skills retain their upstream terms; see [third-party notices](THIRD_PARTY_NOTICES.md).