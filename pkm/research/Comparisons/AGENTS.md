# AGENTS.md — Comparisons

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds notes comparing approaches and results.

## Folder Mission

Store self-contained, durable comparisons that clarify trade-offs between
related approaches or findings.

## Responsibilities

- Maintain one atomic note per comparison.
- Compare on explicit, consistent criteria.
- Record differences and trade-offs accurately.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Link comparisons to their source notes.

## Boundaries

- One comparison per note; never merge topics.
- No results stated beyond the sources compared.
- Do not restate sources that notes already cover.
- Do not duplicate comparison coverage across categories.
- Keep criteria explicit and self-contained.

## Documentation Rules

- One idea per note; keep notes under 100 lines.
- Follow the repository naming conventions strictly.
- Use the templates in templates/ as the starting shape.
- Write in plain, clear language.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- List the compared notes in the related key.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Point links only to existing notes.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link comparisons to the approaches compared.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update comparisons as new evidence appears.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild comparisons from linked source notes.
- Repair broken front matter against validation.yaml.
- Merge overlapping comparisons into one.

## Common Mistakes

- Comparing without explicit criteria.
- Storing unfinished or half-formed ideas here.
- Writing overlapping or duplicate content.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
