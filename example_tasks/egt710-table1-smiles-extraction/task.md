---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The agent must interpret chemical drawings in a paper, reconstruct nine complete molecules, and pair them with exact assay values.
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
  - medicinal-chemistry
  - smiles
  - structure-activity
  - pdf
  - chemical-structure
verifier:
  type: test-script
  timeout_sec: 900.0
  service: main
  hardening:
    cleanup_conftests: true
agent:
  timeout_sec: 7200.0
environment:
  network_mode: public
  build_timeout_sec: 900.0
  os: linux
  cpus: 4
  memory_mb: 8192
  storage_mb: 10240
  gpus: 0
---

Open `/root/input/source_paper.pdf` and locate Table 1 in “Discovery of EGT710, an Oral Nonpeptidomimetic Reversible Covalent SARS-CoV-2 Main Protease Inhibitor.” Reconstruct compounds 1 through 9 from the table's chemical drawings, validate each complete structure with the staged chemical editor, and capture the reported `IC50_uM` and `Solubility_mM` values.

Write exactly one file, `/root/output/submission.csv`, with the columns `Compound_ID,SMILES,IC50_uM,Solubility_mM`. Include one row for each compound ID from 1 through 9. Each SMILES string must represent the complete molecule and be chemically valid; do not save screenshots or alternate outputs.
