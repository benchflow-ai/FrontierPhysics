#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

import h5py
import numpy as np
from scipy.optimize import curve_fit

INTENSITY = np.asarray(
    [0.96912696, 0.9844114, 0.99344862, 0.99840835, 1.0, 0.99840835, 0.99344862, 0.9844114, 0.96912696],
    dtype=float,
)
PHONONS = np.arange(500, dtype=float)
HBAR = 6.62607004e-34 / (2.0 * np.pi)
OMEGA_Z = 2.0 * np.pi * 0.177e6
ETA = 2.0 * np.pi * np.sqrt(HBAR / (2.0 * OMEGA_Z * 6.6551079e-26)) / 729e-9 / np.sqrt(9.0)
CORRECTION = 1.0 - ETA**2 * (PHONONS + 0.5) + ETA**4 * (1.0 + 2.0 * PHONONS * (1.0 + PHONONS)) / 8.0


@dataclass(frozen=True)
class Case:
    delay_us: float
    filename: str
    drop_tail: int
    guess: tuple[float, float, float, float]


CASES = (
    Case(0.0, "delay_0us.h5", 10, (1.0, 0.04, 0.1, 20.0)),
    Case(300.0, "delay_300us.h5", 10, (1.0, 0.03, 0.1, 20.0)),
    Case(500.0, "delay_500us.h5", 10, (1.0, 0.03, 0.1, 20.0)),
    Case(1000.0, "delay_1000us.h5", 9, (1.0, 0.01, 0.1, 0.0)),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def carrier(time_us: np.ndarray, rabi_mhz: float, mean_quanta: float) -> np.ndarray:
    weights = np.power(mean_quanta / (mean_quanta + 1.0), PHONONS) / (mean_quanta + 1.0)
    phases = 2.0 * np.pi * (rabi_mhz * CORRECTION)[:, None] * time_us[None, :]
    return 0.5 - 0.5 * np.sum(weights[:, None] * np.cos(phases), axis=0)


def model(
    time_us: np.ndarray,
    amplitude: float,
    base_rabi_mhz: float,
    offset: float,
    mean_quanta: float,
) -> np.ndarray:
    return np.mean(
        [amplitude * carrier(time_us, factor * base_rabi_mhz, mean_quanta) + offset for factor in INTENSITY],
        axis=0,
    )


def load_case(data_dir: Path, case: Case) -> tuple[np.ndarray, np.ndarray]:
    path = data_dir / case.filename
    with h5py.File(path, "r") as handle:
        time_us = np.asarray(handle["datasets/rabi_t"][:], dtype=float)
        counts = np.asarray(handle["datasets/pmt_counts_avg_thresholded"][:], dtype=float)
    time_us = time_us[: -case.drop_tail]
    counts = counts[: -case.drop_tail]
    excitation = counts.max() - counts
    excitation /= excitation.max()
    return time_us, excitation


def analyze(data_dir: Path) -> dict[str, object]:
    provenance = json.loads((data_dir / "provenance.json").read_text())
    fits: list[dict[str, object]] = []
    occupations: list[float] = []

    for case in CASES:
        path = data_dir / case.filename
        expected_hash = provenance["files"][case.filename]["sha256"]
        if sha256(path) != expected_hash:
            raise RuntimeError(f"Input hash mismatch for {case.filename}")

        time_us, excitation = load_case(data_dir, case)
        parameters, covariance = curve_fit(
            model,
            time_us,
            excitation,
            p0=case.guess,
            maxfev=20_000,
        )
        errors = np.sqrt(np.diag(covariance))
        residual = excitation - model(time_us, *parameters)
        occupations.append(float(parameters[3]))
        fits.append(
            {
                "delay_us": case.delay_us,
                "filename": case.filename,
                "points_used": int(time_us.size),
                "parameters": {
                    "amplitude": float(parameters[0]),
                    "base_rabi_mhz": float(parameters[1]),
                    "offset": float(parameters[2]),
                    "mean_quanta": float(parameters[3]),
                },
                "standard_errors": {
                    "amplitude": float(errors[0]),
                    "base_rabi_mhz": float(errors[1]),
                    "offset": float(errors[2]),
                    "mean_quanta": float(errors[3]),
                },
                "rmse": float(np.sqrt(np.mean(residual**2))),
            }
        )

    delays = np.asarray([case.delay_us for case in CASES], dtype=float)
    coefficients, covariance = np.polyfit(delays, np.asarray(occupations), 1, cov=True)
    heating_rate = float(coefficients[0] * 1.0e6)
    return {
        "occupations": occupations,
        "fits": fits,
        "heating_rate_quanta_per_s": heating_rate,
        "heating_rate_standard_error_quanta_per_s": float(np.sqrt(covariance[0, 0]) * 1.0e6),
        "linear_coefficients": coefficients.tolist(),
        "linear_covariance": covariance.tolist(),
        "lamb_dicke_parameter_com": float(ETA),
        "provenance": provenance,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Fit nine-ion carrier thermometry traces and infer the heating rate.")
    parser.add_argument("--data-dir", type=Path, default=Path("/root/data"))
    parser.add_argument("--output", type=Path, default=Path("/root/result.md"))
    parser.add_argument("--diagnostics", type=Path, default=Path("/root/fit_diagnostics.json"))
    args = parser.parse_args()

    result = analyze(args.data_dir)
    values = [*result["occupations"], result["heating_rate_quanta_per_s"]]
    args.output.write_text("\n".join(f"{float(value):.10f}" for value in values) + "\n")
    args.diagnostics.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
