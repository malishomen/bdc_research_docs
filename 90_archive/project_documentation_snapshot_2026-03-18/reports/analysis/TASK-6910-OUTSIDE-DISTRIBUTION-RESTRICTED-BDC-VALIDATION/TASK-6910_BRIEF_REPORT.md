# TASK-6910 BRIEF REPORT

## Scope
- Validate restricted BDC core under 6 OOD validation domains.

## Changes
- Added runner: `scripts/analysis/run_phase22_ood_restricted_bdc_validation.py`
- Added task file: `tasks/TASK-6910-OUTSIDE-DISTRIBUTION-RESTRICTED-BDC-VALIDATION.json`
- Added test: `tests/test_phase22_ood_restricted_bdc_validation.py`
- Generated:
  - `results/ood_restricted_bdc_validation/domain_manifest.csv`
  - `results/ood_restricted_bdc_validation/equilibrium_transfer.csv`
  - `results/ood_restricted_bdc_validation/hybrid_transfer.csv`
  - `results/ood_restricted_bdc_validation/role_count_transfer.csv`
  - `results/ood_restricted_bdc_validation/ood_validation_summary.json`

## Verification (L0)
- `python -m py_compile scripts/analysis/run_phase22_ood_restricted_bdc_validation.py` -> PASS
- `pytest -q tests/test_phase22_ood_restricted_bdc_validation.py` -> PASS (`1 passed`)
- `python scripts/analysis/run_phase22_ood_restricted_bdc_validation.py --restricted_json results/restricted_bdc_consolidation/theory_scope_statement.json --hybrid_json results/hybrid_architecture_search/hybrid_value_summary.json --stopping_json results/effective_role_count/stopping_rule_summary.json --out_root results/ood_restricted_bdc_validation` -> PASS

## Key Results
- `supported = true`
- `equilibrium_transfer_pass_rate = 0.8333`
- `hybrid_transfer_pass_rate = 1.0`
- `role_count_transfer_pass_rate = 1.0`

## Rollback
- `git revert <TASK-6910-commit-hash>`

