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
  - experiment
  - data-processing
  modality:
  - scientific-data
  - h5
  interface:
  - terminal
  - python
  skill_type:
  - -
  tags:
  - experiment
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

In the experiment we shot 729 nm beam to drive the transition from S to D state of 40Ca+ ions chain (9 ions chain in a linear paul trap). The trap is a marco 3D trap and 9 ions are lined up along the axial direction. We can assume the trap potential is a 3D-harmonic-oscillator.

For the gaussian-beam along axial direction, the intensity distribution is modelled by this array [0.96912696, 0.9844114, 0.99344862, 0.99840835, 1., 0.99840835, 0.99344862, 0.9844114, 0.96912696]. Given the rabi flop experimental data in the env (florescence collected from 9 ions in total):

```
/root/data/delay_0us.h5
/root/data/delay_300us.h5
/root/data/delay_500us.h5
/root/data/delay_1000us.h5
```

I want to calculate the heating rate in this trap for the ion chain for COM motional mode. In the unit of quanta/s. During fitting you should consider uncertainties.

In the end write a `result.md` as below (with 5 raw numbers):

```md
number_of_quanta_at_0us
number_of_quanta_at_300us
number_of_quanta_at_500us
number_of_quanta_at_1000us
heating_rate
```