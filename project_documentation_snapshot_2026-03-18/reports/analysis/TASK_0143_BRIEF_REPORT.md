# TASK-0143 BRIEF REPORT — exp_0017 DataLoader throughput knobs + RUN_METADATA traceability + 45m quality run (batch_size=32 unchanged)

Branch/HEAD: `test` @ `388b8b4d07e63b2afe46470d7435e3b0b189718d`

## Change Summary (No Semantics Changes)

File changed:
- `experiments/exp_0017_comprehension_v0_cloze/src/train.py`

Added input-pipeline knobs (performance-only; logged to `RUN_METADATA.json`):
- `--num_workers` (default `2`)
- `--pin_memory/--no-pin_memory` (default: `True` on CUDA, else `False`)
- `--prefetch_factor` (default `2`)
- `--persistent_workers/--no-persistent_workers` (default: `True` if `num_workers>0`)

Crash-safe artifact guarantees from TASK-0142-FIX preserved:
- `metrics_by_step.jsonl` starts with `RUN_START` and is fsync’d
- `RUN_STATUS.json` heartbeat (atomic writes)
- terminal artifact: `metrics.json` or `CRASH.json`

## 45m Quality Run (GPU; batch_size unchanged)

Dataset integrity gate:
- `KC_DATA_INTEGRITY: PASS` (docs.jsonl sha256 matches derived manifest)

Command (stdout/stderr tee’d):
```powershell
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --device cuda `
  --seed 12345 `
  --time_budget_minutes 45 `
  --max_steps 100000000 `
  --eval_every 1000 `
  --log_every 200 `
  --num_workers 4 `
  --pin_memory `
  --prefetch_factor 2 `
  --persistent_workers `
  --run_tag task0143_quality_45m_io
```

Run outputs (gitignored):
- run_dir: `logs/exp_0017_comprehension_v0_cloze/run_20260209T063040Z_388b8b4_task0143_quality_45m_io`
- launcher log: `logs/exp_0017_comprehension_v0_cloze/_launchers/launcher_20260209T063036Z_task0143_quality_45m_io.log`
- GPU util log (nvidia-smi, 5s): `logs/exp_0017_comprehension_v0_cloze/_launchers/nvidia_smi_20260209T063036Z_task0143_quality_45m_io.csv`

RUN_METADATA (training block):
- `batch_size=32`
- `num_workers=4`
- `pin_memory=true`
- `prefetch_factor=2`
- `persistent_workers=true`

Completion:
- `TIME_BUDGET_REACHED step=32306 budget_minutes=45`

Final metrics (`metrics.json`):
- `val_acc=0.4936300094` (k=58546, n=118603)
- `test_acc=0.4740753906` (k=58682, n=123782)
- shuffled baseline `val_acc=0.0276468555`
- `verdict_kc_sanity=PASS`

## GPU Utilization (Observed)

From `nvidia_smi_...csv` (samples=538, 5s cadence):
- gpu_util min: `2`
- gpu_util p50: `55`
- gpu_util mean: `51.49`
- gpu_util max: `75`

## Artifact Integrity + Hashes

Integrity check:
```powershell
python tools/analysis/exp0017_artifact_integrity_check.py `
  --run_dir logs/exp_0017_comprehension_v0_cloze/run_20260209T063040Z_388b8b4_task0143_quality_45m_io `
  --hash
```
Result: PASS.

SHA256:
- `RUN_METADATA.json`: `8b7aa54d30aedc844f34fa02949249ed7e3e4eb8b1646eddd510eb9a654ebae7`
- `RUN_STATUS.json`: `ca6f4696781c9fbb5569c8098a35d94269520a12097dcaf436b9cf285d87218e`
- `metrics_by_step.jsonl`: `d9867ced214190e087a6ebfec05867ee725b41f495037fe580a06d7422c012e4`
- `metrics.json`: `8ffaf4c81ed28449e4430c70b4e6bc1ebb3281a3b0b0d4f74c58c63ef56afcb6`

## Policy Verdict (Progress Policy)

```powershell
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0143_quality_45m_io `
  --require_integrity `
  --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --require_sanity
```

Result:
- `exit_code=0` / `VERDICT: PASS`

