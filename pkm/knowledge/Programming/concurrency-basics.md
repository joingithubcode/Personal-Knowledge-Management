---
title: "concurrency-basics"
status: draft
created: 2026-08-08
tags:
  - programming
  - concurrency
  - performance
---

# concurrency-basics

## Purpose

Explain concurrency and the mechanisms programs use to do several things at
once.

## Context

Modern programs handle many tasks at once: serving requests, processing
uploads, animating the UI. Doing them sequentially wastes time. Concurrency
lets a program make progress on multiple things, using threads, processes,
or async code. The benefit comes with the risk of shared-state races.

## Main Notes

- Concurrency means making progress on multiple tasks, which is not the same
  as running them simultaneously on separate cores.
- Threads are lightweight units of execution within one process, sharing
  memory.
- Processes are separate programs with isolated memory, communicating
  through defined channels.
- Asynchronous code overlaps waiting: while one operation waits on I/O,
  others run, often in a single thread.
- Parallelism is running tasks on multiple cores at the same time; it needs
  concurrency but concurrency does not need it.
- Shared mutable state causes races: interleaved updates produce wrong
  results, so locks or immutable data are needed.
- Locks protect critical sections but risk deadlock when held in the wrong
  order.
- Most bugs come from coordination, not from the concurrency itself; prefer
  message passing and immutability.

## References

- Foundational concept; no single source.
- Standard topic in operating systems and programming literature.

## Related Notes

No related notes yet.

## Tags

This note is tagged in the front matter as programming, concurrency,
performance.

## Review History

- 2026-08-08: Created as a draft.
