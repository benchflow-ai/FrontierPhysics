---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The task scans the full QM9 corpus, performs large conformer searches and constrained potential-energy scans, and consolidates chemically meaningful failure modes across five dependent phases.
  category: natural-science
  subcategory: computational-chemistry
  category_confidence: high
  task_type:
  - analysis
  - simulation
  modality:
  - scientific-data
  - csv
  - json
  - image
  interface:
  - terminal
  - python
  skill_type:
  - domain-procedure
  - library-api-usage
  tags:
  - qm9
  - mmff94
  - force-field
  - conformer-search
  - potential-energy-surface
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
  build_timeout_sec: 1800.0
  os: linux
  cpus: 4
  memory_mb: 16384
  storage_mb: 30720
  gpus: 0
---

Survey systematic MMFF94 force-field failures against the B3LYP/6-31G(2df,p) geometries in `/root/input/dsgdb9nsd.xyz.tar.bz2`. Stream the archive without extracting it. For molecules containing exactly two O, N, or F atoms, run a seeded single-conformer MMFF94 comparison and retain discrepancies of at least `1.0 Å`; classify those candidates with a seeded 200-conformer global-minimum search and a `0.5 Å` residual-discrepancy threshold. Analyze Murcko scaffolds and functional groups for the genuine failures, select the five largest residuals, and perform a constrained MMFF94 distance scan from `8.0 Å` to `2.5 Å` in `0.1 Å` steps with a fresh force field at each step.

Write the following artifacts under `/root/output`: `force_field_failures.csv`, `phase2_classified.csv`, `phase3_scaffold_analysis.json`, `phase4_pes_results.json`, `pes_scan_rank1.png` through `pes_scan_rank5.png`, and `phase5_final_report.json`. Use the exact schemas described below:

- `force_field_failures.csv`: `Molecule_ID,SMILES,QM9_Dist_A,RDKit_Dist_A,Discrepancy_A`.
- `phase2_classified.csv`: `Molecule_ID,SMILES,QM9_Dist_A,Naive_MMFF94_Dist_A,Naive_Discrepancy_A,Global_Min_Dist_A,Global_Min_Energy_kcal,Residual_Discrepancy_A,Classification`.
- `phase3_scaffold_analysis.json`: `survey_statistics`, `scaffold_analysis`, `top5_worst_molecules`, and `all_genuine_failures`; identify molecules there by rank and SMILES rather than QM9 ID.
- `phase4_pes_results.json`: keys `rank_1` through `rank_5`, each recording the canonical SMILES, heteroatom pair, reference and MMFF94 distances, global-minimum and constrained energies, snap distance and energy drop, and `delta_e`.
- `phase5_final_report.json`: `survey_statistics`, `scaffold_analysis`, `top5_characterization`, and `top5_pes_summary`, including separate short- and long-reference-distance groups and an explanation of their physical failure modes.

Use `randomSeed=42` for ETKDG and process molecules sequentially without spawning operating-system worker processes. Do not use network access or write final artifacts outside `/root/output`.
