# Prompt Guidelines for FrontierPhysics Tasks

The prompt body in `task.md` is the only user message the evaluated agent
receives. Write it as a concise research brief for a capable colleague.

## Required qualities

1. State the physical problem and requested outputs.
2. Use explicit absolute paths for all inputs and outputs.
3. Specify units, conventions, boundary conditions, and required precision or
   sampling shape.
4. Describe the end state without revealing the mentor-skill recipe.
5. Make every verifier requirement traceable to the prompt, supplied source,
   or standard domain convention.
6. Freeze mutable data or provide a cutoff date.

## Avoid

- naming or directing the agent to a skill;
- disclosing verifier thresholds or expected numbers;
- prescribing a specific command when multiple scientific implementations are
  valid;
- adding ambiguity to make the task artificially hard;
- testing formatting details that are not scientifically meaningful.

## Checklist

- [ ] Human-authored.
- [ ] Physical objective is clear.
- [ ] Inputs and outputs use absolute paths.
- [ ] Units and coordinate conventions are defined.
- [ ] Artifact schemas and sample counts are explicit.
- [ ] No skill names, answer hints, or hidden grader details.
