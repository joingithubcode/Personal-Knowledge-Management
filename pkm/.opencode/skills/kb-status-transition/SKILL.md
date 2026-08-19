| metadata | plugin | workflow | audience | trigger |
|---|---|---|---|---|
| | personal-knowledge-management | maintenance | agents | manual+chained |

## Purpose

Changes a note's status field (draft, active, complete, archived)
correctly, and records the change in the note's Review History section
so the transition is traceable.

## When to Invoke

Trigger `kb-status-transition` when:
- A draft note has been reviewed and confirmed accurate — promote to
  active or complete.
- A note is no longer relevant but should be kept for reference —
  transition to archived.
- kb-frontmatter-validate has already confirmed the note's front matter
  is otherwise valid.

Do NOT invoke when:
- The requested target status isn't one of: draft, active, complete,
  archived — reject the request and explain the allowed values instead.
- No reason for the transition has been given — ask for one before
  proceeding, since Review History must record why.

## Workflow Steps

Step 1 — Read the note's current front matter and confirm the current
status value.

Step 2 — Confirm the requested new status is one of the four allowed
values in validation.yaml.

Step 3 — Update the `status:` field in front matter to the new value.

Step 4 — Append one line to the ## Review History section:
`- YYYY-MM-DD: Status changed from <old> to <new>. <one-line reason>.`
using today's date.

Step 5 — Report the change made. Do not alter any other section of the
note.