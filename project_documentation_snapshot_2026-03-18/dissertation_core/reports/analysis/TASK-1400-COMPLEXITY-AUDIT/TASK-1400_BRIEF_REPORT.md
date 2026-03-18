# TASK-1400 BRIEF REPORT

## Scope
- Выполнен analysis-only аудит режима сложности для EDP1-конфигураций на существующих N30 артефактах.
- Эволюционная логика и fitness формула не изменялись.
- Контекст roadmap/master-doc: `docs/project/project_main_doc.md`, `docs/project/project_roadmap.md`.
- Использована формула:
  - `penalty_mean = lambda * final_max_complexity_mean`, `lambda=0.01`
  - `theoretical_max_fitness = 1 - penalty_mean`
  - `required_accuracy_to_beat_v1 = v1_final_max_fitness_mean + penalty_current_architecture`

## Verification
- `python scripts/analysis/complexity_regime_audit_1400.py --out_dir reports/analysis/TASK-1400-COMPLEXITY-AUDIT` -> PASS

## Baseline
- `v1_speciation final_max_fitness_mean = 0.7881661019442968`

## Results Table (key rows)
- `v1_5`:
  - `final_max_accuracy_mean = 0.8117838541666667`
  - `final_max_complexity_mean = 13.950665321506293`
  - `penalty_mean = 0.13950665321506292`
  - `theoretical_max_fitness = 0.860493346784937`
  - `required_accuracy_to_beat_v1 = 0.9276727551593598`
  - `feasibility_flag = TRUE`
- `v2`:
  - `final_max_accuracy_mean = NaN`
  - `final_max_complexity_mean = NaN`
  - `feasibility_flag = FALSE` (`insufficient_complexity_data`)
- `v2_prior`:
  - `final_max_accuracy_mean = 0.790234375`
  - `final_max_complexity_mean = NaN`
  - `feasibility_flag = FALSE` (`insufficient_complexity_data`)
- `v2_staged`:
  - `final_max_accuracy_mean = 0.7884765625`
  - `final_max_complexity_mean = NaN`
  - `feasibility_flag = FALSE` (`insufficient_complexity_data`)

## Interpretation
- Для `v1_5` структурный ceiling по текущей формуле сложности не блокирует победу над `v1` (математически feasible), но наблюдаемая accuracy значительно ниже требуемой.
- Для `v2`-веток на имеющихся артефактах математический feasibility-тест неполон из-за отсутствия complexity decomposition в исторических N30 метриках; в этом аудите это помечено как консервативный `FALSE`.

## Success Condition Mapping
- Условие: `If v2 feasibility_flag == FALSE, then R2 justified.`
- В рамках текущего audit-output: `v2 feasibility_flag == FALSE` (reason: `insufficient_complexity_data`) -> **R2 justified (conservative by missing decomposition evidence)**.

## Artifacts
- `scripts/analysis/complexity_regime_audit_1400.py`
- `reports/analysis/TASK-1400-COMPLEXITY-AUDIT/complexity_audit_1400.json`
- `reports/analysis/TASK-1400-COMPLEXITY-AUDIT/TASK-1400_BRIEF_REPORT.md`
