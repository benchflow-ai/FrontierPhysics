# Verifier Guidelines for FrontierPhysics Tasks

FrontierPhysics verifiers grade scientific outcomes. They do not grade which
skill, command, library, or internal implementation an agent used.

## Design

- Use roughly 4–10 focused tests.
- Combine existence, parseability, and basic structure into one artifact test.
- Parameterize repeated checks.
- Use relative and absolute tolerances for floating-point values.
- Prefer independent recomputation, physical invariants, conservation laws,
  symmetry, dimensional analysis, and robust diagnostics over exact snapshots.
- Preserve agent outputs and useful reference diagnostics under
  `/logs/verifier/`.
- Keep grading offline and deterministic.

## Numerical tasks

- Pin scientific package versions and thread counts when reproducibility
  matters.
- Choose tolerances from convergence studies or method variation, not from a
  single lucky output.
- Separate different physical effects rather than collapsing them into one
  score.
- Test units and coordinate conventions explicitly when a plausible wrong
  interpretation would otherwise pass.

## Shell entrypoint

Capture the test runner's exit code directly:

```bash
python3 -m pytest /verifier/test_outputs.py -rA -v \
  > /logs/verifier/output.txt 2>&1
RC=$?

if [ "$RC" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
exit 0
```

Do not read `$?` after a pipe to `tee`; that records the pipe's final command
rather than pytest.
