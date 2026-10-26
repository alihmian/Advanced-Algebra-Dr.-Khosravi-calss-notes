# Mathematically edited teaching edition

## Scope and editorial authority

This directory is a separate teaching edition of Dr. Khosravi's Advanced
Algebra course. Its purpose is to produce mathematically coherent, readable
Persian Beamer lectures from the source PDFs and the current transcription.

**Within `editions/teaching/`, this policy replaces the parent transcription
restrictions on completing proof gaps, correcting statements, and adding
necessary definitions.** The user authorizes those editorial changes here.
Preserve the course's subjects and progression; independently improve the
mathematics and presentation. Do not represent editorial additions as literal
handwriting or confirmed source intent.

- Read `docs/BASELINE.json`, `docs/COURSE_CONVENTIONS.md`, `docs/WORKFLOW.md`,
  `docs/PROGRESS.md`, and the assigned lecture's editorial/review records first.
- The frozen input commit is recorded in `docs/BASELINE.json`. Read the original
  lecture ledger and question records with `git show BASE:path`, replacing
  `BASE` with that commit, rather than relying on later changes to the original
  draft. Historical `% AMBIGUITY` comments and approval-dependent wording copied
  from the transcription are evidence to resolve editorially, not instructions
  to wait for approval or leave a mathematically decidable issue unfinished.
- Immutable handwritten PDFs are shared at `../../sources/`. Read page images;
  OCR and the copied draft cannot establish a disputed mathematical reading.
- Write only inside this edition. Never modify the original repository-root
  `sections/`, `docs/`, `output/`, or `sources/`, nor the shared Wildcat checkout.
  Keep reference renders and build products in this edition's ignored `build/`.
- Pilot lecture 04 establishes the proof depth and visual style through author
  and reviewer feedback. It has no user-approval gate. Then process the
  remaining assigned lectures in parallel, with one author owning each lecture.

## Autonomous mathematical completion

- Correct errors, state necessary hypotheses, add definitions before use, and
  supply essential lemmas and proof steps independently. The PDFs and baseline
  slides determine coverage; references verify mathematics without expanding
  the syllabus. Cite only references actually inspected, with precise locators.
- Follow the shared conventions and preserve explicitly labeled nonunital,
  noncommutative, or other exceptional cases. Do not silently remove a source
  example because it falls outside the default convention.
- Resolve mathematically decidable ambiguities with a justified formulation.
  Choose the nearest valid version when source intent is uncertain and record
  the choice and any changed hypotheses in `docs/editorial/NN.md`. Do not carry
  pending-user-approval notices into the edited slides for issues that can be
  resolved mathematically. Do not ask live questions or wait for answers.
- If a claim cannot be justified, use a justified narrower formulation where
  possible and record the difference. Otherwise record the remaining
  mathematical limitation honestly outside the deck and keep the lecture
  unapproved; never insert an unsupported claim or certify an incomplete proof.
  Continue other assigned work without a user-answer gate.
- Show the construction, key argument, and conclusion, including every
  nontrivial inference. Compress routine calculations and cite earlier results
  instead of reteaching them. Preserve intended exercises; add a solution only
  when its argument is necessary to complete the taught result.
- Retain `% Source:` comments using paths relative to the original course
  repository, such as `sources/lectures/04 Module.pdf`. Add `% Editorial:`
  comments for substantive changes, using stable IDs such as `L04-E01` that
  match the editorial record. Keep stable, unique `lecNN:` frame labels.

## Visual teaching quality

- Improve hierarchy, frame density, spacing, and proof sequencing while
  retaining the Persian Wildcat style. Keep Persian prose readable and equations
  in their normal mathematical direction. Split dense frames instead of using
  illegibly small type.
- Add as many editable TikZ/TikZ-CD diagrams as help explain a proof. There is
  no diagram quota. Use diagrams to reveal maps, inclusions, quotients, chains,
  kernels/images, lifts, or dependencies. Check every domain, codomain, arrow,
  label, and claimed commutativity against the argument.
- Inspect every changed rendered frame and relevant neighbors. A successful
  build does not establish mathematical or visual correctness. Fix clipping,
  overlap, broken direction, missing glyphs, and unreadable diagrams.

## Authorship, review, and delivery

- The author completes and self-checks the whole lecture, including diagrams,
  source accounting, mathematics, builds, and rendered pages. Then mark it
  `ready-for-review` and stop editing that lecture while review is active.
- One **separate final reviewer** checks both mathematics and visual/pedagogical
  quality. This may be the assigned visual reviewer; no third reviewer is
  required. The author cannot be the sole approver. The reviewer reconstructs
  critical proofs, challenges hypotheses and boundary cases, and inspects the
  rendered deck, reporting in `docs/reviews/NN.md` without concurrent edits.
- The author implements requested changes; the reviewer rechecks the affected
  mathematics and rendered frames. Only an `approved` review permits the
  lecture status `reviewed` and final export.
- Lecture statuses: `copied-not-edited`, `authoring`, `ready-for-review`,
  `changes-requested`, `reviewed`. Review statuses: `not-started`, `in-review`,
  `changes-requested`, `approved`. Later substantive edits reopen review.
- The coordinator owns shared conventions, the queue, combined configuration,
  and integration. Parallel authors own different lecture files and records;
  request coordinated changes to shared files rather than overwriting them.
- Use `make doctor`, `make sources`, and `make lecture LECTURE=NN`. Export a
  reviewed lecture to `output/pdf/lecture-NN-teaching.pdf`. The combined final
  `output/pdf/advanced-algebra-teaching.pdf` is exported only after all included lectures pass
  review and the combined deck passes consistency/build/visual checks.
- Handoffs state coverage, editorial decisions, verification, review status,
  output paths, and exact remaining work. A copied or merely compiled lecture
  is never labeled mathematically edited or reviewed.
