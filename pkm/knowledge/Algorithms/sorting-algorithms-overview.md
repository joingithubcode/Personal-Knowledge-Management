---
title: "sorting-algorithms-overview"
status: draft
created: 2026-08-08
tags:
  - algorithms
  - sorting
  - complexity
related:
  - big-o-notation
  - searching-algorithms-overview
---

# sorting-algorithms-overview

## Purpose

Survey common sorting algorithms and how their behavior and complexity
differ.

## Context

Sorting is a fundamental operation that many other algorithms rely on, from
searching to merging data. No single sort fits every situation: algorithms
differ in average and worst-case speed, memory use, and stability. Choosing
well depends on the data and the constraints.

## Main Notes

- Bubble sort repeatedly swaps neighbors and is O(n squared); it is simple
  to teach but slow.
- Insertion sort builds a sorted portion one item at a time; it is O(n
  squared) on average but fast on nearly sorted data.
- Selection sort picks the smallest remaining element each pass; it is
  O(n squared) with a fixed number of swaps.
- Merge sort divides, sorts, and merges; it is O(n log n) in all cases but
  needs extra memory.
- Quick sort partitions around a pivot and averages O(n log n), with the
  worst case avoidable by good pivot choice.
- Heap sort is O(n log n) and sorts in place.
- Stability matters: a stable sort keeps equal items in their original
  order, which matters when sorting by several keys.
- Libraries use hybrid sorts that switch strategies by data size.

## References

- Foundational concept; no single source.
- Standard topic in algorithm textbooks.

## Related Notes

- [[big-o-notation]]
- [[searching-algorithms-overview]]

## Tags

This note is tagged in the front matter as algorithms, sorting, complexity.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
