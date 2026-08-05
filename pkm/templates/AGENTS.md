# AGENTS.md — templates/

Working rules for humans, editors, and AI agents working in the templates
folder. This folder holds the reusable note skeletons for the repository.

## Folder Mission

Provide a consistent, validated starting shape for every new note, so all
content follows one structure that humans and AI can rely on.

## Responsibilities

- Maintain one template per content folder.
- Keep templates in sync with validation.yaml and the root AGENTS.md.
- Keep every template under 100 lines.
- Make templates copy-ready for creating real notes.

## Boundaries

- Templates only; never actual notes or sample content.
- Do not add placeholders that look like real content.
- Do not modify content folders from here.
- Do not store anything that is not a note skeleton.

## Documentation Rules

- Every template contains: front matter, Purpose, Context, Main Notes,
  References, Related Notes, Tags, Review History.
- Keep section order identical across all templates.
- Write section headers exactly as defined in the root AGENTS.md.
- Never include completed example knowledge.

## YAML Rules

- Use complete front matter: title, status, created, tags.
- Status must be draft, active, complete, or archived.
- Use YYYY-MM-DD dates and lowercase tags.
- Match the title to the eventual note filename.
- Keep the optional keys related and source when relevant.

## Navigation Rules

- Do not link templates to actual notes.
- Use generic headings only; no repository-specific targets.
- Keep this folder registered in INDEX.md and SUMMARY.md.
- Keep this README as the folder entry point.

## Validation Rules

- Run all checks from validation.yaml before finishing.
- Verify front matter, naming, and line counts.
- Confirm template files stay under 100 lines.
- Confirm no real notes were created by mistake.

## Editing Rules

- Edit templates when rules in validation.yaml change.
- Propagate rule changes to every template at once.
- Keep the four templates structurally parallel.
- Keep language neutral and reusable across all years.

## Recovery Workflow

- Restore lost templates from git history.
- Recreate a template from the root AGENTS.md sections.
- Align any drifted template back to validation.yaml.
- Confirm all four templates still match after recovery.

## Common Mistakes

- Writing sample content inside a template.
- Diverging section order between templates.
- Using statuses or dates not allowed by validation.yaml.
- Letting a template exceed 100 lines.
- Creating real notes while testing a template.
- Forgetting to sync templates with rule changes.
