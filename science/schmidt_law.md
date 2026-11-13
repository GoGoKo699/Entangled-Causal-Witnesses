# A sharp dimension, entanglement and noise law

[Science overview](README.md) · [Model](model.md) · [Entanglement cost](entanglement_cost.md) · [Temporal witness](witness.md)

This page proves the main theorem for the fixed Bell-effect measurement channel of the [model](model.md). The optimized quantity $`\mathcal F_k(d,q)`$ uses all initial mixed states of Schmidt number at most $`k`$. The normalization is $`f(R)=\|R\|_1-1`$.

## 1. Finite bounds and the uniform theorem

Put $`s=1-2q`$ and define

```math
L(t,q)=\frac{\sqrt{(2q+st)^2+(st)^2}-(2q+st)}2,
\qquad 0\lt t\leq1.
```

For an integer $`1\leq k\leq d`$, let

```math
m(k)=
\begin{cases}
1,&k=1,\\
2\lfloor k/2\rfloor,&k\geq2.
\end{cases}
```

**Finite-bound theorem.** For every integer $`d\geq2`$, every $`1\leq k\leq d`$, and $`0\leq q\lt 1/2`$,

```math
L\!\left(\frac{m(k)}d,q\right)
\leq\mathcal F_k(d,q)
\leq 2(1-2q)\frac{k}{d}.
```

For $`q>0`$ there is also the stronger upper bound

```math
\mathcal F_k(d,q)
\leq\frac{(1-2q)^2 k^2}{2q(1-q)d^2}.
```

These are bounds on the global optimization. The lower bound is an explicitly attained value, not a claim that its input globally optimizes the PDM negativity.

**Uniform consequence.** Fix any $`0\leq q_0\lt 1/2`$ and write $`s_0=1-2q_0`$. Simultaneously for all $`d,k`$ above and all $`0\leq q\leq q_0`$,

```math
\frac{s_0^2}{16(1+\sqrt2)}
\frac{k^2}{d(k+qd)}
\leq\mathcal F_k(d,q)
\leq4\frac{k^2}{d(k+qd)}.
```

In particular,

```math
\boxed{\displaystyle
\mathcal F_k(d,q)
=\Theta_{q_0}\!\left(\frac{k^2}{d(k+qd)}\right).}
```

The constants are independent of how $`d`$, $`k`$, and $`q`$ vary within the stated range. Keeping $`q_0`$ strictly below $`1/2`$ matters: the channel becomes a constant fair-bit channel at $`q=1/2`$, where every negativity vanishes.

## 2. Amplitude matrices

It first suffices to consider a pure input. Write it with a matrix whose rows are indexed by $`B`$ and columns by $`A`$:

```math
|\psi\rangle=\sum_{i,j=1}^dY_{ji}|i\rangle_A|j\rangle_B,
\qquad \|Y\|_2=1,
\qquad \operatorname{rank}Y\leq k.
```

Here $`\|Y\|_2`$ is the Hilbert–Schmidt norm, not the operator norm. Set $`\alpha=\operatorname{Tr}Y`$. Direct partial tracing gives

```math
\rho_B=YY^\dagger,
\qquad
H_E:=\frac12\operatorname{Tr}_A(E_d\rho+\rho E_d)
=\frac{\alpha Y^\dagger+\overline\alpha Y}{2d}.
```

For example, $`\langle\Phi_d|\psi\rangle=\alpha/\sqrt d`$, and $`\operatorname{Tr}_A(E_d\rho)=\alpha Y^\dagger/d`$; averaging with its adjoint proves the second identity. Thus the two PDM blocks are

```math
H_1=qYY^\dagger+\frac{s}{2d}
               (\alpha Y^\dagger+\overline\alpha Y),
```

```math
H_0=(1-q)YY^\dagger-\frac{s}{2d}
               (\alpha Y^\dagger+\overline\alpha Y).
```

Two elementary norm bounds will be used:

```math
|\alpha|\leq\|Y\|_1\leq\sqrt{k}\|Y\|_2=\sqrt{k},
\qquad
\|H_E\|_1\leq\frac{|\alpha|\|Y\|_1}{d}\leq\frac{k}{d}.
```

The first inequality is the trace/operator-norm duality with the identity; the second uses Cauchy–Schwarz on at most $`k`$ nonzero singular values.

## 3. The linear upper bound

Apply the trace-norm triangle inequality to the two blocks:

```math
\begin{aligned}
\|H_1\|_1&\leq q\operatorname{Tr}(YY^\dagger)+s\|H_E\|_1,\\
\|H_0\|_1&\leq(1-q)\operatorname{Tr}(YY^\dagger)+s\|H_E\|_1.
\end{aligned}
```

Since $`\operatorname{Tr}(YY^\dagger)=1`$, subtraction of the unit trace yields

```math
f(R_{BC})\leq2s\|H_E\|_1\leq2s\frac{k}{d}.
```

This proof includes $`q=0`$.

## 4. The quadratic upper bound

Assume $`q>0`$. Let $`P`$ be the orthogonal projection onto the row support $`\operatorname{ran}Y^\dagger`$, of rank at most $`k`$. Then $`YP=Y`$ and $`PY^\dagger=Y^\dagger`$. Define $`\beta=s\alpha/(2d)`$. Completing the square gives the exact identities

```math
H_1=q\left(Y+\frac\beta qP\right)
          \left(Y+\frac\beta qP\right)^\dagger
       -\frac{|\beta|^2}{q}P,
```

```math
H_0=(1-q)\left(Y-\frac\beta{1-q}P\right)
          \left(Y-\frac\beta{1-q}P\right)^\dagger
       -\frac{|\beta|^2}{1-q}P.
```

If a Hermitian matrix has the form $`K=S-cP`$ with $`S\succeq0`$, $`c\geq0`$, and $`P`$ a projection, then

```math
\operatorname{Tr}K_-
=-\operatorname{Tr}(\Pi_-K)
\leq c\operatorname{Tr}(\Pi_-P)
\leq c\operatorname{Tr}P,
```

where $`\Pi_-`$ is its negative spectral projection. Applying this fact to the two completed squares and recalling that $`f`$ is twice the sum of the negative weights gives

```math
\begin{aligned}
f(R_{BC})
&\leq2k|\beta|^2\left(\frac1q+\frac1{1-q}\right)\\
&=\frac{s^2 k|\alpha|^2}{2q(1-q)d^2}
\leq\frac{s^2 k^2}{2q(1-q)d^2}.
\end{aligned}
```

Every mixed state of Schmidt number at most $`k`$ is a convex combination of pure states satisfying the same bound. Convexity of $`f`$ therefore extends both upper bounds to the full mixed-state optimization.

The completed square is essential to the stronger conclusion. The standard Bell-overlap inequality $`\operatorname{Tr}(E_d\rho)\leq k/d`$ combined with a generic overlap-based upper bound would give only a linear $`O_q(k/d)`$ estimate. The argument above gives the square $`O_q((k/d)^2)`$ at fixed positive noise.

## 5. An attaining family for every even Schmidt budget

Take an even integer $`m\leq k`$. On the first $`m`$ basis states define the maximally entangled vector $`|\Phi_m\rangle`$ and a diagonal Hermitian unitary $`U_m`$ with $`m/2`$ eigenvalues of each sign. Regard these as embedded in the $`d`$-dimensional spaces. The vectors $`|\Phi_m\rangle`$ and $`(I\otimes U_m)|\Phi_m\rangle`$ are orthogonal. For $`0\leq p\leq1/2`$ prepare

```math
|\psi_p^{(m)}\rangle
=\sqrt p\,|\Phi_m\rangle
 +\sqrt{1-p}\,(I\otimes U_m)|\Phi_m\rangle.
```

Its Schmidt rank is at most $`m`$. Put $`t=m/d`$ and $`r=\sqrt{p(1-p)}`$. On the embedded support,

```math
\rho_B=\frac{I_m+2rU_m}{m},
\qquad
H_E=\frac{pI_m+rU_m}{d}.
```

The eigenvalues of the PDM blocks are therefore

```math
H_1:\quad
\frac{q+stp\pm(2q+st)r}{m},
```

```math
H_0:\quad
\frac{1-q-stp\pm(2(1-q)-st)r}{m},
```

each repeated $`m/2`$ times; the remaining eigenvalues vanish. The lower sign of $`H_0`$ is nonnegative, because

```math
1-q-stp-(2(1-q)-st)r
=(1-q)(1-2r)+st(r-p)\geq0.
```

Here $`2r\leq1`$ and $`r\geq p`$ on the chosen interval. The upper sign of $`H_1`$ is nonnegative. Consequently its lower sign is the only possible negative eigenvalue type, and the exact attained negativity is

```math
f(R_{BC}(\psi_p^{(m)}))
=[(2q+st)\sqrt{p(1-p)}-stp-q]_+.
```

For $`a=2q+st`$ and $`b=st`$, maximization within this family gives

```math
p_*=\frac12\left(1-\frac{b}{\sqrt{a^2+b^2}}\right),
\qquad
\max_p[a\sqrt{p(1-p)}-bp]
=\frac{\sqrt{a^2+b^2}-b}{2}.
```

One can verify the second identity by setting $`2p-1=-\cos\theta`$, or by differentiating. The stated $`p_*`$ lies in $`(0,1/2)`$ because $`a,b>0`$. Subtracting $`q`$ gives the strictly positive value $`L(t,q)`$ in the theorem.

## 6. Separable preparations and odd Schmidt budgets

For a pure product input $`|a\rangle_A|b\rangle_B`$, let

```math
c=|\langle a^*|b\rangle|^2,
\quad
u=\frac{s\sqrt{c(1-c)}}{2d},
\quad
a_1=q+\frac{sc}{d},
\quad
a_0=1-q-\frac{sc}{d}.
```

In the span of $`|b\rangle`$ and $`|a^*\rangle`$, with the first vector $`|b\rangle`$, phases can be chosen so that the blocks are

```math
H_1=\begin{pmatrix}a_1&u\\u&0\end{pmatrix},
\qquad
H_0=\begin{pmatrix}a_0&-u\\-u&0\end{pmatrix}.
```

The formula includes the degenerate endpoint cases by continuity. Each block's trace norm is the square root of its squared diagonal trace plus $`4u^2`$. Thus

```math
f_{\rm prod}(c)
=\sqrt{a_1^2+4u^2}-a_1
 +\sqrt{a_0^2+4u^2}-a_0.
```

All $`c\in[0,1]`$ are realizable when $`d\geq2`$. Convexity therefore gives the exact one-variable reduction

```math
\mathcal F_1(d,q)=\max_{0\leq c\leq1}f_{\rm prod}(c).
```

At $`c=1/2`$, the first block alone contributes

```math
\sqrt{\left(q+\frac{s}{2d}\right)^2+\frac{s^2}{4d^2}}
 -q-\frac{s}{2d}
=L(1/d,q).
```

This proves the required lower bound for $`k=1`$. For every $`k\geq2`$ choose the largest even $`m\leq k`$ in the preceding construction. This includes odd $`k`$ and odd $`d`$. No even-dimension restriction remains in the theorem.

For reference, the exact product formula also gives a sharper fixed-noise asymptotic. For each fixed $`0\lt q\lt 1/2`$, expansion uniformly over $`c\in[0,1]`$ yields

```math
\mathcal F_1(d,q)
=\frac{s^2}{8q(1-q)d^2}+O_q(d^{-3}).
```

Indeed $`a_1\geq q`$, $`a_0\geq1/2`$, and
$`\sqrt{a^2+4u^2}-a=2u^2/a+O_q(u^4)`$. Replacing the two denominators by $`q`$ and $`1-q`$ incurs a uniform $`O_q(d^{-3})`$ error. The leading coefficient is proportional to $`c(1-c)`$ and is maximized at $`c=1/2`$.

## 7. Uniform constants

Let $`t=k/d`$ and $`\tau=m(k)/d`$, so $`t/2\leq\tau\leq t`$. Rationalizing the lower-bound expression gives

```math
L(\tau,q)
=\frac{s^2\tau^2}
 {2\left(\sqrt{(2q+s\tau)^2+(s\tau)^2}+2q+s\tau\right)}.
```

Since $`s\tau\leq2q+s\tau`$, its denominator is at most
$`2(1+\sqrt2)(2q+s\tau)\leq4(1+\sqrt2)(q+\tau)`$. Consequently

```math
L(\tau,q)
\geq\frac{s_0^2}{4(1+\sqrt2)}\frac{\tau^2}{q+\tau}
\geq\frac{s_0^2}{16(1+\sqrt2)}\frac{t^2}{q+t}.
```

For the upper bound, $`1-q\geq1/2`$ and $`s\leq1`$ give

```math
\mathcal F_k(d,q)\leq\min\{2t,t^2/q\},\qquad q>0.
```

If $`q\leq t`$, use $`2t\leq4t^2/(q+t)`$; if $`q\geq t`$, use $`t^2/q\leq2t^2/(q+t)`$. At $`q=0`$ the linear bound is already at most $`4t`$. This completes the proof with the displayed uniform constants.

## 8. Meaning of the crossover

For $`q=0`$, $`\mathcal F_k=\Theta(k/d)`$. When $`q\gg k/d`$ while $`q\leq q_0`$, the law becomes $`\Theta(k^2/(qd^2))`$. The transition is therefore at $`q\asymp k/d`$, not at a dimension-independent noise level.

In particular, the optimum over separable inputs is $`\Theta(1/d)`$ without output noise and $`\Theta_q(1/d^2)`$ at fixed positive output noise. Suitable inputs with Schmidt number proportional to $`d`$ attain constant negativity in both regimes. The theorem concerns witness strength under an explicit preparation budget. It does not convert these ratios into universal sample savings or an optimized metrological advantage.
