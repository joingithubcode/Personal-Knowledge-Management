---
title: "common-web-vulnerabilities"
status: draft
created: 2026-08-08
tags:
  - security
  - web-development
  - vulnerabilities
related:
  - web-security-headers
---

# common-web-vulnerabilities

## Purpose

Describe the most common classes of web vulnerabilities and how to defend
against them.

## Context

Web applications face a predictable set of attack patterns that recur across
frameworks and languages. Most breaches come from a short list of flaws:
untrusted input reaching a dangerous place. Knowing the common classes helps
developers write code that does not introduce them.

## Main Notes

- Injection (SQL and others): attacker input is executed as commands because
  it is concatenated into queries; parameterized queries prevent it.
- Cross-site scripting (XSS): attacker scripts run in other users' browsers;
  escape output and validate input.
- Cross-site request forgery (CSRF): an attacker tricks a user's browser into
  sending a state-changing request; anti-CSRF tokens block it.
- Broken authentication and session management: weak passwords, leaked
  tokens, and poor session handling let attackers impersonate users.
- Sensitive data exposure: unencrypted data in transit or at rest leaks;
  use HTTPS and encrypt storage.
- Broken access control: users reach resources they should not, because
  authorization checks are missing.
- Security misconfiguration: default credentials, verbose errors, and
  missing hardening settings.
- The OWASP Top Ten is the standard reference list; defenses start with
  validating input, escaping output, and enforcing authorization.

## References

- OWASP Top Ten, Open Worldwide Application Security Project.

## Related Notes

- [[web-security-headers]]

## Tags

This note is tagged in the front matter as security, web-development,
vulnerabilities.

## Review History

- 2026-08-08: Created as a draft.
