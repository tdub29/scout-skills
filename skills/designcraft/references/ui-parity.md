# UI and interaction parity

> **Last reviewed:** 2026-10-10 Â· **Last updated:** 2026-10-10 Â· **Change:** minor (stage re-normalized to pre-alpha by the core-workflow gate; earlier today: major, first version) Â· **Target:** Adobe InDesign 2026 (21.6, Medium Dark, macOS)

Tools, handles, snapping, nudging, modifiers, shortcuts, panels, menus, context menus and feel,
against InDesign 2026. The look was measured from the running app
(`plan/indesign/11-observed-ui.md`, local); behaviour from `plan/indesign/02-ui-ux.md`,
`05-tools.md`, `06-panels.md`, `07-dialogs.md` and `09-shortcuts.md`, and from user reports.
Overall numbers: [target-app-parity.md](target-app-parity.md).

**Dimension score: ~45% ready (estimated), 120â€“180 h.** The chrome looks like InDesign; the
basics of editing fail for too many users on Windows and Linux.

## Measured

| What | Value | How |
|---|---|---|
| InDesign 21.6 menu items matched (in scope) | 331 / 482 (69%) | script over the running app's menu dump; see target-app-parity.md |
| Menu bar | 9 menus, 49 submenus, 340 items | `MENUS` in `crates/ui-egui/src/menus.rs` |
| Commands | 446 engine (188 in menus) + 99 UI | `crates/engine/src/cmd/*`, `UI_COMMANDS` |
| Theme colours | measured hex values of Medium Dark, 4 brightness themes + High Contrast | `theme::Tokens` vs `11-observed-ui.md` Â§1 |

## Checklist

**âœ“** like InDesign Â· **~** present, differs or unreliable Â· **âœ—** missing.

| Area | InDesign 2026 | DesignCraft | Status | Evidence |
|---|---|---|---|---|
| Chrome: app bar, Control panel, Tools panel, dock, doc tabs, status bar | Medium Dark, measured sizes | measured look | âœ“ | 11-observed-ui.md |
| Properties panel and Contextual Task Bar | per selection | âœ“, task bar movable (#143) | âœ“ | |
| Selection tool: click, marquee, move, Alt-duplicate, resize handles, rotate from corners | âœ“ | âœ“ | âœ“ | |
| Direct Selection, Pen family, Pencil, Scissors | âœ“ | âœ“ | ~ | moving reference point "0" fails (#337) |
| Live corners (yellow handle) | âœ“ | âœ“ | ~ | not working for some users (#186) |
| Content grabber, frame fitting by double-click | âœ“ | âœ“ | âœ“ | |
| Smart guides, snapping to guides/grid/baseline | âœ“ | âœ“ (2,049-line `snap.rs`) | ~ | vertical smart spacing between two rectangles (#188) |
| Nudging with arrows, Shift Ã—10 | âœ“ | âœ“ | âœ“ | |
| Gridify while drawing, Gap tool, Live Distribute | âœ“ | âœ“ | âœ“ | |
| Type tool: caret, selection, double/triple click, drag-and-drop text | âœ“ | âœ“ | ~ | formatting at a caret discarded (#289); text editing complaints (#23, #174) |
| Threading: click out port, load text cursor, click frame | âœ“ | âœ— ports drawn only; no thread/unthread command; Primary Text Frame and autoflow on Place | âœ— | **alpha blocker** (#352, #194, #165, #140) |
| Copy / cut / paste objects and text, Paste Into / in Place | âœ“ | âœ“ on macOS | ~ | **failing on Windows/Linux** (#351, #348, #312, #185, #164, #201, #212) |
| Context menus (canvas, panels, rulers) | âœ“ everywhere | 9 context-menu sites, ruler units by right-click | ~ | **not opening for several users** (#238, #187, #160) |
| IME text input on the canvas | âœ“ | âœ— | âœ— | #322 |
| Font menu: search, preview, favourites, type-ahead | âœ“ | âœ“ | ~ | search field focus on macOS (#335, #86) |
| Keyboard shortcuts: InDesign defaults, editor, sets | âœ“ | âœ“ editor; defaults from 09-shortcuts.md | âœ“ | |
| Quick Apply | âœ“ | âœ“ | âœ“ | |
| Numeric fields: units, arithmetic, scrubbing | âœ“ | 21 pt spinner fields with arithmetic | âœ“ | |
| Colour fields: hex, picker from any swatch field | âœ“ | âœ“ | ~ | hex entry and picker issues (#323, #190) |
| Panels: Pages, Layers, Swatches, Color, Stroke, Character, Paragraph, Styles, Links, Effects, Text Wrap, Align, Pathfinder, Table, Index, TOC, Hyperlinks, Bookmarks, Articles, Tags, Notes, Track Changes, Object States, Buttons and Forms, Preflight, Data Merge, Library, Scripts, Glyphs, Info | âœ“ | all present | ~ | **Tabs panel missing** (#326); Navigator, Trap Presets, Animation, Timing missing; pull-down panels can't scroll on Linux (#267) |
| Dialogs: New Document, Document Setup, Preferences (all pages), Paragraph/Character/Object/Table/Cell Style Options, Export PDF, Print, Package, Find/Change | âœ“ | present | ~ | generated command dialogs fill the long tail; depth varies |
| Workspaces | Essentials, Advanced, Book, Digital Publishing, Interactive for PDF, Printing and Proofing, Typography, Touch | âœ“ named workspaces + custom | ~ | tab bar overlaps menus in Book/Advanced (#182) |
| Story Editor | âœ“ | âœ“ | ~ | style-name column, depth ruler missing |
| Undo granularity (a drag = one step) | âœ“ | âœ“ (Begin/Preview/Commit) | âœ“ | |
| Closing with unsaved changes asks | âœ“ | âœ“ (#146) | âœ“ | |
| UI scaling, System appearance | âœ“ | scaling âœ“ (#281); follows macOS light/dark âœ— (#237) | ~ | |
| Window controls, full screen | âœ“ | ~ | ~ | misaligned on macOS (#333) |

Counted 2026-10-10: 27 rows, 11 âœ“, 14 ~, 2 âœ— â†’ **67% presence**, scoring âœ“ = 1, ~ = 0.5. Ready
for real work is lower, ~45%, because threading is missing and three of the ~ rows (copy/paste,
context menus, typing at a caret) are things a layout artist does every minute, and their failures stop work.

## Remaining effort

| Work | Opus 5.5 h |
|---|---|
| Copy/paste, context menus, threading clicks, caret formatting on every platform, with control-channel regression tests | 30â€“50 |
| Canvas IME (port from VectorCraft) | 10â€“20 |
| Missing menu items (~150) and panels (Tabs, Navigator, Trap Presets) | 40â€“70 |
| Handle/tool feel fixes (#186, #188, #337), font search focus | 10â€“20 |
| Dialog depth pass against 07-dialogs.md | 30â€“40 |
| **Total** | **120â€“180** (overlaps gaps 1, 8, 16) |

## Revision history

| Date | Change | Summary |
|---|---|---|
| 2026-10-10 | minor | Threading row corrected to âœ— after checking the code (no out-port interaction, no thread command) |
| 2026-10-10 | major | Created: measured menu coverage, 27-row interaction checklist from the code and issues |
