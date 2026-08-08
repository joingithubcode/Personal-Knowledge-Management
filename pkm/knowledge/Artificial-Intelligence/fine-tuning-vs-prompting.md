---
title: "fine-tuning-vs-prompting"
status: draft
created: 2026-08-08
tags:
  - artificial-intelligence
  - large-language-models
  - model-training
related:
  - prompt-engineering-basics
---

# fine-tuning-vs-prompting

## Purpose

Compare fine-tuning a language model with prompting it, and when to use each.

## Context

To make a model behave well on a specific task, teams can adapt it or steer
it. Fine-tuning updates the model's weights on extra data; prompting changes
only the input text. The choice affects cost, skill, latency, and
flexibility.

## Main Notes

- Prompting changes behavior through instructions and examples inside the
  request; no weights are modified.
- Fine-tuning adjusts the model's parameters by training it further on
  task-specific examples.
- Prompting is fast to try, needs no training pipeline, and stays fully
  flexible as prompts change.
- Fine-tuning locks in a behavior across all requests, improves consistency,
  and can shrink the prompt needed.
- Fine-tuning requires a curated dataset, training compute, and evaluation;
  it is heavier to build and maintain.
- Prompting works within the model's existing abilities; fine-tuning can
  teach formats and styles the model handles poorly.
- Start with prompting; fine-tune only when prompt-only results are
  insufficient or too expensive at scale.
- The two combine: prompt a fine-tuned model for the final layer of control.

## References

- Foundational concept; no single source.
- Documented in language model fine-tuning guides and research literature.

## Related Notes

- [[prompt-engineering-basics]]

## Tags

This note is tagged in the front matter as artificial-intelligence,
large-language-models, model-training.

## Review History

- 2026-08-08: Created as a draft.
