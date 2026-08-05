# AGENTS.md — ideas/

Working rules for humans, editors, and AI agents working in the ideas
folder. This folder holds raw, undeveloped thoughts.

## Folder Mission

Capture thoughts quickly and safely, and route them forward as they grow:
to research, to projects, or to permanent knowledge.

## Responsibilities

- Capture every worthwhile thought in one atomic note.
- Keep idea notes short and honest about their state.
- Register every idea note in INDEX.md.
- Review ideas regularly and move or discard them.
- Promote developed ideas to research or projects.

## Boundaries

- Keep ideas unfinished by design; do not develop them here.
- Never store finished knowledge or settled findings.
- Do not duplicate an idea that already exists.
- Do not capture tasks, schedules, or action lists.
- Do not include vendor or external system detail.

## Documentation Rules

- One idea per note; keep notes well under 100 lines.
- Write enough to recall the idea, no more.
- Never add placeholders or generated content.
- Prefer a clear title over a long description.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.
- Keep tags simple and few.

## Navigation Rules

- Link only to existing notes in this repository.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link ideas to related research or project notes.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note exists in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Keep idea notes minimal and fast to scan.
- Refine titles and tags when an idea develops.
- Move an idea to research or projects when it matures.
- Archive or delete ideas that go nowhere.

## Recovery Workflow

- Restore lost ideas from git history.
- Repair broken front matter against validation.yaml.
- Recreate short idea notes from memory if needed.
- Merge duplicate ideas into one note.

## Common Mistakes

- Developing ideas fully inside this folder.
- Writing idea notes that are too long.
- Storing finished knowledge as ideas.
- Capturing tasks or scheduling material.
- Using invalid status values or missing YAML keys.
- Never reviewing or pruning the idea folder.
