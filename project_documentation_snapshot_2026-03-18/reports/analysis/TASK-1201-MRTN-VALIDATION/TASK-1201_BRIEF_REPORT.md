# TASK-1201 BRIEF REPORT

## Scope
- Полная валидация Genome v2 (MRTN) на конфигурации `N=30 / G=100 / P=100`.
- Параметры запуска синхронизированы с v1 baseline (`mutation_rate=0.2`, shock/speciation включены, тот же seed диапазон `1337..1366`).
- Сравнение с v1 baseline из `results/edp1_exp0200_speciation`.

## Run Config (L0)
- Command family:
  - `python -m evolution.edp1_symbolic.run_generations --genome_version v2 --generations 100 --population 100 --seed <1337..1366> --phase0_min_generations 10 --selection_top_pct_phase1 0.2 --mutation_rate 0.2 --diversity_shock_pct 0.2 --diversity_shock_cooldown 10 --speciation_distance_threshold 3 --max_species_fraction 0.5`
- Output root:
  - `results/edp1_exp0200_v2/seeds/seed_<seed>/`
- Aggregation:
  - `python scripts/edp1/aggregate_results.py --in results/edp1_exp0200_v2 --out results/edp1_exp0200_v2/aggregates --phase0_generations 10`

## Required Metrics
- `pass_rate` (aggregator): `0.0`
- `max_accuracy_mean` (mean of per-seed max accuracy): `0.8117838541666667`
- `best_single_accuracy`: `0.861328125` (seed `1340`, generation `8`)
- `functional_diversity` (final mean): `0.9906666666666664`
- `species_count` (final mean): `100.0`
- `largest_species_fraction` (final mean): `0.010000000000000004`
- `plateau_generation_mean`: `null` (в `summary.json` нет plateau-kill по v2 run)

## Success Criteria Evaluation
- `pass_rate_gt_0`: **FAIL** (`0.0`)
- `max_accuracy_mean_gt_0_85`: **FAIL** (`0.81178`)
- `best_single_accuracy_gt_theoretical_LTF_ceiling`: **PASS** (`0.86133 > 0.837890625`)

Итог по criteria set: **FAIL** (2/3 критериев не выполнены).

## v1 vs v2 Comparison
- v1 (`results/edp1_exp0200_speciation`):
  - `pass_rate=0.0`
  - `max_accuracy_mean=0.8270833333333333`
  - `best_single_accuracy=0.865234375`
- v2 (`results/edp1_exp0200_v2`):
  - `pass_rate=0.0`
  - `max_accuracy_mean=0.8117838541666667`
  - `best_single_accuracy=0.861328125`

### Accuracy trajectory overlay (sample generations)
- g1: v1 `0.7916015625` vs v2 `0.786328125`
- g10: v1 `0.7873697916666667` vs v2 `0.7795572916666667`
- g25: v1 `0.809765625` vs v2 `0.78203125`
- g50: v1 `0.8150390625` vs v2 `0.7821614583333333`
- g75: v1 `0.8178385416666667` vs v2 `0.782421875`
- g100: v1 `0.82421875` vs v2 `0.7803385416666667`

### Functional diversity comparison
- v1 trajectory: `NaN` (исторический baseline был собран до внедрения этой метрики).
- v2 trajectory: стабильно около `0.99`.

## Verification (L0)
- `python scripts/edp1/aggregate_results.py --in results/edp1_exp0200_v2 --out results/edp1_exp0200_v2/aggregates --phase0_generations 10` -> PASS
- `Get-ChildItem results/edp1_exp0200_v2/seeds -Directory | Measure-Object` -> PASS (`30`)
- `Test-Path results/edp1_exp0200_v2/aggregates/metrics_agg.csv` -> PASS
- `Test-Path results/edp1_exp0200_v2/aggregates/fitness_trajectory_agg.csv` -> PASS

## Artifacts
- `results/edp1_exp0200_v2/aggregates/metrics_agg.csv`
- `results/edp1_exp0200_v2/aggregates/fitness_trajectory_agg.csv`
- `results/edp1_exp0200_v2/aggregates/diversity_trajectory_agg.csv`
- `results/edp1_exp0200_v2/aggregates/lineage_summary.csv`
- `reports/analysis/TASK-1201-MRTN-VALIDATION/TASK-1201_BRIEF_REPORT.md`
- `reports/analysis/TASK-1201-MRTN-VALIDATION/metrics_summary.json`
- `reports/analysis/TASK-1201-MRTN-VALIDATION/v1_vs_v2_accuracy_overlay.csv`

## Risks / Limitations
- Обнаружена несогласованность источников `pass_rate`:
  - per-seed `summary.json` от `run_generations` для v2 показывает `kill_status=PASS`.
  - `aggregate_results.py` пересчитывает kill-criteria постфактум и даёт `pass_rate=0.0`.
- До унификации kill-evaluation между runtime и aggregator показатель `pass_rate` должен считаться ограниченно достоверным.

## Rollback
- Код эволюции в этом таске не менялся; rollback не требуется.
- Для повторной валидации удалить `results/edp1_exp0200_v2/` и перезапустить sweep с теми же seed/params.
