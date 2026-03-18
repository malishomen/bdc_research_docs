## Versioning

Single source of truth for versioning rules.

## Change classes
- R0 (refactor): no numerical result change; requires regression verification.
- R1 (method): changes method/metrics/thresholds; new experiment version required.
- R2 (hypothesis): changes hypothesis or kill-criteria; roadmap revision required.

## Experiment versions
- Each experiment MUST have an ID and version in `EXPERIMENT_SPEC.md`.
- Any R1 change increments the experiment version (TODO: define exact scheme).

## TRL versions
- TRL transitions require completed checklists and updated `KILL_CRITERIA.yaml`.
- Any R2 change requires a roadmap update and ADR.

UNVERIFIED/TODO: formal tag naming and SemVer mapping are not defined in sources and
must be approved before first public release.

