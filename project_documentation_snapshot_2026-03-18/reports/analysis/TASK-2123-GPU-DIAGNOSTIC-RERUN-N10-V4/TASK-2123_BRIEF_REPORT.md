# TASK-2123 BRIEF REPORT

## Scope
- Execute official GPU-only diagnostic rerun `N=10` using contract v4 and pre-registered profile id.
- Validate row-level run contract and recompute aggregate CI.

## Changes
- Runtime outputs generated (not committed):
  - `results/exp_0700_applied_v4/diagnostic/gpu/...`
  - `results/exp_0700_applied_v4/diagnostic/aggregates/run_index_v4.json`
  - `results/exp_0700_applied_v4/diagnostic/aggregates/exp0700_diagnostic_summary.json|csv`
- Added this report.

## Verification (L0)
- Command: `python scripts/applied/run_applied_matrix.py --level diagnostic --out_root results/exp_0700_applied_v4 --base_seed 1337 --seeds 10 --pilots gpu --gpu_profile_id gpu_opt_amp_bs8_steps120_lr3e5_fp32crit_clip1 --gpu_validation_interval 20`
- Result: PASS
- Output summary: `runs=20`, `failure_count=0`.

- Command: `python scripts/applied/replay_from_manifest.py --run_index results/exp_0700_applied_v4/diagnostic/aggregates/run_index_v4.json`
- Result: PASS
- Output summary: `schema=run-index-v4`, `rows=20`, `missing_manifest_paths=0`.

- Command: `python scripts/analysis/applied_aggregate_exp0700.py --out_root results/exp_0700_applied_v4 --level diagnostic --out_json results/exp_0700_applied_v4/diagnostic/aggregates/exp0700_diagnostic_summary.json --out_csv results/exp_0700_applied_v4/diagnostic/aggregates/exp0700_diagnostic_summary.csv`
- Result: PASS

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/exp_0700_applied_v4/diagnostic/aggregates/exp0700_diagnostic_summary.json').read_text(encoding='utf-8')); print(d['gpu']['verdict_pass'], d['gpu']['stats']['mean'], d['gpu']['stats']['ci95_low'], d['gpu']['stats']['stability_fail_rate'])"`
- Result: PASS
- Output summary: `gpu.verdict_pass=True`, `mean_delta=1.5488766988`, `ci95_low=0.5886021347`, `stability_fail_rate=0.0`.

## Artifacts
- `reports/analysis/TASK-2123-GPU-DIAGNOSTIC-RERUN-N10-V4/TASK-2123_BRIEF_REPORT.md` - task report.

## Risks / Limitations
- CPU pilot was intentionally not rerun in this task (GPU-only scope).
- Gate transition requires TASK-2124 + TASK-2125 governance decision.

## Rollback
- Runtime artifacts only; code rollback not required for this task.
