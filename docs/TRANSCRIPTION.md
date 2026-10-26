# Per-lecture transcription workflow

The goal is a readable Persian teaching deck grounded in each handwritten PDF.
One numbered PDF is one lecture work item even when its opening pages continue
the previous topic. The two files numbered 15 are unresolved variants of one
work item. Original PDF pages are numbered from 1, regardless of handwritten
page numbers.

**Current user policy:** collect questions in a separate PDF and continue
autonomously. Do not ask live clarification questions, wait for answers, or make
ambiguity resolution a prerequisite for finishing a transcription pass. This
replaces the earlier ask-and-wait workflow, including old handoff instructions.

## Start or resume

1. Read `AGENTS.md`, the [progress index](PROGRESS.md), and the relevant
   `docs/lectures/NN.md` ledger. Honor recorded user decisions. If no lecture is
   specified, resume the first unfinished transcription pass. A pass marked
   `transcribed-with-open-questions` is finished for sequencing; do not loop on
   it waiting for answers. A single-lecture request ends with its deliverables;
   a batch request continues to the next assigned lecture.
2. Run `python3 scripts/lectures.py show NN`. Confirm source paths, variants,
   page counts, and the existing or planned slide file. For lecture 15, compare
   both versions, use 16-page `unresolved-a` as a provisional working order, and
   record differences and source-selection uncertainty without stopping.
3. Inspect existing `sections/sectionN.tex`, including commented blocks. Lectures
   have different audit states; read the current ledger. The initial lecture/
   section association was based on numbering and topics and must be reconciled
   against the PDF, rather than assumed from the filename.
4. Render the first few pages, then proceed in small batches. For example:

   ```sh
   python3 scripts/lectures.py render 04 --page 1 --last-page 3
   python3 scripts/lectures.py render 15 --variant unresolved-a --page 1
   ```

   The helper prints absolute image paths under `build/source-pages/`. Inspect
   them with the available image viewer. Increase `--dpi` for small symbols.
   Extraction/OCR is an aid, never the authoritative reading of handwriting.

## Transcribe and reconcile

- For each page, list definitions, statements, proofs, examples, exercises, and
  diagrams in source order. Compare them with active **and commented** draft
  material. Reuse accurate frames, repair only supported errors, and add gaps.
- Keep a single main source `sections/sectionN.tex` for that lecture. New lecture
  files should begin with a Persian `\section{...}`. Use small frames with one
  central claim or a coherent proof step. Preserve the present style and avoid
  solving overflow by shrinking all text.
- Put a source comment before each frame or frame group. A proof spanning pages
  can cite a range; distinguish multiple source items on the same page:

  ```tex
  % Source: sources/lectures/04 Module.pdf | PDF page: 3 | item: generated submodule
  \begin{frame}{...}
    \label{lec04:generated-submodule}
    % Faithful mathematical content, in the existing Persian style.
  \end{frame}
  ```

- Update the ledger's page coverage table with stable frame labels (or titles
  for unchanged legacy frames), missing material, and audit state. Use
  `unchecked`, `partial`, `open-question`, or `checked` per page. The legacy
  `needs-clarification` annotation also means an open question, never a request
  to stop. `checked`
  means every item on that page is accounted for in verified frames or an
  explicitly justified omission/cross-reference. A page can be split across
  many frames; a frame can refer to more than one page.
- Overlap between lectures is allowed. Record where a repeated result is
  covered and whether to repeat or cross-reference it. Do not silently drop
  source material because it looks familiar.
- Inspect current commented material before reusing it; old drafts may have
  been retained as archives after a later source audit.

## Record uncertainty without stopping

An unclear symbol can change a theorem. Inspect a higher resolution page/crop
and surrounding pages first, then write a specific question in the lecture's
separate PDF, for example:

> Lecture NN, PDF page P, second displayed formula: does the relation read
> `...` or `...`? The choice changes the hypothesis used in the next line.

This is an example question format, not an identified source problem. Include a
source image/crop and enough context for later review. Do not send it as an
interactive chat question or wait for a response.

Create a matching entry `LNN-Qxx` in the lecture ledger. Record source path
and variant, PDF page and location, observed fragment, candidate readings,
mathematical consequence, question, status, and the user's eventual answer.
For suspected mathematical errors, distinguish the literal reading from any
proposed correction. A working correction or assumption must be visibly labeled
provisional; if no defensible reading exists, defer the affected item explicitly.

### Separate questions PDF

Every lecture with ambiguities or questions must have its own PDF at
`output/pdf/lecture-NN-questions.pdf`, separate from the course slides. Use the
existing lecture 04 question project as an example. For a new lecture, create
`docs/ambiguities/lectureNN/main.tex` from `docs/ambiguities/template.tex` and
store evidence crops under that project's `images/` folder. Replace the template
placeholders and add actual questions; do not invent uncertainties or export
an empty template as a completed review artifact.

Each question must contain:

- The same `LNN-Qxx` ID used in the ledger and relevant slide comments.
- The exact source filename/variant and 1-based PDF page/location. For a
  whole-document source-selection question, identify the files and say so.
- The literal unclear fragment and a readable evidence crop when useful.
- Possible readings or proposed corrections, why the distinction matters, and
  a specific question for the user.
- Pending/answered/incorporated status, space for an answer, and the eventual
  user answer, resolution, and date. Retain resolved entries as decision history.

```sh
make questions LECTURE=04
pdftoppm -r 100 -png output/pdf/lecture-04-questions.pdf build/questions-04-review
```

Inspect all changed question pages for Persian direction, readable formulas and
crops, and clipping. Update the PDF whenever a question or answer changes, keep
the ledger synchronized, and deliver the PDF with the lecture at handoff.
The PDF contains the full questions; do not repeat them as live clarification
requests or make delivery conditional on an answer.
Keep the `.tex`, evidence crops, and final PDF in version control. Build files
stay under ignored `build/questions/`. A lecture with no questions needs no
empty questions PDF; record that outcome in its ledger after the source audit.

Continue through the entire lecture. For an affected claim, leave an
`% AMBIGUITY[LNN-Qxx]` comment and visibly mark a provisional reading or deferred
item on the slide. Preserve clear surrounding material and never fabricate a
missing proof. An open question remains open, but its presence does not block
the lecture build, visual checks, delivery, or next assigned lecture. Record
later user answers if supplied; requesting an answer is not part of this pass.

## Build and review

```sh
make lecture LECTURE=04
pdftoppm -r 100 -png build/lecture-04.pdf build/lecture-04-review
```

An isolated deck includes the usual cover and only that lecture. Its section
counter matches the lecture number. The helper refuses to build a not-started
lecture with no active frames; create real content before building it. Source
images and previews stay in ignored `build/`.

Inspect **every changed frame**, plus adjacent frames for continuation problems.
Check Persian text direction, mixed Latin text, equations, proof/QED placement,
diagram labels, and clipping. Read the build log for `Overfull` boxes and other
relevant warnings. Retain unresolved or preexisting defects in the ledger.

When a new lecture is suitable for the combined draft, add its ordered
`\input{sections/sectionN.tex}` to `config/sections.tex`, then run `make slides`.
Keep the optional TA material separate. A partially transcribed lecture may be
included as a draft, provided its ledger and handoff clearly state that status.

## Status and completion

Lecture status is maintained in the progress index and its ledger:

| Status | Meaning |
| --- | --- |
| `existing-draft-unverified` | Slides predate the per-PDF audit; completeness unknown. |
| `not-started` | No transcription work or lecture slide file yet. |
| `in-progress` | Source reconciliation or transcription is underway. |
| `needs-clarification` | Legacy annotation for open questions; not a waiting state. Continue remaining work and replace it with an appropriate pass status. |
| `ready-for-review` | All source items accounted for, including documented provisional/deferred items; final checks remain. |
| `transcribed-with-open-questions` | Pass finished and verified; unresolved items documented in the separate PDF. Delivery and further assigned lectures can proceed. |
| `complete` | Pass finished and verified with no unresolved source items. |

Before finishing a transcription pass, verify:

- Every page of the selected source has been visually read and all material is
  mapped to frames or a documented omission/cross-reference.
- Every added or audited frame has accurate source markers. Clear content
  matches the source; provisional readings and deferred statements/proofs are
  explicitly marked and linked to a question ID rather than presented as settled.
- Every ambiguity is recorded with evidence and possible readings in the PDF.
  Answers are not required. For lecture 15, record the provisional ordering and
  account for both variants' additions/conflicts; do not silently exclude a
  variant or describe a working choice as a confirmed authority decision.
- The separate questions PDF is up to date with all questions and recorded
  answers, or the ledger explicitly records that no questions arose. Its IDs
  and decisions agree with the ledger and relevant slide comments.
- The lecture builds and all changed frames pass visual review; new content is
  included in the combined deck when appropriate, and the combined build passes.
- The ledger and index agree, and their final handoff states coverage, checks,
  remaining limitations (if any), and the next lecture.

Use `transcribed-with-open-questions` when any source item remains provisional
or deferred, and `complete` when none does. Both finish the pass for sequencing.
Do not wait on an optional later resolution round before delivering the pass.

## Reusable agent prompt

```text
Continue lecture 04 from its numbered PDF. Read AGENTS.md and
docs/lectures/04.md first. Reconcile existing slides page by page, transcribe
missing content, and preserve the current Persian Beamer style. Record unclear
handwriting, formulas, hypotheses, and proof steps in the separate questions PDF
with exact pages, evidence, and possible readings. Do not ask me questions or
wait for answers during transcription. Mark affected items provisional or
deferred, finish all clear content and verification, and deliver both PDFs.
Record coverage, checks, and a precise handoff; use transcribed-with-open-questions
if anything remains unresolved. Work on this lecture only unless I say otherwise.
```
