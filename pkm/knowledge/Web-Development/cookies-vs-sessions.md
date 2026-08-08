---
title: "cookies-vs-sessions"
status: draft
created: 2026-08-08
tags:
  - web-development
  - authentication
  - state-management
related:
  - http-request-response-cycle
  - jwt-authentication
---

# cookies-vs-sessions

## Purpose

Distinguish cookies from sessions and explain how they keep a user logged in
across HTTP requests.

## Context

HTTP is stateless; the server treats each request as new. To recognize a
returning user, the server must remember something between requests. Cookies
and sessions are the two halves of that mechanism: the cookie is what the
browser holds, the session is the state the server keeps.

## Main Notes

- A cookie is a small piece of data the server sets and the browser stores
  and sends back with every request to that domain.
- A session is server-side state tied to one user, typically held in memory,
  a database, or a cache, and identified by an id.
- The common pattern: the server creates a session, puts its id in a cookie,
  and later looks up the session from the id in each request.
- Cookies can also hold small data directly, but sensitive data belongs in
  the session, not the cookie.
- Session ids are random, unguessable values; they must not reveal user
  identity.
- Security attributes matter: HttpOnly keeps scripts from reading the cookie,
  Secure sends it only over HTTPS, and SameSite limits cross-site sending.
- Sessions expire after inactivity; cookies carry an expiration date of
  their own.
- Alternatives like JSON web tokens move state to the client instead of the
  server.

## References

- Foundational concept; no single source.
- Cookie behavior specified in IETF RFC 6265.

## Related Notes

- [[http-request-response-cycle]]
- [[jwt-authentication]]

## Tags

This note is tagged in the front matter as web-development, authentication,
state-management.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
