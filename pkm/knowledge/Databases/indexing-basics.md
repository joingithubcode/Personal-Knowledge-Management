---
title: "indexing-basics"
status: draft
created: 2026-08-08
tags:
  - databases
  - performance
  - querying
related:
  - query-optimization-basics
---

# indexing-basics

## Purpose

Explain what a database index is, how it speeds up queries, and its costs.

## Context

A table stores rows in no particular order, so finding a value can require
scanning every row. An index is a separate structure that maps key values to
their locations, letting the database skip most rows. Indexes trade extra
writes and storage for faster reads.

## Main Notes

- An index is built on one or more columns and stores sorted key values with
  pointers to the rows.
- B-tree indexes support range scans and ordered access; hash indexes support
  fast exact lookups.
- Lookups by an indexed column drop from a full table scan to roughly a
  logarithmic search.
- Composite indexes cover multiple columns; column order in the index matters
  for which queries it serves.
- Every write that touches an indexed column also updates the index, slowing
  inserts and updates.
- Indexes consume disk space and memory; keep only those that serve real query
  patterns.
- A primary key is indexed automatically because lookups by key must be fast.
- Query planners choose an index when the estimated cost beats a scan; the
  explain plan shows the choice.

## References

- Foundational concept; no single source.
- Covered in standard database textbooks such as those by Silberschatz,
  Korth, and Sudarshan.

## Related Notes

- [[query-optimization-basics]]

## Tags

This note is tagged in the front matter as databases, performance, querying.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
