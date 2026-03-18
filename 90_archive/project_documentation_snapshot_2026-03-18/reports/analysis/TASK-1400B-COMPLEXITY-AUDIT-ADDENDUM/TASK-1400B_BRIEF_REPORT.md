# TASK-1400B BRIEF REPORT

## Scope
- Выполнен execution-only addendum для TASK-1400 на актуальной схеме decomposition.
- Прогнаны недостающие N=30/G=100/P=100 наборы: `v2_prior_decomp`, `v2_staged_decomp`.
- Для `v2_decomp` выполнена агрегация на текущем коде.
- Пересчитан complexity audit для baseline `v1_speciation`, `v1_5`, `v2_decomp`, `v2_prior_decomp`, `v2_staged_decomp`.
- Контекст roadmap/master-doc: `docs/project/project_main_doc.md`, `docs/project/project_roadmap.md`.

## Execution
- `bash scripts/edp1/run_edp1_sweep.sh --seeds 30 --generations 100 --population 100 --genome_version v2 --base_seed 1337 --out_root results/edp1_exp0200_v2_prior_decomp`
- Manual staged loop (30 seeds) with:
  - `python -m evolution.edp1_symbolic.run_generations ... --staged_subrule_first --staged_threshold_fitness 0.60`
  - output root: `results/edp1_exp0200_v2_staged_decomp`
- `python scripts/edp1/aggregate_results.py --in results/edp1_exp0200_v2_decomp --out results/edp1_exp0200_v2_decomp/aggregates --phase0_generations 10`
- Runtime override of `INPUTS` in `complexity_regime_audit_1400.py` to point at decomp roots; output written to addendum directory.

## Key Results (v2 real decomposition)
- Lambda: `0.01`
- Baseline for beat condition: `v1_speciation final_max_fitness_mean = 0.7881661019442968`

### v2
- `final_max_complexity_mean = 34.19378741318382`
- `penalty_mean = 0.3419378741318382`
- `required_accuracy_to_beat_v1 = 1.130103976076135`
- `feasibility_flag = false` (`required_accuracy>1.0`)

### v2_prior
- `final_max_complexity_mean = 34.19378741318382`
- `penalty_mean = 0.3419378741318382`
- `required_accuracy_to_beat_v1 = 1.130103976076135`
- `feasibility_flag = false` (`required_accuracy>1.0`)

### v2_staged
- `final_max_complexity_mean = 34.189465763975186`
- `penalty_mean = 0.34189465763975185`
- `required_accuracy_to_beat_v1 = 1.1300607595840486`
- `feasibility_flag = false` (`required_accuracy>1.0`)

## Conclusion
- Для всех проверенных `v2*` вариантов при текущем режиме (`fitness = accuracy - 0.01 * complexity`) наблюдается:
  - `required_accuracy_to_beat_v1 > 1.0`.
- Это математически исключает победу `v2*` над `v1_speciation` в текущем complexity regime.

## Deliverables
- `reports/analysis/TASK-1400B-COMPLEXITY-AUDIT-ADDENDUM/complexity_audit_1400b.json`
- `reports/analysis/TASK-1400B-COMPLEXITY-AUDIT-ADDENDUM/TASK-1400B_BRIEF_REPORT.md`
