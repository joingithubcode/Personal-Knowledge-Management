---
title: "xtts-v2-commercial-license-restriction"
status: active
created: 2026-08-08
tags:
  - ai-voice-platform
  - licensing
  - voice-cloning
related:
  - ai-voice-platform-tech-stack
  - elevenlabs-voiceid-caching-sidecar
  - openvoice-v2-cloning-emotion-engine
  - xtts-v2-audio-quality-fixes
---

# xtts-v2-commercial-license-restriction

## Purpose

Record the commercial-use restriction on XTTS-v2 and the fallback decision
for Urdu voice cloning.

## Context

XTTS-v2 is the primary voice cloning engine, but its license bans commercial
use. Open CPU-optimized models do not yet handle Urdu well, so an alternative
is needed for that language.

## Main Notes

- XTTS-v2 is the primary voice cloning engine for the platform.
- Its license bans commercial use.
- Decision: use the ElevenLabs API as the fallback specifically for Urdu
  voice cloning.
- Reason: XTTS-v2 and other CPU-optimized open models do not yet handle Urdu
  well.
- This creates a hybrid routing architecture.

## References

- Source: the author's AI-Voice-Platform project history, 2026.

## Related Notes

- [[ai-voice-platform-tech-stack]]
- [[elevenlabs-voiceid-caching-sidecar]]
- [[openvoice-v2-cloning-emotion-engine]]
- [[xtts-v2-audio-quality-fixes]]

## Tags

This note is tagged in the front matter as ai-voice-platform, licensing,
voice-cloning.

## Review History

- 2026-08-08: Created as an active project note.
- 2026-08-08: Added related note links.
