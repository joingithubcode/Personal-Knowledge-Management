---
title: "llm-vs-traditional-nlp"
status: draft
created: 2026-08-08
tags:
  - artificial-intelligence
  - natural-language-processing
  - machine-learning
related:
  - ai-agent-vs-chatbot
  - context-window-basics
  - hallucination-in-llms
---

# llm-vs-traditional-nlp

## Purpose

Contrast large language models with earlier natural language processing
approaches.

## Context

NLP has evolved through two broad eras. Traditional NLP used hand-crafted
features, rules, and smaller statistical models, each built for one task.
Large language models are huge neural networks trained on massive text that
generalize across many tasks. Knowing the difference explains why modern
systems behave so differently.

## Main Notes

- Traditional NLP built task-specific systems: separate pipelines for
  tagging, parsing, classification, and extraction.
- Those systems relied on engineered features and labeled data per task;
  they were transparent but narrow and brittle.
- Large language models are trained on enormous text corpora and learn
  language structure from the data itself.
- LLMs handle many tasks with the same weights; prompting steers them without
  new training data.
- LLMs read and produce long, coherent text and follow complex instructions;
  traditional models could not.
- LLMs have a context window that limits what they see in one call; earlier
  models worked on fixed small inputs.
- LLMs hallucinate and need grounding; traditional models, though weaker,
  rarely invented fluent falsehoods.
- In practice, systems combine both: focused traditional components and
  LLM-based reasoning.

## References

- Foundational concept; no single source.
- Survey literature on language models and NLP history.

## Related Notes

- [[ai-agent-vs-chatbot]]
- [[context-window-basics]]
- [[hallucination-in-llms]]

## Tags

This note is tagged in the front matter as artificial-intelligence,
natural-language-processing, machine-learning.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
