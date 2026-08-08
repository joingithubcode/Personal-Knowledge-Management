---
title: "linux-file-permissions"
status: draft
created: 2026-08-08
tags:
  - linux
  - security
  - administration
related:
  - bash-scripting-basics
---

# linux-file-permissions

## Purpose

Explain Linux file permissions and how they control who can do what.

## Context

A Linux system holds files for many users, and not everyone may read, change,
or run every file. Permissions attach to each file and directory and describe
what the owner, the owner's group, and everyone else may do. Getting them
right protects data; getting them wrong is a common cause of both breakage
and breaches.

## Main Notes

- Each file has three permission classes: owner, group, and others.
- Each class has three permissions: read (r), write (w), and execute (x).
- Read lets a file be viewed; write lets it be changed; execute lets it run.
- Permissions display as a ten-character string, such as -rwxr-xr--, and
  also as octal numbers.
- Octal digits encode each class: read is 4, write is 2, execute is 1; 755
  means rwxr-xr-x.
- Directories interpret the bits differently: execute is needed to enter and
  read lists the contents.
- The special setuid and setgid bits run a program with another user's
  rights; they need care.
- The root user bypasses most permission checks, so root access is the real
  boundary.

## References

- Foundational concept; no single source.
- Documented in Linux manual pages and POSIX standards.

## Related Notes

- [[bash-scripting-basics]]

## Tags

This note is tagged in the front matter as linux, security, administration.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
