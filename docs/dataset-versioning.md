# Benchmark Versioning

FrontierPhysics versions immutable task snapshots independently from the
BenchFlow harness.

## Principles

1. A published task version never changes in place.
2. Any prompt, environment, skill, oracle, verifier, or input change produces a
   new content digest and benchmark version.
3. Results record the task commit, digest, harness version, agent, model, and
   skill condition.
4. No-skill and with-skill results remain separate.
5. Superseded versions stay identifiable for reproducibility.

## Version semantics

- Major: task roster changes.
- Minor: task-content fixes with the same roster.

A future release manifest should pin the Git commit and a deterministic digest
over every regular file in each task directory.
