# AGENTS.md — retraction-prediction-analysis

Working rules for humans and AI agents working in this project folder.

## Folder Mission

Capture project-scoped knowledge about retraction prediction analysis in atomic notes that can grow into reusable insights.

## Responsibilities

- Maintain one atomic note per analysis topic or findings.
- Record insights, patterns, and decisions specific to retraction prediction.
- Link project notes to related research notes in the research/ folder.
- Register every note in this folder's INDEX.md; update the note count in the root pkm/INDEX.md.
- Extract general lessons into the knowledge/ folder when the project ends.

## Boundaries

- Keep notes scoped to a single personal project (retraction prediction analysis).
- Never store general-purpose knowledge here.
- Do not duplicate content that lives in research/ or knowledge/.
- Do not include vendor or external system detail beyond what is relevant to the analysis.

## Documentation Rules

- One topic per note; keep notes under 100 lines.
- State the project context in the content.
- Write so the note is readable without the project open.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Tag notes with the project name for grouping.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Link only to existing notes in this repository.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link project notes to their research counterparts.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note exists in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Update notes as the analysis progresses.
- Mark archived status when the analysis ends.
- Extract general lessons to knowledge/ before archiving.
- Keep one note per analysis topic, merging overlaps.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced general notes into knowledge/.
- Merge duplicate project notes into one.

## Common Mistakes

- Storing general knowledge in project notes.
- Copying research notes into project notes.
- Adding analysis task lists or planning artifacts.
- Using analysis-specific jargon without explanation.
- Using invalid status values or missing YAML keys.
- Forgetting to register notes in the index files.