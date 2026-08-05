# CONTRIBUTING.md

Single responsibility: the workflow for creating, editing, and
maintaining notes. The standards each step must satisfy are
cross-referenced below.

## Creating a note

1. Choose the correct folder from its README.md.
2. Copy the matching template from templates/.
3. Name the file per STANDARDS.md section 4.
4. Fill the front matter per STANDARDS.md section 3.
5. Write the body per STANDARDS.md section 2.
6. Register the note in INDEX.md and SUMMARY.md.

## Editing a note

- Follow the same standards as when creating.
- Keep the note under 100 lines after every edit.
- Update the `updated` date and Review History.
- Fix every affected link per STANDARDS.md section 5.

## Promoting a note

- Move ideas to research or projects when developed.
- Move settled research into knowledge.
- Follow the transitions in STANDARDS.md section 7.
- Update INDEX.md, SUMMARY.md, and all links.

## Renaming or deleting

- Rename only when the name is misleading.
- Update links, INDEX.md, and SUMMARY.md after a rename.
- Archive instead of delete; delete only duplicates.

## Validation before commit

1. Read validation.yaml and run every applicable rule.
2. Verify front matter, naming, links, and line counts.
3. Confirm INDEX.md and SUMMARY.md are current.
4. Confirm all wiki links resolve.

## Recovery

- Restore lost notes from git history.
- Repair broken front matter against STANDARDS.md section 3.
- Re-align drifted structure with STANDARDS.md section 1.
- Merge duplicates into a single atomic note.

## Review workflow

- Review notes on the cadence in STANDARDS.md section 7.
- Record every review in the Review History section.

## Related documents

- [STANDARDS.md](STANDARDS.md) — the rules each step applies.
- [WORKFLOW.md](WORKFLOW.md) — the note lifecycle.
- [AI-GUIDE.md](AI-GUIDE.md) — how AI agents contribute.
