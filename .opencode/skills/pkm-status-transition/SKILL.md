---
name: pkm-status-transition
description: Change a note's status only along the allowed lifecycle
---
Allowed lifecycle: draft -> reviewed -> accepted -> superseded.
- Only move one step forward at a time.
- accepted requires a reviewer verdict of approve (ask the caller for it).
- Update the updated: date when status changes.
Refuse any other transition and explain why.
