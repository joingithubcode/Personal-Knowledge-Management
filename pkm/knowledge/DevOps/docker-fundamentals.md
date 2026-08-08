---
title: "docker-fundamentals"
status: draft
created: 2026-08-08
tags:
  - devops
  - containers
  - tooling
related:
  - containerization-vs-virtualization
---

# docker-fundamentals

## Purpose

Explain Docker's core concepts: images, containers, and how applications are
packaged.

## Context

An app runs differently on a laptop, a staging server, and production,
because environments differ. Docker packages an application with its runtime,
libraries, and settings into a single image. The same image then runs
identically anywhere Docker is installed.

## Main Notes

- An image is a read-only template: the application, its runtime, and
  dependencies, built from a Dockerfile.
- A container is a running instance of an image; it is isolated in its own
  process and filesystem view.
- The Dockerfile lists steps: a base image, files to copy, and the command to
  run.
- Containers share the host operating system kernel, which keeps them light
  compared to full virtual machines.
- Images are layered; each instruction adds a layer, and layers are cached
  and reused across builds.
- Containers are ephemeral: storage written inside a container is lost unless
  mounted from a volume.
- Ports and data are exposed explicitly: the host maps a port to the
  container, and volumes persist data.
- Compose and orchestration (Kubernetes) coordinate many containers; Docker
  itself runs one or a few.

## References

- Foundational concept; no single source.
- Docker documentation at docs.docker.com.

## Related Notes

- [[containerization-vs-virtualization]]

## Tags

This note is tagged in the front matter as devops, containers, tooling.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
