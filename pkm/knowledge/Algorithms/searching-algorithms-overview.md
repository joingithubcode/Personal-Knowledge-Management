---
title: "searching-algorithms-overview"
status: draft
created: 2026-08-08
tags:
  - algorithms
  - searching
  - complexity
related:
  - big-o-notation
  - sorting-algorithms-overview
---

# searching-algorithms-overview

## Purpose

Survey common searching algorithms and the data each works best on.

## Context

Finding an item in a collection is a daily programming task, but the best way
depends on the structure of the data. A search on sorted data can be far
faster than one on arbitrary data. Knowing the main options explains the
difference between acceptable and impractical lookups.

## Main Notes

- Linear search checks each element in order; it is O(n) and works on any
  data, sorted or not.
- Binary search repeatedly halves the search space and is O(log n), but it
  requires sorted data.
- Hash-based lookup finds an item in expected O(1) time but has no order and
  costs memory.
- Search trees keep items ordered and support O(log n) lookup plus sorted
  traversal.
- Binary search trades the cost of sorting (O(n log n)) for fast searches
  afterward.
- The right choice depends on access pattern: one search or millions, and
  whether data changes.
- Search complexity depends on the container, not only the algorithm.
- Graphs and other structures use specialized searches such as depth-first
  and breadth-first traversal.

## References

- Foundational concept; no single source.
- Standard topic in algorithm textbooks.

## Related Notes

- [[big-o-notation]]
- [[sorting-algorithms-overview]]

## Tags

This note is tagged in the front matter as algorithms, searching, complexity.

## Review History

- 2026-08-08: Created as a draft.
