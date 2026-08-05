# AGENTS.md — System-Design

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds durable knowledge about system design.

## Folder Mission

Store self-contained, long-lived notes about architecture, scalability,
and design trade-offs, independent of any specific product.

## Responsibilities

- Maintain atomic notes for system design topics.
- Keep every note accurate, current, and self-contained.
- Register every note in the repository INDEX.md.
- Link related notes across categories.
- Promote mature material from research into this folder.

## Boundaries

- Only finished knowledge; nothing temporary or in-progress.
- No raw sources or unprocessed material.
- No product-specific or vendor-specific content.
- Do not duplicate concepts across notes or categories.
- Keep material useful across system architectures.

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
- Use the README as the entry point for this category.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for clarity, accuracy, and self-containment.
- Keep the atomic structure when editing.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced notes and fix INDEX.md and SUMMARY.md.
- Merge duplicate notes into a single atomic note.

## Common Mistakes

- Storing unfinished or half-formed ideas here.
- Writing overlapping or duplicate content.
- Including product-specific or vendor-specific detail.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
