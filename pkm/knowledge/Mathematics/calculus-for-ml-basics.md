---
title: "calculus-for-ml-basics"
status: draft
created: 2026-08-08
tags:
  - mathematics
  - machine-learning
  - optimization
related:
  - backpropagation-basics
  - gradient-descent-basics
---

# calculus-for-ml-basics

## Purpose

Explain the calculus concepts that machine learning training depends on.

## Context

Training a model means reducing a loss value, and reducing it requires
knowing which direction lowers it. Calculus provides that answer: derivatives
measure how a change in one variable changes the output. Gradient descent,
the workhorse of training, is built directly on this idea.

## Main Notes

- A derivative measures the rate of change of a function at a point, its
  slope.
- The gradient is the vector of partial derivatives, pointing in the
  direction of steepest increase.
- Gradient descent moves parameters in the opposite direction of the
  gradient to reduce the loss.
- The chain rule computes derivatives through composed functions, which is
  how error flows through layered models.
- Backpropagation uses the chain rule to compute gradients for every weight
  in a neural network.
- Derivatives find minima where the slope is zero, but loss surfaces need
  iterative search, not just solving.
- Partial derivatives isolate how one input affects the output while others
  stay fixed.
- Calculus also appears in probability as densities and in statistics as
  continuous expectation.

## References

- Foundational concept; no single source.
- Standard topic in calculus and machine learning textbooks.

## Related Notes

- [[backpropagation-basics]]
- [[gradient-descent-basics]]

## Tags

This note is tagged in the front matter as mathematics, machine-learning,
optimization.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
