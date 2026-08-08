---
title: "caching-strategies"
status: draft
created: 2026-08-08
tags:
  - system-design
  - performance
  - architecture
related:
  - cdn-basics
  - elevenlabs-voiceid-caching-sidecar
---

# caching-strategies

## Purpose

Explain caching and the strategies for keeping cached data correct and fresh.

## Context

Reading data is far cheaper when it comes from fast local memory than from a
database or a remote service. Caching stores copies of expensive results so
repeated requests skip the slow path. The hard part is deciding when a cache
is stale, which is what the strategies address.

## Main Notes

- A cache keeps copies of data so repeated reads avoid the original source.
- Cache-aside: the application reads the cache, fills it on a miss, and
  writes through on updates; it is simple and popular.
- Write-through: writes update the cache and the store together, keeping the
  cache always warm but adding write latency.
- Write-back: writes land in the cache and flush to the store later,
  fast but risky on failure.
- TTL (time to live) expires entries after a set period, bounding staleness.
- Invalidation removes entries when the source data changes, giving
  stronger freshness.
- Cache keys must match the data; a key layout mistake silently serves wrong
  data.
- The big wins come from caching stable, expensive, read-heavy data; caching
  volatile data adds risk for little gain.

## References

- Foundational concept; no single source.
- Standard topic in system design literature.

## Related Notes

- [[cdn-basics]]
- [[elevenlabs-voiceid-caching-sidecar]]

## Tags

This note is tagged in the front matter as system-design, performance,
architecture.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
