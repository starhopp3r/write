#!/bin/sh
# Install the skills in this repo for Claude Code as personal skills.
#
#   ./install.sh                   install every skill (write, write-academic)
#   ./install.sh write-academic    install only the skills you name
#   ./install.sh --link ...        link to this folder, so edits here take effect at once
#   ./install.sh --force ...       replace an existing install
set -e

root="$(cd "$(dirname "$0")" && pwd)"
dest_root="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
link=0
force=0
names=""
for arg in "$@"; do
  case "$arg" in
    --link) link=1 ;;
    --force) force=1 ;;
    -*) echo "Unknown option: $arg" >&2; exit 2 ;;
    *) names="$names $arg" ;;
  esac
done
[ -n "$names" ] || names="$(ls "$root/skills")"

status=0
mkdir -p "$dest_root"
for name in $names; do
  src="$root/skills/$name"
  dest="$dest_root/$name"
  if [ ! -f "$src/SKILL.md" ]; then
    echo "There is no skill named $name in $root/skills." >&2
    status=2
    continue
  fi
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    if [ "$force" -eq 0 ]; then
      echo "$dest already exists. Run again with --force to replace it." >&2
      status=1
      continue
    fi
    rm -rf "${dest:?}"
  fi
  if [ "$link" -eq 1 ]; then
    ln -s "$src" "$dest"
    echo "Linked $dest -> $src"
  else
    cp -R "$src" "$dest"
    echo "Copied $name to $dest"
  fi
done
echo "Start a new Claude Code session to use the new skills."
exit $status
