---
title: "load-balancing-basics"
status: draft
created: 2026-08-08
tags:
  - system-design
  - scalability
  - infrastructure
related:
  - api-gateway-basics
  - horizontal-vs-vertical-scaling
---

# load-balancing-basics

## Purpose

Explain load balancing and how it spreads traffic across multiple servers.

## Context

Horizontal scaling adds servers, but those servers are only useful if work is
distributed among them. A load balancer sits in front of the servers, receives
requests, and routes each one to an available instance. It is the control
point for capacity, health, and failover.

## Main Notes

- A load balancer distributes incoming requests across a pool of servers.
- Common algorithms: round robin sends to each server in turn; least
  connections sends to the least busy; hashing pins a client to one server.
- Health checks remove failing servers from the pool so traffic avoids them.
- The balancer can also terminate TLS and offload work from the servers.
- Because clients connect to the balancer, servers can be added or removed
  without changing the client.
- Sticky sessions pin a user to one server, useful when state is held
  server-side, but they reduce the flexibility of the pool.
- Balancers work at the network/transport layer or the application layer;
  application-level balancers can route on URLs and headers.
- Load balancing applies to databases, caches, and services, not only web
  servers.

## References

- Foundational concept; no single source.
- Standard topic in system design and networking material.

## Related Notes

- [[api-gateway-basics]]
- [[horizontal-vs-vertical-scaling]]

## Tags

This note is tagged in the front matter as system-design, scalability,
infrastructure.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
