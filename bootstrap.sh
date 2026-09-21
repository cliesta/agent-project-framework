#!/usr/bin/env bash
set -euo pipefail

target="${1:?Usage: bootstrap.sh <target-directory>}"
root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$target/.agent-framework"

cp "$root/AGENTS.md" "$target/AGENTS.md"
cp "$root/framework/"*.md "$target/.agent-framework/"
cp "$root/templates/project.md" "$target/project.md"
cp "$root/templates/project-rules.md" "$target/project-rules.md"
cp "$root/templates/wip.md" "$target/wip.md"

echo "Installed agent framework into: $target"