# AGENTS.md — research/

Working rules for humans, editors, and AI agents working in the research
folder. This folder holds active inquiries and working material.

## Folder Mission

Capture the process of learning: open questions, sources, and evolving
findings, in atomic notes that can grow into permanent knowledge.

## Responsibilities

- Maintain one atomic note per active inquiry.
- Record the question, sources, and current findings.
- Track progress with status changes from draft to active.
- Promote settled findings to the knowledge folder.
- Register every research note in INDEX.md.

## Boundaries

- Keep working material here only while it is unfinished.
- Never treat research notes as final knowledge.
- Do not store permanent references here.
- Avoid duplicate notes for the same inquiry.
- Do not include project-specific or vendor content.

## Documentation Rules

- One inquiry per note; keep notes under 100 lines.
- State the question clearly at the top of the note.
- Record where material came from so it is reproducible.
- Write plainly; research notes are still readable by all.
- Never add placeholders or generated content.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Record the source of material when relevant.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the note filename.

## Navigation Rules

- Link only to existing notes in this repository.
- Use wiki links, never absolute paths.
- Keep INDEX.md and SUMMARY.md entries in sync.
- Link related research notes to each other.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, links, and line counts.
- Confirm the note exists in INDEX.md and SUMMARY.md.
- Validate that every link target resolves.

## Editing Rules

- Update research notes as findings evolve.
- Change status when the inquiry moves forward.
- Refine titles and tags as understanding grows.
- Promote to knowledge when the finding is settled.

## Recovery Workflow

- Restore lost notes from git history.
- Rebuild partial notes from recorded sources.
- Repair broken front matter against validation.yaml.
- Merge duplicate research notes into one inquiry note.

## Common Mistakes

- Leaving research notes in the folder after completion.
- Copying finished knowledge into research notes.
- Writing notes without a clear question or source.
- Forgetting to update status as the inquiry progresses.
- Using invalid status values or missing YAML keys.
- Failing to register notes in the index files.
