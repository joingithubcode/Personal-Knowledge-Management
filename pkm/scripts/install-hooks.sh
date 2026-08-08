#!/bin/sh
# Installs the PKM pre-commit validation hook.
#
# Copies pkm/scripts/hooks/pre-commit into .git/hooks/pre-commit (and makes
# it executable) so the validation gate runs before every commit.
#
# Usage:
#   bash pkm/scripts/install-hooks.sh
#
# Run this once after cloning. The hook can be reinstalled at any time; it
# just overwrites the local copy with the versioned hook.

set -e

script_dir=$(cd "$(dirname "$0")" && pwd)
repo_root=$(cd "$script_dir/../.." && pwd)

source_hook="$script_dir/hooks/pre-commit"
target_hook="$repo_root/.git/hooks/pre-commit"

if [ ! -f "$source_hook" ]; then
    echo "error: versioned hook not found: $source_hook" >&2
    exit 1
fi

if [ ! -d "$repo_root/.git/hooks" ]; then
    echo "error: not inside a git repository ($repo_root/.git/hooks missing)" >&2
    exit 1
fi

cp "$source_hook" "$target_hook"
chmod +x "$target_hook"

echo "Installed PKM pre-commit hook: $target_hook"
echo "The validation gate is now active for every commit."
