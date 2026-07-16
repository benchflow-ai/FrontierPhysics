---
name: task-creator
description: FrontierPhysics task authoring workflow. Use when converting an advanced physics research problem into a native BenchFlow task package, writing mentor skills, building a scientific oracle/verifier, or preparing a FrontierPhysics pull request.
---

# FrontierPhysics task authoring

Produce a runnable task under `tasks/<task-id>/` plus evidence for a reviewed
pull request.

## Workflow

1. Propose the authentic physics workflow, practitioner, inputs, outputs, and
   verification plan.
2. Scaffold a native BenchFlow task package.
3. Preserve or write the human-authored prompt.
4. Build a reproducible environment with frozen inputs.
5. Write outcome-based, tolerance-aware tests.
6. Write a human-authored oracle that derives the result.
7. Add one or more mentor skills.
8. Validate structure and run the oracle.
9. Run a strong agent without skills and with skills.
10. Audit trajectories and submit a PR.

## Package

```text
tasks/<task-id>/
├── task.md
├── environment/
│   ├── Dockerfile
│   ├── <inputs>
│   └── skills/
├── oracle/
│   └── solve.sh
└── verifier/
    ├── test.sh
    └── test_outputs.py
```

## Prompt

- Human-authored.
- State the physical objective, artifacts, units, conventions, and constraints.
- Use absolute paths.
- Do not mention skill names or grader details.
- Describe the outcome rather than the mentor recipe.
- Anchor mutable data to an immutable snapshot or cutoff date.

## Environment

- Prefer `python:3.12-slim`.
- Pin Python dependencies.
- Bundle stable scientific inputs and provenance.
- Pre-create `/app` and agent home directories.
- Never copy skills, oracle, verifier, expected outputs, or answer keys into the
  image.

## Verifier

- Use roughly 4–10 distinct tests.
- Check physical outcomes and durable artifacts.
- Use tolerance bands derived from numerical convergence or legitimate method
  variation.
- Preserve outputs and diagnostics under `/logs/verifier/`.
- Capture pytest's exit code directly.
- Keep grading offline.

Read [references/test-design.md](references/test-design.md) and the relevant
task-family guide:

- [computational and numerical physics](references/tasktype-scientific.md);
- [scientific software](references/tasktype-code.md);
- [experimental systems, controls, and HPC](references/tasktype-infrastructure.md);
- [literature-grounded research](references/tasktype-research.md);
- [scientific artifacts and multimodal outputs](references/tasktype-multimodal.md).

## Oracle

The oracle must be human-authored and derive the result through a legitimate
scientific workflow. It runs without skills. Record the provenance of papers,
data, meshes, source repositories, commits, models, and constants.

## Mentor skills

Every task includes at least one mentor skill. FrontierPhysics intentionally
allows task-specific coaching.

A good mentor skill may:

- provide an ordered expert recipe;
- explain equations, units, boundary conditions, and diagnostics;
- identify exact software setup steps;
- bundle parameterized scripts for fragile scientific operations;
- bundle references and derived intermediate assets.

It must not:

- contain hardcoded final answers;
- copy verifier assertions or hidden tolerances;
- direct the agent to `/oracle` or `/verifier`;
- merely emit accepted output files without doing the requested computation;
- be baked into the Docker image.

Use the sibling `skill-creator` guidance for structure. Prefer concise
`SKILL.md` instructions with detailed equations in `references/`, deterministic
helpers in `scripts/`, and non-text resources in `assets/`.

## Validation

```bash
uv run python .github/scripts/validate_repository.py
uv run python .github/scripts/validate_tasks.py tasks
uv run python .github/scripts/lint_taxonomy.py
uv run python .github/scripts/lint_skill_frontmatter.py
bench tasks check tasks/<task-id>
bench eval run \
  --tasks-dir tasks/<task-id> \
  --agent oracle \
  --sandbox docker \
  --jobs-dir jobs/<task-id>-oracle
```

Oracle reward must be `1.0`.

## Agent conditions

Run the same strong current model and settings in both conditions:

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

No-skill pass rate is the benchmark result. The with-skill run is a control and
should pass for at least one strong agent before merge. If it does not, inspect
the task, dependencies, mentor recipe, verifier, and trajectory before claiming
the task exceeds agent capability.

## Submission

The PR must include:

- motivation and physics provenance;
- oracle reward and verifier summary;
- no-skill result;
- with-skill control result;
- exact agent/model/reasoning settings;
- trajectory-based failure analysis;
- preserved scientific artifacts.

Invoke the sibling `task-review` skill as a final self-review.
