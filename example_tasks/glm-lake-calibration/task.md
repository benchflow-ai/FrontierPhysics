---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The agent must calibrate interacting lake-model parameters against multi-year depth profiles while preserving the supplied forcing data and runtime.
  category: natural-science
  subcategory: hydrology
  category_confidence: high
  task_type:
  - simulation
  - optimization
  modality:
  - scientific-data
  - time-series
  interface:
  - terminal
  - simulation-tool
  skill_type:
  - domain-procedure
  - tool-workflow
  tags:
  - hydrology
  - lake-modeling
  - glm
  - calibration
  - temperature-profile
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
  storage_mb: 20480
  gpus: 0
---

Calibrate the staged GLM 3 model for Lake Mendota by editing `/root/input/glm3.nml`. Use the forcing files in `/root/input/bcs` and the observed temperature profiles in `/root/input/field_temp_oxy.csv`. Run the model through `/root/software/run_glm_from_input.sh` and tune the namelist until the overall RMSE between simulated and observed vertical temperatures is below `1.5 C`.

Save the final NetCDF simulation to `/root/output/output.nc`, covering January 1, 2009 through late December 2015. Modify only `/root/input/glm3.nml`; do not change the observations, boundary conditions, GLM binary, wrapper, or shared libraries.
