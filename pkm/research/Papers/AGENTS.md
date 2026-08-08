# AGENTS.md — Papers

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds notes about individual academic papers.

## Folder Mission

Store self-contained, durable notes about papers and their findings,
accurate enough to cite and reuse years later.

## Responsibilities

- Maintain one atomic note per paper.
- Record the claim, method, and finding accurately.
- Note the source clearly for later citation.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Link papers to reviews, comparisons, and questions.

## Boundaries

- One paper per note; never merge papers together.
- No full text or copied excerpts; summarize in your own words.
- No unfinished impressions as if they were findings.
- Do not duplicate paper coverage across categories.
- Keep notes tool independent and self-contained.

## Documentation Rules

- One idea per note; keep notes under 100 lines.
- Follow the repository naming conventions strictly.
- Use the templates in templates/ as the starting shape.
- Write in plain, clear language.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Record the paper source in the source key.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Point links only to existing notes.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link each paper to related research notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Correct claims as understanding improves.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild notes from recorded paper sources.
- Repair broken front matter against validation.yaml.
- Merge duplicate paper notes into one.

## Common Mistakes

- Storing unfinished or half-formed ideas here.
- Copying text instead of summarizing findings.
- Writing overlapping or duplicate content.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
