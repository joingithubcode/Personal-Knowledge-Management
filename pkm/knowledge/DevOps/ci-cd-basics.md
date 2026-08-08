---
title: "ci-cd-basics"
status: draft
created: 2026-08-08
tags:
  - devops
  - automation
  - software-delivery
related:
  - testing-pyramid-basics
  - version-control-basics
---

# ci-cd-basics

## Purpose

Explain continuous integration and continuous delivery and how they make
releases safe and repeatable.

## Context

Releasing software by hand is slow and error-prone. CI/CD automates the
pipeline from code change to deployment: every change is integrated and
tested automatically, and good builds can ship automatically. The result is
small, frequent, low-risk releases instead of rare, large ones.

## Main Notes

- Continuous integration (CI) automatically builds and tests every change
  pushed to the main branch.
- CI catches integration problems early by merging often and checking each
  merge.
- Continuous delivery (CD) keeps every passing build ready to deploy;
  continuous deployment ships passing builds automatically.
- A pipeline chains stages: lint, build, test, package, and deploy.
- Pipelines run in CI servers or managed platforms; a failure blocks the
  change from proceeding.
- Pipeline definition should live in the repository as code, so it is
  versioned and reviewed like the app.
- Fast feedback is the goal: developers learn within minutes whether a
  change is safe.
- Good pipelines make deployments boring; a release is no longer a
  high-risk event.

## References

- Foundational concept; no single source.
- Standard practice in DevOps and software delivery literature.

## Related Notes

- [[testing-pyramid-basics]]
- [[version-control-basics]]

## Tags

This note is tagged in the front matter as devops, automation,
software-delivery.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
