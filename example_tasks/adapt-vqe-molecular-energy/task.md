---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The solver must implement variational quantum eigensolver logic from Pauli Hamiltonians without using a quantum-computing framework.
  category: natural-science
  subcategory: quantum-computing
  category_confidence: high
  task_type:
  - calculation
  - optimization
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
  - quantum-computing
  - vqe
  - adapt-vqe
  - molecular-energy
  - scipy
verifier:
  type: test-script
  timeout_sec: 900.0
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
  storage_mb: 10240
  gpus: 0
---

Compute the molecular ground-state energies defined by the Jordan-Wigner Hamiltonians in `/root/input/h2_hamiltonian.json`, `/root/input/lih_hamiltonian.json`, and `/root/input/beh2_hamiltonian.json`. Read `/root/input/problem_spec.md` for the tier definitions and output schema. Implement dense-matrix VQE and ADAPT-VQE-style optimization using only NumPy and SciPy; do not use Qiskit, Cirq, PennyLane, OpenFermion, Tequila, or another quantum-computing framework.

Write `/root/output/results.json` with the required result for each molecule. The H2 record must include `molecule`, `energy_ha`, `method`, and `n_parameters`. The LiH and BeH2 records must additionally include `adapt_iterations` and `operator_sequence`. Use the molecule, qubit, electron, active-space, and Pauli-term data from the input JSON files without modifying anything under `/root/input`.
