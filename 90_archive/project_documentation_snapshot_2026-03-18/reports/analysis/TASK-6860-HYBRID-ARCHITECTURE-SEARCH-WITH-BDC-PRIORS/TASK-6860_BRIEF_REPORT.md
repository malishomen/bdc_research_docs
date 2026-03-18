# TASK-6860 BRIEF REPORT

## Scope
- Evaluate whether BDC priors add practical value as hybrid search components (`H1`, `H2`) versus unguided/bruteforce/standalone baselines (`H3`, `H4`, `H5`) under matched budget.

## Changes
- Added runner: `scripts/analysis/run_phase20_hybrid_architecture_search_with_bdc_priors.py`.
- Added task descriptor: `tasks/TASK-6860-HYBRID-ARCHITECTURE-SEARCH-WITH-BDC-PRIORS.json`.
- Added smoke test: `tests/test_phase20_hybrid_architecture_search_with_bdc_priors.py`.
- Generated runtime artifacts:
  - `results/hybrid_architecture_search/search_arm_manifest.csv`
  - `results/hybrid_architecture_search/raw_benchmark_results.csv`
  - `results/hybrid_architecture_search/efficiency_summary.csv`
  - `results/hybrid_architecture_search/performance_robustness_summary.csv`
  - `results/hybrid_architecture_search/hybrid_value_summary.json`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/run_phase20_hybrid_architecture_search_with_bdc_priors.py`
- Result: PASS

- Command: `pytest -q tests/test_phase20_hybrid_architecture_search_with_bdc_priors.py`
- Result: PASS (`1 passed`)

- Command: `python scripts/analysis/run_phase20_hybrid_architecture_search_with_bdc_priors.py --base_seed 1337 --seeds_per_family 20 --generations 80 --search_budget 20 --out_root results/hybrid_architecture_search`
- Result: PASS

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/hybrid_architecture_search/hybrid_value_summary.json').read_text(encoding='utf-8')); print(d['best_hybrid_arm'], d['hybrid_value_supported'], d['checks'])"`
- Result: PASS
- Output summary:
  - `best_hybrid_arm = H2`
  - `hybrid_value_supported = true`
  - all 4 criteria checks = `true`

## Key Metrics
- `H2 mean_final_fitness = 0.1870` (best among all arms)
- `H2 mean_best_fitness_under_budget = 0.00725` vs `H4 = 0.00557` (beats bruteforce baseline)
- `H2 mean_search_efficiency = 0.00935` vs `H3 = 0.00727` (beats unguided random search)
- `H2 seed_robustness_std_final_fitness = 0.0326` vs `H4 = 0.0539` (not worse than bruteforce)
- `H2` also outperforms standalone BDC (`H5 mean_final_fitness = 0.1441`)

## Artifacts
- `scripts/analysis/run_phase20_hybrid_architecture_search_with_bdc_priors.py`
- `tests/test_phase20_hybrid_architecture_search_with_bdc_priors.py`
- `tasks/TASK-6860-HYBRID-ARCHITECTURE-SEARCH-WITH-BDC-PRIORS.json`
- `results/hybrid_architecture_search/hybrid_value_summary.json`

## Risks / Limitations
- This is an oracle-driven matched-budget architecture-selection benchmark, not full end-to-end retraining per arm.
- Hybrid advantage should be rechecked under stricter external holdout (unseen family variants) before product-level claims.

## Rollback
- Revert with: `git revert <TASK-6860-commit-hash>`.

