---
name: frontierphysics
description: FrontierPhysics contribution and evaluation workflow. Use when creating, reviewing, validating, or benchmarking advanced physics task packages in benchflow-ai/FrontierPhysics.
---

# FrontierPhysics

FrontierPhysics is a no-skill-first benchmark for advanced physics research
workflows.

## Core distinction

- No skill: primary capability score.
- With skills: mentor-guided solvability control.
- Oracle: reference and verifier control.

Every task includes mentor skills. They may be task-specific and
step-by-step, but may not hardcode final answers or expose verifier internals.

## Workflow

```bash
uv tool install "benchflow>=0.6.2,<0.7"
uv sync --locked

python3 .github/scripts/validate_repository.py
bench tasks check tasks/<task-id>
bench eval run --tasks-dir tasks/<task-id> --agent oracle --sandbox docker

bench eval run --tasks-dir tasks/<task-id> \
  --agent <agent> --model <model> \
  --skill-mode no-skill --sandbox docker

bench eval run --tasks-dir tasks/<task-id> \
  --agent <agent> --model <model> \
  --skill-mode with-skill \
  --skills-dir tasks/<task-id>/environment/skills/ \
  --sandbox docker
```

Read [CONTRIBUTING.md](../../../CONTRIBUTING.md) and invoke the sibling
`task-review` skill before submission.
