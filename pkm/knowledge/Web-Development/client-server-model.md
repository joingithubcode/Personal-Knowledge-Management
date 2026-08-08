---
title: "client-server-model"
status: draft
created: 2026-08-08
tags:
  - networking
  - architecture
  - web-development
related:
  - frontend-vs-backend
  - http-request-response-cycle
  - web-application-architecture
---

# client-server-model

## Purpose

Explain the client-server model, the request-response pattern that most
networked applications use.

## Context

Applications that talk over a network need a way to divide work. The
client-server model splits participants into clients that ask for services
and servers that provide them. It underlies the web, email, file sharing,
and most database and API traffic.

## Main Notes

- A client initiates requests; a server listens and responds to them.
- One server can serve many clients, and each client can talk to many
  servers.
- Clients are often user devices or programs; servers are usually dedicated
  machines running continuous services.
- The server typically holds shared state and enforces access rules; clients
  hold only their own context.
- Requests and responses travel over a protocol such as HTTP, which both
  sides must speak.
- Communication is usually request-response: the client waits while the
  server processes and answers.
- The model scales by adding servers behind a load balancer and by keeping
  servers stateless where possible.
- Alternatives exist, such as peer-to-peer, but client-server dominates
  because it centralizes control and data.

## References

- Foundational concept; no single source.
- Described in distributed systems and networking textbooks.

## Related Notes

- [[frontend-vs-backend]]
- [[http-request-response-cycle]]
- [[web-application-architecture]]

## Tags

This note is tagged in the front matter as networking, architecture,
web-development.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
