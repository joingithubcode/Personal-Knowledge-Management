---
title: "oop-fundamentals"
status: draft
created: 2026-08-08
tags:
  - programming
  - object-oriented
  - design
related:
  - functional-vs-oop
  - solid-principles
---

# oop-fundamentals

## Purpose

Explain the core ideas of object-oriented programming and what they buy.

## Context

Programs grow beyond simple scripts, and scattered functions struggle to
manage state and change. Object-oriented programming organizes code around
objects: units that bundle data and the behavior that works on it. Four core
ideas shape most OOP code in Java, Python, C++, and others.

## Main Notes

- An object combines state (fields) with behavior (methods) for one concept.
- Encapsulation hides internal state behind an interface, so outside code
  cannot corrupt it.
- Abstraction exposes only what is needed, hiding implementation details.
- Inheritance lets a class take fields and methods from a parent class,
  sharing behavior across types.
- Polymorphism lets different classes respond to the same call in their own
  way, so callers use one interface.
- Classes are blueprints; objects are the instances created from them.
- Composition (holding another object) is often preferred over inheritance
  for flexibility.
- OOP is a tool, not a rule; its value depends on matching it to the
  problem.

## References

- Foundational concept; no single source.
- Standard topic in programming textbooks and object-oriented design
  literature.

## Related Notes

- [[functional-vs-oop]]
- [[solid-principles]]

## Tags

This note is tagged in the front matter as programming, object-oriented,
design.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
