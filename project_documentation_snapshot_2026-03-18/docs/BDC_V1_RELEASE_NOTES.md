# BDC Designer v1 Release Candidate Notes

## Release
- Version: `1.0.0`
- Tag: `bdc-designer-v1.0.0-rc1`
- Status: release candidate for pilot distribution

## Stable Entrypoints
- `bdc-designer` (package script entrypoint)
- `python tools/bdc_designer_cli.py` (backward-compatible launcher)

## Included Assets
- Release-ready CLI package metadata (`pyproject.toml`)
- Windows launchers (`.bat` + `.ps1`)
- Installation docs and onboarding docs
- Real-task validation suite and public casebook artifacts

## Scope Freeze (Restricted BDC v1)
- Supported:
  - causal-equilibrium-guided architecture priors
  - strategy-mode recommendation for hybrid design workflows
  - caution-flag exposure and bounded decision support
- Explicitly not claimed:
  - universal optimizer behavior
  - universal portable transition-law guarantees
  - guaranteed dominance across all tasks and environments

## Integrity and Reproducibility
- Artifact checksums are recorded in `results/release_candidate/artifact_checksums.csv`.
- Release manifest and scope freeze are recorded in `results/release_candidate/`.
