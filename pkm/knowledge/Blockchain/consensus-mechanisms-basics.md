---
title: "consensus-mechanisms-basics"
status: draft
created: 2026-08-08
tags:
  - blockchain
  - distributed-systems
  - protocols
related:
  - blockchain-basics
---

# consensus-mechanisms-basics

## Purpose

Explain consensus mechanisms and how decentralized networks agree on a
single history.

## Context

A blockchain has no central authority, yet all nodes must accept the same
blocks in the same order; otherwise the ledger forks into confusion. Consensus
mechanisms solve this by giving the network a rule for who may add the next
block and how others verify it. The rule shapes the network's security and
energy use.

## Main Notes

- Consensus is the process by which nodes agree on a shared, valid
  history.
- Proof of work requires miners to solve a hard computational puzzle; the
  winner adds the next block.
- Proof of work makes rewriting history expensive, which secures the chain,
  but it consumes large amounts of energy.
- Proof of stake selects block producers based on the stake they lock up,
  with losses for dishonest behavior.
- Proof of stake uses far less energy and speeds transactions, at the cost of
  different trust assumptions.
- Other mechanisms exist, such as delegated proof of stake and practical
  byzantine fault tolerance for permissioned networks.
- A network follows the longest valid chain, so honest nodes converge on one
  history.
- The choice of mechanism is a trade between security, energy, speed, and
  decentralization.

## References

- Foundational concept; no single source.
- Proof of work from the Bitcoin whitepaper, 2008; proof of stake from
  later blockchain literature.

## Related Notes

- [[blockchain-basics]]

## Tags

This note is tagged in the front matter as blockchain, distributed-systems,
protocols.

## Review History

- 2026-08-08: Created as a draft.
