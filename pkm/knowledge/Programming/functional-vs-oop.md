---
title: "functional-vs-oop"
status: draft
created: 2026-08-08
tags:
  - programming
  - paradigms
  - design
related:
  - oop-fundamentals
---

# functional-vs-oop

## Purpose

Contrast functional programming with object-oriented programming.

## Context

Different problems reward different ways of structuring code. Object-oriented
code organizes around objects with state; functional code organizes around
pure functions that transform data. Neither is better overall; each shapes
how state, flow, and reuse are handled.

## Main Notes

- Functional programming treats computation as applying functions to data.
- Pure functions give the same output for the same input and change nothing
  outside themselves, making them easy to test.
- Immutability means data is not modified; changes produce new values
  instead of mutating in place.
- Functions are first-class values: they can be passed, returned, and
  composed like data.
- OOP groups state and behavior in objects and often relies on mutation.
- Functional code favors explicit data flow and avoids hidden shared state.
- Modern languages mix the two: classes with functional methods, or
  functional cores with object interfaces.
- Pure functions and immutability simplify concurrency because there is no
  shared mutable state to race.

## References

- Foundational concept; no single source.
- Standard topic in programming paradigm literature.

## Related Notes

- [[oop-fundamentals]]

## Tags

This note is tagged in the front matter as programming, paradigms, design.

## Review History

- 2026-08-08: Created as a draft.
