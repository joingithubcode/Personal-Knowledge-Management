# AGENTS.md — Meetings

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds knowledge from project meetings.

## Folder Mission

Store self-contained, durable records of what meetings produced: outcomes,
agreements, and actions the project depends on.

## Responsibilities

- Maintain one atomic note per meaningful meeting.
- Record outcomes and agreements accurately.
- Note agreed follow-ups without tracking tasks.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Link meetings to decisions and project notes.

## Boundaries

- Outcomes only; no verbatim transcripts.
- No task lists or schedules in notes.
- Do not duplicate decision content in meeting notes.
- Do not record private or irrelevant detail.
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
- Link meetings to related project notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Correct the record as understanding improves.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild records from surviving notes.
- Repair broken front matter against validation.yaml.
- Merge duplicate meeting notes into one.

## Common Mistakes

- Writing verbatim transcripts instead of outcomes.
- Tracking tasks inside meeting notes.
- Duplicating decision content in meeting notes.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
