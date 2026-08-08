---
title: "native-vs-cross-platform"
status: draft
created: 2026-08-08
tags:
  - mobile-development
  - architecture
  - decision-making
related:
  - frontend-vs-backend
---

# native-vs-cross-platform

## Purpose

Compare native and cross-platform mobile development approaches.

## Context

A mobile app can target one platform with its own tools or many platforms
from a single shared codebase. Native development uses the platform's own
language and frameworks; cross-platform frameworks reuse one codebase across
operating systems. The choice trades reach, cost, and platform access.

## Main Notes

- Native development builds separately for each platform, using its own
  language and SDKs.
- iOS native uses Swift and the Apple SDKs; Android native uses Kotlin and
  the Android SDK.
- Native apps get full access to every platform feature and the best
  performance and feel.
- Cross-platform development writes one codebase that runs on multiple
  platforms.
- Common cross-platform approaches include web-based wrappers and compiled
  shared frameworks.
- Cross-platform saves effort and keeps behavior consistent but can lag
  behind new platform features.
- Some apps combine approaches: shared logic plus native code where needed.
- The right choice weighs team skills, performance needs, and the number of
  platforms to support.

## References

- Foundational concept; no single source.
- Standard topic in mobile development literature and platform
  documentation.

## Related Notes

- [[frontend-vs-backend]]

## Tags

This note is tagged in the front matter as mobile-development, architecture,
decision-making.

## Review History

- 2026-08-08: Created as a draft.
