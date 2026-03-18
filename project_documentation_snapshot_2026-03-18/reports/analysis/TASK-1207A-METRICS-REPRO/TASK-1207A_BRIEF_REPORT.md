# TASK-1207A BRIEF REPORT

## Scope
- Reproduced `max_accuracy_mean` reporting discrepancy from raw `metrics.csv` for `results/edp1_exp0200_v2_staged`.
- Analysis-only for reporting integrity; experiment outcomes were not recomputed.

## Verification
- `python scripts/analysis/verify_max_accuracy_discrepancy_1207a.py --root results/edp1_exp0200_v2_staged --out reports/analysis/TASK-1207A-METRICS-REPRO/metrics_repro_result.json`
- Result: PASS (script execution), reporting status: FAIL

## Findings
- Seeds discovered: 30
- Mean of per-seed `final_max_accuracy`: `0.7884765625`
- Mean of per-seed `final_mean_accuracy`: `0.7106119791666666`
- `TASK-1206_BRIEF_REPORT.md` declared `final_max_accuracy_mean=0.6904947916666666` -> mismatch confirmed.
- `comparison_vs_v2_prior.json` value for `final_max_accuracy_mean` matches raw reproduction (`0.7884765625`).

## Status
- Reporting integrity status for current TASK-1206 report labeling: **FAIL**
- Reason: incorrect `max_accuracy_mean` value/label in TASK-1206 brief report text.

## Artifacts
- `scripts/analysis/verify_max_accuracy_discrepancy_1207a.py`
- `reports/analysis/TASK-1207A-METRICS-REPRO/metrics_repro_result.json`
- `reports/analysis/TASK-1207A-METRICS-REPRO/TASK-1207A_BRIEF_REPORT.md`
