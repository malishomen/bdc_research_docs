# TASK-2004 BRIEF REPORT

## Scope
- Execute Pilot A (GPU) diagnostic baseline-vs-optimized runs (`N=10`).
- Compute paired CI and evaluate ADR-0013 diagnostic gate criteria.

## Changes
- Executed GPU diagnostic matrix through unified runner.
- Aggregated paired deltas in:
  - `results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.json`

## Verification (L0)
- Command: `python scripts/applied/run_applied_matrix.py --level diagnostic --out_root results/exp_0700_applied --base_seed 1337 --seeds 10 --pilots all`
- Result: PARTIAL (runner completed but reported failures, expected for gate assessment)
- Failure summary:
  - `failure_count=6` (all in `pilot=gpu`, `variant=optimized`)
  - error signature: assertion failure in `scripts/wiki_pilot/run_once.py` (`softmax probabilities must sum to ~1`)

- Command: `python scripts/analysis/applied_aggregate_exp0700.py --out_root results/exp_0700_applied --level diagnostic --out_json results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.json --out_csv results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.csv`
- Result: PASS

## Diagnostic result (Pilot A)
- `mean_delta_gpu = -6.675720215199021e-05`
- `CI95(delta_gpu) = [-7.366727137305437e-05, -5.984713293092605e-05]`
- `stability_fail_rate = 0.6`
- ADR-0013 diagnostic gate verdict: **FAIL**

## Artifacts
- `results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.json` (runtime)
- `results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.csv` (runtime)
- `results/exp_0700_applied/diagnostic/aggregates/run_index_v2.json` (runtime)
- `reports/analysis/TASK-2004-PILOT-A-GPU-BASELINE-VS-OPT/TASK-2004_BRIEF_REPORT.md`

## Risks / Limitations
- GPU optimized arm is unstable under current config; stop-rule triggered.
- No post-hoc threshold relaxation is allowed by ADR-0013.

## Rollback
- `git revert <commit-hash-containing-task-2004>`
