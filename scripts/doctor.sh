#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
failed=0
for tool in python3 latexmk xelatex kpsewhich pdfinfo pdftoppm; do
  if command -v "$tool" >/dev/null 2>&1; then
    echo "OK $tool: $(command -v "$tool")"
  else
    echo "MISSING $tool (see README.md for setup)" >&2
    failed=1
  fi
done

if command -v kpsewhich >/dev/null 2>&1; then
  for package in beamer.cls xepersian.sty unicode-math.sty tikz-cd.sty tcolorbox.sty; do
    if [[ -n "$(kpsewhich "$package")" ]]; then
      echo "OK TeX package: $package"
    else
      echo "MISSING TeX package: $package" >&2
      failed=1
    fi
  done
fi

for file in .wildcat/config/preamble.tex theme/beamerthemewildcat.sty theme/wildcat-palettes.tex .wildcat/assets/Aut-logo_en-white.png; do
  if [[ -f "$root/$file" ]]; then
    echo "OK theme asset: $file"
  else
    echo "MISSING theme asset: $file (run make theme)" >&2
    failed=1
  fi
done

echo "The build also requires XB Roya and the Wildcat theme's bundled fonts."
echo "Compile a lecture to verify font loading and the full TeX dependency chain."
exit "$failed"
