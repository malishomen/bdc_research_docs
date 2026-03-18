# Reproducibility Note

## One-command check
python scripts/analysis/run_phase22_independent_reproduction_package.py --out_root results/reproduction_package

## Required artifacts
- results/restricted_bdc_consolidation/core_claims_matrix.csv
- results/restricted_bdc_consolidation/theory_scope_statement.json
- results/negative_transition_result/restricted_bdc_theory.json
- results/hybrid_architecture_search/hybrid_value_summary.json
- results/design_rulebook/design_rules.json
- results/effective_role_count/stopping_rule_summary.json

## Integrity checks
1. Verify expected artifacts exist in `results/reproduction_package/expected_artifacts.csv`.
2. Verify claim statuses in `results/reproduction_package/claim_reproduction_matrix.csv`.
3. Verify manuscript freeze tables in `results/submission_package/`.
