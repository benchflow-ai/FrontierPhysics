# FrontierPhysics Trajectory Audit

Audit trajectories after execution. A scalar reward is never sufficient
evidence for scientific validity or a capability claim.

For mentor-control checks, also apply
[audit-frontierphysics.md](audit-frontierphysics.md).

## Inputs

Inspect:

- `result.json`;
- full ACP or native trajectory JSONL;
- agent transcript;
- verifier output and CTRF report;
- submitted artifacts and diagnostics;
- task commit, model, harness, skill mode, timing, and token metadata.

## 1. Condition integrity

Confirm the task commit, prompt, model, reasoning settings, resources, and
verifier match across paired runs. Confirm task skills are absent from the
no-skill run.

Any successful no-skill access to injected skills, `/oracle`, `/verifier`,
expected outputs, or answer-bearing files invalidates the run.

## 2. Scientific method

Reconstruct what the agent actually did:

- physical model and approximations;
- coordinate, sign, amplitude, and unit conventions;
- algorithms, solvers, data cuts, and fit models;
- convergence and uncertainty checks;
- interpretation of the requested quantity.

Do not infer the method from the final prose when the tool trace shows
something different.

## 3. Failure classification

Classify each non-passing run:

- `capability_gap`: coherent task, fair verifier, wrong or incomplete physics;
- `task_ambiguity`: a reasonable interpretation was not specified;
- `verifier_mismatch`: scientifically acceptable output was rejected;
- `environment_failure`: dependency, permission, network, or resource failure;
- `format_only`: physical result was correct but serialization failed;
- `ignored_requirement`: agent solved a different problem;
- `provider_failure`: model or authentication failed before task execution.

Quote both the agent's relevant statement and the verifier failure.

## 4. Verifier alignment

For a failed run, compare the produced artifact with an independent
recomputation, oracle artifact, or physical invariant. Confirm the verifier's
diagnosis matches the real scientific difference.

If the task fails only because of syntax, harmless metadata, or an
implementation-specific expectation, request verifier changes.

## 5. Physical plausibility

Check domain-appropriate signals:

- dimensions and units;
- conservation laws;
- symmetry and sign;
- analytic limits and scaling;
- solver residuals and convergence;
- fit uncertainty and identifiability;
- whether an optimum or root lies on a search boundary.

A plausible-looking number without these checks may still be wrong.

## 6. Artifact integrity

Open every scientific artifact needed to interpret the result. Confirm that
plots, waveforms, meshes, tables, and images match their machine-readable
source data and are preserved under verifier logs.

## 7. Agent behavior

Record:

- tool calls by kind and title;
- input inspection before solving;
- solver rewrites and repeated commands;
- mid-run reversals;
- whether the agent verified its own output;
- filesystem or package side effects outside permitted work paths.

Struggle is evidence about model behavior, not an automatic task defect.

## 8. Memorization and public leakage

Flag immediate recognition of a public solved instance, exact answer values
without derivation, or use of a public issue/commit that contains the solution.
Do not reject solely because the agent knows a standard physical method.

## 9. Verbatim final statement

Capture the final non-empty agent message. If absent, use the last substantive
thought or solver output. This quote anchors downstream review.

## Verdict aggregation

| Condition | Review effect |
|---|---|
| Oracle reward below 1.0 | Major changes |
| Invalid condition isolation or answer leakage | Reject |
| Verifier misaligned with scientific truth | Major changes or reject |
| Strong-agent with-skill control fails | Major changes |
| No-skill run fails for a fair capability reason | Valid benchmark result |
| All controls clean | Approve |

## Audit schema

```json
{
  "config": "no-skill | with-skill",
  "model": "",
  "reward": 0.0,
  "verdict": "CLEAN | WARN | INVALID",
  "condition_integrity": {"status": "PASS", "evidence": ""},
  "scientific_method": {"summary": "", "assumptions": [], "diagnostics": []},
  "failure_class": "passed | capability_gap | task_ambiguity | verifier_mismatch | environment_failure | format_only | ignored_requirement | provider_failure",
  "verifier_alignment": {"status": "aligned | misaligned | not_checked", "evidence": ""},
  "artifact_integrity": {"status": "PASS | WARN | FAIL", "evidence": ""},
  "tool_breakdown": {"total": 0, "by_kind": {}, "by_title": {}},
  "filesystem_safety": {"status": "PASS | WARN | FAIL", "evidence": ""},
  "verbatim_final": ""
}
```
