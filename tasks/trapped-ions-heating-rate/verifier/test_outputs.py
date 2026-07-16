from __future__ import annotations

import functools
import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path

import h5py
import numpy as np
from scipy.optimize import least_squares

ROOT = Path("/root")
DATA_DIR = ROOT / "data"
LOGS = Path("/logs/verifier")

RELATIVE_TOLERANCE = 0.35
ABSOLUTE_QUANTA_TOLERANCE = 2.0
ABSOLUTE_RATE_TOLERANCE = 3000.0

EXPECTED_HASHES = {
    "delay_0us.h5": "84b3d5d35855c52c1c740b04d254994d254843f5be5efb25b68e377c4c087c15",
    "delay_300us.h5": "0e58f2c410ee24de13e81a8992986900ea4c7ad4abab40ab9ad5f4d267ba3e71",
    "delay_500us.h5": "0bf154dd82dafc2b5f70e17033b4efcc420e932d7abf1843364bac8583e6ffe4",
    "delay_1000us.h5": "bcb07719b5d9865919b3e3a1e1d08f12712555334c6f321031a1ca4acdbe0a60",
}

INTENSITY = np.asarray(
    [0.96912696, 0.9844114, 0.99344862, 0.99840835, 1.0, 0.99840835, 0.99344862, 0.9844114, 0.96912696],
    dtype=float,
)
N = np.arange(500, dtype=float)
HBAR = 6.62607004e-34 / (2.0 * np.pi)
OMEGA = 2.0 * np.pi * 0.177e6
ETA = 2.0 * np.pi * np.sqrt(HBAR / (2.0 * OMEGA * 6.6551079e-26)) / 729e-9 / np.sqrt(9.0)
FREQUENCY_FACTOR = 1.0 - ETA**2 * (N + 0.5) + ETA**4 * (1.0 + 2.0 * N * (1.0 + N)) / 8.0


@dataclass(frozen=True)
class ReferenceCase:
    delay_us: float
    filename: str
    drop_tail: int
    start: tuple[float, float, float, float]


REFERENCE_CASES = (
    ReferenceCase(0.0, "delay_0us.h5", 10, (1.0, 0.04, 0.1, 20.0)),
    ReferenceCase(300.0, "delay_300us.h5", 10, (1.0, 0.03, 0.1, 20.0)),
    ReferenceCase(500.0, "delay_500us.h5", 10, (1.0, 0.03, 0.1, 20.0)),
    ReferenceCase(1000.0, "delay_1000us.h5", 9, (1.0, 0.01, 0.1, 0.0)),
)

NUMBER_LINE = re.compile(r"^\s*[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?\s*$")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_result() -> np.ndarray:
    path = ROOT / "result.md"
    assert path.is_file(), "Missing /root/result.md"
    lines = [line for line in path.read_text().splitlines() if line.strip()]
    assert len(lines) == 5, f"/root/result.md must contain exactly five non-empty lines; found {len(lines)}"
    assert all(NUMBER_LINE.fullmatch(line) for line in lines), "Every result.md line must contain one raw number and no label"
    values = np.asarray([float(line) for line in lines], dtype=float)
    assert np.isfinite(values).all(), "result.md contains a non-finite value"
    return values


def carrier_probability(time_us: np.ndarray, rabi_mhz: float, mean_quanta: float) -> np.ndarray:
    thermal_weights = np.power(mean_quanta / (mean_quanta + 1.0), N) / (mean_quanta + 1.0)
    phase = 2.0 * np.pi * (rabi_mhz * FREQUENCY_FACTOR)[:, None] * time_us[None, :]
    return 0.5 - 0.5 * np.einsum("n,nt->t", thermal_weights, np.cos(phase))


def ensemble_prediction(parameters: np.ndarray, time_us: np.ndarray) -> np.ndarray:
    amplitude, base_rabi_mhz, offset, mean_quanta = parameters
    per_ion = [amplitude * carrier_probability(time_us, base_rabi_mhz * scale, mean_quanta) + offset for scale in INTENSITY]
    return np.asarray(per_ion).mean(axis=0)


def load_normalized_trace(case: ReferenceCase) -> tuple[np.ndarray, np.ndarray]:
    path = DATA_DIR / case.filename
    assert file_sha256(path) == EXPECTED_HASHES[case.filename], f"Frozen input was modified: {case.filename}"
    with h5py.File(path, "r") as handle:
        time_us = np.asarray(handle["datasets/rabi_t"][:], dtype=float)
        counts = np.asarray(handle["datasets/pmt_counts_avg_thresholded"][:], dtype=float)
    assert time_us.shape == (50,) and counts.shape == (50,), f"Unexpected trace shape in {case.filename}"
    time_us = time_us[: -case.drop_tail]
    counts = counts[: -case.drop_tail]
    excitation = counts.max() - counts
    excitation /= excitation.max()
    return time_us, excitation


@functools.lru_cache(maxsize=1)
def independent_reference() -> dict[str, object]:
    fits: list[dict[str, object]] = []
    mean_quanta: list[float] = []
    for case in REFERENCE_CASES:
        time_us, excitation = load_normalized_trace(case)
        solution = least_squares(
            lambda parameters, fit_time=time_us, observed=excitation: ensemble_prediction(parameters, fit_time) - observed,
            x0=np.asarray(case.start, dtype=float),
            bounds=([0.0, 0.0, -0.5, 0.0], [2.0, 0.1, 0.5, 500.0]),
            x_scale="jac",
            ftol=1e-12,
            xtol=1e-12,
            gtol=1e-12,
            max_nfev=10_000,
        )
        assert solution.success, f"Independent fit failed for {case.filename}: {solution.message}"
        parameters = solution.x
        dof = max(1, excitation.size - parameters.size)
        normal_matrix = solution.jac.T @ solution.jac
        covariance = np.linalg.pinv(normal_matrix) * (2.0 * solution.cost / dof)
        errors = np.sqrt(np.diag(covariance))
        mean_quanta.append(float(parameters[3]))
        fits.append(
            {
                "delay_us": case.delay_us,
                "filename": case.filename,
                "parameters": parameters.tolist(),
                "standard_errors": errors.tolist(),
                "cost": float(solution.cost),
                "optimality": float(solution.optimality),
                "points_used": int(excitation.size),
            }
        )

    delays = np.asarray([case.delay_us for case in REFERENCE_CASES], dtype=float)
    quanta = np.asarray(mean_quanta, dtype=float)
    coefficients, covariance = np.polyfit(delays, quanta, 1, cov=True)
    result = {
        "fits": fits,
        "mean_quanta": quanta.tolist(),
        "heating_rate_quanta_per_s": float(coefficients[0] * 1.0e6),
        "heating_rate_standard_error_quanta_per_s": float(np.sqrt(covariance[0, 0]) * 1.0e6),
        "linear_coefficients": coefficients.tolist(),
        "linear_covariance": covariance.tolist(),
    }
    LOGS.mkdir(parents=True, exist_ok=True)
    (LOGS / "independent_reference.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def test_result_has_exactly_five_raw_finite_numbers() -> None:
    parse_result()


def test_four_mean_quanta_values_match_independent_trace_fits() -> None:
    actual = parse_result()[:4]
    expected = np.asarray(independent_reference()["mean_quanta"], dtype=float)
    np.testing.assert_allclose(
        actual,
        expected,
        rtol=RELATIVE_TOLERANCE,
        atol=ABSOLUTE_QUANTA_TOLERANCE,
        err_msg="One or more reported mean phonon occupations do not agree with the Rabi-flop fits",
    )


def test_heating_rate_matches_independent_linear_fit() -> None:
    actual_rate = float(parse_result()[4])
    expected_rate = float(independent_reference()["heating_rate_quanta_per_s"])
    assert math.isclose(
        actual_rate,
        expected_rate,
        rel_tol=RELATIVE_TOLERANCE,
        abs_tol=ABSOLUTE_RATE_TOLERANCE,
    ), f"Heating rate is {actual_rate:.6g} quanta/s; independent fit gives {expected_rate:.6g} quanta/s"


def test_heating_rate_is_consistent_with_submitted_quanta_and_is_positive() -> None:
    values = parse_result()
    quanta = values[:4]
    submitted_rate = float(values[4])
    delays_us = np.asarray([case.delay_us for case in REFERENCE_CASES], dtype=float)
    derived_rate = float(np.polyfit(delays_us, quanta, 1)[0] * 1.0e6)
    assert np.all(quanta >= 0.0), "Mean phonon occupations must be non-negative"
    assert submitted_rate > 0.0 and derived_rate > 0.0, "The fitted heating rate must be positive"
    assert math.isclose(
        submitted_rate,
        derived_rate,
        rel_tol=RELATIVE_TOLERANCE,
        abs_tol=ABSOLUTE_RATE_TOLERANCE,
    ), "The reported heating rate is not consistent with a linear fit to the four submitted occupations"
