# TASK-2105 BRIEF REPORT

## Scope
- Execute applied diagnostic rerun (`N=10`) for both pilots under ADR-0013 + ADR-0014.
- Use recovered GPU profile selected in TASK-2103 (`opt_amp_bs8`).
- Verify row-level run contract v3 and aggregate verdict prerequisites for gate.

## Changes
- Executed diagnostic matrix rerun at:
  - `results/exp_0700_applied_v2/diagnostic/...` (runtime only, not committed)
- Produced diagnostic aggregate:
  - `results/exp_0700_applied_v2/diagnostic/aggregates/exp0700_diagnostic_summary.json`
  - `results/exp_0700_applied_v2/diagnostic/aggregates/exp0700_diagnostic_summary.csv`

## Verification (L0)
- Command: `python scripts/applied/run_applied_matrix.py --level diagnostic --out_root results/exp_0700_applied_v2 --base_seed 1337 --seeds 10 --pilots all --gpu_optimized_amp_mode on --gpu_optimized_batch_size 8`
- Result: PASS
- Output summary: `{"event":"applied_matrix_done","level":"diagnostic","runs":40,"failure_count":0}`.

- Command: `python scripts/applied/replay_from_manifest.py --run_index "D:/projects/Bio_Digital_Core/Bio_digital_core/results/exp_0700_applied_v2/diagnostic/aggregates/run_index_v3.json"`
- Result: PASS
- Output summary: `run_index_v3_contract_ok`, `rows=40`, `missing_manifest_paths=0`.

- Command: `python scripts/analysis/applied_aggregate_exp0700.py --out_root results/exp_0700_applied_v2 --level diagnostic --out_json results/exp_0700_applied_v2/diagnostic/aggregates/exp0700_diagnostic_summary.json --out_csv results/exp_0700_applied_v2/diagnostic/aggregates/exp0700_diagnostic_summary.csv`
- Result: PASS
- Output summary: `{"event":"exp0700_aggregate_done","level":"diagnostic","gpu_pass":false,"cpu_pass":true}`.

- Command: `python -c "import json, pathlib; d=json.loads(pathlib.Path('D:/projects/Bio_Digital_Core/Bio_digital_core/results/exp_0700_applied_v2/diagnostic/aggregates/exp0700_diagnostic_summary.json').read_text(encoding='utf-8')); print(d['gpu']['verdict_pass'], d['gpu']['stats']['mean'], d['gpu']['stats']['ci95_low'], d['gpu']['stats']['stability_fail_rate']); print(d['cpu']['verdict_pass'], d['cpu']['stats']['mean'], d['cpu']['stats']['ci95_low'], d['cpu']['stats']['stability_fail_rate'])"`
- Result: PASS
- Output summary:
  - GPU: `verdict=False`, `mean_delta=0.31609`, `ci95_low=-0.67478`, `stability_fail_rate=0.0`
  - CPU: `verdict=True`, `mean_delta=0.09293`, `ci95_low=0.08906`, `stability_fail_rate=0.0`

## Artifacts
- `results/exp_0700_applied_v2/diagnostic/aggregates/run_index_v3.json` - contract-v3 run index.
- `results/exp_0700_applied_v2/diagnostic/aggregates/exp0700_diagnostic_summary.json` - rerun aggregate verdicts.
- `reports/analysis/TASK-2105-DIAGNOSTIC-RERUN-N10/TASK-2105_BRIEF_REPORT.md` - task report.

## Risks / Limitations
- GPU stability blocker (crash) is fixed (`failure_count=0`), but statistical gate criterion still fails (`ci95_low <= 0`).
- Per ADR-0014 stop-rules, gate N=30 is blocked.

## Rollback
- Revert with: `git revert <TASK-2105_commit_hash>`
