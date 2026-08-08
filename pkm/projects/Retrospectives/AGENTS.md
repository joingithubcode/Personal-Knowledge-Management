# AGENTS.md — Retrospectives

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds lessons from reflecting on finished work.

## Folder Mission

Store self-contained, durable records of what projects taught, so lessons
carry forward into future work.

## Responsibilities

- Maintain one atomic note per retrospective.
- Record what worked, what did not, and why.
- Draw actionable lessons from the review.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Link retrospectives to completed projects.

## Boundaries

- Lessons only; no blame or private detail.
- No tasks or schedules in notes.
- Do not duplicate content that meeting notes cover.
- Do not keep the project itself in this folder.
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
- Link retrospectives to related project notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update lessons as more is learned.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild notes from surviving material.
- Repair broken front matter against validation.yaml.
- Merge duplicate retrospective notes into one.

## Common Mistakes

- Focusing on blame instead of lessons.
- Tracking tasks inside retrospective notes.
- Duplicating meeting content in retrospectives.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
