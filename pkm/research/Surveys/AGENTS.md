# AGENTS.md — Surveys

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds notes mapping a field or topic.

## Folder Mission

Store self-contained, durable overviews that map a field's landscape and
orient future reading.

## Responsibilities

- Maintain one atomic note per surveyed topic.
- Map the field's work, themes, and groups accurately.
- Distinguish the map from deep critical analysis.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Link surveys to the notes they point to.

## Boundaries

- Surveys orient; they do not deeply critique sources.
- No full text or copied excerpts from sources.
- Do not restate a single paper as a survey.
- Do not duplicate survey coverage across categories.
- Keep each survey's scope explicit.

## Documentation Rules

- One idea per note; keep notes under 100 lines.
- Follow the repository naming conventions strictly.
- Use the templates in templates/ as the starting shape.
- Write in plain, clear language.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- List the covered sources in the related key.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Point links only to existing notes.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link surveys to their covered paper notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update surveys as the field evolves.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild surveys from linked paper notes.
- Repair broken front matter against validation.yaml.
- Merge overlapping surveys into one.

## Common Mistakes

- Confusing surveys with deep reviews.
- Storing unfinished or half-formed ideas here.
- Writing overlapping or duplicate content.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
