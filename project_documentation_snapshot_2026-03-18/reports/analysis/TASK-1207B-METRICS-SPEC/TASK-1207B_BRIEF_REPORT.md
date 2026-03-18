# TASK-1207B BRIEF REPORT

## Scope
- Fixed max/mean accuracy aggregation integrity in `scripts/edp1/aggregate_results.py`.
- Added canonical metrics definitions in `docs/EDP1_METRICS_SPEC.md`.

## Changes
- `scripts/edp1/aggregate_results.py`
  - Added strict required-column validation (`max_accuracy`, `mean_accuracy`, core fitness columns).
  - Added explicit per-seed outputs for `final_max_accuracy` and `final_mean_accuracy`.
  - Added aggregate outputs:
    - `final_max_accuracy_mean`
    - `final_mean_accuracy_mean`
    - plus decomposition fields (`complexity`/`penalty`) when available.
  - Extended trajectory aggregation to include `max_accuracy_mean` and `mean_accuracy_mean`.
- `docs/EDP1_METRICS_SPEC.md`
  - Added canonical definitions and aggregation semantics.

## Verification
- `python scripts/edp1/aggregate_results.py --in results/edp1_exp0200_v2_staged --out results/edp1_exp0200_v2_staged/aggregates --phase0_generations 10` -> PASS
- `python scripts/analysis/verify_max_accuracy_discrepancy_1207a.py --root results/edp1_exp0200_v2_staged --out reports/analysis/TASK-1207A-METRICS-REPRO/metrics_repro_result_postfix.json` -> reporting FAIL remains (expected until errata)

## Status
- Aggregation/labeling fix: **PASS**
- Historical report inconsistency remains documented for errata phase.
