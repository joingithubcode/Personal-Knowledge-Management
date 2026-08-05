# AGENTS.md — Archived

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds the record of retired projects.

## Folder Mission

Store the durable, self-contained record of projects no longer active,
kept readable without being kept current.

## Responsibilities

- Maintain atomic notes per archived project topic.
- Preserve the record accurately and completely.
- Mark retired notes clearly as archived.
- Register every note in the repository INDEX.md.
- Route retired projects here from Active or Completed.

## Boundaries

- Only retired projects; nothing current or planned.
- No task lists, schedules, or status tracking.
- Do not duplicate knowledge that lives in knowledge/.
- Do not keep anything that must stay current here.
- Keep notes self-contained and tool independent.

## Documentation Rules

- One idea per note; keep notes under 100 lines.
- Follow the repository naming conventions strictly.
- Use the templates in templates/ as the starting shape.
- Write in plain, clear language.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Status must be archived for retired notes.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Point links only to existing notes.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link archived notes to related project notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy and self-containment only.
- Do not keep active content in archived notes.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced notes to their proper category.
- Merge duplicate archived notes into one.

## Common Mistakes

- Archiving content that is still active.
- Deleting records instead of archiving them.
- Keeping general knowledge in archived notes.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
