---
title: "wsl-basics"
status: draft
created: 2026-08-08
tags:
  - linux
  - windows
  - development-tools
---

# wsl-basics

## Purpose

Explain Windows Subsystem for Linux and how it runs Linux on Windows.

## Context

Developers on Windows often need Linux tools: the shell, package managers,
and the same environment as production servers. The Windows Subsystem for
Linux (WSL) runs a real Linux distribution alongside Windows without a
virtual machine or dual boot. It bridges the two worlds for development.

## Main Notes

- WSL runs Linux distributions on Windows by providing a Linux kernel and
  userspace.
- WSL 2 runs Linux in a lightweight virtual machine with near-native
  performance and full kernel support.
- A user installs a distribution such as Ubuntu and gets a normal Linux
  terminal, filesystem, and toolchain.
- Windows and Linux filesystems are mutually accessible, so files can be
  shared between the two.
- WSL integrates with Windows tools: editors and terminals can launch WSL
  commands.
- Networking is shared, so services started in Linux are reachable from
  Windows programs.
- The Linux environment in WSL behaves like a real Linux box, making it a
  faithful development and testing target.
- Resource usage is dynamic; WSL reclaims memory when the Linux environment
  is idle.

## References

- Foundational concept; no single source.
- Documented in Microsoft's WSL documentation.

## Related Notes

No related notes yet.

## Tags

This note is tagged in the front matter as linux, windows,
development-tools.

## Review History

- 2026-08-08: Created as a draft.
