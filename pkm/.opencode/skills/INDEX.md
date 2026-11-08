# Skills index

| Name | Purpose | Invoke when | Path |
|---|---|---|---|
| kb-cross-link-check | Verifies every [[wiki-link]] resolves; broken links are violations, missing back-links are optional suggestions. | Related Notes are written or edited, or before a commit. | pkm/.opencode/skills/kb-cross-link-check/SKILL.md |
| kb-duplicate-detector | Checks a proposed note for overlap with an existing note. | Before creating a new note. | pkm/.opencode/skills/kb-duplicate-detector/SKILL.md |
| kb-frontmatter-validate | Validates YAML front matter against AGENTS.md, STANDARDS.md, and validation.yaml. | After creating or editing a note, before registration. | pkm/.opencode/skills/kb-frontmatter-validate/SKILL.md |
| kb-injection-scan | Flags note text that reads as an instruction to an AI agent. | Reviewing imported or untrusted notes. | pkm/.opencode/skills/kb-injection-scan/SKILL.md |
| kb-orphan-finder | Finds notes with zero inbound wiki-links. | Periodic vault health checks. | pkm/.opencode/skills/kb-orphan-finder/SKILL.md |
| kb-registration-sync | Registers a note in INDEX and SUMMARY and updates the root INDEX count. | After a note is created, moved, renamed, or deleted. | pkm/.opencode/skills/kb-registration-sync/SKILL.md |
| kb-scaffold-note | Creates a new atomic note with correct front matter and sections. | Starting a new note that does not exist yet. | pkm/.opencode/skills/kb-scaffold-note/SKILL.md |
| kb-status-transition | Moves a note along the status lifecycle and records the change. | Promoting or archiving a note. | pkm/.opencode/skills/kb-status-transition/SKILL.md |
| kb-validation-pipeline | Runs validate.py and reports actionable results. | Before a commit or as a final health check. | pkm/.opencode/skills/kb-validation-pipeline/SKILL.md |
