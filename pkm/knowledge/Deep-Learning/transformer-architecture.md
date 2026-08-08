---
title: "transformer-architecture"
status: draft
created: 2026-08-08
tags:
  - deep-learning
  - neural-networks
  - language-models
related:
  - neural-networks-basics
  - context-window-basics
---

# transformer-architecture

## Purpose

Explain the transformer architecture and why it powers modern language
models.

## Context

Earlier models for text processed one word at a time, which limited how much
context they could use and how fast they trained. The transformer processes
all tokens at once, letting every token attend to every other. Its success on
language tasks made it the backbone of large language models.

## Main Notes

- The transformer was introduced for translation and quickly became the
  standard for language.
- Its key idea is self-attention: every token looks at every other token and
  weights their influence.
- Attention lets the model relate distant words, such as a pronoun to its
  noun, regardless of the gap.
- Positional encodings add order information, since the model sees tokens in
  parallel rather than in sequence.
- Stacked encoder and decoder layers compose the model; many modern models
  use only the decoder side.
- Parallel processing makes transformers far faster to train on hardware than
  step-by-step recurrent models.
- Scaling up data, parameters, and compute steadily improves them, producing
  today's large language models.
- The context window bounds attention; the architecture's memory use grows
  with sequence length.

## References

- Vaswani et al., "Attention Is All You Need", 2017.

## Related Notes

- [[neural-networks-basics]]
- [[context-window-basics]]

## Tags

This note is tagged in the front matter as deep-learning, neural-networks,
language-models.

## Review History

- 2026-08-08: Created as a draft.
