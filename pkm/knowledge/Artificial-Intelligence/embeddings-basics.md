---
title: "embeddings-basics"
status: draft
created: 2026-08-08
tags:
  - machine-learning
  - natural-language-processing
  - representations
related:
  - what-is-rag
---

# embeddings-basics

## Purpose

Explain word and text embeddings and why vector representations power modern
AI systems.

## Context

Models cannot read words directly; they need numbers. Embeddings map words,
sentences, or documents to fixed-length vectors of numbers. The position of a
vector in the space encodes meaning, so similar texts sit near each other.
This property drives search, similarity, and retrieval systems.

## Main Notes

- An embedding turns a unit of text into a dense vector of real numbers.
- Meaningful structure emerges: similar words and related concepts end up
  close together in the vector space.
- Arithmetic holds loosely; famous examples show king minus man plus woman
  landing near queen.
- Word embeddings learn from large corpora; sentence and document embeddings
  extend the idea to whole passages.
- Similarity is measured with cosine similarity, a distance over the
  vectors.
- Embeddings are central to RAG: documents and queries are embedded, and
  retrieval finds the nearest vectors.
- The embedding model is a separate component from the language model that
  generates answers.
- Choosing an embedding model trades quality against cost and latency.

## References

- Foundational concept; no single source.
- Word2vec from Mikolov et al., 2013; related representation learning work.

## Related Notes

- [[what-is-rag]]

## Tags

This note is tagged in the front matter as machine-learning,
natural-language-processing, representations.

## Review History

- 2026-08-08: Created as a draft.
