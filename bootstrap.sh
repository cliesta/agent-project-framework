#!/usr/bin/env bash
set -euo pipefail

target="${1:?Usage: bootstrap.sh <target-directory>}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -d "$target" ]]; then
    shopt -s dotglob nullglob
    entries=("$target"/*)
    if (( ${#entries[@]} > 0 )); then
        echo "Cannot install into a non-empty directory: $target" >&2
        exit 1
    fi
elif [[ -e "$target" || -L "$target" ]]; then
    echo "Target is not a directory: $target" >&2
    exit 1
fi

mkdir -p "$target/.agent-framework"

cp "$root/skeleton/AGENTS.md" "$target/AGENTS.md"
cp "$root/skeleton/.agent-framework/"*.md "$target/.agent-framework/"
cp "$root/skeleton/templates/project.md" "$target/project.md"
cp "$root/skeleton/templates/project-rules.md" "$target/project-rules.md"
cp "$root/skeleton/templates/wip.md" "$target/wip.md"

echo "Installed agent framework into: $target"
