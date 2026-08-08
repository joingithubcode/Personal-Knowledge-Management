---
title: "web-security-headers"
status: draft
created: 2026-08-08
tags:
  - security
  - http
  - web-development
related:
  - common-web-vulnerabilities
  - http-request-response-cycle
---

# web-security-headers

## Purpose

List the most important HTTP response headers that harden a web application.

## Context

A server can attach headers to every response that tell the browser how to
behave. Security headers reduce the attack surface by disabling risky
features and restricting what a page may do. They are cheap to set and
require no code changes in the page itself.

## Main Notes

- Content-Security-Policy restricts which sources scripts, styles, and other
  content may load, limiting cross-site scripting.
- X-Content-Type-Options: nosniff stops the browser from guessing a file's
  type, blocking certain injection tricks.
- Strict-Transport-Security forces the browser to use HTTPS only for the
  domain.
- X-Frame-Options or frame-ancestors in the CSP stops the page being embedded
  in another site (clickjacking).
- Referrer-Policy controls how much of the URL leaks in the Referer header on
  navigation.
- Permissions-Policy limits which browser features (camera, microphone) the
  page can use.
- Cache-Control: no-store keeps sensitive responses out of browser and proxy
  caches.
- Headers are defense in depth: they help, but they do not replace secure
  code, input validation, and authentication.

## References

- Foundational concept; no single source.
- Documented by standards bodies and security references such as OWASP
  Secure Headers Project.

## Related Notes

- [[common-web-vulnerabilities]]
- [[http-request-response-cycle]]

## Tags

This note is tagged in the front matter as security, http, web-development.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
