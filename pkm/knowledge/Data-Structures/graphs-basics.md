---
title: "graphs-basics"
status: draft
created: 2026-08-08
tags:
  - data-structures
  - networks
  - algorithms
related:
  - trees-basics
---

# graphs-basics

## Purpose

Explain graphs and how they model relationships between things.

## Context

Relationships rarely fit in rows or trees: friends of friends, roads between
cities, dependencies between services. A graph models this with nodes
(vertices) and the connections (edges) between them. Graphs are the general
form; trees are a special kind of graph.

## Main Notes

- A graph is a set of vertices connected by edges.
- Edges can be directed (one-way) or undirected (two-way), and weighted
  when they carry a cost or distance.
- A path is a route of edges between vertices; a cycle is a path that loops
  back.
- Trees are connected, acyclic graphs; not all graphs are trees.
- Graphs are stored as adjacency lists or adjacency matrices; lists are
  efficient for sparse graphs.
- Depth-first search (DFS) explores one branch fully before backtracking;
  breadth-first search (BFS) explores in layers.
- BFS finds the shortest path in unweighted graphs; Dijkstra's algorithm
  handles weighted edges.
- Real uses include social networks, maps, dependency resolution, and
  recommendation systems.

## References

- Foundational concept; no single source.
- Standard topic in data structure and algorithm textbooks.

## Related Notes

- [[trees-basics]]

## Tags

This note is tagged in the front matter as data-structures, networks,
algorithms.

## Review History

- 2026-08-08: Created as a draft.
