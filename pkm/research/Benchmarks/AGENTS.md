# AGENTS.md — Benchmarks

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds notes about evaluation benchmarks.

## Folder Mission

Store self-contained, durable notes about benchmarks: what they measure,
how they score, and how to read their results.

## Responsibilities

- Maintain one atomic note per benchmark.
- Record the task, data, metrics, and caveats accurately.
- Note how results are compared across studies.
- Register every note in the repository INDEX.md.
- Link benchmarks to evaluations and experiments.

## Boundaries

- One benchmark per note; never merge families.
- No raw datasets or scoring artifacts in notes.
- No results attributed beyond the source.
- Do not duplicate benchmark coverage across categories.
- Keep notes self-contained and tool independent.

## Documentation Rules

- One idea per note; keep notes under 100 lines.
- Follow the repository naming conventions strictly.
- Use the templates in templates/ as the starting shape.
- Write in plain, clear language.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Record the benchmark source when known.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Point links only to existing notes.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link benchmarks to related research notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update notes when a benchmark changes.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild notes from recorded sources.
- Repair broken front matter against validation.yaml.
- Merge duplicate benchmark notes into one.

## Common Mistakes

- Storing unfinished or half-formed ideas here.
- Confusing benchmark results with conclusions.
- Writing overlapping or duplicate content.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
