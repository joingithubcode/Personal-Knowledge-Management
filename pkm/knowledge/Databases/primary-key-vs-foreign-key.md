---
title: "primary-key-vs-foreign-key"
status: draft
created: 2026-08-08
tags:
  - databases
  - data-modeling
  - relational-model
related:
  - entity-relationship-modeling
  - normalization-1nf-2nf-3nf
---

# primary-key-vs-foreign-key

## Purpose

Distinguish primary keys from foreign keys and explain their roles in
relational integrity.

## Context

Relational tables need a way to identify each row and to connect rows across
tables. Keys are the mechanism. A primary key identifies a row within its own
table; a foreign key references a primary key in another table to record a
relationship.

## Main Notes

- A primary key uniquely identifies each row: no two rows share the same
  value, and it never holds null.
- A table has at most one primary key, though a composite primary key can use
  several columns together.
- A foreign key is a column (or columns) whose values must match a primary
  key value in another table.
- Foreign keys enforce referential integrity: the database rejects a foreign
  value that has no matching primary key.
- A foreign key value may repeat, and it may be null when the relationship is
  optional.
- The referenced primary key is usually an index, so join queries find
  matches quickly.
- Tables reference one another through these key pairs; joins use them as
  the natural match condition.
- Design rules: choose stable, minimal primary keys; name foreign keys by the
  table and column they reference.

## References

- Foundational concept; no single source.
- Relational model from Edgar F. Codd; SQL standards (ISO/IEC 9075).

## Related Notes

- [[entity-relationship-modeling]]
- [[normalization-1nf-2nf-3nf]]

## Tags

This note is tagged in the front matter as databases, data-modeling,
relational-model.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
