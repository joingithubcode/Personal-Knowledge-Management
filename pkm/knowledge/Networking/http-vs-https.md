---
title: "http-vs-https"
status: draft
created: 2026-08-08
tags:
  - networking
  - security
  - http
related:
  - tcp-vs-udp
  - encryption-basics
---

# http-vs-https

## Purpose

Explain the difference between HTTP and HTTPS and why encryption matters.

## Context

HTTP is the protocol that moves web traffic, but it sends everything in
plain text. Anyone on the path can read or modify it. HTTPS is HTTP wrapped
in TLS encryption, so the traffic is confidential, authentic, and
tamper-evident. Modern web treats HTTPS as the default.

## Main Notes

- HTTP carries web requests and responses in plain text over TCP.
- HTTPS is HTTP layered on TLS (Transport Layer Security), which encrypts the
  traffic.
- Encryption keeps content secret from anyone who can observe the network
  path.
- TLS verifies the server's identity through certificates, so clients know
  they are talking to the real site.
- Integrity checking in TLS detects if data was changed in transit.
- HTTPS protects everything the URL and page reveal, including logins,
  cookies, and form data.
- Sites without HTTPS are flagged and rank lower; certificates are
  available at no cost.
- HTTPS adds a small handshake cost, largely hidden by connection reuse and
  modern TLS.

## References

- Foundational concept; no single source.
- HTTP defined in IETF RFC 9110; TLS in IETF RFC 8446.

## Related Notes

- [[tcp-vs-udp]]
- [[encryption-basics]]

## Tags

This note is tagged in the front matter as networking, security, http.

## Review History

- 2026-08-08: Created as a draft.
