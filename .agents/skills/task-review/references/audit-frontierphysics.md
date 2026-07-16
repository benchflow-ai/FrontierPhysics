# Trajectory audit — FrontierPhysics control layer

Apply these checks on top of `audit-general.md`.

## Skill injection

Confirm the with-skill job actually exposed and loaded at least one task skill,
and the no-skill job did not.

Common signals:

| Harness | Signal |
|---|---|
| Claude ACP | `Skill` tool call with `Launching skill: ...` |
| Codex ACP | read of a `SKILL.md` under an injected skills path |
| Generic ACP | read of `**/skills/**/SKILL.md` |

Record:

- `VERIFIED`: skill loaded and later actions reflect it;
- `PARTIAL`: top-level skill read but linked references/scripts ignored;
- `NOT_INVOKED`: skill was mounted but never read;
- `CONTAMINATED_NO_SKILL`: any task skill visible in a no-skill run.

`CONTAMINATED_NO_SKILL` invalidates the primary benchmark run.

## Solvability control

Compare the same agent, model, reasoning settings, task commit, and sandbox
under no-skill and with-skill conditions.

The important questions are:

1. Did the with-skill run pass?
2. Which mentor step unlocked the solution?
3. If it failed, was the cause scientific reasoning, missing guidance,
   dependency setup, instructions, or verifier behavior?
4. Did the skill reveal an answer instead of coaching the computation?

A strong-agent with-skill failure blocks approval until investigated. A
no-skill failure does not.

## Mentor-skill misuse

Flag:

- reading only `SKILL.md` while ignoring required references or scripts;
- following only part of the recipe;
- changing units or conventions contrary to the skill;
- copying fixed values without computation;
- using a helper outside its stated parameter or convergence range.

## Cross-run report

Store a control comparison in `summary.json`:

```json
{
  "primary_no_skill": {
    "reward": 0.0,
    "failure_class": "capability"
  },
  "solvability_control": {
    "reward": 1.0,
    "skill_invocation": "VERIFIED",
    "unlock_evidence": "..."
  }
}
```

Do not merge the two rewards into one score.

## Approval effect

| Pattern | Effect |
|---|---|
| No-skill fails, with-skill passes cleanly | Valid capability result |
| Both pass | Valid but easier task for this model |
| No-skill passes, with-skill fails | Investigate harmful or broken skill; blocks approval |
| Both fail | Investigate task, environment, verifier, and mentor recipe; blocks approval |
| No-skill sees task skills | Invalid primary run |
