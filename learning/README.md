# Learn Entangled Causal Witnesses

[Repository](../README.md) · [Science overview](../science/README.md)

Start with two quantum registers entering a joint Bell test and one noisy reported bit. A measurement on the earlier register changes the experiment, so statistics from two different contexts can reveal a temporal correlation. The central question is how strongly that correlation can be witnessed when the initial entanglement is limited.

## One source and one connected route

The educational anchor is **John Watrous, [The Theory of Quantum Information (2018)](https://cs.uwaterloo.ca/~watrous/TQI/)**, using the author's standard-layout manuscript. The book supplies matrix norms, states, channels, entropy and bipartite entanglement. The temporal-PDM framework and this project's resource law require additional research arguments, identified explicitly in the bridge.

1. **[A complete six-qubit example](WORKED_EXAMPLE.md):** follow preparation, joint measurement, noise, the two ordinary probability tables and the negative temporal witness.
2. **[Watrous-to-project bridge](WATROUS_BRIDGE.md):** read only the relevant foundations, translate the notation and see which steps the project supplies beyond the textbook.
3. **[The 30-milestone map](MILESTONES.md):** connect the individual objects to the full model, then assemble the converse, construction, resource interpretation and scope.
4. **[The scientific account](../science/README.md):** inspect the authoritative theorem and complete proofs; reproduce the [finite checks](../verification/README.md) when useful.

The milestones are common understanding targets for any reader. The first 12 build the background framework from local objects to the whole experiment; the remaining 18 follow the argument from its matrix mechanism to the complete scientific consequence. They provide a path through this project, not an assignment to finish the entire textbook.

## Keep the distinctions visible

The optimized witness is $`f(R)=\lVert R\rVert_1-1`$, twice ordinary trace negativity. For $`0\le q\le q_0<1/2`$, its maximum under initial Schmidt number at most $`k`$ obeys

```math
\mathcal F_k(d,q)
=\Theta_{q_0}\!\left(\frac{k^2}{d(k+qd)}\right).
```

The lower bound concerns an optimum over allowed preparations; some product inputs give zero negativity. The displayed entangled family matches scaling rather than the exact global constant. A negative temporal expectation is reconstructed from two measurement contexts and is not a negative physical probability. Initial entanglement and the joint apparatus are charged, and the final-bit noise model leaves internal operations ideal.

Schmidt number and entanglement of formation answer different resource questions. The two-setting estimator avoids full tomography for this known construction, but the witness-strength ratio is not a universal sampling-complexity separation. These distinctions remain part of the learning route rather than being deferred to a specialist footnote.
