# TASK-0148 MONITORING COMMANDS — Pac-Man viz policy sidecar + 1-min snapshots + 45m governed run (exp_0017)

All commands assume repo root: `D:\projects\Bio_Digital_Core\Bio_digital_core`.

## Terminal A — Train (45m; governed; IO-tuned)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core

$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"

# KC_DATA_INTEGRITY gate (must PASS before training)
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --integrity_only --dataset_root $root

$launcherDir = "logs/exp_0017_comprehension_v0_cloze/_launchers"
New-Item -ItemType Directory -Force $launcherDir | Out-Null
$launchLog = Join-Path $launcherDir "launcher_task0148_quality_45m_viz.log"

python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root $root `
  --device cuda `
  --seed 12345 `
  --time_budget_minutes 45 `
  --max_steps 100000000 `
  --eval_every 1000 `
  --eval_max_docs 2000 `
  --log_every 200 `
  --batch_size 32 `
  --num_workers 4 `
  --pin_memory `
  --prefetch_factor 2 `
  --persistent_workers `
  --run_tag task0148_quality_45m_viz 2>&1 | Tee-Object -FilePath $launchLog

Write-Host "TRAIN_EXIT_CODE=$LASTEXITCODE"
```

## Terminal B — Policy Sidecar Loop (every 2 minutes)

Writes `<run_dir>/policy_eval.json` atomically. This is viewer-only evidence and must not influence training.

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
$runs = "logs/exp_0017_comprehension_v0_cloze"

while ($true) {
  python tools/analysis/exp0017_write_policy_sidecar.py `
    --runs_root $runs `
    --run_tag task0148_quality_45m_viz `
    --dataset_root $root `
    --require_integrity `
    --require_sanity
  Start-Sleep -Seconds 120
}
```

## Terminal C — 1-Min Snapshot Daemon (offline; gitignored output)

Snapshots are written to `ui/pacman_viz/_snapshots/...` (gitignored). Viewer reads snapshot JSON only.

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core

$runsRoot = "logs/exp_0017_comprehension_v0_cloze"
$runDir = (Get-ChildItem $runsRoot -Directory |
  Where-Object { $_.Name -like "*task0148_quality_45m_viz" } |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 1).FullName

Write-Host "RUN_DIR=$runDir"

$outDir = "ui/pacman_viz/_snapshots/task0148_quality_45m_viz"
python ui/pacman_viz/src/snapshot_daemon.py `
  --run_dir $runDir `
  --out_dir $outDir `
  --interval_sec 60 `
  --time_budget_minutes 45 `
  --write_latest_pointer
```

## Post-Run Checks (L0; must be recorded)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core

$runsRoot = "logs/exp_0017_comprehension_v0_cloze"
$runDir = (Get-ChildItem $runsRoot -Directory |
  Where-Object { $_.Name -like "*task0148_quality_45m_viz" } |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 1).FullName

Write-Host "RUN_DIR=$runDir"

# Training artifact integrity (must PASS)
python tools/analysis/exp0017_artifact_integrity_check.py --run_dir $runDir --hash

# Policy tool direct (should not ERROR)
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root $runsRoot `
  --run_tags task0148_quality_45m_viz `
  --require_integrity `
  --dataset_root $root `
  --require_sanity

# Sidecar presence
python -c "from pathlib import Path; import json; p=Path(r'$runDir')/'policy_eval.json'; j=json.loads(p.read_text('utf-8')); print('policy_exit_code', j['exit_code']); print('quat', j['quaternary_state']);"

# Snapshot count (>= 40 for 45m; allow small startup slack only)
python -c "from pathlib import Path; p=Path('ui/pacman_viz/_snapshots/task0148_quality_45m_viz'); snaps=sorted(p.glob('snapshot_*.json')); print('snapshots',len(snaps)); raise SystemExit(0 if len(snaps)>=40 else 2)"
```

