# Agent Inventory

Read-only inventory of every agent definition in `pkm/.opencode/agents` and `.opencode/agents`.

| File | Name | Mode | Permission block |
|------|------|------|------------------|
| `pkm/.opencode/agents/kb-editor.md` | kb-editor | subagent | `edit: deny`, `task: deny`, `bash: deny`, `webfetch: deny` |
| `pkm/.opencode/agents/pkm-auditor.md` | pkm-auditor | subagent | `edit: deny`, `task: deny`, `bash: {"*": deny, "python3 pkm/scripts/validate.py*": allow, "python3 scripts/validate.py*": allow, "git log*": allow, "git status*": allow, "git diff*": allow, "grep*": allow}`, `webfetch: deny` |
| `pkm/.opencode/agents/kb-tech-lead.md` | kb-tech-lead | subagent | `edit: deny`, `task: deny`, `bash: deny`, `webfetch: deny` |
| `pkm/.opencode/agents/kb-skill-reviewer.md` | kb-skill-reviewer | primary | `read: allow`, `glob: allow`, `grep: allow`, `list: allow`, `edit: deny`, `task: deny`, `bash: deny`, `webfetch: deny` |
| `pkm/.opencode/agents/kb-architect.md` | kb-architect | subagent | `edit: deny`, `task: deny`, `bash: {"*": deny, "python3 pkm/scripts/validate.py*": allow, "python3 scripts/validate.py*": allow}`, `webfetch: deny` |
| `.opencode/agents/pkm-writer.md` | pkm-writer | all | `read: allow`, `glob: allow`, `grep: allow`, `edit: allow`, `webfetch: deny`, `question: deny`, `task: deny`, `bash: {"*": deny, "git status": allow, "git diff*": allow, "python3 pkm/scripts/validate.py*": allow, "python3 scripts/validate.py*": allow}`, `skill: {"*": deny, "pkm-*": allow}` |
| `.opencode/agents/pkm-proofreader.md` | pkm-proofreader | all | `read: allow`, `glob: allow`, `grep: allow`, `edit: deny`, `webfetch: deny`, `question: deny`, `task: deny`, `bash: {"*": deny}` |
| `.opencode/agents/pkm-architect.md` | pkm-architect | all | `read: allow`, `glob: allow`, `grep: allow`, `edit: deny`, `webfetch: deny`, `question: deny`, `task: deny`, `bash: {"*": deny, "git log*": allow, "git status": allow}`, `skill: {"*": deny, "pkm-*": allow}` |
| `.opencode/agents/pkm-reviewer.md` | pkm-reviewer | all | `read: allow`, `glob: allow`, `grep: allow`, `edit: deny`, `webfetch: deny`, `question: deny`, `task: deny`, `bash: {"*": deny, "git diff*": allow, "git log*": allow, "git status": allow, "python3 pkm/scripts/validate.py*": allow, "python3 scripts/validate.py*": allow}`, `skill: {"*": deny, "pkm-*": allow}` |
