# AGENTS.md — Evaluations

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds notes assessing approaches and systems.

## Folder Mission

Store self-contained, durable assessments of how well approaches work,
with the criteria and evidence behind each judgment.

## Responsibilities

- Maintain one atomic note per evaluation.
- State criteria, evidence, and judgment clearly.
- Record the limits of each assessment.
- Register every note in this folder's own INDEX.md and SUMMARY.md; update the note count for this category in the root pkm/INDEX.md.
- Link evaluations to benchmarks and experiments.

## Boundaries

- One evaluation per note; never merge assessments.
- No judgments without the evidence behind them.
- Do not restate sources that other notes cover.
- Do not duplicate evaluation coverage across categories.
- Keep criteria explicit and self-contained.

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
- Link evaluations to related research notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update judgments as new evidence appears.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild assessments from linked evidence.
- Repair broken front matter against validation.yaml.
- Merge duplicate evaluation notes into one.

## Common Mistakes

- Judging without recorded evidence.
- Storing unfinished or half-formed ideas here.
- Writing overlapping or duplicate content.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
