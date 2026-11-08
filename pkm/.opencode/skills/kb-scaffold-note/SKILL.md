---
name: kb-scaffold-note
description: Creates a new atomic note with correct front matter, filename, and section structure in the target category before content is written.
---

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
^[a-z0-9]+(-[a-z0-9]+)*\.md$, at most 60 characters.

Step 3 — Write the front matter: title (quoted, matches filename in
readable form), status: draft, created (today's date, YYYY-MM-DD), tags
(1 to 5 tags, 2 to 5 preferred; lowercase hyphenated words).

Step 4 — Write the section skeleton in order: # Title, ## Purpose,
## Context, ## Main Notes, ## References, ## Related Notes, ## Tags,
## Review History. Leave each section empty until real content is written;
do not add placeholder text, TODO markers, or boilerplate.

Step 5 — Report the created file path and remind the caller that
kb-frontmatter-validate must run next, then kb-registration-sync to
register it in INDEX.md and SUMMARY.md.