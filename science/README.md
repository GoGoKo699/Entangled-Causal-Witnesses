# The scientific account

How much initial spatial entanglement is needed to obtain a strong temporal causal witness from the same apparatus?

We study an explicit joint measurement on two $`d`$-dimensional systems. It tests the maximally entangled Bell effect, retains one classical bit, and flips that bit with probability $`q`$. The initial $`B`$ event and later output bit define a reduced pseudo-density matrix (PDM). Its negativity $`f=\|R\|_1-1`$ certifies signalling in this experiment, even when the input is initially correlated.

The question is quantitative. Qualitative sufficiency of some product preparation does not mean product preparations provide the strongest negativity.

## Main result

Let $`\mathcal F_k(d,q)`$ be the maximum negativity over all mixed initial states of Schmidt number at most $`k`$. For each fixed $`q_0\lt 1/2`$, uniformly for all integer $`d\geq2`$, $`1\leq k\leq d`$, and $`0\leq q\leq q_0`$,

```math
\boxed{\displaystyle
\mathcal F_k(d,q)
=\Theta_{q_0}\!\left(\frac{k^2}{d(k+qd)}\right).}
```

The proof supplies explicit finite upper bounds and explicit attaining lower bounds. The orders match; exact global optimum constants are not established.

Without output noise, the law is $`\Theta(k/d)`$. At fixed positive noise it is $`\Theta_q((k/d)^2)`$. The crossover occurs when $`q`$ is comparable to $`k/d`$. Thus the optimum over all separable preparations, including arbitrary classical mixtures, is $`\Theta_q(d^{-2})`$ at fixed positive noise, whereas an entangled preparation attains a constant. The latter uses $`\log_2d-O_q(1)`$ ebits of pure-state entanglement. A separate converse proves that every input producing fixed positive negativity has $`\Omega(\log d)`$ entanglement of formation.

The channel has a classical output. The entanglement resource is in the initial preparation, and both input systems enter the joint apparatus. Its magnitude changes the causal influence accessible through that preparation as well as the PDM response. The theorem does not compare inputs with identical operational signalling strength.

## Read the complete argument

| Question | Account |
|---|---|
| What is measured, retained, charged and optimized? | [Model and exact conventions](model.md) |
| Why does every Schmidt-number-bounded state satisfy the converse? | [Sharp law and proof](schmidt_law.md) |
| Which explicit preparations attain the matching orders? | [Attaining families](schmidt_law.md#5-an-attaining-family-for-every-even-schmidt-budget) |
| Why is genuinely large formation entanglement necessary? | [Entanglement cost](entanglement_cost.md) |
| How can the constant witness be measured in two contexts? | [Temporal witness](witness.md) |
| What does a qubit implementation require? | [Implementation](implementation.md) |
| What changes in interpretation, and what is not claimed? | [Interpretation](interpretation.md) |
| Which ingredients and nearby results are inherited? | [Related work](../references/RELATED_WORK.md) |
| What do the numerical checks establish? | [Verification](../verification/README.md) |

The argument connects the standard coarse-measurement PDM and witness framework to a preparation-entanglement budget. The quadratic converse needs a support-aware completed square, beyond the familiar Schmidt-number bound on Bell overlap. The no-noise and noisy regimes belong to one uniform theorem, rather than to incompatible orders of limits.

The apparatus is an engineered global Bell-effect measurement, with ideal preparations and controls apart from the stated output-bit noise. No universal optimality over causal channels, net metrological advantage, or universal sample-complexity separation is inferred from the negativity ratios. The two-setting witness retains both output outcomes and uses distinct initial-measurement contexts; its negative value is not a negative ordinary joint probability.
