---
title: "jwt-authentication"
status: draft
created: 2026-08-08
tags:
  - security
  - authentication
  - web-development
related:
  - cookies-vs-sessions
  - oauth2-basics
  - rbac-fundamentals
---

# jwt-authentication

## Purpose

Explain JSON web tokens and how they carry authentication state in the token
itself.

## Context

Server-side sessions need the server to remember each user, which adds
state and lookup cost. A JSON web token (JWT) moves the state to the client:
a signed, self-contained token that proves who the user is. Servers can
verify the token without storing a session.

## Main Notes

- A JWT is an encoded token with three parts: a header, a payload, and a
  signature.
- The header names the signing algorithm; the payload carries claims such as
  user id and expiry.
- The signature is computed from header and payload with a secret key or
  private key, so tampering is detected.
- The server verifies the signature and checks the expiry on every request;
  it does not need to store session state.
- Tokens are sent by clients, usually in an Authorization header, and should
  never go into URLs.
- Because the token is signed but not encrypted by default, sensitive data
  must not be placed in the payload.
- Short expiry plus refresh tokens limits the damage if a token leaks.
- Weaknesses include revocation difficulty: a stolen token stays valid until
  it expires, so keep lifetimes short.

## References

- Foundational concept; no single source.
- JWT specified in IETF RFC 7519.

## Related Notes

- [[cookies-vs-sessions]]
- [[oauth2-basics]]
- [[rbac-fundamentals]]

## Tags

This note is tagged in the front matter as security, authentication,
web-development.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
