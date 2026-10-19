# Inspect upstream changes, then update one bundle

Reading upstream's latest instructions and applying an update are separate actions. This repository has no automatic upstream update checker or blanket synchronization command. Updating this checkout from its own GitHub remote also does not fetch every skill's original upstream.

## Find the original source and recorded revision

Look up the bundle name in [PROVENANCE.md](../PROVENANCE.md) and [provenance.json](../provenance.json). The JSON record uses `upstream_url`, `recorded_source`, `recorded_upstream_revision`, `revision_verified`, and `upstream_skill_path`. A path can identify `SKILL.md`; review its containing directory as the complete bundle.

For example, the `ab-testing` record links to [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) and records `skills/ab-testing/SKILL.md`. Its revision is currently unrecorded, so this record does not establish which historical upstream version the local copy came from.

A missing revision or path requires manual source identification and comparison. An unverified revision is a lead to investigate, not a trusted update baseline. Some skills have no established upstream at all; keep those cases explicit rather than choosing a similarly named repository.

## Inspect history without replacing anything

For a known GitHub repository, the following URL patterns separate a current view, file history, and a comparison:

```text
https://github.com/OWNER/REPO/tree/HEAD/PATH_TO_BUNDLE
https://github.com/OWNER/REPO/commits/HEAD/PATH_TO_BUNDLE
https://github.com/OWNER/REPO/compare/RECORDED_COMMIT...CANDIDATE_COMMIT
```

The [ab-testing history](https://github.com/coreyhaines31/marketingskills/commits/HEAD/skills/ab-testing) is a concrete source link. `HEAD` follows upstream's current default branch and can move. Use an actual candidate commit ID for a reproducible review; use the compare form only after establishing the recorded baseline. With a missing baseline, compare the current local directory directly against a chosen upstream commit and describe the uncertainty.

Fetch the upstream repository into a separate temporary directory outside this checkout. This example downloads a source for inspection only:

```sh
git clone https://github.com/coreyhaines31/marketingskills.git /tmp/marketingskills-review
git -C /tmp/marketingskills-review log -- skills/ab-testing
git diff --no-index skills/ab-testing /tmp/marketingskills-review/skills/ab-testing
```

Run the last command from the scout-skills root. A difference makes `git diff --no-index` exit nonzero; that is expected during review. Choose an unused temporary path on your system. After inspecting history, check out the selected upstream commit in that temporary clone before preparing the replacement.

## Accept the changes intentionally

Compare every file under the selected bundle, including references, scripts, templates, and notices. Identify which differences are upstream changes and which are local adaptations. Review changed setup requirements, external calls, and permissions before adopting new instructions.

Preserve the current local bundle as a review backup outside the library. Prepare the complete candidate directory in the temporary area, retaining applicable upstream copyright and license notices and the local adaptations you intend to keep. Replace only the selected `skills/NAME/` after review; remove obsolete files only when the comparison establishes that they are obsolete. Copying just `SKILL.md` or merging files blindly can leave an incomplete or inconsistent bundle.

Do not run `git pull` from an upstream repository over this collection or automatically overwrite all imported skills. A read of latest upstream content does not authorize applying it, and missing provenance is not repaired by overwriting the local copy.

## Record what changed and rebuild the catalogue

Record the actual accepted upstream commit and source path in `provenance.json`, updating verification and classification only when supported. Describe retained and new local adaptations in the per-skill provenance documentation. Update [PROVENANCE.md](../PROVENANCE.md) and [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) as needed without diluting unresolved statuses or upstream terms.

Then regenerate and check from the repository root:

```sh
python scripts/build-catalog.py
python scripts/build-catalog.py --check
python scripts/find-local-skill.py --rebuild
python scripts/find-local-skill.py --selftest
```

Review the diff for just that bundle, its provenance/notices, and generated catalogue pages. Follow any bundle-specific validation and resolve broken relative links before accepting the update.
