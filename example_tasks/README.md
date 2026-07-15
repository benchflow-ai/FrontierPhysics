# Agents' Last Exam physics task conversions

This directory contains review-only conversions of the 15 tasks under
[`rdi-berkeley/agents-last-exam/tasks/physical_sciences`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences)
at source commit
[`5af2f6d`](https://github.com/rdi-berkeley/agents-last-exam/commit/5af2f6d5c8cd42617c85528caf1edb31ee73a34c).

Each example uses the native SkillsBench/BenchFlow `task.md` schema version
`1.3`: YAML front matter followed by the standalone agent-facing instruction.
Source-relative ALE paths such as `base/input` and `base/output` have been
normalized to `/root/input` and `/root/output`.

## Review status

These are prompt conversions, not runnable benchmark packages. A runnable
SkillsBench task also requires:

- `environment/Dockerfile` and the frozen input data or software;
- `oracle/solve.sh`;
- `verifier/test.sh` and deterministic grading logic.

ALE's hidden references, licensed software, VM snapshots, and large input
archives have not been copied into this repository.

## Converted tasks

| Example | Source task | Area |
|---|---|---|
| [`adapt-vqe-molecular-energy`](adapt-vqe-molecular-energy/task.md) | [`adapt_vqe_molecular_energy`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/adapt_vqe_molecular_energy) | Quantum computing |
| [`climate-prediction`](climate-prediction/task.md) | [`climate_prediction`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/climate_prediction) | Climate emulation |
| [`computational-materials-science`](computational-materials-science/task.md) | [`computational_materials_science`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/computational_materials_science) | GW electronic structure |
| [`egt710-table1-smiles-extraction`](egt710-table1-smiles-extraction/task.md) | [`egt710_table1_smiles_extraction`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/egt710_table1_smiles_extraction) | Medicinal chemistry |
| [`exact-diag-heisenberg-j1j2`](exact-diag-heisenberg-j1j2/task.md) | [`exact_diag_heisenberg_j1j2`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/exact_diag_heisenberg_j1j2) | Condensed-matter physics |
| [`gillespie-gene-regulatory-network`](gillespie-gene-regulatory-network/task.md) | [`gillespie_gene_regulatory_network`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/gillespie_gene_regulatory_network) | Stochastic biophysics |
| [`glm-lake-calibration`](glm-lake-calibration/task.md) | [`glm_lake_calibration`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/glm_lake_calibration) | Environmental modeling |
| [`hst-acs-wfc-visit-reduction`](hst-acs-wfc-visit-reduction/task.md) | [`hst_acs_wfc_visit_reduction`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/hst_acs_wfc_visit_reduction) | Astronomy |
| [`ketcher-smiles-reproduction`](ketcher-smiles-reproduction/task.md) | [`ketcher_smiles_reproduction`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/ketcher_smiles_reproduction) | Molecular drawing |
| [`lenacapavir-sar-table2-extraction`](lenacapavir-sar-table2-extraction/task.md) | [`lenacapavir_sar_table2_extraction`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/lenacapavir_sar_table2_extraction) | Medicinal chemistry |
| [`molecular-structure-plausibility`](molecular-structure-plausibility/task.md) | [`molecular_structure_plausibility`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/molecular_structure_plausibility) | Computational chemistry |
| [`mose2-bse-absorption-soc`](mose2-bse-absorption-soc/task.md) | [`mose2_bse_absorption_soc`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/mose2_bse_absorption_soc) | Materials physics |
| [`phonon-dispersion-thermodynamics`](phonon-dispersion-thermodynamics/task.md) | [`phonon_dispersion_thermodynamics`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/phonon_dispersion_thermodynamics) | Solid-state physics |
| [`qm9-mmff94-forcefield-survey`](qm9-mmff94-forcefield-survey/task.md) | [`qm9_mmff94_forcefield_survey_1`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/qm9_mmff94_forcefield_survey_1) | Computational chemistry |
| [`silicon-bse-absorption`](silicon-bse-absorption/task.md) | [`silicon_bse_absorption`](https://github.com/rdi-berkeley/agents-last-exam/tree/main/tasks/physical_sciences/silicon_bse_absorption) | Materials physics |

## Review notes

- `glm-lake-calibration` overlaps the existing SkillsBench
  [`glm-lake-mendota`](https://github.com/benchflow-ai/skillsbench/tree/main/tasks/glm-lake-mendota)
  task, but retains ALE's stricter `1.5 C` RMSE target.
- The current ALE taxonomy reclassifies ADAPT-VQE, the Gillespie network, GLM
  calibration, and the lenacapavir extraction outside the physical-sciences
  domain. They remain here because their source directories are part of the
  requested set.
- The three browser-oriented chemistry tasks need a Linux-compatible staged
  browser application before they can become runnable SkillsBench packages.
- The QM9 prompt describes a very large full-dataset computation. Its source VM
  timeout is two hours even though the upstream runtime note estimates
  substantially longer execution; that budget needs resolution during
  implementation review.
