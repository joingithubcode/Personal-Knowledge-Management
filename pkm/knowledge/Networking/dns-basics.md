---
title: "dns-basics"
status: draft
created: 2026-08-08
tags:
  - networking
  - dns
  - infrastructure
related:
  - tcp-vs-udp
---

# dns-basics

## Purpose

Explain the Domain Name System and how names become addresses.

## Context

People remember names, but computers need numbers. The Domain Name System
(DNS) translates hostnames such as example.com into the IP addresses that
routing uses. It is a distributed, hierarchical directory that every web
request depends on, so failures there break everything.

## Main Notes

- DNS maps human-readable domain names to IP addresses.
- The system is hierarchical: root servers, top-level domains, and
  authoritative name servers for each domain.
- A resolver asks a chain of servers until it finds the address for a name.
- Records come in types: A and AAAA hold IPv4 and IPv6 addresses; CNAME
  aliases names; MX directs email.
- Results are cached with a time to live (TTL), trading freshness for
  speed.
- DNS usually runs over UDP, falling back to TCP for large responses.
- DNS itself is only as reliable as its configuration; DNSSEC adds
  signature verification.
- A single lookup can involve several servers, but caching keeps typical
  lookups fast.

## References

- Foundational concept; no single source.
- DNS specified in IETF RFC 1035.

## Related Notes

- [[tcp-vs-udp]]

## Tags

This note is tagged in the front matter as networking, dns, infrastructure.

## Review History

- 2026-08-08: Created as a draft.
