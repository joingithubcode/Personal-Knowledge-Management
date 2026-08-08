---
title: "stacks-vs-queues"
status: draft
created: 2026-08-08
tags:
  - data-structures
  - programming
  - algorithms
related:
  - arrays-vs-linked-lists
---

# stacks-vs-queues

## Purpose

Explain stacks and queues and the ordering rules each enforces.

## Context

Many algorithms need a way to hold items and process them in a strict order.
Two simple containers do this. A stack processes the newest item first; a
queue processes the oldest first. Choosing the wrong order breaks the
algorithm, so the distinction matters.

## Main Notes

- A stack is last in, first out (LIFO): the most recently added item is
  removed first.
- A queue is first in, first out (FIFO): the oldest item is removed first.
- Stack operations are push (add) and pop (remove); both act at the top.
- Queue operations are enqueue (add at the back) and dequeue (remove from
  the front).
- Stacks power function call history, undo features, and parsing.
- Queues power task processing, breadth-first search, and buffers.
- Both can be built on arrays or linked lists; the choice trades memory and
  resize behavior.
- A deque allows adding and removing at both ends, mixing the two roles.

## References

- Foundational concept; no single source.
- Standard topic in data structure textbooks.

## Related Notes

- [[arrays-vs-linked-lists]]

## Tags

This note is tagged in the front matter as data-structures, programming,
algorithms.

## Review History

- 2026-08-08: Created as a draft.
