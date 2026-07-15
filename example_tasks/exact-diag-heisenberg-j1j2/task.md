---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The solver must exploit spin conservation to diagonalize a frustrated 4 x 4 quantum magnet and derive static and dynamical observables.
  category: natural-science
  subcategory: condensed-matter-physics
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
  - heisenberg-model
  - exact-diagonalization
  - quantum-magnetism
  - lanczos
  - structure-factor
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
  memory_mb: 16384
  storage_mb: 20480
  gpus: 0
---

Implement exact diagonalization for the spin-1/2 J1-J2 Heisenberg antiferromagnet on a periodic `4 x 4` square lattice in the conserved `S_z = 0` sector. Follow the lattice, coupling, momentum-grid, Lanczos, numerical-tolerance, and file-schema requirements in `/root/input/problem_spec.md`. Use NumPy and SciPy only; do not install or use an external quantum framework.

Write `/root/output/ground_state.npz`, `/root/output/correlations.npz`, `/root/output/dynamical_sf.npz`, and `/root/output/results.json`. The files must contain the required ground-state energies and vector, spin gap, real-space correlations, static structure factor, frequency-resolved dynamical structure factor, reproducibility coefficients, and scalar summaries. Do not modify `/root/input` or write final artifacts outside `/root/output`.
