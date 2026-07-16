---
schema_version: '1.3'
metadata:
  author_name: Bingran You
  author_email: bingran.you@berkeley.edu
  difficulty: medium
  category: atomic-molecular-and-optical-physics
  subcategory: trapped-ions
  category_confidence: high
  task_type:
  - data-processing
  - experiment
  modality:
  - scientific-data
  - h5
  interface:
  - terminal
  - python
  skill_type:
  - -
  tags:
  - atomic-molecular-and-optical-physics
  - trapped-ions
  - data-analysis
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

