| metadata | plugin | workflow | audience | trigger |
|---|---|---|---|---|
| | personal-knowledge-management | validation | agents | manual+chained |

## Purpose

Checks a single note's YAML front matter against the rules in pkm/AGENTS.md,
pkm/STANDARDS.md, and pkm/validation.yaml. Reports every violation found —
missing keys, invalid status, bad date format, empty tags — without
modifying the file.

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

Step 1 — Read the note file and pkm/validation.yaml.

Step 2 — Check front matter delimiters: file must open with `---` and
close with a second `---`.

Step 3 — Check required keys are present and non-empty: title, status,
created, tags.

Step 4 — Check status is one of: draft, active, complete, archived.

Step 5 — Check created matches YYYY-MM-DD format.

Step 6 — Check tags is a non-empty list of lowercase hyphenated words.

Step 7 — Report every violation found, in this format:
- Field: <field name>
- Value found: <value>
- Problem: <what's wrong>
- Expected: <what it should be>

If no violations are found, report "Front matter valid."
