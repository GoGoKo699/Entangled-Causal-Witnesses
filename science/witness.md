# A temporal witness from two measurement settings

[Overview](README.md) · [Model](model.md) · [Resource implementation](implementation.md)

The reduced pseudo-density matrix is inferred from sequential measurement contexts. Its negative expectation under a positive operator witnesses temporal correlations that cannot be represented by a spatial density matrix. For the construction here, that expectation can be obtained without reconstructing all entries of the PDM.

## The attaining input and its negative subspace

Take even $`d`$ and a Hermitian unitary $`U`$ with equal multiplicities of eigenvalues $`+1,-1`$. Define

```math
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{j=1}^{d}|j,j\rangle,
\qquad
|\psi_p\rangle=\sqrt p\,|\Phi_d\rangle
+\sqrt{1-p}\,(I\otimes U)|\Phi_d\rangle.
```

Set $`s=1-2q`$, $`r=\sqrt{p(1-p)}`$. The reduced input state and the Bell-effect Jordan term are

```math
\rho_B=\frac{I+2rU}{d},
\qquad
\frac12\operatorname{Tr}_A\{E_d,\rho_{AB}\}
=\frac{pI+rU}{d}.
```

Consequently, the two classical-output blocks of $`R_{BC}`$ are

```math
H_1=\frac{(q+sp)I+rU}{d},
\qquad
H_0=\frac{(1-q-sp)I+rU}{d}.
```

For $`0\le p\le1/2`$, $`H_0`$ is positive semidefinite. Any negative eigenvalues lie in $`H_1`$ on the $`U=-1`$ subspace. With

```math
p_* =\frac12\left(1-\frac{s}{\sqrt{1+s^2}}\right),
\qquad
f_* =\frac{\sqrt{1+s^2}-1}{2},
```

the input attains $`f(R)=f_*`$. This optimizes this particular balanced-$`U`$ family; it does not assert the all-input optimum.

Let $`\Pi_-=(I-U)/2`$. The operator

```math
W=\Pi_-\otimes|1\rangle\langle1|
```

is positive semidefinite on the formal $`B_1\otimes C_2`$ tensor product. Every ordinary spatial density matrix has a nonnegative expectation under $`W`$. For the attaining temporal data,

```math
w:=\operatorname{Tr}(WR_{BC})=-\frac{f_*}{2}<0
\qquad(0\le q<1/2).
```

The PSD-witness construction is inherited from the spatial-incompatibility framework of Liu, Verma, Xiao, Dahlsten and Gu; the [related-work account](../references/RELATED_WORK.md) identifies the precise contribution of this project.

## Two separate physical contexts

Collect independent runs in each of these settings, using the same initial preparation and channel.

1. **Baseline:** apply the channel with no first-time measurement and estimate $`p_1=\Pr(C=1)`$.
2. **Sequential setting:** measure $`U`$ at the first time, retain its outcome $`u\in\{-1,+1\}`$, then apply the channel and estimate $`m_U=\mathbb E[u\,\mathbf1_{C=1}]`$.

Every run is retained. A zero final bit contributes zero to the second estimator; it is not a postselection condition. The coarse Lüders measurement gives

```math
m_U=\frac12\operatorname{Tr}\!\left[
\rho_{AB}\{I_A\otimes U,F_1\}\right],
\qquad
w=\frac12(p_1-m_U).
```

For the state above,

```math
p_1=q+sp_*,\qquad m_U=r_*,\qquad
\Pr(C=1\mid\text{the }U\text{ setting is used})=\frac12.
```

The last marginal differs from the undisturbed baseline. This is the essential temporal distinction: $`w`$ is a difference of statistics from two contexts, not the probability of one physical joint event. Actual sequential probabilities remain nonnegative. The negative number is the expectation of a positive operator under the reconstructed temporal PDM.

## Precision and what the estimator establishes

The baseline sample lies in $`[0,1]`$ and the sequential sample lies in $`[-1,1]`$. Standard bounded-variable concentration therefore estimates $`w`$ to additive accuracy $`\eta`$ with $`O(\eta^{-2}\log(1/\delta))`$ channel uses at failure probability at most $`\delta`$, divided between two settings. At fixed $`q<1/2`$, $`f_*`$ is independent of $`d`$, so a fixed confidence in the sign requires a number of repetitions independent of $`d`$ for this known witness. Each repetition still incurs the preparation and apparatus costs in the [implementation account](implementation.md).

This is a constructive upper bound for the stated estimator. The small optimized separable negativity does not itself give a converse on every inference method, estimator, adaptive protocol or multi-use experiment. No universal shot advantage is inferred.

## Causal interpretation

Under the fixed-channel, coarse-measurement model, a channel with no signalling from $`B`$ to $`C`$ gives a positive reduced PDM for every initially correlated state. The [model](model.md) supplies the direct proof and credits Liu, Qiu, Dahlsten and Vedral. Initial entanglement therefore does not create a false causal positive within those assumptions. It is the combination of the actual signalling apparatus, initial preparation and first-time measurement disturbance that produces the negative witness.
