---
title: "monolith-vs-microservices"
status: draft
created: 2026-08-08
tags:
  - architecture
  - system-design
  - software-engineering
related:
  - api-gateway-basics
  - web-application-architecture
---

# monolith-vs-microservices

## Purpose

Compare monolithic and microservice architectures and the trade-offs between
them.

## Context

A codebase can be shipped as one application or as many small services. The
monolith keeps everything in a single deployable unit; microservices split
the system into independently deployable services. The right choice depends
on team, scale, and operational maturity, not on fashion.

## Main Notes

- A monolith is one application that handles all features, usually with one
  codebase and one deployment.
- Microservices split features into small services, each with its own
  process, data, and deployment lifecycle.
- Monoliths are simpler to build, test, and reason about at small scale;
  development, deployment, and debugging are straightforward.
- Monoliths strain at scale: a change to one part needs the whole app
  deployed, and teams conflict on one codebase.
- Microservices scale independently, isolate failures, and let teams own
  separate services and release on their own cadence.
- Microservices add cost: distributed debugging, network latency, data
  consistency, and much more operational surface.
- A common path is to start with a monolith and split services only when
  concrete pain justifies it.
- Modular monoliths keep the simplicity while enforcing boundaries inside one
  deployable.

## References

- Foundational concept; no single source.
- Widely discussed in software architecture literature.

## Related Notes

- [[api-gateway-basics]]
- [[web-application-architecture]]

## Tags

This note is tagged in the front matter as architecture, system-design,
software-engineering.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
