---
title: "ai-voice-platform-tech-stack"
status: active
created: 2026-08-08
tags:
  - ai-voice-platform
  - tech-stack
  - architecture
related:
  - ai-voice-platform-overview
  - celery-redis-workers
  - piper-subprocess-isolation-licensing
  - xtts-v2-commercial-license-restriction
---

# ai-voice-platform-tech-stack

## Purpose

Record the complete technology stack of the AI Voice platform as a
reference.

## Context

The AI Voice platform runs a specific set of components. This note documents
the full stack so the architecture is recorded in one place.

## Main Notes

- Backend: Python FastAPI.
- Frontend: Next.js 15+ with App Router.
- Database: PostgreSQL.
- Queue and cache: Redis with Celery for background jobs.
- Auth: JWT/OAuth2.
- Storage: S3-compatible.
- TTS engines: Piper (primary CPU), Kokoro TTS, MeloTTS, Chatterbox,
  Kitten TTS.
- Voice cloning: XTTS-v2 (primary, commercial-use banned), OpenVoice V2
  (cloning/emotion), Pocket TTS, Sopro TTS, NeuTTS Air, VoxCPM.
- STT: faster-whisper.
- Urdu fallback: ElevenLabs API.

## References

- Source: the author's AI-Voice-Platform project history, 2026.

## Related Notes

- [[ai-voice-platform-overview]]
- [[celery-redis-workers]]
- [[piper-subprocess-isolation-licensing]]
- [[xtts-v2-commercial-license-restriction]]

## Tags

This note is tagged in the front matter as ai-voice-platform, tech-stack,
architecture.

## Review History

- 2026-08-08: Created as an active project note.
- 2026-08-08: Added related note links.
