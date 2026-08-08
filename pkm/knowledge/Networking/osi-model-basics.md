---
title: "osi-model-basics"
status: draft
created: 2026-08-08
tags:
  - networking
  - protocols
  - models
related:
  - tcp-vs-udp
---

# osi-model-basics

## Purpose

Explain the OSI model and how it organizes networking into layers.

## Context

Networking involves many separate jobs: sending bits on a cable, finding
addresses, and interpreting application messages. The OSI model splits these
into seven layers so each concern is handled independently. It is a
reference model for understanding, while the internet itself runs on the
simpler TCP/IP stack.

## Main Notes

- The OSI model has seven layers, from the physical medium up to the
  application.
- Layer 1 physical carries raw bits; layer 2 data link frames data between
  directly connected devices.
- Layer 3 network routes packets across networks using IP addresses.
- Layer 4 transport manages end-to-end delivery, with TCP and UDP as the
  main protocols.
- Layer 5 session manages connections; layer 6 presentation handles
  encoding and encryption.
- Layer 7 application is where users interact, via protocols like HTTP, DNS,
  and email.
- Each layer uses the one below it and serves the one above it.
- The internet model compresses this to four layers, but OSI is the standard
  teaching model for reasoning about networks.

## References

- Foundational concept; no single source.
- OSI model standardized by ISO/IEC 7498.

## Related Notes

- [[tcp-vs-udp]]

## Tags

This note is tagged in the front matter as networking, protocols, models.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
