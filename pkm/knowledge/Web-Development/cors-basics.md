---
title: "cors-basics"
status: draft
created: 2026-08-08
tags:
  - web-development
  - security
  - http
related:
  - http-request-response-cycle
---

# cors-basics

## Purpose

Explain Cross-Origin Resource Sharing (CORS) and why browsers enforce it.

## Context

A browser page on one origin (scheme, host, and port) may want to read data
from another origin, such as an API at a different domain. By default the
browser blocks such cross-origin reads to stop malicious sites from
harvesting a user's data from other sites. CORS is the mechanism a server
uses to grant permission.

## Main Notes

- An origin is the combination of scheme, host, and port; the same host
  served over plain HTTP and over HTTPS counts as two different origins.
- Same-origin policy lets a page read responses only from its own origin;
  cross-origin reads are blocked unless the server opts in.
- CORS uses response headers, chiefly Access-Control-Allow-Origin, to say
  which origins may read the response.
- Simple requests (such as GET) pass with the allow-origin header alone.
- Preflight requests occur for requests that change data or use custom
  headers: the browser first sends an OPTIONS request asking permission, then
  the real request if approved.
- The server, not the browser, decides the policy; CORS is configured
  server-side and enforced browser-side.
- Credentials (cookies) require Access-Control-Allow-Credentials and an
  explicit, non-wildcard origin.
- CORS does not protect the server; it protects the user's browser session
  from other websites.

## References

- Foundational concept; no single source.
- CORS specified by the WHATWG Fetch standard.

## Related Notes

- [[http-request-response-cycle]]

## Tags

This note is tagged in the front matter as web-development, security, http.

## Review History

- 2026-08-08: Created as a draft.
