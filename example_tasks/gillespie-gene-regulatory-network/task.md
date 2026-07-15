---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The task combines exact stochastic simulation, ensemble analysis, bifurcation scanning, and a validated tau-leaping implementation under strict reproducibility constraints.
  category: natural-science
  subcategory: stochastic-biophysics
  category_confidence: high
  task_type:
  - simulation
  - analysis
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
  - gillespie
  - stochastic-simulation
  - gene-regulatory-network
  - tau-leaping
  - bifurcation
verifier:
  type: test-script
  timeout_sec: 1800.0
  service: main
  hardening:
    cleanup_conftests: true
agent:
  timeout_sec: 28800.0
environment:
  network_mode: no-network
  build_timeout_sec: 900.0
  os: linux
  cpus: 4
  memory_mb: 8192
  storage_mb: 20480
  gpus: 0
---

Implement the stochastic simulations specified in `/root/input/problem_spec.md`. Complete the exact Gillespie SSA validation for the birth-death process, the exact SSA study of the three-gene mutual-inhibition network, and the bifurcation and tau-leaping comparison. Use `numpy.random.default_rng` with every prescribed seed, implement the reaction logic yourself, and follow the specified event counts, parameter grids, leap condition, and non-negative population handling. Do not use SciPy or a dedicated stochastic-simulation package.

Write `/root/output/tier1_results.json`, `/root/output/tier2_results.json`, `/root/output/tier3_results.json`, and the reusable implementation `/root/output/gillespie_solver.py`. Follow every JSON schema in the problem specification; probabilities and basin fractions must be finite values in `[0, 1]` and must sum to one wherever they define a partition. Do not modify `/root/input` or write final artifacts outside `/root/output`.
