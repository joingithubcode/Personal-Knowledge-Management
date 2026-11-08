---
name: kb-status-transition
description: Changes a note's status along the allowed lifecycle and records the change in Review History when a note is promoted or archived.
---

## Purpose

Changes a note's status field (draft, active, complete, archived)
correctly, and records the change in the note's Review History section
so the transition is traceable.

## When to Invoke

Trigger `kb-status-transition` when:
- A draft note has been reviewed and confirmed accurate — promote to
  active.
- An active note is finished and durable — promote to complete.
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

Step 2 — Compare the current status with the requested new status against
the lifecycle in pkm/STANDARDS.md lines 80-86: draft -> active -> complete
-> archived. Allow only these transitions:
- draft -> active
- active -> complete
- complete -> archived
- any non-archived status -> archived, since archiving is the only allowed
  demotion and applies when a note is outdated or a project/inquiry ends.

Reject draft -> complete (a skipped step), any backward move, and any move
out of archived. Explain the allowed lifecycle and stop.

Step 3 — Update the `status:` field in front matter to the new value.

Step 4 — If the front matter has an `updated:` key, set it to today's
date in YYYY-MM-DD, as STANDARDS.md line 35 requires.

Step 5 — Append one line to the ## Review History section:
`- YYYY-MM-DD: Status changed from <old> to <new>. <one-line reason>.`
using today's date.

Step 6 — Report the change made. Do not alter any other section of the
note.