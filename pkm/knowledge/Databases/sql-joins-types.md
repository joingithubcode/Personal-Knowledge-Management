---
title: "sql-joins-types"
status: draft
created: 2026-08-08
tags:
  - databases
  - sql
  - querying
related:
  - codds-12-rules
---

# sql-joins-types

## Purpose

Explain the main SQL join types and the row sets each returns.

## Context

Relational data lives in separate tables that connect through shared columns,
usually keys. A join combines rows from two or more tables based on a match
condition, letting one query see related data together. Choosing the right
join type controls which rows appear in the result.

## Main Notes

- An inner join returns only rows with a match in both tables; unmatched rows
  are dropped.
- A left outer join keeps every row from the left table and adds matching
  right rows, filling unmatched columns with null.
- A right outer join mirrors the left: it keeps every row from the right
  table and adds matching left rows.
- A full outer join keeps all rows from both sides, matching where possible
  and using null elsewhere.
- A cross join returns every pair of rows (the cartesian product) and has no
  match condition.
- A self join joins a table to itself, useful for hierarchies such as
  employees and their managers.
- A natural join matches columns with the same name automatically; explicit
  on clauses are usually clearer and preferred.
- Join conditions use keys: primary key to foreign key is the common pattern.

## References

- Foundational concept; no single source.
- SQL standards (ISO/IEC 9075) define join semantics.

## Related Notes

- [[codds-12-rules]]

## Tags

This note is tagged in the front matter as databases, sql, querying.

## Review History

- 2026-08-08: Created as a draft.
