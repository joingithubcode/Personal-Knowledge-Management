# AGENTS.md — Planning

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds knowledge for projects being planned.

## Folder Mission

Store self-contained, durable knowledge that shapes projects before they
start: goals, scope, and the rationale behind plans.

## Responsibilities

- Maintain atomic notes per planning topic.
- Record goals, scope, and approach clearly.
- Preserve the reasoning behind each plan.
- Register every note in the repository INDEX.md.
- Hand planned projects to Active when they start.

## Boundaries

- Only pre-execution thinking; nothing running yet.
- No task lists, schedules, or status tracking.
- Do not duplicate roadmap or decision content.
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
- Link planning notes to related project notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update plans as the approach evolves.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced notes to their proper category.
- Merge duplicate planning notes into one.

## Common Mistakes

- Storing task lists or schedules in planning notes.
- Keeping planning notes after the project starts.
- Copying roadmap or decision content here.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
