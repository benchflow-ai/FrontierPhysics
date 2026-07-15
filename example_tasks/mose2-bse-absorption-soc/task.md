---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The task requires a spin-orbit-coupled, noncollinear GW-BSE workflow for a two-dimensional material with physically correct truncation and optical outputs.
  category: natural-science
  subcategory: computational-materials-science
  category_confidence: high
  task_type:
  - simulation
  - calculation
  modality:
  - scientific-data
  - image
  interface:
  - terminal
  - simulation-tool
  skill_type:
  - domain-procedure
  - tool-workflow
  tags:
  - mose2
  - spin-orbit-coupling
  - gw
  - bse
  - optical-spectrum
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
  cpus: 16
  memory_mb: 32768
  storage_mb: 30720
  gpus: 0
---

Compute the spin-orbit-coupled GW-BSE optical response of monolayer MoSe2 using `/root/input/MoSe2.vasp`, `/root/input/Mo.soc.upf`, and `/root/input/Se.soc.upf`. Create the necessary Quantum ESPRESSO and BerkeleyGW input decks, run the mean-field calculation with explicit SOC and noncollinear settings, and complete the dielectric, self-energy, kernel, and absorption stages with the required two-dimensional Coulomb-truncation treatment. Use the staged executables under `/root/software/bin`.

Write `/root/output/MoSe2_bands.dat.gnu`, `/root/output/MoSe2_bands.png`, `/root/output/absorption_eh.dat`, and `/root/output/exciton_absorption_spectra_avg.png`. The results must expose physically consistent band edges, spin-orbit splittings, and the first two prominent excitonic features. Do not write final artifacts outside `/root/output`.
