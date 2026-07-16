# Time-Invariance in Physics Tasks

A fixed benchmark task must produce the same target interpretation when it is
run months or years later.

## Drift risks

- revised calibration files or detector conditions;
- expanding observational catalogs;
- corrected simulation datasets;
- mutable software releases and default parameters;
- literature searches without a publication cutoff;
- live mission, weather, or facility telemetry;
- web pages whose tables are edited in place.

Physical constants and published equations are usually stable, but their
recommended values, uncertainty conventions, and software implementations can
change. Pin the source and release.

## Preferred controls

1. Bundle the exact dataset, calibration, geometry, or paper snapshot.
2. Record source URL, accession or DOI, release, commit, date, and hash.
3. Name a cutoff date when the agent searches a changing literature or data
   collection.
4. Keep verifier ground truth offline.
5. Publish a new task version when the scientific inputs change.

## Prompt example

Weak:

> Compare the latest measurements of the Hubble constant.

Stable:

> Compare the measurements in the supplied source set, limited to papers
> published on or before December 31, 2025. Report each quoted uncertainty
> convention separately.

## Review check

Ask whether a correct future agent could reasonably find newer evidence and
disagree with the frozen verifier. If yes, freeze the evidence set or state the
cutoff in the prompt.
