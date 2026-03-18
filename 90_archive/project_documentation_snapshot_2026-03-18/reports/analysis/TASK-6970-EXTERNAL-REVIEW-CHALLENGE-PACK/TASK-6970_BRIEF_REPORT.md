# TASK-6970 BRIEF REPORT

## Scope
- Prepare adversarial external-review challenge package for restricted BDC submission, including attack matrix, claim-defense mapping, overclaim risk flags, and reviewer QA pack.

## Changes
- Added runner: `scripts/analysis/run_phase24_external_review_challenge_pack.py`
- Added task file: `tasks/TASK-6970-EXTERNAL-REVIEW-CHALLENGE-PACK.json`
- Added test: `tests/test_phase24_external_review_challenge_pack.py`
- Generated:
  - `results/review_challenge/reviewer_attack_matrix.csv`
  - `results/review_challenge/claim_defense_map.csv`
  - `results/review_challenge/overclaim_risk_flags.csv`
  - `reports/analysis/TASK-6970-EXTERNAL-REVIEW-CHALLENGE-PACK/REVIEWER_QA_PACK.md`

## Verification (L0)
- `python -m py_compile scripts/analysis/run_phase24_external_review_challenge_pack.py` -> PASS
- `pytest -q tests/test_phase24_external_review_challenge_pack.py` -> PASS (`1 passed`)
- `python scripts/analysis/run_phase24_external_review_challenge_pack.py --frozen_claims_csv results/submission_package/frozen_claims_table.csv --scope_json results/submission_package/submission_scope_statement.json --manuscript_md reports/analysis/TASK-6960-SUBMISSION-READY-MANUSCRIPT-PACKAGE/MANUSCRIPT_SUBMISSION_READY.md --out_root results/review_challenge --report_root reports/analysis/TASK-6970-EXTERNAL-REVIEW-CHALLENGE-PACK` -> PASS

## Key Results
- `attack_matrix_compiled = true`
- `defense_map_written = true`
- `overclaim_flags_written = true`
- `reviewer_qa_pack_written = true`
- `high_risk_flag_count = 1`

## Rollback
- `git revert <TASK-6970-commit-hash>`
