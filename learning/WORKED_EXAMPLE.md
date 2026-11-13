# A complete six-qubit experiment

[Learning route](README.md) · [Watrous bridge](WATROUS_BRIDGE.md) · [30 milestones](MILESTONES.md) · [Scientific model](../science/model.md)

Take a three-qubit register $`A`$ and a three-qubit register $`B`$. Each register has dimension $`d=8`$. A known apparatus tests whether the six-qubit input equals three specified Bell pairs, then reports one noisy bit. We compare input preparations while keeping that apparatus fixed.

The example shows a strict finite-dimensional gap: one entangled preparation has PDM negativity approximately $`0.140312`$, whereas **every separable preparation**, including classically correlated mixtures, has negativity at most $`1/18\approx0.055556`$. The latter is a proved finite upper bound, not a claim to have found the exact separable optimum.

## 1. Specify the apparatus

For one pair let $`|\Phi^\pm\rangle=(|00\rangle\pm|11\rangle)/\sqrt2`$. The ideal success effect is

```math
E_8=|\Phi_8\rangle\langle\Phi_8|,
\qquad
|\Phi_8\rangle=|\Phi^+\rangle_{A_1B_1}
\otimes|\Phi^+\rangle_{A_2B_2}
\otimes|\Phi^+\rangle_{A_3B_3}.
```

One implementation measures each pair in its Bell basis and computes whether **all three** outcomes were $`\Phi^+`$. The apparatus keeps that single truth value. It flips this final bit with probability $`q=1/10`$, so $`s=1-2q=4/5`$ and

```math
F_1=\frac1{10}I+\frac45E_8,
\qquad
F_0=I-F_1.
```

The bit flip is one error **after** the ideal all-Bell-success predicate. It is not an independent error on every pair detector before the predicate. The internal Bell measurements, input preparation and initial measurement choice below are ideal in this model.

## 2. Prepare the entangled input

Let $`U=Z`$ on $`B_1`$, with identity on $`B_2B_3`$. Choose

```math
p_* =\frac12\left(1-\frac4{\sqrt{41}}\right)
\approx0.1876524762,
\qquad
r_* =\sqrt{p_*(1-p_*)}=\frac5{2\sqrt{41}}.
```

Prepare

```math
|\psi\rangle=
\left(\sqrt{p_*}|\Phi^+\rangle
+\sqrt{1-p_*}|\Phi^-\rangle\right)_{A_1B_1}
\otimes|\Phi^+\rangle_{A_2B_2}
\otimes|\Phi^+\rangle_{A_3B_3}.
```

Only the first pair is partially entangled. Its computational-basis amplitudes are

```math
\sqrt{\lambda_+}|00\rangle-\sqrt{\lambda_-}|11\rangle,
\qquad
\lambda_\pm=\frac12\left(1\pm\frac5{\sqrt{41}}\right).
```

The minus sign matters: it makes the unmeasured first pair's Bell-success probability $`p_*`$, rather than $`1-p_*`$.

## 3. Collect two ordinary data sets

Use independent repetitions of the same preparation and apparatus.

**Baseline context:** do not measure $`B`$ initially. The overlap with $`|\Phi_8\rangle`$ is $`p_*`$, so the reported-one probability is

```math
p_1=\Pr(C=1\mid\text{baseline})
=\frac1{10}+\frac45p_*
=\frac12-\frac8{5\sqrt{41}}
\approx0.2501219810.
```

**Sequential context:** measure only $`Z`$ on $`B_1`$ first, retaining its signed outcome $`u=+1`$ or $`-1`$. Do not resolve all eight basis strings of $`B`$. This is the coarse measurement of $`U`$. Then apply the same apparatus.

The initial outcomes have probabilities $`\Pr(u=\pm1)=\lambda_\pm`$. Conditional on either outcome, the first pair is $`|00\rangle`$ or $`|11\rangle`$. Each has Bell-success probability $`1/2`$; the other two pairs still succeed with certainty. The final noisy reported bit is therefore fair in either branch. The full sequential probabilities are

| First outcome | $`C=1`$ | $`C=0`$ |
|---|---:|---:|
| $`u=+1`$ | $`(1+5/\sqrt{41})/4\approx0.4452172024`$ | $`(1+5/\sqrt{41})/4\approx0.4452172024`$ |
| $`u=-1`$ | $`(1-5/\sqrt{41})/4\approx0.0547827976`$ | $`(1-5/\sqrt{41})/4\approx0.0547827976`$ |

All four probabilities are positive and sum to one. They give

```math
m_U=\mathbb E[u\,\mathbf1_{C=1}]
=\frac5{2\sqrt{41}}\approx0.3904344047.
```

Every repetition contributes: a final zero contributes zero to this signed average and is still retained. The final-one probability in this sequential context is $`1/2`$, which differs from the baseline. The initial measurement changes the state entering the apparatus.

## 4. Assemble the temporal witness

The reduced PDM keeps the initial $`B`$ event and the later bit $`C`$. Let

```math
W=\frac{I-U}{2}\otimes|1\rangle\langle1|.
```

It is a positive operator on the formal two-event tensor product. The measured temporal functional is

```math
w=\operatorname{Tr}(WR_{BC})
=\frac12(p_1-m_U)
=\frac{5-\sqrt{41}}{20}
\approx-0.0701562119.
```

This is a difference between statistics from **two contexts**, not the probability $`\Pr(u=-1,C=1)`$ from the table. That actual joint probability is positive. The negative temporal functional rules out an ordinary positive density matrix for these correlators.

Here the negative PDM eigenvalues all lie in the $`U=-1,C=1`$ block selected by $`W`$. With the repository's convention,

```math
f(R)=\|R\|_1-1=-2w
=\frac{\sqrt{41}-5}{10}
\approx0.1403124237.
```

The [causal null theorem](../science/model.md#3-what-negativity-certifies) ensures that initial entanglement does not create a false signalling positive under this model: a channel unable to signal from $`B`$ to $`C`$ has positive reduced PDM for every initial state.

## 5. Compare every separable preparation

For $`k=1`$, the finite quadratic converse in [the main theorem](../science/schmidt_law.md#1-finite-bounds-and-the-uniform-theorem) gives

```math
\mathcal F_1(8,1/10)
\leq\frac{(4/5)^2}{2(1/10)(9/10)8^2}
=\frac1{18}
\lt\frac{\sqrt{41}-5}{10}.
```

Both sides use the same effects and readout error. The bound includes every separable mixed preparation, so changing product states or mixing them with shared classical randomness cannot close this finite gap. The example does not assert that the displayed entangled state is globally optimal over all entangled inputs.

## 6. Account for the resources

The input has Schmidt rank eight. Its pure-state entanglement of formation is

```math
E_F(\psi)=2+h_2\!\left(\frac{1+5/\sqrt{41}}2\right)
\approx2.4986042704\ \text{ebits}.
```

That is two full Bell-pair ebits plus the first pair's partial entanglement. Three Bell pairs are a sufficient exact one-use supply if the state is prepared by LOCC from Bell pairs; this supply count is distinct from the noninteger value $`E_F`$. The input is consumed on each run. The two three-qubit registers, cross-register Bell tests and classical all-success computation are also part of the experiment's resources.

Schmidt number counts entanglement dimension; entropy counts a different resource. Full Schmidt rank alone can coexist with tiny entropy. The [separate formation theorem](../science/entanglement_cost.md) proves that constant temporal negativity in this family requires logarithmic-order formation entanglement as $`d`$ grows.

The known witness needs only two measurement settings, but a setting is not a free run. Each repetition pays for preparation and the joint apparatus. The gap in mathematical negativity supplies no universal lower bound on the samples needed by every separable-input inference protocol, and the proof does not cover arbitrary internal gate, detector or preparation noise.
