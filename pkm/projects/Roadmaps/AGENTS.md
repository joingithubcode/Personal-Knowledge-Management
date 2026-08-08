# AGENTS.md — Roadmaps

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds knowledge about project direction.

## Folder Mission

Store self-contained, durable records of project direction: goals,
phases, and the reasoning behind future work.

## Responsibilities

- Maintain atomic notes per roadmap topic.
- Record goals, phases, and sequencing clearly.
- Preserve the reasoning behind each direction.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Link roadmaps to planning and decision notes.

## Boundaries

- Direction only; no day-to-day task tracking.
- No schedules or status reports.
- Do not duplicate planning or decision content.
- Do not store finished project knowledge here.
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
- Link roadmaps to related project notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update roadmaps as direction evolves.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced notes to their proper category.
- Merge duplicate roadmap notes into one.

## Common Mistakes

- Tracking tasks or schedules in roadmaps.
- Copying planning or decision content here.
- Keeping roadmaps for finished projects.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
