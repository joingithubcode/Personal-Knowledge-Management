| metadata | plugin | workflow | audience | trigger |
|---|---|---|---|---|
| | personal-knowledge-management | authoring | agents | manual+chained |

## Purpose

Registers a note in all required places after it's created or moved: its
category's own README.md and INDEX.md, its category's SUMMARY.md note
count, and the root pkm/INDEX.md per-category count. Keeps every registry
in sync with what's actually on disk.

## When to Invoke

Trigger `kb-registration-sync` when:
- A new note was just created via kb-scaffold-note or otherwise.
- A note was deleted, renamed, or moved to a different category.
- kb-frontmatter-validate has already passed on the note.

Do NOT invoke when:
- The file is a navigation file itself (README.md, AGENTS.md, INDEX.md,
  SUMMARY.md), not a note.

## Workflow Steps

Step 1 — Identify the note's category folder (e.g.
knowledge/Databases/).

Step 2 — Add or remove the note's entry in that category's README.md
note list, keeping it sorted alphabetically.

Step 3 — Add or remove the note's entry in that category's INDEX.md
under "## Note registry", keeping it sorted alphabetically, format:
`note-name — one-line description`.

Step 4 — Count the actual .md note files on disk in that category
(excluding README.md, AGENTS.md, INDEX.md, SUMMARY.md) and update that
count in the category's SUMMARY.md.

Step 5 — Update the same category's note count in the root pkm/INDEX.md.

Step 6 — Report every file touched and the before/after counts. If any
count doesn't match after the update, flag it as an error rather than
silently continuing.