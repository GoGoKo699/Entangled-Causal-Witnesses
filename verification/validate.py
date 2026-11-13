#!/usr/bin/env python3
"""Finite numerical checks for the Bell-effect causal-witness model.

These deterministic floating-point checks are not proofs or an exhaustive search.
Only NumPy and the Python standard library are required.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys

import numpy as np


ATOL = 2e-11
RNG_SEED = 20261113


def pure_from_amplitude(v: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Rows of V label B, columns label A; AB uses A-major ordering."""
    v = np.asarray(v, dtype=complex)
    v = v / np.linalg.norm(v)
    psi = v.T.reshape(-1)
    return v, np.outer(psi, psi.conj())


def bell_projector(d: int) -> np.ndarray:
    phi = np.eye(d, dtype=complex).reshape(-1) / math.sqrt(d)
    return np.outer(phi, phi.conj())


def partial_trace_a(x: np.ndarray, d: int) -> np.ndarray:
    return np.einsum("abad->bd", x.reshape(d, d, d, d))


def direct_blocks(rho: np.ndarray, d: int, q: float) -> tuple[np.ndarray, np.ndarray]:
    """Definition via full AB effect multiplication and partial trace."""
    e = bell_projector(d)
    f1 = q * np.eye(d * d) + (1.0 - 2.0 * q) * e
    f0 = np.eye(d * d) - f1
    return tuple(partial_trace_a((fj @ rho + rho @ fj) / 2.0, d)
                 for fj in (f0, f1))


def amplitude_blocks(v: np.ndarray, q: float) -> tuple[np.ndarray, np.ndarray]:
    """Independent reduced formula, avoiding full AB matrices."""
    d = v.shape[0]
    rho_b = v @ v.conj().T
    y = np.trace(v).conjugate() * v / d
    cross = (1.0 - 2.0 * q) * (y + y.conj().T) / 2.0
    return (1.0 - q) * rho_b - cross, q * rho_b + cross


def negativity(blocks: tuple[np.ndarray, np.ndarray]) -> float:
    return float(sum(2.0 * np.maximum(-np.linalg.eigvalsh(b), 0.0).sum()
                     for b in blocks))


def pdm_matrix(blocks: tuple[np.ndarray, np.ndarray]) -> np.ndarray:
    return np.kron(blocks[0], np.diag([1.0, 0.0])) + np.kron(blocks[1], np.diag([0.0, 1.0]))


def rank_k_amplitude(rng: np.random.Generator, d: int, k: int) -> np.ndarray:
    x = rng.normal(size=(d, k)) + 1j * rng.normal(size=(d, k))
    y = rng.normal(size=(k, d)) + 1j * rng.normal(size=(k, d))
    v = x @ y
    return v / np.linalg.norm(v)


def schmidt_upper(d: int, k: int, q: float) -> float:
    s = 1.0 - 2.0 * q
    linear = 2.0 * s * k / d
    if q == 0.0:
        return linear
    return min(linear, s * s * k * k / (2.0 * q * (1.0 - q) * d * d))


def lower_formula(t: float, q: float) -> float:
    """Cancellation-safe expression for the displayed construction."""
    b = (1.0 - 2.0 * q) * t
    a = 2.0 * q + b
    if b == 0.0:
        return 0.0
    return b * b / (2.0 * (math.hypot(a, b) + a))


def constructed_amplitude(d: int, k: int, q: float) -> tuple[np.ndarray, int]:
    """Even-rank family; odd ranks embed k-1; k=1 uses a product."""
    v = np.zeros((d, d), dtype=complex)
    if k == 1:
        v[0, 0] = 1.0 / math.sqrt(2.0)
        v[0, 1] = 1.0 / math.sqrt(2.0)
        return v, 1
    m = 2 * (k // 2)
    t = m / d
    b = (1.0 - 2.0 * q) * t
    a = 2.0 * q + b
    p = (1.0 - b / math.hypot(a, b)) / 2.0
    signs = np.r_[np.ones(m // 2), -np.ones(m // 2)]
    v[np.arange(m), np.arange(m)] = (math.sqrt(p) + math.sqrt(1.0 - p) * signs) / math.sqrt(m)
    return v, m


def paulis(n: int) -> list[np.ndarray]:
    single = [np.eye(2), np.array([[0, 1], [1, 0]]),
              np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
    out = []
    for choices in itertools.product(range(4), repeat=n):
        p = np.ones((1, 1), dtype=complex)
        for i in choices:
            p = np.kron(p, single[i])
        out.append(p)
    return out


def sequential_pauli_reconstruction(rho: np.ndarray, d: int, q: float) -> tuple[np.ndarray, float]:
    """Actual coarse-grained projectors, Born probabilities, then tomography.

    This route does not use the reduced anticommutator/amplitude formula.
    """
    e = bell_projector(d)
    f1 = q * np.eye(d * d) + (1.0 - 2.0 * q) * e
    effects = (np.eye(d * d) - f1, f1)
    z = np.diag([1.0, -1.0])
    reconstructed = np.zeros((2 * d, 2 * d), dtype=complex)
    min_probability = 1.0
    for p in paulis(int(round(math.log2(d)))):
        corr_i = 0.0
        corr_z = 0.0
        for outcome in (1.0, -1.0):
            proj_b = (np.eye(d) + outcome * p) / 2.0
            proj_ab = np.kron(np.eye(d), proj_b)
            post = proj_ab @ rho @ proj_ab
            probs = [float(np.trace(fj @ post).real) for fj in effects]
            min_probability = min(min_probability, *probs)
            corr_i += outcome * sum(probs)
            corr_z += outcome * (probs[0] - probs[1])
        reconstructed += (corr_i * np.kron(p, np.eye(2)) + corr_z * np.kron(p, z)) / (2.0 * d)
    return reconstructed, min_probability


def binary_entropy(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def entropy_of_reduced(v: np.ndarray) -> float:
    eigs = np.linalg.eigvalsh(v @ v.conj().T)
    eigs = eigs[eigs > 1e-15]
    return float(-(eigs * np.log2(eigs)).sum())


def full_pdm_bound(fidelity: float, q: float) -> float:
    s = 1.0 - 2.0 * q
    return math.sqrt(max(0.0, q * q + s * fidelity)) + math.sqrt(max(0.0, (1.0 - q) ** 2 - s * fidelity)) - 1.0


class Checks:
    def __init__(self) -> None:
        self.groups: list[dict] = []
        self.failures: list[str] = []

    def require(self, value: bool, message: str) -> None:
        if not value:
            self.failures.append(message)

    def add(self, name: str, cases: int, **metrics: object) -> None:
        self.groups.append({"name": name, "cases": cases, **metrics})


def run_checks() -> dict:
    c = Checks()
    rng = np.random.default_rng(RNG_SEED)

    # Nonreal, nonsymmetric amplitudes test transpose/conjugation conventions.
    count = 0
    max_block_error = max_trace_error = max_hermiticity_error = max_norm_identity_error = 0.0
    for d in (2, 3, 4, 6):
        for q in (0.0, 0.0001, 0.05, 0.2, 0.4, 0.5):
            for k in (1, d):
                for _ in range(4):
                    v = rank_k_amplitude(rng, d, k)
                    v, rho = pure_from_amplitude(v)
                    direct = direct_blocks(rho, d, q)
                    reduced = amplitude_blocks(v, q)
                    err = max(float(np.max(np.abs(a - b))) for a, b in zip(direct, reduced))
                    max_block_error = max(max_block_error, err)
                    max_trace_error = max(max_trace_error, abs(sum(np.trace(b) for b in direct) - 1.0))
                    max_hermiticity_error = max(max_hermiticity_error, *(float(np.max(np.abs(b - b.conj().T))) for b in direct))
                    r = pdm_matrix(direct)
                    norm_identity_error = abs(float(np.abs(np.linalg.eigvalsh(r)).sum()) - 1.0 - negativity(direct))
                    max_norm_identity_error = max(max_norm_identity_error, norm_identity_error)
                    c.require(err <= ATOL, f"amplitude/direct mismatch d={d}, k={k}, q={q}: {err}")
                    count += 1
    c.require(max_trace_error <= ATOL and max_hermiticity_error <= ATOL and max_norm_identity_error <= ATOL,
              "Hermiticity, trace-one, or negativity identity failed")
    c.add("complex_amplitude_vs_full_effect_partial_trace", count,
          dimensions=[2, 3, 4, 6], max_entry_error=max_block_error,
          max_trace_error=float(max_trace_error), max_hermiticity_error=max_hermiticity_error,
          max_trace_norm_identity_error=max_norm_identity_error)

    count = 0
    max_pauli_error = 0.0
    min_probability = 1.0
    for d in (2, 4):
        for q in (0.0, 0.05, 0.2, 0.4):
            for mixed in (False, True):
                _, rho = pure_from_amplitude(rank_k_amplitude(rng, d, d))
                if mixed:
                    _, second = pure_from_amplitude(rank_k_amplitude(rng, d, 1))
                    rho = 0.37 * rho + 0.63 * second
                reconstructed, min_p = sequential_pauli_reconstruction(rho, d, q)
                expected = pdm_matrix(direct_blocks(rho, d, q))
                error = float(np.max(np.abs(reconstructed - expected)))
                max_pauli_error = max(max_pauli_error, error)
                min_probability = min(min_probability, min_p)
                c.require(error <= ATOL and min_p >= -ATOL, f"Pauli sequential reconstruction failed d={d},q={q},mixed={mixed}")
                count += 1
    c.add("independent_pauli_sequential_reconstruction", count,
          dimensions=[2, 4], max_entry_error=max_pauli_error,
          minimum_born_probability=min_probability,
          measurement="Coarse-grained +/-1 Pauli-string projectors on B, then classical output bit")

    count = 0
    max_upper_violation = max_convexity_violation = 0.0
    for d in (2, 3, 4, 8):
        for k in range(1, d + 1):
            for q in (0.0, 0.0001, 0.05, 0.2, 0.4):
                for _ in range(3):
                    states = [pure_from_amplitude(rank_k_amplitude(rng, d, j))
                              for j in (1, max(1, k - 1), k)]
                    weights = np.array([0.19, 0.34, 0.47])
                    rho = sum(w * pair[1] for w, pair in zip(weights, states))
                    value = negativity(direct_blocks(rho, d, q))
                    pure_values = [negativity(amplitude_blocks(pair[0], q)) for pair in states]
                    bound = schmidt_upper(d, k, q)
                    max_upper_violation = max(max_upper_violation, value - bound, *[f - bound for f in pure_values])
                    max_convexity_violation = max(max_convexity_violation, value - float(weights @ pure_values))
                    c.require(value <= bound + ATOL and all(f <= bound + ATOL for f in pure_values),
                              f"Schmidt upper failed d={d},k={k},q={q}")
                    c.require(value <= weights @ pure_values + ATOL, "Convexity failed on known Schmidt-number ensemble")
                    count += 1
    c.add("schmidt_number_and_mixture_bounds", count,
          dimensions=[2, 3, 4, 8], each_k=True, mixture_size=3,
          max_upper_bound_violation=max_upper_violation,
          max_convexity_violation=max_convexity_violation,
          scope="Known decompositions of Schmidt rank <=k; not an algorithm for deciding Schmidt number")

    count = 0
    max_attainer_error = max_lower_violation = 0.0
    min_scaled_value = float("inf")
    max_scaled_value = 0.0
    qmax = 0.4
    lower_constant = (1.0 - 2.0 * qmax) ** 2 / (16.0 * (1.0 + math.sqrt(2.0)))
    examples = []
    for d in (2, 3, 4, 8, 16):
        for k in range(1, d + 1):
            for q in (0.0, 1e-6, 0.001, 0.05, 0.2, 0.4):
                v, m = constructed_amplitude(d, k, q)
                value = negativity(amplitude_blocks(v, q))
                lower = lower_formula(m / d, q)
                if k >= 2:
                    max_attainer_error = max(max_attainer_error, abs(value - lower))
                    c.require(abs(value - lower) <= ATOL, f"even embedding formula failed d={d},k={k},q={q}")
                max_lower_violation = max(max_lower_violation, lower - value)
                c.require(value + ATOL >= lower, "Product/odd-rank lower embedding failed")
                t = k / d
                scale = t * t / (q + t)
                ratio = value / scale
                min_scaled_value = min(min_scaled_value, ratio)
                max_scaled_value = max(max_scaled_value, ratio)
                c.require(lower + ATOL >= lower_constant * scale, "Uniform lower scaling constant failed")
                c.require(schmidt_upper(d, k, q) <= 4.0 * scale + ATOL, "Uniform upper scaling constant failed")
                count += 1
    for d in (4, 16, 64, 256):
        for q in (0.0, 0.001, 0.2):
            examples.append({"d": d, "k": 1, "q": q,
                             "analytic_construction_lower": lower_formula(1.0 / d, q)})
    c.add("attainers_odd_embeddings_and_noise_crossover", count,
          dimensions=[2, 3, 4, 8, 16], each_k=True,
          q_values=[0.0, 1e-6, 0.001, 0.05, 0.2, 0.4],
          max_even_embedding_formula_error=max_attainer_error,
          max_lower_bound_violation=max_lower_violation,
          uniform_qmax=qmax, uniform_lower_constant=lower_constant,
          observed_construction_over_t_squared_div_q_plus_t=[min_scaled_value, max_scaled_value],
          crossover_examples=examples,
          warning="Scaling-matching constructions are not claimed to be exact global maximizers")

    count = 0
    max_fidelity_bound_violation = max_linear_fidelity_violation = max_entropy_violation = 0.0
    for d in (2, 3, 4, 8):
        for q in (0.05, 0.2, 0.4):
            for k in range(1, d + 1):
                for _ in range(3):
                    v, rho = pure_from_amplitude(rank_k_amplitude(rng, d, k))
                    value = negativity(amplitude_blocks(v, q))
                    fidelity = float(np.trace(bell_projector(d) @ rho).real)
                    g = full_pdm_bound(fidelity, q)
                    cq = (1.0 - 2.0 * q) ** 2 / (2.0 * q * (1.0 - q))
                    entropy = entropy_of_reduced(v)
                    ef_lower = max(0.0, value * math.log2(d) / cq - 1.0)
                    fidelity_entropy_lower = fidelity * math.log2(d) - binary_entropy(fidelity)
                    max_fidelity_bound_violation = max(max_fidelity_bound_violation, value - g)
                    max_linear_fidelity_violation = max(max_linear_fidelity_violation, value - cq * fidelity)
                    max_entropy_violation = max(max_entropy_violation, ef_lower - entropy, fidelity_entropy_lower - entropy)
                    c.require(value <= g + ATOL and value <= cq * fidelity + ATOL, "Bell-fidelity negativity bound failed")
                    c.require(entropy + ATOL >= ef_lower and entropy + ATOL >= fidelity_entropy_lower,
                              "Pure-state entropy lower bound failed")
                    count += 1
    entropy_examples = []
    for d in (16, 256, 4096, 65536):
        q = 0.4
        s = 1.0 - 2.0 * q
        p = (1.0 - s / math.sqrt(1.0 + s * s)) / 2.0
        r = math.sqrt(p * (1.0 - p))
        probs = np.r_[np.full(d // 2, (1.0 + 2.0 * r) / d),
                      np.full(d // 2, (1.0 - 2.0 * r) / d)]
        entropy = float(-(probs * np.log2(probs)).sum())
        value = lower_formula(1.0, q)
        cq = s * s / (2.0 * q * (1.0 - q))
        lower = max(0.0, value * math.log2(d) / cq - 1.0)
        c.require(entropy + ATOL >= lower, "Large-d pure construction entropy failed")
        entropy_examples.append({"d": d, "q": q, "construction_negativity": value,
                                 "pure_state_entanglement_bits": entropy,
                                 "formation_entanglement_lower_bits": lower})
    c.add("fidelity_and_formation_entropy_bounds", count + len(entropy_examples),
          dimensions_for_matrix_checks=[2, 3, 4, 8],
          max_fidelity_bound_violation=max_fidelity_bound_violation,
          max_linear_fidelity_violation=max_linear_fidelity_violation,
          max_pure_entropy_lower_bound_violation=max_entropy_violation,
          large_dimension_diagonal_examples=entropy_examples,
          scope="Pure-state entanglement computed from reduced spectra. These checks do not compute the mixed-state entanglement-of-formation convex roof.")

    count = 0
    max_two_setting_error = max_negative_mass_error = 0.0
    min_joint_probability = 1.0
    for d in (2, 4, 8):
        u = np.diag(np.r_[np.ones(d // 2), -np.ones(d // 2)])
        ua = np.kron(np.eye(d), u)
        for q in (0.0, 0.05, 0.2, 0.4):
            v, _ = constructed_amplitude(d, d, q)
            _, rho = pure_from_amplitude(v)
            f1 = q * np.eye(d * d) + (1.0 - 2.0 * q) * bell_projector(d)
            no_measurement = float(np.trace(f1 @ rho).real)
            measured_correlation = 0.0
            for sign in (1.0, -1.0):
                proj = (np.eye(d * d) + sign * ua) / 2.0
                joint_probability = float(np.trace(f1 @ proj @ rho @ proj).real)
                min_joint_probability = min(min_joint_probability, joint_probability)
                measured_correlation += sign * joint_probability
            lhs = float(np.trace((np.eye(d) - u) / 2.0 @ amplitude_blocks(v, q)[1]).real)
            rhs = (no_measurement - measured_correlation) / 2.0
            fvalue = negativity(amplitude_blocks(v, q))
            max_two_setting_error = max(max_two_setting_error, abs(lhs - rhs))
            max_negative_mass_error = max(max_negative_mass_error, abs(lhs + fvalue / 2.0))
            c.require(abs(lhs - rhs) <= ATOL and abs(lhs + fvalue / 2.0) <= ATOL,
                      "Two-setting witness identity failed")
            c.require(min_joint_probability >= -ATOL, "Negative physical Born probability")
            count += 1
    c.add("two_setting_unconditioned_witness_identity", count,
          dimensions=[2, 4, 8], q_values=[0.0, 0.05, 0.2, 0.4],
          max_two_setting_identity_error=max_two_setting_error,
          max_negative_mass_identity_error=max_negative_mass_error,
          minimum_joint_born_probability=min_joint_probability,
          settings=["Output bit without an earlier measurement", "Coarse-grained U measurement on B followed by output bit"],
          conditioning="None: every trial in each setting contributes")

    # A local-A measurement has no B->C signalling, even with entangled inputs.
    count = 0
    max_control_negativity = 0.0
    for d in (2, 4, 8):
        for _ in range(6):
            _, rho = pure_from_amplitude(rank_k_amplitude(rng, d, d))
            a = rng.normal(size=d) + 1j * rng.normal(size=d)
            a /= np.linalg.norm(a)
            ga = 0.13 * np.eye(d) + 0.71 * np.outer(a, a.conj())
            f1 = np.kron(ga, np.eye(d))
            effects = (np.eye(d * d) - f1, f1)
            blocks = tuple(partial_trace_a((fj @ rho + rho @ fj) / 2.0, d) for fj in effects)
            value = negativity(blocks)
            max_control_negativity = max(max_control_negativity, value)
            c.require(value <= ATOL, "Initial-entanglement nonsignalling control failed")
            count += 1
    c.add("nonsignalling_control_with_initial_entanglement", count,
          dimensions=[2, 4, 8], maximum_negativity=max_control_negativity,
          effect="F1=G_A tensor I_B; no B-to-output signalling")

    # Explicit guard against mistaking the convenient balanced family for a global optimizer.
    d, q = 4, 0.0
    alternative = np.diag([1.0, 1.0, 1.0, -1.0]) / 2.0
    alternative_value = negativity(amplitude_blocks(alternative, q))
    balanced_value = lower_formula(1.0, q)
    c.require(abs(alternative_value - 0.25) <= ATOL and alternative_value > balanced_value,
              "Nonoptimal-family guard failed")
    c.add("construction_is_not_global_optimizer_guard", 1,
          d=d, q=q, alternative_negativity=alternative_value,
          balanced_construction_negativity=balanced_value,
          claim="The analytic family matches scaling; exact global optimization is not established")

    return {
        "schema_version": 1,
        "passed": not c.failures,
        "rng_seed": RNG_SEED,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "absolute_tolerance": ATOL,
        "numpy_version": np.__version__,
        "python_version": sys.version.split()[0],
        "total_cases": sum(g["cases"] for g in c.groups),
        "groups": c.groups,
        "failures": c.failures,
        "limits": [
            "Deterministic finite floating-point checks, not formal proofs or exhaustive validation.",
            "Schmidt-number bounds are tested on states with known decompositions; Schmidt number is not numerically certified for arbitrary states.",
            "The construction is scaling-matching, not an exact global optimizer.",
            "No experimental sample-complexity separation follows from these numerical checks.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-results", type=Path,
                        help="Write a complete JSON report to this path after checking")
    args = parser.parse_args()
    result = run_checks()
    if args.write_results:
        args.write_results.parent.mkdir(parents=True, exist_ok=True)
        args.write_results.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": result["passed"], "total_cases": result["total_cases"],
                      "groups": len(result["groups"]), "failures": result["failures"]}, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
