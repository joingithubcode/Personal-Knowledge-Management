# PR1
- agent: pkm-proofreader
- model: opencode/deepseek-v4.1-flash-free
- date: 2026-11-15T19:26:00+05:00
- prompt: Review knowledge/Databases/zz-test-wrong-fact.md.

## Response

[0m
> pkm-proofreader · deepseek-v4.1-flash-free
[0m
[0m→ [0mRead knowledge/Databases/zz-test-wrong-fact.md
[0m✱ [0mGlob ".opencode/agents/**"[90m 0 matches[0m
[0m✱ [0mGlob "knowledge/Databases/**"[90m 22 matches[0m
[0m✗ [0mRead  failed
[91m[1mError: [0mTool execution aborted
[0m✱ [0mGlob "templates/**"[90m 6 matches[0m
[0m→ [0mRead validation.yaml
[0m→ [0mRead STANDARDS.md
[0m→ [0mRead knowledge/Databases/INDEX.md
[0m→ [0mRead knowledge/Databases/SUMMARY.md
[0m→ [0mRead knowledge/Databases/acid-properties.md
## Issues
| # | Check | Quote | Problem | Severity |
|---|-------|-------|---------|----------|
| 1 | Task fit (accuracy) | "PostgreSQL is a NoSQL document database. It does not support SQL and has no transactions." | The core claim is factually false. PostgreSQL is a relational SQL database with full transaction support. This is the only substantive content in `Main Notes`. | high |
| 2 | Language (contradiction) | "Define the ACID properties that make database transactions reliable." | The Purpose promises a definition of ACID, but `Main Notes` never defines Atomicity, Consistency, Isolation, or Durability, and instead asserts the subject system has "no transactions." Purpose and body contradict each other. | high |
| 3 | Grounding / duplicate content | "A transaction is a batch of operations treated as one unit of work. Without" | This note is a near-verbatim copy of `knowledge/Databases/acid-properties.md` (identical front matter, Purpose, Context, References, Related Notes, Tags, Review History; only `Main Notes` differs). AGENTS.md forbids duplicate/overlapping notes and requires extending the existing note instead. | high |
| 4 | Format (naming/placeholders) | `zz-test-wrong-fact` | The name is derived from the filename and is not a "unique, meaningful" note name as required by AGENTS.md atomic note principles; the `zz-test-` prefix and content mark it as test/generated material, which AGENTS.md and validation.yaml (`no_generated_notes: true`, `no_placeholders: true`) prohibit in `knowledge/`. | medium |
| 5 | Task fit (registration) | "zz-test-wrong-fact" (absent from `knowledge/Databases/INDEX.md`) | The note is not listed in the category `INDEX.md` note registry (which ends at `test-topic — test topic`), so it violates the mandatory registration workflow in AGENTS.md. | medium |

## Corrected points
- Replace the false `Main Notes` sentence with an accurate ACID definition, or remove the note as a duplicate.
- Do not create this as a new note: merge/delete in favor of `acid-properties.md` per the no-duplicate rule.
- If kept, rename to a meaningful lowercase slug and strip any `zz-test-` / test-fixture framing.
- Register the note in `knowledge/Databases/INDEX.md` and reconcile the 18-note count in `SUMMARY.md`.
- Make Purpose and body consistent so the note actually defines ACID.
VERDICT: REVISE
