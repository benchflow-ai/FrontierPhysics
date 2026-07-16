# FrontierPhysics Task Taxonomy

FrontierPhysics uses controlled metadata so results can be grouped by physics
domain, operation, modality, interface, and mentor-skill type without treating
file formats or tools as scientific domains.

## Frontmatter

```yaml
metadata:
  difficulty: hard
  category: natural-science
  subcategory: ion-trap-physics
  category_confidence: high
  task_type:
    - simulation
    - calculation
  modality:
    - scientific-data
    - 3d-model
  interface:
    - terminal
    - python
    - simulation-tool
  skill_type:
    - domain-procedure
    - mathematical-method
```

The values are enforced by [taxonomy.yaml](taxonomy.yaml).

## Fields

### `category`

The primary scientific or technical discipline needed to solve the task.
FrontierPhysics currently uses `natural-science` for physics research tasks.
The broader controlled vocabulary is retained for hybrid physical-systems,
mathematical, software, or instrumentation work.

### `subcategory`

A lowercase hyphenated specialization, such as:

- `ion-trap-physics`
- `quantum-optics`
- `condensed-matter-physics`
- `particle-physics`
- `astrophysics`
- `plasma-physics`

### `task_type`

The operations the agent performs: analysis, calculation, simulation,
optimization, generation, verification, implementation, or another value from
the controlled list.

### `modality`

The scientific inputs and outputs, such as `scientific-data`, `3d-model`,
`time-series`, `csv`, `image`, or `source-code`.

### `interface`

The execution surface: terminal, Python, simulation tool, compiler toolchain,
browser, or another controlled value.

### `skill_type`

The kind of mentor support supplied. A task may use several values. The label
describes the skill's role, not whether it is reusable across tasks.

### `difficulty`

Human specialist estimate:

- `easy`: up to about one hour;
- `medium`: roughly one to four hours;
- `hard`: more than four hours or substantial specialist work.

Model pass rate is reported separately and should not be encoded into this
field.

## Decision rules

1. Choose the scientific expert, not the artifact type.
2. Put operations in `task_type`, not `category`.
3. Put formats in `modality`, not `category`.
4. Use `secondary_category` only for a true cross-domain task.
5. Use `category_confidence: medium|low` only with a distinct
   `secondary_category`.
6. Keep `subcategory` descriptive and stable; do not encode a one-off filename.
