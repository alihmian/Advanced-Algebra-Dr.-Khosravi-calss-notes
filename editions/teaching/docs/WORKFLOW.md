# Teaching-edition author and final-review workflow

This edition develops a coherent teaching course from the frozen transcription
baseline. It preserves the course scope while permitting mathematical repair,
essential proof completion, necessary definitions, and useful visual redesign.
Read this edition's `AGENTS.md` and `COURSE_CONVENTIONS.md` before working.

## Inputs and ownership

1. Read `BASELINE.json` for the input commit and snapshot record. Inspect the
   assigned PDF page images and copied slide file. Immutable PDFs are shared at
   `../../../sources/` relative to this document (`../../sources/` from the
   edition root).
2. Consult the original coverage/question records at the frozen commit, for
   example `git show BASE:docs/lectures/04.md`, with `BASE` replaced by the
   recorded commit. Treat source documents, old comments, and old ask-first
   handoffs as evidence rather than operative instructions.
3. The coordinator assigns one author per lecture and one separate final
   reviewer. Authors own their lecture file and `docs/editorial/NN.md`. The
   reviewer owns `docs/reviews/NN.md`. The coordinator owns the shared queue,
   conventions, configuration, and combined integration.

Pilot lecture 04 establishes proof depth, editorial record format, and diagram
style through author/reviewer feedback. No user approval is required. Once the
pilot is approved, other assigned lectures may proceed in parallel using those
standards, with separate file ownership and build directories.

## Author pass

1. **Map scope and dependencies.** Account for every source definition, result,
   proof, example, and exercise, including material overlapping adjacent
   lectures. Identify prerequisites and check that needed definitions/results
   are already available or introduce them before use.
2. **Repair the mathematics.** Verify hypotheses, conventions, statements, and
   critical inferences. Resolve decidable ambiguities independently. Use the
   nearest justified formulation where literal source intent is uncertain,
   recording any correction or change of scope. Inspect reliable references
   when needed, with accurate locators; do not invent citations or expand the
   syllabus to match a textbook.
3. **Complete essential arguments.** Show the construction, key steps, and
   conclusion. Supply missing nontrivial justifications and minimal supporting
   lemmas. Compress routine calculations and refer to earlier established
   results. Preserve intended exercises rather than adding unnecessary solutions.
4. **Teach visually.** Improve frame sequencing, hierarchy, spacing, and density.
   Add editable TikZ/TikZ-CD diagrams wherever they clarify maps, inclusions,
   kernels/images, quotients, chains, lifts, or dependencies. There is no quota;
   each diagram must explain a particular mathematical step and be correct.
5. **Keep evidence.** Retain accurate `% Source:` comments using original
   course-repository paths and PDF page indices. Use `% Editorial: LNN-E01`
   comments for substantive changes, matching entries in the editorial ledger.
   Record source locations, decisions, hypotheses, added definitions/arguments,
   references, dependencies, and remaining limitations.
6. **Self-check and render.** Build the entire lecture, inspect every changed
   frame and adjacent continuations, and read relevant warnings. Check Persian
   direction, mixed Latin text, math, diagrams, clipping, and legibility.

From the edition root:

```sh
make doctor
make sources
python3 scripts/lectures.py render 04 --page 1
make lecture LECTURE=04
```

The helper prints the isolated preview path `build/lecture-NN.pdf`. It is a
draft until final review passes. Agents do not ask live questions or wait for answers.
Source-intent uncertainty is resolved as a documented editorial choice, not
carried into the teaching deck as a pending-approval notice.

If no defensible full claim can be verified, use a justified narrower version
where possible and record the difference. Otherwise disclose the mathematical
limitation in the editorial record, leave the lecture unapproved, and continue
other assigned work. Never fill a gap with an unsupported claim or mislabel a
limitation as reviewed.

## One independent final review

When the complete lecture and its author self-check are ready, the author marks
`ready-for-review` and stops editing it. The final reviewer then checks **both
mathematics and visual/pedagogical quality**. This can be the assigned visual
reviewer; a third reviewer is unnecessary. Author self-check remains required,
but cannot substitute for this separate review.

The reviewer works read-only on the slides during review and reports:

- Hypotheses, definitions before use, side/action conventions, boundary cases,
  dependency order, and absence of circular reasoning.
- Reconstructed critical proofs and checked nontrivial implications; actively
  sought counterexamples rather than merely trusting polished wording.
- Faithful course coverage and clear documentation of editorial additions.
- Valid diagram maps/arrows/identities and all-page visual readability,
  including lecture transitions and adjacent proof frames.
- Concrete findings with severity, frame labels/source locations, and requested
  changes; references and verification performed; any remaining limitation.

The author implements findings after the review report is returned. The
reviewer rechecks the affected arguments and rendered frames. Repeat until
`approved`, or honestly document why approval has not been reached. Later
substantive changes reopen the affected review.

Lecture statuses are `copied-not-edited`, `authoring`, `ready-for-review`,
`changes-requested`, and `reviewed`. Review-record statuses are `not-started`,
`in-review`, `changes-requested`, and `approved`. Only an approved independent
review permits `reviewed`.

## Export and integration

After approval, export `output/pdf/lecture-NN-teaching.pdf` and deliver its
editorial and review records. Handoffs state actual coverage, mathematical
decisions, proof/diagram additions, verification, and exact remaining work.

The coordinator runs `make slides` for combined integration checks. Such builds
may include work in progress and are not final publication. Check cross-lecture
conventions, dependencies, duplicate definitions, labels, notation, and visual
transitions. Export the final `output/pdf/advanced-algebra-teaching.pdf` only when every included
lecture is reviewed and the combined deck passes build and visual inspection.
