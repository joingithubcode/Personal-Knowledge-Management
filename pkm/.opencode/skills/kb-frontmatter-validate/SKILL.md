---
name: kb-frontmatter-validate
description: Validates a note's YAML front matter against pkm/AGENTS.md, pkm/STANDARDS.md, and pkm/validation.yaml before registration or after edits.
---

## Purpose

Checks a single note's YAML front matter against the rules in pkm/AGENTS.md,
pkm/STANDARDS.md, and pkm/validation.yaml: delimiters, required and optional
keys, title form, status, dates, and tags. Reports every violation found
without modifying the file.

## When to Invoke

Trigger `kb-frontmatter-validate` when:
- A new note has just been created and needs a pre-registration check.
- An existing note's front matter was edited and needs re-validation.
- Preparing to run `kb-registration-sync` (front matter must be valid first).

Do NOT invoke when:
- The file is not a note (README.md, AGENTS.md, INDEX.md, SUMMARY.md are
  navigation files, not notes).
- No front matter exists yet and the note is still being drafted.

## Workflow Steps

Step 1 — Read the note file, pkm/validation.yaml, and the front matter and
tagging rules in pkm/STANDARDS.md (sections 3 and 6).

Step 2 — Check front matter delimiters: the file must open with `---` on
its own line and close with a second `---` on its own line, and the block
must come before the title.

Step 3 — Check required keys are present and non-empty: title, status,
created, tags.

Step 4 — Check title is a quoted string that matches the filename in
readable form and matches the validation.yaml pattern `^[a-z0-9].*$`.

Step 5 — Check status is one of: draft, active, complete, archived.

Step 6 — Check created, and updated when present, match YYYY-MM-DD.

Step 7 — Check tags is a YAML list, one label per line, with 1 to 5 tags,
2 to 5 preferred; validation.yaml sets no minimum, and STANDARDS.md line
72 says a single tag is often enough. Each tag matches
`^[a-z]+(-[a-z]+){0,2}$` (lowercase, hyphenated, at most three words, no
spaces, uppercase, or punctuation).

Step 8 — Check optional keys, when present: related is a list of note
names; source and other scalar values are plain strings.

Step 9 — Report every violation found, in this format:
- Field: <field name>
- Value found: <value>
- Problem: <what's wrong>
- Expected: <what it should be>

If no violations are found, report "Front matter valid."
