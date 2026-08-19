| metadata | plugin | workflow | audience | trigger |
|---|---|---|---|---|
| | personal-knowledge-management | authoring | agents | manual+chained |

## Purpose

Creates a new, empty atomic note with correct front matter, filename, and
section structure already in place, in the correct category folder —
before any real content is written.

## When to Invoke

Trigger `kb-scaffold-note` when:
- Starting a brand new note and the file doesn't exist yet.
- The user specifies a topic and a target folder (knowledge/research/
  projects/ideas + category).

Do NOT invoke when:
- The note already exists (use direct editing instead).
- The target folder/category doesn't exist yet in the vault.

## Workflow Steps

Step 1 — Confirm the target folder exists under knowledge/, research/,
projects/, or ideas/.

Step 2 — Derive the filename: lowercase words, hyphen-separated, matching
^[a-z0-9]+(-[a-z0-9]+)*\.md$, under 60 characters.

Step 3 — Write the front matter: title (quoted, matches filename in
readable form), status: draft, created (today's date, YYYY-MM-DD), tags
(2-5 lowercase hyphenated words).

Step 4 — Write the section skeleton in order: # Title, ## Purpose,
## Context, ## Main Notes, ## References, ## Related Notes, ## Tags,
## Review History. Leave each section with a one-line placeholder
describing what belongs there — do not invent real content.

Step 5 — Report the created file path and remind the caller that
kb-registration-sync must run next to register it in INDEX.md and
SUMMARY.md.