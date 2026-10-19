---
name: data-mesh-principles
description: Apply Dehghani's data mesh principles: domain ownership, data product usability, self-serve platform, federated computational governance. Triggers: data mesh, domain ownership, data product, discoverable addressable understandable trustworthy, platform paved road, federated governance, policy as code. Load the matching reference file when a specific framework is needed.
---

# data-mesh-principles

Book provenance: **Zhamak Dehghani - Data Mesh (O'Reilly Early Release, 2021)**. Load the matching `references/*.md` file when a specific framework is needed.

## When to use

Use this hub when the user's question matches any sub-framework trigger in the frontmatter description. Route to **one** reference file, read it fully, then execute that framework's process and output format.

Do not improvise a hybrid of multiple frameworks unless the user explicitly asks for a combined pass.

## Quick routing

| User cue (examples) | Reference |
| Domain ownership, source-aligned aggregate consumer-aligned | `references/domain-ownership-map.md` |
| Data product scorecard, discoverable, trustworthy, product contract | `references/data-product-usability-scorecard.md` |
| Self-serve platform, paved road, platform capabilities | `references/self-serve-platform-map.md` |
| Federated governance, policy automation, computational governance | `references/federated-governance-charter.md` |

## How to apply

1. Match the user request to a row in **Quick routing** (or the description triggers).
2. Read the corresponding file under `references/`.
3. Follow that reference's artifact, process, failure modes, and output format.
4. Return the reference's output artifact; add hub-level manipulation-risk or cross-reference notes only when the reference requires it.

## Common failure modes (hub-level)

- **Wrong reference** - loading one sub-framework when another row in Quick routing fits better.
- **Router-only answer** - summarizing the hub without loading the reference's full framework.
- **Retired atomic names** - legacy per-framework skill folders were collapsed into this hub; use `references/` only.
- **Skipping evidence** - each reference requires evidence-backed scores and explicit unknowns; do not default to parity.

## References

- [references/domain-ownership-map.md](references/domain-ownership-map.md)
- [references/data-product-usability-scorecard.md](references/data-product-usability-scorecard.md)
- [references/self-serve-platform-map.md](references/self-serve-platform-map.md)
- [references/federated-governance-charter.md](references/federated-governance-charter.md)

- **Book:** Zhamak Dehghani - Data Mesh (O'Reilly Early Release, 2021)