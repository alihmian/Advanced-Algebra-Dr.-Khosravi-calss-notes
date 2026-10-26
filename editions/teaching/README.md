# Advanced Algebra: mathematically edited teaching edition

This is a separate editable copy of the source-backed draft, frozen from
commit `5db5b6e74bdf618a9a5e45bb3ddb9bbb53ca50d2` on 2026-10-26. Its copied slides are starting material,
not completed mathematical edits. The original transcription remains at the
repository root and must not be edited by teaching-edition agents.

Read [AGENTS.md](AGENTS.md), [course conventions](docs/COURSE_CONVENTIONS.md),
[workflow](docs/WORKFLOW.md), and [the work queue](docs/PROGRESS.md).
The user authorizes independent mathematical corrections, necessary definitions,
essential proof completion, improved slide design, and helpful editable diagrams.
Use source PDFs and the baseline slides to determine scope. No live questions
or user-answer prerequisite applies to this edition.

## Inputs and separation

- The original 21 immutable PDFs remain in `../../sources/lectures/`.
- Source inventory: [manifest](../../sources/manifest.json).
- [Baseline metadata](docs/BASELINE.json) records the exact starting commit and
  copied-file hashes. Read frozen original ledgers with `git show BASE:docs/lectures/NN.md`.
- `sections/` and `config/` here are independent copies. Build files are local
  to this edition's ignored `build/`; shared theme assets are linked read-only.
- `docs/editorial/NN.md` records source coverage and mathematical decisions.
- `docs/reviews/NN.md` is written by a separate final reviewer checking both
  mathematics and visual/pedagogical quality after the author self-check.

## Build

Run these commands from this directory:

```sh
make doctor
make lecture LECTURE=04
python3 scripts/lectures.py render 04 --page 1
make slides
```

The helper prints `build/lecture-04.pdf`. The combined build is
`build/advanced-algebra-teaching.pdf`; it can contain unreviewed lectures until
the entire queue is done. Successful compilation does not establish review.
After independent approval, export the reviewed lecture as
`output/pdf/lecture-04-teaching.pdf` and record the review evidence. Export the
combined reviewed course as `output/pdf/advanced-algebra-teaching.pdf` only
after all lecture reviews and the course-wide consistency check pass.

## Execution

Pilot lecture 04 calibrates mathematical depth and proof-diagram style through
internal author/reviewer feedback. Then edit remaining lectures in parallel,
with one author per lecture and one independent final reviewer per stable draft.
The same final reviewer can check mathematics and visuals; a third reviewer is
not required. The coordinator owns shared conventions/configuration and queue
updates. See the workflow for acceptance criteria and handoffs.
