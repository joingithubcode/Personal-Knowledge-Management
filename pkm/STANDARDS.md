# STANDARDS.md
Consolidated standards for this repository; each section governs one responsibility.
Working rules live in AGENTS.md; machine-readable rules live in validation.yaml.

## Authority

This document extends AGENTS.md and never overrides it; AGENTS.md always takes precedence.

## 1. Documentation structure
Scope: notes in knowledge/, research/, projects/, ideas/; navigation files (README, SUMMARY, INDEX) follow the same discipline.
- One note holds exactly one idea; notes are self-contained and readable alone.
- A note never duplicates content that exists in another note.
- Required sections in order: front matter; `# Note Title` (matches filename); `## Purpose`; `## Context`; `## Main Notes`; `## References`; `## Related Notes`; `## Tags`; `## Review History`.
- Keep every note under 100 lines; use templates/ as the starting shape.
- SUMMARY.md is the repository map, listing every folder and standards file.
- INDEX.md is the index of indexes; register every new note in its
  category's own INDEX.md and SUMMARY.md, and keep the category's note
  count current in the root INDEX.md.
- This standard governs structure only; content quality is governed by section 2.
- Any conflict between standards: the specific standard wins.

## 2. Writing
Scope: the body text of every note; front matter and filenames are governed by sections 3 and 4.
- Write simple, direct, factual sentences; prefer short words; use the active voice.
- Avoid jargon unless defined in the note or GLOSSARY.md; define abbreviations on first use.
- State the main idea early, in the Purpose section; use the first person sparingly.
- Write so the note is clear without opening any other file.
- Include only what the reader needs; one bullet per distinct point in Main Notes; remove filler.
- If a note exceeds the line limit, split or trim it.
- Use `#` for the title and `##` for sections only; bullets for parallel facts, numbered lists for steps.
- Use bold only for key terms and italics sparingly; keep tables minimal.
- No placeholder text, TODO markers, or lorem ipsum; no generated or boilerplate content.
- No copied blocks from external sources; no opinions presented as fact, mark uncertainty clearly.
- Rewrite for clarity during review, never just append; keep the note self-contained after every edit.
- Update the updated date and Review History when content changes.

## 3. YAML front matter
Scope: the front matter block of every note in the content folders.
- Front matter is enclosed by `---` on its own lines; it is the first content, before the title.
- Required keys: `title` (quoted, matches the filename), `status`, `created`, `tags`.
- Optional keys: `updated` (YYYY-MM-DD), `related` (list of note names), `source` (origin).
- Status values: draft (exists, incomplete); active (being developed); complete (finished, durable); archived (kept, no longer active).
- Dates are always YYYY-MM-DD; tags are a YAML list, one label per line.
- Titles are quoted strings; other values are plain strings.
- Every note must pass the front matter rules in validation.yaml; fix invalid keys before committing.

## 4. Naming
Scope: every note file and every folder under pkm/.
- Filenames: lowercase words joined by single hyphens; only `a-z`, `0-9`, and `-`; no spaces, underscores, or uppercase; under 60 characters; ending in `.md`. Pattern: `^[a-z0-9]+(-[a-z0-9]+)*\.md$`
- Folders: a single lowercase word; no hyphens, numbers, or uppercase.
- The `title` key and the `# Heading` must reflect the filename; rename the file when the topic's name changes.
- No dates or numbers at the start of a filename; no version numbers (git handles versions); no unclear abbreviations.
- Reserved names (README, AGENTS, standards filenames) are never used for notes.
- Rename only when the old name is misleading; after a rename, update INDEX.md, SUMMARY.md, and all links.

## 5. Linking
Scope: the Related Notes section and any wiki links in note bodies.
- Wiki links use `[[note-name]]`; the target is the filename without the `.md` extension; write it exactly, links are case-sensitive.
- Link to existing notes only; a broken link is an error.
- Internal links only; external URLs are forbidden.
- Link when genuinely relevant, not reflexively; prefer one best link over many weak ones.
- When notes share content, link instead of copying; a shared concept belongs in one note others link to.
- Create a link where a reader would otherwise search.
- Related Notes: bullet per note, ordered by relevance (most relevant first); keep the list short and meaningful.
- Fix every broken link when a note is renamed or deleted; check all links before committing.
- Links must resolve under the validation rules in validation.yaml.

## 6. Tagging
Scope: the `tags` list in every note's front matter.
- Each tag: one lowercase word or hyphenated phrase; no spaces, uppercase, or punctuation.
- Plural tags are preferred; maximum three words per tag. Pattern: `^[a-z]+(-[a-z]+)*$`
- Use 2 to 5 tags per note; a single tag is often enough.
- Tags are for topic, not status or project; prefer existing tags; a tag must help find the note.
- Folder conventions: knowledge, topic+discipline; research, topic+question; projects, project name+topic; ideas, topic only.
- Check existing tags before creating a new one; keep the same spelling (tags are case-sensitive).
- Merge near-duplicate tags when discovered; update affected notes when a tag is renamed.

## 7. Review
Scope: the status of every note and its Review History section.
- Status lifecycle: draft -> active -> complete -> archived; every transition is recorded in Review History.
- Reviews confirm a note is accurate and self-contained.
- Rewrite unclear content per section 2; remove content that no longer belongs; update tags and links.
- Cadence: ideas each capture session and monthly; research as findings evolve; knowledge when a related note changes.
- Projects are archived when the project ends.
- Ideas mature into research or projects when developed; research findings promote to knowledge when settled.
- Knowledge and project notes demote only by archive; a move updates INDEX.md, SUMMARY.md, and links.
- Archive when outdated but worth keeping, or when a project or inquiry is finished.
- Archived notes stay readable and linked, never deleted; delete only duplicates or notes with no value.
- Review History: one dated line per review, newest last; format `- YYYY-MM-DD: short summary of the review.`
- Record status changes and significant rewrites.

## Related documents
- [WORKFLOW.md](WORKFLOW.md) — how the rules are applied.
- [AGENTS.md](AGENTS.md) — repository working rules.
- [validation.yaml](validation.yaml) — machine-readable rules.
- [CONTRIBUTING.md](CONTRIBUTING.md) — the contribution workflow.
- [AI-GUIDE.md](AI-GUIDE.md) — how AI agents apply these standards.
