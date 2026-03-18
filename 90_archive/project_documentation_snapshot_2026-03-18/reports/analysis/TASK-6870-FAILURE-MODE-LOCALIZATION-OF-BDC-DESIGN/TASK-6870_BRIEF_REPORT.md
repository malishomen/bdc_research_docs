# TASK-6870 BRIEF REPORT

## Scope
- Localize failure modes of standalone BDC equilibrium-guided design (`A1`) against stronger baselines from TASK-6850.
- Quantify failure slices, ranked predictors, robustness breakdown, and design limits.

## Changes
- Added runner: `scripts/analysis/run_phase20_failure_mode_localization_bdc_design.py`.
- Added task descriptor: `tasks/TASK-6870-FAILURE-MODE-LOCALIZATION-OF-BDC-DESIGN.json`.
- Added test: `tests/test_phase20_failure_mode_localization_bdc_design.py`.
- Generated artifacts:
  - `results/bdc_design_failure_modes/failure_slices.csv`
  - `results/bdc_design_failure_modes/failure_predictors.csv`
  - `results/bdc_design_failure_modes/robustness_breakdown.csv`
  - `results/bdc_design_failure_modes/design_limits_summary.json`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/run_phase20_failure_mode_localization_bdc_design.py`
- Result: PASS

- Command: `pytest -q tests/test_phase20_failure_mode_localization_bdc_design.py`
- Result: PASS (`1 passed`)

- Command: `python scripts/analysis/run_phase20_failure_mode_localization_bdc_design.py --raw_csv results/equilibrium_design_value/raw_benchmark_results.csv --perf_csv results/equilibrium_design_value/performance_summary.csv --rob_csv results/equilibrium_design_value/robustness_summary.csv --out_root results/bdc_design_failure_modes`
- Result: PASS

- Output summary:
  - global failure rate (`A1` vs strongest baseline): `0.55`
  - top predictor: `equilibrium_concentration` (score `0.8263`)

## Key Findings
- Standalone BDC design fails in a majority of `(family, seed)` points under current benchmark conditions.
- Failure correlates strongest with concentration of prior mass and perturbation sensitivity.
- Robustness breakdown confirms that brute-force/randomized baselines dominate in selected slices.

## Artifacts
- `scripts/analysis/run_phase20_failure_mode_localization_bdc_design.py`
- `tests/test_phase20_failure_mode_localization_bdc_design.py`
- `results/bdc_design_failure_modes/design_limits_summary.json`

## Risks / Limitations
- Localization is based on TASK-6850 oracle-driven benchmark outputs and inherits those assumptions.
- Predictor ranking is correlation-based (not full causal attribution).

## Rollback
- Revert with: `git revert <TASK-6870-commit-hash>`.

