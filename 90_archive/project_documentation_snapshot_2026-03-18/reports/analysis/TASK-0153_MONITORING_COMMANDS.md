# TASK-0153 MONITORING COMMANDS — power-loss safe artifacts + STOP control (localhost-only)

Canon:
- STOP control is opt-in and localhost-only (bind `127.0.0.1`).
- Training semantics/metrics unchanged; only durability + control-plane.
- No large artifacts committed (`logs/**`, `ui/pacman_viz/_snapshots/**` are gitignored).

## Terminal A (Single Command Orchestrator; Live Stack)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
python tools/launchers/exp0017_live_run.py `
  --dataset_root $root `
  --device cuda `
  --time_budget_minutes 3 `
  --enable_stop_control
```

Expected stdout highlights:
- `VIEWER_URL http://127.0.0.1:8848/viewer.html?control_token=...`
- `RUN_DIR ...\logs\exp_0017_comprehension_v0_cloze\run_..._<run_tag>`

## Terminal B (Quick Health Checks; Read-Only)

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
curl.exe -i http://127.0.0.1:8848/LATEST.json | Select-Object -First 30
netstat -ano | findstr :8848
```

## STOP From Browser (Opt-In)

1. Open the `VIEWER_URL` printed by orchestrator.
2. In the viewer, click `Send STOP request` (token is prefilled from the URL).

Expected artifacts in `<RUN_DIR>`:
- `STOP_REQUEST.json` (written by localhost server)
- `STOPPED.json` (written by trainer on cooperative stop)
- `metrics_by_step.jsonl` last line has `{"event":"RUN_END", ... "state":"STOPPED" ...}`

## Post-Run Checks

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
python tools/analysis/exp0017_artifact_integrity_check.py --run_dir <RUN_DIR> --hash
Get-Content <RUN_DIR>\metrics_by_step.jsonl -TotalCount 1
Get-Content <RUN_DIR>\metrics_by_step.jsonl -Tail 1
```

