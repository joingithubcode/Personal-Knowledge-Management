---
title: "context-window-basics"
status: draft
created: 2026-08-08
tags:
  - artificial-intelligence
  - large-language-models
  - architecture
related:
  - llm-vs-traditional-nlp
  - prompt-engineering-basics
  - transformer-architecture
---

# context-window-basics

## Purpose

Explain the context window of a language model and how it limits a single
conversation or prompt.

## Context

A language model processes text in fixed-size chunks. The context window is
the maximum amount of text the model can consider at once. Everything the
model sees in one call, including the prompt and its answer, must fit inside
it. This limit shapes how applications build prompts and manage long
conversations.

## Main Notes

- The context window is the total number of tokens a model accepts in one
  request.
- Input, instructions, documents, conversation history, and the generated
  output all count against the same window.
- Tokens are chunks of text, usually a fraction of a word, so window sizes
  are stated in tokens.
- When input exceeds the window, it must be truncated, summarized, or
  handled by retrieval.
- Larger windows let a model handle long documents but cost more compute and
  can spread attention thin.
- Long conversations grow until they hit the limit, so apps summarize or
  drop older turns.
- RAG keeps prompts small by injecting only the most relevant retrieved
  passages instead of full documents.
- Prompt engineering must respect the window: wasted tokens reduce the space
  for useful content.

## References

- Foundational concept; no single source.
- Described in model documentation for transformer-based language models.

## Related Notes

- [[llm-vs-traditional-nlp]]
- [[prompt-engineering-basics]]
- [[transformer-architecture]]

## Tags

This note is tagged in the front matter as artificial-intelligence,
large-language-models, architecture.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
