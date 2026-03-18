# TASK-1300 BRIEF REPORT

## Scope
- Implemented `genome_version=v1_5` as minimal extension of v1 with 3 interaction terms.
- Kept fitness formula and complexity lambda unchanged.
- Reused v1 mutation/speciation/shock flow.

## Changes
- `evolution/edp1_symbolic/genome.py`
  - Added `RuleGenomeV1_5` with new weights:
    - `w_gate_pattern`
    - `w_first_last`
    - `w_pos3_pos7`
  - Added interaction features:
    - `f_gate_pattern = f_gate * f_pattern_101`
    - `f_first_last = f_first_bit * f_last_bit`
    - `f_pos3_pos7 = f_pos3 * f_pos7`
  - Complexity remains `sum(abs(weights)) + threshold_count/16` (no normalization change).
- `evolution/edp1_symbolic/mutate.py`
  - Added `random_genome(..., genome_version='v1_5')`
  - Added Gaussian mutation branch for `RuleGenomeV1_5` (same style as v1)
- `evolution/edp1_symbolic/speciation.py`
  - Added v1.5-aware distance including interaction weights.
- `evolution/edp1_symbolic/run_generations.py`
  - Added CLI support: `--genome_version v1_5`.
- `scripts/edp1/run_edp1_sweep.sh`
  - Updated CLI help to `v1|v1_5|v2`.

## Verification
- Smoke:
  - `python -m evolution.edp1_symbolic.run_generations --out_dir results/edp1_exp0200_v1_5_smoke --genome_version v1_5 --generations 20 --population 50 --seed 1337` -> PASS
- Determinism replay:
  - same command to `..._replay` -> `metrics.csv` identical, `summary.json` identical excluding time/path.
- Full validation:
  - `bash scripts/edp1/run_edp1_sweep.sh --seeds 30 --generations 100 --population 100 --base_seed 1337 --out_root results/edp1_exp0200_v1_5 --genome_version v1_5` -> PASS

## Results (N=30, G=100, P=100)
From `results/edp1_exp0200_v1_5/aggregates/metrics_agg.csv`:
- `final_max_accuracy_mean = 0.8117838541666667`
- `final_max_fitness_mean = 0.7637578865767252`
- `final_mean_accuracy_mean = 0.5864765625`
- `final_mean_fitness_mean = 0.5051887468064893`
- `final_max_penalty_mean = 0.13950665321506295`
- `final_max_complexity_mean = 13.950665321506293`

Additional criterion check:
- `>=10/30 seeds with best_single_accuracy > 0.85` -> `2/30` (FAIL)

## Success Criteria Evaluation
- `final_max_accuracy_mean > 0.85` -> FAIL
- `final_max_fitness_mean > 0.79` -> FAIL
- `>=10/30 seeds with best_single_accuracy > 0.85` -> FAIL
- Failure condition `final_max_accuracy_mean <= 0.84` -> TRIGGERED

## Status
- `FAIL` (method implemented correctly, target performance criteria not met).

## Artifacts
- `reports/analysis/TASK-1300-GENOME-V1_5/TASK-1300_BRIEF_REPORT.md`
- `results/edp1_exp0200_v1_5/aggregates/metrics_agg.csv`
