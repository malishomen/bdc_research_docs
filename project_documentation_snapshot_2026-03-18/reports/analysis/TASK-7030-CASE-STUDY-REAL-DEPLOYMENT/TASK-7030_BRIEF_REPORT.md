# TASK-7030 BRIEF REPORT

## Scope
- Execute an end-to-end real deployment case using BDC Designer CLI + validated hybrid playbook and compare against baseline and direct-CLI arms.

## Changes
- Added runner: `scripts/analysis/run_phase26_case_study_real_deployment.py`
- Added task file: `tasks/TASK-7030-CASE-STUDY-REAL-DEPLOYMENT.json`
- Added test: `tests/test_phase26_case_study_real_deployment.py`
- Generated:
  - `results/case_study_real_deployment/case_selection_manifest.json`
  - `results/case_study_real_deployment/baseline_snapshot.csv`
  - `results/case_study_real_deployment/bdc_cli_outputs.json`
  - `results/case_study_real_deployment/hybrid_refinement_results.csv`
  - `results/case_study_real_deployment/deployment_comparison_summary.csv`
  - `results/case_study_real_deployment/deployment_outcome_summary.json`
- Added public flagship writeup:
  - `reports/public_release/TASK-7030-CASE-STUDY-REAL-DEPLOYMENT/FLAGSHIP_CASE_STUDY.md`

## Verification (L0)
- `python -m py_compile scripts/analysis/run_phase26_case_study_real_deployment.py` -> PASS
- `pytest -q tests/test_phase26_case_study_real_deployment.py` -> PASS (`1 passed`)
- `python scripts/analysis/run_phase26_case_study_real_deployment.py --cli_script tools/bdc_designer_cli.py --out_root results/case_study_real_deployment` -> PASS
- `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/case_study_real_deployment/deployment_outcome_summary.json').read_text(encoding='utf-8')); print(d['case_study_supported'], d['wins_count'], d['checks']['bdc_cli_outputs_used_without_schema_failure'])"` -> PASS

## Key Results
- Selected case: `case_02` (`planner-executor-checker workflow`), `selection_score=0.963`.
- Arm outcomes:
  - Baseline (D1): `time_to_target=36.0h`, `quality=0.701`, `search_cost=145.0`, `iterations=13`.
  - CLI only (D2): `time_to_target=29.88h`, `quality=0.7556`, `search_cost=116.0`, `iterations=10`.
  - CLI + hybrid (D3): `time_to_target=24.203h`, `quality=0.8036`, `search_cost=119.48`, `iterations=7`.
- Core check: D3 beats baseline on all 3 core metrics (`wins_count=3`).
- CLI schema and caution flags captured without failures.

## Rollback
- `git revert <TASK-7030-commit-hash>`
