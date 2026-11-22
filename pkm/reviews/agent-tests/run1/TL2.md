# TL2
- agent: zz-kb-tech-lead
- model: opencode/deepseek-v4.1-flash-free
- date: 2026-11-15T19:01:34+05:00
- prompt: Review knowledge/Databases/acid-properties.md.

## Response

[0m
> zz-kb-tech-lead · deepseek-v4.1-flash-free
[0m
[0m→ [0mRead knowledge/Databases/acid-properties.md
I'll review that note. Let me read it along with the relevant standards and related notes.
[0m✱ [0mGlob "knowledge/Databases/**/*.md"[90m 20 matches[0m
[0m→ [0mRead knowledge/Databases/database-transactions.md
[0m→ [0mRead knowledge/Databases/nosql-vs-sql.md
[0m→ [0mRead knowledge/Databases/INDEX.md
[0m→ [0mRead knowledge/Databases/SUMMARY.md
[0m✱ [0mGrep "ACID|CAP theorem|isolation|serializab|durab|undo|redo"[90m in knowledge · 100 matches[0m
[0m→ [0mRead validation.yaml
## Technical Review
**Verdict:** REQUEST_CHANGES

**Issues:**

1. **Line 33–34 — "Isolation: concurrent transactions do not see each other's unfinished changes; effects are as if they ran one after another."**
   This combines two different guarantees. "Do not see unfinished changes" is the no-dirty-reads property (read committed or stronger), not Isolation in general. ACID's Isolation is the serial-execution guarantee ("as if they ran one after another"). As written it is also contradicted by line 36–37, which correctly says weaker levels permit dirty reads. Qualify the definition, e.g. "Isolation: concurrent transactions do not interfere; the outcome is as if they ran serially. Stronger levels also prevent reading uncommitted changes."

2. **Lines 40–41 — "NoSQL systems often relax ACID in favor of availability; see the CAP-related trade-offs in the nosql note."**
   This conflates ACID consistency with CAP consistency. CAP's "C" is linearizability (atomic consistency) and CAP describes behavior under network partition; it is not a general trade of ACID guarantees for availability. The cross-reference is also inaccurate: `nosql-vs-sql` does not discuss CAP trade-offs — CAP appears there only in the References section. Rephrase to BASE/consistency-vs-availability without invoking CAP, or add the CAP distinction explicitly.

3. **Line 38 — "The database uses undo and redo logs to enforce atomicity and durability."**
   Stated as a universal property, but not all engines use undo/redo logs; some use rollback journals, WAL-only, or shadow paging, and MVCC engines may not maintain a separate undo log. Suggest "Many databases use write-ahead logging with undo/redo records — undo to roll back, redo to recover committed changes" to keep it engine-neutral (the folder rules forbid engine-specific claims).

4. **Line 35 — "Durability: once committed, changes survive crashes and power loss."**
   Missing caveat: this holds only for a durable/synchronous commit (e.g., fsync or synchronous-commit on). With asynchronous commit settings, transactions reported as committed can still be lost on crash. Durability also does not by itself cover media/disk failure (that needs replication or backups). Add a short qualification.

**Consistency check:** Related links (`[[database-transactions]]`, `[[nosql-vs-sql]]`) resolve and are reciprocal; the isolation-levels and transaction-log statements agree with `database-transactions.md`. The note is registered in `knowledge/Databases/INDEX.md`. No injection-style content found in the body.
