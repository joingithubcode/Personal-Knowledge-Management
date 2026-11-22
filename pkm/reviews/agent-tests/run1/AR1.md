# AR1
- agent: zz-kb-architect
- model: opencode/deepseek-v4.1-flash-free
- date: 2026-11-15T19:04:51+05:00
- prompt: Review knowledge/Databases/zz-test-bad-frontmatter.md.

## Response

[0m
> zz-kb-architect · deepseek-v4.1-flash-free
[0m
[0m✗ [0mls -la && echo "---" && ls -la knowledge 2>/dev/null && echo "---" && ls -la knowledge/Databases 2>/dev/null failed
[91m[1mError: [0mThe user has specified a rule which prevents you from using this specific tool call. Here are some of the relevant rules [{"permission":"*","action":"allow","pattern":"*"},{"permission":"bash","pattern":"*","action":"ask"},{"permission":"bash","pattern":"git status*","action":"allow"},{"permission":"bash","pattern":"git log*","action":"allow"},{"permission":"bash","pattern":"git diff*","action":"allow"},{"permission":"bash","pattern":"grep*","action":"allow"},{"permission":"bash","pattern":"python3 pkm/scripts/validate.py*","action":"allow"},{"permission":"bash","pattern":"python3 scripts/validate.py*","action":"allow"},{"permission":"bash","pattern":"*","action":"deny"},{"permission":"bash","pattern":"python3 pkm/scripts/validate.py*","action":"allow"},{"permission":"bash","pattern":"python3 scripts/validate.py*","action":"allow"}]
[0m✱ [0mGlob "**/zz-test-bad-frontmatter.md"[90m 1 match[0m
[0m→ [0mRead knowledge/Databases/zz-test-bad-frontmatter.md
[0m→ [0mRead validation.yaml
[0m→ [0mRead STANDARDS.md
[0m✱ [0mGlob "knowledge/Databases/**"[90m 20 matches[0m
[0m✱ [0mGlob "**/{database-transactions,nosql-vs-sql}.md"[90m 2 matches[0m
[0m
[0m$ [0mpython3 pkm/scripts/validate.py
========================================================================
PKM VALIDATION REPORT
========================================================================

## knowledge
  FAIL knowledge/Databases/zz-test-bad-frontmatter.md [frontmatter] status 'finished' not in allowed values ['draft', 'active', 'complete', 'archived']
  FAIL knowledge/Databases/zz-test-bad-frontmatter.md [frontmatter] created '08-11-2026' does not match YYYY-MM-DD
  FAIL knowledge/Databases/zz-test-bad-frontmatter.md [frontmatter] tags must be a non-empty list
  FAIL knowledge/Databases/zz-test-broken-link.md [links] wiki link [[does-not-exist-anywhere]] does not resolve to any .md file

## structure
  FAIL knowledge/Databases [counts] SUMMARY.md says 15 notes, disk has 16
  FAIL knowledge/Databases [counts] root INDEX.md says 15 notes, disk has 16

## structure
  PASS structure checks

========================================================================
133 notes checked, 6 violations found
========================================================================
[0m
[0m→ [0mRead knowledge/Databases/INDEX.md
[0m→ [0mRead knowledge/Databases/SUMMARY.md
[0m→ [0mRead INDEX.md
[0m→ [0mRead knowledge/Databases/acid-properties.md
## Architecture Review

**Verdict:** REQUEST_CHANGES

**Note:** `knowledge/Databases/zz-test-bad-frontmatter.md` (58 lines). I did not modify anything; findings are report-only.

### Validator output (repo root, `python3 pkm/scripts/validate.py`)

```
## knowledge
  FAIL knowledge/Databases/zz-test-bad-frontmatter.md [frontmatter] status 'finished' not in allowed values ['draft', 'active', 'complete', 'archived']
  FAIL knowledge/Databases/zz-test-bad-frontmatter.md [frontmatter] created '08-11-2026' does not match YYYY-MM-DD
  FAIL knowledge/Databases/zz-test-bad-frontmatter.md [frontmatter] tags must be a non-empty list
  FAIL knowledge/Databases/zz-test-broken-link.md [links] wiki link [[does-not-exist-anywhere]] does not resolve to any .md file

## structure
  FAIL knowledge/Databases [counts] SUMMARY.md says 15 notes, disk has 16
  FAIL knowledge/Databases [counts] root INDEX.md says 15 notes, disk has 16

133 notes checked, 6 violations found
```

(The `zz-test-broken-link.md` failure is in a different note and is pre-existing/unrelated to this review; the two count failures relate directly to this note's registration.)

### Compliant points
- Folder placement is correct: the body is durable database knowledge, so `knowledge/Databases/` is the right category (AGENTS.md — "knowledge: permanent, organized, durable understanding").
- Filename matches `^[a-z0-9]+(-[a-z0-9]+)*\.md$` and is under 60 characters (validation.yaml `naming.note_files`; STANDARDS.md §4).
- All four required keys are present, `related` is a permitted additional key, `title` is quoted and matches the filename, and both wiki links (`database-transactions`, `nosql-vs-sql`) resolve (validation.yaml `frontmatter.required_keys`, `links.target_must_exist`).
- 58 lines, under the 100-line note limit (validation.yaml `line_limits.notes`).
- Injection scan: no instruction-like or prompt-injection text in the body (kb-injection-scan).

### Issues

1. **Invalid `status` value.** `status: finished` is not an allowed value. Allowed: `draft`, `active`, `complete`, `archived`.
   - Rule: validation.yaml `frontmatter.status.allowed`; STANDARDS.md §3 ("Status values: draft, active, complete, archived"); AGENTS.md → YAML standards ("Status must be one of: draft, active, complete, archived").

2. **Invalid `created` date format.** `created: 08-11-2026` is not ISO `YYYY-MM-DD` (also ambiguous DD-MM vs MM-DD).
   - Rule: validation.yaml `frontmatter.created.format: YYYY-MM-DD`; STANDARDS.md §3 ("Dates are always YYYY-MM-DD"); AGENTS.md → YAML standards.

3. **Empty `tags` list.** `tags: []` fails validation; tags must be a non-empty lowercase list, and the standards require 2–5 tags. The body's `## Tags` section even claims "databases, transactions, reliability" while the front matter is empty.
   - Rule: validation.yaml `frontmatter.tags` (validator: "tags must be a non-empty list"); STANDARDS.md §6 ("Use 2 to 5 tags per note"; lowercase list); AGENTS.md → YAML standards ("tags are lowercase lists").

4. **Duplicate content.** The note body is a near-verbatim duplicate of `knowledge/Databases/acid-properties.md` (identical Purpose, Context, Main Notes, References, Related Notes, Tags, and Review History). A note must link to existing content, not copy it.
   - Rule: AGENTS.md → Atomic note principles ("Notes connect through wiki links, never through duplicate content"); AGENTS.md → Common mistakes ("Writing notes with duplicate or overlapping content"); STANDARDS.md §1 ("A note never duplicates content that exists in another note"). This note should be deleted or merged into `acid-properties.md`.

5. **Filename/title is a meaningless test placeholder.** `zz-test-bad-frontmatter` violates the requirement for a unique, meaningful note name; it is a test artifact rather than knowledge. Its name/title does not describe the actual content (ACID), and placeholders/generated content are prohibited.
   - Rule: AGENTS.md → Naming conventions ("Each note has a unique, meaningful, lowercase name"); AGENTS.md → Common mistakes ("Using spaces, uppercase, or dates in filenames" plus placeholder content); validation.yaml `content.no_placeholders: true`, `content.no_generated_notes: true`; STANDARDS.md §2 ("No placeholder text, TODO markers… no generated or boilerplate content") and §4 ("no unclear abbreviations").

6. **Not registered in the category INDEX.md.** The `## Note registry` in `knowledge/Databases/INDEX.md` does not list this note (only 11 of 16 note files are listed; none of the `zz-test-*` files appear).
   - Rule: AGENTS.md → Validation workflow ("Register new notes in their category's INDEX.md and SUMMARY.md"); AGENTS.md → Common mistakes ("Forgetting to register notes in INDEX.md and SUMMARY.md"); `knowledge/Databases/AGENTS.md` → Navigation Rules ("Keep INDEX.md and SUMMARY.md entries in sync").

7. **Category SUMMARY.md count is stale.** `knowledge/Databases/SUMMARY.md` says `15 notes`; disk has 16.
   - Rule: validation.yaml `navigation` (structure/count checks); AGENTS.md → Validation workflow; `knowledge/Databases/AGENTS.md` → Responsibilities ("update the note count for this category in the root pkm/INDEX.md") and SUMMARY.md maintenance notes.

8. **Root INDEX.md category count is stale.** `pkm/INDEX.md` lists Databases as `15 notes`; disk has 16.
   - Rule: AGENTS.md → Validation workflow ("update the root INDEX.md per-category count"); pkm/INDEX.md → Maintenance ("Update the note count on this page whenever a category's count changes"); validation.yaml structure checks.

9. **Internal inconsistencies (secondary).** Front matter `created: 08-11-2026` conflicts with Review History entries dated `2026-08-08`, and the body `## Tags` section lists tags that are absent from the front matter. The note is not self-contained/consistent across its own sections.
   - Rule: STANDARDS.md §2 (self-contained, no filler) and §3 (front matter is the source of tags); STANDARDS.md §7 (Review History must reflect actual reviews/status changes).

### Required changes
- Replace the body with either deletion (preferred, since it duplicates `acid-properties.md`) or a genuine, non-duplicate note; if kept, give it a meaningful filename/title matching the topic.
- Fix `status` to `draft|active|complete|archived`, `created` to `YYYY-MM-DD`, and provide 2–5 lowercase tags.
- Register it in `knowledge/Databases/INDEX.md` and update the counts in `knowledge/Databases/SUMMARY.md` and `pkm/INDEX.md` to the actual note total (16, or 15 if this duplicate is removed).
