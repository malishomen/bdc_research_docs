# TASK-2005 BRIEF REPORT

## Scope
- Execute Pilot B (CPU symbolic) diagnostic baseline-vs-optimized runs (`N=10`).
- Compute paired CI and evaluate ADR-0013 diagnostic gate criteria.

## Changes
- Diagnostic runs executed via matrix runner.
- Paired CI extracted from:
  - `results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.json`

## Verification (L0)
- Command: `python scripts/analysis/applied_aggregate_exp0700.py --out_root results/exp_0700_applied --level diagnostic --out_json results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.json --out_csv results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.csv`
- Result: PASS

## Diagnostic result (Pilot B)
- `mean_delta_cpu = 0.09293265546483671`
- `CI95(delta_cpu) = [0.08906083916821825, 0.09680447176145518]`
- `stability_fail_rate = 0.0`
- ADR-0013 diagnostic gate verdict: **PASS**

## Artifacts
- `results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.json` (runtime)
- `results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.csv` (runtime)
- `reports/analysis/TASK-2005-PILOT-B-CPU-BASELINE-VS-OPT/TASK-2005_BRIEF_REPORT.md`

## Risks / Limitations
- Despite Pilot B PASS, ADR-0013 requires both pilots to pass before N=30 gate.

## Rollback
- `git revert <commit-hash-containing-task-2005>`
