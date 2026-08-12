---
title: "redis-vs-rabbitmq-as-broker"
status: active
created: 2026-08-12
tags:
  - system-design
  - architecture
  - messaging
  - task-queues
related:
  - message-queues-basics
---

# redis-vs-rabbitmq-as-broker

## Purpose

Compare Redis and RabbitMQ as message brokers for task queues, such as those
used with Celery, and outline the general trade-off between them.

## Context

Task queues need a broker to move work from producers to workers. Redis is
often already in the stack as a cache, while RabbitMQ is a dedicated broker.
Both work, but they differ in delivery guarantees, routing, and operations.

## Main Notes

- Redis is an in-memory data store, often already in use for caching, so it
  can double as a broker through lists and pub/sub.
- As a broker, Redis has weaker delivery guarantees: no built-in
  acknowledgment and retry semantics as robust as a dedicated broker.
- Redis offers no advanced routing beyond simple list and pub/sub patterns.
- RabbitMQ is a dedicated AMQP message broker with exchanges and routing
  rules.
- RabbitMQ provides stronger delivery guarantees: acknowledgments and
  dead-letter queues.
- RabbitMQ costs an extra service to deploy and operate, with more
  operational complexity from the Erlang runtime and tuning.
- General trade-off: Redis is simpler when it is already in the stack and
  task delivery guarantees are not critical.
- RabbitMQ is preferred when routing complexity or strict delivery
  guarantees matter.
- This note is general knowledge about the trade-off, not a record of a
  specific project's decision.

## References

- Foundational concept; no single source.
- Standard topic in system design and messaging material.

## Related Notes

- [[message-queues-basics]]

## Tags

This note is tagged in the front matter as system-design, architecture,
messaging, task-queues.

## Review History

- 2026-08-12: Created as an active note.