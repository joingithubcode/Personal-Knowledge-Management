---
title: "frontend-vs-backend"
status: draft
created: 2026-08-08
tags:
  - web-development
  - architecture
  - software-engineering
related:
  - client-server-model
  - javascript-event-loop
  - native-vs-cross-platform
  - php-basics
  - web-application-architecture
---

# frontend-vs-backend

## Purpose

Distinguish the frontend and backend parts of a web application and the work
each does.

## Context

Web applications split along a clear line: what the user sees and interacts
with, and everything that runs away from the user. Knowing which side a
problem belongs to guides where code, data, and security live.

## Main Notes

- The frontend runs in the user's browser and handles rendering and
  interaction: layout, styling, and in-page behavior.
- The backend runs on a server and handles business logic, validation,
  authentication, and data access.
- Frontend code uses web standards such as HTML, CSS, and JavaScript; modern
  frontends often use frameworks built on these.
- Backend code can be written in many languages (PHP, Python, JavaScript,
  Java) and talks to databases and other services.
- The two sides communicate over HTTP; the frontend sends requests and the
  backend returns responses, often JSON.
- Security boundaries matter: the browser exposes frontend code to users, so
  secrets and rules belong on the backend.
- A developer may work on one side or both; "full-stack" describes those who
  handle both.
- The split also exists in native mobile apps, where a local UI talks to a
  remote backend.

## References

- Foundational concept; no single source.
- Standard web development curricula and tutorials.

## Related Notes

- [[client-server-model]]
- [[javascript-event-loop]]
- [[native-vs-cross-platform]]
- [[php-basics]]
- [[web-application-architecture]]

## Tags

This note is tagged in the front matter as web-development, architecture,
software-engineering.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
