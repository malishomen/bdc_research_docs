# Practical Readiness Decision v2 (TASK-2107)

Date: 2026-03-04  
Branch: `test`  
Governance: ADR-0013 + ADR-0014

## Decision
- **Applied verdict (v2 iteration): FAIL**

## Basis

From TASK-2105 diagnostic rerun (`N=10`):
- GPU pilot:
  - `verdict_pass = false`
  - `mean_delta = 0.3160929362`
  - `ci95 = [-0.6747752261, 1.3069610985]`
  - `stability_fail_rate = 0.0`
- CPU pilot:
  - `verdict_pass = true`
  - `mean_delta = 0.0929326555`
  - `ci95 = [0.0890608392, 0.0968044718]`
  - `stability_fail_rate = 0.0`

Gate prerequisite for TASK-2106 requires both pilot verdicts `True`.  
Condition not met (`gpu=False`, `cpu=True`) => gate N=30 is not allowed.

## Interpretation
- GPU technical crash blocker from TASK-2004 is resolved (no runtime failures in rerun).
- Statistical readiness criterion for GPU pilot remains unmet in this iteration.

## Scope Guard
- **Scientific baseline unchanged:** Phase 4 remains `RUN COMPLETE / GATE FAIL`.
- This document applies only to the parallel applied track.

## Next
- Open a new applied-iteration task to improve GPU uplift robustness without changing ADR-0013 thresholds.
