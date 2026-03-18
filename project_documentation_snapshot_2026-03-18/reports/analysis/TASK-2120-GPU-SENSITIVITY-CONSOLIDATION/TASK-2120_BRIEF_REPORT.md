# TASK-2120 BRIEF REPORT

## Scope
- Consolidate GPU root-cause evidence across TASK-2100, TASK-2110, TASK-2113 and EXP-0700 v3 diagnostic aggregate.
- Quantify per-seed sensitivity impact on `CI95_low(delta_gpu)`.

## Changes
- Added machine-readable sensitivity artifacts:
  - `reports/analysis/TASK-2120-GPU-SENSITIVITY-CONSOLIDATION/gpu_seed_sensitivity.json`
  - `reports/analysis/TASK-2120-GPU-SENSITIVITY-CONSOLIDATION/gpu_seed_sensitivity.csv`
- Added this report.

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/task2110_gpu_variance_decomposition.py`
- Result: PASS

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/exp_0700_applied_v3/diagnostic/aggregates/exp0700_diagnostic_summary.json').read_text(encoding='utf-8')); print(d['gpu']['stats']['mean'], d['gpu']['stats']['ci95_low'])"`
- Result: PASS
- Output summary: `0.7992378234863253 -0.17206888915672247`

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('reports/analysis/TASK-2120-GPU-SENSITIVITY-CONSOLIDATION/gpu_seed_sensitivity.json').read_text(encoding='utf-8')); print(d['baseline_stats']['ci95_low'], d['negative_delta_seeds'])"`
- Result: PASS
- Output summary: two dominant negative seeds: `1339`, `1342`.

## Artifacts
- `reports/analysis/TASK-2120-GPU-SENSITIVITY-CONSOLIDATION/gpu_seed_sensitivity.json` - ranked seed impact on CI lower bound (leave-one-out shifts).
- `reports/analysis/TASK-2120-GPU-SENSITIVITY-CONSOLIDATION/gpu_seed_sensitivity.csv` - tabular seed-level sensitivity.
- `reports/analysis/TASK-2120-GPU-SENSITIVITY-CONSOLIDATION/TASK-2120_BRIEF_REPORT.md` - task report.

## Risks / Limitations
- This task is analytical and does not change execution policy. Governance fix is required before rerun (TASK-2121).
- Sensitivity findings are specific to v3 profile and current seed policy.

## Rollback
- Revert with: `git revert <TASK-2120_commit_hash>`
