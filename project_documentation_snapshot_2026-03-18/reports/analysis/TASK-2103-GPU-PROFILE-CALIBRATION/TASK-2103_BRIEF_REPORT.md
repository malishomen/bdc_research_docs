# TASK-2103 BRIEF REPORT

## Scope
- Run mini calibration (`N=5`) for GPU optimized profile.
- Compare AMP on/off, batch-size variants, and choose one profile by fixed rule:
  1. `stability_fail_rate <= 0.10`
  2. maximize `mean_delta = baseline_val_loss - optimized_val_loss`.

## Changes
- Added calibration runner:
  - `scripts/applied/calibrate_gpu_profile.py`
- Updated ops note with selected profile:
  - `docs/ops/LOCAL_GPU_RUN_PROFILE.md`

## Verification (L0)
- Command: `python scripts/applied/calibrate_gpu_profile.py --out_root results/exp_0700_applied --base_seed 1337 --seeds 5`
- Result: PASS
- Output summary: `{"event":"task2103_calibration_done","chosen_profile":"opt_amp_bs8","selection_reason":"eligible_max_mean_delta"}`.

- Command: `python -c "import json, pathlib; d=json.loads(pathlib.Path('results/exp_0700_applied/calibration_gpu_task2103/aggregates/gpu_profile_calibration_summary.json').read_text(encoding='utf-8')); print(d['chosen_profile'], [(p['profile'], p['stability_fail_rate'], p['stats']['mean']) for p in d['optimized_profiles']])"`
- Result: PASS
- Output summary:
  - `opt_amp_bs12`: fail_rate `0.0`, mean_delta `-7.63e-05`
  - `opt_fp32_bs12`: fail_rate `0.0`, mean_delta `0.0`
  - `opt_amp_bs8`: fail_rate `0.0`, mean_delta `0.61786` (chosen by rule).

## Artifacts
- `scripts/applied/calibrate_gpu_profile.py` - calibration runner for GPU optimized profiles.
- `docs/ops/LOCAL_GPU_RUN_PROFILE.md` - selected profile update and fallback.
- `results/exp_0700_applied/calibration_gpu_task2103/aggregates/gpu_profile_calibration_summary.json` - runtime summary (not committed).
- `results/exp_0700_applied/calibration_gpu_task2103/aggregates/gpu_profile_calibration_rows.csv` - runtime seed-level table (not committed).

## Risks / Limitations
- `opt_amp_bs8` has wide CI (`ci95_low < 0`) despite positive mean; this is acceptable for calibration selection but not for gate decisions.
- Calibration uses `N=5`; gate admission still depends on full diagnostic rerun rules from ADR-0013/ADR-0014.

## Rollback
- Revert with: `git revert <TASK-2103_commit_hash>`
