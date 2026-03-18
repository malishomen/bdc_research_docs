# TASK-4500 BRIEF REPORT

## Scope
- Execute final reproducibility run for Phase-4 locked reference GPU profile (`N=30`, seeds `1337..1366`).

## Changes
- Added reproducibility runner:
  - `scripts/applied/run_phase4_repro_reference.py`
- Produced runtime artifacts (not committed):
  - `results/repro_run/per_seed_metrics.csv`
  - `results/repro_run/aggregate_metrics.json`
  - `results/repro_run/CI_report.md`

## Verification (L0)
- Command: `python scripts/applied/run_phase4_repro_reference.py --base_seed 1337 --seeds 30 --out_root results/repro_run --baseline_root results/exp_0700_applied_v4_gpu_gate/gate/gpu/baseline --profile_path configs/profiles/gpu_profile_v4_reference.yaml --validation_interval 20`
- Result: PASS
- Output summary: `n_rows=30`, `pass=true`.
- Command: `python -c "import json, pathlib; d=json.loads(pathlib.Path('results/repro_run/aggregate_metrics.json').read_text()); print(d['stats']['ci95_low'], d['negative_seed_rate'], d['pass'])"`
- Result: PASS
- Output summary:
  - `ci95_low = 0.9233480782 > 0`
  - `negative_seed_rate = 0.1666666667 < 0.25`
  - `pass = True`

## Artifacts
- `scripts/applied/run_phase4_repro_reference.py` - locked-profile reproducibility runner.
- `results/repro_run/per_seed_metrics.csv` - per-seed paired deltas.
- `results/repro_run/aggregate_metrics.json` - aggregate CI + robustness metrics.
- `results/repro_run/CI_report.md` - human-readable reproducibility summary.

## Risks / Limitations
- Repro run used existing baseline losses from v4 gate baseline roots for paired delta computation.

## Rollback
- `git revert <commit_hash>`
