# Skill catalog

Browse by the task you want to do. Each bundle has one primary category for navigation; categories make no authorship or licensing claim.

824 skill bundles across 15 categories. Descriptions come from SKILL.md frontmatter and are shortened for browsing.

| Category | Bundles |
| --- | ---: |
| [Sports and fantasy](sports-and-fantasy.md) | 23 |
| [Finance and trading](finance-and-trading.md) | 69 |
| [Careers and job search](careers-and-job-search.md) | 27 |
| [Security and compliance](security-and-compliance.md) | 44 |
| [Animation and web effects](animation-and-web-effects.md) | 56 |
| [Images, video and audio](images-video-and-audio.md) | 45 |
| [Design and interfaces](design-and-interfaces.md) | 94 |
| [Data and analytics](data-and-analytics.md) | 65 |
| [Marketing and growth](marketing-and-growth.md) | 90 |
| [Agents, skills and workflows](agents-skills-and-workflows.md) | 72 |
| [Software engineering](software-engineering.md) | 77 |
| [Business, product and operations](business-product-and-operations.md) | 49 |
| [Writing and documents](writing-and-documents.md) | 35 |
| [Personal health and productivity](personal-health-and-productivity.md) | 12 |
| [Research and decisions](research-and-decisions.md) | 66 |

## Recorded origins

| Label | Bundles |
| --- | ---: |
| Imported; modification history unverified | 542 |
| Adapted from recorded sources | 114 |
| Local creation claim; unverified | 120 |
| Origin unresolved | 48 |

These labels describe recorded provenance, not license clearance or certified original authorship. Each category lists recorded upstream source links and revisions where available. See [provenance](../../PROVENANCE.md), [third-party notices](../../THIRD_PARTY_NOTICES.md), and [how to review and update skills](../UPDATING.md).

## Search or rebuild

For overlapping topics, use the local ranker from the repository root:

```sh
python scripts/find-local-skill.py "your task" --top 8
python scripts/build-catalog.py
python scripts/build-catalog.py --check
```

The generator uses skill frontmatter, provenance records and ordered lexical category rules. Results are deterministic; categories guide browsing rather than replacing a read of the skill itself.
