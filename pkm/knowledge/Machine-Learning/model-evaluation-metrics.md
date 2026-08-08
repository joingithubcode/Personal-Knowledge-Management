---
title: "model-evaluation-metrics"
status: draft
created: 2026-08-08
tags:
  - machine-learning
  - evaluation
  - metrics
related:
  - training-validation-test-split
---

# model-evaluation-metrics

## Purpose

Explain the common metrics for measuring model performance and when each one
is meaningful.

## Context

A model's quality cannot be read from a single number. Different tasks and
different data distributions call for different metrics. Choosing the right
one prevents drawing the wrong conclusion about a model's usefulness.

## Main Notes

- Accuracy is the share of correct predictions; it misleads when classes are
  imbalanced.
- Precision is the share of positive predictions that were correct; it
  measures how much to trust a positive call.
- Recall is the share of actual positives that were found; it measures how
  much of the target the model catches.
- F1 score balances precision and recall with a single harmonic mean.
- Confusion matrices lay out true and false positives and negatives, the
  raw material of the other metrics.
- For regression, common metrics are mean squared error, mean absolute
  error, and R-squared.
- Imbalanced problems favor precision, recall, or F1 over accuracy; the
  choice depends on the cost of each error type.
- Cross-validation reports the metric over folds so the estimate is
  stable and honest.

## References

- Foundational concept; no single source.
- Standard topic in machine learning textbooks and model evaluation guides.

## Related Notes

- [[training-validation-test-split]]

## Tags

This note is tagged in the front matter as machine-learning, evaluation,
metrics.

## Review History

- 2026-08-08: Created as a draft.
