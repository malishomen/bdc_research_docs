# TASK-6400 BRIEF REPORT

## Scope
- Validate information-law hypothesis:
  - `w_r ≈ I(role_r ; task_outcome) / Σ I(role_k ; task_outcome)`
- Inputs:
  - `results/task_structure_mapping/per_seed_metrics.csv`
  - `results/task_structure_mapping/role_ratio_by_task.csv`
- Pipeline outputs:
  - `role_signals.csv`
  - `information_metrics.csv`
  - `theoretical_weights.csv`
  - `weight_information_comparison.csv`
  - `information_law_validation.json`

## Changes
- Added analysis runner:
  - `scripts/analysis/run_phase14_information_law.py`
- Added test:
  - `tests/test_phase14_information_law.py`
- Added canonical task JSON:
  - `tasks/TASK-6400-ROLE-INFORMATION-LAW-VALIDATION.json`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/run_phase14_information_law.py tests/test_phase14_information_law.py`
- Result: PASS

- Command: `pytest -q tests/test_phase14_information_law.py`
- Result: PASS
- Output summary: `1 passed`.

- Command: `python scripts/analysis/run_phase14_information_law.py --per_seed_metrics_csv results/task_structure_mapping/per_seed_metrics.csv --role_ratio_by_task_csv results/task_structure_mapping/role_ratio_by_task.csv --out_root results/information_law --bins 4`
- Result: PASS
- Output summary:
  - `pearson_correlation=0.14534542188918945`
  - `mean_absolute_error=0.22581970618677938`
  - `rank_consistency=false`
  - `law_confirmed=false`

## Artifacts
- `results/information_law/role_signals.csv`
- `results/information_law/information_metrics.csv`
- `results/information_law/theoretical_weights.csv`
- `results/information_law/weight_information_comparison.csv`
- `results/information_law/information_law_validation.json`

## Results
- Law criteria are not met:
  - `pearson >= 0.85` -> FAIL (`0.1453`)
  - `MAE <= 0.08` -> FAIL (`0.2258`)
  - `rank_consistency` -> FAIL (`false`)
- Family-level ranking mismatches:
  - `aggregator_dominant`: empirical top=`aggregator`, theoretical top=`predictor`
  - `predictor_dominant`: empirical top=`predictor`, theoretical top=`critic`

## Interpretation
- With the current role-signal extraction and MI/CMI estimation protocol, normalized information contributions do not reproduce emergent role ratios.
- This indicates either:
  - information-law is not valid in this formulation, or
  - the current observable signal proxies are insufficient for causal information attribution.

## Risks / Limitations
- Role signals are derived proxies from aggregate seed-level outputs; no raw per-step model internals are available.
- CMI uses discretized `other-role` proxy, which is an approximation.

## Rollback
- Revert commits:
  - `git revert <TASK-6400-implementation-hash>`
  - `git revert <TASK-6400-hash-followup-hash>`
