# TASK-0144 MONITORING COMMANDS — governed 2h exp_0017 run (io-tuned; crash-safe artifacts)

Run tag:
- `task0144_quality_2h_io`

Dataset root (external-only; pinned):
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

## Terminal A (run + tee log)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
git checkout test

$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
$launcherDir = "logs/exp_0017_comprehension_v0_cloze/_launchers"
New-Item -ItemType Directory -Force $launcherDir | Out-Null

# Integrity gate (must PASS before training)
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --integrity_only --dataset_root $root

$ts = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
$launchLog = Join-Path $launcherDir ("launcher_" + $ts + "_task0144_quality_2h_io.log")

python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --device cuda `
  --seed 12345 `
  --time_budget_minutes 120 `
  --max_steps 100000000 `
  --eval_every 1000 `
  --eval_max_docs 2000 `
  --log_every 200 `
  --batch_size 32 `
  --num_workers 4 `
  --pin_memory `
  --prefetch_factor 2 `
  --persistent_workers `
  --run_tag task0144_quality_2h_io 2>&1 | Tee-Object -FilePath $launchLog

Write-Host "TRAIN_EXIT_CODE=$LASTEXITCODE"
```

## Terminal B (GPU monitoring)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$ts = (Get-Date).ToUniversalTime().ToString("yyyyMMddTHHmmssZ")
$launcherDir = "logs/exp_0017_comprehension_v0_cloze/_launchers"
New-Item -ItemType Directory -Force $launcherDir | Out-Null
$gpuLog = Join-Path $launcherDir ("nvidia_smi_" + $ts + "_task0144_quality_2h_io.csv")

"timestamp,utilization.gpu,utilization.memory,memory.used,memory.total,temperature.gpu,power.draw" |
  Out-File -Encoding ascii -FilePath $gpuLog

while ($true) {
  nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.used,memory.total,temperature.gpu,power.draw --format=csv,noheader,nounits |
    Out-File -Append -Encoding ascii -FilePath $gpuLog
  Start-Sleep -Seconds 5
}
```

## Post-run verification

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$runsRoot = "logs/exp_0017_comprehension_v0_cloze"
$runDir = (Get-ChildItem $runsRoot -Directory | Where-Object { $_.Name -like "*task0144_quality_2h_io" } | Sort-Object LastWriteTimeUtc -Descending | Select-Object -First 1).FullName
Write-Host "RUN_DIR=$runDir"

python tools/analysis/exp0017_artifact_integrity_check.py --run_dir $runDir --hash
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root $runsRoot `
  --run_tags task0144_quality_2h_io `
  --require_integrity `
  --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --require_sanity
Write-Host "POLICY_EXIT_CODE=$LASTEXITCODE"
```

