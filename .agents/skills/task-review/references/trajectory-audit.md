# Trajectory Audit Entry Point

Read both layers for every FrontierPhysics agent run:

| Layer | File | Purpose |
|---|---|---|
| Scientific audit | [audit-general.md](audit-general.md) | condition integrity, method reconstruction, failure fairness, verifier alignment, artifacts, and behavior |
| Mentor-control audit | [audit-frontierphysics.md](audit-frontierphysics.md) | skill isolation, invocation, follow-through, and paired-run interpretation |

Produce one `audit-<config>.json` per run and a paired summary that keeps the
primary no-skill result separate from the with-skill solvability control.
