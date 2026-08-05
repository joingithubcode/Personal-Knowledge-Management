# AGENTS.md — Case-Studies

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds notes about specific real-world cases.

## Folder Mission

Store self-contained, durable accounts of real cases and the general
lessons they support.

## Responsibilities

- Maintain one atomic note per case study.
- Record the facts of the case accurately.
- Separate what happened from what it implies.
- Register every note in the repository INDEX.md.
- Link case studies to related research notes.

## Boundaries

- One case per note; never merge unrelated cases.
- No identifiable private detail without consent.
- Do not overgeneralize beyond what the case shows.
- Do not duplicate case coverage across categories.
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
- Link case studies to related research notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update notes as case details are verified.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild notes from recorded sources.
- Repair broken front matter against validation.yaml.
- Merge duplicate case notes into one.

## Common Mistakes

- Generalizing beyond what the case shows.
- Storing unfinished or half-formed ideas here.
- Writing overlapping or duplicate content.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
