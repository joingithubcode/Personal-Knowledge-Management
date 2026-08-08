---
title: "gradient-descent-basics"
status: draft
created: 2026-08-08
tags:
  - machine-learning
  - optimization
  - mathematics
related:
  - calculus-for-ml-basics
  - neural-networks-basics
---

# gradient-descent-basics

## Purpose

Explain gradient descent, the optimization method used to train most machine
learning models.

## Context

A model has parameters and a loss function that scores how wrong its
predictions are. Training means finding parameter values that minimize the
loss. Gradient descent does this by repeatedly stepping downhill along the
steepest direction of the loss surface.

## Main Notes

- The gradient of the loss points in the direction of steepest increase;
  gradient descent steps the opposite way.
- A learning rate controls step size: too large overshoots, too small
  crawls.
- Each step recomputes the loss gradient and updates the parameters.
- Batch gradient descent uses the whole dataset per step; stochastic
  gradient descent uses one sample; mini-batch sits between.
- Mini-batch is the practical default, balancing stability and speed.
- Local minima and plateaus can trap the search; momentum and adaptive
  methods (Adam) help escape them.
- Feature scaling matters: scaled features produce smoother, faster
  convergence.
- Training is iterative: run, inspect loss curves, and tune the learning
  rate and schedule.

## References

- Foundational concept; no single source.
- Standard topic in machine learning and optimization textbooks.

## Related Notes

- [[calculus-for-ml-basics]]
- [[neural-networks-basics]]

## Tags

This note is tagged in the front matter as machine-learning, optimization,
mathematics.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
