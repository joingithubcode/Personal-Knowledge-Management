| metadata | plugin | workflow | audience | trigger |
|---|---|---|---|---|
| | personal-knowledge-management | authoring | agents | manual+chained |

## Purpose

Checks whether a proposed new note's topic significantly overlaps with 
an existing note's title or Purpose section, before the note is created 
— to prevent duplicate or near-duplicate notes accumulating in the vault.

## When to Invoke

Trigger kb-duplicate-detector when:
- A new note topic has been requested, before kb-scaffold-note runs.
- Doing a periodic vault cleanup to find existing duplicates.

Do NOT invoke when:
- The task is editing an existing, already-identified note.

## Workflow Steps

Step 1 — Take the proposed topic/title and the target category folder.

Step 2 — List every existing note's filename and front matter title in 
that category folder.

Step 3 — Compare the proposed topic against each existing title for 
close similarity (same core concept, not just shared keywords).

Step 4 — If a likely duplicate is found, report it: the existing file 
path and why it looks like a match. Recommend extending the existing 
note instead of creating a new one.

Step 5 — If no likely duplicate is found, report "No duplicate found — 
safe to proceed with kb-scaffold-note."

Do not create or edit any file — only report findings.
