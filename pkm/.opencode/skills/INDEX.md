# Skills index

Launching OpenCode from `pkm/` exposes the `kb-*` names; launching from the repo root exposes the `pkm-*` wrappers.

| Name | Purpose | Invoke when | Path | Root wrapper |
|---|---|---|---|---|
| kb-cross-link-check | Verifies every [[wiki-link]] resolves; broken links are violations, missing back-links are optional suggestions. | Related Notes are written or edited, or before a commit. | pkm/.opencode/skills/kb-cross-link-check/SKILL.md | pkm-cross-link-check |
| kb-duplicate-detector | Checks a proposed note for overlap with an existing note. | Before creating a new note. | pkm/.opencode/skills/kb-duplicate-detector/SKILL.md | pkm-duplicate-detector |
| kb-frontmatter-validate | Validates YAML front matter against AGENTS.md, STANDARDS.md, and validation.yaml. | After creating or editing a note, before registration. | pkm/.opencode/skills/kb-frontmatter-validate/SKILL.md | pkm-frontmatter-validate |
| kb-injection-scan | Flags note text that reads as an instruction to an AI agent. | Reviewing imported or untrusted notes. | pkm/.opencode/skills/kb-injection-scan/SKILL.md | pkm-injection-scan |
| kb-orphan-finder | Finds notes with zero inbound wiki-links. | Periodic vault health checks. | pkm/.opencode/skills/kb-orphan-finder/SKILL.md | pkm-orphan-finder |
| kb-registration-sync | Registers a note in INDEX and SUMMARY and updates the root INDEX count. | After a note is created, moved, renamed, or deleted. | pkm/.opencode/skills/kb-registration-sync/SKILL.md | pkm-registration-sync |
| kb-scaffold-note | Creates a new atomic note with correct front matter and sections. | Starting a new note that does not exist yet. | pkm/.opencode/skills/kb-scaffold-note/SKILL.md | pkm-scaffold-topic |
| kb-status-transition | Moves a note along the status lifecycle and records the change. | Promoting or archiving a note. | pkm/.opencode/skills/kb-status-transition/SKILL.md | pkm-status-transition |
| kb-validation-pipeline | Runs validate.py and reports actionable results. | Before a commit or as a final health check. | pkm/.opencode/skills/kb-validation-pipeline/SKILL.md | pkm-validation-pipeline |
