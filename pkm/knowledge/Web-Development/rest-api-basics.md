---
title: "rest-api-basics"
status: draft
created: 2026-08-08
tags:
  - api-design
  - http
  - web-development
related:
  - http-request-response-cycle
---

# rest-api-basics

## Purpose

Explain what a REST API is and the conventions that make it predictable.

## Context

Applications share data over HTTP using APIs. REST (Representational State
Transfer) is a widely used style that organizes an API around resources.
Following its conventions makes an interface intuitive for every client that
consumes it.

## Main Notes

- A REST API exposes resources, each identified by a URL, such as
  /users/42.
- HTTP methods map to operations: GET reads, POST creates, PUT or PATCH
  updates, DELETE removes.
- Requests and responses usually carry JSON; content-type headers describe
  the format.
- REST APIs are stateless: each request carries all the context the server
  needs, and no client state is kept between calls.
- Responses use meaningful status codes to signal success or failure.
- Resource names are nouns, plural, and lowercase; URLs never embed verbs or
  actions.
- Nesting shows relationships (a user's posts under /users/1/posts), but
  flat top-level collections keep URLs simple.
- Versioning the API (for example /v1/) protects existing clients when the
  contract changes.

## References

- Foundational concept; no single source.
- REST described by Roy Fielding in his 2000 doctoral dissertation.

## Related Notes

- [[http-request-response-cycle]]

## Tags

This note is tagged in the front matter as api-design, http, web-development.

## Review History

- 2026-08-08: Created as a draft.
