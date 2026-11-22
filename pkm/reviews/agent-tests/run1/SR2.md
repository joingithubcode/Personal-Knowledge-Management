# SR2
- agent: kb-skill-reviewer
- model: opencode/deepseek-v4.1-flash-free
- date: 2026-11-15T19:13:21+05:00
- prompt: Review only .opencode/skills/kb-orphan-finder/SKILL.md. Return the full report in the required format.

## Response

[0m
> kb-skill-reviewer · deepseek-v4.1-flash-free
[0m
[0m→ [0mRead .opencode/skills/kb-orphan-finder/SKILL.md
[0m→ [0mRead validation.yaml
[0m→ [0mRead .opencode/skills/INDEX.md
[0m✱ [0mGrep "orphan|inbound|wiki-link"[90m in STANDARDS.md · 41 matches[0m
[0m✱ [0mGrep "[ \t]+$"[90m in .opencode/skills/kb-orphan-finder/SKILL.md · 8 matches[0m
[0m✱ [0mGrep "orphan|inbound back|README|INDEX"[90m in STANDARDS.md · 100 matches[0m
[0m→ [0mRead .opencode/skills/kb-cross-link-check/SKILL.md
[0m→ [0mRead STANDARDS.md[90m [offset=45, limit=35][0m
### Review report

- Files reviewed: `pkm/.opencode/skills/kb-orphan-finder/SKILL.md` (the only in-scope file). Reference only: `pkm/validation.yaml`, `pkm/STANDARDS.md`, `pkm/AGENTS.md` (Available Skills), `pkm/.opencode/skills/INDEX.md`, `pkm/.opencode/skills/kb-cross-link-check/SKILL.md` (for overlap check).
- Critical: 0
- Major: 0
- Minor: 4
- Nitpicks: 1

| # | Severity | File:line | Problem | Suggested fix |
|---|---|---|---|---|
| 1 | Minor | `pkm/.opencode/skills/kb-orphan-finder/SKILL.md:24-25` | Step 1 says "List every note across knowledge/, research/, projects/, and ideas/" but never defines what counts as a note. Those four folders also contain mandatory `README.md` and `AGENTS.md` (validation.yaml:59-61), and STANDARDS.md:53 states reserved names "are never used for notes". As written, the workflow can list, scan, and report `README.md`/`AGENTS.md` as orphans. The step is not checkable. | Add: include only files matching validation.yaml `naming.note_files` (`^[a-z0-9]+(-[a-z0-9]+)*\.md$`) and explicitly exclude `README.md` and `AGENTS.md`. |
| 2 | Minor | `pkm/.opencode/skills/kb-orphan-finder/SKILL.md:24-28` | The set of files scanned as link sources is inconsistent. Root `pkm/INDEX.md` and `pkm/SUMMARY.md` are outside the four folders, so they are never scanned, while category-level `INDEX.md`/`SUMMARY.md` inside those folders are swept in by "every note across knowledge/, research/, ...". Two files of the same class get opposite treatment, so the orphan list depends on an unstated choice. | State the source set explicitly (for example: only note files matching the naming pattern, navigation/registration files ignored) and apply it uniformly. |
| 3 | Minor | `pkm/.opencode/skills/kb-orphan-finder/SKILL.md:27-31` | The link-matching rule is undefined. validation.yaml:72 and STANDARDS.md:58 define a link as `[[note-name]]` — the filename without `.md`, case-sensitive — but Step 2 only says scan for a link "pointing to it" and Step 3 says "List it with its file path". Whether `[[atomic-note-principles]]` matches `atomic-note-principles.md`, and whether a note linking to itself counts as inbound, is left open; results are not reproducible. | Add the matching rule from STANDARDS.md:58 (strip `.md`, exact case-sensitive match on filename stem) and state that self-links do not count as inbound links. |
| 4 | Minor | `pkm/.opencode/skills/kb-orphan-finder/SKILL.md:33-34` | Step 4 asks for "at least one existing note it could plausibly link to or from". A link *from* the orphan to another note leaves the orphan with zero inbound links, so the recommended fix does not resolve the finding. The step also duplicates the suggestion duty already owned by `kb-cross-link-check` (kb-cross-link-check/SKILL.md:38-40, "suggested back-link (optional)"), without stating the relationship between the two skills. | Require suggestions that create an inbound link (another note linking *to* the orphan), verify the target exists per validation.yaml:74, and note the boundary with `kb-cross-link-check` (that skill checks a note's existing links; this one proposes missing inbound links). |
| 5 | Minor | `pkm/.opencode/skills/kb-orphan-finder/SKILL.md:19-20` | "The vault has fewer than a handful of notes" is not a checkable threshold — "a handful" has no defined value, so different runs can invoke or skip the skill at different vault sizes. | Replace with a concrete number, e.g. "fewer than 5 note files". |
| 6 | Nitpick | `pkm/.opencode/skills/kb-orphan-finder/SKILL.md:8,9,19,24,27,30,33,36` | Trailing whitespace at end of line (8 lines), and the skill name is written bare in "Trigger kb-orphan-finder when:" (line 14) while the sibling skill uses backticks (`kb-cross-link-check/SKILL.md`). Purely cosmetic. | Strip trailing spaces; wrap the skill name in backticks for consistency. |

Verdict: FAIL (0 Critical, 0 Major, 4 Minor).
