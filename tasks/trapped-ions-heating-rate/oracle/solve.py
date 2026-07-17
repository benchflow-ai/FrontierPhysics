#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

import h5py
import numpy as np
from scipy.optimize import curve_fit

ROOT = Path("/root")
DATA_DIR = ROOT / "data"
PROVENANCE_PATH = DATA_DIR / "provenance.json"

ION_COUNT = 9
AXIAL_FREQUENCY_HZ = 0.177e6
LASER_WAVELENGTH_M = 729e-9
CALCIUM_40_MASS_KG = 6.6551079e-26
HBAR = 6.62607004e-34 / (2.0 * np.pi)
THERMAL_CUTOFF = 500
INTENSITY_DISTRIBUTION = np.array(
    [0.96912696, 0.9844114, 0.99344862, 0.99840835, 1.0, 0.99840835, 0.99344862, 0.9844114, 0.96912696],
    dtype=float,
)


@dataclass(frozen=True)
class FitCase:
    delay_us: float
    filename: str
    tail_points_excluded: int
    initial_guess: tuple[float, float, float, float]


CASES = (
    FitCase(0.0, "delay_0us.h5", 10, (1.0, 0.04, 0.1, 20.0)),
    FitCase(300.0, "delay_300us.h5", 10, (1.0, 0.03, 0.1, 20.0)),
    FitCase(500.0, "delay_500us.h5", 10, (1.0, 0.03, 0.1, 20.0)),
    FitCase(1000.0, "delay_1000us.h5", 9, (1.0, 0.01, 0.1, 0.0)),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def lamb_dicke_parameter() -> float:
    angular_frequency = 2.0 * np.pi * AXIAL_FREQUENCY_HZ
    single_ion_eta = 2.0 * np.pi * np.sqrt(HBAR / (2.0 * angular_frequency * CALCIUM_40_MASS_KG)) / LASER_WAVELENGTH_M
    return float(single_ion_eta / np.sqrt(ION_COUNT))


ETA = lamb_dicke_parameter()
PHONON_INDEX = np.arange(THERMAL_CUTOFF, dtype=float)
RABI_CORRECTION = 1.0 - ETA**2 * (PHONON_INDEX + 0.5) + ETA**4 * (1.0 + 2.0 * PHONON_INDEX * (1.0 + PHONON_INDEX)) / 8.0


def thermal_carrier(time_us: np.ndarray, rabi_mhz: float, mean_quanta: float) -> np.ndarray:
    ratio = mean_quanta / (mean_quanta + 1.0)
    populations = np.power(ratio, PHONON_INDEX) / (mean_quanta + 1.0)
    phases = 2.0 * np.pi * (rabi_mhz * RABI_CORRECTION)[:, None] * np.asarray(time_us, dtype=float)[None, :]
    return 0.5 - 0.5 * np.sum(populations[:, None] * np.cos(phases), axis=0)


def nine_ion_model(
    time_us: np.ndarray,
    amplitude: float,
    base_rabi_mhz: float,
    offset: float,
    mean_quanta: float,
) -> np.ndarray:
    traces = [amplitude * thermal_carrier(time_us, intensity * base_rabi_mhz, mean_quanta) + offset for intensity in INTENSITY_DISTRIBUTION]
    return np.mean(traces, axis=0)


def load_trace(case: FitCase) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    path = DATA_DIR / case.filename
    with h5py.File(path, "r") as handle:
        time_us = np.asarray(handle["datasets/rabi_t"][:], dtype=float)
        raw_counts = np.asarray(handle["datasets/pmt_counts_avg_thresholded"][:], dtype=float)

    if time_us.shape != (50,) or raw_counts.shape != (50,):
        raise RuntimeError(f"{case.filename} does not contain the expected 50-point trace")

    usable = slice(None, -case.tail_points_excluded)
    time_us = time_us[usable]
    raw_counts = raw_counts[usable]
    inverted = np.max(raw_counts) - raw_counts
    excitation = inverted / np.max(inverted)
    return time_us, raw_counts, excitation


def fit_trace(case: FitCase) -> dict[str, object]:
    time_us, raw_counts, excitation = load_trace(case)
    parameters, covariance = curve_fit(
        nine_ion_model,
        time_us,
        excitation,
        p0=case.initial_guess,
        maxfev=20_000,
    )
    errors = np.sqrt(np.diag(covariance))
    fitted = nine_ion_model(time_us, *parameters)
    residual = excitation - fitted
    return {
        "delay_us": case.delay_us,
        "filename": case.filename,
        "points_used": int(time_us.size),
        "tail_points_excluded": case.tail_points_excluded,
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
        "covariance": covariance.tolist(),
        "rmse": float(np.sqrt(np.mean(residual**2))),
        "raw_count_min": float(np.min(raw_counts)),
        "raw_count_max": float(np.max(raw_counts)),
    }


def main() -> None:
    provenance = json.loads(PROVENANCE_PATH.read_text())
    for case in CASES:
        expected_hash = provenance["files"][case.filename]["sha256"]
        actual_hash = sha256(DATA_DIR / case.filename)
        if actual_hash != expected_hash:
            raise RuntimeError(f"{case.filename} does not match its provenance hash")

    fits = [fit_trace(case) for case in CASES]
    delays_us = np.array([fit["delay_us"] for fit in fits], dtype=float)
    mean_quanta = np.array([fit["parameters"]["mean_quanta"] for fit in fits], dtype=float)
    heating_coefficients, heating_covariance = np.polyfit(delays_us, mean_quanta, 1, cov=True)
    heating_rate_quanta_per_s = float(heating_coefficients[0] * 1.0e6)
    heating_rate_error_quanta_per_s = float(np.sqrt(heating_covariance[0, 0]) * 1.0e6)

    result_values = [*mean_quanta.tolist(), heating_rate_quanta_per_s]
    (ROOT / "result.md").write_text("\n".join(f"{value:.10f}" for value in result_values) + "\n")

    diagnostics = {
        "model": {
            "axial_frequency_hz": AXIAL_FREQUENCY_HZ,
            "calcium_40_mass_kg": CALCIUM_40_MASS_KG,
            "ion_count": ION_COUNT,
            "lamb_dicke_parameter_com": ETA,
            "laser_wavelength_m": LASER_WAVELENGTH_M,
            "thermal_cutoff": THERMAL_CUTOFF,
            "intensity_distribution": INTENSITY_DISTRIBUTION.tolist(),
        },
        "fits": fits,
        "heating_fit": {
            "slope_quanta_per_us": float(heating_coefficients[0]),
            "intercept_quanta": float(heating_coefficients[1]),
            "covariance": heating_covariance.tolist(),
            "heating_rate_quanta_per_s": heating_rate_quanta_per_s,
            "standard_error_quanta_per_s": heating_rate_error_quanta_per_s,
        },
        "provenance": provenance,
    }
    (ROOT / "oracle_diagnostics.json").write_text(json.dumps(diagnostics, indent=2, sort_keys=True) + "\n")
    print(json.dumps(diagnostics, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
