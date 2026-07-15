---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The solver must derive a two-atom lattice dynamical matrix and consistently propagate its eigenfrequencies into dispersion, density-of-states, and thermodynamic calculations.
  category: natural-science
  subcategory: solid-state-physics
  category_confidence: high
  task_type:
  - calculation
  - simulation
  modality:
  - scientific-data
  - json
  interface:
  - terminal
  - python
  skill_type:
  - mathematical-method
  - domain-procedure
  tags:
  - phonons
  - lattice-dynamics
  - density-of-states
  - thermodynamics
  - solid-state-physics
verifier:
  type: test-script
  timeout_sec: 1800.0
  service: main
  hardening:
    cleanup_conftests: true
agent:
  timeout_sec: 7200.0
environment:
  network_mode: no-network
  build_timeout_sec: 900.0
  os: linux
  cpus: 4
  memory_mb: 8192
  storage_mb: 20480
  gpus: 0
---

Follow `/root/input/problem_spec.md` to construct the dynamical matrix for the specified two-atom, two-dimensional hexagonal lattice. Complete the one-dimensional diatomic-chain validation, evaluate the phonon branches along the required high-symmetry path, compute the phonon density of states, and derive the requested temperature-dependent vibrational observables. Implement the lattice dynamics directly with NumPy and SciPy; do not use Phonopy, ASE, or another phonon framework.

Write `/root/output/diatomic_1d.npz`, `/root/output/dispersion_2d.npz`, `/root/output/dos.npz`, `/root/output/thermodynamics.npz`, and `/root/output/results.json`. Follow the exact array keys, shapes, grids, units, and summary schema in the problem specification. Do not modify `/root/input` or write final artifacts outside `/root/output`.
