# TASK-7010 BRIEF REPORT

## Scope
- Assemble public-facing Restricted BDC v1 release package with frozen-claim safety checks, manuscript/repro bundles, public scope statement, claims sheet, and release manifest.

## Changes
- Added runner: `scripts/analysis/run_phase26_public_release_package.py`
- Added task file: `tasks/TASK-7010-PUBLIC-RELEASE-PACKAGE.json`
- Added test: `tests/test_phase26_public_release_package.py`
- Generated runtime package outputs in `results/public_release/*` and public bundle docs in `reports/public_release/TASK-7010-PUBLIC-RELEASE-PACKAGE/*`

## Verification (L0)
- `python -m py_compile scripts/analysis/run_phase26_public_release_package.py` -> PASS
- `pytest -q tests/test_phase26_public_release_package.py` -> PASS (`1 passed`)
- `python scripts/analysis/run_phase26_public_release_package.py --frozen_claims_csv results/submission_package/frozen_claims_table.csv --theory_scope_json results/restricted_bdc_consolidation/theory_scope_statement.json --overclaim_flags_csv results/review_challenge/overclaim_risk_flags.csv --manuscript_md reports/analysis/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE/MANUSCRIPT_SUBMISSION_READY.md --appendix_md reports/analysis/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE/APPENDIX_SUBMISSION_READY.md --repro_note_md reports/analysis/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE/REPRODUCIBILITY_NOTE.md --repro_manifest_json results/reproduction_package/reproduction_manifest.json --expected_artifacts_csv results/reproduction_package/expected_artifacts.csv --claim_repro_csv results/reproduction_package/claim_reproduction_matrix.csv --out_root results/public_release --public_report_root reports/public_release/TASK-7010-PUBLIC-RELEASE-PACKAGE` -> PASS
- `python -c "import json, pathlib; d=json.loads(pathlib.Path('results/public_release/public_release_manifest.json').read_text(encoding='utf-8')); print(d['public_release_supported'], d['checks']['all_public_claims_within_frozen_scope'], d['checks']['negative_results_explicitly_included'])"` -> PASS (`True True True`)

## Key Results
- `public_release_supported = true`
- `frozen_claim_count = 7`
- `negative_claim_count = 4`
- `all_public_claims_within_frozen_scope = true`
- `high_overclaim_flag_count = 1` (tracked explicitly in release metrics)

## Artifacts
- `scripts/analysis/run_phase26_public_release_package.py`
- `tests/test_phase26_public_release_package.py`
- `tasks/TASK-7010-PUBLIC-RELEASE-PACKAGE.json`
- `reports/public_release/TASK-7010-PUBLIC-RELEASE-PACKAGE/MANUSCRIPT_BUNDLE.md`
- `reports/public_release/TASK-7010-PUBLIC-RELEASE-PACKAGE/REPRODUCIBILITY_BUNDLE.md`
- `reports/public_release/TASK-7010-PUBLIC-RELEASE-PACKAGE/SCOPE_STATEMENT_PUBLIC.md`
- `reports/public_release/TASK-7010-PUBLIC-RELEASE-PACKAGE/PUBLIC_CLAIMS_SHEET.md`
- `results/public_release/*` (runtime, not committed)

## Rollback
- `git revert <TASK-7010-commit-hash>`
