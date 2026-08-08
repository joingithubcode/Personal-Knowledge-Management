---
title: "query-optimization-basics"
status: draft
created: 2026-08-08
tags:
  - databases
  - performance
  - sql
related:
  - indexing-basics
---

# query-optimization-basics

## Purpose

Describe how databases optimize queries and how developers write queries that
execute efficiently.

## Context

The same logical query can be executed many ways: different join orders,
different access paths, different algorithms. A query optimizer picks a plan
by estimating costs. Developers improve slow queries by understanding that
planner and by shaping schemas, indexes, and statements to give it good
options.

## Main Notes

- The optimizer rewrites a query into equivalent forms and chooses the
  cheapest execution plan by estimated row counts and costs.
- Explain plans reveal the chosen plan: index scans, full table scans, join
  methods, and sort operations.
- The largest wins come from finding a missing index for filter, join, and
  order-by columns.
- Select only needed columns; returning large unused payloads wastes
  bandwidth and memory.
- Avoid functions on indexed columns in where clauses, because they can stop
  the index from being used.
- Keep join filters selective so the planner does not multiply large row
  sets; earlier, tighter filters shrink the work.
- Statistics drive the planner; keep them updated so estimates match reality.
- Optimize measured slow queries first; speculative tuning often wastes
  effort.

## References

- Foundational concept; no single source.
- Covered in database textbook literature on query processing and cost-based
  optimization.

## Related Notes

- [[indexing-basics]]

## Tags

This note is tagged in the front matter as databases, performance, sql.

## Review History

- 2026-08-08: Created as a draft.
