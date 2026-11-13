# What the resource law means

[Overview](README.md) · [Model](model.md) · [Schmidt-number proof](schmidt_law.md)

## Qualitative detection and quantitative strength

A signalling channel can possess a pure product input with nonzero temporal PDM negativity. That qualitative existence statement does not promise a dimension-independent negative weight. In the Bell-effect family studied here, the optimum over all separable states—including mixtures with arbitrary classical correlations—is of order $`d^{-2}`$ at fixed nonzero reported-bit noise. The apparatus still signals, and a suitable entangled preparation produces a constant witness.

The sharper statement prices the initial resource continuously through Schmidt number:

```math
F_k(d,q)=\Theta_{q_0}\!\left(\frac{k^2}{d(k+qd)}\right).
```

The transition occurs when $`q`$ is of order $`k/d`$. Below this scale, the optimal response has the noiseless linear order $`k/d`$. Above it, full-support output noise makes the optimized negativity quadratic in that small ratio. One uniform theorem controls both limits; taking $`q\to0`$ inside a fixed-positive-noise asymptotic would miss the crossover.

The negative block is a useful way to see the mechanism. At a pure product input, the nontrivial effective Bell effect has norm $`1/d`$. When a positive baseline of size $`q`$ is present, a small Jordan off-diagonal produces a negative eigenvalue at second order. The [completed-square bound](schmidt_law.md) proves that the same suppression holds for every input with bounded Schmidt number, including mixed inputs. The construction then attains the same scaling.

## What is held fixed

The apparatus and its noise are fixed across the comparison. The initial preparation resource changes. For any fixed pure state on $`A`$, the induced channel from $`B`$ to the output bit has an output-probability diameter at most $`(1-2q)/d`$. With suitable initial entanglement, local changes on $`B`$ can instead change the Bell-test probability by an amount of constant order.

Thus entanglement also changes the causal influence accessible with that initial resource. The theorem does not compare preparations at the same normalized unassisted causal strength. Its contribution is a resource-dependent robustness law for the temporal witness, rather than a claim that a poor witness alone hides an otherwise fixed-strength influence.

The known no-signalling theorem remains essential: initial correlations by themselves do not produce reduced-PDM negativity when the channel has no $`B\to C`$ influence. The [model](model.md) states and reconstructs that implication. Consequently the entangled preparation is not a false-positive confounder in the specified model.

## Entanglement is necessary and charged

At any fixed positive $`q<1/2`$, constant negativity forces Schmidt number of order $`d`$. Large Schmidt rank alone could coexist with very little entropy, so a second argument is needed. The [entanglement account](entanglement_cost.md) shows that constant negativity also requires $`\Omega_q(\log d)`$ entanglement of formation for one prepared input. An explicit pure state uses $`\log_2d-O_q(1)`$ ebits, matching the required order.

Entanglement of formation is a single-state quantity. The theorem does not identify it with the regularized asymptotic entanglement cost of arbitrary mixed states, nor does it establish an optimal distillation or amortized formation rate.

When $`d=2^n`$, the dimension-dependent gap is exponential in $`n`$, while the attaining state requires order $`n`$ ebits and an explicit joint apparatus with order $`n`$ gates and workspace in a direct implementation. These resources are described in [the implementation](implementation.md); an exponentially large abstract dimension is not a free preparation or interaction resource.

## Relation to earlier mechanisms

The Bell-overlap constraint $`\langle\Phi_d|\rho|\Phi_d\rangle\le k/d`$ for Schmidt-number-$`k`$ states is inherited. So are the PDM framework, positive temporal witnesses, qualitative product-input completeness, and entanglement-assisted protection against readout noise in weak-value protocols. Applying only the overlap constraint and a generic linear PDM bound would give order $`k/d`$, which does not establish the fixed-noise squared law for every allowed input.

The new account is the fixed-channel converse, matching construction and uniform noise crossover, together with their initial-entanglement consequence. The [source comparison](../references/RELATED_WORK.md) distinguishes its model from tailored ancilla-assisted channel discrimination and postselected metrological amplification. Shared ingredients do not imply that those other operational advantages have been achieved here.

## Boundaries of the conclusion

The family has a known global Bell effect, one final noisy output bit, and ideal internal preparation and operations. It supplies a controlled example and a matching-order theorem, rather than an optimum over arbitrary signalling channels or arbitrary apparatus noise.

The two-setting witness can be estimated directly; full PDM tomography is unnecessary for that construction. Small negativity alone does not impose the same cost on all possible statistical procedures. A different estimator may exploit larger off-diagonal signals, model information or additional interventions. Universal sampling-complexity, communication-capacity and computational-advantage claims therefore remain outside the result.

Finally, the balanced construction is not the exact global optimizer of negativity. Explicit finite bounds and matching scaling are the supported endpoint. Optimizing all constants or adding unrelated channel families is not required for that endpoint.
