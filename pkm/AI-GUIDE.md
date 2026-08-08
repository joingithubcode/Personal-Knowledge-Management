# AI-GUIDE.md

How AI agents should read, search, and update this repository. Read this
file together with AGENTS.md before any AI-assisted work.

## Before any change

Before creating, editing, moving, deleting, or linking notes, an AI agent MUST:

- Read AGENTS.md.
- Validate against validation.yaml.
- Follow STANDARDS.md.
- Execute WORKFLOW.md.
- Use the correct template.
- Update INDEX.md and SUMMARY.md if required.

## How AI should read the PKM

- Read AGENTS.md first; it is the authority.
- Read the folder README.md before touching that folder.
- Read the relevant standards before any edit.
- Never assume content; verify against files.

## Search order

1. SUMMARY.md for the repository map.
2. The folder README.md for category layout.
3. The category INDEX.md for note registration.
4. The category SUMMARY.md for the category map.
5. Tags for cross-cutting topics per WORKFLOW.md section 5.

## Retrieval rules

- Retrieve the full note before quoting or editing it.
- Confirm the note exists in INDEX.md and SUMMARY.md.
- Follow wiki links to related material.
- Report what is missing rather than inventing it.

## Update rules

- Follow WORKFLOW.md section 2 for every change.
- Update front matter per STANDARDS.md section 3.
- Update the category INDEX.md and SUMMARY.md when adding notes; update
  the root INDEX.md per-category count.
- Never create a note outside the approved structure.

## Editing constraints

- Keep every file under 100 lines.
- Keep notes self-contained and atomic.
- Follow STANDARDS.md section 2 in all prose.
- Never add placeholders, examples, or generated content.

## Recovery behavior

- If a file is missing or broken, report it.
- Repair front matter against STANDARDS.md section 3.
- Restore lost content from git history.
- Fix links per STANDARDS.md section 5.
- Never fabricate a note to fill a gap.

## Prohibitions

- No creating actual knowledge notes without request.
- No modifying validation.yaml.
- No modifying existing system files without request.
- No external content or vendor-specific material.

## Related documents

- [AGENTS.md](AGENTS.md) — repository working rules.
- [WORKFLOW.md#5-search-strategy](WORKFLOW.md#5-search-strategy) — how to find information.
- [WORKFLOW.md#9-knowledge-capture](WORKFLOW.md#9-knowledge-capture) — how notes are added.
- [WORKFLOW.md#3-review-workflow](WORKFLOW.md#3-review-workflow) — how notes are assessed.
