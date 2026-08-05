# AGENTS.md — projects/

Working rules for humans, editors, and AI agents working in the projects
folder. This folder holds knowledge scoped to personal projects.

## Folder Mission

Capture project-bound knowledge in atomic notes, and feed any general
lessons back into the knowledge folder for reuse.

## Responsibilities

- Maintain one atomic note per project or project topic.
- Record decisions, context, and insights specific to the project.
- Link project notes to related general knowledge.
- Register every project note in INDEX.md.
- Extract general lessons into the knowledge folder.

## Boundaries

- Keep notes scoped to a single personal project.
- Never store general-purpose knowledge here.
- Do not duplicate content that lives in knowledge/.
- Do not include vendor or external system detail.
- Do not document project tasks or planning output.

## Documentation Rules

- One project topic per note; keep notes under 100 lines.
- State which project a note belongs to in its content.
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
- Link project notes to their general knowledge counterparts.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note exists in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Update notes as the project progresses.
- Mark archived status when a project ends.
- Extract general lessons to knowledge before archiving.
- Keep one note per project topic, merging overlaps.

## Recovery Workflow

- Restore lost notes from git history.
- Repair broken front matter against validation.yaml.
- Move misplaced general notes into knowledge/.
- Merge duplicate project notes into one.

## Common Mistakes

- Storing general knowledge in project notes.
- Copying knowledge notes into project notes.
- Adding project task lists or planning artifacts.
- Using project jargon without explanation.
- Using invalid status values or missing YAML keys.
- Forgetting to register notes in the index files.
