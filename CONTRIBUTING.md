# Contributing to FrontierPhysics

FrontierPhysics evaluates whether AI agents can complete advanced physics
research workflows. The benchmark's primary result is performance without
skills. Every task also includes a reviewable mentor-skill condition that
serves as a solvability control.

## Submission contract

Each task is a native BenchFlow package:

```text
tasks/<task-id>/
├── task.md
├── environment/
│   ├── Dockerfile
│   ├── <frozen inputs>
│   └── skills/
│       └── <mentor-skill>/
│           ├── SKILL.md
│           ├── references/
│           ├── scripts/
│           └── assets/
├── oracle/
│   └── solve.sh
└── verifier/
    ├── test.sh
    └── test_outputs.py
```

The public repository currently contains exactly one task,
`surface-ion-trap-shuttling`. Do not copy another benchmark's task corpus into
this repository.

## What FrontierPhysics measures

Run and report both conditions:

1. **No skill:** the primary benchmark score. This measures the agent's
   independent scientific reasoning, coding, tool use, and research ability.
2. **With skills:** a control condition. This checks whether a strong agent can
   solve the task with expert coaching and helps detect broken instructions,
   dependencies, reference answers, or verifier assumptions.

A task may remain valuable when all tested agents fail without skills. It is
not ready to merge when the oracle fails, the verifier is unfair, or capable
agents still cannot solve it with an accurate mentor skill.

## Mentor skills

Every submission must include at least one skill under
`environment/skills/`.

FrontierPhysics does not require skills to generalize beyond the submitted
task. A skill may act like a senior researcher mentoring a student or intern:

- give an ordered research recipe;
- explain non-obvious equations, units, conventions, and diagnostics;
- identify appropriate software and exact setup steps;
- bundle reviewable scripts for fragile numerical operations;
- bundle references or derived intermediate assets needed to make the recipe
  practical.

The following remain prohibited:

- hardcoded final answers or expected result files;
- copies of verifier assertions or hidden tolerances;
- instructions to read `/oracle` or `/verifier`;
- scripts that simply emit the accepted output without performing the stated
  scientific computation;
- baked skills in the Docker image, which would contaminate no-skill runs.

Task-specific helper code may overlap conceptually with the oracle, but it must
remain inspectable, parameterized, and computational. Reviewers should be able
to explain why the skill is scientifically sound without trusting the
verifier.

## Task requirements

### Prompt

- Human-authored, clear, and outcome-focused.
- Explicit absolute paths for every input and output.
- No skill names or directions to use a skill.
- No hidden requirements that appear only in tests.
- Frozen inputs or an explicit time cutoff for mutable sources.

### Environment

- Python 3.12+ unless the task documents a justified exception.
- Pin Python packages to exact versions.
- Bundle reproducible scientific inputs.
- Do not copy skills, oracle files, verifier files, or answer keys into the
  agent image.

### Oracle

- Human-authored reference workflow.
- Derive outputs through scientific computation.
- Run without injected skills.
- Preserve provenance for source data, meshes, models, papers, and code.

### Verifier

- Check outcomes and scientifically meaningful artifacts.
- Prefer tolerance-banded numerical checks over exact floating-point equality.
- Keep tests deterministic and independent of live APIs.
- Copy outputs and useful diagnostics to `/logs/verifier/`.
- Do not test whether a particular skill, command, or package was used.

## Required evaluation

Before opening a PR:

```bash
bench tasks check tasks/<task-id>
bench eval run --tasks-dir tasks/<task-id> --agent oracle --sandbox docker
```

Then run at least one strong current agent in both conditions:

```bash
bench eval run --tasks-dir tasks/<task-id> \
  --agent <agent> --model <model> \
  --skill-mode no-skill --sandbox docker

bench eval run --tasks-dir tasks/<task-id> \
  --agent <agent> --model <model> \
  --skill-mode with-skill \
  --skills-dir tasks/<task-id>/environment/skills/ \
  --sandbox docker
```

The PR must include:

- oracle reward and verifier summary;
- no-skill pass rate, with model and reasoning settings;
- with-skill pass rate as the control;
- trajectory-based failure analysis;
- output artifacts or visual previews when applicable;
- source and license provenance.

## Review bar

A merge-ready task is:

- authentic advanced physics work;
- difficult because of physics, modeling, research judgment, or scientific
  tooling rather than ambiguity;
- deterministic enough to grade fairly;
- oracle-grounded and anti-cheat aware;
- independently hard in the no-skill condition;
- demonstrably solvable in the with-skill control condition.

See [MAINTAINER.md](MAINTAINER.md) and the
[task-review skill](.agents/skills/task-review/) for the full workflow.
