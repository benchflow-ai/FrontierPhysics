# Principles for high-quality FrontierPhysics tasks

## Authentic physics work

The task should preserve a real research or engineering operation: modeling,
simulation, inference, data reduction, control design, derivation, numerical
analysis, or scientific artifact production. Difficulty should come from the
physics and workflow, not vague instructions or clerical burden.

Use real or provenance-backed data, geometry, code, papers, and experimental
artifacts whenever available.

## Clear objective

Brief a capable colleague. State outputs, units, conventions, constraints, and
sources. Do not reveal the mentor recipe, skill names, answer values, or grader
details.

Every verifier assertion must trace to the prompt, supplied source, documented
physical model, or a standard convention that a domain expert would infer.

## Verifiable and time-invariant

Prefer deterministic local verification. Freeze mutable inputs. Use stable
identifiers and provenance. Grade scientific outcomes with:

- independent recomputation;
- tolerance bands;
- physical invariants;
- symmetry and conservation checks;
- artifact structure and diagnostics.

Avoid live verifier APIs and exact floating-point equality.

## Solvable and oracle-grounded

The human-authored oracle derives the result through a legitimate workflow. It
must not bare-echo answers, rely on hidden assumptions, or copy accepted values
from the verifier.

The oracle passing proves harness consistency, not scientific truth. Reviewers
must still inspect equations, assumptions, units, convergence, provenance, and
artifacts.

## Environment-safe

Each trial starts clean. Pin dependencies, bundle stable inputs, and document
resources. Do not expose skills in no-skill runs. Do not expose `/oracle`,
`/verifier`, expected outputs, task-specific answer keys, or prior solved Git
history to the agent.

## Anti-cheat robust

Assume the agent explores its environment. Check for leaked answers, public
solution breadcrumbs, fake wrappers, monkey-patching, cached outputs, and
verifier interference.

## Mentor-skill control

Every task includes one or more mentor skills. The skill may be tailored to the
task and may include:

- an ordered research recipe;
- detailed domain references;
- exact setup and diagnostic guidance;
- parameterized helper scripts;
- derived intermediate assets.

The skill must remain reviewable and computational. It must not:

- hardcode final answer values;
- copy verifier logic or hidden tolerances;
- emit accepted artifacts without performing the requested work;
- tell the agent to inspect oracle or verifier files.

At least one strong agent should pass with the skill. A no-skill failure paired
with a clean with-skill pass is a useful capability result.

## Reviewable evidence

Preserve result JSON, trajectories, verifier reports, outputs, diagnostics,
time, token/cost metadata, task commit, model identifier, reasoning settings,
and skill mode. A scalar reward alone is insufficient.

## Reviewer questions

1. What real physics work does this represent?
2. Are the source data and assumptions authentic and documented?
3. Does every test follow from the task or physical model?
4. Could a valid alternative method pass?
5. Could the agent obtain the answer without solving the task?
6. Does the oracle independently derive the result?
7. Are tolerances justified by convergence or method variation?
8. Does the mentor skill coach rather than reveal?
9. Does a strong agent pass the with-skill control?
10. Are no-skill failures capability failures rather than infrastructure bugs?
