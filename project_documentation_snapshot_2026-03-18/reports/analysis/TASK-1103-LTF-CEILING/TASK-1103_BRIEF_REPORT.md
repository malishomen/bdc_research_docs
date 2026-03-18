# TASK-1103 BRIEF REPORT

## Scope
- Part A: computed LTF representational ceiling for Genome v1 feature family using deterministic 512-sample dataset.
- Part B: added `functional_diversity` metric to EDP1 runtime and aggregate pipeline.
- No evolution operator/fitness/selection policy changes.

## Changes
- Added `scripts/analysis/ltf_ceiling_proof.py`.
- Updated `evolution/edp1_symbolic/evaluate.py`:
  - added `prediction_vector(genome, dataset)`.
- Updated `evolution/edp1_symbolic/run_generations.py`:
  - computes `functional_diversity = unique_prediction_vectors / population_size`;
  - adds `functional_diversity` column to `metrics.csv`.
- Updated `scripts/edp1/aggregate_results.py`:
  - aggregates functional diversity into `diversity_trajectory_agg.csv`:
    - `functional_diversity_mean`
    - `functional_diversity_median`
    - `functional_diversity_ci95`

## Verification (L0)
- Ceiling proof:
  - `python scripts/analysis/ltf_ceiling_proof.py --out reports/analysis/TASK-1103-LTF-CEILING/ltf_ceiling_result.json --baseline_root results/edp1_exp0200`
  - Result: `PASS` (JSON produced).
- Functional diversity smoke:
  - `bash scripts/edp1/run_edp1_local.sh --out_dir results/edp1_exp0200_task1103_smoke --generations 20 --population 50 --seed 1337`
  - Check:
    - `functional_diversity <= 1.0` -> `PASS` (`max=0.98`)
    - `functional_diversity < diversity_index` -> `PASS` (all generations true in smoke run)
- Aggregation check on new multi-seed run:
  - `bash scripts/edp1/run_edp1_sweep.sh --seeds 5 --generations 20 --population 50 --base_seed 1337 --out_root results/edp1_exp0200_task1103_sweep --phase0_generations 10 --selection_top_pct_phase1 0.2 --mutation_rate 0.2 --diversity_shock_pct 0.2 --diversity_shock_cooldown 10 --speciation_distance_threshold 3 --max_species_fraction 0.5`
  - Result: `PASS`, aggregates produced with functional diversity fields.

## Required Results
- Theoretical max_accuracy (LTF ceiling): `0.837890625`
- Experimental max_accuracy_mean (exp0200): `0.849609375`
- Delta (theory - experiment): `-0.01171875`
- Functional diversity trajectory mean (5-seed sweep):
  - g1: `0.968`
  - g10: `0.936`
  - g20: `0.468`

## Conclusion
- **Ceiling confirmed:** `NO` (not confirmed with current dataset/method alignment).
- Observed `experimental > theoretical` indicates either:
  - dataset alignment mismatch between ceiling setup and exp0200 aggregate target, or
  - MILP formulation constraints (margin/bounds) are conservative for this proof setup.
- Functional diversity metric integration is complete and operational.

## Artifacts
- `reports/analysis/TASK-1103-LTF-CEILING/ltf_ceiling_result.json`
- `reports/analysis/TASK-1103-LTF-CEILING/TASK-1103_BRIEF_REPORT.md`
- `results/edp1_exp0200_task1103_sweep/aggregates/diversity_trajectory_agg.csv`

## Risks / Limitations
- Theoretical proof result is sensitive to exact dataset definition and MILP modeling assumptions.
- Current conclusion is explicitly `NOT CONFIRMED`, not post-hoc adjusted.

## Rollback
- Revert this task commit to remove the new metric and analysis script.
