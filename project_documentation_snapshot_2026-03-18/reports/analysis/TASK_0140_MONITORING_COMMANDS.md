# TASK-0140 MONITORING COMMANDS — governed exp_0017 replicate + policy eval

Constraints:
- No network calls.
- Use pinned dataset root (external): `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`
- Large artifacts stay under `logs/` (gitignored).

## Terminal A (Two Governed Runs + Policy Eval)

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core

$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"

# Integrity gate (must be exit 0)
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --dataset_root $root --integrity_only

# Governed run #1 (time budgeted)
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --max_steps 12000 `
  --time_budget_minutes 240 `
  --seed 12345 `
  --run_tag task0140_main1 `
  --log_every 100 `
  --eval_every 500

# Governed replicate #2 (same config/seed)
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --max_steps 12000 `
  --time_budget_minutes 240 `
  --seed 12345 `
  --run_tag task0140_main2 `
  --log_every 100 `
  --eval_every 500

# Policy evaluation (PASS=0 / FAIL=2 / ERROR=1)
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root logs/exp_0017_comprehension_v0_cloze `
  --run_tags task0140_main1 task0140_main2 `
  --require_integrity `
  --dataset_root $root `
  --require_sanity
```

Note:
- If you use `--time_budget_minutes`, replicates may stop at different step counts due to throughput variance.
- For strict replicate comparability, prefer fixed `--max_steps` without `--time_budget_minutes` (or enforce a fixed stop-step externally).

## Terminal B (GPU + Tail Logs)

GPU utilization:
```powershell
while ($true) {
  nvidia-smi --query-gpu=timestamp,name,utilization.gpu,utilization.memory,memory.used,memory.total,temperature.gpu,power.draw --format=csv
  Start-Sleep -Seconds 5
}
```

Tail latest training output:
```powershell
Get-ChildItem -Directory logs\exp_0017_comprehension_v0_cloze | Sort-Object LastWriteTime | Select-Object -Last 1 | ForEach-Object {
  $d = $_.FullName
  "LATEST_RUN_DIR: $d"
  Get-Content (Join-Path $d "metrics_by_step.jsonl") -Tail 10 -ErrorAction SilentlyContinue
  Get-Content (Join-Path $d "metrics.json") -Tail 80 -ErrorAction SilentlyContinue
}
```
