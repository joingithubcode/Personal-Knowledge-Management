---
title: "hallucination-in-llms"
status: draft
created: 2026-08-08
tags:
  - artificial-intelligence
  - large-language-models
  - reliability
related:
  - llm-vs-traditional-nlp
---

# hallucination-in-llms

## Purpose

Explain why language models hallucinate and how to reduce the risk of false
output.

## Context

Language models generate text by predicting plausible continuations, not by
looking up verified facts. As a result, they can produce fluent, confident
statements that are false or invented. Hallucination is a known limitation of
the technology, and systems that rely on LLM output must account for it.

## Main Notes

- A hallucination is fluent, believable output that is not grounded in real
  facts or sources.
- Models generate likely-sounding text, so gaps in knowledge surface as
  confident guesses rather than admission of ignorance.
- Hallucinations are more likely on obscure, recent, or numerical topics and
  when the model is asked to go beyond its training.
- Grounding with retrieved sources, as in RAG, reduces fabrication by giving
  the model real text to follow.
- Asking the model to cite its sources or answer only from provided text
  lowers the risk of invented content.
- Verification matters: outputs that carry risk should be checked by a human
  or by automated rules before use.
- No prompt fully eliminates hallucination; treat it as a system design
  concern, not a fixable model flaw.
- The model's own uncertainty markers (such as "I don't know") can be
  encouraged but are not guaranteed.

## References

- Foundational concept; no single source.
- Surveyed in large language model reliability literature.

## Related Notes

- [[llm-vs-traditional-nlp]]

## Tags

This note is tagged in the front matter as artificial-intelligence,
large-language-models, reliability.

## Review History

- 2026-08-08: Created as a draft.
