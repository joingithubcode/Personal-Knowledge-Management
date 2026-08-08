# AGENTS.md — Personal

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds ideas about personal life and growth.

## Folder Mission

Capture and organize personal ideas early, keeping life and growth
concepts intact until they are pursued or dropped.

## Responsibilities

- Maintain one atomic note per personal idea.
- Record the concept and why it matters briefly.
- Keep notes honest about their undeveloped state.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Route developed ideas to projects or knowledge.

## Boundaries

- Ideas only; no plans or tracking here.
- No tasks, schedules, or habit tracking.
- Do not duplicate an idea that already exists.
- Do not store finished personal knowledge here.
- Keep notes self-contained and tool independent.

## Documentation Rules

- One idea per note; keep notes under 100 lines.
- Follow the repository naming conventions strictly.
- Use the templates in templates/ as the starting shape.
- Write in plain, clear language.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Point links only to existing notes.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link ideas to related idea notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Keep idea notes minimal and fast to scan.
- Refine titles and tags when an idea develops.
- Move developed ideas to projects or knowledge.
- Archive or delete ideas that go nowhere.

## Recovery Workflow

- Restore lost notes from git history.
- Recreate short idea notes from memory if needed.
- Repair broken front matter against validation.yaml.
- Merge duplicate ideas into one note.

## Common Mistakes

- Developing ideas fully inside this folder.
- Writing idea notes that are too long.
- Capturing tasks or scheduling material.
- Using invalid status values or missing YAML keys.
- Never reviewing or pruning the idea folder.
- Forgetting to register notes in the index files.
