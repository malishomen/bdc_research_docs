# TASK-1203A BRIEF REPORT

## Scope
- Выполнена диагностическая аналитика MRTN v2 на фактических артефактах `results/edp1_exp0200_v2/seeds/*`.
- Анализ строго read-only: без изменения эволюционной логики и без пересчёта kill-criteria.
- PASS/FAIL использован только из canonical runtime источника `summary.json.kill_status`.

## Changes
- Добавлен диагностический скрипт:
  - `scripts/analysis/mrtn_diagnostic_1203a.py`
- Сформирован основной результат:
  - `reports/analysis/TASK-1203A-MRTN-DIAGNOSTIC/diagnostic_results.json`
- Дополнительно сохранены контекстные сравнения v1:
  - `reports/analysis/TASK-1203A-MRTN-DIAGNOSTIC/diagnostic_results_v1_speciation_context.json`
  - `reports/analysis/TASK-1203A-MRTN-DIAGNOSTIC/diagnostic_results_v1_shock_context.json`

## Verification (L0)
- Command:
  - `python scripts/analysis/mrtn_diagnostic_1203a.py --in results/edp1_exp0200_v2 --out reports/analysis/TASK-1203A-MRTN-DIAGNOSTIC/diagnostic_results.json`
- Result: PASS

## Required Analyses

### 1) Shock damage assessment
- `shock_event_count`: `240`
- `window[-1,+1] delta_max_fitness`:
  - mean `0.00015681224639339567`
  - median `0.0`
  - p25/p75 `0.0 / 0.0`
- `window[-1,+1] delta_mean_fitness`:
  - mean `0.0006898903880967081`
  - median `0.0004885156027991666`
  - p25/p75 `-0.005849008808709484 / 0.006841978652706346`
- `window[-3,+3]` показывает тот же знак и порядок величин.

Факт: в MRTN-v2 на текущих артефактах shock не даёт выраженного прироста `max_fitness` (медиана нулевая, IQR по `max_fitness` нулевой).

### 2) Truth-table convergence
- Поля, требующие per-genome состояние (`truth_table_bit_entropy_mean`, `truth_table_hamming_to_mode_mean`), **невычислимы** из текущих артефактов (в seeds есть только `metrics.csv`, `summary.json`).
- Прокси по доступному полю `rule_entropy`:
  - траектория фактически константна около `4.605170185988083` (по поколениям и по сиду).

### 3) Sub-rule specialization
- `subrule_output_corr_matrix_summary`: `null`
- `unique_subrule_output_patterns`: `null`
- Причина: sub-rule outputs не логируются и не сохраняются в seed artifacts.

### 4) Mutation impact attribution (proxy)
- `delta_weights_norm`: `null`
- `delta_truth_table_hamming`: `null`
- Ассоциации-прокси (доступные по агрегатам):
  - corr(`delta_rule_entropy`, `delta_max_fitness`) = `nan`
  - corr(`delta_rule_entropy`, `delta_mean_fitness`) = `nan`
  - corr(`shock_applied`, `delta_max_fitness`) = `-0.018469111561007355`
  - corr(`shock_applied`, `delta_mean_fitness`) = `0.009554060611991686`

Факт: по имеющемуся агрегированному слою линейная связь shock↔fitness-delta близка к нулю.

### 5) Functional vs parametric diversity
- `functional_diversity_mean`: `0.9914666666666665`
- `functional_diversity_ci95`: `0.0002907782256561145`
- `diversity_index_mean`: `1.0`
- `diversity_index_ci95`: `0.0`
- relation_to_fitness:
  - corr(`functional_diversity_mean`, `max_fitness_mean`) = `-0.4164302261198318`
  - corr(`diversity_index_mean`, `max_fitness_mean`) = `nan` (ряд константный = 1.0)

Факт: при очень высокой functional/parametric diversity, fitness остаётся низким/стагнирующим.

## Runtime Canonical Status (v2)
- `runs_total=30`, `runs_pass=30`, `pass_rate=1.0` (только из `summary.json.kill_status`).

## Artifacts
- `scripts/analysis/mrtn_diagnostic_1203a.py`
- `reports/analysis/TASK-1203A-MRTN-DIAGNOSTIC/diagnostic_results.json`
- `reports/analysis/TASK-1203A-MRTN-DIAGNOSTIC/TASK-1203A_BRIEF_REPORT.md`

## Risks / Limitations
- Без per-generation genome snapshots невозможно вычислить прямые truth-table/sub-rule/mutation-component метрики; доступны только агрегатные proxy-оценки.
- Для полноценной причинной диагностики нужен follow-up на расширение диагностического логирования (без изменения эволюционной логики).

## Rollback
- Не требуется (analysis-only).
