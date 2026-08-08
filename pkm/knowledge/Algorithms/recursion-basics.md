---
title: "recursion-basics"
status: draft
created: 2026-08-08
tags:
  - algorithms
  - programming
  - problem-solving
related:
  - dynamic-programming-basics
  - trees-basics
---

# recursion-basics

## Purpose

Explain recursion and when it is a natural fit for a problem.

## Context

Some problems are defined in terms of themselves: a folder contains folders,
a list is an item followed by a list. Recursion solves these by a function
calling itself on a smaller version of the problem. It mirrors how such
structures are defined and often produces the clearest solution.

## Main Notes

- A recursive function calls itself to solve a smaller instance of the same
  problem.
- Every recursive function needs a base case that stops the calls and a
  recursive case that moves toward it.
- Without a base case, recursion never stops and exhausts the call stack.
- Each call has its own local variables; the stack unwinds as calls return.
- Recursion suits tree, graph, and divide-and-conquer problems naturally.
- Every recursive solution has an iterative version, but recursion is often
  more readable for nested structures.
- Deep recursion can overflow the stack; languages with tail call
  optimization handle some cases iteratively.
- Costs to watch: repeated identical calls waste work unless results are
  stored (memoization).

## References

- Foundational concept; no single source.
- Standard topic in programming and algorithm textbooks.

## Related Notes

- [[dynamic-programming-basics]]
- [[trees-basics]]

## Tags

This note is tagged in the front matter as algorithms, programming,
problem-solving.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
