# TASK-6920 BRIEF REPORT

## Scope
- Build independent reproduction package for restricted BDC core claims.

## Changes
- Added runner: `scripts/analysis/run_phase22_independent_reproduction_package.py`
- Added task file: `tasks/TASK-6920-INDEPENDENT-REPRODUCTION-PACKAGE.json`
- Added test: `tests/test_phase22_independent_reproduction_package.py`
- Generated:
  - `results/reproduction_package/reproduction_manifest.json`
  - `results/reproduction_package/expected_artifacts.csv`
  - `results/reproduction_package/claim_reproduction_matrix.csv`
  - `results/reproduction_package/REPRODUCTION_README.md`

## Verification (L0)
- `python -m py_compile scripts/analysis/run_phase22_independent_reproduction_package.py` -> PASS
- `pytest -q tests/test_phase22_independent_reproduction_package.py` -> PASS (`1 passed`)
- `python scripts/analysis/run_phase22_independent_reproduction_package.py --out_root results/reproduction_package` -> PASS

## Key Results
- `available_artifacts = 7 / 7`
- claim matrix produced with reproducibility statuses and one-command workflow documented.

## Rollback
- `git revert <TASK-6920-commit-hash>`

