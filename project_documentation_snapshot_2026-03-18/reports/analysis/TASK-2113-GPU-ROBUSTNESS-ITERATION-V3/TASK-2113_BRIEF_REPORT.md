# TASK-2113 BRIEF REPORT

## Scope
- Apply minimal GPU stabilizers without changing ADR-0013 metrics.
- Rerun full diagnostic `N=10` (GPU+CPU) and evaluate gate condition.

## Changes
- Updated `scripts/wiki_pilot/run_once.py`:
  - AMP FP32 critical path option for loss/softmax (`--fp32_critical_path`).
  - Tunable stabilizers:
    - `--grad_clip_norm`
    - `--amp_init_scale`
    - `--amp_growth_factor`
    - `--amp_backoff_factor`
    - `--amp_growth_interval`
- Updated `scripts/applied/run_applied_matrix.py`:
  - GPU override flags for robustness protocol:
    - `--gpu_optimized_fp32_critical_path`
    - `--gpu_optimized_grad_clip_norm`
    - `--gpu_optimized_amp_init_scale`
    - `--gpu_optimized_amp_growth_interval`
    - `--gpu_validation_interval`

## Verification (L0)
- Command: `python -m py_compile scripts/wiki_pilot/run_once.py scripts/applied/run_applied_matrix.py tests/test_exp0700_numeric_guardrails.py`
- Result: PASS

- Command: `pytest -q tests/test_exp0700_numeric_guardrails.py`
- Result: PASS (`4 passed`)

- Command: `python scripts/applied/run_applied_matrix.py --level diagnostic --out_root results/exp_0700_applied_v3 --base_seed 1337 --seeds 10 --pilots all --gpu_validation_interval 20 --gpu_optimized_amp_mode on --gpu_optimized_batch_size 8 --gpu_optimized_steps 120 --gpu_optimized_lr 2e-5 --gpu_optimized_fp32_critical_path --gpu_optimized_grad_clip_norm 0.8 --gpu_optimized_amp_init_scale 2048 --gpu_optimized_amp_growth_interval 400`
- Result: PASS
- Output summary: `failure_count=0`.

- Command: `python scripts/applied/replay_from_manifest.py --run_index D:/projects/Bio_Digital_Core/Bio_digital_core/results/exp_0700_applied_v3/diagnostic/aggregates/run_index_v3.json`
- Result: PASS (`run_index_v3_contract_ok`, `rows=40`).

- Command: `python scripts/analysis/applied_aggregate_exp0700.py --out_root results/exp_0700_applied_v3 --level diagnostic --out_json results/exp_0700_applied_v3/diagnostic/aggregates/exp0700_diagnostic_summary.json --out_csv results/exp_0700_applied_v3/diagnostic/aggregates/exp0700_diagnostic_summary.csv`
- Result: PASS
- Output summary: `gpu_pass=false`, `cpu_pass=true`.

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/exp_0700_applied_v3/diagnostic/aggregates/exp0700_diagnostic_summary.json').read_text(encoding='utf-8')); print(d['gpu']['stats']['mean'], d['gpu']['stats']['ci95_low'], d['gpu']['stats']['stability_fail_rate'], d['gpu']['verdict_pass']); print(d['cpu']['stats']['mean'], d['cpu']['stats']['ci95_low'], d['cpu']['stats']['stability_fail_rate'], d['cpu']['verdict_pass'])"`
- Result: PASS
- Output summary:
  - GPU: `mean=0.79924`, `ci95_low=-0.17207`, `stability_fail_rate=0.0`, `verdict=False`
  - CPU: `mean=0.09293`, `ci95_low=0.08906`, `stability_fail_rate=0.0`, `verdict=True`

## Verdict
- **TASK-2113 status: FAILURE (stop-rule triggered)**
  - Technical blocker resolved (`failure_count=0`), but gate criterion not met (`CI95_low(delta_gpu) <= 0`).
  - Proceeding to `TASK-2114` is not allowed.

## Artifacts
- `scripts/wiki_pilot/run_once.py`
- `scripts/applied/run_applied_matrix.py`
- `reports/analysis/TASK-2113-GPU-ROBUSTNESS-ITERATION-V3/TASK-2113_BRIEF_REPORT.md`
- Runtime outputs (not committed):
  - `results/exp_0700_applied_v3/diagnostic/aggregates/run_index_v3.json`
  - `results/exp_0700_applied_v3/diagnostic/aggregates/exp0700_diagnostic_summary.json`

## Risks / Limitations
- Two seeds remain negative on GPU optimized arm (`1339`, `1342`), dominating CI lower bound.
- Additional optimization hypothesis is required for next iteration.

## Rollback
- Revert with: `git revert <TASK-2113_commit_hash>`
