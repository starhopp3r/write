#!/bin/sh
# Make one zip for each skill in dist/, for upload to claude.ai
# (Settings > Capabilities > Skills).
set -e

root="$(cd "$(dirname "$0")" && pwd)"

# Each skill carries its own copy of the checker, so that it works on its own.
# Stop if the copies have drifted apart.
first=""
for script in "$root"/skills/*/scripts/check.py; do
  if [ -z "$first" ]; then
    first="$script"
  elif ! cmp -s "$first" "$script"; then
    echo "$script differs from $first. Copy one over the other, then run again." >&2
    exit 1
  fi
done

mkdir -p "$root/dist"
for dir in "$root"/skills/*/; do
  name="$(basename "$dir")"
  rm -f "$root/dist/$name.zip"
  (cd "$root/skills" && zip -r -X "$root/dist/$name.zip" "$name" -x '*/__pycache__/*' '*.DS_Store' >/dev/null)
  echo "Made $root/dist/$name.zip"
done
