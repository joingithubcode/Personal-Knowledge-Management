---
title: "big-o-notation"
status: draft
created: 2026-08-08
tags:
  - algorithms
  - complexity
  - performance
related:
  - arrays-vs-linked-lists
  - searching-algorithms-overview
  - sorting-algorithms-overview
  - technical-interview-preparation
---

# big-o-notation

## Purpose

Explain big-O notation and how it describes how fast an algorithm grows.

## Context

An algorithm's speed matters more as the input grows. Big-O notation measures
how resource use scales with input size, ignoring constants and small cases.
It answers a design question: will this still be fast at ten million items,
or does the work explode?

## Main Notes

- Big-O describes the upper bound of growth: how time or space scales with
  input size n.
- It drops constants and lower-order terms, so 3n plus 5 is still O(n).
- Common classes from best to worst: O(1) constant, O(log n) logarithmic,
  O(n) linear, O(n log n), O(n squared), O(2 to the n) exponential.
- O(1) means the work does not grow with input, like reading an array by
  index.
- O(log n) grows slowly, like binary search halving the search space.
- O(n squared) and worse become impractical quickly at large n.
- Time and space complexity are both considered; trade-offs between them
  are common.
- Big-O is a guide to scaling behavior, not a precise timer; real speed
  still depends on constants and hardware.

## References

- Foundational concept; no single source.
- Standard topic in algorithm textbooks.

## Related Notes

- [[arrays-vs-linked-lists]]
- [[searching-algorithms-overview]]
- [[sorting-algorithms-overview]]
- [[technical-interview-preparation]]

## Tags

This note is tagged in the front matter as algorithms, complexity,
performance.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
