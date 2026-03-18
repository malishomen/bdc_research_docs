# TASK-2003 BRIEF REPORT

## Scope
- Run parity smoke suite across GPU and CPU pilots before diagnostic N=10.
- Validate artifacts/schema/determinism and detect silent fallback.

## Changes
- Executed smoke suite via:
  - `scripts/applied/run_applied_smoke_suite.py`
- Generated runtime artifact:
  - `results/exp_0700_applied/smoke/aggregates/smoke_suite.json`

## Verification (L0)
- Command: `python scripts/applied/run_applied_smoke_suite.py --out_root results/exp_0700_applied --base_seed 1337`
- Result: PASS
- Output summary:
  - `status=PASS`
  - `determinism_gpu=true`
  - `determinism_cpu=true`
  - `fallback_ok=true`
  - `schema_ok=true`

## Artifacts
- `results/exp_0700_applied/smoke/aggregates/smoke_suite.json` (runtime)
- `results/exp_0700_applied/smoke/aggregates/exp0700_smoke_summary.json` (runtime)
- `results/exp_0700_applied/smoke/aggregates/exp0700_smoke_summary.csv` (runtime)
- `reports/analysis/TASK-2003-GPU-CPU-PARITY-SMOKE-SUITE/TASK-2003_BRIEF_REPORT.md`

## Risks / Limitations
- Smoke PASS does not imply diagnostic or gate success; it only validates preflight pipeline integrity.

## Rollback
- `git revert <commit-hash-containing-task-2003>`
