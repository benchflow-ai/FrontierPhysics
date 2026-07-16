# Harness Guidance

FrontierPhysics compares the same agent and model under two isolated
conditions: no skill and with skills. Harness integrations must preserve that
separation and record enough evidence to audit it.

- [Skill invocation surfaces](skill-invocation-surfaces.md) explains discovery,
  isolation, and trajectory evidence across agent harnesses.

Harness-specific implementation details may change. Benchmark reports should
record the harness version, model identifier, skill mode, effective skill
directory, and task commit used by each run.
