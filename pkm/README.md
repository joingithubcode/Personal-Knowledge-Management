# Personal Knowledge Management (PKM)

A personal, lifelong knowledge repository. This system stores what you
learn, research, build, and think about, in plain Markdown that humans and
AI can both use for years.

## Purpose

Capture and organize personal knowledge so it is:

- Durable: plain Markdown, no vendor lock-in.
- Reusable: every note is a self-contained unit of meaning.
- Searchable: consistent naming, YAML, and links.
- AI friendly: predictable structure machines can read and assist with.

## Scope

- Personal learning notes, research, project knowledge, and ideas.
- Long-term storage of knowledge that survives any single tool.

## Structure

```
pkm/
├── README.md          This file
├── SUMMARY.md         Map of the whole repository
├── INDEX.md           Master index of every note
├── CHANGELOG.md       History of changes
├── GLOSSARY.md        Terms used across the repository
├── AGENTS.md          Working rules for AI agents and editors
├── validation.yaml    Machine-readable validation rules
├── STANDARDS.md               Consolidated standards
├── WORKFLOW.md                Consolidated workflows
├── AI-GUIDE.md                AI usage guide
├── CONTRIBUTING.md            Contribution workflow
├── knowledge/         Permanent, organized knowledge
├── research/          In-progress inquiries and sources
├── projects/          Knowledge attached to personal projects
└── ideas/             Unformed thoughts awaiting refinement
```

## How to navigate

- Start at SUMMARY.md for the big picture.
- Use INDEX.md to locate any note.
- Read AGENTS.md before editing or creating notes.
- Run validation checks against validation.yaml before committing.

## System documents

- STANDARDS.md — how every note is structured, written, named, linked, and tagged.
- WORKFLOW.md — how notes move through the lifecycle.
- AI-GUIDE.md — how AI agents read and update the repository.
- CONTRIBUTING.md — the contribution workflow.

Each document covers one responsibility. Read the relevant one before
creating or editing a note.

## Quick start

1. Read AGENTS.md.
2. Read SUMMARY.md.
3. Add your first note to the right folder.
4. Register it in INDEX.md and SUMMARY.md.

## Setup

Enable the pre-commit validation gate after cloning:

```sh
bash pkm/scripts/install-hooks.sh
```

Run it once. It copies `pkm/scripts/hooks/pre-commit` into `.git/hooks/`
and makes it executable, so `pkm/scripts/validate.py` runs before every
commit and blocks the commit if any validation violations are found.

## Status

Foundation stage: structure only. No knowledge documents exist yet.
