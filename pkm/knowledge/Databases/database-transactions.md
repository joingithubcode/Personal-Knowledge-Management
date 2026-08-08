---
title: "database-transactions"
status: draft
created: 2026-08-08
tags:
  - databases
  - transactions
  - concurrency
related:
  - acid-properties
---

# database-transactions

## Purpose

Explain database transactions: their lifecycle, concurrency behavior, and
isolation levels.

## Context

Real workloads mix reads and writes from many clients at once. Without
coordination, interleaved operations corrupt data. A transaction bundles
operations into one unit that runs as though alone, governed by the ACID
properties.

## Main Notes

- A transaction begins, runs statements, then commits (makes all changes
  permanent) or rolls back (undoes all changes).
- Commit and rollback are atomic: the group of changes stands or falls
  together.
- Concurrency control keeps concurrent transactions from interfering; locking
  and multi-versioning are the two main techniques.
- Isolation levels define how much concurrency is allowed: read uncommitted,
  read committed, repeatable read, and serializable.
- Weaker levels allow anomalies: dirty reads, non-repeatable reads, and
  phantom rows.
- Serializable is the strictest but most expensive; most engines default to
  read committed or repeatable read.
- Long-running transactions hold resources longer and can block others; keep
  them short.
- The transaction log records changes so the database can undo on rollback
  and redo on recovery.

## References

- Foundational concept; no single source.
- SQL standard (ISO/IEC 9075) defines isolation levels.

## Related Notes

- [[acid-properties]]

## Tags

This note is tagged in the front matter as databases, transactions,
concurrency.

## Review History

- 2026-08-08: Created as a draft.
