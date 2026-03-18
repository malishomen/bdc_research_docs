# TASK-1203C BRIEF REPORT

## Scope
- Реализована структурированная мутация для `genome_version=v2` (MRTN): за событие мутирует только один sub-rule.
- Truth table bit-flip отделён в отдельный параметр `--truth_table_bitflip_rate` (default `0.01`).
- Shock/kill/speciation/genome-structure/v1 логика не менялись.

## Changes
- `evolution/edp1_symbolic/mutate.py`
  - Для v2:
    - выбирается `sub_rule_idx` случайно из `0..3`;
    - Gaussian mutation применяется только к выбранному sub-rule;
    - остальные sub-rules остаются неизменными;
    - truth table bit-flip по независимой вероятности `truth_table_flip_prob` (передаётся как `truth_table_bitflip_rate`).
  - Для v1: без изменений.
- `evolution/edp1_symbolic/run_generations.py`
  - Добавлен CLI: `--truth_table_bitflip_rate` (default `0.01`).
  - Вызовы мутации v2 используют `truth_table_bitflip_rate` вместо `mutation_rate` для truth table.
  - В `summary.json` добавлено поле `structured_mutation`.

## Verification (L0)
1. Smoke (`G30/P50/seed1337`, v2, structured):
- Command: `python -m evolution.edp1_symbolic.run_generations ... --genome_version v2 --truth_table_bitflip_rate 0.01`
- Result: **PASS**, `structured_mutation=true`.

2. Determinism replay (тот же seed, повторный run):
- `metrics.csv` SHA256 совпал.
- `summary.json` совпал после исключения `finished_at_utc/out_dir`.

3. One-subrule mutation check (debug assertion + explicit check):
- Проверка через короткий скрипт на 20 последовательных мутаций: `changed_subrules_always_1=PASS`.

4. Full validation (`N=30/G=100/P=100`):
- Root: `results/edp1_exp0200_v2_structured`
- Aggregation: `python scripts/edp1/aggregate_results.py --in results/edp1_exp0200_v2_structured --out results/edp1_exp0200_v2_structured/aggregates --phase0_generations 10`

## Results vs baseline_v2
Source comparison: `reports/analysis/TASK-1203C-H2-STRUCTURED-MUTATION/comparison_vs_v2_baseline.json`

- Delta:
  - `final_max_fitness_mean`: `-0.007427386451264506` (хуже baseline)
  - `best_single_accuracy_mean`: `-0.008072916666666652` (хуже baseline)
  - `runtime_pass_rate`: `0.0` (паритет, оба `1.0`)

- Criteria evaluation:
  - `final_max_fitness_mean(v2_structured) > 0.75`: **FAIL**
  - `>=5/30 seeds best_single_accuracy > 0.75`: **PASS**
  - `trajectory восходящий тренд`: **FAIL** (`delta <= 0`, non-decreasing ratio не выше baseline)

## H2 Decision
- Итог: **H2 not supported** на текущей конфигурации.
- Структурированная мутация в изоляции не восстановила селекционный градиент по fitness/trajectory относительно baseline v2.

## Artifacts
- `results/edp1_exp0200_v2_structured/aggregates/metrics_agg.csv`
- `reports/analysis/TASK-1203C-H2-STRUCTURED-MUTATION/TASK-1203C_BRIEF_REPORT.md`
- `reports/analysis/TASK-1203C-H2-STRUCTURED-MUTATION/comparison_vs_v2_baseline.json`

## Risks / Limitations
- Сравнение базируется на текущих исторических baseline-v2 артефактах и их метриках.
- Для причинного разложения по компонентам мутации по-прежнему нужны per-genome диагностические снимки.

## Rollback
- Откат коммита `TASK-1203C` вернёт прежнюю v2 мутацию.
