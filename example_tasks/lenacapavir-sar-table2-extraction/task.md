---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The task requires combining a shared medicinal-chemistry scaffold with row-specific substituent drawings and exact potency values for 17 compounds.
  category: natural-science
  subcategory: medicinal-chemistry
  category_confidence: high
  task_type:
  - extraction
  - reconstruction
  modality:
  - document
  - image
  - csv
  interface:
  - browser
  - terminal
  skill_type:
  - domain-procedure
  - visual-interpretation
  tags:
  - lenacapavir
  - medicinal-chemistry
  - smiles
  - structure-activity
  - pdf
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

Open `/root/input/source_paper.pdf` and locate Table 2, “SAR for R1 Analogs.” Combine the common scaffold shown with the table and each row's R1 substituent to reconstruct the complete molecule for compounds 23 and 25 through 40. Extract the corresponding MT-4 EC50 value reported in nanomolar units. Use only the staged manuscript as the source of truth; do not search for answers online.

Write `/root/output/submission.csv` with the exact columns `Ligand_ID,SMILES,EC50_MT4` and one row for each of the 17 compounds. Every SMILES value must encode the full molecule rather than the isolated R1 fragment. Do not create additional output files.
