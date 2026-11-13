# Reproduce the finite checks

Run from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/validate.py --write-results verification/results.json
```

The command exits unsuccessfully if a check fails. It uses NumPy and the Python standard library, with a fixed random seed and an absolute tolerance of `2e-11`. The saved [results](results.json) include the script's SHA-256 digest, environment versions, tested parameter sets, and observed errors. They were generated with Python 3.12.14 and NumPy 2.3.5. The workflow additionally specifies NumPy 1.26.4 on Python 3.11; a workflow configuration alone is not evidence that its remote run passed.

These are finite floating-point checks of the calculations and operational conventions. The proofs are in [`science/`](../science/). The numerical report does not establish an unrestricted optimum, a mixed-state entanglement-of-formation value, or an experimental sampling advantage.

## What is checked

| Check | Cases | Purpose |
| --- | ---: | --- |
| General complex amplitudes versus full effect multiplication and partial trace | 192 | Detect transpose, conjugation, normalization, and trace-norm convention errors. |
| Independent Pauli sequential reconstruction | 16 | Reconstruct the PDM from coarse-grained Born probabilities at dimensions 2 and 4. |
| Schmidt-number bounds and mixtures | 255 | Test pure states and known three-state decompositions of Schmidt number at most `k`, including classical correlations. |
| Constructions, odd-rank embeddings, and readout-noise crossover | 198 | Check the exact construction formula, the product case, the odd-rank embedding, and the uniform scaling constants. |
| Bell-fidelity and formation-entropy bounds | 157 | Compare negativity bounds to computed pure-state entropies; include diagonal constructions through dimension 65,536. |
| Two-setting witness identity | 12 | Recover the negative expectation from two ordinary experimental contexts, without retaining a selected subensemble. |
| Nonsignalling control with initial entanglement | 18 | Verify zero negativity for effects acting only on `A`, despite spatially entangled inputs. |
| Nonoptimal-family guard | 1 | Exhibit a state outperforming the convenient balanced construction at `d=4, q=0`. |
| **Total** | **849** | |

The first calculation uses full operators on `AB`; the amplitude calculation uses only `d × d` matrices. The Pauli reconstruction follows a third route: it forms the coarse-grained projectors, computes the sequential probabilities, and performs Pauli tomography. Agreement checks the operational definition rather than only comparing two versions of the same eigenvalue formula.

The Schmidt-number tests use known decompositions. They do not solve the Schmidt-number decision problem for arbitrary mixed states. The entropy tests evaluate pure-state entanglement from reduced spectra; they do not numerically compute a mixed-state convex roof.

## Observed accuracy

All 849 cases passed. The largest full-effect/amplitude entry difference was below `2.3e-16`; the independent Pauli reconstruction differed by less than `5.8e-17`. The exact even-rank construction formula agreed within `8.4e-17`. The largest pure-state entropy lower-bound discrepancy was below `1.3e-15`, attributable to floating-point rounding. Full metrics are in [results.json](results.json).

The tests include noiseless readout, `q=10⁻⁶`, fixed nonzero readout noise, and the completely random bit limit. The uniform crossover checks use `q ≤ 0.4`. Testing these values does not prove a continuous-parameter statement; the analytical bounds supply that statement.

## Two contexts, no postselection

The full-rank construction uses `U² = I` and the positive witness defined below. Its expectation can be evaluated as

```math
W=(I-U)/2\otimes|1\rangle\langle1|,
\qquad
\operatorname{Tr}(W R)=\frac12\left[p_1^{\mathrm{no\ measurement}}-\mathbb{E}_{\mathrm{measured}}(u\,\mathbf{1}_{C=1})\right].
```

One context reads the output bit with no earlier measurement. The other measures the coarse-grained `U` observable on `B` and then reads the output bit. Each context contributes all its trials. The negative quantity is a difference of context-dependent statistics; no physical joint probability becomes negative.

## Construction versus optimum

At `d=4, q=0`, the normalized amplitude matrix `diag(1,1,1,-1)/2` gives negativity `1/4`. The balanced construction gives approximately `0.2071`, below `1/4`. The explicit guard prevents the scaling-matching family from being described as an exact global optimizer.
