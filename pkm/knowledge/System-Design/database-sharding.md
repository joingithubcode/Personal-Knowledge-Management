---
title: "database-sharding"
status: draft
created: 2026-08-08
tags:
  - system-design
  - databases
  - scalability
related:
  - horizontal-vs-vertical-scaling
---

# database-sharding

## Purpose

Explain database sharding and how it spreads data across multiple databases.

## Context

A single database eventually becomes a bottleneck: its storage fills, its
writes serialize, and one machine caps the capacity. Sharding splits the data
into parts called shards, each stored on its own database instance. The
database then scales out horizontally like the application servers around it.

## Main Notes

- Sharding partitions rows across several databases, each holding a subset.
- A shard key decides which database owns each row; the key must be chosen
  so reads and writes route predictably.
- Common schemes: range sharding (contiguous key ranges) and hash sharding
  (a hash of the key spreads rows evenly).
- Reads that hit one shard are fast; cross-shard queries and joins become
  expensive or impossible.
- The shard key choice is permanent in practice, because rebalancing and
  resharding is difficult.
- Hotspots form when the shard key concentrates traffic on one shard.
- Sharding adds complexity: the application must route by key, and
  transactions that span shards are hard to keep consistent.
- Exhaust simpler options first: indexes, read replicas, and caching, before
  committing to shards.

## References

- Foundational concept; no single source.
- Standard topic in database scaling and system design literature.

## Related Notes

- [[horizontal-vs-vertical-scaling]]

## Tags

This note is tagged in the front matter as system-design, databases,
scalability.

## Review History

- 2026-08-08: Created as a draft.
