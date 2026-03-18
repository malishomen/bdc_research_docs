# TASK-6940 BRIEF REPORT

## Scope
- Produce a full manuscript draft for restricted BDC, integrating positive/negative claims, OOD transfer, and hybrid-playbook implications.

## Changes
- Added runner: `scripts/analysis/run_phase22_manuscript_draft_restricted_bdc.py`
- Added task file: `tasks/TASK-6940-MANUSCRIPT-DRAFT-RESTRICTED-BDC.json`
- Added test: `tests/test_phase22_manuscript_draft_restricted_bdc.py`
- Generated:
  - `results/manuscript_draft/section_manifest.csv`
  - `results/manuscript_draft/figure_table_plan.csv`
  - `reports/analysis/TASK-6940-MANUSCRIPT-DRAFT-RESTRICTED-BDC/MANUSCRIPT_DRAFT.md`

## Verification (L0)
- `python -m py_compile scripts/analysis/run_phase22_manuscript_draft_restricted_bdc.py` -> PASS
- `pytest -q tests/test_phase22_manuscript_draft_restricted_bdc.py` -> PASS (`1 passed`)
- `python scripts/analysis/run_phase22_manuscript_draft_restricted_bdc.py --core_claims_csv results/restricted_bdc_consolidation/core_claims_matrix.csv --scope_json results/restricted_bdc_consolidation/theory_scope_statement.json --ood_json results/ood_restricted_bdc_validation/ood_validation_summary.json --playbook_json results/hybrid_playbook/playbook_reliability_summary.json --out_root results/manuscript_draft --draft_path reports/analysis/TASK-6940-MANUSCRIPT-DRAFT-RESTRICTED-BDC/MANUSCRIPT_DRAFT.md` -> PASS

## Key Results
- `full_draft_written = true`
- `figures_and_tables_mapped = true`
- `claims_aligned_with_scope = true`
- Draft summary counts: `supported_claim_count = 3`, `falsified_claim_count = 4`

## Rollback
- `git revert <TASK-6940-commit-hash>`
