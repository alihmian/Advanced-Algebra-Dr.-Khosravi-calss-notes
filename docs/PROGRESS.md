# Lecture progress

The work unit is one numbered lecture PDF. The table and individual ledgers
record the current source coverage and verification state as lectures progress.

**Questions are for later review, not a waiting state.** Record ambiguities in
the separate questions PDF and finish all other transcription/build/review work
without asking live questions or requiring answers. A pass marked
`transcribed-with-open-questions` is finished for delivery and sequencing;
continue to the next assigned lecture. It does not claim that unresolved
mathematics is settled. Older obtain-answers-first handoffs are superseded.

Use [the transcription workflow](TRANSCRIPTION.md), then open the lecture ledger.
Each ledger tracks every 1-based PDF page, source/frame evidence, questions for the
user, and an exact resume point. Topic overlap across PDFs remains part of each
PDF’s scope and must be accounted for explicitly.

| Lecture | Topic | PDF pages | Status | Ledger | Slide source |
| --- | --- | --- | --- | --- | --- |
| 01 | Introduction | 18 | `existing-draft-unverified` | [01](lectures/01.md) | [`section1.tex`](../sections/section1.tex) |
| 02 | Zorn's Lemma | 5 | `existing-draft-unverified` | [02](lectures/02.md) | [`section2.tex`](../sections/section2.tex) |
| 03 | Introduction, continued | 3 | `existing-draft-unverified` | [03](lectures/03.md) | [`section3.tex`](../sections/section3.tex) |
| 04 | Modules | 11 | `transcribed-with-open-questions` | [04](lectures/04.md) | [`section4.tex`](../sections/section4.tex) |
| 05 | Maximal Submodules | 8 | `in-progress` | [05](lectures/05.md) | [`section5.tex`](../sections/section5.tex) |
| 06 | Simple and Semisimple Modules | 8 | `transcribed-with-open-questions` | [06](lectures/06.md) | [`section6.tex`](../sections/section6.tex) |
| 07 | Homomorphisms | 8 | `transcribed-with-open-questions` | [07](lectures/07.md) | [`section7.tex`](../sections/section7.tex) |
| 08 | Direct Sums | 6 | `transcribed-with-open-questions` | [08](lectures/08.md) | [`section8.tex`](../sections/section8.tex) |
| 09 | Free Modules | 4 | `transcribed-with-open-questions` | [09](lectures/09.md) | [`section9.tex`](../sections/section9.tex) |
| 10 | Noetherian and Artinian Modules | 8 | `transcribed-with-open-questions` | [10](lectures/10.md) | [`section10.tex`](../sections/section10.tex) |
| 11 | Noetherian and Artinian Modules, continued | 8 | `transcribed-with-open-questions` | [11](lectures/11.md) | [`section11.tex`](../sections/section11.tex) |
| 12 | Noetherian and Artinian Rings | 12 | `transcribed-with-open-questions` | [12](lectures/12.md) | [`section12.tex`](../sections/section12.tex) |
| 13 | Length of a Module | 8 | `transcribed-with-open-questions` | [13](lectures/13.md) | [`section13.tex`](../sections/section13.tex) |
| 14 | Primitive Rings | 5 | `transcribed-with-open-questions` | [14](lectures/14.md) | [`section14.tex`](../sections/section14.tex) |
| 15 | Jacobson Radical | 16 + 13 (variants) | `transcribed-with-open-questions` | [15](lectures/15.md) | [`section15.tex`](../sections/section15.tex) |
| 16 | Nakayama's Lemma and Exact Sequences | 9 | `transcribed-with-open-questions` | [16](lectures/16.md) | [`section16.tex`](../sections/section16.tex) |
| 17 | Injective and Projective Modules | 11 | `transcribed-with-open-questions` | [17](lectures/17.md) | [`section17.tex`](../sections/section17.tex) |
| 18 | Injective and Projective Modules, continued | 7 | `transcribed-with-open-questions` | [18](lectures/18.md) | [`section18.tex`](../sections/section18.tex) |
| 19 | Tensor Products | 12 | `transcribed-with-open-questions` | [19](lectures/19.md) | [`section19.tex`](../sections/section19.tex) |
| 20 | Tensor Products, continued | 13 | `complete` | [20](lectures/20.md) | [`section20.tex`](../sections/section20.tex) |
| 22 | Source not located | Unknown | `not-started` (source unavailable) | [22](lectures/22.md) | Not created |

Lecture 22 source lookup (2026-10-25): the requested PDF was not found in the
repository, original local course folder, nearby user source locations, or
connected Advanced Algebra Google Drive folder. Available numbered sources end
at 20. No transcription or build was possible; no placeholder slides or empty
questions PDF were generated. The [lecture 22 ledger](lectures/22.md) records
the search evidence and exact resume point when its source becomes available.

Lecture 06: all eight source pages visually inspected; five fully checked and
pages 3–5 retain deferred L06-Q01/L06-Q02. The 17 content slides are in the repository.
Review its [separate questions PDF](../output/pdf/lecture-06-questions.pdf) and
[ledger](lectures/06.md) for the two pending decisions.

Lecture 09 handoff (2026-10-25): all four pages are reconciled into 15 content
frames; pages 2 and 4 are checked, and pages 1 and 3 retain L09-Q01/Q02 in the
[two-page ambiguity PDF](../output/pdf/lecture-09-questions.pdf). Isolated,
questions, combined, and visual checks passed. Deliver the pass with those
questions deferred and continue the assigned work queue. If answers are later
supplied, incorporate them in a separate resolution pass and rebuild/review.

The source inventory contains 21 PDFs (193 pages total, counting both lecture 15
variants). Checksums, exact paths, and byte sizes are in
[the source manifest](../sources/manifest.json). Lecture 15 has an unresolved
source-version question in [its ledger](lectures/15.md#l15-q01-source-version-to-transcribe).

## Lecture 07 handoff (2026-10-25)

- Status: `transcribed-with-open-questions`; pages 1-3 and 6-8 checked, pages 4-5 mapped
  with L07-Q01/Q02 pending. Page 8 is blank. Draft has 18 source-marked frames.
- The verified draft has been applied to the original workspace after write
  access became available. Unrelated updated guidance and lecture records
  were preserved.
- Separate [questions PDF](../output/pdf/lecture-07-questions.pdf), editable
  [question source](ambiguities/lecture07/main.tex), and evidence crops retain
  both pending questions using the same IDs as the ledger and slides.
- Original-project isolated build (20 pages), combined build (250 pages), and
  questions build (2 A4 pages) pass. All lecture slides and both question pages
  have passed visual review; the questions build has no warnings/overflow.
- Next: deliver the verified pass and its two-question PDF with dependent proof
  frames visibly provisional/deferred, then continue the assigned work queue.
  Later answers may be incorporated in a separate resolution pass.

## Lecture 14 handoff (2026-10-25)

- Status: `transcribed-with-open-questions`; the pass is finished. All five
  source pages are accounted for in 19 content frames. Pages 1, 3, and 4 are
  checked; pages 2 and 5 have three documented open questions.
- [Lecture PDF](../output/pdf/lecture-14.pdf): 21 pages including cover/divider.
  [Questions PDF](../output/pdf/lecture-14-questions.pdf): 3 A4 pages, with
  [editable source](ambiguities/lecture14/main.tex) and evidence crops.
- L14-Q01 uses a visibly provisional matrix-size assumption; L14-Q02 defers the
  source End example; L14-Q03 uses visibly provisional quotient-action symbols
  and preserves the full corresponding proof/conclusion. No answer is inferred.
- Isolated, questions, and combined builds passed. All lecture frames and
  question pages passed visual review; no overfull boxes. Existing shared
  bidi/font notices remain documented in the [ledger](lectures/14.md).
- Combined snapshot: 323 pages at `build/combined-lecture14/advanced-algebra-slides.pdf`;
  lecture 14 occupies pages 304-323, after the concurrently transcribed lecture
  13. Explicit section numbering stays at 14; transition/end frames checked.
- Exact next step: this single-lecture assignment is finished. Optional later
  answers/new evidence can support a resolution pass; no answer gate or further
  lecture assignment is implied.

## Lecture 10 handoff (2026-10-25)

- Status: `transcribed-with-open-questions`. All 8 source pages visually read and mapped;
  pages 1, 4, and 8 checked; pages 2-3 and 5-7 retain deferred L10-Q01/Q02/Q03.
- Revised draft: 21 source-marked content frames, 23 PDF pages including cover
  and section divider. Isolated build and every rendered page inspected.
  [Review slides](../output/pdf/lecture-10-slides.pdf).
- The [separate questions PDF](../output/pdf/lecture-10-questions.pdf) contains
  all three questions, evidence crops, pending statuses, and reply space.
  Its [editable source](ambiguities/lecture10/main.tex) is retained.
- The user said “put it in question PDF”; this does not resolve the questions.
  Affected rank, Prüfer-classification, and maximal-index passages stay provisional.
- Next: finish any remaining verification and deliver both PDFs with the five
  affected frames explicitly provisional/deferred. Do not wait for answers;
  record any answers supplied later in a separate resolution pass.

## Lecture 13 handoff (2026-10-25)

- Status: `transcribed-with-open-questions`; pass finished under the current
  record-and-continue policy. All eight source pages are accounted for in
  25 source-marked content frames. Pages 1–7 are checked; page 8 retains the
  exact-length Fitting statement provisionally and explicitly defers the
  unprovided exponent-bound argument as L13-Q01.
- Deliverables: [lecture PDF](../output/pdf/lecture-13-slides.pdf), 27 pages,
  and [questions PDF](../output/pdf/lecture-13-questions.pdf), one A4 page.
  The [ledger](lectures/13.md) maps every source page and the optional later item.
- Isolated and questions builds pass, every final page has passed visual review,
  and the combined deck builds in the separate verification directory
  `build/lecture13-combined-verify/` (315-page snapshot). No overfull box or
  missing-character warning occurs in either lecture-13 output.
- Lecture 13 is included before lecture 14. Earlier live-answer/wait language
  has been superseded. No answer is needed to deliver this pass or sequence
  subsequent assigned work; no mathematical resolution has been invented.
- Next: deliver both PDFs. This single-lecture assignment ends here. Revisit
  L13-Q01 only if new evidence or a voluntary later answer is supplied.

## Lecture 11 handoff (2026-10-25)

- Status: `transcribed-with-open-questions`; this single-lecture pass is finished.
- All 8 source pages visually read and mapped to 26 source-marked content frames. Pages 2, 3, 6, and 7 are checked; pages 1, 4, 5, and 8 retain four open issues. L11-Q01 is explicitly deferred; L11-Q02/Q03 are provisional proof corrections; L11-Q04 is a provisional unital-left-module assumption.
- Delivered [lecture PDF](../output/pdf/lecture-11.pdf) (28 pages including cover/divider) and [questions PDF](../output/pdf/lecture-11-questions.pdf) (4 pages), with editable sources/evidence and full coverage in the [ledger](lectures/11.md).
- Isolated/questions builds and all-page visual reviews passed. Combined integration build passed (323 pages); lecture 11 and adjacent boundary pages were checked. Existing combined bidi/name-tree warnings are recorded in the ledger; isolated lecture 11 has no bidi warnings or overfull boxes.
- Next: deliver both PDFs. No answer gate and no further lecture is assigned here. Optional later evidence/answers may support a resolution pass for the four recorded IDs.

## Lecture 12 handoff (2026-10-25)

- Status: `transcribed-with-open-questions`; all 12 source pages visually read
  and reconciled into 28 labeled/source-marked content frames. Pages 1 and 6-9
  are checked; pages 2-5 and 10-12 contain explicitly provisional L12-Q01/Q02/Q03.
- Deliverables: [lecture PDF](../output/pdf/lecture-12.pdf), 30 pages including
  cover/divider, and [questions PDF](../output/pdf/lecture-12-questions.pdf),
  3 A4 pages with evidence and optional later questions.
- Isolated and questions builds pass; all final pages visually inspected.
  No lecture/question overflow or missing characters. Combined integration
  check passes in `build/lecture12-combined-pass/` (323-page snapshot, lecture
  12 at pages 249-277). Source checksum and 28 frame/source markers checked.
- The [ledger](lectures/12.md) records all page mappings, three open readings,
  source-supported corrections, overlap and verification limits. No question
  is resolved by assumption and delivery does not wait for an answer.
- Exact next step: deliver both PDFs; this single-lecture assignment ends here.
  Optional later evidence/answers may support a resolution pass.

## Lecture 16 handoff (2026-10-25)

- Status: `transcribed-with-open-questions`. All nine source pages reconciled
  into 25 source-marked content frames; pages 1 and 5 retain L16-Q02/Q01,
  with all other pages checked. No source items omitted.
- [Lecture slides](../output/pdf/lecture-16-slides.pdf): 27 pages including cover
  and section divider. [Separate questions PDF](../output/pdf/lecture-16-questions.pdf):
  2 pages with the two literal notation discrepancies, evidence, provisional
  readings, pending statuses, and reply space. Editable sources/evidence are retained.
- Isolated and questions builds pass; all pages visually inspected, including
  the final Nakayama edit. Combined build passes in `build/lecture16-combined/`
  (497 pages); lecture 16 occupies pages 357-382. Boundary review and exact
  content-raster comparison with the isolated lecture pass. Existing combined
  bidi/name-tree notices are recorded in the [ledger](lectures/16.md).
- Next: deliver both PDFs; optional later answers may be incorporated in a
  separate resolution pass. No answer is required for completion or sequencing.
  Lecture 17 is the next numbered lecture, outside this assignment.

## Status meanings

- `existing-draft-unverified`: slides exist, but source coverage and accuracy require page-by-page audit.
- `not-started`: no lecture slide source has been created.
- `in-progress`: transcription or source reconciliation is underway.
- `needs-clarification`: legacy annotation for open questions, never a request to stop or ask the user. Finish remaining work and replace it with the appropriate pass status.
- `ready-for-review`: all items accounted for, including documented provisional/deferred items; final checks remain.
- `transcribed-with-open-questions`: transcription pass, source accounting, and build/visual checks finished; open items documented in the separate PDF. Deliver and continue assigned lectures without waiting.
- `complete`: transcription pass and checks finished with no unresolved source items.

Update the status here and in the lecture ledger together. A successful build alone
does not establish source fidelity or completion. Do not promote an old draft to
complete based on its size, topic headings, or the presence of a generated PDF.
Both `complete` and `transcribed-with-open-questions` finish the pass for work
queue sequencing. Neither is permission to invent a resolution or ignore
unverified source material. Source-page annotations can remain open without
blocking the lecture pass.

## Starting or resuming one lecture

```sh
python3 scripts/lectures.py show 04
make lecture LECTURE=04
```

The `show` command provides the lecture’s source and work paths. The build command
previews that lecture when its slide source exists; it does not transcribe the notes.
For an unstarted lecture, create actual content before building it.

A useful agent prompt is:

> Work on lecture 04 only. Read AGENTS.md, docs/TRANSCRIPTION.md, and
> docs/lectures/04.md. Audit the existing section against its PDF page by page,
> finish the transcription pass, and put ambiguities in its separate questions
> PDF without asking me live questions or waiting for answers. Mark affected
> items provisional/deferred, finish verification, and deliver both PDFs.

Setup inventory date: 2026-10-25.

## Lecture 18 handoff (2026-10-25)

- Status: `transcribed-with-open-questions`. All seven source pages visually read and reconciled into 23 source-marked content frames (25 PDF pages including cover and divider); pages 3-6 checked, pages 1, 2 and 7 retain L18-Q01/Q02/Q03.
- [Lecture slides](../output/pdf/lecture-18-slides.pdf) and [three-page questions PDF](../output/pdf/lecture-18-questions.pdf) are exported. [Editable questions source](ambiguities/lecture18/main.tex) and evidence crops are retained; all three questions remain open with matching slide/ledger IDs and visible provisional/deferred passages.
- Isolated build, questions build, and visual inspection of every new frame/question page passed. Colored TikZ arrow rendering was repaired locally; no overfull boxes or missing glyphs remain in lecture 18. Source SHA-256 matches the manifest.
- Combined integration build passed at `build/lecture18-combined/advanced-algebra-slides.pdf` (497 pages); its lecture 18 content, pages 411-433, preserves numbering and layout. Separate output avoids preexisting auxiliary-file ownership restrictions; shared theme/legacy diagnostics are detailed in the [ledger](lectures/18.md).
- This single-lecture assignment is finished. Deliver both PDFs; optional later answers/new evidence can support a resolution pass for Q01/Q02/Q03, followed by synchronized rebuild and visual review. Do not wait for answers or automatically start another lecture from this chat.


## Lecture 19 handoff (2026-10-25)

- Status: `transcribed-with-open-questions`; all 12 source pages visually read
  and reconciled into 33 content frames (35-page isolated PDF). Pages 1-11 are
  checked; page 12 retains the explicit provisional notation reading L19-Q01.
- Deliver the [lecture slides](../output/pdf/lecture-19-slides.pdf) with the
  [one-page questions PDF](../output/pdf/lecture-19-questions.pdf). The latter
  contains the page-12 evidence crop, alternative readings, open status and
  reply space. The [ledger](lectures/19.md) records full per-page coverage.
- Isolated and questions builds pass; every rendered output page was visually
  checked. Source checksums/page counts match the manifest. The isolated deck
  has no overfull boxes; retained bidi frame-end diagnostics have no observed
  visual defect and are documented in the ledger.
- Lecture 19 is included in the combined draft. The build in `build/combined-19`
  passes at 497 pages, with lecture 19's divider/content on pages 434-467.
  Both boundaries and adjacent pages were inspected; lecture numbering is correct.
- Exact next step: deliver this finished pass. The single-lecture assignment ends
  here. A later Q01 answer can support an optional correction/rebuild; no answer
  is needed to deliver the pass or continue other assigned lectures.

## Lecture 20 handoff (2026-10-25)

- Status: `complete`; all 13 source pages visually inspected and reconciled into
  29 source-marked content frames. An independent read-only source audit agrees.
- [Lecture slides](../output/pdf/lecture-20-slides.pdf): 31 PDF pages including
  cover and divider. [Editable source](../sections/section20.tex) and
  [page coverage ledger](lectures/20.md) are up to date.
- No unresolved ambiguities or deferred items; no questions PDF required.
  The source's teaching prompts and analogous-proof references are retained.
- Isolated build and all rendered pages passed visual review. Combined build
  passed in `build/lecture20-combined/` (497 pages), with lecture 20 at pages
  468-497. Combined integration samples passed visual inspection. Existing
  legacy bidi/name-tree warnings are recorded in the ledger; lecture 20's
  isolated build has no bidi errors, overfull boxes, or missing characters.
- Original source SHA-256 still matches the manifest. No source content omitted.
- Next: deliver the finished lecture PDF. No required lecture-20 work remains,
  and this single-lecture assignment does not advance to another lecture.

## Lecture 15 handoff (2026-10-25)

- Finished transcription pass: all 16 A pages and 13 B pages visually compared and accounted for in 32 source-marked content frames. A supplies provisional order; B1-12 match A1-12 and B13 contains the A13 theorem statement only. The A-only proof and consequences are retained.
- [Slides](../output/pdf/lecture-15-slides.pdf): 34 pages including cover/divider. [Separate questions PDF](../output/pdf/lecture-15-questions.pdf): 3 pages, with Q01 source authority, Q02 two exponent discrepancies, and Q03 a repeated exercise subscript open. Working choices are visibly provisional; no answer was inferred.
- Isolated, questions, source-checksum, and fresh combined builds pass. Every lecture/question page and adjacent combined transitions visually checked. No overfull boxes or missing characters; shared Beamer/XePersian bidi and package diagnostics remain without a related visual defect. Combined snapshot: 497 pages in `build/lecture15-combined/`.
- Editable slide/question sources, evidence, detailed correspondence, and all pending decisions are in the [ledger](lectures/15.md). Next: incorporate later answers only if supplied, then rebuild/review; open questions do not block further assigned lectures.


## Lecture 17 handoff (2026-10-26)

- Status: `transcribed-with-open-questions`. All 11 source pages reconciled;
  pages 1–4 and 7–9 checked, pages 5–6 and 10–11 fully accounted for with
  provisional L17-Q02 and L17-Q01 respectively. No source items remain unaudited.
- New [slide source](../sections/section17.tex): 27 content frames, with exact
  source markers and unique `lec17:` labels. [Delivered lecture PDF](../output/pdf/lecture-17-slides.pdf)
  has 29 pages including cover and divider.
- [Separate questions PDF](../output/pdf/lecture-17-questions.pdf): 2 A4 pages,
  with evidence crops, possible readings, explicit open statuses and reply space.
  [Editable question source](ambiguities/lecture17/main.tex) is retained.
- L17-Q01: scalar argument in the larger-domain Baer extension formula;
  the final three dependent proof frames use the page-11 reading provisionally.
  L17-Q02: unclear base-ring numeral in the cyclic nonfree example; the working
  Z6 reading and its use as an example for the next two conclusions are marked.
- Isolated and questions builds passed; every lecture slide and both final
  question pages visually reviewed. Combined build passed in the fresh
  `build/combined-17/` directory (498-page snapshot, lecture 17 at pages 383–410),
  with integration spot checks. Original source checksums match the manifest.
- This lecture-only request is finished. Deliver both PDFs without waiting on
  answers. A later supplied answer can trigger a separate resolution pass;
  consult current lecture ledgers before beginning another assigned lecture.
