# AGENTS.md — Resources

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds reusable project resources.

## Folder Mission

Store self-contained, durable material that projects can draw on
repeatedly, without recreating it each time.

## Responsibilities

- Maintain one atomic note per reusable resource.
- Record what the resource is and how to use it.
- Keep resources stable and accurate.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Link resources to the projects that use them.

## Boundaries

- Only reusable material; nothing project-specific.
- No large files or raw assets in notes.
- Do not duplicate general knowledge that lives in knowledge/.
- Do not store active project context here.
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
- Link resources to related project notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update resources as they change.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced notes to their proper category.
- Merge duplicate resource notes into one.

## Common Mistakes

- Storing project-specific material as a resource.
- Duplicating general knowledge in resources.
- Keeping stale or unused resources indefinitely.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
