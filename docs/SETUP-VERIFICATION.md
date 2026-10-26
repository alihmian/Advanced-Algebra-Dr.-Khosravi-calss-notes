# Setup verification: 2026-10-25

This records repository/workflow checks, not a mathematical transcription audit.
No source page is marked checked and no lecture is marked complete by this setup.
Existing slide content and commented blocks were preserved.

## Checks performed

- All 21 user-supplied PDFs were copied into `sources/lectures/` without changing
  their bytes. Source/copy SHA-256 hashes agree. The manifest inventories 20
  numbered lectures, 193 PDF pages including both lecture 15 versions, and
  139,471,004 bytes. `make check-sources` also verifies page counts with pdfinfo.
- `make doctor` passed for the current environment: Python, XeLaTeX, latexmk,
  selected core TeX packages, Poppler tools, and linked theme assets.
- `make lecture LECTURE=04` compiled `build/lecture-04.pdf`, 19 pages. All 19
  rendered preview pages were inspected for visible layout issues; no clipping,
  overlaps, or unreadable math were observed. This does not verify fidelity to
  the handwriting or coverage of lecture 04.
- `make slides` compiled `build/advanced-algebra-slides.pdf`, 229 pages. The
  combined deck remains the existing draft; it was not audited page by page.
- Source rendering, lecture lookup, Python/shell syntax, and whitespace checks
  passed. Lecture 15 rendering without an explicit variant is rejected; a build
  of lecture 13 with no slide source is rejected rather than creating a
  misleading empty lecture preview.
- The 20 ledgers account for all 193 source pages. Every page starts `unchecked`.
  Lecture status remains `existing-draft-unverified` for 01-12 and `not-started`
  for 13-20. Lecture 15's version-selection question is recorded for its future
  transcription session.

## Context for future work

- Current source-to-section associations are provisional. Section 1 includes
  Zorn material, and adjacent lectures can overlap. Reconcile against images.
- Section 4 has substantial commented-out introductory module material; active
  slides begin with generated submodules. Its ledger records this for review.
- The combined build log contains three small horizontal overflow reports
  (approximately 0.5-0.9 pt), font-size-in-math warnings, underfull boxes, and
  package/PDF bookmark warnings. Compilation succeeds. Check relevant frames
  when editing them; this setup does not claim to fix existing content warnings.
- The external Wildcat checkout is based on
  `be4cddc2d7a912f35f567701927076bf1ffb869a` with preexisting local changes.
  Those files were not edited. A clean checkout of that commit alone may differ
  in appearance; see the README for obtaining/linking the shared theme.
- Build products and rendered images are ignored. The source PDFs, manifest,
  agent instructions, lecture ledgers, and helper scripts are intended to be
  versioned. The preexisting repository reorganization was not committed or
  reverted as part of setup.
