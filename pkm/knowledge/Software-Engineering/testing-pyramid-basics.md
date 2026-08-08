---
title: "testing-pyramid-basics"
status: draft
created: 2026-08-08
tags:
  - software-engineering
  - testing
  - quality
related:
  - ci-cd-basics
---

# testing-pyramid-basics

## Purpose

Explain the testing pyramid and how test layers balance speed, cost, and
confidence.

## Context

Tests come in many sizes, from a single function to a whole running system.
Spending effort in the wrong layer wastes time and gives false confidence.
The testing pyramid describes a balanced shape: many fast, cheap unit tests
at the base, fewer integration tests in the middle, and a small number of
slow end-to-end tests at the top.

## Main Notes

- Unit tests exercise one small piece in isolation, typically a function or
  class; they are fast and cheap to write.
- Integration tests check that pieces work together, such as code against a
  database or a service.
- End-to-end tests drive the whole system as a user would; they give the most
  confidence and cost the most.
- The pyramid shape comes from cost: write many cheap tests and few
  expensive ones.
- Unit tests pinpoint failures quickly; a failing end-to-end test tells you
  only that something is broken.
- Tests at every layer complement each other; the layers are not
  interchangeable.
- Test scope should follow the system: choose a small number of full journeys
  plus broad unit coverage.
- Good tests are fast enough to run constantly, feeding CI and enabling safe
  refactoring.

## References

- Foundational concept; no single source.
- Introduced by Mike Cohn in "Succeeding with Agile", 2009.

## Related Notes

- [[ci-cd-basics]]

## Tags

This note is tagged in the front matter as software-engineering, testing,
quality.

## Review History

- 2026-08-08: Created as a draft.
