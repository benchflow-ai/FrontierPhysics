---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The task requires building a complete first-principles GW-BSE workflow and producing mutually consistent quasiparticle bands and optical spectra.
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
  - silicon
  - gw
  - bse
  - absorption
  - berkeleygw
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

Compute the GW-BSE absorption spectrum of bulk silicon using `/root/input/silicon.vasp` and `/root/input/Si.UPF`. Create the required Quantum ESPRESSO and BerkeleyGW input decks, run the mean-field and quasiparticle workflow, and compute optical spectra both with and without electron-hole interactions. Use the staged `pw.x`, `mpirun`, `epsilon.cplx.x`, `sigma.cplx.x`, `kernel.cplx.x`, `absorption.cplx.x`, and `inteqp.cplx.x` executables under `/root/software/bin`.

Write `/root/output/bandstructure.dat`, `eqp.dat`, `eqp_q.dat`, `absorption_eh.dat`, `absorption_noeh.dat`, `eigenvalues.dat`, `eigenvalues_noeh.dat`, `bandstructure_inteqp.png`, and `absorption.png`. The files must support extraction of the DFT and GW gaps, band-edge topology, first bright excitation, principal absorption features, and the spectral change introduced by electron-hole interactions. Do not write final artifacts outside `/root/output`.
