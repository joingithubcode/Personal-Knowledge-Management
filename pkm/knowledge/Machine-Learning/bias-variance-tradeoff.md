---
title: "bias-variance-tradeoff"
status: draft
created: 2026-08-08
tags:
  - machine-learning
  - model-tuning
  - statistics
related:
  - overfitting-vs-underfitting
---

# bias-variance-tradeoff

## Purpose

Explain the bias-variance tradeoff and how it governs model complexity.

## Context

A model's error on new data splits into three parts: noise we cannot remove,
bias from oversimplification, and variance from sensitivity to the training
sample. Reducing one usually raises the other. This tension explains why the
best model is not the simplest or the most complex.

## Main Notes

- Bias is the error from a model that is too simple to capture the real
  pattern; high bias ignores data detail.
- Variance is the error from a model that is too sensitive to the training
  sample; high variance changes a lot between datasets.
- Total error equals bias squared plus variance plus irreducible noise.
- A simple model has high bias and low variance; a complex model has low
  bias and high variance.
- High bias shows up as underfitting; high variance shows up as
  overfitting.
- The tradeoff drives complexity choices: pick the level where total error
  is lowest, not where training error is lowest.
- Regularization and more data both reduce variance with little added bias.
- The validation set reveals the balance: watch both training and validation
  error as complexity grows.

## References

- Foundational concept; no single source.
- Standard topic in statistics and machine learning textbooks.

## Related Notes

- [[overfitting-vs-underfitting]]

## Tags

This note is tagged in the front matter as machine-learning, model-tuning,
statistics.

## Review History

- 2026-08-08: Created as a draft.
