# Entanglement needed for a constant witness

[Science overview](README.md) · [Model](model.md) · [Schmidt-number law](schmidt_law.md) · [Temporal witness](witness.md)

Large Schmidt number need not imply large entanglement entropy. This page gives a separate lower bound on the entanglement of formation of every input that produces a fixed positive PDM negativity. The proof uses standard relative-entropy entanglement and Bell-overlap ingredients, after deriving a channel-specific bound on how much negativity a given overlap can produce.

Throughout, logarithms in entanglement measures have base two, and $`f=\Vert R\Vert_1-1`$ has the normalization of the [model](model.md).

## 1. A bound in terms of Bell overlap

For any initial state define

```math
F=\mathrm{Tr}(E_d\rho_{AB})\in[0,1],
\qquad s=1-2q.
```

The reduced PDM obeys

```math
f(R_{BC}(\rho))\leq g_q(F),
```

```math
g_q(F)=\sqrt{q^2+sF}
       +\sqrt{(1-q)^2-sF}-1.
```

This bound is valid for mixed inputs and includes $`q=0`$.

**Proof for a pure input.** Before tracing out $`A`$, the full input-to-output PDM has blocks

```math
K_1=q\rho+\frac{s}{2}(E_d\rho+\rho E_d),
\qquad
K_0=(1-q)\rho-\frac{s}{2}(E_d\rho+\rho E_d).
```

For $`\rho=|\psi\rangle\langle\psi|`$, these blocks are supported in the span of $`|\psi\rangle`$ and $`|\Phi_d\rangle`$. Choose the phase of the latter so its overlap with $`|\psi\rangle`$ is $`\sqrt F`$. In an orthonormal basis beginning with $`|\psi\rangle`$, the two blocks are

```math
K_1=
\begin{pmatrix}
q+sF & s\sqrt{F(1-F)}/2\\
s\sqrt{F(1-F)}/2&0
\end{pmatrix},
```

```math
K_0=
\begin{pmatrix}
1-q-sF &-s\sqrt{F(1-F)}/2\\
-s\sqrt{F(1-F)}/2&0
\end{pmatrix}.
```

Endpoint cases follow by continuity. Their trace norms are $`\sqrt{q^2+sF}`$ and $`\sqrt{(1-q)^2-sF}`$, because $`2q+s=1`$ and $`2(1-q)-s=1`$. Thus the full PDM has exactly the negativity $`g_q(F)`$. Its partial trace over $`A`$ is the reduced $`R_{BC}`$. Trace-norm contractivity under that partial trace proves the desired inequality.

**Extension to mixed inputs.** Decompose $`\rho=\sum_i p_i\rho_i`$ into pure states, with overlaps $`F_i`$. The function $`g_q`$ is concave on $`[0,1]`$, as a sum of square roots of nonnegative affine functions. Convexity of the PDM negativity therefore gives

```math
f(R(\rho))\leq\sum_i p_i f(R(\rho_i))
\leq\sum_i p_i g_q(F_i)
\leq g_q\!\left(\sum_i p_iF_i\right)=g_q(F).
```

In particular, maximizing this one-variable envelope gives a dimension-independent all-input bound:

```math
f(R_{BC})\leq\max_{0\leq F\leq1}g_q(F)
=\sqrt{1+s^2}-1.
```

The maximum of the envelope occurs at $`F=1/2`$. This does not assert that a reduced PDM attains it: tracing out $`A`$ can strictly reduce the negativity.

For fixed $`0\lt q\lt 1/2`$, the tangent to $`g_q`$ at zero yields the convenient linear bound

```math
g_q(F)\leq C_qF,
\qquad C_q=\frac{s^2}{2q(1-q)}.
```

Indeed $`g_q(0)=0`$ and $`g_q'(0)=C_q`$, so this follows from concavity. There is also a bound with no singularity at $`q=0`$:

```math
f(R_{BC})\leq\sqrt F.
```

To see it, output-bit flips are a classical postprocessing of the noiseless PDM and cannot increase its trace norm. At $`q=0`$, the envelope is $`g_0(F)=\sqrt F+\sqrt{1-F}-1\leq\sqrt F`$. The same mixed-input argument applies.

## 2. From overlap to entanglement of formation

Let $`E_F(\rho)`$ denote the usual entanglement of formation: the minimum average pure-state entanglement entropy over decompositions of $`\rho`$. Let

```math
E_R(\rho)=\inf_{\sigma\in\mathrm{SEP}}D_2(\rho\Vert\sigma)
```

be relative-entropy entanglement, with logarithms of base two. The standard inequality $`E_F\geq E_R`$ and quantum relative-entropy data processing are inherited tools; [related work](../references/RELATED_WORK.md) records their attribution.

Every separable state has Bell overlap at most $`1/d`$. For a product vector this is Cauchy–Schwarz applied to $`\langle\Phi_d|a,b\rangle`$; convexity extends it to all separable states. Measuring $`\{E_d,I-E_d\}`$ in the relative-entropy data-processing inequality therefore gives, whenever $`F\geq1/d`$,

```math
E_R(\rho)
\geq D_{\rm bin}(F\Vert1/d)
\geq F\log_2d-h_2(F).
```

For completeness, the first inequality has a threshold condition. The measured overlap of a separable comparison state is some $`G\leq1/d`$. For $`F\geq1/d`$, the binary relative entropy $`D_{\rm bin}(F\Vert G)`$ decreases with $`G`$ on that interval, so its minimum is at $`G=1/d`$. No such minimization claim is made when $`F\lt 1/d`$. The second inequality follows by expanding

```math
D_{\rm bin}(F\Vert1/d)
=F\log_2d-h_2(F)
 -(1-F)\log_2(1-1/d).
```

The last term is nonnegative. When $`F\lt 1/d`$, the expression $`F\log_2d-h_2(F)`$ is nonpositive, because $`h_2(F)\geq F\log_2(1/F)\geq F\log_2d`$. Nonnegativity of entanglement then gives the same weaker conclusion. Hence the useful inequality

```math
E_F(\rho)\geq F\log_2d-h_2(F)
            \geq F\log_2d-1
```

holds for every initial state, without a threshold exception.

Combining it with the overlap bounds proves:

```math
\boxed{\displaystyle
E_F(\rho)\geq\max\{0,\ f(R_{BC})^2\log_2d-1\}.}
```

For $`0\lt q\lt 1/2`$ one may additionally use

```math
\boxed{\displaystyle
E_F(\rho)\geq\max\left\{0,
\frac{2q(1-q)}{(1-2q)^2}f(R_{BC})\log_2d-1\right\}.}
```

The two lower bounds are both valid; neither is asserted to give optimal constants. In particular, any fixed negativity $`f\geq\varepsilon>0`$ requires $`\Omega_\varepsilon(\log d)`$ entanglement of formation, including the noiseless case. At fixed positive $`q`$, the linear-in-$`f`$ bound gives an additional explicit coefficient.

## 3. Matching the order of the preparation cost

For even $`d`$, the full-support family of the [Schmidt-law proof](schmidt_law.md#5-an-attaining-family-for-every-even-schmidt-budget), with its optimized $`p_*`$, attains

```math
f_{\rm att}(q)=\frac{\sqrt{1+(1-2q)^2}-1}{2}>0.
```

For $`r=\sqrt{p_*(1-p_*)}`$, its reduced-state eigenvalues are $`(1+2r)/d`$ and $`(1-2r)/d`$, each repeated $`d/2`$ times. Since the input is pure, its entanglement of formation is exactly

```math
E_F(\psi_{p_*})
=\log_2(d/2)+h_2\!\left(\frac{1+2r}{2}\right)
=\log_2d-O_q(1).
```

For odd $`d`$, embed the even support $`d-1`$. The exact attained value is $`L((d-1)/d,q)`$, which tends to $`f_{\rm att}(q)`$ as $`d`$ grows, and the preparation entropy is $`\log_2(d-1)-O_q(1)`$. Thus constant witness strength needs and admits logarithmic-order preparation entanglement in this family.

This is a preparation-resource statement about $`E_F`$. It also lower-bounds the number of initially supplied Bell-pair ebits for an exact one-use LOCC preparation, by monotonicity of $`E_F`$; any other initially supplied entanglement must be charged as well. It does not identify $`E_F`$ with the regularized asymptotic entanglement cost, nor claim an optimal amortized dilution or distillation rate.

The Schmidt-number theorem and this entropy theorem serve different purposes. The former resolves the full dimension/noise crossover under a rank constraint, including a quadratic suppression that Bell overlap alone does not provide. The latter rules out obtaining a constant witness from states with large rank but negligible formation entanglement.
