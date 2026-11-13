# Thirty milestones through the project

[Learning introduction](README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [Scientific account](../science/README.md)

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018), using the author's standard-layout text. The [bridge](WATROUS_BRIDGE.md) verifies the section locators and supplies the translations into this project. Primary research references provide attribution and specialist dependencies; they are not additional educational anchors.

The map has **12 background/preliminaries milestones** and **18 narrative/innovation milestones**. The first phase assembles states, operations, temporal measurement contexts, operator norms and preparation entanglement into one experiment. The second builds the converse and attaining families into the uniform resource law, then connects it to formation entanglement, a measurable witness and the limits of the result. Within each phase, local objects lead to the whole account.

The central quantity is the maximum PDM negativity over initial states of Schmidt number at most $`k`$. For fixed $`q_0\lt1/2`$ and all $`0\leq q\leq q_0`$,

```math
\mathcal F_k(d,q)=\Theta_{q_0}\!\left(\frac{k^2}{d(k+qd)}\right).
```

This compact formula is explained progressively below. The [scientific proof](../science/schmidt_law.md) remains the authority for its quantifiers and finite bounds.

## Phase I — Background/preliminaries

### M01 — A preparation is a quantum state

**Central question:** What information about a physical preparation is contained in its density operator?

**Understanding target:** Explain positivity, unit trace, pure and mixed states, and the support on which a state can have nonzero probability.

**Dependencies and story role:** This starting point supplies the input object before interactions, measurements or temporal correlations are introduced.

**Conceptual connection:** Later negative PDM eigenvalues matter precisely because ordinary preparation states cannot have them; the two operator types share some properties but differ in positivity.

**Source pointers:** Watrous §2.1.2; [model, operational PDM](../science/model.md#2-the-operational-pdm).

### M02 — Subsystems and discarded information

**Central question:** What remains of a joint state when one subsystem is omitted?

**Understanding target:** Read tensor-product labels and partial traces, distinguishing a joint preparation from either reduced state and from a hypothetical untouched reference.

**Dependencies and story role:** Uses M01 to place two initially correlated systems into the story and identify the later retained events.

**Conceptual connection:** The experiment retains the initial B event and final output C, while discarding A; that reduction can diminish negativity and prevents a full-PDM bound from automatically being attained.

**Source pointers:** Watrous §2.1.3; [model](../science/model.md#1-a-joint-measurement-with-one-noisy-output-bit); [overlap envelope](../science/entanglement_cost.md#1-a-bound-in-terms-of-bell-overlap).

### M03 — Measurement effects and reported outcomes

**Central question:** How does an effect operator determine an outcome probability?

**Understanding target:** Distinguish a POVM effect, a prepared state and an outcome label; explain why positive effects summing to identity define a measurement.

**Dependencies and story role:** Uses M01–M02 to introduce the apparatus before asking how it changes a state or generates temporal data.

**Conceptual connection:** The Bell projector and its complement are two effects, while the retained output is only a classical bit. A binary output does not make the underlying joint measurement local.

**Source pointers:** Watrous §2.3.1; [channel effects](../science/model.md#1-a-joint-measurement-with-one-noisy-output-bit).

### M04 — A channel can end in a classical bit

**Central question:** What physical transformation includes both the joint measurement and its noisy report?

**Understanding target:** Recognize a completely positive trace-preserving measurement channel and explain how one final binary symmetric error changes its effects.

**Dependencies and story role:** Joins the states of M01–M02 and effects of M03 into the fixed apparatus used in every comparison.

**Conceptual connection:** The parameter q describes one final reported-bit flip. It does not silently include independent errors on every internal detector, faulty gates or imperfect input entanglement.

**Source pointers:** Watrous §§2.2.1–2.2.2; [model channel](../science/model.md#1-a-joint-measurement-with-one-noisy-output-bit); [noise boundary](../science/implementation.md#noise-and-precision-boundary).

### M05 — A first measurement changes the experiment

**Central question:** Why must an initial measurement be specified by its state update as well as its probabilities?

**Understanding target:** Explain coarse Lüders projectors, their signed outcomes and the anticommutator representing the difference of their unnormalized postmeasurement states.

**Dependencies and story role:** Builds on M03–M04 to turn one input-to-output channel into a sequential measurement experiment.

**Conceptual connection:** Measuring a register-wide dichotomic observable is different from resolving every basis string. This disturbance is part of the temporal correlator and later separates the witness's two measurement contexts.

**Source pointers:** Watrous §2.3.2; [operational PDM derivation](../science/model.md#2-the-operational-pdm).

### M06 — Temporal data need not form a density matrix

**Central question:** How can valid sequential measurements determine a Hermitian unit-trace operator that is not positive?

**Understanding target:** Define the reduced PDM through its correlators and explain why its negative eigenvalues do not represent negative physical outcome probabilities.

**Dependencies and story role:** Integrates M02 and M05 into the temporal object whose strength the project studies.

**Conceptual connection:** The PDM combines statistics from different initial-measurement contexts. Its ordinary-looking marginals do not turn that combination into a single spatial joint state.

**Source pointers:** Watrous §§2.1.2, 2.3.1 for foundational contrasts; [local PDM construction](../science/model.md#2-the-operational-pdm).

### M07 — Negative spectral weight has a norm

**Central question:** How does the trace norm quantify a Hermitian operator's failure of positivity?

**Understanding target:** Relate positive and negative spectral parts to the trace norm, keeping the project's f normalization distinct from ordinary negative weight and logarithmic negativity.

**Dependencies and story role:** Uses M01 and M06 to replace qualitative nonpositivity with one numerical figure of merit.

**Conceptual connection:** The classical output separates the PDM into two orthogonal blocks, so their trace norms add. This simple identity makes both the converse and the attaining spectra tractable.

**Source pointers:** Watrous §1.1.3; [negativity convention](../science/model.md#2-the-operational-pdm).

### M08 — Classical mixtures and convex bounds

**Central question:** Why can a proof for pure preparations constrain arbitrary classical mixtures?

**Understanding target:** Explain linearity of the PDM map and convexity of its negativity, without assuming that a mixed state possesses one unique pure-state decomposition.

**Dependencies and story role:** Connects M01 and M07 to an optimization over a physically meaningful class of preparations.

**Conceptual connection:** A shared classical random variable is already included when separable mixtures are allowed. It cannot evade a bound that holds for every pure product state and extends by convexity.

**Source pointers:** Watrous §1.2.1 and §6.1.1; [preparation constraint](../science/model.md#4-the-preparation-constraint).

### M09 — Entanglement dimension is a preparation budget

**Central question:** What does a bound on Schmidt number allow and exclude?

**Understanding target:** Connect Schmidt decomposition to coefficient-matrix rank, and define the mixed-state constraint through decompositions with bounded pure-state rank.

**Dependencies and story role:** Uses M02 and M08 to identify the resource optimized throughout the theorem.

**Conceptual connection:** Schmidt number limits the dimension of spatial entanglement, while a large Schmidt rank can still carry very little entropy. A later argument must address the actual formation-entanglement requirement separately.

**Source pointers:** Watrous §1.1.3, §6.1.1 and Definition 6.14; [Schmidt-number convention](../science/model.md#4-the-preparation-constraint).

### M10 — Bell overlap and a joint apparatus

**Central question:** What special role does the maximally entangled Bell effect play here?

**Understanding target:** Explain its overlap with product and Schmidt-number-bounded inputs, while keeping that familiar overlap constraint distinct from the new PDM-negativity bound.

**Dependencies and story role:** Combines M03, M04 and M09 into the specific interaction whose preparation dependence will be analyzed.

**Conceptual connection:** The channel's output is classical and entanglement breaking, but realizing its Bell effect still requires a joint A–B operation. Both preparation and apparatus resources must remain visible.

**Source pointers:** Watrous §2.2.2 and Proposition 6.15; [fixed apparatus](../science/model.md#1-a-joint-measurement-with-one-noisy-output-bit); [implementation](../science/implementation.md#realize-the-bell-effect-apparatus).

### M11 — Entropy measures a different resource

**Central question:** How can entanglement entropy and relative entropy strengthen a rank-based resource statement?

**Understanding target:** Distinguish pure-state entropy, entanglement of formation and relative-entropy entanglement, including the difference between a single-state quantity and a regularized formation rate.

**Dependencies and story role:** Extends the preparation budget of M09 without replacing it, preparing the second resource converse.

**Conceptual connection:** A Bell-overlap measurement can feed a relative-entropy lower bound, connecting a measurable geometric quantity to formation entanglement even for mixed inputs.

**Source pointers:** Watrous §§5.2.1, 5.2.3, Theorem 5.35, §6.2.2 and Exercise 6.3; [formation proof](../science/entanglement_cost.md#2-from-overlap-to-entanglement-of-formation).

### M12 — Assemble the complete experiment

**Central question:** Which objects and assumptions must be fixed before two preparation resources can be compared?

**Understanding target:** Describe the initial A–B state, joint Bell test, final-bit noise, retained B–C PDM, Schmidt-number optimization and negativity convention in one account.

**Dependencies and story role:** Integrates M01–M11 into the framework needed for the project's new argument.

**Conceptual connection:** The same apparatus and noise are used across the comparison, while the initial resource changes. This does not promise the same accessible signalling strength, an untouched reference, or a statistical advantage.

**Source pointers:** Watrous §§2.1–2.3 and §6.1.1; [complete model](../science/model.md); [interpretation](../science/interpretation.md#what-is-held-fixed).

## Phase II — Narrative/innovation

### M13 — Compress a pure input into a matrix

**Central question:** Which matrix identities reveal how the Bell effect acts on an arbitrary pure input?

**Understanding target:** Obtain the reduced input state and Bell-effect Jordan term from the amplitude matrix, its adjoint and its trace, including complex nonnormal matrices.

**Dependencies and story role:** Starts the new argument locally, using the partial traces and Schmidt budget assembled in M02, M09 and M12.

**Conceptual connection:** One matrix simultaneously records normalization, Schmidt rank, Bell overlap and the temporal cross terms. This provides a common language for every allowed pure preparation rather than only symmetric examples.

**Source pointers:** Watrous §1.1.3; [amplitude identities](../science/schmidt_law.md#2-amplitude-matrices).

### M14 — Obtain the noiseless-order upper bound

**Central question:** What can the triangle inequality already say about every rank-bounded preparation?

**Understanding target:** Combine the trace bound and singular-value bound of the amplitude matrix to control the norm of the Bell-effect Jordan term.

**Dependencies and story role:** Uses M07 and M13 to establish the first converse, valid even when q vanishes.

**Conceptual connection:** The resulting linear order in k/d is useful and uniform, but it does not capture the stronger suppression created by a positive output-noise baseline. This identifies exactly what the next proof must add.

**Source pointers:** Watrous §1.1.3; [linear converse](../science/schmidt_law.md#3-the-linear-upper-bound).

### M15 — A noisy baseline permits a completed square

**Central question:** Why does positive output noise make the allowed negative weight quadratic in a small preparation ratio?

**Understanding target:** Explain the support projection, complete each block into a positive square minus a controlled rank-bounded term, and bound its negative trace.

**Dependencies and story role:** Builds directly on M13–M14 to expose the load-bearing mechanism of the stronger converse.

**Conceptual connection:** The bound uses the input's row support as well as Bell overlap. It therefore controls arbitrary amplitude matrices more strongly than simply inserting the familiar overlap bound into a generic PDM estimate.

**Source pointers:** Watrous §1.1.3 for operator foundations; [quadratic converse](../science/schmidt_law.md#4-the-quadratic-upper-bound).

### M16 — Keep the converse's quantifiers intact

**Central question:** Which preparation strategies are covered when the pure-state converse is extended?

**Understanding target:** Carry the same uniform bound through every decomposition of a Schmidt-number-bounded mixed input, including arbitrary classical correlations and shared randomness.

**Dependencies and story role:** Combines M08–M09 with M15 to complete the global preparation-class upper bound.

**Conceptual connection:** Optimizing over all separable states is stronger than inspecting a few uncorrelated examples. Convexity extends the proof, but does not enlarge the experiment to adaptive multi-use strategies or arbitrary alternative interventions.

**Source pointers:** Watrous §§1.2.1, 6.1.1; [preparation optimization](../science/model.md#4-the-preparation-constraint); [mixed extension](../science/schmidt_law.md#4-the-quadratic-upper-bound).

### M17 — Build a controlled entangled family

**Central question:** How can an embedded entangled preparation turn the converse into an achievable scaling?

**Understanding target:** Describe the superposition of two orthogonal Bell-type vectors on an even-dimensional support and identify its Schmidt budget and free preparation parameter.

**Dependencies and story role:** Uses M09–M10 and M13 to move from a universal obstruction to an explicit constructive mechanism.

**Conceptual connection:** The support size controls k/d, while one balanced sign operator separates two eigenvalue groups. The family is deliberately simple enough to track both its reduced-state entropy and its PDM spectrum.

**Source pointers:** Watrous §1.1.3 and §6.1.1; [embedded attaining family](../science/schmidt_law.md#5-an-attaining-family-for-every-even-schmidt-budget).

### M18 — Locate the negative subspace

**Central question:** Which part of the attaining family's PDM can actually become negative?

**Understanding target:** Follow the two sign groups through both classical-output blocks and explain why the zero-output block stays positive in the chosen parameter range.

**Dependencies and story role:** Develops M17 into the exact spectrum needed for an attaining lower bound.

**Conceptual connection:** The negativity is concentrated in a known sign subspace of the one-output block. That spectral localization later supplies a particularly simple positive temporal witness instead of requiring full matrix reconstruction.

**Source pointers:** Watrous §1.1.3; [attaining block spectra](../science/schmidt_law.md#5-an-attaining-family-for-every-even-schmidt-budget); [negative subspace](../science/witness.md#the-attaining-input-and-its-negative-subspace).

### M19 — Optimize a family without overstating optimality

**Central question:** What is established by optimizing the one preparation parameter?

**Understanding target:** Identify the exact attained lower-bound function and distinguish optimization within the balanced family from maximization over every admissible input.

**Dependencies and story role:** Uses M17–M18 to obtain a concrete value that can be compared with the converse.

**Conceptual connection:** Matching asymptotic orders does not settle exact global constants. The family's tractability is a constructive advantage, while finite counterexamples can still surpass its constant without invalidating the resource law.

**Source pointers:** Watrous §1.2.1 for optimization foundations; [family optimization and finite theorem](../science/schmidt_law.md#1-finite-bounds-and-the-uniform-theorem); [attainer](../science/schmidt_law.md#5-an-attaining-family-for-every-even-schmidt-budget).

### M20 — Resolve the whole separable benchmark

**Central question:** How can every separable preparation be reduced to a one-variable product calculation?

**Understanding target:** Explain the overlap parameter between two local pure vectors, derive the two small output blocks, and connect their maximum to the optimization over all separable mixtures.

**Dependencies and story role:** Joins M08, M16 and M18 to supply the k=1 endpoint without an even-support construction.

**Conceptual connection:** This endpoint both attains a useful lower bound and fixes the leading coefficient at fixed positive noise. It does not identify the exact maximizing overlap at every finite dimension and noise level.

**Source pointers:** Watrous §§1.1.3, 6.1.1; [separable reduction](../science/schmidt_law.md#6-separable-preparations-and-odd-schmidt-budgets).

### M21 — Cover every integer budget and dimension

**Central question:** How do the explicit examples establish a theorem beyond even Schmidt supports?

**Understanding target:** Combine the product endpoint with the largest even support below an odd budget, keeping the lost constant factor separate from the scaling.

**Dependencies and story role:** Integrates M17–M20 into a feasible lower bound for every integer d and k in the model.

**Conceptual connection:** An embedded support does not require changing the apparatus's Bell effect or local dimension. This keeps the same experimental family throughout the proof rather than comparing different channels for different parity cases.

**Source pointers:** Watrous §6.1.1; [integer-case proof](../science/schmidt_law.md#6-separable-preparations-and-odd-schmidt-budgets); [finite bounds](../science/schmidt_law.md#1-finite-bounds-and-the-uniform-theorem).

### M22 — Join the regimes in one uniform law

**Central question:** When does output noise change the preparation dependence from linear to quadratic?

**Understanding target:** Connect the finite upper and lower bounds to the crossover at q comparable to k/d, with constants uniform below a fixed noise ceiling q0 less than one half.

**Dependencies and story role:** Integrates M14–M21 into the main theorem rather than treating the two limits independently.

**Conceptual connection:** A fixed-positive-noise expansion cannot be extrapolated through a vanishing-noise sequence without checking its regime. At one-half noise the channel is constant, so that endpoint is explicitly outside the uniform constants.

**Source pointers:** Watrous §1.1.3 for norm foundations; [uniform constants](../science/schmidt_law.md#7-uniform-constants); [crossover](../science/schmidt_law.md#8-meaning-of-the-crossover).

### M23 — Interpret the same-apparatus comparison

**Central question:** What changes physically when the initial entanglement resource is increased?

**Understanding target:** Explain that the apparatus and noise remain fixed while the accessible causal influence and temporal witness strength may both change with the preparation.

**Dependencies and story role:** Uses the complete law of M22 to assess its operational meaning before attaching further claims.

**Conceptual connection:** Initial entanglement is not a false causal positive for a nonsignalling channel, but the theorem also does not hold unassisted signalling strength constant. These two qualifications preserve the actual causal conclusion.

**Source pointers:** Watrous §§2.2.1, 6.1.1; [no-false-positive argument](../science/model.md#3-what-negativity-certifies); [what is fixed](../science/interpretation.md#what-is-held-fixed).

### M24 — Bound negativity by Bell overlap

**Central question:** How does the full PDM constrain the reduced witness for an arbitrary mixed input?

**Understanding target:** Follow the pure-state two-dimensional block calculation, partial-trace contractivity and concavity of its overlap envelope through the mixed-state extension.

**Dependencies and story role:** Uses M07–M08 and M18 to start a second resource argument addressing the entropy limitation left open by Schmidt number.

**Conceptual connection:** The envelope gives a dimension-independent upper bound, but may lose negativity when A is traced out. Its overlap dependence is useful for formation entanglement without claiming an exact reduced-PDM optimum.

**Source pointers:** Watrous §§1.1.3, 1.2.1; [overlap-envelope proof](../science/entanglement_cost.md#1-a-bound-in-terms-of-bell-overlap).

### M25 — Close the low-entropy loophole

**Central question:** Why must a constant witness require substantial entanglement of formation, not merely large rank?

**Understanding target:** Combine Bell overlap, relative-entropy data processing and the formation-entanglement bound, treating the Bell-overlap threshold correctly and distinguishing exact preparation cost from regularized rates.

**Dependencies and story role:** Joins M11 and M24 to make the resource consequence quantitative for every mixed input.

**Conceptual connection:** The input entropy lower bound and explicit pure-state entropy match in logarithmic order. The conclusion prevents a nominally full-rank but negligibly entangled preparation from supplying the same constant witness.

**Source pointers:** Watrous §§5.2.1, 5.2.3, Theorem 5.35, §6.2.2 and Exercise 6.3; [formation theorem](../science/entanglement_cost.md#2-from-overlap-to-entanglement-of-formation); [matching preparation](../science/entanglement_cost.md#3-matching-the-order-of-the-preparation-cost).

### M26 — Measure a negative expectation in two contexts

**Central question:** How can a positive operator have a negative expectation inferred from valid measurements?

**Understanding target:** Identify the known negative subspace, construct its positive temporal witness and reconstruct its expectation from baseline and sequential-setting statistics.

**Dependencies and story role:** Uses M05–M06 and M18 to turn the spectral construction into an explicit observable procedure.

**Conceptual connection:** Every outcome is retained, but the baseline has no initial measurement and the other setting does. Their combination is a temporal-data functional, not a negative probability for one ordinary joint event.

**Source pointers:** Watrous §§2.3.1–2.3.2; [two physical contexts](../science/witness.md#two-separate-physical-contexts); [witness operator](../science/witness.md#the-attaining-input-and-its-negative-subspace).

### M27 — Account for the qubit realization

**Central question:** What does one run cost when the local dimension is represented by n qubits?

**Understanding target:** Describe the partially entangled first pair, remaining Bell pairs, joint Bell-effect test, classical predicate and final noisy bit, with preparation and interaction resources included.

**Dependencies and story role:** Combines M10, M17 and M26 into a concrete realization of the otherwise abstract dimension-dependent result.

**Conceptual connection:** Two measurement settings do not make a run free. Cross-register operations, entanglement distribution, ideal internal readout and rotation precision remain physical assumptions or charged implementation requirements.

**Source pointers:** Watrous §2.2.2; [qubit preparation](../science/implementation.md#prepare-the-input); [joint apparatus](../science/implementation.md#realize-the-bell-effect-apparatus); [precision boundary](../science/implementation.md#noise-and-precision-boundary).

### M28 — Keep statistical conclusions within their scope

**Central question:** Which experimental repetition claim follows from the explicit two-setting estimator?

**Understanding target:** Explain why a known constant witness admits a dimension-independent repetition upper bound at fixed confidence, while each repetition still incurs the apparatus and preparation costs.

**Dependencies and story role:** Uses M22 and M26–M27 to separate witness strength, statistical estimation and total implementation resources.

**Conceptual connection:** Small separable negativity alone is not a universal lower bound on every estimator. Other procedures may exploit model knowledge, larger correlators or extra interventions; the theorem makes no universal sampling-speedup claim.

**Source pointers:** Watrous §2.3.2; [estimator scope](../science/witness.md#precision-and-what-the-estimator-establishes); [interpretation limits](../science/interpretation.md#boundaries-of-the-conclusion).

### M29 — Identify the consequential addition

**Central question:** What remains new after the closest earlier frameworks and mechanisms are credited?

**Understanding target:** Separate inherited PDMs, positive temporal witnesses, Bell-overlap constraints and entanglement-assisted noise protection from this fixed-channel all-Schmidt-number converse and matching crossover construction.

**Dependencies and story role:** Integrates the mathematical and operational conclusions of M13–M28 with their primary-source comparisons.

**Conceptual connection:** A shared mechanism does not transfer a different task's advantage automatically. Tailored channel discrimination, postselected amplification and this unconditioned temporal-negativity optimization have different inputs, outputs and performance criteria.

**Source pointers:** Watrous §§2.2.2, 6.1.1 for shared foundations; [related work](../references/RELATED_WORK.md); [scientific distinction](../science/interpretation.md#relation-to-earlier-mechanisms).

### M30 — Reconstruct the whole scientific proposition

**Central question:** How do the mechanism, theorem, resource requirement and observable witness fit together?

**Understanding target:** State the fixed-family uniform law, its all-mixed-input scope, explicit attaining values, formation-entanglement consequence, two-context witness and ideal-apparatus limitations without replacing bounds by exact optima.

**Dependencies and story role:** Synthesizes M13–M29 into the project's account and connects it to the experiment assembled in M12.

**Conceptual connection:** Initial spatial entanglement can materially strengthen temporal causal witnesses under reported-bit noise, with the preparation budget and global interaction charged. The result remains a resource law rather than a universal channel or algorithmic advantage.

**Source pointers:** [Watrous bridge](WATROUS_BRIDGE.md); [science overview](../science/README.md); [main theorem](../science/schmidt_law.md#1-finite-bounds-and-the-uniform-theorem); [scope](../science/interpretation.md#boundaries-of-the-conclusion).
