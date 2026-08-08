#!/usr/bin/env python3
"""Validate the PKM repository against pkm/validation.yaml.

Scans every note under knowledge/, research/, projects/, and ideas/ plus
repository-wide structure, and reports all violations. Rules are read from
validation.yaml at runtime, never hardcoded.

Usage: python3 pkm/scripts/validate.py
Exit codes: 0 clean, 1 violations found, 2 error (missing dependency/config).
"""

import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover - depends on runtime environment
    print(
        "PyYAML is required. Install dependencies with:\n"
        "    pip install -r pkm/scripts/requirements.txt",
        file=sys.stderr,
    )
    sys.exit(2)

PKM_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VALIDATION_PATH = os.path.join(PKM_ROOT, "validation.yaml")

NOTE_DIRS = ["knowledge", "research", "projects", "ideas"]
NAV_FILES = {"README.md", "AGENTS.md", "INDEX.md", "SUMMARY.md"}

# Template files intentionally contain placeholder syntax (literal dates like
# YYYY-MM-DD and dummy wiki links) that is replaced on use. They are exempt
# from the created-date format and broken-link checks only; all other checks
# still apply.
TEMPLATE_DIRS = (
    "templates",
    os.path.join("projects", "Templates"),
)

WIKI_LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
EXTERNAL_URL_RE = re.compile(r"https?://[^\s)\]>\"']+", re.IGNORECASE)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PLACEHOLDER_RE = re.compile(r"TODO|lorem ipsum", re.IGNORECASE)

# Reports are grouped under these top-level sections.
SECTION_ORDER = ["knowledge", "research", "projects", "ideas", "structure"]

violations = []  # (section, path, rule, message)
checked_notes = 0


def violation(section, path, rule, message):
    violations.append((section, path, rule, message))


def load_config():
    with open(VALIDATION_PATH, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)
    if not isinstance(cfg, dict):
        raise ValueError("validation.yaml must contain a YAML mapping")
    return cfg


def line_count(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return sum(1 for _ in fh)


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def rel(path):
    return os.path.relpath(path, PKM_ROOT)


def section_of(path):
    parts = rel(path).split(os.sep)
    return parts[0] if parts else "structure"


def is_template_file(path):
    """True when the path lives under a template directory."""
    rel_path = rel(path)
    for template_dir in TEMPLATE_DIRS:
        if rel_path == template_dir or rel_path.startswith(template_dir + os.sep):
            return True
    return False


def iter_note_dirs(root):
    for top in NOTE_DIRS:
        base = os.path.join(root, top)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            full = os.path.join(base, name)
            if os.path.isdir(full):
                yield top, name, full


def list_notes(folder):
    """Return note .md files (nav files excluded) in a category folder."""
    return [
        os.path.join(folder, name)
        for name in sorted(os.listdir(folder))
        if name.endswith(".md") and name not in NAV_FILES
    ]


def parse_frontmatter(raw):
    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing opening '---' delimiter"
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close = i
            break
    if close is None:
        return None, "missing closing '---' delimiter"
    fm_text = "\n".join(lines[1:close])
    try:
        data = yaml.safe_load(fm_text)
    except yaml.YAMLError as exc:
        return None, f"invalid YAML front matter: {exc}"
    if data is None:
        data = {}
    if not isinstance(data, dict):
        return None, "front matter must be a YAML mapping"
    return data, None


def body_without_frontmatter(raw):
    """Return the note content with the front matter block removed."""
    lines = raw.splitlines()
    if not lines or lines[0].strip() != "---":
        return raw
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1:])
    return raw


def check_frontmatter(path, fm_rules, data, skip_date=False):
    for key in fm_rules.get("required_keys", []):
        if key not in data or data[key] is None:
            violation(
                section_of(path), rel(path), "frontmatter",
                f"missing required key '{key}'",
            )
    allowed = fm_rules.get("status", {}).get("allowed", [])
    if "status" in data and allowed and data["status"] not in allowed:
        violation(
            section_of(path), rel(path), "frontmatter",
            f"status '{data['status']}' not in allowed values {allowed}",
        )
    if not skip_date:
        created = data.get("created")
        if created is not None and not DATE_RE.match(str(created)):
            violation(
                section_of(path), rel(path), "frontmatter",
                f"created '{created}' does not match YYYY-MM-DD",
            )
    tags = data.get("tags")
    if tags is None or not isinstance(tags, list) or not tags:
        violation(
            section_of(path), rel(path), "frontmatter",
            "tags must be a non-empty list",
        )


def check_filename(path, naming_rules):
    name = os.path.basename(path)
    pattern = naming_rules.get("note_files", {}).get("pattern")
    if pattern and not re.match(pattern, name):
        violation(
            section_of(path), rel(path), "naming",
            f"filename '{name}' does not match pattern {pattern}",
        )
    max_len = naming_rules.get("note_files", {}).get("max_length")
    if max_len and len(name) > max_len:
        violation(
            section_of(path), rel(path), "naming",
            f"filename '{name}' is {len(name)} chars, over max_length {max_len}",
        )
    forbidden = naming_rules.get("forbidden_characters", [])
    for ch in forbidden:
        if ch in name:
            violation(
                section_of(path), rel(path), "naming",
                f"filename contains forbidden character {ch!r}",
            )


def check_line_count(path, limit, rule_name):
    count = line_count(path)
    if count > limit:
        violation(
            section_of(path), rel(path), rule_name,
            f"file has {count} lines, over limit {limit}",
        )


def check_links(path, body, root, skip_broken=False):
    if not skip_broken:
        for target in WIKI_LINK_RE.findall(body):
            if not link_target_exists(root, target):
                violation(
                    section_of(path), rel(path), "links",
                    f"wiki link [[{target}]] does not resolve to any .md file",
                )
    for url in EXTERNAL_URL_RE.findall(body):
        violation(
            section_of(path), rel(path), "links",
            f"external URL found: {url} (internal_only)",
        )


def link_target_exists(root, target):
    """True if a file named '<target>.md' exists anywhere under root."""
    target_name = target + ".md"
    for dirpath, dirnames, filenames in os.walk(root):
        if target_name in filenames:
            return True
    return False


def check_placeholders(path, body):
    for m in PLACEHOLDER_RE.finditer(body):
        violation(
            section_of(path), rel(path), "content",
            f"placeholder content found: {m.group()!r}",
        )


def check_note(path, cfg, root):
    global checked_notes
    checked_notes += 1
    name = os.path.basename(path)

    check_filename(path, cfg.get("naming", {}))

    raw = read_text(path)
    data, fm_err = parse_frontmatter(raw)
    if fm_err is not None:
        violation(section_of(path), rel(path), "frontmatter", fm_err)
    else:
        check_frontmatter(
            path, cfg.get("frontmatter", {}), data,
            skip_date=is_template_file(path),
        )

    body = body_without_frontmatter(raw)

    notes_limit = cfg.get("line_limits", {}).get("notes")
    if notes_limit:
        check_line_count(path, notes_limit, "line_limits")

    check_links(path, body, root, skip_broken=is_template_file(path))
    check_placeholders(path, body)


def check_structure(cfg, root):
    nav = cfg.get("navigation", {})
    limits = cfg.get("line_limits", {})

    for folder in nav.get("required_folders", []):
        if not os.path.isdir(os.path.join(root, folder)):
            violation("structure", folder, "navigation",
                      "required folder is missing")

    for req in nav.get("root_required_files", []):
        if not os.path.isfile(os.path.join(root, req)):
            violation("structure", req, "navigation",
                      "required root file is missing")

    repo_agents = limits.get("repository_agents")
    if repo_agents and os.path.isfile(os.path.join(root, "AGENTS.md")):
        check_line_count(os.path.join(root, "AGENTS.md"), repo_agents,
                         "line_limits")

    for top, category, folder in iter_note_dirs(root):
        for req in nav.get("folder_required_files", []):
            if not os.path.isfile(os.path.join(folder, req)):
                violation(
                    "structure", rel(folder), "navigation",
                    f"missing required folder file '{req}'",
                )
        agents_path = os.path.join(folder, "AGENTS.md")
        if os.path.isfile(agents_path):
            limit = limits.get("folder_agents")
            if limit:
                check_line_count(agents_path, limit, "line_limits")
        readme_path = os.path.join(folder, "README.md")
        if os.path.isfile(readme_path):
            limit = limits.get("folder_readme")
            if limit:
                check_line_count(readme_path, limit, "line_limits")

    root_files_limit = limits.get("root_files")
    if root_files_limit:
        for name in sorted(os.listdir(root)):
            full = os.path.join(root, name)
            if (
                os.path.isfile(full)
                and name.endswith(".md")
                and name != "AGENTS.md"
            ):
                check_line_count(full, root_files_limit, "line_limits")


def disk_note_count(folder):
    return len(list_notes(folder))


def summary_note_count(summary_path):
    """Parse '<N> notes.' from the '## Current note count' section."""
    if not os.path.isfile(summary_path):
        return None
    try:
        text = read_text(summary_path)
    except OSError:
        return None
    in_section = False
    for line in text.splitlines():
        if line.strip().startswith("## "):
            in_section = "current note count" in line.lower()
            continue
        if in_section:
            m = re.match(r"^\s*(\d+)\s+notes?\.?\s*$", line)
            if m:
                return int(m.group(1))
    return None


def root_index_counts(root):
    """Parse pkm/INDEX.md into {category_path: count}."""
    index_path = os.path.join(root, "INDEX.md")
    counts = {}
    if not os.path.isfile(index_path):
        return counts
    for line in read_text(index_path).splitlines():
        m = re.match(
            r"^\s*-\s*\[[^\]]+\]\(([^)]+)\)\s*[—-]\s*(\d+)\s+notes?\.?\s*$",
            line,
        )
        if m:
            target = m.group(1).replace("/INDEX.md", "")
            counts[target] = int(m.group(2))
    return counts


def check_counts(cfg, root):
    index_counts = root_index_counts(root)
    for top, category, folder in iter_note_dirs(root):
        disk = disk_note_count(folder)
        rel_folder = os.path.relpath(folder, root)
        key = rel_folder.replace(os.sep, "/")
        summary = summary_note_count(os.path.join(folder, "SUMMARY.md"))
        if summary is None:
            violation(
                "structure", rel(folder), "counts",
                "could not parse note count from SUMMARY.md",
            )
        elif summary != disk:
            violation(
                "structure", rel(folder), "counts",
                f"SUMMARY.md says {summary} notes, disk has {disk}",
            )
        if key in index_counts:
            stated = index_counts[key]
            if stated != disk:
                violation(
                    "structure", rel(folder), "counts",
                    f"root INDEX.md says {stated} notes, disk has {disk}",
                )
        else:
            violation(
                "structure", rel(folder), "counts",
                "category not found in root INDEX.md",
            )


def print_report():
    print("=" * 72)
    print("PKM VALIDATION REPORT")
    print("=" * 72)

    by_section = {}
    for item in violations:
        by_section.setdefault(item[0], []).append(item)

    clean_sections = [s for s in SECTION_ORDER if s not in by_section]

    for section in SECTION_ORDER:
        if section not in by_section:
            continue
        print(f"\n## {section}")
        seen = set()
        for sec, path, rule, message in by_section[section]:
            if (path, rule, message) in seen:
                continue
            seen.add((path, rule, message))
            print(f"  FAIL {path} [{rule}] {message}")

    if clean_sections:
        print("\n## structure")
        print("  PASS structure checks")

    total = len(violations)
    print()
    print("=" * 72)
    print(f"{checked_notes} notes checked, {total} violations found")
    print("=" * 72)
    return 1 if total else 0


def main():
    if not os.path.isfile(VALIDATION_PATH):
        print(f"validation.yaml not found at {VALIDATION_PATH}", file=sys.stderr)
        return 2
    try:
        cfg = load_config()
    except Exception as exc:
        print(f"failed to load validation.yaml: {exc}", file=sys.stderr)
        return 2

    for top in NOTE_DIRS:
        base = os.path.join(PKM_ROOT, top)
        if not os.path.isdir(base):
            continue
        for category in sorted(os.listdir(base)):
            folder = os.path.join(base, category)
            if not os.path.isdir(folder):
                continue
            for note in list_notes(folder):
                check_note(note, cfg, PKM_ROOT)

    check_structure(cfg, PKM_ROOT)
    check_counts(cfg, PKM_ROOT)

    return print_report()


if __name__ == "__main__":
    sys.exit(main())
