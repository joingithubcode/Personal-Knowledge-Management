---
title: "cdn-basics"
status: draft
created: 2026-08-08
tags:
  - cloud
  - networking
  - performance
related:
  - caching-strategies
---

# cdn-basics

## Purpose

Explain content delivery networks and how they bring content closer to users.

## Context

The physical distance between a user and a server adds real latency, and one
origin server can be overwhelmed by global traffic. A content delivery
network (CDN) places cached copies of content on many servers around the
world. Users fetch from the nearest one, so loads are faster and the origin
stays cheap to run.

## Main Notes

- A CDN is a network of edge servers that cache and serve content from
  locations near users.
- The CDN chooses the closest edge server to each user, often using DNS to
  route them.
- Static assets such as images, scripts, and styles load faster and put no
  load on the origin.
- The CDN caches responses with rules; the origin stays the source of truth
  and is hit only on cache misses.
- CDNs also shield the origin from traffic spikes and attacks such as DDoS.
- Dynamic content can use edge computing, running logic near the user
  instead of round-tripping to the origin.
- Cache invalidation matters: updated content must be purged or given new
  versions.
- HTTPS terminates at the edge, with certificates managed by the CDN.

## References

- Foundational concept; no single source.
- Standard topic in networking and web performance literature.

## Related Notes

- [[caching-strategies]]

## Tags

This note is tagged in the front matter as cloud, networking, performance.

## Review History

- 2026-08-08: Created as a draft.
