---
title: "horizontal-vs-vertical-scaling"
status: draft
created: 2026-08-08
tags:
  - system-design
  - scalability
  - infrastructure
related:
  - database-sharding
  - load-balancing-basics
---

# horizontal-vs-vertical-scaling

## Purpose

Explain the two ways to add capacity to a system and when each is used.

## Context

When a system runs out of capacity, it can grow in two directions. Vertical
scaling adds power to the existing machine; horizontal scaling adds more
machines. The choice shapes the architecture, cost, and reliability of the
whole system.

## Main Notes

- Vertical scaling increases a single machine's resources: CPU, memory, or
  disk.
- Horizontal scaling adds more machines working in parallel behind a load
  balancer.
- Vertical scaling is simple to set up because the code is unchanged, but it
  hits a hardware ceiling and creates a single point of failure.
- Horizontal scaling is limited by software: the application must be
  stateless enough for any instance to handle any request.
- Databases are harder to scale horizontally; sharding or read replicas are
  needed.
- Horizontal scaling also brings resilience: losing one instance keeps the
  service running.
- Cloud instances blur the line, since you can resize or replicate with a
  setting.
- Mature systems typically scale out (horizontally) for compute and accept
  some vertical scaling where it is unavoidable.

## References

- Foundational concept; no single source.
- Standard topic in system design and infrastructure material.

## Related Notes

- [[database-sharding]]
- [[load-balancing-basics]]

## Tags

This note is tagged in the front matter as system-design, scalability,
infrastructure.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
