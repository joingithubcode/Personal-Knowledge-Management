---
title: "infrastructure-as-code-basics"
status: draft
created: 2026-08-08
tags:
  - devops
  - infrastructure
  - automation
related:
  - cloud-service-models
---

# infrastructure-as-code-basics

## Purpose

Explain infrastructure as code and why servers should be defined in files.

## Context

Clicking through consoles to create servers, networks, and databases leaves no
record, invites drift, and cannot be repeated exactly. Infrastructure as code
defines that infrastructure in declarative files that are versioned,
reviewed, and applied automatically. The environment then becomes
reproducible like application code.

## Main Notes

- Infrastructure as code describes infrastructure in files rather than
  through manual clicks.
- Declarative tools state the desired end state, and the tool works out how
  to reach it.
- Configuration files live in version control, so changes are reviewed,
  rolled back, and shared.
- The same definition builds identical environments: dev, staging, and
  production no longer drift apart.
- Applying a change modifies infrastructure automatically instead of through
  step-by-step manual work.
- Idempotency matters: applying the same file twice converges to the same
  state instead of duplicating resources.
- Secrets still need separate, careful handling; they do not belong in the
  plain configuration file.
- Common categories cover virtual machines, containers, and application
  configuration, each with its own tools.

## References

- Foundational concept; no single source.
- Standard practice in DevOps and site reliability engineering material.

## Related Notes

- [[cloud-service-models]]

## Tags

This note is tagged in the front matter as devops, infrastructure,
automation.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
