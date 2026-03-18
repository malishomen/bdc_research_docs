# TASK-1206 BRIEF REPORT

## Scope
- Проверена гипотеза staged schedule для MRTN v2: сначала sub-rule-first с freeze truth table (Phase A), затем разморозка truth table (Phase B).
- Изменён только search schedule в `run_generations.py`; fitness/shock/speciation/kill criteria не менялись.

## Changes
- `evolution/edp1_symbolic/run_generations.py`
  - Добавлен флаг `--staged_subrule_first` (default: false)
  - Добавлен параметр `--staged_threshold_fitness` (default: 0.60)
  - Для `genome_version=v2` и включённого staged-режима:
    - Phase A: truth table фиксируется и не мутирует (`truth_table_flip_prob=0.0`)
    - freeze применяется также при shock-иммиграции
    - Phase B: после `max_fitness >= threshold` или `gen >= phase0_min_generations` truth table мутация включается обратно
  - В `summary.json` добавлены:
    - `staged_subrule_first`
    - `staged_threshold_fitness`
    - `staged_transition_generation`
    - `staged_truth_table_diverged_generation`
    - `staged_frozen_truth_table_hash`

## Verification (L0)
- Smoke:
  - `python -m evolution.edp1_symbolic.run_generations --out_dir results/edp1_exp0200_v2_staged_smoke --genome_version v2 --generations 30 --population 50 --seed 1337 --staged_subrule_first --staged_threshold_fitness 0.60`
  - Result: PASS
- Determinism replay:
  - `... --out_dir results/edp1_exp0200_v2_staged_det_a ...`
  - `... --out_dir results/edp1_exp0200_v2_staged_det_b ...`
  - `metrics.csv` identical: `True`
  - `summary.json` identical excluding time/path: `True`
- Full validation:
  - Seeds `1337..1366`, `N=30/G=100/P=100` -> `results/edp1_exp0200_v2_staged/seeds/*`
  - Aggregation: `python scripts/edp1/aggregate_results.py --in results/edp1_exp0200_v2_staged --out results/edp1_exp0200_v2_staged/aggregates --phase0_generations 10`

## Results
- `final_max_fitness_mean`:
  - v2_prior: `0.5531664379938884`
  - v2_staged: `0.5524726487966959`
  - delta: `-0.0006937891971925316`
- Phase A criterion (`max_fitness > 0.60` in Phase A):
  - hits: `2/30` (target `>=10`) -> FAIL
- Trajectory (staged max_fitness_mean):
  - gen1 `0.5495`, gen10 `0.5495`, gen25 `0.5492`, gen50 `0.5503`, gen75 `0.5522`, gen100 `0.5525`
  - тренд умеренно восходящий, но без прорыва порога
- Additional:
  - `best_single_max_fitness_gt_0.68_count`: `0`
  - `final_max_accuracy_mean`: `0.6904947916666666` (не > `0.75`)

## Evaluation vs Criteria
- Phase A > 0.60 at least in 10/30: **FAIL** (2/30)
- `final_max_fitness_mean > 0.68`: **FAIL**
- Upward trajectory without degradation: **PARTIAL PASS**
- `max_accuracy_mean > 0.75`: **FAIL**

## Conclusion
- Гипотеза о снятии локального аттрактора через staged subrule-first в текущей конфигурации не подтверждена.
- Режим стабилизирует траекторию, но не даёт улучшения относительно `v2_prior` по итоговой fitness.

## Artifacts
- `results/edp1_exp0200_v2_staged/aggregates/metrics_agg.csv`
- `reports/analysis/TASK-1206-STAGED-EVOLUTION/comparison_vs_v2_prior.json`
- `reports/analysis/TASK-1206-STAGED-EVOLUTION/TASK-1206_BRIEF_REPORT.md`
