---
schema_version: '1.3'
metadata:
  author_name: RDI Berkeley
  author_email: rdi_research@berkeley.edu
  difficulty: hard
  difficulty_explanation: The task requires building a leakage-free spatiotemporal climate-emulation pipeline and producing predictions in several exact array and tabular formats.
  category: natural-science
  subcategory: climate-science
  category_confidence: high
  task_type:
  - prediction
  - machine-learning
  modality:
  - scientific-data
  - time-series
  interface:
  - terminal
  - python
  skill_type:
  - domain-procedure
  - library-api-usage
  tags:
  - climate
  - cmip6
  - zarr
  - xarray
  - emulation
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

Build a climate-emulation pipeline from `/root/input/data.zarr`. Train on all months from the `ssp126`, `ssp370`, and `ssp585` scenarios, and predict the final 120 months of the held-out `ssp245` scenario. Use `member_id = 0` for target tensors, broadcast the scalar `CO2` and `CH4` forcings onto the `48 x 72` grid, rename the spatial dimensions from `latitude` and `longitude` to `y` and `x`, and fit every normalization statistic on the training split only. The held-out `tas` and `pr` labels are masked and must not be used during training.

Follow `/root/input/output_contract.json` and write `/root/output/processed/train_inputs.npy`, `train_outputs.npy`, `test_inputs.npy`, `metadata.json`, and `test_predictions.npy`, plus `/root/output/submissions/kaggle_submission.csv`. The CSV must contain the required flattened predictions, and every array must have the shape specified by the contract. `/root/input/metadata.json` and `/root/input/Starter.md` provide the dataset description and implementation guidance.
