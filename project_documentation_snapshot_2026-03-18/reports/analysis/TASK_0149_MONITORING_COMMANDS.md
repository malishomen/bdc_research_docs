# TASK-0149 MONITORING COMMANDS — Pac-Man Viz Variant B (localhost-only) + 45m governed run + 1-min snapshots

Repo root: `D:\projects\Bio_Digital_Core\Bio_digital_core`

## Terminal A — Train (45m; governed; crash-safe)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core

$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"

# KC_DATA_INTEGRITY gate
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --integrity_only --dataset_root $root

$launcherDir = "logs/exp_0017_comprehension_v0_cloze/_launchers"
New-Item -ItemType Directory -Force $launcherDir | Out-Null
$launchLog = Join-Path $launcherDir "launcher_task0149_quality_45m_viz_localhost.log"

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
  --run_tag task0149_quality_45m_viz_localhost 2>&1 | Tee-Object -FilePath $launchLog

Write-Host "TRAIN_EXIT_CODE=$LASTEXITCODE"
```

## Terminal B — Policy Sidecar Loop (every 2 minutes; atomic)

Writes `<run_dir>/policy_eval.json` atomically (viewer-only evidence).

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
$runs = "logs/exp_0017_comprehension_v0_cloze"

while ($true) {
  python tools/analysis/exp0017_write_policy_sidecar.py `
    --runs_root $runs `
    --run_tag task0149_quality_45m_viz_localhost `
    --dataset_root $root `
    --require_integrity `
    --require_sanity
  Start-Sleep -Seconds 120
}
```

## Terminal C — Snapshot Daemon (1-min; atomic; gitignored output)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core

$runsRoot = "logs/exp_0017_comprehension_v0_cloze"
$runDir = (Get-ChildItem $runsRoot -Directory |
  Where-Object { $_.Name -like "*task0149_quality_45m_viz_localhost" } |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 1).FullName

Write-Host "RUN_DIR=$runDir"

$snapRoot = "ui/pacman_viz/_snapshots/task0149_quality_45m_viz_localhost"
python ui/pacman_viz/src/snapshot_daemon.py `
  --run_dir $runDir `
  --out_dir $snapRoot `
  --interval_sec 60 `
  --time_budget_minutes 45 `
  --write_latest_pointer
```

## Terminal D — Localhost Server (loopback-only)

Serves only JSON files from snapshot root + a single embedded `viewer.html`.

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$snapRoot = "ui/pacman_viz/_snapshots/task0149_quality_45m_viz_localhost"
python ui/pacman_viz/src/localhost_server.py --root_dir $snapRoot --port 8848 --bind 127.0.0.1
```

Open in browser:
- `http://127.0.0.1:8848/viewer.html`
- Live URL should remain `http://127.0.0.1:8848/LATEST.json`

## Post-Run Checks (L0)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core

$runsRoot = "logs/exp_0017_comprehension_v0_cloze"
$runDir = (Get-ChildItem $runsRoot -Directory |
  Where-Object { $_.Name -like "*task0149_quality_45m_viz_localhost" } |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 1).FullName

Write-Host "RUN_DIR=$runDir"

# exp_0017 artifact integrity
python tools/analysis/exp0017_artifact_integrity_check.py --run_dir $runDir --hash

# policy sidecar exists
python -c "from pathlib import Path; import json; p=Path(r'$runDir')/'policy_eval.json'; j=json.loads(p.read_text('utf-8')); print('exit_code',j['exit_code']); print('quat',j['quaternary_state']);"

# snapshot count (>= 40 for 45m; allow small slack)
python -c "from pathlib import Path; p=Path('ui/pacman_viz/_snapshots/task0149_quality_45m_viz_localhost'); snaps=sorted([x for x in p.iterdir() if x.name.startswith('snapshot_') and x.suffix=='.json']); print('snapshots',len(snaps)); raise SystemExit(0 if len(snaps)>=40 else 2)"

# LATEST parses
python -c "import json; from pathlib import Path; j=json.loads(Path('ui/pacman_viz/_snapshots/task0149_quality_45m_viz_localhost/LATEST.json').read_text('utf-8')); print('LATEST ok', j.get('ts_utc'), j.get('quat_source'), j.get('quat_state'))"
```

