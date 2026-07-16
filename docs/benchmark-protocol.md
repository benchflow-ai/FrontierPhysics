# FrontierPhysics Benchmark Protocol

## Conditions

| Condition | Purpose | Leaderboard role |
|---|---|---|
| Oracle | Reference implementation and verifier control | Not ranked |
| No skill | Independent agent capability | Primary score |
| With skills | Mentor-guided solvability control | Reported separately |

Use the same task commit, sandbox backend, resource limits, agent harness, model
version, and reasoning settings when comparing no-skill and with-skill runs.

## Required evidence

Preserve:

- `result.json`;
- full trajectory JSONL;
- verifier output, CTRF report, and reward;
- task outputs and diagnostics;
- elapsed time, token counts, and cost when available;
- exact model and harness identifiers;
- skill-injection mode and skill digest.

## Interpretation

- A no-skill failure with a with-skill pass is an agent-capability signal.
- Failure in both conditions requires investigation before claiming the task is
  beyond model capability.
- A with-skill pass is not proof that the physics is correct when the mentor
  skill and oracle share assumptions. Human scientific review and provenance
  remain mandatory.
- Infrastructure failures, missing dependencies, and ambiguous instructions
  are excluded from capability claims.
