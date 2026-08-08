---
title: "prompt-engineering-basics"
status: draft
created: 2026-08-08
tags:
  - artificial-intelligence
  - large-language-models
  - interaction-design
related:
  - context-window-basics
  - fine-tuning-vs-prompting
---

# prompt-engineering-basics

## Purpose

Explain prompt engineering: how instructions to a language model are shaped
to get reliable, useful output.

## Context

Large language models respond to the text they receive. Because they are
trained to continue text plausibly, the way a request is worded strongly
changes the result. Prompt engineering is the practice of writing and
structuring that input deliberately.

## Main Notes

- A prompt is the input given to a model; its wording shapes the output.
- Be specific: state the task, the format, and the constraints clearly
  instead of leaving them implied.
- Give the model a role or context when it improves focus, such as "you are
  a careful proofreader".
- Provide examples; few-shot prompting shows the model the desired pattern
  before the real task.
- Break complex asks into steps; asking for a plan first produces steadier
  results.
- Constrain the output with explicit instructions like length, style, or
  "answer from the provided text only".
- The context window bounds the prompt, so keep instructions and examples
  within budget.
- Iterate: run, inspect the failure, and adjust the wording; prompting is
  empirical, not a fixed formula.

## References

- Foundational concept; no single source.
- Emerged with large language model research and model documentation.

## Related Notes

- [[context-window-basics]]
- [[fine-tuning-vs-prompting]]

## Tags

This note is tagged in the front matter as artificial-intelligence,
large-language-models, interaction-design.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
