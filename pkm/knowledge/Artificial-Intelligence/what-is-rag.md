---
title: "what-is-rag"
status: draft
created: 2026-08-08
tags:
  - artificial-intelligence
  - large-language-models
  - information-retrieval
related:
  - embeddings-basics
---

# what-is-rag

## Purpose

Explain retrieval-augmented generation (RAG) and the problem it solves for
large language models.

## Context

Large language models answer from patterns learned during training, so their
knowledge is frozen at that point and may miss private or recent information.
RAG adds a retrieval step: it finds relevant documents at query time and
feeds them to the model, so answers are grounded in current, specific
sources.

## Main Notes

- RAG splits the work into two stages: retrieval and generation.
- Retrieval finds the most relevant passages from a knowledge base for the
  user's question.
- Generation passes those passages, plus the question, to a language model,
  which answers from them.
- Embeddings turn text into vectors so retrieval can find similar passages
  by distance.
- RAG lets a system use private, changing, or specialized data without
  retraining the model.
- Answers can cite the retrieved sources, improving trust and
  verifiability.
- RAG reduces hallucinations by giving the model real text to draw on.
- The knowledge base must be indexed and kept current for the retrieval to
  stay useful.

## References

- Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP
  Tasks", 2020.

## Related Notes

- [[embeddings-basics]]

## Tags

This note is tagged in the front matter as artificial-intelligence,
large-language-models, information-retrieval.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
