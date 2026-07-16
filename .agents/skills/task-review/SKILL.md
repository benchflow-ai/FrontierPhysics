---
name: task-review
description: FrontierPhysics task review workflow. Use when reviewing a local task or pull request, validating scientific correctness, running oracle plus no-skill and with-skill controls, auditing trajectories, or preparing a FrontierPhysics review report.
---

# FrontierPhysics task review

Review task validity separately from model capability.

## Workflow

1. Fetch or identify the task without disturbing unrelated work.
2. Read every task file and classify it as computational, literature, or
   artifact track.
3. Run repository, structure, taxonomy, and skill checks.
4. Audit prompt, environment, oracle, verifier, provenance, and mentor skills.
5. Run the oracle.
6. Run at least one strong current agent without skills.
7. Run the same agent with skills.
8. Audit trajectories and outputs.
9. Report the no-skill result as primary and the with-skill result as control.

## Static stop conditions

Stop before expensive agent runs if:

- prompt or oracle logic is not human-authored;
- oracle emits a known answer instead of deriving it;
- task inputs, licenses, or physical assumptions lack provenance;
- Docker image exposes skills, oracle, verifier, or expected outputs;
- verifier requirements do not follow from the prompt or physical model;
- mentor skills contain hardcoded final answers or verifier internals;
- dependencies required by the task or skills are missing.

Apply [references/policy-rubric.md](references/policy-rubric.md) and
[goodtask-v2.md](goodtask-v2.md).

## Structural checks

```bash
uv run python .github/scripts/validate_repository.py
uv run python .github/scripts/validate_tasks.py tasks
uv run python .github/scripts/lint_taxonomy.py
uv run python .github/scripts/lint_skill_frontmatter.py
bench tasks check tasks/<task-id>
```

## Oracle

```bash
bench eval run \
  --tasks-dir tasks/<task-id> \
  --agent oracle \
  --sandbox docker \
  --jobs-dir jobs/<task-id>-oracle
```

Abort and request changes unless reward is `1.0`. Inspect outputs and verifier
logs, not only the scalar reward.

## Agent matrix

Verify current model identifiers from local configuration and official provider
documentation before running.

```bash
bench eval run --tasks-dir tasks/<task-id> \
  --agent <agent> --model <model> \
  --skill-mode no-skill \
  --sandbox docker \
  --jobs-dir jobs/<task-id>-no-skill

bench eval run --tasks-dir tasks/<task-id> \
  --agent <agent> --model <model> \
  --skill-mode with-skill \
  --skills-dir tasks/<task-id>/environment/skills/ \
  --sandbox docker \
  --jobs-dir jobs/<task-id>-with-skill
```

The no-skill run may fail and still be a valid benchmark result. At least one
strong agent should pass the with-skill control before approval.

## Trajectory audit

For each agent job, inspect:

- skill presence or absence as configured;
- actual skill discovery and use;
- oracle/verifier leakage or reward hacking;
- repeated commands, stalled exploration, and dependency failures;
- scientific method, assumptions, units, and numerical diagnostics;
- output artifacts, result JSON, verifier report, time, tokens, and cost.

Use [references/audit-general.md](references/audit-general.md) and
[references/audit-frontierphysics.md](references/audit-frontierphysics.md).

## Verdicts

- **Approve:** oracle passes, scientific review is sound, evidence is complete,
  and a strong agent passes with skills.
- **Approve with caveats:** minor non-scientific issues.
- **Major changes:** broken control run, brittle verifier, ambiguous prompt,
  missing provenance, or unsupported physics.
- **Reject:** contrived task, leaked answers, invalid oracle, or irreproducible
  grading.

Lead the report with no-skill pass rate. Keep the with-skill result in a
separate solvability-control column.
