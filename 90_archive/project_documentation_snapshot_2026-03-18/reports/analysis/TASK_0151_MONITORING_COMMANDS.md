# TASK-0151 MONITORING COMMANDS — exp_0017 live orchestrator (single command) + post-run L0 checks

Repo root: `D:\projects\Bio_Digital_Core\Bio_digital_core`

## One Command: Launch Train + Sidecar + Snapshot Daemon + Localhost Viewer

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core

$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"

python tools/launchers/exp0017_live_run.py `
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
  --snapshot_interval_sec 60 `
  --sidecar_interval_sec 60 `
  --port 8848 `
  --run_tag task0151_live_45m
```

Expected stdout highlights:
- `VIEWER_URL http://127.0.0.1:8848/viewer.html`
- `LATEST_URL http://127.0.0.1:8848/LATEST.json`
- `RUN_DIR logs/exp_0017_comprehension_v0_cloze/run_..._task0151_live_45m`
- `SNAPSHOT_ROOT ui/pacman_viz/_snapshots/task0151_live_45m`
- `MANIFEST logs/exp_0017_comprehension_v0_cloze/_launchers/RUN_LAUNCH_MANIFEST_...json`

## Open Viewer

- Open in browser: `http://127.0.0.1:8848/viewer.html`
- In Live panel, keep URL at `http://127.0.0.1:8848/LATEST.json` and click Start Live.

## Post-Run L0 Checks

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core

$runsRoot = "logs/exp_0017_comprehension_v0_cloze"
$runDir = (Get-ChildItem $runsRoot -Directory |
  Where-Object { $_.Name -like "*_task0151_live_45m" } |
  Sort-Object LastWriteTime -Descending |
  Select-Object -First 1).FullName

Write-Host "RUN_DIR=$runDir"

# Dataset integrity
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python experiments/exp_0017_comprehension_v0_cloze/src/eval.py --integrity_only --dataset_root $root

# Crash-safe artifact integrity
python tools/analysis/exp0017_artifact_integrity_check.py --run_dir $runDir --hash

# Policy eval direct (should not ERROR)
python tools/analysis/exp0017_progress_policy_eval.py `
  --runs_root $runsRoot `
  --run_tags task0151_live_45m `
  --require_integrity `
  --dataset_root $root `
  --require_sanity

# Sidecar presence
python -c "from pathlib import Path; import json; p=Path(r'$runDir')/'policy_eval.json'; j=json.loads(p.read_text('utf-8')); print('exit_code',j['exit_code']); print('quat',j['quaternary_state']);"

# Snapshot count (>= 40 for 45m; allow small slack)
python -c "from pathlib import Path; p=Path('ui/pacman_viz/_snapshots/task0151_live_45m'); snaps=sorted([x for x in p.iterdir() if x.name.startswith('snapshot_') and x.suffix=='.json']); print('snapshots',len(snaps)); raise SystemExit(0 if len(snaps)>=40 else 2)"
```

## Dry Run (No Launch)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python tools/launchers/exp0017_live_run.py --dataset_root $root --run_tag demo --dry_run --start_ts_utc 2026-02-09T00:00:00Z
```

