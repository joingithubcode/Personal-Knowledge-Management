# AGENTS.md — Open-Questions

Working rules for humans, editors, and AI agents working in this category
folder. This folder holds notes about unanswered research questions.

## Folder Mission

Store self-contained, durable records of open questions and the progress
made toward answering them.

## Responsibilities

- Maintain one atomic note per open question.
- State the question and why it matters clearly.
- Track partial progress and directions tried.
- Register every note in the repository INDEX.md.
- Link questions to related papers and notes.

## Boundaries

- One question per note; never merge unrelated unknowns.
- No answers claimed that are not yet found.
- Do not duplicate questions across multiple notes.
- Do not let open questions age into silence.
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
- Link questions to related research notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note is registered in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Edit for accuracy, clarity, and self-containment.
- Update progress as the question develops.
- Archive questions that are answered or abandoned.
- Record changes in the Review History section.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild notes from recorded sources.
- Repair broken front matter against validation.yaml.
- Merge duplicate question notes into one.

## Common Mistakes

- Answering a question that remains unanswered.
- Storing unfinished or half-formed ideas here.
- Writing overlapping or duplicate content.
- Using invalid status values or missing YAML keys.
- Linking to notes that do not exist.
- Forgetting to register notes in the index files.
