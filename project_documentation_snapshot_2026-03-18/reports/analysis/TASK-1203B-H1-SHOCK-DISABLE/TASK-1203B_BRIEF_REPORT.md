# TASK-1203B BRIEF REPORT

## Scope
- Добавлен флаг `--disable_shock` для изоляции гипотезы H1 в MRTN-v2.
- Проверено влияние отключения shock на `v2` при неизменных mutation/kill/speciation.
- Проведен полный run: `N=30 / G=100 / P=100` в `results/edp1_exp0200_v2_noshock`.

## Code Change (single file)
- `evolution/edp1_symbolic/run_generations.py`
  - Добавлен CLI флаг: `--disable_shock` (default `false`).
  - Применение shock (замена индивидов) выполняется только если `not args.disable_shock`.
  - В plateau-шаге `can_shock` зависит от `not args.disable_shock`.
  - В `summary.json` добавлено поле `shock_disabled`.

## Verification (L0)
1. Smoke v2 + `--disable_shock` (`G30/P50/seed1337`):
   - Result: `FAIL (plateau @ gen=21)`
   - `summary.json`: `shock_disabled=true`, `diversity_shocks_total=0`.
2. Smoke v2 baseline без флага (`G30/P50/seed1337`):
   - Result: `PASS`
   - `diversity_shocks_total=1`.
3. Full validation (`N=30/G100/P100`, with `--disable_shock`):
   - Все 30 seed завершились `FAIL (plateau @ gen=21)`.
   - `shock_event_count_total=0`.

## Evaluation Criteria
- `final_max_fitness_mean(v2_noshock)` vs baseline_v2:
  - noshock: `0.5344320536004282`
  - baseline: `0.5356865515715754`
  - delta: `-0.0012544979711471838`
- `best_single_accuracy` distribution (mean):
  - noshock: baseline-дельта `-0.001953125`
- Trajectory monotonicity (`max_fitness_mean`, aggregate trajectory):
  - noshock remains low and terminates early (kill at gen 21 runtime-canonical).
- Shock events:
  - noshock: `0`
  - baseline_v2: `240`

## H1 Decision
- Success signal check:
  - "final_max_fitness_mean > 0.75 хотя бы в 5/30 seeds" -> **NOT MET** (`0/30`, mean `0.5344`).
- Conclusion:
  - **H1 rejected** on current setup.
  - Disabling shock degrades runtime outcomes (runtime pass_rate: baseline `1.0` -> noshock `0.0`) and does not improve fitness.

## Artifacts
- `results/edp1_exp0200_v2_noshock/aggregates/metrics_agg.csv`
- `reports/analysis/TASK-1203B-H1-SHOCK-DISABLE/TASK-1203B_BRIEF_REPORT.md`
- `reports/analysis/TASK-1203B-H1-SHOCK-DISABLE/comparison_summary.json`

## Risks / Limitations
- В задаче требовался "smoke PASS" для noshock, но фактический L0 результат: plateau fail на `gen=21`.
- Aggregate `pass_rate` в проекте не используется как canonical; вывод по PASS/FAIL основан на `summary.json.kill_status`.

## Rollback
- Удалить флаг из `run_generations.py` или запускать без `--disable_shock` (baseline behavior unchanged).
