---
title: "technical-debt"
status: draft
created: 2026-08-08
tags:
  - software-engineering
  - maintenance
  - quality
---

# technical-debt

## Purpose

Explain technical debt and how to manage it deliberately instead of
accumulating it blindly.

## Context

Rushing a feature with shortcuts makes today's deadline but often costs more
later: future changes are slower and buggier because the code fights the
developers. Technical debt names this trade-off between speed now and cost
later. Like financial debt, it is sometimes worth taking, but it must be
tracked and repaid.

## Main Notes

- Technical debt is the future cost of shortcuts taken in the present.
- It shows up as duplicated code, missing tests, unclear names, and
  deferred fixes.
- Debt slows new features and raises the chance of bugs as the codebase
  grows.
- Some debt is strategic: ship the quick version to learn before investing.
- Accidental debt from carelessness or pressure is rarely worth it.
- Debt must be visible to be repaid; track it in the backlog like other
  work.
- Refactoring repays debt by improving structure without changing behavior.
- The goal is not zero debt but a conscious balance: take it knowingly,
  list it, and schedule repayment.

## References

- Foundational concept; no single source.
- Term popularized by Ward Cunningham; widely discussed in software
  engineering literature.

## Related Notes

No related notes yet.

## Tags

This note is tagged in the front matter as software-engineering,
maintenance, quality.

## Review History

- 2026-08-08: Created as a draft.
