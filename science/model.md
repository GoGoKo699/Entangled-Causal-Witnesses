# Model and exact conventions

[Science overview](README.md) · [Schmidt-number law](schmidt_law.md) · [Entanglement cost](entanglement_cost.md) · [Related work](../references/RELATED_WORK.md)

The task is to maximize the negativity of one reduced two-time pseudo-density matrix (PDM), while limiting the entanglement in its initial spatial preparation. Both initial subsystems enter a fixed joint channel. There is no untouched reference system and no conditioning on a successful channel outcome.

## 1. A joint measurement with one noisy output bit

Let $`A`$ and $`B`$ have the same integer dimension $`d\geq2`$, with fixed identified orthonormal bases. Define

```math
|\Phi_d\rangle=\frac1{\sqrt d}\sum_{i=1}^{d}|i\rangle_A|i\rangle_B,
\qquad E_d=|\Phi_d\rangle\langle\Phi_d|.
```

The apparatus measures the two effects $`E_d`$ and $`I-E_d`$. It reports their binary outcome after a binary symmetric channel with error probability $`0\leq q\lt 1/2`$. Write $`s=1-2q`$. The complete channel, whose sole output is a classical bit $`C`$, is

```math
\Gamma_{d,q}(X)
=\operatorname{Tr}(F_0X)|0\rangle\langle0|
 +\operatorname{Tr}(F_1X)|1\rangle\langle1|,
```

```math
F_1=qI+sE_d,
\qquad F_0=(1-q)I-sE_d=I-F_1.
```

Both effects are positive, and they sum to the identity. Thus $`\Gamma_{d,q}`$ is a completely positive trace-preserving measurement channel. It is entanglement breaking as a channel from the entire input $`AB`$ to $`C`$. The measurement effect itself is a joint operation on $`A`$ and $`B`$; it is not a free local measurement.

The initial state $`\rho_{AB}`$ may be mixed and correlated. The initial subsystem $`B`$ and the later output $`C`$ are the two events retained in the PDM. The initial $`A`$ event and all discarded physical outputs are omitted. A fixed discarded output can be appended if a bipartite-output channel is desired; it changes none of the formulas.

## 2. The operational PDM

At the initial event, choose any Hermitian involution $`X`$ on $`B`$, so $`X^2=I`$. Its coarse projective measurement has projectors $`P_\pm=(I\pm X)/2`$ and signed outcomes $`\pm1`$. At the later event measure an observable $`Y`$ on $`C`$. The sequential correlator is

```math
\langle X,Y\rangle_{\rm seq}
=\operatorname{Tr}\!\left[
Y\,\Gamma_{d,q}\!\left(
\frac{(I_A\otimes X)\rho+\rho(I_A\otimes X)}2
\right)\right].
```

Indeed, the difference of the two unnormalized postmeasurement states is the anticommutator in this expression. Setting $`X=I`$ means making no initial measurement. The reduced PDM $`R_{BC}(\rho)`$ is the unique operator satisfying

```math
\operatorname{Tr}[R_{BC}(\rho)(X\otimes Y)]
=\langle X,Y\rangle_{\rm seq}.
```

This is the coarse-measurement PDM convention of Liu, Qiu, Dahlsten and Vedral; see [the source comparison](../references/RELATED_WORK.md). It works for every integer dimension here: the involutions $`2|v\rangle\langle v|-I`$ and the identity span the Hermitian operators, so the correlators determine a unique operator. For qubit registers one can use the Pauli basis.

For the present classical-output channel, a direct calculation gives the particularly useful form

```math
R_{BC}(\rho)=H_0(\rho)\otimes|0\rangle\langle0|
             +H_1(\rho)\otimes|1\rangle\langle1|,
```

```math
H_j(\rho)=\frac12\operatorname{Tr}_A(F_j\rho+\rho F_j).
```

To verify it, cyclically move $`I_A\otimes X`$ in the sequential-correlator trace and then take the partial trace over $`A`$. The coefficient of $`Y_{jj}`$ becomes exactly $`\operatorname{Tr}(XH_j)`$. Off-diagonal output observables have zero expectation for this channel.

The PDM is Hermitian with trace one. Its marginals are

```math
H_0+H_1=\rho_B,
\qquad
\operatorname{Tr}_B R_{BC}=\Gamma_{d,q}(\rho).
```

It need not be positive. The convention used throughout this repository is

```math
f(R)=\|R\|_1-1=2\operatorname{Tr}R_-,
\qquad
R_-=\frac{|R|-R}{2}.
```

Thus $`f`$ is twice the ordinary negative spectral weight. It is not the logarithmic negativity. Because the output blocks are orthogonal,

```math
f(R_{BC})=\|H_0\|_1+\|H_1\|_1-1
         =2\operatorname{Tr}(H_0)_-+2\operatorname{Tr}(H_1)_-.
```

Linearity of $`\rho\mapsto R_{BC}(\rho)`$ and convexity of the trace norm make $`f(R_{BC}(\rho))`$ convex in the initial state.

## 3. What negativity certifies

For this experiment, $`f>0`$ rules out a channel that cannot signal from $`B`$ to $`C`$. Initial spatial correlations do not invalidate that conclusion. This is a special case of the inherited semicausal null-negativity theorem, and can also be proved directly here.

For a general quantum-to-classical channel, absence of signalling from $`B`$ means that each output probability depends only on $`\rho_A`$. Equivalently its effects have the form $`F_j=G_j\otimes I_B`$, for a POVM $`\{G_j\}`$ on $`A`$. The corresponding block is

```math
H_j
=\operatorname{Tr}_A[(G_j\otimes I_B)\rho]
=\operatorname{Tr}_A[(\sqrt{G_j}\otimes I_B)\rho
                     (\sqrt{G_j}\otimes I_B)]\succeq0.
```

The first equality uses cyclicity on the traced subsystem. Therefore every block, and hence the PDM, is positive for every initially correlated state.

The fixed channel $`\Gamma_{d,q}`$ actually is signalling for $`q\lt 1/2`$. Fix a pure state $`|a\rangle`$ on $`A`$. Its effective effect on $`B`$ is $`qI+(s/d)|a^*\rangle\langle a^*|`$. Choosing $`B`$ aligned or orthogonal to $`|a^*\rangle`$ changes the output-one probability by $`s/d>0`$.

Negativity is therefore a valid temporal causal witness here. Its magnitude is a property of the specified PDM experiment. It is not automatically a communication capacity, a channel-discrimination probability, or a sample-complexity advantage.

## 4. The preparation constraint

A pure state has Schmidt rank at most $`k`$ when its coefficient matrix has rank at most $`k`$. A mixed state has Schmidt number at most $`k`$ when it admits a convex decomposition into such pure states. The optimized figure is

```math
\mathcal F_k(d,q)
=\max_{\rho_{AB}:\,\operatorname{SN}(\rho_{AB})\leq k}
   f(R_{BC}(\rho_{AB})),
\qquad 1\leq k\leq d.
```

The feasible set is the convex hull of a compact pure-state set; it is compact in finite dimension, so the maximum exists. Convexity of $`f`$ implies that this maximum is already attained by a pure state of Schmidt rank at most $`k`$. Nevertheless, the converse covers the entire mixed feasible set, including arbitrary classical shared randomness. In particular $`k=1`$ is the optimization over all separable preparations, not only over uncorrelated ones.

Schmidt number is an entanglement-dimension constraint. It does not by itself measure ebits: a full-rank pure state can have arbitrarily small entropy. [The separate formation-entanglement theorem](entanglement_cost.md) closes that distinction for constant negativity at fixed positive noise.

## 5. Resources and scope

The variable resource is the initial spatial preparation. The apparatus, local dimensions, output noise, and PDM convention are fixed on both sides of every comparison. The initial state is consumed. Both $`A`$ and $`B`$ enter the joint apparatus; neither is an untouched external ancilla. All output bits are retained, including both reported outcomes. Local computation and classical aggregation of outcomes are not optimized by the theorem.

The mathematical model assumes ideal input states, ideal choices of the initial coarse projective measurements, and an exact Bell effect, followed by the explicitly charged output-bit noise $`q`$. It does not establish robustness to arbitrary input noise or faulty gates. For $`d=2^n`$, the specified apparatus and attaining preparations admit circuits with a number of elementary operations polynomial in $`n`$; the [witness and implementation account](witness.md) gives that construction and the measurement contexts.

The main result is for this explicit channel family. It does not assert an optimal Schmidt-number law for all signalling channels, or infer a universal statistical cost from a small value of $`f`$.
