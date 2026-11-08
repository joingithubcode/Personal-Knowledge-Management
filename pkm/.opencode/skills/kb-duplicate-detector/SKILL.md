---
name: kb-duplicate-detector
description: Checks whether a proposed note overlaps an existing note before creation and recommends extending the existing note when a duplicate is likely.
---

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

Step 2 — Use grep to search note filenames and front matter `title:`
lines across the whole vault: knowledge/, research/, projects/, and
ideas/ — not just the target category folder.

Step 3 — For each close title match, read that note's `## Purpose`
section.

Step 4 — Compare the proposed topic against the candidate titles and
Purpose sections for close similarity (same core concept, not just
shared keywords).

Step 5 — If a likely duplicate is found, report it: the existing file
path and why it looks like a match. Recommend extending the existing
note instead of creating a new one.

Step 6 — If no likely duplicate is found, report "No likely duplicate
found in the titles and Purpose sections checked."

Do not create or edit any file — only report findings.
