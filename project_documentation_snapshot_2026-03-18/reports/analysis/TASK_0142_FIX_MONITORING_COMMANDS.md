# TASK-0142-FIX MONITORING COMMANDS — exp_0017 crash-safe artifacts + 4x 5min validations

Constraints:
- No semantic changes to training. Only durability/logging/finalization.
- Every run must create immediately: `metrics_by_step.jsonl` (RUN_START) + `RUN_STATUS.json` heartbeat.
- Every run must end with `metrics.json` OR `CRASH.json`.
- Redirect stdout/stderr to a launcher log (Tee-Object).
- Quaternary mapping from policy-eval exit code only: `0->YES`, `2->NO`, `1->MAYBE_NO`.

Dataset root (external-only):
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

## Terminal A (4 runs)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
git checkout test

$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
$logdir = "logs\exp_0017_comprehension_v0_cloze\_launchers"
New-Item -ItemType Directory -Force $logdir | Out-Null

# 0) integrity gate
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --dataset_root $root --integrity_only

# 1) GPU time-budget 5m
python experiments/exp_0017_comprehension_v0_cloze/src/train.py --dataset_root $root --device cuda --seed 12345 --time_budget_minutes 5 --max_steps 1000000 --eval_every 1000 --log_every 200 --run_tag task0142_fix_gpu_time5m 2>&1 |
  Tee-Object -FilePath (Join-Path $logdir "task0142_fix_gpu_time5m.log")

# 2) GPU steps (force at least 1 eval)
python experiments/exp_0017_comprehension_v0_cloze/src/train.py --dataset_root $root --device cuda --seed 12345 --max_steps 250 --eval_every 50 --log_every 50 --run_tag task0142_fix_gpu_steps 2>&1 |
  Tee-Object -FilePath (Join-Path $logdir "task0142_fix_gpu_steps.log")

# 3) CPU time-budget 5m
python experiments/exp_0017_comprehension_v0_cloze/src/train.py --dataset_root $root --device cpu --seed 12345 --time_budget_minutes 5 --max_steps 999999 --eval_every 1000 --log_every 200 --run_tag task0142_fix_cpu_time5m 2>&1 |
  Tee-Object -FilePath (Join-Path $logdir "task0142_fix_cpu_time5m.log")

# 4) Hybrid_quat: GPU train 5m; then policy-eval (CPU) => quaternary verdict by exit code only.
python experiments/exp_0017_comprehension_v0_cloze/src/train.py --dataset_root $root --device cuda --seed 12345 --time_budget_minutes 5 --max_steps 1000000 --eval_every 1000 --log_every 200 --run_tag task0142_fix_hybrid_quat5m 2>&1 |
  Tee-Object -FilePath (Join-Path $logdir "task0142_fix_hybrid_quat5m.log")

python tools/analysis/exp0017_progress_policy_eval.py --runs_root logs/exp_0017_comprehension_v0_cloze --run_tags task0142_fix_hybrid_quat5m --require_integrity --dataset_root $root --require_sanity
```

## Terminal B (monitor)

GPU utilization:
```powershell
while ($true) {
  nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory,memory.used,memory.total,temperature.gpu,power.draw --format=csv
  Start-Sleep -Seconds 15
}
```

Tail latest run status quickly:
```powershell
Get-ChildItem -Directory logs\exp_0017_comprehension_v0_cloze | Sort-Object LastWriteTime | Select-Object -Last 1 | ForEach-Object {
  $d = $_.FullName
  "LATEST_RUN_DIR: $d"
  Get-Content (Join-Path $d "RUN_STATUS.json") -Tail 60 -ErrorAction SilentlyContinue
  Get-Content (Join-Path $d "metrics_by_step.jsonl") -Tail 3 -ErrorAction SilentlyContinue
}
```

## Post-run artifact integrity (per run_dir)

```powershell
$run = "logs\exp_0017_comprehension_v0_cloze\<RUN_DIR_NAME>"
python tools/analysis/exp0017_artifact_integrity_check.py --run_dir $run --hash
```
