---
title: "websockets-basics"
status: draft
created: 2026-08-08
tags:
  - networking
  - real-time
  - web-development
related:
  - http-request-response-cycle
  - tcp-vs-udp
---

# websockets-basics

## Purpose

Explain WebSockets and how they give browsers a persistent, two-way channel.

## Context

HTTP is request-response: the server answers only when the client asks, so
the server cannot push updates on its own. Real-time features such as chat
and live scores need the server to send data unprompted. WebSockets provide a
long-lived connection where either side can send at any time.

## Main Notes

- WebSockets open a persistent connection between client and server.
- The connection starts with an HTTP handshake that upgrades to the
  WebSocket protocol.
- After the upgrade, both sides send messages freely without a new request
  per message.
- The full-duplex channel lets the server push events without the client
  polling.
- WebSockets fit chat, notifications, live games, and collaborative
  editing.
- Alternatives such as long polling and server-sent events push one-way;
  WebSockets are the bidirectional option.
- Each open socket holds resources and a connection, so they do not scale
  for free.
- Connection handling needs care: reconnects, heartbeats, and close events
  must be managed.

## References

- Foundational concept; no single source.
- WebSocket protocol in IETF RFC 6455.

## Related Notes

- [[http-request-response-cycle]]
- [[tcp-vs-udp]]

## Tags

This note is tagged in the front matter as networking, real-time,
web-development.

## Review History

- 2026-08-08: Created as a draft.
