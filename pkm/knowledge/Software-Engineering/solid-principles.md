---
title: "solid-principles"
status: draft
created: 2026-08-08
tags:
  - software-engineering
  - design
  - object-oriented
related:
  - design-patterns-overview
  - oop-fundamentals
---

# solid-principles

## Purpose

Explain the SOLID principles and how they keep object-oriented code
maintainable.

## Context

Code that grows without discipline becomes hard to change: a fix in one place
breaks another, and features require editing old code. SOLID is a set of five
design principles that guide how classes and modules depend on each other,
making the code easier to extend and reason about.

## Main Notes

- Single responsibility: a class should have one reason to change, one
  clear job.
- Open/closed: code should be open for extension but closed for
  modification, adding behavior without rewriting existing code.
- Liskov substitution: a subclass must be usable wherever its base class is
  expected, without breaking behavior.
- Interface segregation: clients should not depend on interfaces they do not
  use; keep interfaces small and specific.
- Dependency inversion: depend on abstractions, not on concrete
  implementations, so high-level logic does not tie to low-level details.
- The principles reduce coupling and raise cohesion, which lowers the cost of
  change.
- They are guidance, not rules; applying them mechanically can add
  complexity that outweighs the benefit.
- SOLID pairs with design patterns, which are concrete solutions that follow
  these principles.

## References

- Foundational concept; no single source.
- Coined by Robert C. Martin; rooted in earlier object-oriented design work.

## Related Notes

- [[design-patterns-overview]]
- [[oop-fundamentals]]

## Tags

This note is tagged in the front matter as software-engineering, design,
object-oriented.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
