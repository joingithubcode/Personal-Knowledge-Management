# WORKFLOW.md
Consolidated workflows for this repository; the rules behind each process live in STANDARDS.md.
Every workflow complies with AGENTS.md and STANDARDS.md.

## 1. Knowledge lifecycle
How knowledge moves through the repository over time.

- Stages: Ideas (ideas/) raw thoughts; Research (research/) active inquiry; Knowledge (knowledge/) settled understanding; Projects (projects/) knowledge applied to specific work.
- Flow: a thought is captured as an idea note; the developed idea becomes research or a project; settled findings promote to knowledge; project lessons feed back into knowledge; inactive content is archived.
- Promote an idea when it becomes a real inquiry or project; promote research when a finding is settled and durable; promote a project lesson when it generalizes beyond the project.
- Promotion moves the note to the destination folder and updates INDEX.md, SUMMARY.md, and all links; promote only complete, self-contained notes.
- Demote only by archiving; content never moves backward; demote unsupported research and ended projects; demotion follows section 4.
- A note is complete when accurate and self-contained; it stays in knowledge until outdated; completion is recorded in status and Review History.
- Every move updates front matter status, INDEX.md and SUMMARY.md, and fixes affected links; moves follow CONTRIBUTING.md.

## 2. Note workflow
How individual notes are created and changed.

- Create: choose the folder from its README.md; copy the matching template from templates/; name per STANDARDS.md section 4; fill front matter per section 3; write the body per section 2; register in INDEX.md and SUMMARY.md.
- Update: edit for clarity and accuracy, never just append; keep under 100 lines; update the updated date and Review History; fix affected links.
- Split when one note holds more than one idea; each part becomes its own atomic note; keep a summary in the original; link the parts; register every new note.
- Merge when two notes hold the same idea; keep one and fold the other's content in; preserve sources and Review History; redirect all links; remove the merged note from INDEX.md and SUMMARY.md.
- Link to existing notes only; link instead of duplicating; place links in Related Notes; verify every link before committing; fix links on rename or move.
- Rename only when misleading; update the title, heading, and all links; update INDEX.md and SUMMARY.md; never use a reserved name.
- Run all checks from validation.yaml after any change; confirm INDEX.md and SUMMARY.md stay current.

## 3. Review workflow
How notes are reviewed and kept accurate.

- Purpose: confirm accuracy and self-containment; rewrite unclear content; remove content that no longer belongs; keep tags, links, and status current.
- Frequency: ideas each capture session and monthly; research as findings evolve; knowledge when a related note changes; projects at the end; the full repository at least once per quarter.
- Audit: check required sections; verify front matter; verify all links resolve; verify registration in INDEX.md and SUMMARY.md; confirm the folder.
- Outdated notes: update when new understanding corrects them; mark for revision during review; archive when they cannot be kept accurate; never delete.
- Evergreen notes: accurate, complete, and stable; stay in knowledge without frequent change; reviews confirm accuracy; update only when the truth changes.
- Record every review in Review History; update the updated date on content change; change status only per the lifecycle.

## 4. Archiving
When and how notes are archived, and how they are recovered.

- Archive when a note is outdated and cannot be kept accurate; a project or inquiry finishes; an idea is deliberately set aside; a note is no longer acted on but still worth keeping.
- Criteria: no longer needs updates to be valuable; accurate enough as a record; not duplicating an active note; keeping it current costs more than it is worth.
- Process: 1 move to the archive folder; 2 set status to archived; 3 record in Review History; 4 update INDEX.md and SUMMARY.md; 5 fix affected links; 6 keep readable, never delete.
- Archiving is not deleting and not a judgment of value; archived notes stay searchable and linked; only duplicates or worthless notes are deleted.
- Recovery: restore from git history; move back to the active folder; set a new status and record the recovery; update INDEX.md and SUMMARY.md; restore only notes that are still accurate.
- Review the archive during the quarterly audit; keep records that still have value; delete only confirmed duplicates.

## 5. Search strategy
How information is found quickly in this repository.

- Naming: predictable filenames make notes findable by name alone; follow the naming rules; the name states the topic and the title and heading match it.
- Tags: tags group notes across folders; 2 to 5 lowercase tags; reuse existing tags, avoid near-duplicates; search by tag to collect a topic.
- Wiki links: links connect related notes and reveal clusters; internal only; Related Notes points to the best matches; follow links instead of re-searching.
- Navigation: SUMMARY.md maps the repository; folder README.md describes categories; category SUMMARY.md and INDEX.md map and register notes; start at SUMMARY.md and drill down by folder.
- Find quickly: 1 guess the filename; 2 check the category INDEX.md; 3 search the repository INDEX.md; 4 search by tag; 5 follow wiki links; 6 use the glossary.
- Keep search working: register every note; keep names, titles, and headings consistent; keep tags stable; keep every link valid.

## 6. Daily workflow
The daily operating routine.

- Capture: record new thoughts as idea notes during the day; capture quickly and refine later; follow the note workflow; register every new note.
- Inbox: process new notes at a fixed time daily; decide keep, develop, promote, or archive; keep undeveloped thoughts in ideas; move developed ideas to research or projects; leave nothing unclassified.
- Linking: link each new note to its best related notes; existing targets only; link instead of duplicating; add links in Related Notes.
- Checklist: valid front matter; registered in INDEX.md and SUMMARY.md; links resolve; correct folder.
- The routine is light by design; nothing is automatic; a day with no capture is valid.

## 7. Weekly maintenance
The weekly health check.

- Broken links: find links that do not resolve; fix or remove them; check Related Notes of changed notes; verify renamed notes.
- Duplicates: find notes covering the same topic; merge confirmed duplicates; keep the clearer note; redirect all links to it.
- Tag cleanup: list all tags; merge near-duplicates; remove single-use tags with no search value; keep the tag set consistent.
- Folder review: confirm correct folder placement; confirm every category has its four system files; promote mature research; fix misplaced notes.
- Validation checklist: run validation.yaml checks; notes under 100 lines; registered in INDEX.md and SUMMARY.md; front matter matches the YAML rules.

## 8. Monthly review
The monthly deep review of the whole repository.

- Archive review: review archived notes; confirm each decision holds; delete only confirmed duplicates; restore notes that are relevant again.
- Knowledge growth: review INDEX.md and SUMMARY.md; confirm note and category counts; identify growth and neglect; decide future effort.
- Research promotion: review research notes; promote settled findings to knowledge; archive dead research; update INDEX.md and SUMMARY.md after moves.
- Project cleanup: review project notes; close finished projects into Completed; archive inactive projects; extract general lessons into knowledge.
- Repository health: confirm all folders and categories intact; confirm system files current; run full validation; fix drift.

## 9. Knowledge capture
How new knowledge enters the repository and is routed correctly.

- Entry: a thought is captured as an idea note; the idea develops into research or a project; settled findings become knowledge notes; every note enters through the note workflow.
- Classify: raw and undeveloped -> ideas/; active and unsettled -> research/; settled and durable -> knowledge/; relevant only to one effort -> projects/; when unsure, capture in ideas/ first.
- Folder selection: ideas/, thoughts before development; research/, questions, sources, and findings; knowledge/, durable understanding; projects/, knowledge tied to one project; read the folder README first.
- Naming: follow the naming rules; use a specific, lowercase, hyphenated name; title and heading match the filename; rename early rather than later.
- Linking: link every new note to its best related notes; existing targets only; link instead of duplicating; register in INDEX.md and SUMMARY.md.
- Quality: capture in your own words; record the source when one exists; keep under 100 lines; follow the writing rules for the body.

## Related documents
- [STANDARDS.md](STANDARDS.md) — the rules each workflow applies.
- [CONTRIBUTING.md](CONTRIBUTING.md) — the contribution workflow.
- [AGENTS.md](AGENTS.md) — repository working rules.
- [validation.yaml](validation.yaml) — machine-readable checks.
- [AI-GUIDE.md](AI-GUIDE.md) — how AI agents use these workflows.
