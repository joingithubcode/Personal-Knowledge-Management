---
title: "s3-compatible-storage"
status: draft
created: 2026-08-08
tags:
  - cloud
  - storage
  - object-storage
---

# s3-compatible-storage

## Purpose

Explain object storage and what makes S3-compatible storage a common choice.

## Context

Traditional file systems and databases do not fit every kind of data,
especially large blobs such as images, videos, and backups. Object storage
holds data as objects in buckets, addressed by name rather than by position.
The Amazon S3 API became the de facto interface, and other providers offer
S3-compatible storage to reuse the same tooling.

## Main Notes

- Object storage stores data as objects, each with a unique key, held in
  containers called buckets.
- Objects are addressed by their key over HTTP, not by filesystem paths or
  block offsets.
- Object storage scales to huge amounts of data and is durable across
  failures by replication.
- The S3 API (list, get, put, delete on buckets and objects) is a widely
  adopted standard interface.
- S3-compatible providers implement the same API, so applications and tools
  work without changes.
- Access control is per bucket and per object, using keys and policies.
- Object storage is not a general-purpose database; it is ideal for blobs,
  static assets, backups, and archives.
- Lifecycle rules automate moving old objects to cheaper tiers or deleting
  them.

## References

- Amazon S3 API documentation; S3-compatible standards widely documented.

## Related Notes

No related notes yet.

## Tags

This note is tagged in the front matter as cloud, storage, object-storage.

## Review History

- 2026-08-08: Created as a draft.
