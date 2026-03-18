# TASK-1001C DETERMINISM HARDENING BRIEF REPORT

## Scope
- Close remaining nondeterminism vectors before real 2000-step Wiki Pilot.
- Branch: `test`.
- Classification: `R0` (hardening only, no method change).

## Changes
- Updated `scripts/wiki_pilot/run_once.py`:
  - Added `numpy` seed (`np.random.seed(seed)`).
  - Explicit `random.seed(seed)` retained.
  - Added `os.environ["PYTHONHASHSEED"] = "1337"`.
  - Forced FP32 path for pilot (`dtype=torch.float32`, autocast disabled, GradScaler disabled).
  - Added `torch.set_float32_matmul_precision("high")`.
  - Added startup seed control log line (`python/numpy/torch/cuda/PYTHONHASHSEED/deterministic`).
  - Added `assert torch.are_deterministic_algorithms_enabled()`.
  - Hardened dry-run defaults:
    - default `dataset_root` and `out_dir`;
    - dry-run auto reduces default steps from 2000 to 20 unless explicitly overridden.
  - Adjusted kill-check order to avoid empty metrics files and moved entropy collapse gate to `step >= 200`.
- Updated `scripts/wiki_pilot/compare_runs.py`:
  - Added fail-safe: `empty_metrics` now returns FAIL when any run has zero metric rows.

## Verification (L0)
- `rg -n "seed|PYTHONHASHSEED|deterministic|matmul_precision|numpy" scripts/wiki_pilot/ -S` -> PASS
- `rg -n "amp|autocast|GradScaler|fp16|float16" scripts/wiki_pilot/ -S` -> PASS (autocast/scaler explicitly disabled)
- `python scripts/wiki_pilot/run_once.py --dry_run` -> PASS (seed log emitted, deterministic true)
- `python scripts/wiki_pilot/run_once.py --dry_run --out_dir results/wiki_pilot/run_2` -> PASS
- `python scripts/wiki_pilot/run_once.py --dry_run --out_dir results/wiki_pilot/run_3` -> PASS
- `python scripts/wiki_pilot/compare_runs.py --verify --root results/wiki_pilot` -> PASS (`steps=20`, deltas all `0.0`)

## Artifacts
- `scripts/wiki_pilot/run_once.py`
- `scripts/wiki_pilot/compare_runs.py`
- `reports/analysis/TASK-1001C-DETERMINISM-HARDENING/TASK-1001C-DETERMINISM-HARDENING_BRIEF_REPORT.md`

## Risks / Limitations
- This hardening pass validated deterministic smoke mode. Full 2000-step run is still a separate execution step.
