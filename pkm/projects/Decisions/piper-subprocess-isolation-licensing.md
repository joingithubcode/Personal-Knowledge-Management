---
title: "piper-subprocess-isolation-licensing"
status: active
created: 2026-08-08
tags:
  - ai-voice-platform
  - licensing
  - gpl
related:
  - ai-voice-platform-tech-stack
  - gpl-license-basics
  - platform-critical-review-findings
---

# piper-subprocess-isolation-licensing

## Purpose

Record the decision to isolate Piper as a subprocess to avoid GPL license
contamination.

## Context

Piper TTS is the primary CPU TTS engine for the platform, but Piper is
GPL-3.0 licensed. The platform codebase is proprietary SaaS, so mixing Piper
into it would risk GPL obligations.

## Main Notes

- Piper TTS is used as the primary CPU TTS engine.
- Piper is GPL-3.0 licensed.
- Decision: Piper must be called as an isolated subprocess.
- It must never be imported directly into the codebase.
- This avoids GPL license contamination of the proprietary SaaS codebase.

## References

- Source: the author's AI-Voice-Platform project history, 2026.

## Related Notes

- [[ai-voice-platform-tech-stack]]
- [[gpl-license-basics]]
- [[platform-critical-review-findings]]

## Tags

This note is tagged in the front matter as ai-voice-platform, licensing, gpl.

## Review History

- 2026-08-08: Created as an active project note.
- 2026-08-08: Added related note links.
