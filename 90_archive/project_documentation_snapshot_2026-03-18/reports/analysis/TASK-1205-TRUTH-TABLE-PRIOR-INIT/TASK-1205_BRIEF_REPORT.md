# TASK-1205 BRIEF REPORT

## Scope
- Implemented prior-informed truth-table initialization for MRTN v2 only.
- Single-variable change preserved: mutation/shock/selection/speciation/kill criteria untouched.

## Changes
- `evolution/edp1_symbolic/genome.py`
  - Added constant `V2_TRUTH_TABLE_CLASS_PRIOR = 0.677734375` (from TASK-1204).
- `evolution/edp1_symbolic/mutate.py`
  - Updated v2 `random_genome()` truth-table init from `p(bit=1)=0.5` to `p(bit=1)=0.677734375`.
- `evolution/edp1_symbolic/run_generations.py`
  - Added summary field `truth_table_prior_init`.

## Verification (L0)
- Smoke run:
  - `python -m evolution.edp1_symbolic.run_generations --out_dir results/edp1_exp0200_v2_prior_smoke --genome_version v2 --generations 30 --population 50 --seed 1337`
  - Result: PASS
- Determinism replay:
  - `... --out_dir results/edp1_exp0200_v2_prior_det_a ...`
  - `... --out_dir results/edp1_exp0200_v2_prior_det_b ...`
  - `metrics.csv` identical: `True`
  - `summary.json` identical excluding `finished_at_utc/out_dir`: `True`
- Full validation:
  - Executed `N=30/G=100/P=100`, seeds `1337..1366` into `results/edp1_exp0200_v2_prior/seeds/*`.
  - Aggregated via `python scripts/edp1/aggregate_results.py --in results/edp1_exp0200_v2_prior --out results/edp1_exp0200_v2_prior/aggregates --phase0_generations 10`.

## Key Results
- `truth_table_prior_init=true` in summaries: `30/30` runs.
- Baseline v2 final max fitness mean: `0.5356865515715755`
- v2_prior final max fitness mean: `0.5531664379938884`
- Delta final max fitness mean: `+0.01747988642231288`
- Pass rate (aggregate): baseline `0.0`, v2_prior `0.0`

### Trajectory (max_fitness_mean)
- Baseline v2: gen1 `0.5475`, gen10 `0.5344`, gen25 `0.5364`, gen50 `0.5360`, gen75 `0.5309`, gen100 `0.5357`
- v2_prior: gen1 `0.5497`, gen10 `0.5434`, gen25 `0.5458`, gen50 `0.5477`, gen75 `0.5504`, gen100 `0.5532`

## Evaluation vs TASK-1205 Criteria
- `final_max_fitness_mean > 0.68`: **FAIL** (`0.5532`)
- `>=10/30 seeds with best_single_accuracy > 0.68` (proxy via per-seed final_max_fitness): **FAIL** (`0/30`)
- No descending trend vs baseline: **PASS** (upward trajectory relative to baseline)
- Strong breakthrough (`max_accuracy_mean > 0.75`): **FAIL**

## Artifacts
- `results/edp1_exp0200_v2_prior/aggregates/metrics_agg.csv`
- `reports/analysis/TASK-1205-TRUTH-TABLE-PRIOR-INIT/comparison_vs_v2_baseline.json`
- `reports/analysis/TASK-1205-TRUTH-TABLE-PRIOR-INIT/TASK-1205_BRIEF_REPORT.md`

## Conclusion
- Prior-informed truth-table init improved MRTN v2 fitness trajectory and final aggregate fitness, but did not break through the trivial-attractor regime to the requested threshold band.
