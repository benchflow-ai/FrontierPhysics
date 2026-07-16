---
schema_version: '1.3'
metadata:
  author_name: Bingran You
  author_email: bingran.you@berkeley.edu
  difficulty: hard
  category: natural-science
  subcategory: ion-trap-shuttling
  category_confidence: high
  task_type:
  - simulation
  - calculation
  - generation
  modality:
  - 3d-model
  - scientific-data
  - csv
  interface:
  - terminal
  - python
  - simulation-tool
  skill_type:
  - domain-procedure
  - mathematical-method
  - library-api-usage
  tags:
  - physics
  - trapped-ions
  - trap-simulation
  - shuttling-simulation
verifier:
  type: test-script
  timeout_sec: 900.0
  service: main
  pytest_plugins:
  - ctrf
  hardening:
    cleanup_conftests: true
agent:
  timeout_sec: 3600.0
environment:
  network_mode: public
  build_timeout_sec: 1200.0
  os: linux
  cpus: 4
  memory_mb: 10240
  storage_mb: 20480
  gpus: 0
---

