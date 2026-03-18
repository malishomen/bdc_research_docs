# ERRATA for TASK-1206

## Issue
In `TASK-1206_BRIEF_REPORT.md` the field labeled as `final_max_accuracy_mean` was incorrectly reported as:
- `0.6904947916666666`

Raw CSV reproduction (TASK-1207A) confirms the correct value is:
- `mean(final_max_accuracy over 30 seeds) = 0.7884765625`

Reference:
- `reports/analysis/TASK-1207A-METRICS-REPRO/metrics_repro_result.json`

## Root Cause
Metrics reporting pipeline mixed/incorrectly labeled `max_accuracy_mean` vs `mean_accuracy` at report layer.

## Corrected values
- Correct `final_max_accuracy_mean`: `0.7884765625`
- `mean(final_mean_accuracy)`: `0.7106119791666666`

## Impact on conclusions
- No change to main TASK-1206 conclusion:
  - staged schedule still does not beat `v2_prior` on `final_max_fitness_mean`
  - phase-A threshold criterion remains FAIL
- Only metric labeling/value in report text was incorrect.
