---
title: "rate-limiting-basics"
status: draft
created: 2026-08-08
tags:
  - system-design
  - api
  - reliability
related:
  - api-gateway-basics
---

# rate-limiting-basics

## Purpose

Explain rate limiting and how it protects services from overload and abuse.

## Context

Uncontrolled traffic can exhaust CPU, memory, or database connections and
take a service down, whether the flood comes from a bug, a misbehaving
client, or an attacker. Rate limiting caps how many requests a client can
make in a window, so the service stays responsive for everyone.

## Main Notes

- Rate limiting restricts the number of requests a client or key may make
  within a time window.
- It is usually enforced per client identity: API key, user, or IP address.
- Common algorithms: token bucket (steady allowance with bursts), fixed
  window (count per window), and sliding window (smooth boundary).
- When a client exceeds the limit, the service returns a 429 status and
  often a retry-after header.
- Rate limits protect shared resources: database queries, expensive
  computation, and third-party calls.
- Limits can be global or per endpoint, letting cheap endpoints be generous
  and costly ones strict.
- The limiter itself needs to be fast and shared, often in a gateway or a
  distributed store.
- Reasonable limits with clear error responses keep legitimate users working
  while stopping runaway traffic.

## References

- Foundational concept; no single source.
- Standard topic in API design and system design material.

## Related Notes

- [[api-gateway-basics]]

## Tags

This note is tagged in the front matter as system-design, api, reliability.

## Review History

- 2026-08-08: Created as a draft.
