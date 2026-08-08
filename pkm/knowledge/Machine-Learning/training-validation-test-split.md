---
title: "training-validation-test-split"
status: draft
created: 2026-08-08
tags:
  - machine-learning
  - evaluation
  - model-development
related:
  - model-evaluation-metrics
  - overfitting-vs-underfitting
---

# training-validation-test-split

## Purpose

Explain why data is split into training, validation, and test sets and what
each is for.

## Context

A model fitted to data can look better than it really is, because the model
may simply memorize the data it saw. To get an honest measure of performance,
the data is divided into separate sets used for different jobs. The split is
the standard discipline for model development.

## Main Notes

- The training set teaches the model its parameters.
- The validation set tunes choices the model does not learn from data, such
  as model type and hyperparameters.
- The test set measures final performance on data never used during
  development.
- Without a held-out test set, tuning decisions can leak into the reported
  score and flatter the model.
- Common splits are around 60/20/20 or 70/15/15 training/validation/test.
- Each set should reflect the same underlying distribution; shuffle and
  stratify to keep class balance.
- Small datasets need care: cross-validation uses multiple folds instead of
  one fixed split.
- Validation and test sets must never be tuned against; use them only for
  their intended job.

## References

- Foundational concept; no single source.
- Standard practice in machine learning textbooks and tooling.

## Related Notes

- [[model-evaluation-metrics]]
- [[overfitting-vs-underfitting]]

## Tags

This note is tagged in the front matter as machine-learning, evaluation,
model-development.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
