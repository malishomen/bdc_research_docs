# TASK-2126 BRIEF REPORT

## Scope
- Execute gate `N=30` for applied v4 under fixed GPU profile contract.
- Validate run-index v4 and aggregate CI on gate-level artifacts.

## Changes
- Runtime outputs generated (not committed):
  - `results/exp_0700_applied_v4_gpu_gate/gate/gpu/...`
  - `results/exp_0700_applied_v4_gpu_gate/gate/aggregates/run_index_v4.json`
  - `results/exp_0700_applied_v4_gpu_gate/gate/aggregates/exp0700_gate_summary.json|csv`
- Added this report.

## Verification (L0)
- Command: `python scripts/applied/run_applied_matrix.py --level gate --out_root results/exp_0700_applied_v4_gpu_gate --base_seed 1337 --seeds 30 --pilots gpu --gpu_profile_id gpu_opt_amp_bs8_steps120_lr3e5_fp32crit_clip1 --gpu_validation_interval 20`
- Result: PASS
- Output summary: `runs=60`, `failure_count=0`.

- Command: `python scripts/applied/replay_from_manifest.py --run_index results/exp_0700_applied_v4_gpu_gate/gate/aggregates/run_index_v4.json`
- Result: PASS
- Output summary: `schema=run-index-v4`, `rows=60`, `missing_manifest_paths=0`.

- Command: `python scripts/analysis/applied_aggregate_exp0700.py --out_root results/exp_0700_applied_v4_gpu_gate --level gate --out_json results/exp_0700_applied_v4_gpu_gate/gate/aggregates/exp0700_gate_summary.json --out_csv results/exp_0700_applied_v4_gpu_gate/gate/aggregates/exp0700_gate_summary.csv`
- Result: PASS

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/exp_0700_applied_v4_gpu_gate/gate/aggregates/exp0700_gate_summary.json').read_text(encoding='utf-8')); print(d['gpu']['verdict_pass'], d['gpu']['stats']['mean'], d['gpu']['stats']['ci95_low'], d['gpu']['stats']['stability_fail_rate'])"`
- Result: PASS
- Output summary: `gpu.verdict_pass=True`, `mean_delta=1.3836773343`, `ci95_low=0.9475860640`, `stability_fail_rate=0.0`.

## Notes on Scope
- This gate run executed the qualifying GPU pilot under ADR-0013/0015 metrics.
- CPU gate arm was not executed in this task; CPU diagnostic carry-forward remained valid for transition checks.

## Artifacts
- `reports/analysis/TASK-2126-APPLIED-GATE-N30-V4/TASK-2126_BRIEF_REPORT.md`

## Risks / Limitations
- If policy requires symmetric N=30 execution for all pilots, a separate CPU gate run task is required.

## Rollback
- Runtime artifacts only; code rollback not required for this task.
