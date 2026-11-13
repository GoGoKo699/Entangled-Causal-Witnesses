# Entangled Causal Witnesses

**How much initial entanglement is needed to obtain a strong temporal witness of causal influence?** Product inputs can detect signalling in principle, yet that qualitative fact does not guarantee a witness of useful strength. This project gives an explicit process for which the optimized witness strength depends sharply on the available initial entanglement and the noise in one reported bit.

Two registers $`A,B`$ each have dimension $`d`$. A fixed joint apparatus tests the maximally entangled Bell projector, emits one classical bit at $`C`$, and flips that bit with probability $`q`$. For the reduced two-time pseudo-density matrix $`R_{BC}`$, use the trace-norm negativity $`f(R)=\lVert R\rVert_1-1`$. Let $`F_k(d,q)`$ be the largest value attainable with an initial state of Schmidt number at most $`k`$ across $`A\mid B`$.

For every fixed $`q_0\lt1/2`$, uniformly over $`d\ge2`$, $`1\le k\le d`$ and $`0\le q\le q_0`$,

```math
F_k(d,q)=\Theta_{q_0}\!\left(\frac{k^2}{d(k+qd)}\right).
```

The [proof](science/schmidt_law.md) supplies finite upper bounds and explicit inputs attaining the same order. The displayed input family need not maximize the exact constant.

| Regime | Optimized witness strength | Consequence |
|---|---|---|
| No reported-bit noise | $`\Theta(k/d)`$ | Initial entanglement dimension controls a linear response. |
| Any fixed $`0\lt q\lt1/2`$ | $`\Theta_q((k/d)^2)`$ | Full-support noise makes low-Schmidt-number witnesses quadratically weak. |
| Separable inputs, fixed positive noise | $`\Theta_q(d^{-2})`$ | Classical correlations in the preparation do not remove the suppression. |
| Suitable entangled inputs with Schmidt number $`\Theta(d)`$ | A positive constant independent of $`d`$ | A two-setting temporal witness remains strong. |

Constant witness strength requires $`\Omega_q(\log d)`$ entanglement of formation for a single prepared input; an explicit pure input uses $`\log_2 d-O_q(1)`$ ebits. This is a statement about the initial preparation resource, with the joint apparatus and its implementation also charged.

## Read the science

Start with the [connected overview](science/README.md), or follow the question that matters to you.

| Question | Account |
|---|---|
| What process, temporal data and entanglement budget are specified? | [Model and conventions](science/model.md) |
| Why does the uniform dimension–entanglement–noise law hold? | [Schmidt-number law](science/schmidt_law.md) |
| Why is a large initial entanglement resource necessary? | [Entanglement of formation](science/entanglement_cost.md) |
| How is negativity observed without reconstructing the full PDM? | [Two-setting witness](science/witness.md) |
| What gates, preparation, workspace and noise assumptions are used? | [Implementation and resources](science/implementation.md) |
| What changes physically, and what remains outside the result? | [Interpretation](science/interpretation.md) |
| Which ingredients are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Which finite calculations can be reproduced? | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps detailed questions to their authoritative files.

## Learn the argument

The educational anchor is **John Watrous, [The Theory of Quantum Information (2018)](https://cs.uwaterloo.ca/~watrous/TQI/)**, using the author's standard-layout manuscript. Start with the [complete six-qubit example](learning/WORKED_EXAMPLE.md), then use the [source bridge](learning/WATROUS_BRIDGE.md) and [30-milestone map](learning/MILESTONES.md) to connect the foundations to the resource law. The [learning guide](learning/README.md) explains the route; the direct scientific reading path remains available above.

## Scope

The law concerns a specified family of known global Bell-effect channels and the strength of a particular temporal-correlation measure. Both input registers enter that apparatus. The entangled register is not an untouched external reference.

The noise acts on one final reported bit. State preparation, internal gates and the first-time measurement are ideal in this model; independent errors throughout those operations are not covered. Initial entanglement also changes the causal influence accessible with that preparation resource, so the comparison does not hold an unassisted causal-strength normalization fixed.

The two-setting construction gives a direct witness estimator. The negativity law alone supplies no universal sampling-complexity separation, channel-capacity advantage or algorithmic speedup. Exact optimizing states and constants remain separate from the proved matching-order law.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
