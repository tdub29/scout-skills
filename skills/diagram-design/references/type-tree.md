# Tree / Hierarchy

**Best for:** org charts, dependency trees, taxonomy, file trees, decision breakdowns, skill trees.

## Layout conventions
- Root at top, children fan out below (or root at left, children to right).
- Nodes are small labeled rectangles (`rx=6`), Geist 12px 600 name + optional Geist Mono 9px sublabel. Width 120â€“180px, height 40â€“52px.
- **Connectors are orthogonal (elbow-style), never diagonal.** Parent drops a short vertical line, then a horizontal bus connects siblings, then each child has a short vertical drop into its top edge. 1px muted stroke.
- Leaf indicator: thinner stroke (0.8) or different fill â€” OR let terminal position do the work.
- Max depth: 4 (root + 3 tiers). Max breadth per level: 5.
- Coral on **one** node: root OR critical leaf. Not both.
- Draw connectors before nodes.

## Anti-patterns
- Tree 5+ levels deep on a single page (illegible â€” split).
- Nodes of wildly varying widths â€” pick 2 widths max.
- Diagonal connector lines.
- Skipped levels (parent connected to grandchild with no middle).
- Coral on root AND a leaf.

## Examples
- `assets/example-tree.html` â€” minimal light
- `assets/example-tree-dark.html` â€” minimal dark
- `assets/example-tree-full.html` â€” full editorial
