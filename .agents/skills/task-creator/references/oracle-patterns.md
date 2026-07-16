# Oracle Patterns for Physics Tasks

The oracle is a human-authored reference workflow. It proves that the task can
be solved under the declared assumptions and resources; it does not establish
scientific truth by itself.

## 1. Numerical derivation

Use for simulation, fitting, inference, dynamics, field solves, and numerical
linear algebra.

- compute from bundled inputs;
- pin package versions and random seeds;
- emit intermediate diagnostics;
- check convergence before accepting a value;
- preserve units until final serialization.

For expensive solvers, precomputed meshes or basis data may be bundled in
`oracle/` when their provenance and hashes are recorded. Final answers must
still be derived at runtime.

## 2. Independent data reduction

Use for experimental or observational datasets.

1. Parse the raw or minimally processed artifact.
2. Apply documented calibration and quality cuts.
3. Fit or aggregate with a method appropriate to the measurement model.
4. Save residuals, uncertainties, and fit diagnostics.

Do not derive expected values by calling the verifier. Oracle and verifier may
share constants and source data, but their computational paths should be
independently reviewable.

## 3. Scientific software

For a broken simulation or analysis codebase, the oracle may apply a
human-authored patch:

```bash
#!/bin/bash
set -euo pipefail
git -C /root/project apply /oracle/reference.patch
```

The verifier should test the scientific or numerical behavior, not compare the
submitted diff with the reference patch.

## 4. Native scientific artifacts

A copy oracle is acceptable only when the deliverable is a hand-authored
artifact that cannot be reproduced faithfully in the sandbox—for example, a
CAD assembly, instrument project file, or manually annotated image.

Document why copying is more faithful than programmatic regeneration. Preserve
the artifact for human inspection and verify measurable properties
independently.

## 5. Literature-grounded answers

Freeze the evidence set with stable identifiers or a dated snapshot. The
oracle extracts or synthesizes from that snapshot; the verifier never fetches
live ground truth.

## Numerical safeguards

- Pin BLAS/OpenMP thread counts where nondeterminism matters.
- Pass random seeds to every stochastic library, not only NumPy.
- Record solver status, residuals, iteration counts, and condition numbers.
- Reject optima or roots that sit on an unexplained search boundary.
- Compare at least two resolutions when discretization error is material.
- Keep uncertainty in the verifier tolerance rather than rounding the oracle.

## Long-running workflows

Set realistic build, agent, and verifier timeouts. Emit progress during long
subprocesses so the harness does not misclassify a healthy solve as idle.

## Self-check

```bash
bench eval run \
  --tasks-dir tasks/<task-id> \
  --agent oracle \
  --sandbox docker \
  --jobs-dir jobs/<task-id>-oracle
```

Require reward `1.0`, inspect every generated artifact, and read the verifier
log before running paid agents.
