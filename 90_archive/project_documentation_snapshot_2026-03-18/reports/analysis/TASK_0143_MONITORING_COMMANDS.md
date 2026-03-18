# TASK-0143 MONITORING COMMANDS — exp_0017 DataLoader knobs + 45m quality run (batch_size=32 unchanged)

Dataset root (external-only; pinned):
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

## Terminal A (45m run; stdout/stderr captured)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
git checkout test

$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
$logdir = "logs\exp_0017_comprehension_v0_cloze\_launchers"
New-Item -ItemType Directory -Force $logdir | Out-Null

# Integrity gate (must PASS before training)
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --dataset_root $root --integrity_only

# 45m quality baseline run (batch_size default=32; unchanged)
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
  --run_tag task0143_quality_45m_io 2>&1 |
  Tee-Object -FilePath (Join-Path $logdir "task0143_quality_45m_io.log")

# Post-run: locate run_dir and policy eval
$run = Get-ChildItem -Directory logs\exp_0017_comprehension_v0_cloze |
  Where-Object { $_.Name -like "run_*_task0143_quality_45m_io" } |
  Sort-Object LastWriteTimeUtc -Descending | Select-Object -First 1
$run.FullName

python tools/analysis/exp0017_artifact_integrity_check.py --run_dir $run.FullName --hash
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0143_quality_45m_io `
  --require_integrity `
  --dataset_root $root `
  --require_sanity
```

## Terminal B (GPU + progress monitoring)

GPU utilization loop (5s cadence):
```powershell
while ($true) {
  nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.used,memory.total,temperature.gpu,power.draw --format=csv
  Start-Sleep -Seconds 5
}
```

Tail latest run status:
```powershell
Get-ChildItem -Directory logs\exp_0017_comprehension_v0_cloze | Sort-Object LastWriteTime | Select-Object -Last 1 | ForEach-Object {
  $d = $_.FullName
  "LATEST_RUN_DIR: $d"
  Get-Content (Join-Path $d "RUN_STATUS.json") -Tail 80 -ErrorAction SilentlyContinue
  Get-Content (Join-Path $d "metrics_by_step.jsonl") -Tail 5 -ErrorAction SilentlyContinue
}
```

