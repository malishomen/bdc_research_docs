# EXP-0600A: GPU Robustness Addendum (2026-03-05)

## Background
- This addendum documents robustness and reproducibility controls for the Phase-4 applied GPU profile.
- Scientific Phase-4 verdict remains unchanged: `RUN COMPLETE / GATE FAIL`.

## Reference Profile
- `profile_id: gpu_profile_v4_reference`
- Locked file: `configs/profiles/gpu_profile_v4_reference.yaml`
- Parameters:
  - `batch_size=8`
  - `steps=120`
  - `lr=3e-5`
  - `AMP=on`
  - `fp32_critical=on`
  - `clip=1`

## Robustness Metrics
- Pipeline now exports `reports/metrics.json` with:
  - `mean_delta`
  - `ci95_low`
  - `ci95_high`
  - `negative_seed_rate`
  - `negative_seeds`
- `negative_seed_rate = N_negative / N` where `N_negative = count(delta < 0)`.

## Forensic Scope
- Negative seeds are analyzed from gate aggregates and stored as:
  - `analysis/seed_forensics/seed_<id>.json`
  - `reports/seed_failure_analysis.md`
- For each seed:
  - loss trajectory,
  - gradient norm trajectory,
  - learning-rate trajectory,
  - deterministic batch-order windows,
  - logits magnitude diagnostics.

## Search Space Declaration
- Predeclared profile space is fixed in `docs/profile_search_space.md`.
- The selected reference profile is explicitly tagged as chosen from this predeclared space.

## Reproducibility
- Repro sweep artifact root:
  - `results/repro_run/`
- Required artifacts:
  - `per_seed_metrics.csv`
  - `aggregate_metrics.json`
  - `CI_report.md`
