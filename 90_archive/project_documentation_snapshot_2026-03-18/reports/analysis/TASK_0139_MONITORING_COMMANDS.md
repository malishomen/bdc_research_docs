# TASK-0139 MONITORING COMMANDS — comprehension_v0_cloze (train + eval + GPU monitor)

Constraints:
- No network calls.
- Dataset is external-only and must pass sha256 integrity check against `datasets/simplified_wiki_v0/DERIVED_MANIFEST.json`.
- Large artifacts (checkpoints/logits) must not be committed; run outputs go to `logs/` (gitignored).

## Terminal A (Train + Periodic Eval)

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core

$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"

# Required: integrity check (STOP if exit code != 0)
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --dataset_root $root --mode integrity

# Smoke train (fast) + built-in val/test eval + baselines
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --max_docs 2000 `
  --max_steps 200 `
  --seed 12345 `
  --run_tag smoke1 `
  --log_every 25 `
  --eval_every 100

# Main train (budgeted)
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --max_steps 2000 `
  --seed 12345 `
  --run_tag main `
  --log_every 50 `
  --eval_every 200
```

Baselines (standalone):
```powershell
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --dataset_root $root --mode shuffled --seed 12345
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --dataset_root $root --mode random --seed 12345
```

Repro check (smoke repeat):
```powershell
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --max_docs 2000 `
  --max_steps 200 `
  --seed 12345 `
  --run_tag repro2 `
  --log_every 25 `
  --eval_every 100
```

## Terminal B (GPU + Logs)

GPU utilization:
```powershell
while ($true) {
  nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory,memory.used,memory.total,temperature.gpu,power.draw --format=csv
  Start-Sleep -Seconds 5
}
```

Tail latest run logs/metrics (runs write under `logs/exp_0017_comprehension_v0_cloze/`):
```powershell
Get-ChildItem -Directory logs\exp_0017_comprehension_v0_cloze | Sort-Object LastWriteTime | Select-Object -Last 1 | ForEach-Object {
  $d = $_.FullName
  "LATEST_RUN_DIR: $d"
  Get-Content (Join-Path $d "metrics_by_step.jsonl") -Tail 10 -ErrorAction SilentlyContinue
  Get-Content (Join-Path $d "metrics.json") -Tail 60 -ErrorAction SilentlyContinue
}
```

