# AGENTS.md — Experiments

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds records of research experiments.

## Folder Mission

Store self-contained, durable records of experiments: hypothesis, setup,
procedure, and results, interpretable years later.

## Responsibilities

- Maintain one atomic note per experiment.
- Record the hypothesis and method accurately.
- Record results and conditions without distortion.
- Register every note in the repository INDEX.md.
- Link experiments to benchmarks and evaluations.

## Boundaries

- One experiment per note; never merge runs.
- No raw logs or full datasets in notes.
- No results claimed beyond what was observed.
- Do not duplicate experiment coverage across categories.
- Keep records self-contained and tool independent.

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
- Link experiments to related research notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Correct results as verification improves.
- Update the updated date when content changes.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild records from preserved results.
- Repair broken front matter against validation.yaml.
- Merge duplicate experiment notes into one.

## Common Mistakes

- Storing unfinished or half-formed ideas here.
- Recording results without their conditions.
- Writing overlapping or duplicate content.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
