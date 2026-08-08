---
title: "encryption-basics"
status: draft
created: 2026-08-08
tags:
  - security
  - cryptography
  - data-protection
related:
  - blockchain-basics
  - http-vs-https
---

# encryption-basics

## Purpose

Explain encryption and the difference between symmetric and asymmetric
schemes.

## Context

Data is exposed to whoever reads it: on the wire, in storage, and in files.
Encryption scrambles data so only someone with the right key can read it.
Understanding the two main families of encryption explains how TLS,
passwords, and secure messaging all work.

## Main Notes

- Encryption transforms readable data into ciphertext using a key; decryption
  reverses it with the key.
- Symmetric encryption uses one shared key for both encrypting and
  decrypting; it is fast and good for bulk data.
- Asymmetric encryption uses a key pair: a public key to encrypt and a
  private key to decrypt.
- Asymmetric keys also enable digital signatures, proving who sent a message
  and that it was not altered.
- The two combine in practice: TLS exchanges keys with asymmetric encryption,
  then encrypts the session with symmetric encryption.
- Hashing is related but different: a one-way function used for password
  storage and integrity, never for reversible storage.
- Keys must be managed: generated safely, stored in secret managers, and
  rotated.
- Encryption protects data at rest and in transit, but it does not protect
  a system where the attacker has the keys.

## References

- Foundational concept; no single source.
- Standard cryptography material; algorithms specified in standards such as
  NIST publications.

## Related Notes

- [[blockchain-basics]]
- [[http-vs-https]]

## Tags

This note is tagged in the front matter as security, cryptography,
data-protection.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
