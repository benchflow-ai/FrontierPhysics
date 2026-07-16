# Task Family: Scientific Artifacts and Multimodal Outputs

Use this family when the agent consumes or produces images, plots, spectra,
waveforms, CAD/mesh files, annotated PDFs, audio, video, or other structured
scientific artifacts.

## Requirements

- Preserve the submitted artifact under `/logs/verifier/`.
- Preserve the numerical data or metadata needed to audit it.
- Include an expected artifact or independently generated preview when useful.
- Combine programmatic decoding with human inspection.

## Verifier

Check measurable properties appropriate to the artifact:

- dimensions, sampling rate, duration, frame count, or mesh topology;
- axes, units, labels, legends, and data ranges;
- embedded metadata and provenance;
- agreement between rendered content and machine-readable source data;
- visual or signal quality only with a validated rubric.

Do not grade a scientific figure solely by pixel similarity when multiple
valid renderings exist.

## Oracle

Generate artifacts programmatically when that reflects the scientific
workflow. A copy oracle is acceptable for a manually annotated or
instrument-native artifact that cannot be reproduced faithfully; document the
trade-off.

## Common failure modes

- preserving the scalar reward but not the artifact;
- checking file existence without decoding it;
- allowing polished visuals with wrong underlying data;
- brittle hashes broken by timestamps or harmless metadata;
- visual review without a mapping to quantitative requirements.
