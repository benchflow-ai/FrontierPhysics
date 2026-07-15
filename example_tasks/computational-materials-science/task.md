---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The task requires constructing and executing a multi-stage Quantum ESPRESSO and BerkeleyGW workflow with physically valid convergence settings.
  category: natural-science
  subcategory: computational-materials-science
  category_confidence: high
  task_type:
  - simulation
  - calculation
  modality:
  - scientific-data
  interface:
  - terminal
  - simulation-tool
  skill_type:
  - domain-procedure
  - tool-workflow
  tags:
  - silicon
  - quantum-espresso
  - berkeleygw
  - gw
  - band-gap
verifier:
  type: test-script
  timeout_sec: 1800.0
  service: main
  hardening:
    cleanup_conftests: true
agent:
  timeout_sec: 14400.0
environment:
  network_mode: no-network
  build_timeout_sec: 1800.0
  os: linux
  cpus: 8
  memory_mb: 16384
  storage_mb: 30720
  gpus: 0
---

Compute the indirect GW quasiparticle band gap of bulk silicon using the structure `/root/input/silicon/silicon.vasp` and pseudopotential `/root/input/silicon/Si.UPF`. Create the required Quantum ESPRESSO and BerkeleyGW input decks, then run SCF, NSCF or bands, `pw2bgw`, `epsilon`, `sigma`, and `inteqp` through `/root/software/launch_qe_bgw.sh`. Use approximately `5 x 5 x 5` wavefunction k-point sampling, a `10 Ry` dielectric cutoff, about 39 GW summation bands, `OMP_NUM_THREADS=1`, and no more than four MPI ranks.

Save `/root/output/silicon/bandstructure.dat`, `/root/output/silicon/eqp.dat`, and `/root/output/silicon/bandstructure_inteqp.png`. The outputs must support extraction of the DFT and GW indirect gaps, the VBM and CBM locations, and the quasiparticle gap opening. Do not write final artifacts outside `/root/output`.
