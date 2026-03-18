# TASK-0142 MONITORING COMMANDS — exp_0017 cloze 6-hour governed run (external logs only)

Constraints:
- Run on `test`.
- Integrity gate MUST PASS before training.
- No large artifacts in git. Outputs go to `logs/` (gitignored).

## Terminal A (Integrity Gate + 6h Run)

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
git checkout test

$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"

# Integrity gate (STOP if non-zero)
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --dataset_root $root --integrity_only

# 6-hour governed run (time-budgeted)
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --max_steps 999999 `
  --time_budget_minutes 360 `
  --seed 12345 `
  --run_tag task0142_6h `
  --log_every 200 `
  --eval_every 1000
```

## Terminal B (GPU + Tail Logs)

GPU utilization:
```powershell
while ($true) {
  nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory,memory.used,memory.total,temperature.gpu,power.draw --format=csv
  Start-Sleep -Seconds 15
}
```

Tail latest run metrics:
```powershell
Get-ChildItem -Directory logs\exp_0017_comprehension_v0_cloze | Sort-Object LastWriteTime | Select-Object -Last 1 | ForEach-Object {
  $d = $_.FullName
  "LATEST_RUN_DIR: $d"
  Get-Content (Join-Path $d "metrics_by_step.jsonl") -Tail 10 -ErrorAction SilentlyContinue
  Get-Content (Join-Path $d "metrics.json") -Tail 120 -ErrorAction SilentlyContinue
}
```

## Final Summary (After Completion)

Print final metrics:
```powershell
Get-ChildItem -Directory logs\exp_0017_comprehension_v0_cloze | Sort-Object LastWriteTime | Select-Object -Last 1 | ForEach-Object {
  Get-Content (Join-Path $_.FullName "metrics.json")
}
```

Optional policy evaluation (single-run mode; PASS=0 / FAIL=2 / ERROR=1):
```powershell
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0142_6h `
  --require_integrity `
  --dataset_root $root `
  --require_sanity
```

