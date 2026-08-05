# AGENTS.md — knowledge/

Working rules for humans, editors, and AI agents working in the knowledge
folder. This folder holds permanent, organized understanding.

## Folder Mission

Store durable, self-contained knowledge notes that remain accurate and
useful for years, independent of any tool or project.

## Responsibilities

- Maintain finished, atomic knowledge notes.
- Keep every note complete, accurate, and self-contained.
- Register each note in the repository INDEX.md.
- Promote mature material from research and projects here.
- Keep the folder map in the folder README accurate.

## Boundaries

- Only finished knowledge lives here; nothing temporary.
- Never store raw sources or unprocessed material.
- Do not duplicate a concept across multiple notes.
- Never include project-specific context or vendor tooling.
- Do not reference external systems or the knowledge base.

## Documentation Rules

- One idea per note; keep notes under 100 lines.
- Follow the repository naming conventions strictly.
- Write in clear, plain language for humans and AI.
- Prefer wiki links over duplicated content.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Add updated and related keys when useful.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Point links only to existing notes in this repository.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Keep the folder README as the entry point to this folder.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note exists in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for clarity, accuracy, and self-containment.
- Keep the atomic structure when editing.
- Promote notes from research or projects when they mature.
- Update the updated date when content changes.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced notes and fix INDEX.md and SUMMARY.md.
- Merge duplicate notes into a single atomic note.

## Common Mistakes

- Storing unfinished or half-formed ideas here.
- Writing notes with overlapping or duplicate content.
- Including project-specific or tool-specific detail.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist yet.
- Forgetting to register notes in the index files.
