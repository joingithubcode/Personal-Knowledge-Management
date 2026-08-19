| metadata | plugin | workflow | audience | trigger |
|---|---|---|---|---|
| | personal-knowledge-management | validation | agents | manual+chained |

## Purpose

Checks that every [[wiki-link]] in a note resolves to an existing file,
and that links are symmetric — if note A links to note B, note B's
Related Notes section should link back to A.

## When to Invoke

Trigger `kb-cross-link-check` when:
- A note's Related Notes section was just written or edited.
- Doing a repository-wide health check before a commit.
- kb-frontmatter-validate has already passed on the note in question.

Do NOT invoke when:
- The note has no wiki-links at all (nothing to check).

## Workflow Steps

Step 1 — Extract every [[target]] from the note's body.

Step 2 — For each target, confirm a file named `target.md` exists
somewhere under knowledge/, research/, projects/, or ideas/. Report any
that don't resolve as broken links. Skip this check for files under
templates/ or projects/Templates/, since their links are intentional
placeholders.

Step 3 — For each resolved target, open that target note and check
whether it links back to the current note (in its own Related Notes
section or front matter `related:` list).

Step 4 — Report any one-directional link as asymmetric, and propose
adding the missing back-link.

Step 5 — Summarize: total links checked, broken links found, asymmetric
links found. Do not edit any file — only report findings, unless
explicitly told to fix them.