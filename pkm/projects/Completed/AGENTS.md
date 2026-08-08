# AGENTS.md — Completed

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds knowledge of finished projects.

## Folder Mission

Store self-contained, durable knowledge of completed projects: outcomes,
lessons, and conclusions that remain useful afterward.

## Responsibilities

- Maintain atomic notes per completed project topic.
- Record outcomes and lessons accurately.
- Extract general lessons into the knowledge folder.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Route finished projects here from Active.

## Boundaries

- Only finished projects; nothing running or planned.
- No task lists, schedules, or status tracking.
- Do not duplicate knowledge that lives in knowledge/.
- Do not store general-purpose knowledge here.
- Keep notes self-contained and tool independent.

## Documentation Rules

- One idea per note; keep notes under 100 lines.
- Follow the repository naming conventions strictly.
- Use the templates in templates/ as the starting shape.
- Write in plain, clear language.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Tag notes with the project name for grouping.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Point links only to existing notes.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link completed projects to related knowledge notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Finalize notes when a project completes.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced notes to their proper category.
- Merge duplicate project notes into one.

## Common Mistakes

- Storing running or planned project content here.
- Copying general knowledge into project notes.
- Keeping task lists as completed project records.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
