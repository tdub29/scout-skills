---
name: scout-skills
description: "Which already-installed local skill fits this task"
---

# Scout Skills

Prefer the `/scout-skills` slash command when it is available: it spawns a dedicated Explore
subagent as a blocking gate and already carries the disk-search instructions. This skill is the
fallback for when the command is not reachable.

## Search the disk, not the context listing

**Do not scout from the skills list in your system context.** That listing is over budget and gets
truncated to bare names, so it cannot tell you what any skill does. Measured 2026-08-27: the full
`name: description` listing for the loaded roster is 588,453 chars against a 40,000-char budget at
1M context, a 14.7x overshoot, so the CLI silently drops every description.

The same skills carry their full descriptions on disk, at zero context cost. Search them with the
local ranker rather than by hand:

```
python "scripts/find-local-skill.py" "<the task, in plain words>" --top 12
```

It indexes every SKILL.md across all four local trees, ranks by term frequency over the
description with a name-match and phrase boost, prints which trees hold each hit and whether it is
INVOCABLE, and caches the parsed index so a second query is instant. Add `--json` to post-process,
`--clusters` for the full name-collision report, `--rebuild` after installing a skill. Stdlib only,
no key, no network.

Run it two or three times with different phrasings (the capability, the artifact, the verb): it
does no synonym expansion. Then read the winning SKILL.md frontmatter in full before recommending
it. If the script fails, fall back to a raw grep and say so:

```
grep -H -E '^(name|description):' "skills/"*/SKILL.md
```

## Then confirm it is invocable

`.agents/skills/` is a description source, not a loaded tree. A skill that exists only there cannot
be called with the `Skill` tool. Before recommending one, confirm the same directory name also
exists in a loaded tree:

- `.claude/skills/<name>\`
- `~/.claude/skills/<name>\`

## Collisions: return one winner

About a third of the roster shares a head noun (`design`, `resume`, `seo`, `power-bi`, `security`,
`scroll`), and many names say nothing alone (`bro`, `rfr`, `last30days`, `paste`, `seam-craft`,
`refero`). When candidates cluster, read all their descriptions and return the one that fits, plus a
clause on why the near-misses lost. Do not dump the cluster.

## Installing or building something new

For skills that are NOT installed locally, use the `find-skills` skill, which searches the skills.sh
registry. Note that it searches the registry, not these local mirrors, so run the disk grep above
first: the skill is usually already here.

At `max` extent a gap is never left to memory. Read each registry candidate's real SKILL.md (a
guessed raw URL that 404s is not a read) and judge fit. If none fits, build the skill from the best
sources online: primary docs, then papers with data, then high-signal repos, then evidenced
practitioner write-ups; three independent sources minimum, every rule cited, one fresh verifier
before install. The output is an installed skill, not a notes or knowledge file.

At `max`, **read the *MAX: install, else build* section of `~/.claude/commands/scout-skills.md` in
full before acting**; this summary is not the procedure. Two parts get skipped most:

- **The paper search is mandatory** when the domain has a literature. Health, nutrition, medicine
  and exercise go to PubMed E-utilities and Europe PMC; CS to arXiv and Semantic Scholar; the rest
  to OpenAlex. All key-free. Cite PMID, DOI or arXiv id for papers actually read.
- **A delegated build carries the procedure.** The brief names that section, and the agent reports
  the paper queries it ran and papers read versus cited. Without that report the gap is still open.

Do not report `scout-skills` unavailable. This entry exists so older prompts resolve.
