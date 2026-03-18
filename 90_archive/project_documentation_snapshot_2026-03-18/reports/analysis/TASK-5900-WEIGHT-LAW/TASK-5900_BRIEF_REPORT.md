# TASK-5900 BRIEF REPORT

## Scope
- Discover generalized empirical law for emergent coevolution role weights using:
  - `w_r ∝ sigma_r^alpha / mu_r^beta`
- Use existing artifacts only (no retraining):
  - `results/risk_law/role_statistics.csv`
  - `results/coevolution/role_ratio_dynamics.csv`
  - `results/coevolution/per_seed_metrics.csv`
- Produce full output bundle under `results/weight_law/`.

## Changes
- Added analysis script:
  - `scripts/analysis/task5900_generalized_weight_law_discovery.py`
- Added canonical task spec:
  - `tasks/TASK-5900-GENERALIZED-WEIGHT-LAW-DISCOVERY.json`
- Added unit/smoke test:
  - `tests/test_phase9_weight_law.py`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/task5900_generalized_weight_law_discovery.py`
- Result: PASS

- Command: `pytest -q tests/test_phase9_weight_law.py`
- Result: PASS
- Output summary: `1 passed`.

- Command: `python scripts/analysis/task5900_generalized_weight_law_discovery.py --role_statistics results/risk_law/role_statistics.csv --role_ratio_dynamics results/coevolution/role_ratio_dynamics.csv --per_seed_metrics results/coevolution/per_seed_metrics.csv --out_root results/weight_law`
- Result: PASS
- Output summary:
  - `alpha=1.5714285714285714`
  - `beta=0.6020408163265306`
  - `pearson=0.9821649299187987`
  - `MAE=0.03882849082931975`
  - `law_confirmed=True`

- Command: `python -c "import json,pathlib; b=json.loads(pathlib.Path('results/weight_law/best_parameters.json').read_text(encoding='utf-8')); print(b['best_parameters']['alpha'], b['best_parameters']['beta'], b['fit_metrics']['pearson_correlation'], b['fit_metrics']['mean_absolute_error'], b['law_confirmed'])"`
- Result: PASS
- Output summary: `1.5714285714285714 0.6020408163265306 0.9821649299187987 0.03882849082931975 True`.

## Artifacts
- `results/weight_law/grid_parameters.csv`
- `results/weight_law/predicted_weight_grid.csv`
- `results/weight_law/model_fit_metrics.csv`
- `results/weight_law/best_parameters.json`
- `results/weight_law/stability_analysis.csv`

## Findings
- Grid search (`50 x 50 = 2500` configs) identified best generalized law parameters:
  - `alpha=1.5714285714285714`
  - `beta=0.6020408163265306`
- Primary criteria are met:
  - `pearson >= 0.9` -> PASS (`0.9822`)
  - `MAE <= 0.05` -> PASS (`0.0388`)
- TASK-5900 generalized law is **confirmed** on global fit.
- Robustness table is generated (per-seed and per-generation), but shows broad variability:
  - mean per-seed correlation is negative, indicating high seed-level heterogeneity.

## Risks / Limitations
- Global fit is strong, but seed-level robustness is uneven; law may describe aggregate behavior better than each individual seed.
- Model fit depends on role-level `mu/std` statistics already derived in TASK-5800; any upstream statistic-definition change requires full recompute.

## Rollback
- Revert commit(s):
  - `git revert <TASK-5900-implementation-hash>`
  - `git revert <TASK-5900-hash-followup-hash>`
