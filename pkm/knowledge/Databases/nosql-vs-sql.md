---
title: "nosql-vs-sql"
status: draft
created: 2026-08-08
tags:
  - databases
  - data-models
  - architecture
related:
  - acid-properties
---

# nosql-vs-sql

## Purpose

Compare SQL and NoSQL databases by data model, consistency, and use case.

## Context

SQL databases store data in fixed tables with schemas and relations. NoSQL is
a broad family of systems that trade strict structure and ACID guarantees for
flexible models and easier scaling. The choice depends on the application's
data shape and requirements, not on which is newer.

## Main Notes

- SQL (relational) databases use tables, rows, and joins, enforced by a
  schema and ACID transactions.
- NoSQL splits into main types: document, key-value, column-family, and
  graph stores.
- Document stores keep self-contained records (JSON-like); key-value stores
  offer simple fast reads; column-family stores suit wide sparse data; graph
  stores excel at relationships.
- SQL gives strong consistency and complex querying; NoSQL often relaxes
  consistency to gain availability and horizontal scaling.
- NoSQL schemas are flexible, so early iteration is faster, but data shape
  discipline must still come from application code.
- Some NoSQL systems (document stores) support joins and transactions today,
  narrowing the practical gap.
- Rule of thumb: structured, strongly related, transactional data suits SQL;
  high-volume, flexible, horizontally scaled data may suit NoSQL.
- Many systems use both: SQL for core records and NoSQL for caches, logs, or
  catalogs.

## References

- Foundational concept; no single source.
- CAP theorem from Eric Brewer; related database literature.

## Related Notes

- [[acid-properties]]

## Tags

This note is tagged in the front matter as databases, data-models,
architecture.

## Review History

- 2026-08-08: Created as a draft.
