---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: medium
  difficulty_explanation: The agent must visually interpret a chemical structure, reproduce its exact connectivity in a molecular editor, and export a valid single-molecule SMILES representation.
  category: natural-science
  subcategory: molecular-chemistry
  category_confidence: high
  task_type:
  - reconstruction
  - extraction
  modality:
  - image
  - chemical-structure
  interface:
  - browser
  skill_type:
  - visual-interpretation
  - tool-workflow
  tags:
  - ketcher
  - smiles
  - molecular-structure
  - chemical-drawing
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

Recreate molecule 7YY from `/root/input/structure.svg` using the staged Ketcher browser application. Preserve the depicted atoms, bond orders, stereochemistry, rings, and connectivity, then export the complete molecule as SMILES.

Save exactly one non-comment SMILES entry to `/root/output/submission.smi`. Do not save screenshots, alternative structures, or additional files.
