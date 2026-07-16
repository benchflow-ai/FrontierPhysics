# FrontierPhysics Review Tracks

Classify the task before applying track-specific review checks.

## Computational track

Default for simulations, derivations, fitting, numerical inference,
optimization, scientific data analysis, and scientific software.

Requirements:

- frozen inputs and pinned dependencies;
- deterministic or bounded stochastic behavior;
- justified numerical tolerance;
- independent recomputation or physical invariants;
- convergence and diagnostic evidence where material.

## Literature track

Use when source discovery, paper comparison, or evidence synthesis is the core
work.

Requirements:

- stable identifiers or a frozen evidence snapshot;
- publication or data cutoff when the source set changes;
- no live verifier ground truth;
- explicit claim-to-source support;
- separate treatment of units, methods, and uncertainty conventions.

## Artifact track

Use when the output is a plot, image, waveform, mesh, CAD file, annotated
document, audio/video record, or other scientific artifact requiring human
inspection.

Requirements:

- preserve the submitted artifact and its machine-readable source data;
- decode and test measurable structure;
- inspect the artifact manually;
- avoid byte-level equality when multiple valid renderings exist;
- document any copy-oracle trade-off.

## Recording the track

Use:

```json
{
  "track": "computational | literature | artifact",
  "track_signals": []
}
```

Hybrid tasks should use the track that determines the hardest verification
problem, then apply the relevant checks from the other track as addenda.
