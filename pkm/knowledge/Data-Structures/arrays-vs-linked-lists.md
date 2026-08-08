---
title: "arrays-vs-linked-lists"
status: draft
created: 2026-08-08
tags:
  - data-structures
  - programming
  - performance
related:
  - big-o-notation
  - hash-tables-basics
  - stacks-vs-queues
---

# arrays-vs-linked-lists

## Purpose

Compare arrays and linked lists and the cost of common operations on each.

## Context

Programs need to store sequences of items, and the container chosen changes
how fast operations run. Arrays and linked lists are the two fundamental
ways to hold a sequence. Their difference is memory layout: contiguous slots
versus scattered nodes with pointers.

## Main Notes

- An array stores elements in contiguous memory and each element is indexed
  directly.
- A linked list stores nodes, each holding a value and a pointer to the next
  node.
- Array access by index is O(1); linked list access by position is O(n).
- Adding or removing at the end of an array is usually O(1), but inserting
  in the middle shifts elements, O(n).
- Linked lists add or remove at a known position in O(1) by rewiring
  pointers.
- Arrays waste little memory but need resizing when full; lists carry per-node
  pointer overhead.
- Arrays are cache-friendly because memory is contiguous; lists cause cache
  misses.
- In practice arrays dominate; lists shine only for frequent insertions away
  from the ends.

## References

- Foundational concept; no single source.
- Standard topic in data structure textbooks.

## Related Notes

- [[big-o-notation]]
- [[hash-tables-basics]]
- [[stacks-vs-queues]]

## Tags

This note is tagged in the front matter as data-structures, programming,
performance.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
