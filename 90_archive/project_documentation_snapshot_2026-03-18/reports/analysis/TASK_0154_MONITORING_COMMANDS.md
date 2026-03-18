# TASK-0154 MONITORING COMMANDS — 5m durability cadence + dual STOP (emergency/graceful) + live stack

Repo: `D:\projects\Bio_Digital_Core\Bio_digital_core` (branch `test`)

Canon:
- No changes to exp_0017 learning semantics/metrics.
- Localhost-only (`127.0.0.1`) control; no external network.
- Runtime artifacts (`logs/**`, `ui/pacman_viz/_snapshots/**`) are gitignored.

Common:

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$root = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
```

## V1 (5m, no STOP)

```powershell
python tools/launchers/exp0017_live_run.py `
  --dataset_root $root `
  --device cuda `
  --time_budget_minutes 5 `
  --run_tag task0154_v1_5m_no_stop
```

## V2 (5m, EMERGENCY STOP at ~2m)

Run orchestrator in a separate process, then `curl` stop endpoint.

```powershell
$tag = "task0154_v2d_5m_emergency_stop"
$tok = "TASK0154_EMERGENCY_TOKEN"
$port = 8848

$p = Start-Process -PassThru -NoNewWindow python -ArgumentList @(
  "tools/launchers/exp0017_live_run.py",
  "--dataset_root", $root,
  "--device", "cuda",
  "--time_budget_minutes", "5",
  "--run_tag", $tag,
  "--enable_stop_control",
  "--control_token", $tok,
  "--port", "$port"
)

Start-Sleep -Seconds 120
$body = @{ token=$tok; mode='emergency'; reason='EMERGENCY_STOP'; run_tag=$tag } | ConvertTo-Json -Compress
curl.exe -s -X POST "http://127.0.0.1:$port/control/stop_emergency" -H "Content-Type: application/json" --data-binary $body

Wait-Process -Id $p.Id
```

## V3 (5m, GRACEFUL STOP at ~2m)

```powershell
$tag = "task0154_v3d_5m_graceful_stop"
$tok = "TASK0154_GRACEFUL_TOKEN"
$port = 8848

$p = Start-Process -PassThru -NoNewWindow python -ArgumentList @(
  "tools/launchers/exp0017_live_run.py",
  "--dataset_root", $root,
  "--device", "cuda",
  "--time_budget_minutes", "5",
  "--run_tag", $tag,
  "--enable_stop_control",
  "--control_token", $tok,
  "--port", "$port",
  "--eval_every", "200"
)

Start-Sleep -Seconds 120
$body = @{ token=$tok; mode='graceful'; reason='GRACEFUL_STOP'; run_tag=$tag } | ConvertTo-Json -Compress
curl.exe -s -X POST "http://127.0.0.1:$port/control/stop_graceful" -H "Content-Type: application/json" --data-binary $body

Wait-Process -Id $p.Id
```

## Post-Run (All)

Resolve `RUN_DIR` by tag, then run L0 checks:

```powershell
$runs = "logs/exp_0017_comprehension_v0_cloze"
$tag = "<TAG>"
$runDir = (Get-ChildItem $runs -Directory | Where-Object { $_.Name -like \"*_$tag\" } | Sort-Object LastWriteTimeUtc -Descending | Select-Object -First 1).FullName
Write-Host \"RUN_DIR=$runDir\"

python tools/analysis/exp0017_artifact_integrity_check.py --run_dir $runDir --hash
python tools/analysis/exp0017_progress_policy_eval.py --runs_root $runs --run_tags $tag --require_integrity --dataset_root $root --require_sanity

# snapshots evidence
$snap = Join-Path \"ui/pacman_viz/_snapshots\" $tag
Get-ChildItem $snap -Filter \"snapshot_*.json\" | Measure-Object | Select-Object Count
Get-FileHash -Algorithm SHA256 (Join-Path $snap \"LATEST.json\")
```
