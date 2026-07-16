# Mentor-Skill Invocation Surfaces

FrontierPhysics uses mentor skills as a task-solvability control. The harness
must prove that task skills are absent from the primary no-skill run and
available to the paired control run.

## Required behavior

| Condition | Required harness behavior |
|---|---|
| No skill | Do not mount, copy, summarize, or name task skills in the agent context |
| With skills | Mount the selected task skill directory read-only and expose its metadata to the agent |
| Both | Keep task commit, model, reasoning settings, resources, prompt, and verifier identical |
| Evidence | Record requested mode, effective skill path, trajectory, outputs, timing, and token usage |

Skills must be injected at trial time. Baking them into the Docker image
invalidates the no-skill condition.

## Discovery signals

Different harnesses expose the same skill package through different surfaces:

| Harness pattern | Typical audit signal |
|---|---|
| Dedicated skill tool | Tool call such as `Launching skill: <name>` |
| Filesystem discovery | Read of an injected `SKILL.md` |
| Prompt catalog | Skill name or description appears only in the with-skill prompt |
| Generic ACP bridge | Read or tool-call event whose path resolves under the effective skill directory |

Do not infer skill use from reward alone. A with-skill pass may occur without
the model reading the skill, and a failed run may still have followed the
mentor recipe.

## Audit procedure

1. Read `result.json` and confirm `skill_mode`, `skill_source`, and effective
   skill path.
2. Search the no-skill trajectory for skill names, `SKILL.md`, and injected
   paths. Any successful access invalidates the run.
3. Search the with-skill trajectory for the skill tool or file reads.
4. Check whether later tool calls follow the referenced workflow, scripts, or
   diagnostics.
5. Compare outputs and verifier results under identical model settings.

Record invocation as:

- `VERIFIED`: skill loaded and the subsequent workflow reflects it;
- `PARTIAL`: skill loaded but required references or steps were skipped;
- `NOT_INVOKED`: skill was mounted but never read;
- `CONTAMINATED_NO_SKILL`: task skills were visible in the primary run.

## Report fields

```json
{
  "skill_mode": "no-skill | with-skill",
  "effective_skills_dir": null,
  "invocation": "VERIFIED | PARTIAL | NOT_INVOKED | CONTAMINATED_NO_SKILL",
  "skills_read": [],
  "evidence": ""
}
```

`CONTAMINATED_NO_SKILL` is invalid benchmark evidence. A strong-agent
with-skill failure blocks task approval until the task, environment, verifier,
or mentor guidance is corrected.
