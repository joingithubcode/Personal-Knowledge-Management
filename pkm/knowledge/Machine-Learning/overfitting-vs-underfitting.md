---
title: "overfitting-vs-underfitting"
status: draft
created: 2026-08-08
tags:
  - machine-learning
  - model-tuning
  - diagnostics
related:
  - bias-variance-tradeoff
  - training-validation-test-split
---

# overfitting-vs-underfitting

## Purpose

Explain overfitting and underfitting, the two failure modes of a trained
model.

## Context

A model is judged on new data, not on the data it trained on. When training
does not match reality, the model fails in one of two directions: it memorizes
the training set (overfitting) or never learns its patterns (underfitting).
Recognizing the symptoms points to the right fix.

## Main Notes

- Overfitting happens when a model learns the training data so well that it
  also learns its noise and quirks.
- An overfit model scores high on training data but poorly on new data; it
  does not generalize.
- Underfitting happens when a model is too simple to capture the pattern, so
  it performs badly on both training and new data.
- Overfitting is more likely with complex models, few training examples, or
  long training.
- Fixes for overfitting: more data, regularization, simpler models, or early
  stopping.
- Fixes for underfitting: a more capable model, better features, or longer
  training.
- The gap between training and validation performance is the key signal for
  detecting overfitting.
- A healthy model has low error on both training and validation sets.

## References

- Foundational concept; no single source.
- Standard topic in machine learning textbooks.

## Related Notes

- [[bias-variance-tradeoff]]
- [[training-validation-test-split]]

## Tags

This note is tagged in the front matter as machine-learning, model-tuning,
diagnostics.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
