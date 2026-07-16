# FrontierPhysics

[![Discord](https://img.shields.io/badge/Discord-Join-7289da?logo=discord&logoColor=white)](https://discord.gg/G9dg3EfSva)
[![GitHub](https://img.shields.io/github/stars/benchflow-ai/FrontierPhysics?style=social)](https://github.com/benchflow-ai/FrontierPhysics)

FrontierPhysics is a public benchmark for evaluating AI agents on advanced
physics research workflows. It uses native
[BenchFlow](https://github.com/benchflow-ai/benchflow) task packages and keeps
the benchmark, reference solution, verifier, and optional mentor skills
reviewable in one repository.

## Benchmark design

FrontierPhysics reports two conditions:

- **Without skills — primary benchmark condition.** This pass rate measures
  what an agent can solve from the task, environment, tools, and public
  internet access alone.
- **With skills — solvability control.** Every task ships reviewable mentor
  guidance that may be task-specific and procedural. This condition checks
  that a capable agent can complete the task when given a sound research
  recipe, helping separate task defects from model capability limits.

Mentor skills may include step-by-step guidance, references, scripts, and
derived intermediate assets. They must not contain hardcoded final answers,
verifier internals, or a bypass around the requested scientific work.

## Quick start

```bash
git clone https://github.com/benchflow-ai/FrontierPhysics.git
cd FrontierPhysics

uv tool install "benchflow>=0.6.2,<0.7"
uv sync --locked

bench tasks check tasks/surface-ion-trap-shuttling
bench eval run \
  --tasks-dir tasks/surface-ion-trap-shuttling \
  --agent oracle \
  --sandbox docker
```

Run an agent without skills:

```bash
bench eval run \
  --tasks-dir tasks/surface-ion-trap-shuttling \
  --agent codex-acp \
  --model <model> \
  --skill-mode no-skill \
  --sandbox docker
```

Run the same agent with the task's mentor skills:

```bash
bench eval run \
  --tasks-dir tasks/surface-ion-trap-shuttling \
  --agent codex-acp \
  --model <model> \
  --skill-mode with-skill \
  --skills-dir tasks/surface-ion-trap-shuttling/environment/skills/ \
  --sandbox docker
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for task requirements and
[MAINTAINER.md](MAINTAINER.md) for the review protocol. The imported
infrastructure and intentional exclusions are documented in
[docs/repository-scope.md](docs/repository-scope.md).

## License and provenance

Repository documentation and original code are licensed under
[Apache 2.0](LICENSE). Bundled third-party components retain their own license
files. See [NOTICE](NOTICE) and each task's provenance records.
