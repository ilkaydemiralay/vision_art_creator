#!/usr/bin/env bash
# vision_art_creator — remove creator-* skill symlinks from Claude Code or Codex skills dir.
#
# Only removes symlinks that point back into this repo. Will not delete a real
# directory or a symlink that points somewhere else, unless --force is passed.
#
# Usage:
#   ./uninstall.sh                  # remove from ~/.claude/skills/
#   ./uninstall.sh --target <dir>   # remove from a different skills dir
#   ./uninstall.sh --codex          # remove from ~/.agents/skills/ (OpenAI Codex)
#   ./uninstall.sh --force          # remove even non-symlinks / foreign links

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

removed=0
skipped=0
for src in "$SKILLS_SRC"/*/; do
  name="$(basename "$src")"
  dest="$TARGET/$name"

  if [[ ! -e "$dest" && ! -L "$dest" ]]; then
    continue
  fi

  if [[ -L "$dest" ]]; then
    link_target="$(readlink "$dest")"
    # Resolve link_target relative to TARGET if it is relative
    case "$link_target" in
      /*) abs="$link_target" ;;
      *)  abs="$TARGET/$link_target" ;;
    esac
    # Normalize trailing slash
    abs="${abs%/}"
    src_norm="${src%/}"
    if [[ "$abs" == "$src_norm" || "$FORCE" -eq 1 ]]; then
      rm "$dest"
      echo "remove $name"
      removed=$((removed+1))
    else
      echo "skip   $name  (link points to $link_target, not this repo)  use --force to remove"
      skipped=$((skipped+1))
    fi
  else
    if [[ "$FORCE" -eq 1 ]]; then
      rm -rf "$dest"
      echo "remove $name  (was real directory)"
      removed=$((removed+1))
    else
      echo "skip   $name  (real directory, not a symlink)  use --force to remove"
      skipped=$((skipped+1))
    fi
  fi
done

echo
echo "Done. removed=$removed  skipped=$skipped  target=$TARGET"
