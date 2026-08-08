---
title: "package-managers-linux"
status: draft
created: 2026-08-08
tags:
  - linux
  - tooling
  - administration
---

# package-managers-linux

## Purpose

Explain Linux package managers and how they install and update software.

## Context

Installing software by hand means hunting for files, resolving dependencies,
and keeping everything updated. Package managers automate this: they fetch
software packages from repositories, check that dependencies are present,
and record what is installed. Each distribution family has its own tool and
package format.

## Main Notes

- A package bundles a program with its files and metadata describing
  dependencies and version.
- A package manager resolves dependencies, installing what a package needs
  and refusing broken setups.
- Repositories are curated collections of packages; the manager downloads
  from them over the network.
- Debian-based systems use apt and the .deb format; Red Hat systems use dnf
  and .rpm.
- Arch uses pacman; other ecosystems have their own tools.
- The manager tracks installed packages so updates and removals stay
  consistent.
- Updates install newer versions of installed packages and their security
  fixes.
- Root privileges are usually required, because packages install to
  system-wide locations.
- Third-party tools add packages outside the default repository, which
  increases convenience and risk.

## References

- Foundational concept; no single source.
- Documented in the manual pages of apt, dnf, and related tools.

## Related Notes

No related notes yet.

## Tags

This note is tagged in the front matter as linux, tooling, administration.

## Review History

- 2026-08-08: Created as a draft.
