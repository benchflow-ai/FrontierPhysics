# FrontierPhysics review policy

## Static checks

### Prompt and metadata

- Human-authored.
- Physics objective, units, outputs, and constraints are clear.
- No skill names, answer hints, or grader details.
- Metadata validates against `taxonomy.yaml`.

### Data and provenance

- Real or provenance-backed inputs.
- Source repository, commit, paper, dataset, mesh, model, and licenses are
  documented where applicable.
- Mutable sources are frozen or date-anchored.

### Oracle

- Human-authored logic.
- Derives results through computation.
- Uses no hidden knowledge absent from the task or provenance.
- Runs without skills.

### Verifier

- Outcome-based and deterministic.
- Requirements follow from the prompt or physical model.
- Numerical tolerances are justified.
- Outputs and diagnostics are preserved.
- No live mutable ground truth.

### Mentor skills

- At least one skill is present.
- Task-specific recipes are allowed.
- Guidance is scientifically substantive.
- Required dependencies and assets are available.
- No hardcoded final answers, verifier internals, or oracle/verifier access.
- Skills are injected at runtime, not copied into the Docker image.

### Environment and security

- Dependencies are pinned.
- Agent image contains no answer leaks.
- No credentials, exfiltration, obfuscated code, or unauthorized calls.

## Runtime checks

1. Repository checks pass.
2. `bench tasks check` passes.
3. Oracle reward is `1.0`.
4. A strong agent is run without skills.
5. The same agent is run with skills.
6. At least one strong with-skill run passes before approval.
7. Trajectories and artifacts are audited.

## Verdict

| Verdict | Condition |
|---|---|
| Approve | Scientific review clean, oracle passes, control passes |
| Approve with caveats | Minor issues without scientific impact |
| Major changes | Broken control, brittle grading, ambiguity, or missing provenance |
| Reject | Invalid or contrived task, leaked answers, or irreproducible result |
