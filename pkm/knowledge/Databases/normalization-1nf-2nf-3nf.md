---
title: "normalization-1nf-2nf-3nf"
status: draft
created: 2026-08-08
tags:
  - databases
  - data-modeling
  - normalization
related:
  - codds-12-rules
  - entity-relationship-modeling
  - primary-key-vs-foreign-key
---

# normalization-1nf-2nf-3nf

## Purpose

Capture the three foundational normalization forms (1NF, 2NF, 3NF) and why
they reduce redundancy and anomalies in relational tables.

## Context

A relational table stores rows of data with columns. Poorly designed tables
store the same fact in many places, which wastes space and invites
inconsistency when a fact changes. Normalization is a step-by-step process
that restructures a table so each fact lives in one place.

## Main Notes

- First normal form (1NF) requires atomic values: every cell holds a single
  value, and rows are identified by a key. No repeating groups or lists in a
  column.
- Second normal form (2NF) starts from 1NF and removes partial dependency:
  every non-key column depends on the whole composite key, not part of it.
- Third normal form (3NF) starts from 2NF and removes transitive dependency:
  a non-key column may not depend on another non-key column.
- Each higher form fixes a class of anomaly: update (one fact changed in many
  rows), insert (can add a row only if every fact is known), and delete
  (removing a row destroys unrelated facts).
- Normalization favors many small, focused tables over fewer wide ones.
- Normalizing to 3NF is common in OLTP design; going further (BCNF, 4NF)
  applies only when needed.
- Over-normalization can hurt read performance because queries must join many
  tables; design balances normalization against query needs.

## References

- Foundational concept; no single source.
- Relational database theory, derived from Edgar F. Codd's relational model.

## Related Notes

- [[codds-12-rules]]
- [[entity-relationship-modeling]]
- [[primary-key-vs-foreign-key]]

## Tags

This note is tagged in the front matter as databases, data-modeling,
normalization.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
