---
name: kb-registration-sync
description: Registers a note in its category's INDEX and SUMMARY and updates the root INDEX count after a note is created, moved, renamed, or deleted.
---

## Purpose

Registers a note in all required places after it's created, moved,
renamed, or deleted: the affected categories' INDEX.md files, their
SUMMARY.md note counts, and the matching counts in the root pkm/INDEX.md.
Keeps every registry in sync with what's actually on disk.

## When to Invoke

Trigger `kb-registration-sync` when:
- A new note was just created via kb-scaffold-note or otherwise.
- A note was deleted, renamed, or moved to a different category. For a
  move or rename, identify both the source and destination category; for a
  delete, update the source only.
- kb-frontmatter-validate has already passed on the note.

Do NOT invoke when:
- The file is a navigation file itself (README.md, AGENTS.md, INDEX.md,
  SUMMARY.md), not a note.

## Workflow Steps

Step 1 — Identify the note's source category folder (e.g.
knowledge/Databases/).

Step 2 — Identify the destination category folder. For a created note,
the destination is the source. For a move or rename, the destination is
where the note now lives; for a rename in place, source and destination
are the same folder. For a delete, there is no destination.

Step 3 — If the destination category has no INDEX.md, stop and report it;
do not skip registration.

Step 4 — If the note exists at a destination, add or update its entry in
the destination category's INDEX.md under "## Note registry", keeping it
sorted alphabetically, format: `note-name — one-line description`.

Step 5 — If the note was deleted, or if its name or category changed
(rename or move), remove the old entry from the source category's
INDEX.md. Both a rename within one category and a move to another category
require this removal.

Step 6 — Count the actual .md note files on disk in every affected
category (excluding README.md, AGENTS.md, INDEX.md, SUMMARY.md) and
update that category's count in its SUMMARY.md.

Step 7 — Update the same affected category counts in the root
pkm/INDEX.md.

Step 8 — Report every file touched and the before/after counts. If any
count doesn't match after the update, flag it as an error rather than
silently continuing.
