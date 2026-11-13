# From Watrous to entangled causal witnesses

[Learning route](README.md) · [30 milestones](MILESTONES.md) · [Complete example](WORKED_EXAMPLE.md) · [Science](../science/README.md)

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018)**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) identifies the publication and provides the authorized manuscript; the [publisher's record](https://doi.org/10.1017/9781316848142) identifies the book. The locators below were checked against the author's **2018 standard-layout manuscript**. Page numbers refer to its printed page labels, which differ from a PDF viewer's page count. No copy of the book is included here.

The point of entry is a six-qubit experiment: prepare two correlated registers, apply one known joint test, and combine statistics from two initial measurement choices. The [worked example](WORKED_EXAMPLE.md) follows that experiment. The book supplies the state, measurement, norm and entanglement language needed to understand it; the PDM formalism and this project's quantitative law are supplied separately.

## A selective foundation route

| Needed idea | Verified book locator | Where it enters this project |
|---|---|---|
| Singular values, Schmidt decomposition and operator norms | §1.1.3, starting p. 24; Schmidt decomposition Eq. (1.164), p. 31 | Rank of the input amplitude matrix and the norm estimates in [the converse](../science/schmidt_law.md#2-amplitude-matrices) |
| Convexity | §1.2.1, starting p. 35 | A mixed preparation is a convex combination; a convex negativity bound for every allowed pure input also bounds every allowed mixture |
| States and reduced states | §§2.1.2–2.1.3, pp. 61 and 67 | $`\rho_{AB}`$ is the preparation; $`\rho_B=\operatorname{Tr}_A\rho_{AB}`$ retains one register |
| Channels and their matrix representations | §§2.2.1–2.2.2, pp. 72 and 77; Choi Eqs. (2.64)–(2.66), p. 78 | Verify that the noisy Bell test is a physical channel; keep the Choi convention distinct from the PDM convention |
| Effects, measurements and state update | §§2.3.1–2.3.2, pp. 100 and 105; nondestructive measurements and instruments, pp. 111–112 | The effects $`F_0,F_1`$ specify final probabilities; the initial coarse measurement also has an explicit state update |
| Entropy and relative entropy | §§5.1.1 and 5.2.1, pp. 250 and 265; §5.2.3, p. 276; Theorem 5.35, p. 280 | Count preparation entanglement and apply relative-entropy data processing in [the formation bound](../science/entanglement_cost.md) |
| Separable states and bounded entanglement dimension | §6.1.1, p. 310; Definition 6.14 and Proposition 6.15, pp. 322–324 | Translate the book's “entanglement rank” into the mixed-state Schmidt-number budget $`k`$ |
| Preparation resources | §6.2.2, p. 345; entanglement of formation in Exercise 6.3, p. 385, Eq. (6.437) | Distinguish an input's formation entanglement from asymptotic entanglement cost and from an exact Bell-pair supply |

These are reference points, not a requirement to finish entire chapters before reading the example. The [milestone map](MILESTONES.md) orders the project's own understanding targets.

## Notation dictionary

| Book notation or convention | Notation here | Translation to keep in mind |
|---|---|---|
| A unit vector $`u`$ and pure-state matrix $`uu^*`$ | $`|\psi\rangle`$ and $`|\psi\rangle\langle\psi|`$ | The adjoint $`*`$ is written $`\dagger`$ in the scientific account |
| $`\mathrm D(\mathcal X)`$ | States such as $`\rho_{AB}`$ | Positive operators of trace one |
| Schatten norms $`\|X\|_1,\|X\|_2,\|X\|_\infty`$ | The same norm subscripts | Trace, Hilbert–Schmidt and operator norms; $`\|Y\|_2=1`$ is not an operator-norm condition |
| Entanglement rank bounded by $`k`$ | $`\operatorname{SN}(\rho)\leq k`$ | A mixed-state decomposition with every pure component of Schmidt rank at most $`k`$; ordinary matrix rank of $`\rho`$ is different |
| Entropy $`H`$ | $`S`$ or $`h_2`$ | Base-two von Neumann entropy or the binary entropy; one ebit is the entropy of one Bell pair |
| Ordinary density operators are positive | $`R_{BC}`$ can have negative eigenvalues | $`R`$ summarizes temporal correlators and is not an ordinary prepared state |
| A probability computed from an effect | $`F=\operatorname{Tr}(E_d\rho)`$ | $`F`$ is called **Bell overlap** here; no alternative fidelity convention is implicit |

The Choi conversion deserves its own line. Watrous places the positive Choi operator in **output then input** order. The source PDM formula uses **input then output**, with a transpose on the input factor. If $`S`$ swaps the factors, the corresponding PDM matrix is

```math
M=T_{\rm input}\!\left(SJ(\Gamma)S^\dagger\right).
```

These are unnormalized Choi conventions: no extra division by input dimension is inserted. In particular, substituting the positive $`J(\Gamma)`$ directly for $`M`$ in a Jordan formula is incorrect. This project's [direct effect derivation](../science/model.md#2-the-operational-pdm) avoids that conversion:

```math
R_{BC}=\sum_{j=0}^1H_j\otimes|j\rangle\langle j|,
\qquad
H_j=\frac12\operatorname{Tr}_A(F_j\rho+\rho F_j).
```

## The steps beyond the book

1. **From a state update to temporal data.** For $`P_\pm=(I\pm U)/2`$, the signed difference of the two unnormalized updated states is $`(U\rho+\rho U)/2`$. Applying the final apparatus to that difference gives the sequential correlator. This is the missing connection between an ordinary instrument and the temporal PDM.
2. **From positivity to a temporal witness.** For Hermitian trace-one $`R`$, $`f(R)=\|R\|_1-1=2\operatorname{Tr}R_-`$. The source PDM papers establish the relevant causal null theorem and positive-operator witness framework. These are research-level foundations, attributed in [related work](../references/RELATED_WORK.md), rather than theorems attributed to the textbook.
3. **From Schmidt number to the sharp noise law.** The book's Bell-overlap bound is a starting ingredient. The quadratic dependence at fixed noise additionally needs the completed-square estimate for both $`H_j`$ blocks and the embedded attaining construction in [the main proof](../science/schmidt_law.md). Those arguments establish this project's law.
4. **From dimension to paid entanglement.** A large Schmidt number alone permits very small entropy. [The separate formation theorem](../science/entanglement_cost.md) combines overlap, relative-entropy data processing and inherited entanglement inequalities to show that constant negativity requires logarithmic-order formation entanglement.
5. **From a formal witness to two experiments.** [The estimator](../science/witness.md) compares an undisturbed baseline with a sequential measurement context. Its negative value is not a negative probability, and a negativity ratio does not by itself prove a universal sampling advantage.

## Canonical reading order

Begin with the [complete example](WORKED_EXAMPLE.md), then read the [model](../science/model.md), [uniform Schmidt-number law](../science/schmidt_law.md), [formation bound](../science/entanglement_cost.md), [two-context witness](../science/witness.md), [implementation](../science/implementation.md) and [interpretation](../science/interpretation.md). The [30 milestones](MILESTONES.md) join those files into one local-to-global route. Primary research citations remain in [related work](../references/RELATED_WORK.md); Watrous is the single educational anchor.
