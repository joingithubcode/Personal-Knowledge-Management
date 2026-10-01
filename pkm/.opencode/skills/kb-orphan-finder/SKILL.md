| metadata | plugin | workflow | audience | trigger |
|---|---|---|---|---|
| | personal-knowledge-management | maintenance | agents | manual+chained |

## Purpose

Finds notes that have zero inbound [[wiki-links]] from any other note — 
"orphan" notes that are disconnected from the rest of the vault and 
harder to discover.

## When to Invoke

Trigger kb-orphan-finder when:
- Doing a periodic vault health check.
- After a batch of new notes was added, to check they got connected.

Do NOT invoke when:
- The vault has fewer than a handful of notes (orphan status is not 
  meaningful yet).

## Workflow Steps

Step 1 — List every note across knowledge/, research/, projects/, and 
ideas/.

Step 2 — For each note, scan every other note's body for a [[wiki-link]] 
pointing to it.

Step 3 — Any note with zero inbound links is an orphan. List it with its 
file path.

Step 4 — For each orphan, suggest at least one existing note it could 
plausibly link to or from, based on shared topic/category.

Step 5 — Report the total orphan count and the list. Do not edit any 
file — only report findings.
