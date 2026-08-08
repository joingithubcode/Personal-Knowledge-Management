---
title: "codds-12-rules"
status: draft
created: 2026-08-08
tags:
  - databases
  - relational-model
  - data-management
related:
  - normalization-1nf-2nf-3nf
  - sql-joins-types
---

# codds-12-rules

## Purpose

Describe Edgar F. Codd's twelve rules, a test for how fully a database system
behaves as a true relational database.

## Context

Codd proposed the relational model in 1970. The twelve rules, published in
1985, define what a system must satisfy to be called genuinely relational.
No commercial product has ever met all twelve, so they serve as an ideal
benchmark rather than a compliance checklist.

## Main Notes

- The rules center on one idea: data is exposed only through a logical
  relational model, not through physical storage details.
- Rule 0 (foundation): a relational system must manage data solely through
  its relational capabilities.
- Key rules include: information represented only as table data; guaranteed
  access via table name, primary key, and column; null values treated
  systematically; a catalog of metadata stored as ordinary tables.
- Data manipulation must be offered at the logical level: a single language
  (SQL) supports data definition, manipulation, integrity, and transactions.
- Rules cover logical data independence (views), physical data independence,
  and integrity constraints defined in the catalog.
- Distribution independence and the "non-subversion" rule (no way to bypass
  relational integrity) complete the set.
- The rules assume a relational engine; systems that merely imitate tables
  with other structures do not satisfy them.
- Practical databases implement most rules through SQL standards while
  vendor extensions keep the rules from being fully met.

## References

- Edgar F. Codd, "Is Your DBMS Really Relational?" and "Does Your DBMS Run
  By The Rules?", Computerworld, 1985.

## Related Notes

- [[normalization-1nf-2nf-3nf]]
- [[sql-joins-types]]

## Tags

This note is tagged in the front matter as databases, relational-model,
data-management.

## Review History

- 2026-08-08: Created as a draft.
- 2026-08-08: Added related note links.
