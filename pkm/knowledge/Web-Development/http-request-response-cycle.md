---
title: "http-request-response-cycle"
status: draft
created: 2026-08-08
tags:
  - networking
  - http
  - web-development
related:
  - client-server-model
  - cookies-vs-sessions
  - cors-basics
  - rest-api-basics
  - seo-fundamentals
  - web-security-headers
  - websockets-basics
---

# http-request-response-cycle

## Purpose

Explain how an HTTP request travels from client to server and returns as a
response.

## Context

HTTP is the protocol that powers the web. Every page load, API call, and
form submission is an HTTP exchange. Understanding the cycle reveals where
latency, caching, and errors come from.

## Main Notes

- The cycle starts with a client (browser or app) that builds a request
  message.
- A request has a method (GET, POST, PUT, DELETE), a target URL, headers,
  and optionally a body.
- DNS resolves the hostname to an IP address, then the request opens a TCP
  connection to the server.
- The server reads the request, runs the application, and builds a response
  message.
- A response has a status code (200 success, 404 not found, 500 server
  error), headers, and a body.
- Headers carry metadata: content type, caching rules, cookies, and security
  settings.
- Modern web uses HTTP/1.1 and HTTP/2 with persistent connections; HTTPS
  encrypts the whole exchange with TLS.
- The cycle repeats per resource; a page of many assets triggers many
  exchanges.

## References

- Foundational concept; no single source.
- HTTP defined in IETF RFC 9110 and RFC 9112.

## Related Notes

- [[client-server-model]]
- [[cookies-vs-sessions]]
- [[cors-basics]]
- [[rest-api-basics]]
- [[seo-fundamentals]]
- [[web-security-headers]]
- [[websockets-basics]]

## Tags

This note is tagged in the front matter as networking, http, web-development.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
