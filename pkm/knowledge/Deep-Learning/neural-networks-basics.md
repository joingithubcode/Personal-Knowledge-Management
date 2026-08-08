---
title: "neural-networks-basics"
status: draft
created: 2026-08-08
tags:
  - deep-learning
  - machine-learning
  - neural-networks
related:
  - backpropagation-basics
  - cnn-vs-rnn
  - gradient-descent-basics
  - transformer-architecture
---

# neural-networks-basics

## Purpose

Explain the structure of a neural network and how it learns.

## Context

Some patterns are too complex for hand-written rules, and simpler models
struggle with rich data such as images and text. Neural networks learn such
patterns from examples. They are layers of simple units whose connections are
adjusted during training until the network maps inputs to correct outputs.

## Main Notes

- A neural network is made of layers of units called neurons, each computing
  a weighted sum plus an activation.
- Connections carry weights; the network's behavior is stored in these
  weights.
- Activations add nonlinearity, letting the network model patterns that a
  plain line cannot.
- An input flows forward through the layers to produce a prediction.
- Training compares the prediction with the true answer using a loss
  function.
- Backpropagation computes how each weight caused the error, and gradient
  descent updates the weights to reduce it.
- Layers give depth: early layers find simple features and later layers
  combine them.
- More data and computation generally improve these networks, which is why
  they dominate modern AI.

## References

- Foundational concept; no single source.
- Standard topic in deep learning textbooks.

## Related Notes

- [[backpropagation-basics]]
- [[cnn-vs-rnn]]
- [[gradient-descent-basics]]
- [[transformer-architecture]]

## Tags

This note is tagged in the front matter as deep-learning, machine-learning,
neural-networks.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
