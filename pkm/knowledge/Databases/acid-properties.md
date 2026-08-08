---
title: "acid-properties"
status: draft
created: 2026-08-08
tags:
  - databases
  - transactions
  - reliability
related:
  - database-transactions
  - nosql-vs-sql
---

# acid-properties

## Purpose

Define the ACID properties that make database transactions reliable.

## Context

A transaction is a batch of operations treated as one unit of work. Without
guardrails, a partial failure can leave data half-changed. ACID names four
properties a transaction system upholds so the database stays consistent
under concurrent access and crashes.

## Main Notes

- Atomicity: all operations in a transaction commit or all roll back; there
  is no partial result.
- Consistency: a transaction moves the database from one valid state to
  another, respecting all constraints and rules.
- Isolation: concurrent transactions do not see each other's unfinished
  changes; effects are as if they ran one after another.
- Durability: once committed, changes survive crashes and power loss.
- Isolation levels trade strictness against performance; weaker levels permit
  some anomalies such as dirty reads.
- The database uses undo and redo logs to enforce atomicity and durability.
- ACID is a property of the engine's transaction layer, not of a single query.
- NoSQL systems often relax ACID in favor of availability; see the
  CAP-related trade-offs in the nosql note.

## References

- Foundational concept; no single source.
- Formalized in database systems literature, including work by Jim Gray.

## Related Notes

- [[database-transactions]]
- [[nosql-vs-sql]]

## Tags

This note is tagged in the front matter as databases, transactions,
reliability.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
