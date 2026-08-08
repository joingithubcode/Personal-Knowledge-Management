---
title: "hash-tables-basics"
status: draft
created: 2026-08-08
tags:
  - data-structures
  - performance
  - programming
related:
  - arrays-vs-linked-lists
---

# hash-tables-basics

## Purpose

Explain hash tables and why they make lookups nearly instant.

## Context

Finding an item by its key is the most common operation in programs, from
user ids to settings names. A hash table stores key-value pairs so a key maps
directly to its location. A hash function computes where the value lives,
giving lookups that cost about O(1) on average.

## Main Notes

- A hash table stores pairs of keys and values and looks up by key.
- A hash function turns a key into a bucket index, an array position.
- Lookup, insert, and delete are about O(1) on average when collisions are
  rare.
- Collisions happen when two keys hash to the same bucket; chaining stores
  several entries per bucket.
- Open addressing handles collisions by probing for the next free slot.
- A load factor measures how full the table is; high load means more
  collisions, so the table grows by resizing.
- Hash functions must be fast and spread keys evenly; weak hashes cause
  clustering and slowdowns.
- A good hash function is crucial: insertion order does not matter, and
  worst-case behavior degrades to O(n).

## References

- Foundational concept; no single source.
- Standard topic in data structure textbooks.

## Related Notes

- [[arrays-vs-linked-lists]]

## Tags

This note is tagged in the front matter as data-structures, performance,
programming.

## Review History

- 2026-08-08: Created as a draft.
