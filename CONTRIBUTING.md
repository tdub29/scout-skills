# Contributing

This repository contains local search tooling and a curated collection from multiple authors. Changes to the ranker are different from changes to upstream-derived instructions. Keep pull requests scoped to the affected tooling or complete skill bundle.

## Describe where a skill comes from

Before adding or replacing a bundle, record its source URL, exact upstream revision and source path, author attribution, applicable license, and local adaptations. Preserve the whole bundle and all existing LICENSE, COPYING, NOTICE, AUTHORS, COPYRIGHT, reference, script, and template files. Check repository-level upstream notices as well as files inside the skill directory.

Update the skill's entry in [provenance.json](provenance.json), [PROVENANCE.md](PROVENANCE.md), and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) where applicable. Record only revisions and authorship you can establish. Keep unknown and unverified statuses explicit; a local folder or an import label does not prove original authorship, a pristine upstream copy, or redistribution rights. The root MIT license does not relicense third-party skills.

Existing unresolved entries are documented as unresolved, not approved examples for new imports. If required attribution or terms remain unclear, describe the gap rather than replacing them with an assumed license.

## Update one bundle at a time

Follow [the upstream update procedure](docs/UPDATING.md). Compare the complete existing bundle with the proposed upstream version, preserve local adaptations intentionally, and explain any removed files. Do not pull an upstream repository over the entire library or overwrite unrelated skills.

A useful pull request identifies the affected path, source and revision, local changes, and the validation relevant to that skill. Avoid broad formatting changes in imported content.

## Rebuild the catalogue and check the tooling

Run commands from the repository root after accepted metadata or bundle changes:

```sh
python scripts/build-catalog.py
python scripts/build-catalog.py --check
python scripts/find-local-skill.py --rebuild
python scripts/find-local-skill.py --selftest
```

The catalogue generator produces the browsing pages from the current collection. Commit regenerated output with the source change; `--check` should report no drift. These commands validate the catalogue and local search behavior, not the correctness or external dependencies of every skill. Check changed relative links and run any bundle-specific validation separately.
