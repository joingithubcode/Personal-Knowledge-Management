---
title: "error-handling-patterns"
status: draft
created: 2026-08-08
tags:
  - programming
  - reliability
  - software-engineering
---

# error-handling-patterns

## Purpose

Explain the common ways programs handle errors and what each protects.

## Context

Programs fail: files are missing, networks drop, input is malformed. An
unhandled error crashes the program or corrupts state. Error handling is the
deliberate plan for what happens when things go wrong, and the mechanism
differs across languages.

## Main Notes

- Return codes make functions report success or failure as a value; callers
  must check it.
- Exceptions let an error unwind the call stack to a handler, skipping
  normal code paths.
- Throwing and catching separates the code that detects failure from the
  code that recovers.
- Every error should be caught at the layer that can act on it; swallowing
  errors hides real problems.
- Log errors with context (what, where, when) so failures are diagnosable.
- Failures need defined behavior: retry transient errors, abort invalid
  operations, and fail closed for safety.
- Resources must be released on both success and failure paths.
- Types can make failure explicit: results and option types force callers
  to handle the error case.

## References

- Foundational concept; no single source.
- Standard topic in programming and software reliability literature.

## Related Notes

No related notes yet.

## Tags

This note is tagged in the front matter as programming, reliability,
software-engineering.

## Review History

- 2026-08-08: Created as a draft.
