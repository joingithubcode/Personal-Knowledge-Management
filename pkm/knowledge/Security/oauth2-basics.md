---
title: "oauth2-basics"
status: draft
created: 2026-08-08
tags:
  - security
  - authentication
  - authorization
related:
  - jwt-authentication
---

# oauth2-basics

## Purpose

Explain OAuth 2.0 and how it lets applications access resources without
seeing a user's password.

## Context

An app often needs to act on a user's behalf at another service, such as
reading their calendar. Handing over the password is dangerous and grants
everything. OAuth 2.0 is an authorization framework where the resource owner
approves limited, revocable access, and the app receives a token it can use.

## Main Notes

- OAuth 2.0 grants access to resources on a user's behalf without the app
  receiving their credentials.
- The four roles are the resource owner (user), the client (app), the
  authorization server, and the resource server.
- The resource owner approves the client with a consent screen, which scopes
  what the client may do.
- The authorization server issues an access token; the client presents it to
  the resource server.
- Grant types cover different client situations; the authorization code
  grant is the standard flow for web apps.
- Scopes bound each token to specific permissions, so access is limited and
  reviewable.
- Access tokens expire and are refreshed; revoking the grant cuts off the
  client.
- OAuth authorizes access; identity and login itself come from OpenID
  Connect on top of it.

## References

- Foundational concept; no single source.
- OAuth 2.0 specified in IETF RFC 6749.

## Related Notes

- [[jwt-authentication]]

## Tags

This note is tagged in the front matter as security, authentication,
authorization.

## Review History

- 2026-08-08: Created as a draft.
