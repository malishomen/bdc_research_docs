# TASK-2110 BRIEF REPORT

## Scope
- Decompose GPU pilot variance using baseline artifacts from failing diagnostic `N=10`.
- Quantify within-seed vs between-seed variance on selected seeds (`fail/median/best`).
- Produce one unambiguous root-cause verdict.

## Changes
- Added decomposition script:
  - `scripts/analysis/task2110_gpu_variance_decomposition.py`
- Produced machine-readable artifacts:
  - `reports/analysis/TASK-2110-GPU-VARIANCE-DECOMPOSITION/gpu_variance_decomposition.json`
  - `reports/analysis/TASK-2110-GPU-VARIANCE-DECOMPOSITION/gpu_variance_decomposition_rows.csv`

## Verification (L0)
- Command: `python -c "import json,pathlib; p=pathlib.Path('results/exp_0700_applied/diagnostic/aggregates/exp0700_diagnostic_summary.json'); d=json.loads(p.read_text(encoding='utf-8')); print(d['gpu']['stats']['mean'], d['gpu']['stats']['ci95_low'], d['gpu']['stats']['ci95_high'], d['gpu']['stats']['stability_fail_rate'])"`
- Result: PASS
- Output summary: baseline confirmed (`-6.6757e-05`, CI95 `[-7.37e-05,-5.98e-05]`, fail rate `0.6`).

- Command: `python scripts/analysis/task2110_gpu_variance_decomposition.py --baseline_root results/exp_0700_applied/diagnostic/gpu --out_root results/.tmp_task2110_variance --seeds 1337,1339,1343 --repeats 5`
- Result: PASS
- Output summary: `dominant_source=seed_or_protocol_sensitivity`, `within_mean=0.0`, `between_var=2.587e-11`, `ratio=0.0`.

- Command: `python -c "import json,pathlib; d=json.loads(pathlib.Path('reports/analysis/TASK-2110-GPU-VARIANCE-DECOMPOSITION/gpu_variance_decomposition.json').read_text(encoding='utf-8')); print(d['decomposition']['within_seed_variance_mean'], d['decomposition']['between_seed_variance'], d['verdict']['dominant_source'])"`
- Result: PASS

## Artifacts
- `scripts/analysis/task2110_gpu_variance_decomposition.py` - repeat runner + decomposition calculator.
- `reports/analysis/TASK-2110-GPU-VARIANCE-DECOMPOSITION/gpu_variance_decomposition.json` - decomposition payload with verdict.
- `reports/analysis/TASK-2110-GPU-VARIANCE-DECOMPOSITION/gpu_variance_decomposition_rows.csv` - seed/repeat-level table.
- `reports/analysis/TASK-2110-GPU-VARIANCE-DECOMPOSITION/TASK-2110_BRIEF_REPORT.md` - task report.

## Risks / Limitations
- This decomposition used current executable code against baseline artifacts from earlier failing run; it isolates variance source but does not by itself guarantee gate pass.
- Fail seed from baseline (`1337`) now completes in repeats, indicating technical blocker removal, while statistical uplift robustness remains unresolved.

## Rollback
- Revert with: `git revert <TASK-2110_commit_hash>`
