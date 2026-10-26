# Shared mathematical conventions

These conventions apply to the edited teaching edition. They are editorial
choices, not claims about every convention in the handwritten notes. The
coordinator maintains this document; authors record local exceptions and
proposed global changes in their editorial records before integration.

## Rings and modules

- Rings are associative. The main development uses rings with identity;
  nonunital rings remain in explicitly labeled examples or sections wherever
  the course teaches them. Commutativity is a local hypothesis, never an
  inference from notation.
- Do not silently build `1 != 0` into the word unital. State a nonzero-ring
  hypothesis where needed and check the zero ring during review, particularly
  in arguments about bases, rank, nonzero elements, and division rings.
- The main development uses unital left modules over unital rings. Lecture 04
  must first distinguish the general action axioms from the unital condition,
  retain its zero-action and nonunital examples, and clearly announce the
  transition to the default convention. Preserve general-action formulas in
  that explicitly general setting. A ring identity alone does not license
  using `1m = m` in an arbitrary action.
- Label right modules and bimodules explicitly. Check the required sides in
  regular modules, ideals, annihilators, Hom, quotients, and tensor products.
  Do not replace a one-sided ideal by a two-sided ideal without justification.
- Ring homomorphisms in the unital development preserve identity unless an
  explicit exception is being discussed. When changing scalars or conventions,
  verify that the resulting action satisfies the declared module conditions.
- A simple module is nonzero. A maximal submodule/ideal is proper. A minimal
  nonzero submodule/ideal must be named with its nonzero condition. Keep these
  distinctions visible in definitions and in existence arguments.

## Hom, End, and multiplication order

- `Hom_R(M,N)` denotes the additive group of R-linear maps. Define and justify
  any additional scalar action under explicit hypotheses; do not silently treat
  it as a left R-module in a general noncommutative setting.
- `End_R(M)` contains all endomorphisms, while `Aut_R(M)` denotes the group of
  invertible ones. Keep the Persian terminology and the mathematical objects
  distinct.
- Composition is `fg = f o g`: g acts first. Use this convention in
  endomorphism multiplication, matrices of maps, and opposite-ring arguments.
  Display domains and codomains where a composition could be ambiguous.
- Define the opposite-ring multiplication when introduced, and distinguish it
  from the original product in calculations. Do not reorder factors as though
  the ring or an endomorphism ring were commutative.
- For matrix descriptions, state the coordinate/action convention once and
  verify it against the declared left/right module and composition conventions.
  Prefer a short evaluated calculation to an unexplained assertion about order.

## Notation and dependencies

- Distinguish equality, module isomorphism, and ring isomorphism. Do not replace
  an isomorphism conclusion by equality of particular submodules.
- Distinguish internal/external direct sums and direct products. State the
  ambient module and finite-support condition where needed, especially for
  infinite families. Distinguish a family summing to M from an independent
  family whose sum may be a proper submodule of M.
- Use stable notation for generated submodules, kernels, images, annihilators,
  inclusions, and quotient maps. State the coefficient domain for a linear
  relation and the index ranges used in examples.
- Introduce each needed definition before its first substantive use. For an
  earlier definition, give a concise recall only if necessary for the current
  argument. Preserve the course's progression and refer to established results
  by stable labels rather than assuming that a later theorem is already known.
- Maintain the lecture's dependency list in `docs/editorial/NN.md`. Add the
  smallest necessary lemma before its use when no earlier result suffices.
  Review the dependency chain for circular reasoning.

## Proofs, diagrams, and editorial evidence

Present the construction, essential argument, and conclusion. Justify the
nontrivial uses of well-definedness, linearity, injectivity/surjectivity,
generation, finite support, stabilization, maximality, and prior theorems.
Compress routine algebra once its mechanism is clear. Preserve exercises as
exercises unless an essential taught argument requires their content.

Use proof diagrams when they explain a specific relationship or construction.
Every arrow must have a valid domain/codomain, and every claimed identity or
commuting path must be checked. A diagram supplements the reasoning rather
than concealing a missing step.

Record substantive corrections, added hypotheses/definitions, completed
arguments, and supporting references under stable editorial IDs. Cite only
sources actually inspected and keep additions distinct from literal notes.
Choose mathematically justified formulations autonomously; unresolved source
intent is not a requirement to wait for the user. An unresolved mathematical
limitation, however, must be disclosed and cannot pass final review.
