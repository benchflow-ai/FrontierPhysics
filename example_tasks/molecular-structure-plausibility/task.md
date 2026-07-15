---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: medium
  difficulty_explanation: The agent must combine chemical valence reasoning with three-dimensional geometry checks across dozens of structures while avoiding false positives.
  category: natural-science
  subcategory: computational-chemistry
  category_confidence: high
  task_type:
  - classification
  - analysis
  modality:
  - scientific-data
  interface:
  - terminal
  - python
  skill_type:
  - domain-procedure
  - library-api-usage
  tags:
  - molecular-geometry
  - xyz
  - rdkit
  - chemical-validity
  - structure-filtering
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

Read `/root/input/task_brief.md` and inspect every `.xyz` file in `/root/input/xyz_files`. Identify all structures that violate the brief's chemical-valence or molecular-geometry plausibility rules. You may use the locked scientific Python environment in `/root/input/runtime_env`, including RDKit, NumPy, and SciPy.

Write `/root/output/problematic_structures.txt` with exactly one problematic `.xyz` filename per line. Use the filenames exactly as they appear in the input directory, without directory prefixes, explanations, or additional output files.
