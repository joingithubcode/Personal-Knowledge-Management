---
title: "dynamic-programming-basics"
status: draft
created: 2026-08-08
tags:
  - algorithms
  - optimization
  - problem-solving
related:
  - recursion-basics
---

# dynamic-programming-basics

## Purpose

Explain dynamic programming and how it turns exponential problems into fast
ones.

## Context

Some problems are built from overlapping subproblems: the same smaller
question appears again and again. Naive recursion recomputes them, wasting
time. Dynamic programming solves each subproblem once, stores the answer, and
reuses it, collapsing exponential work to polynomial.

## Main Notes

- Dynamic programming applies when a problem has optimal substructure and
  overlapping subproblems.
- Optimal substructure means the best solution builds from the best
  solutions of its parts.
- Overlapping subproblems means the same subproblem recurs, so storing
  results helps.
- Memoization (top-down) keeps recursion but caches each computed result.
- Tabulation (bottom-up) fills a table of subproblem answers in order, with
  no recursion.
- Classic examples are the Fibonacci sequence, coin change, and longest
  common subsequence.
- The key step is defining states and the transition between them.
- Dynamic programming trades space for time; the table size drives the
  memory cost.

## References

- Foundational concept; no single source.
- Standard topic in algorithm textbooks; attributed to Richard Bellman.

## Related Notes

- [[recursion-basics]]

## Tags

This note is tagged in the front matter as algorithms, optimization,
problem-solving.

## Review History

- 2026-08-08: Created as a draft.
