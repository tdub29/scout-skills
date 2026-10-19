# License check

Run this before adapting. Skill defaults to **stop** on unclear or restrictive licenses â€” don't proceed without explicit the user approval on red cases.

## Policy

| License | Action | Why |
|---|---|---|
| **MIT** | âœ… Proceed | Permissive. Requires only attribution + license notice. |
| **Apache 2.0** | âœ… Proceed | Permissive. Requires attribution + NOTICE file. |
| **BSD (2-clause, 3-clause)** | âœ… Proceed | Permissive. Requires attribution. |
| **ISC** | âœ… Proceed | Equivalent to MIT. |
| **CC0 / Public Domain** | âœ… Proceed | No attribution required (but include anyway for credit). |
| **Unlicense** | âœ… Proceed | Public domain equivalent. |
| **MPL 2.0** | ðŸŸ¡ Warn | File-level reciprocity â€” modified MPL files must stay MPL. Adapt sparingly; consider rewriting from scratch instead of copying. |
| **LGPL** | ðŸŸ¡ Warn | Library-linking exception, but skill files would be derivative. Usually rewrite from scratch is cleaner. |
| **GPL 2.0 / 3.0** | âŒ Stop | Strong copyleft â€” adaptation creates a derivative work that must also be GPL. Stops your repo from being your-license-of-choice. Surface to the user. |
| **AGPL** | âŒ Stop | Even stronger â€” network-use clause triggers. |
| **Custom / proprietary** | âŒ Stop | No legal basis to copy. |
| **No LICENSE file** | ðŸŸ¡ Warn | Default copyright = no rights. Don't copy. Ask author OR rewrite from scratch using only the *ideas* (not the text). |
| **Unclear / conflicting** | ðŸŸ¡ Warn | Surface to the user for a call. |

## Detection script

```bash
# In the source repo
curl -s "https://api.github.com/repos/<owner>/<repo>/license" | jq -r .license.spdx_id
```

Or read the LICENSE file directly:

```bash
cat <repo>/LICENSE | head -5
```

Standard SPDX identifiers: `MIT`, `Apache-2.0`, `BSD-2-Clause`, `BSD-3-Clause`, `ISC`, `MPL-2.0`, `LGPL-3.0`, `GPL-2.0`, `GPL-3.0`, `AGPL-3.0`, `CC0-1.0`, `Unlicense`.

## Required artifacts per license

**MIT / BSD / ISC**: copy the LICENSE text into `references/attribution.md` (or as a separate `LICENSE-<source-name>` file in the skill dir). Include the copyright line verbatim.

**Apache 2.0**: same as MIT + copy any `NOTICE` file from the source.

**CC0 / Unlicense / Public Domain**: attribution not required, but include in `attribution.md` for credit.

**MPL / LGPL / GPL**: don't proceed without the user's explicit call.

## When the source has no license

This is the most common case for skills on personal GitHub repos. Treat it as âŒ red:
- Default copyright applies â€” you have *no* right to copy or redistribute
- Options:
  1. **Open an issue / PR** asking the author to add a permissive license
  2. **Email / DM** the author and ask permission, save the response
  3. **Rewrite from scratch** using only the *ideas* (mechanics, concepts) â€” not the text. Then it's a fresh independent work that happens to be similar. Document this clearly in `attribution.md` so it's not confused with a port.

## Edge case: skills you wrote yourself in another context

If the source is YOUR OWN code in another repo of yours (e.g., personal note â†’ adapt for a sibling plugin), license doesn't apply. Skip this step and just attribute for traceability.
