#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ $# -gt 1 ]]; then
  echo "Usage: $0 [path/to/wildcat_fa]" >&2
  exit 1
elif [[ $# -eq 1 ]]; then
  repo="$1"
elif [[ -n "${WILDCAT_REPO:-}" ]]; then
  repo="$WILDCAT_REPO"
elif [[ -f "$root/.wildcat/config/preamble.tex" ]]; then
  repo="$root/.wildcat"
elif [[ -f "$root/../../.wildcat/config/preamble.tex" ]]; then
  repo="$root/../../.wildcat"
elif [[ -d "$root/../../../wildcat_fa" ]]; then
  repo="$root/../../../wildcat_fa"
elif [[ -d "$root/../../../wildcat_theme_fa" ]]; then
  repo="$root/../../../wildcat_theme_fa"
elif [[ -d "$root/../wildcat_fa" ]]; then
  repo="$root/../wildcat_fa"
elif [[ -d "$root/../wildcat_theme_fa" ]]; then
  repo="$root/../wildcat_theme_fa"
else
  echo "Place wildcat_fa beside this repo or set WILDCAT_REPO." >&2
  exit 1
fi

for required in config/preamble.tex theme/beamerthemewildcat.sty theme/wildcat-palettes.tex assets/Aut-logo_en-white.png; do
  if [[ ! -f "$repo/$required" ]]; then
    echo "Wildcat is missing $required: $repo" >&2
    exit 1
  fi
done
repo="$(cd "$repo" && pwd -P)"

for target in "$root/.wildcat" "$root/theme"; do
  if [[ -e "$target" && ! -L "$target" ]]; then
    echo "Refusing to replace an existing file or directory: $target" >&2
    exit 1
  fi
done

link_path() {
  local source="$1" target="$2"
  if [[ -L "$target" && "$(readlink "$target")" == "$source" ]]; then
    return
  fi
  if [[ -L "$target" ]]; then
    rm "$target"
  fi
  ln -sn "$source" "$target"
}
link_path "$repo" "$root/.wildcat"
link_path "$repo/theme" "$root/theme"
