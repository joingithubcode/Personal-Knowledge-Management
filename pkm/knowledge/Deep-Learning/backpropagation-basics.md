---
title: "backpropagation-basics"
status: draft
created: 2026-08-08
tags:
  - deep-learning
  - training
  - mathematics
related:
  - neural-networks-basics
  - calculus-for-ml-basics
---

# backpropagation-basics

## Purpose

Explain backpropagation, the algorithm that trains neural networks.

## Context

A neural network has many weights, and training must adjust each one to
reduce error. Computing every weight's effect directly is impractical.
Backpropagation works backward through the network, applying the chain rule
to find how much each weight contributed to the loss, then supplies those
gradients to gradient descent.

## Main Notes

- Backpropagation computes the gradient of the loss with respect to every
  weight in the network.
- A forward pass runs the input through the network and records each
  layer's values.
- A backward pass propagates the error from the output back through the
  layers.
- The chain rule breaks the total derivative into a product of local
  derivatives at each layer.
- Each weight's gradient says how much increasing it would change the loss.
- Gradient descent then updates the weights in the direction that lowers the
  loss.
- Backpropagation reuses computed derivatives, so the cost scales with the
  network size rather than exploding.
- The name mixes "propagation" of errors backward with the chain rule from
  calculus.

## References

- Foundational concept; no single source.
- Introduced in early neural network literature; standard deep learning
  textbook topic.

## Related Notes

- [[neural-networks-basics]]
- [[calculus-for-ml-basics]]

## Tags

This note is tagged in the front matter as deep-learning, training,
mathematics.

## Review History

- 2026-08-08: Created as a draft.
