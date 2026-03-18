# TASK-2002 BRIEF REPORT

## Scope
- Implement unified CPU/GPU run-contract (manifest v2), matrix runner, and reproducible replay path.

## Changes
- Added:
  - `scripts/applied/run_applied_matrix.py`
  - `scripts/applied/replay_from_manifest.py`
  - `scripts/analysis/applied_aggregate_exp0700.py`
  - `scripts/applied/run_applied_smoke_suite.py`

## Verification (L0)
- Command: `python -m py_compile scripts/applied/run_applied_matrix.py scripts/applied/replay_from_manifest.py scripts/applied/run_applied_smoke_suite.py scripts/analysis/applied_aggregate_exp0700.py`
- Result: PASS

- Command: `python scripts/applied/run_applied_matrix.py --level smoke --out_root results/exp_0700_applied --base_seed 1337 --seeds 1 --pilots cpu`
- Result: PASS (`failure_count=0`)

- Command: `python scripts/applied/replay_from_manifest.py --manifest results/exp_0700_applied/smoke/cpu/baseline/seed_1337/run_manifest_v2.json --execute`
- Result: PASS (run successfully reproduced from manifest command)

- Command: `python scripts/analysis/applied_aggregate_exp0700.py --out_root results/exp_0700_applied --level smoke --out_json results/exp_0700_applied/smoke/aggregates/exp0700_smoke_summary.json --out_csv results/exp_0700_applied/smoke/aggregates/exp0700_smoke_summary.csv`
- Result: PASS

## Artifacts
- `scripts/applied/run_applied_matrix.py`
- `scripts/applied/replay_from_manifest.py`
- `scripts/analysis/applied_aggregate_exp0700.py`
- `scripts/applied/run_applied_smoke_suite.py`
- `reports/analysis/TASK-2002-RUN-CONTRACT-AND-PROVENANCE-V2/TASK-2002_BRIEF_REPORT.md`

## Risks / Limitations
- GPU metric parsing depends on `run_once.py` output schema (`run_summary.json`, `metrics.csv`).
- Manifest replay reproduces command path; exact runtime equivalence still depends on environment stability.

## Rollback
- `git revert <commit-hash-containing-task-2002>`
