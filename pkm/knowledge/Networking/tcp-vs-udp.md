---
title: "tcp-vs-udp"
status: draft
created: 2026-08-08
tags:
  - networking
  - protocols
  - transport
related:
  - dns-basics
  - http-vs-https
  - osi-model-basics
  - websockets-basics
---

# tcp-vs-udp

## Purpose

Compare TCP and UDP, the two main transport protocols, and when each fits.

## Context

Once data is routed across a network, something must deliver it between
applications. TCP and UDP do this in opposite ways. TCP guarantees reliable,
ordered delivery; UDP sends datagrams with no guarantees. The trade-off is
speed and simplicity against reliability.

## Main Notes

- TCP (Transmission Control Protocol) provides reliable, ordered, connection
  based delivery.
- TCP establishes a connection, numbers packets, retransmits lost ones, and
  reorders arrivals.
- UDP (User Datagram Protocol) sends datagrams with no connection, no
  ordering, and no retransmission.
- TCP suits web, email, and file transfer where every byte must arrive
  intact.
- UDP suits streaming, voice, gaming, and DNS where speed matters more than
  perfect delivery.
- TCP has more overhead and can block on retransmission; UDP adds little
  latency.
- Both run on IP and use port numbers to reach the right application.
- Some applications build their own reliability on UDP to control latency
  and loss behavior.

## References

- Foundational concept; no single source.
- TCP in IETF RFC 9293; UDP in IETF RFC 768.

## Related Notes

- [[dns-basics]]
- [[http-vs-https]]
- [[osi-model-basics]]
- [[websockets-basics]]

## Tags

This note is tagged in the front matter as networking, protocols, transport.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
