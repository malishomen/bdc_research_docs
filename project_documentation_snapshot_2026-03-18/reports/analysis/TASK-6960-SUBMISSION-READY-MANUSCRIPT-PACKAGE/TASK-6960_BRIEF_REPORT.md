# TASK-6960 BRIEF REPORT

## Scope
- Convert restricted BDC manuscript draft into submission-ready package with frozen claims, figure/table freeze, appendix, reproducibility note, and bounded scope statement.

## Changes
- Added runner: `scripts/analysis/run_phase24_submission_ready_manuscript_package.py`
- Added task file: `tasks/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE.json`
- Added test: `tests/test_phase24_submission_ready_manuscript_package.py`
- Generated:
  - `results/submission_package/frozen_claims_table.csv`
  - `results/submission_package/figure_table_freeze.csv`
  - `results/submission_package/appendix_manifest.csv`
  - `results/submission_package/submission_scope_statement.json`
  - `reports/analysis/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE/MANUSCRIPT_SUBMISSION_READY.md`
  - `reports/analysis/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE/APPENDIX_SUBMISSION_READY.md`
  - `reports/analysis/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE/REPRODUCIBILITY_NOTE.md`

## Verification (L0)
- `python -m py_compile scripts/analysis/run_phase24_submission_ready_manuscript_package.py` -> PASS
- `pytest -q tests/test_phase24_submission_ready_manuscript_package.py` -> PASS (`1 passed`)
- `python scripts/analysis/run_phase24_submission_ready_manuscript_package.py --draft_md reports/analysis/TASK-6940-MANUSCRIPT-DRAFT-RESTRICTED-BDC/MANUSCRIPT_DRAFT.md --core_claims_csv results/restricted_bdc_consolidation/core_claims_matrix.csv --claim_repro_csv results/reproduction_package/claim_reproduction_matrix.csv --ood_json results/ood_restricted_bdc_validation/ood_validation_summary.json --playbook_json results/hybrid_playbook/playbook_reliability_summary.json --adaptation_json results/real_world_adaptation/adaptation_findings.json --out_root results/submission_package --report_root reports/analysis/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE` -> PASS

## Key Results
- `submission_ready_manuscript_written = true`
- `appendix_written = true`
- `reproducibility_note_written = true`
- `claims_frozen = true`
- `figures_tables_frozen = true`

## Rollback
- `git revert <TASK-6960-commit-hash>`
