---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The task requires a reusable astronomical image-reduction pipeline that handles masking, alignment, drizzling, astrometry, photometry, and quality control across unseen visits.
  category: natural-science
  subcategory: astronomy
  category_confidence: high
  task_type:
  - data-processing
  - analysis
  modality:
  - scientific-data
  - image
  - csv
  interface:
  - terminal
  - python
  skill_type:
  - domain-procedure
  - library-api-usage
  tags:
  - astronomy
  - hst
  - fits
  - photometry
  - astrometry
  - image-reduction
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

Implement a reusable HST ACS/WFC visit-reduction program at `/root/output/reduce_visit.py`. Read `/root/input/TASK_PROMPT.md`, use `/root/input/starter_project/reduce_visit.py` as the starting point, and validate the implementation on the visible visit under `/root/input/acs_visit_f606w_lockman`. The program must accept `python reduce_visit.py --input <visit-root-or-parent> --output <output-dir>` and process every visit it discovers without relying on hardcoded visit identifiers.

For each visit, create `<output-dir>/<visit_id>/drizzled_image.csv`, `source_catalog.csv`, `alignment_solution.csv`, `photometry_qc.json`, and `reduction_report.md`. Implement the required data-quality masking, exposure alignment, image combination, source photometry, astrometric calibration, and QC reporting so the same script works on evaluator-only visits. Do not modify `/root/input`; keep the implementation and scratch artifacts under `/root/output`.
