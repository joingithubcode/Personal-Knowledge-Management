---
name: kb-cross-link-check
description: Verifies that every [[wiki-link]] in a note resolves, reporting broken links as violations and missing back-links as optional suggestions when Related Notes are written or edited.
---

## Purpose

Checks that every [[wiki-link]] in a note resolves to an existing file.
A broken link is a violation. A missing back-link is not a violation:
report it only as an optional suggestion, following STANDARDS.md line 61
("Link when genuinely relevant, not reflexively; prefer one best link
over many weak ones").

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
that don't resolve as broken links (violations). Skip this check for
files under templates/ or projects/Templates/, since their links are
intentional placeholders.

Step 3 — For each resolved target, open that target note and check
whether it links back to the current note (in its own Related Notes
section or front matter `related:` list).

Step 4 — Report any missing back-link as "suggested back-link (optional)",
citing STANDARDS.md line 61. Do not describe it as asymmetric or as a
violation, and do not require reciprocal links.

Step 5 — Summarize: total links checked, broken links found (violations),
and optional back-link suggestions. Do not edit any file — only report
findings, unless explicitly told to fix them.