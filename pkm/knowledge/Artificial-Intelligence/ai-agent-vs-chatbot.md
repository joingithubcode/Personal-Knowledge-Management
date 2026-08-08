---
title: "ai-agent-vs-chatbot"
status: draft
created: 2026-08-08
tags:
  - artificial-intelligence
  - large-language-models
  - software-design
related:
  - llm-vs-traditional-nlp
---

# ai-agent-vs-chatbot

## Purpose

Distinguish an AI agent from a chatbot and explain what makes an agent act.

## Context

Many products are called AI assistants, but they differ in how much they do.
A chatbot converses; an agent plans and acts. Understanding the difference
helps set expectations and design the right system for a task.

## Main Notes

- A chatbot holds a conversation: it answers questions and follows simple
  instructions within the dialogue.
- An agent goes further: it can plan, decide, and take actions in the world
  using tools.
- Agents call external functions, such as APIs, databases, and web requests,
  and use the results to continue.
- Agents may work in loops: reason, act, observe the result, and reason
  again until the goal is met.
- A chatbot is often a single model call per message; an agent chains calls
  with state and tool access.
- Both are built on language models; the agent adds orchestration,
  tooling, and control flow around them.
- Agents bring more risk because they act; they need permission scopes,
  limits, and human checkpoints.
- The boundary blurs: many chatbots become agents once they add tool calls
  and autonomous steps.

## References

- Foundational concept; no single source.
- Described in agent and tool-use literature for large language models.

## Related Notes

- [[llm-vs-traditional-nlp]]

## Tags

This note is tagged in the front matter as artificial-intelligence,
large-language-models, software-design.

## Review History

- 2026-08-08: Created as a draft.
