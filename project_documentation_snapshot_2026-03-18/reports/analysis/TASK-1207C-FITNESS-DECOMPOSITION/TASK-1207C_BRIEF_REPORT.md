# TASK-1207C BRIEF REPORT

## Scope
- Added explicit fitness decomposition columns to runtime `metrics.csv`.
- Extended aggregation outputs with final accuracy/penalty/complexity means.

## Changes
- `evolution/edp1_symbolic/run_generations.py`
  - Added runtime columns:
    - `mean_complexity`, `max_complexity`
    - `mean_penalty`, `max_penalty`
  - Added decomposition sanity check per individual:
    - `fitness ~= accuracy - complexity_penalty` (eps `1e-12`)
- `scripts/edp1/aggregate_results.py`
  - Added aggregate fields:
    - `final_max_accuracy_mean`, `final_mean_accuracy_mean`
    - `final_max_complexity_mean`, `final_mean_complexity_mean`
    - `final_max_penalty_mean`, `final_mean_penalty_mean`
  - Added trajectory fields in `fitness_trajectory_agg.csv` for accuracy and decomposition metrics.

## Verification
- Smoke sweep (3 seeds):
  - `bash scripts/edp1/run_edp1_sweep.sh --seeds 3 --generations 20 --population 50 --genome_version v2 --base_seed 2500 --out_root results/edp1_exp0200_task1207c_smoke` -> PASS
- Column presence check on `seed_2500/metrics.csv`:
  - `max_accuracy`, `mean_accuracy`, `max_complexity`, `mean_complexity`, `max_penalty`, `mean_penalty` -> present
- Aggregation smoke:
  - generated `results/edp1_exp0200_task1207c_smoke/aggregates/metrics_agg.csv` with new fields -> PASS

## Comparison table (accuracy gap vs penalty gap)
- Produced `reports/analysis/TASK-1207C-FITNESS-DECOMPOSITION/comparison_accuracy_penalty_gap.json`.
- For historical runs (`v2_prior`/`v2_staged`), penalty/complexity columns were absent at runtime, so penalty gaps are `NaN` (UNVERIFIED) by design.

## Status
- Phase C implementation: **PASS**
- Historical decomposition backfill: **UNVERIFIED** (not recomputed by policy).
