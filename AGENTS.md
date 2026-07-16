# FrontierPhysics

Public benchmark for advanced physics research tasks. The primary metric is
agent pass rate without skills; the with-skills condition is a solvability
control.

## Commands

```bash
uv tool install --upgrade benchflow
uv sync --locked
bench tasks check tasks/surface-ion-trap-shuttling
bench eval run --tasks-dir tasks/surface-ion-trap-shuttling --agent oracle --sandbox docker
bench eval run --tasks-dir tasks/surface-ion-trap-shuttling --agent codex-acp --model <model> --skill-mode no-skill --sandbox docker
bench eval run --tasks-dir tasks/surface-ion-trap-shuttling --agent codex-acp --model <model> --skill-mode with-skill --skills-dir tasks/surface-ion-trap-shuttling/environment/skills/ --sandbox docker
uv run python .github/scripts/validate_repository.py
uv run python .github/scripts/validate_tasks.py tasks
uv run python .github/scripts/lint_taxonomy.py
uv run python .github/scripts/lint_skill_frontmatter.py
uv run python .github/scripts/lint_frontierphysics_docs.py
```

## Task layout

```text
tasks/<task-id>/
  task.md
  environment/
    Dockerfile
    skills/
  oracle/
    solve.sh
  verifier/
    test.sh
    test_outputs.py
```

## Rules

- Tasks must represent authentic advanced-physics work and preserve source
  provenance.
- `task.md` prompt bodies and oracle logic must be human-authored.
- Prompts describe outcomes and must not mention skill names.
- Verifiers check scientific outcomes, not which tools or skills were used.
- Every submitted task includes one or more mentor skills.
- Mentor skills may be task-specific, prescriptive recipes.
- Mentor skills may bundle scripts, references, and derived intermediate
  assets, but must not hardcode final answers, expose verifier assertions, or
  bypass the requested scientific computation.
- Oracle must pass with reward `1.0`.
- At least one strong current agent must be shown to solve the task with skills
  before merge. No-skill failures are benchmark results, not automatic task
  failures.
- Keep primary reporting centered on no-skill pass rate. Report with-skill
  results separately as a control.

## References

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [MAINTAINER.md](MAINTAINER.md)
- [docs/benchmark-protocol.md](docs/benchmark-protocol.md)
- [taxonomy.md](taxonomy.md)
- [.agents/skills/task-review/](.agents/skills/task-review/)
