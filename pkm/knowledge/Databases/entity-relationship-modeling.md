---
title: "entity-relationship-modeling"
status: draft
created: 2026-08-08
tags:
  - databases
  - data-modeling
  - design
related:
  - normalization-1nf-2nf-3nf
  - primary-key-vs-foreign-key
---

# entity-relationship-modeling

## Purpose

Explain entity-relationship (ER) modeling, the diagram technique used to
design relational databases before tables exist.

## Context

Before writing schemas, designers need a neutral picture of the domain: what
things exist, what facts describe them, and how they connect. An ER model
captures this with entities, attributes, and relationships, and later maps
cleanly to tables and keys.

## Main Notes

- An entity is a distinct object or concept (customer, order); an attribute
  is a fact about an entity (name, date).
- A relationship connects two or more entities; cardinality describes how many
  of each side participate.
- Cardinality is one-to-one, one-to-many, or many-to-many.
- Primary keys identify entity instances; each entity maps to a table with its
  attributes as columns.
- A one-to-many relationship becomes a foreign key on the "many" side.
- A many-to-many relationship needs a junction table holding both foreign
  keys.
- A one-to-one relationship can place a foreign key on either side.
- Weak entities depend on another entity for their identity and need a
  partial key.
- The ER model is implementation-independent; converting it to a physical
  schema is a later, separate step.

## References

- Foundational concept; no single source.
- ER modeling introduced by Peter Chen, "The Entity-Relationship Model:
  Toward a Unified View of Data", 1976.

## Related Notes

- [[normalization-1nf-2nf-3nf]]
- [[primary-key-vs-foreign-key]]

## Tags

This note is tagged in the front matter as databases, data-modeling, design.

## Review History

- 2026-08-08: Created as a draft.
