---
title: "message-queues-basics"
status: draft
created: 2026-08-08
tags:
  - system-design
  - messaging
  - architecture
related:
  - celery-redis-workers
---

# message-queues-basics

## Purpose

Explain message queues and how they decouple parts of a system.

## Context

When one service must trigger work in another, a direct synchronous call can
chain failures and force the caller to wait. A message queue sits between
them: the producer publishes a message, and a consumer processes it later.
This decoupling smooths spikes and isolates services from each other.

## Main Notes

- A message queue is a buffer where producers publish messages that
  consumers pull and process.
- The producer does not wait for the consumer; the queue absorbs the
  difference in speed between them.
- Queues let a system handle traffic spikes: messages pile up and drain
  at the consumer's pace.
- They decouple services, so a temporary consumer outage does not fail the
  producer's request.
- Common guarantees: at-least-once delivery (with duplicates possible) and
  ordering within a partition.
- Consumers should be idempotent, since at-least-once delivery can repeat a
  message.
- Queues also balance load: multiple consumers split the work from one
  queue.
- Dead-letter queues capture messages that repeatedly fail, for later
  inspection.

## References

- Foundational concept; no single source.
- Standard topic in distributed systems and system design material.

## Related Notes

- [[celery-redis-workers]]

## Tags

This note is tagged in the front matter as system-design, messaging,
architecture.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
