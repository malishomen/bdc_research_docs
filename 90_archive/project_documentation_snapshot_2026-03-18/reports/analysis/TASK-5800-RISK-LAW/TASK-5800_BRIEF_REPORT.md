# TASK-5800 BRIEF REPORT

## Scope
- Empirically verify risk-adjusted weight law hypothesis on coevolution artifacts:
  - `w_r ∝ mu_r / sigma_r^2`
- Use existing Phase-7 outputs only (no retraining):
  - `results/coevolution/per_seed_metrics.csv`
  - `results/coevolution/role_ratio_dynamics.csv`
  - `results/coevolution/partner_sampling_metrics.csv`
- Produce full artifact bundle in `results/risk_law/`.

## Changes
- Added analysis script:
  - `scripts/analysis/task5800_risk_adjusted_weight_law.py`
- Added unit smoke test:
  - `tests/test_phase8_risk_law.py`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/task5800_risk_adjusted_weight_law.py`
- Result: PASS

- Command: `pytest -q tests/test_phase8_risk_law.py`
- Result: PASS
- Output summary: `1 passed`.

- Command: `python scripts/analysis/task5800_risk_adjusted_weight_law.py --per_seed_metrics results/coevolution/per_seed_metrics.csv --role_ratio_dynamics results/coevolution/role_ratio_dynamics.csv --partner_sampling_metrics results/coevolution/partner_sampling_metrics.csv --out_root results/risk_law`
- Result: PASS
- Output summary: `{"pearson_correlation": -0.9835944662021062, "mean_absolute_error": 0.32933314182314616, "law_confirmed": false}`.

- Command: `python -c "import json,pathlib; m=json.loads(pathlib.Path('results/risk_law/weight_comparison_metrics.json').read_text(encoding='utf-8')); print(m['pearson_correlation'], m['mean_absolute_error'], m['law_confirmed'])"`
- Result: PASS
- Output summary: `-0.9835944662021062 0.32933314182314616 False`.

## Artifacts
- `results/risk_law/role_statistics.csv`
- `results/risk_law/signal_to_noise.csv`
- `results/risk_law/predicted_weights.csv`
- `results/risk_law/weight_comparison_metrics.json`
- `results/risk_law/correlation_timeseries.csv`

## Findings
- Estimated `mu/sigma^2` yields predicted weights that are anti-correlated with observed coevolution weights.
- Gate criteria not met:
  - `pearson_correlation >= 0.8` -> FAIL (`-0.9836`)
  - `MAE <= 0.1` -> FAIL (`0.3293`)
- Hypothesis for TASK-5800 is **not confirmed** on current data.

## Risks / Limitations
- Result is post-hoc empirical verification on saved outputs, not a new rerun under altered selection law.
- Contribution proxy is defined from per-seed delta decomposition (`delta * role_weight_ratio`) by current artifact schema.

## Rollback
- Revert commits:
  - `git revert <TASK-5800-implementation-hash>`
  - `git revert <TASK-5800-hash-followup-hash>`
