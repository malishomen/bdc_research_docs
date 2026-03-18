# TASK-0142-FIX BRIEF REPORT — exp_0017 crash-safe artifacts + 4x5min validation runs (GPU/CPU) + quaternary verdict via policy exit code

Branch/HEAD: `test` @ `bb8780a33f3bca38a7b21e4aeaacf9f2b9c92e36`

## Incident (TASK-0142 6h Run Outcome)

Run tag: `task0142_6h`

Run dir:
- `logs/exp_0017_comprehension_v0_cloze/run_20260208T215517Z_ebf32b3_task0142_6h`

Observed contents (L0):
- contains **only** `RUN_METADATA.json` (no `metrics_by_step.jsonl`, no `RUN_STATUS.json`, no `metrics.json`, no `CRASH.json`)

Policy eval (requires `metrics.json`) therefore errors:
```powershell
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0142_6h `
  --require_integrity `
  --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --require_sanity
```
Result: `exit_code=1` with problem `missing metrics.json`.

## Fix Implemented (Crash-Safe Artifacts; No Training Semantics Changes)

File changed:
- `experiments/exp_0017_comprehension_v0_cloze/src/train.py`

Guarantees added:
- `metrics_by_step.jsonl` is created immediately at run start and begins with a `RUN_START` JSON line (flush + fsync).
- `RUN_STATUS.json` heartbeat is written atomically (temp + `os.replace`, flush + fsync) and updates at least every ~30 seconds while RUNNING.
- On any exception/KeyboardInterrupt: write `CRASH.json` atomically and set `RUN_STATUS.json` to `CRASHED`.
- On normal completion: write `metrics.json` atomically and set `RUN_STATUS.json` to `COMPLETED`.

New helper tool (optional verifier):
- `tools/analysis/exp0017_artifact_integrity_check.py` (checks presence + RUN_START + terminal artifact; optional sha256)

Unit test:
- `tests/test_exp0017_crash_safe_artifacts.py` (synthetic tempdir: RUN_START + CRASH.json)

## 4 Validation Runs (All Artifacts Present)

Dataset root (external-only; pinned):
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

Run output dirs are under `logs/` (gitignored). Launcher logs were captured with `Tee-Object` under:
- `logs/exp_0017_comprehension_v0_cloze/_launchers/`

### 1) GPU time-budget 5m

- tag: `task0142_fix_gpu_time5m`
- run_dir: `logs/exp_0017_comprehension_v0_cloze/run_20260209T052515Z_bb8780a_task0142_fix_gpu_time5m`
- launcher_log: `logs/exp_0017_comprehension_v0_cloze/_launchers/launcher_20260209T052511Z_task0142_fix_gpu_time5m.log`
- final_step: `2259`
- RUN_STATUS: `COMPLETED` (wall_s≈`342.059`)
- final metrics: `val_acc=0.128066`, `test_acc=0.125139`, `shuffled_val_acc=0.027647`
- sha256:
  - `metrics_by_step.jsonl`: `5c41586d164f094ad0ba6f57b3b2bf1c3027fed532d6c66df7b79e91b7d665e2`
  - `RUN_STATUS.json`: `24932efc9775b2bec57a8baa574ba67a3ed3f6c1df796768d580fa9d29ecc2ac`
  - `metrics.json`: `e48170a32e11a187d6bc758bcda68f5ce2706682ec438c76bb8db70718a60dde`

### 2) GPU steps (forced eval)

- tag: `task0142_fix_gpu_steps`
- run_dir: `logs/exp_0017_comprehension_v0_cloze/run_20260209T053102Z_bb8780a_task0142_fix_gpu_steps`
- launcher_log: `logs/exp_0017_comprehension_v0_cloze/_launchers/launcher_20260209T053058Z_task0142_fix_gpu_steps.log`
- final_step: `250`
- RUN_STATUS: `COMPLETED` (wall_s≈`132.735`)
- final metrics: `val_acc=0.095731`, `test_acc=0.093608`, `shuffled_val_acc=0.027647`
- sha256:
  - `metrics_by_step.jsonl`: `9ee6c75101ad6fbb013420cc68b7f2a17778bbd9dd8452128edc97831cf40341`
  - `RUN_STATUS.json`: `30c5b29f8d1443f342aab06b15c2e7e10c2940cab3435595ed14fa6affff180b`
  - `metrics.json`: `c6a4651eb2f8ee40d9687dccfa3c9a0dad7898949ee5d6222c84099ce49ae018`

### 3) CPU time-budget 5m

- tag: `task0142_fix_cpu_time5m`
- run_dir: `logs/exp_0017_comprehension_v0_cloze/run_20260209T053319Z_bb8780a_task0142_fix_cpu_time5m`
- launcher_log: `logs/exp_0017_comprehension_v0_cloze/_launchers/launcher_20260209T053315Z_task0142_fix_cpu_time5m.log`
- final_step: `81`
- RUN_STATUS: `COMPLETED` (wall_s≈`464.874`)
- final metrics: `val_acc=0.044307`, `test_acc=0.042720`, `shuffled_val_acc=0.027647`
- sha256:
  - `metrics_by_step.jsonl`: `6dc9865f3052e43f26b0d15c60cf6581ba6a11cdbef66c0404d80606f5b365d2`
  - `RUN_STATUS.json`: `2ad7063ea1b363205e84305a92e163bb0be8b353cc832057400f3432ba3b5f83`
  - `metrics.json`: `4153cc757d901b8aa4fcbdd820864249f7500b5ad1bb7d8d8c4e1a09bc4fe900`

### 4) Hybrid_quat 5m (GPU train; CPU policy eval; quaternary derived only from exit code)

- tag: `task0142_fix_hybrid_quat5m`
- run_dir: `logs/exp_0017_comprehension_v0_cloze/run_20260209T054109Z_bb8780a_task0142_fix_hybrid_quat5m`
- launcher_log: `logs/exp_0017_comprehension_v0_cloze/_launchers/launcher_20260209T054105Z_task0142_fix_hybrid_quat5m.log`
- final_step: `1705`
- RUN_STATUS: `COMPLETED` (wall_s≈`346.508`)
- final metrics: `val_acc=0.111431`, `test_acc=0.108788`, `shuffled_val_acc=0.027647`
- sha256:
  - `metrics_by_step.jsonl`: `b98e173a1eaa42891900438e498aba337c0e068827aa8af14814468800f557fb`
  - `RUN_STATUS.json`: `8dc7bb9b0e64dc5459ab23985cdb668c5ecb03e0fd4794cf44fa80e05fa75db2`
  - `metrics.json`: `9aabfa3091fc0633304c9ee7f71b71a1b31fefa4d32c470cfa7867541ce473e2`

Policy eval:
- command:
```powershell
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0142_fix_hybrid_quat5m `
  --require_integrity `
  --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --require_sanity
```
- result: `exit_code=2` (problem: `KC_IMPROVEMENT: FAIL ... delta=-0.006155 need>=0.020`)

Quaternary mapping (derived only from exit code):
- `2 -> NO`

## Quick Verification Commands

Artifact integrity (per run_dir):
```powershell
python tools/analysis/exp0017_artifact_integrity_check.py --run_dir <RUN_DIR> --hash
```

Smoke crash-path (synthetic; unit test):
```powershell
pytest -q tests/test_exp0017_crash_safe_artifacts.py
```
