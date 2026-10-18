
## AI Agents (OpenCode)

This repo includes three OpenCode agents in `.opencode/agents/`:

| Agent | Role | Can edit files? |
|-------|------|-----------------|
| `pkm-architect` | Plans where a topic belongs, finds duplicates, proposes splits | No (read-only) |
| `pkm-writer` | Creates and updates atomic notes inside `pkm/` | Yes |
| `pkm-reviewer` | Audits notes: frontmatter, links, secrets, quality | No (read-only) |

### Commands

| Command | What it does |
|---------|--------------|
| `/plan-structure <topic>` | Architect returns a placement plan |
| `/new-note <topic>` | Writer creates a note |
| `/review-notes <focus>` | Reviewer returns a findings table and verdict |

### Usage

```bash
npm i -g opencode-ai
opencode auth login
opencode
```

Then run, for example: `/plan-structure postgres indexing notes`

### Design

- One note = one concept, max 250 lines.
- Planning and review agents are read-only (`edit: deny`) for safety.
- Agents are plain markdown files, no code required.
