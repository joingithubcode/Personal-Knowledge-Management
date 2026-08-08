---
title: "blockchain-basics"
status: draft
created: 2026-08-08
tags:
  - blockchain
  - distributed-systems
  - cryptography
related:
  - consensus-mechanisms-basics
  - encryption-basics
---

# blockchain-basics

## Purpose

Explain the core ideas of a blockchain and what it provides.

## Context

Trusting a single party to hold records creates a single point of failure and
a risk of tampering. A blockchain is a distributed ledger: the same record
lives on many machines, and new entries are chained to previous ones with
cryptography. Its value is a shared, tamper-evident record with no central
authority.

## Main Notes

- A blockchain is a chain of blocks, each holding a batch of transactions and
  a link to the previous block.
- Each block includes a hash of the previous block, so changing any old entry
  breaks every later link.
- The ledger is replicated across many nodes, and the network agrees on its
  state without a central server.
- Consensus mechanisms let the nodes agree on which blocks are valid and in
  what order.
- Participants are identified by cryptographic keys; transactions are signed,
  not carried by passwords.
- The tamper-evidence comes from the hashes plus the cost of rewriting
  history across the network.
- Public blockchains are open to anyone; permissioned blockchains restrict
  who may participate.
- Blockchains trade throughput and cost for decentralization; they are not
  the right tool for every record.

## References

- Foundational concept; no single source.
- Originated with the Bitcoin whitepaper by Satoshi Nakamoto, 2008.

## Related Notes

- [[consensus-mechanisms-basics]]
- [[encryption-basics]]

## Tags

This note is tagged in the front matter as blockchain, distributed-systems,
cryptography.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
