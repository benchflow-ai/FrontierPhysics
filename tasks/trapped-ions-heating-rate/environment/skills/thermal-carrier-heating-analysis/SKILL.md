---
name: thermal-carrier-heating-analysis
description: Analyze nine-ion 40Ca+ carrier Rabi-flop HDF5 traces to infer COM-mode thermal occupations and a heating rate, including notebook-matched tail cuts, Gaussian-beam intensity averaging, covariance diagnostics, and unit conversion. Use for the trapped-ions-heating-rate task and similarly structured multi-delay carrier-thermometry data.
---

# Thermal-carrier heating analysis

Use the recorded fluorescence traces to fit the thermal carrier model; do not estimate occupations from oscillation envelopes by eye.

## Run the deterministic analysis

Locate this injected skill and run its parameterized helper:

```bash
SKILL_DIR="$(find -L /home/agent /root \
  -path '*/thermal-carrier-heating-analysis/SKILL.md' -print -quit 2>/dev/null \
  | xargs dirname)"
test -n "$SKILL_DIR"

python3 "$SKILL_DIR/scripts/analyze_heating.py" \
  --data-dir /root/data \
  --output /root/result.md \
  --diagnostics /root/fit_diagnostics.json
```

The helper loads the four HDF5 files, performs the physical fits, propagates fit covariance into diagnostics, and writes the five raw numbers requested by the task.

Read [references/model.md](references/model.md) to audit the model, preprocessing, uncertainty treatment, and units.

## Final checks

- `result.md` has exactly five non-empty lines and no labels.
- The first four values are non-negative mean occupations.
- The fifth value is positive and is in quanta/s, not quanta/ms.
- Inspect `fit_diagnostics.json` for fit convergence, parameter standard errors, and residual RMSE before finishing.
