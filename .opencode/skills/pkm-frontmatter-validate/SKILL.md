---
name: pkm-frontmatter-validate
description: Validate note frontmatter after writing, using the repo validator or a manual check
---
1. Find the repo validator: glob **/validat*.py. If found, run python3 <path> and fix every reported violation in the notes you changed.
2. If none exists, check manually that each changed note has title, category, status, sources, updated.
3. Report the exact outcome (pass or list of violations).
