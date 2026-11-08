---
name: kb-validation-pipeline
description: Runs pkm/scripts/validate.py and turns its output into an actionable report before a commit or as a final health check.
---

## Purpose

Runs the repository's automated validator (pkm/scripts/validate.py) and
turns its raw output into a clear, actionable report — the final check
before any commit.

## When to Invoke

Trigger kb-validation-pipeline when:
- Before committing any change to the vault.
- After kb-frontmatter-validate, kb-cross-link-check, and
  kb-registration-sync have all been run on a note, as a final
  confirmation pass.
- Doing a full repository health check on request.

Do NOT invoke when:
- No changes have been made since the last clean validator run.

## Workflow Steps

Step 1 — Run `python3 pkm/scripts/validate.py` from the repository root.

Step 2 — Parse the output: total notes checked, total violations, and
the exit code.

Step 3 — If violations exist, group them by category (frontmatter,
naming, line_limits, links, content, navigation, counts, structure) and
list each one with its file path and the specific rule broken.

Step 4 — If the exit code is 0, report "Clean — safe to commit."

Step 5 — If the exit code is 1, report "Not clean — do not commit" and
list the specific fixes needed. Name a fixing skill only where one
exists:
- frontmatter -> kb-frontmatter-validate
- links -> kb-cross-link-check
- counts -> kb-registration-sync
For naming, line_limits, content, navigation, and structure violations,
write "fix manually, cite the rule" instead of naming a skill.

Step 6 — If the exit code is 2, report the environment or config error
(for example a missing PyYAML dependency) and stop.

Step 7 — Do not attempt to fix violations yourself — only report
findings and route to the right skill, or mark as "fix manually, cite
the rule" where no skill exists.
