# AGENTS.md — Archive

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds ideas kept for the record.

## Folder Mission

Store the durable, self-contained record of ideas that were considered
and set aside, readable without being kept current.

## Responsibilities

- Maintain one atomic note per archived idea.
- Preserve what the idea was and why it stopped.
- Mark retired ideas clearly as archived.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Route set-aside ideas here from other categories.

## Boundaries

- Only retired ideas; nothing under consideration.
- No active plans or current thinking.
- Do not duplicate an idea that still lives elsewhere.
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
- Status must be archived for retired ideas.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Point links only to existing notes.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link archived ideas to related idea notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy and self-containment only.
- Do not keep active thinking in archived notes.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced notes to their proper category.
- Merge duplicate archived ideas into one.

## Common Mistakes

- Archiving ideas that are still under consideration.
- Deleting records instead of archiving them.
- Keeping active thinking in archived notes.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
