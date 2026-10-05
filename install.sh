#!/usr/bin/env bash
# vision_art_creator — install creator-* skills into Claude Code or Codex skills dir.
#
# Strategy: symlink each skill from this repo into ~/.claude/skills/.
# Running `git pull` in this repo then instantly updates all installed skills.
#
# Usage:
#   ./install.sh                  # install into ~/.claude/skills/
#   ./install.sh --target <dir>   # install into a different skills dir
#   ./install.sh --codex          # install into ~/.agents/skills/ (OpenAI Codex)
#   ./install.sh --force          # overwrite existing symlinks/dirs

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$REPO_DIR/skills"
TARGET="${HOME}/.claude/skills"
FORCE=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --codex)  TARGET="${HOME}/.agents/skills"; shift ;;
    --force)  FORCE=1; shift ;;
    -h|--help)
      sed -n '2,12p' "$0"
      exit 0
      ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [[ ! -d "$SKILLS_SRC" ]]; then
  echo "ERROR: $SKILLS_SRC not found." >&2
  exit 1
fi

mkdir -p "$TARGET"

installed=0
skipped=0
for src in "$SKILLS_SRC"/*/; do
  name="$(basename "$src")"
  dest="$TARGET/$name"

  if [[ -e "$dest" || -L "$dest" ]]; then
    if [[ "$FORCE" -eq 1 ]]; then
      rm -rf "$dest"
    else
      existing="$(readlink "$dest" 2>/dev/null || echo "<dir>")"
      echo "skip   $name  (already exists → $existing)  use --force to overwrite"
      skipped=$((skipped+1))
      continue
    fi
  fi

  ln -s "$src" "$dest"
  echo "link   $name"
  installed=$((installed+1))
done

echo
echo "Done. installed=$installed  skipped=$skipped  target=$TARGET"
echo "Update later with:  cd $REPO_DIR && git pull"
