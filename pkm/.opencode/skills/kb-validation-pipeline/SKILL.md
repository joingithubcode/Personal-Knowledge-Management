| metadata | plugin | workflow | audience | trigger |
|---|---|---|---|---|
| | personal-knowledge-management | validation | agents | manual+chained |

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

Step 1 — Run python3 pkm/scripts/validate.py from the pkm/ directory.

Step 2 — Parse the output: total notes checked, total violations, and
the exit code.

Step 3 — If violations exist, group them by category (frontmatter,
naming, links, line_limits, counts) and list each one with its file path
and the specific rule broken.

Step 4 — If the exit code is 0, report "Clean — safe to commit."

Step 5 — If the exit code is 1, report "Not clean — do not commit" and
list the specific fixes needed, referencing which other skill
(kb-frontmatter-validate, kb-cross-link-check, or kb-registration-sync)
would resolve each violation type.

Step 6 — Do not attempt to fix violations yourself — only report
findings and route to the right skill for the actual fix.