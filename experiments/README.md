# Running FrontierPhysics Experiments

Validate the task and oracle first:

```bash
bench tasks check tasks/surface-ion-trap-shuttling
bench eval run \
  --tasks-dir tasks/surface-ion-trap-shuttling \
  --agent oracle \
  --sandbox docker \
  --jobs-dir jobs/oracle
```

Primary no-skill run:

```bash
bench eval run \
  --tasks-dir tasks/surface-ion-trap-shuttling \
  --agent <agent> \
  --model <model> \
  --skill-mode no-skill \
  --sandbox docker \
  --jobs-dir jobs/<agent>-no-skill
```

Solvability control:

```bash
bench eval run \
  --tasks-dir tasks/surface-ion-trap-shuttling \
  --agent <agent> \
  --model <model> \
  --skill-mode with-skill \
  --skills-dir tasks/surface-ion-trap-shuttling/environment/skills/ \
  --sandbox docker \
  --jobs-dir jobs/<agent>-with-skill
```

Inspect every preserved trajectory and output artifact before reporting a model
capability conclusion.
