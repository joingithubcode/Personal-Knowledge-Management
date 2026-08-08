# INDEX — System-Design

Registry and organizational plan for the System-Design category in the knowledge
section.

## Category purpose

Durable knowledge about designing large, reliable software systems.

## Scope

Architecture patterns, scalability, reliability, and design trade-offs.

Notes here follow the repository's atomic note rules and the standards in
DOCUMENTATION-STANDARDS.md.

## Naming rules

- Lowercase, hyphenated filenames under 60 characters, ending in .md.
- No spaces, uppercase, underscores, or dates at the start of a name.
- Titles in front matter and headings match the filename.
- Never use fake or example filenames.

## Note organization strategy

- One atomic note per topic; never merge topics.
- Register every note below, one line per note.
- Entries follow: `note-name — one-line description`.
- Sort entries alphabetically by note name.

## Tagging guidance

- Use 2 to 5 lowercase tags per note.
- Prefer existing tags over inventing new ones.
- Tag the topic, never the status or the index.

## Navigation policy

- README.md: category overview, purpose, and scope.
- AGENTS.md: working rules for this category.
- SUMMARY.md: category map and current note count.
- Keep this index in sync with SUMMARY.md and the repository INDEX.md.

## Related categories

- [Software-Engineering](../Software-Engineering/README.md)
- [Databases](../Databases/README.md)
- [Cloud](../Cloud/README.md)
- [Networking](../Networking/README.md)

## Note registry

- api-gateway-basics — a single front door to services
- caching-strategies — fast reads with fresh data
- database-sharding — scaling data across databases
- horizontal-vs-vertical-scaling — growing capacity two ways
- load-balancing-basics — spreading traffic across servers
- message-queues-basics — decoupling producers and consumers
- monolith-vs-microservices — one app or many services
- rate-limiting-basics — capping request traffic
