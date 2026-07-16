---
schema_version: '1.3'
metadata:
  author_name: Bingran You
  author_email: bingran.you@berkeley.edu
  difficulty: hard
  category: atomic-molecular-and-optical-physics
  subcategory: trapped-ions
  category_confidence: high
  task_type:
  - experiment
  - simulation
  - optimization
  modality:
  - scientific-data
  - 3d-model
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
  - experiment
  - atomic-molecular-and-optical-physics
  - trapped-ions
  - trap-simulation
  - shuttling-simulation
  - inverse-engineering
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

In `/root/surface_trap.stl` you have a trap model file for a surface ion trap (surface Paul trap). You need to simulate and calculate the trap frequency along the radial direction for a singly charged `40Ca+` ion when an 80 V RF amplitude at 39.15 MHz is applied to the RF electrode. The RF electrode is the "2-rail" electrode in the center and you can treat other electrodes as ground to do the simulation for the radial trap frequency calculation. (Axial is defined as the direction along the 2-rail RF electrode in the center, and radial means the direction parallel to the trap surface and perpendicular to the RF electrode.) Note it down in MHz as number `W_radial_freq`.

After getting `W_radial_freq`, based on the standard Mathieu differential equation, use the anisotropy parameter `α = (W_axial_freq / W_radial_freq)^2 = 0.00174` to calculate the axial trap frequency. Note it down in MHz as number `W_axial_freq`.

Now imagine we are shuttling a one-ion chain along the axial direction. What is the ideal shuttling function if we do harmonic transport at 10 m/s and move a distance of 100 um? Give the trap-center shuttling function obtained using the inverse-engineering method.

Then we expand this into a 9-ion chain of singly charged `40Ca+` ions, and we want to first calculate the equilibrium ion-ion spacing of the whole chain with the given axial trap frequency. Note down 8 positive spacing distances in um: `d1`, `d2`, `d3`, `d4`, ..., `d8`.

With the ion-ion spacing numbers, we can start shuttling the ion chain step by step. I want to find the final shuttling function from beginning to the end. The whole process is: I have a static single-ion addressing beam that does not move. At the beginning the first ion in the chain is sitting at the addressing beam. Then the ion chain starts to move step by step, dwelling for 1 us after each move, until the final ion is addressed. Each shuttling move is 10 us, and for each shuttling stage I want to use the same inverse-engineered shuttling form. Give me the final shuttling function.

In the end you should output `/root/result.md`. Use the following key-value format, with frequencies in MHz and distances in um:

```md
W_radial_freq: <number>
W_axial_freq: <number>
d1: <number>
d2: <number>
d3: <number>
d4: <number>
d5: <number>
d6: <number>
d7: <number>
d8: <number>
```

Also output `/root/1.csv` and `/root/2.csv`, each with exactly 10,000 sampling points plus a header row.

In `1.csv` (the first shuttling function for a single ion) and `2.csv` (the complete shuttling function for the 9-ion chain), the first column is time in us and the second column is the center position of the trap potential along the axial direction in um.
