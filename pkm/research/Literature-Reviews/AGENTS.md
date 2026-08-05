# AGENTS.md — Literature-Reviews

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds syntheses of related literature.

## Folder Mission

Store self-contained, durable syntheses of a body of literature: its
themes, agreements, gaps, and open questions.

## Responsibilities

- Maintain one atomic note per literature review.
- Synthesize many papers into coherent findings.
- Distinguish reported findings from personal conclusions.
- Register every note in the repository INDEX.md.
- Link each review to the papers it covers.

## Boundaries

- Reviews summarize; they do not restate whole papers.
- No full text or copied excerpts from sources.
- Do not store a single paper's summary as a review.
- Keep the scope of each review explicit.
- Do not duplicate synthesis across categories.

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
- Link reviews to their source paper notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update reviews as new literature is added.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild reviews from linked paper notes.
- Repair broken front matter against validation.yaml.
- Merge overlapping reviews into one.

## Common Mistakes

- Restating papers instead of synthesizing them.
- Storing unfinished or half-formed ideas here.
- Writing overlapping or duplicate content.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
