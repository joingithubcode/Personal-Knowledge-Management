# AGENTS.md — Repository Rules

Working rules for humans, editors, and AI agents. Read this file before
creating, editing, or deleting anything in this repository. When in doubt,
follow the rules here over tool-specific behavior.

## Repository Authority

The authority order for this repository, highest first:

1. AGENTS.md
2. validation.yaml
3. STANDARDS.md
4. WORKFLOW.md
5. AI-GUIDE.md
6. Templates
7. Notes

Higher documents always override lower ones. Every AI agent MUST read
AGENTS.md before performing any operation. AGENTS.md is the single source
of truth for repository operational rules. If instructions conflict,
follow the highest-authority document.

## Repository mission

Maintain a durable, self-contained, personal knowledge repository in plain
Markdown that remains useful for a lifetime. It must be independent of any
software project, tool, or vendor, and equally readable by humans and AI.

## PKM philosophy

- Knowledge is owned by the writer, not by any tool.
- Plain Markdown and YAML are the only formats used.
- Everything is human-readable, git-friendly, and vendor independent.
- Notes capture understanding, not decoration.
- Structure is fixed; content grows over time.

## Atomic note principles

- One note holds exactly one idea.
- Each note is self-contained and understandable without context.
- Each note has a unique, meaningful, lowercase name.
- Each note carries complete YAML front matter.
- Notes connect through wiki links, never through duplicate content.
- Notes are registered in INDEX.md and SUMMARY.md.

## Folder responsibilities

- **knowledge**: permanent, organized, durable understanding.
- **research**: active inquiries, sources, and working notes.
- **projects**: knowledge tied to specific personal projects.
- **ideas**: raw, undeveloped thoughts awaiting refinement.
- Content belongs in exactly one folder; move it as it matures.

## Naming conventions

- Note files: lowercase, hyphenated words, no spaces, no uppercase.
- Example: `atomic-note-principles.md`.
- Folder names: single lowercase word.
- Titles in front matter match the filename in readable form.
- Never use dates or numbers to start a filename.

## YAML standards

- Every note starts with YAML front matter enclosed by `---`.
- Required keys: `title`, `status`, `created`, `tags`.
- Optional keys: `updated`, `related`, `source`.
- Status must be one of: draft, active, complete, archived.
- Dates use `YYYY-MM-DD`; tags are lowercase lists.
- Validate every file against validation.yaml.

## Validation workflow

- Read validation.yaml before creating or editing a file.
- Verify front matter, naming, line counts, and links.
- Check that all wiki links resolve to existing notes.
- Register new notes in INDEX.md and SUMMARY.md.
- Run validation checks before committing changes.

## Navigation rules

- SUMMARY.md is the entry point; keep it accurate.
- INDEX.md is the master index; keep every note listed.
- Every folder has a README.md describing its contents.
- Prefer wiki links over absolute paths.
- Never link to files outside this repository.

## Recovery workflow

- If a note is lost, restore from git history or the last backup.
- If structure drifts, re-align to SUMMARY.md and validation.yaml.
- If a note is misplaced, move it and update INDEX.md and SUMMARY.md.
- If front matter is broken, repair it against validation.yaml.
- If conflicts arise, resolve in favor of the repository rules.

## Expansion rules

- Add new notes inside existing folders first.
- Only create a new folder after clear, repeated need.
- A new folder needs README.md and AGENTS.md before any content.
- Register any new folder in SUMMARY.md and this file.
- Update this file and validation.yaml only when rules change.
- Never rename or remove the top-level structure.

## Common mistakes

- Writing notes with duplicate or overlapping content.
- Using spaces, uppercase, or dates in filenames.
- Missing or invalid YAML front matter.
- Forgetting to register notes in INDEX.md and SUMMARY.md.
- Linking to notes that do not exist.
- Placing content in the wrong folder.
- Treating temporary research as permanent knowledge.
- Exceeding the line limits defined in validation.yaml.

## Final rule

If a rule is unclear, favor readability, durability, and self-containment.
