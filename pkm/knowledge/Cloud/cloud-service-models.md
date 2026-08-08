---
title: "cloud-service-models"
status: draft
created: 2026-08-08
tags:
  - cloud
  - infrastructure
  - architecture
related:
  - cloud-vs-self-hosted
  - infrastructure-as-code-basics
---

# cloud-service-models

## Purpose

Explain the IaaS, PaaS, and SaaS service models and what each handles for you.

## Context

Cloud providers offer infrastructure at different levels of abstraction. The
more the provider manages, the less the customer controls and operates. The
three classic models, IaaS, PaaS, and SaaS, define the split of
responsibility between provider and customer.

## Main Notes

- IaaS (infrastructure as a service) provides raw compute, storage, and
  networking; the customer installs and manages the operating system and
  everything above it.
- PaaS (platform as a service) provides a managed runtime: the customer
  uploads code and the platform handles servers, scaling, and middleware.
- SaaS (software as a service) provides a finished application the customer
  uses over the internet, with no infrastructure to manage.
- The responsibility moves as the model moves: the provider owns more of the
  stack from IaaS to SaaS.
- IaaS gives the most control and the most operational work; SaaS the least
  of both.
- FaaS (functions as a service) extends PaaS toward running single functions
  on demand.
- A single system mixes models: a serverless function (FaaS) that calls a
  managed database (PaaS).
- Choose the model that matches your focus; do not operate what a managed
  service can handle.

## References

- Foundational concept; no single source.
- Standard topic in cloud computing literature and certification material.

## Related Notes

- [[cloud-vs-self-hosted]]
- [[infrastructure-as-code-basics]]

## Tags

This note is tagged in the front matter as cloud, infrastructure,
architecture.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
