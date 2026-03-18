# TASK-0155 MONITORING COMMANDS — end-to-end verification of TASK-0154 stack via orchestrator

Repo:
- `D:\projects\Bio_Digital_Core\Bio_digital_core` (branch `test`)

Dataset root (external-only):
- `D:\datasets\bdc\simplified_wiki_v0\20260201\full_build`

Canon:
- No changes to exp_0017 learning semantics/metrics (orchestrator/control-plane only).
- No external network; localhost-only (`127.0.0.1`).
- Runtime artifacts under `logs/**` and `ui/pacman_viz/_snapshots/**` are gitignored.

Common:

```powershell
cd D:\projects\Bio_Digital_Core\Bio_digital_core
$DATASET_ROOT = "D:\datasets\bdc\simplified_wiki_v0\20260201\full_build"
```

## R0 (2m): preferred port busy => auto-select

Terminal A (occupy `127.0.0.1:8848` temporarily):

```powershell
# occupy port 8848 (loopback only)
$busyLog = "logs/exp_0017_comprehension_v0_cloze/_launchers/task0155_r0_busy_8848.log"
New-Item -ItemType Directory -Force (Split-Path $busyLog) | Out-Null
$busy = Start-Process -PassThru -NoNewWindow python -ArgumentList @(
  "-u","-m","http.server","8848","--bind","127.0.0.1"
) -RedirectStandardOutput $busyLog -RedirectStandardError $busyLog
Write-Host "BUSY_PID=$($busy.Id)"
```

Terminal B (orchestrator):

```powershell
$tag = "task0155_r0_port_busy_smoke"
$log = "logs/exp_0017_comprehension_v0_cloze/_launchers/task0155_r0_orchestrator_stdout.log"
python tools/launchers/exp0017_live_run.py `
  --dataset_root $DATASET_ROOT `
  --device cuda `
  --seed 12345 `
  --batch_size 32 `
  --num_workers 4 `
  --pin_memory `
  --prefetch_factor 2 `
  --persistent_workers `
  --eval_every 1000 `
  --eval_max_docs 2000 `
  --log_every 200 `
  --max_steps 100000000 `
  --time_budget_minutes 2 `
  --snapshot_interval_sec 60 `
  --durable_interval_sec 300 `
  --enable_stop_control `
  --port_preferred 8848 `
  --port_auto `
  --run_tag $tag 2>&1 | Tee-Object -FilePath $log
```

After R0 finishes:

```powershell
Stop-Process -Id $busy.Id -Force
```

## R1 (10m): live stack, no STOP

```powershell
$tag = "task0155_r1_live_10m_no_stop"
$log = "logs/exp_0017_comprehension_v0_cloze/_launchers/task0155_r1_orchestrator_stdout.log"
python tools/launchers/exp0017_live_run.py `
  --dataset_root $DATASET_ROOT `
  --device cuda `
  --seed 12345 `
  --batch_size 32 `
  --num_workers 4 `
  --pin_memory `
  --prefetch_factor 2 `
  --persistent_workers `
  --eval_every 1000 `
  --eval_max_docs 2000 `
  --log_every 200 `
  --max_steps 100000000 `
  --time_budget_minutes 10 `
  --snapshot_interval_sec 60 `
  --durable_interval_sec 300 `
  --enable_stop_control `
  --port_preferred 8848 `
  --port_auto `
  --run_tag $tag 2>&1 | Tee-Object -FilePath $log
```

## R2 (10m): emergency STOP at ~2m

```powershell
$tag = "task0155_r2_live_10m_stop_emergency"
$tok = "TASK0155_EMERGENCY_TOKEN"
$pref = 8849
$runsRoot = "logs/exp_0017_comprehension_v0_cloze"
$stdout = "logs/exp_0017_comprehension_v0_cloze/_launchers/task0155_r2_orchestrator_stdout.log"

$p = Start-Process -PassThru -NoNewWindow python -ArgumentList @(
  "tools/launchers/exp0017_live_run.py",
  "--dataset_root",$DATASET_ROOT,
  "--device","cuda",
  "--seed","12345",
  "--batch_size","32",
  "--num_workers","4",
  "--pin_memory",
  "--prefetch_factor","2",
  "--persistent_workers",
  "--eval_every","1000",
  "--eval_max_docs","2000",
  "--log_every","200",
  "--max_steps","100000000",
  "--time_budget_minutes","10",
  "--snapshot_interval_sec","60",
  "--durable_interval_sec","300",
  "--enable_stop_control",
  "--control_token",$tok,
  "--port_preferred","$pref",
  "--port_auto",
  "--run_tag",$tag
) -RedirectStandardOutput $stdout -RedirectStandardError $stdout

# wait until PORT_SELECTION file exists (port may auto-shift)
do { Start-Sleep -Seconds 2 } while (-not (Test-Path "$runsRoot/_launchers/PORT_SELECTION_$tag.json"))
$chosen = (Get-Content "$runsRoot/_launchers/PORT_SELECTION_$tag.json" | ConvertFrom-Json).chosen_port

Start-Sleep -Seconds 120
$body = @{ token=$tok; mode='emergency'; reason='EMERGENCY_STOP'; run_tag=$tag } | ConvertTo-Json -Compress
curl.exe -s -X POST "http://127.0.0.1:$chosen/control/stop_emergency" -H "Content-Type: application/json" --data-binary $body

Wait-Process -Id $p.Id
```

## R3 (10m): graceful STOP at ~2m

```powershell
$tag = "task0155_r3_live_10m_stop_graceful"
$tok = "TASK0155_GRACEFUL_TOKEN"
$pref = 8850
$runsRoot = "logs/exp_0017_comprehension_v0_cloze"
$stdout = "logs/exp_0017_comprehension_v0_cloze/_launchers/task0155_r3_orchestrator_stdout.log"

$p = Start-Process -PassThru -NoNewWindow python -ArgumentList @(
  "tools/launchers/exp0017_live_run.py",
  "--dataset_root",$DATASET_ROOT,
  "--device","cuda",
  "--seed","12345",
  "--batch_size","32",
  "--num_workers","4",
  "--pin_memory",
  "--prefetch_factor","2",
  "--persistent_workers",
  "--eval_every","1000",
  "--eval_max_docs","2000",
  "--log_every","200",
  "--max_steps","100000000",
  "--time_budget_minutes","10",
  "--snapshot_interval_sec","60",
  "--durable_interval_sec","300",
  "--enable_stop_control",
  "--control_token",$tok,
  "--port_preferred","$pref",
  "--port_auto",
  "--run_tag",$tag
) -RedirectStandardOutput $stdout -RedirectStandardError $stdout

do { Start-Sleep -Seconds 2 } while (-not (Test-Path "$runsRoot/_launchers/PORT_SELECTION_$tag.json"))
$chosen = (Get-Content "$runsRoot/_launchers/PORT_SELECTION_$tag.json" | ConvertFrom-Json).chosen_port

Start-Sleep -Seconds 120
$body = @{ token=$tok; mode='graceful'; reason='GRACEFUL_STOP'; run_tag=$tag } | ConvertTo-Json -Compress
curl.exe -s -X POST "http://127.0.0.1:$chosen/control/stop_graceful" -H "Content-Type: application/json" --data-binary $body

Wait-Process -Id $p.Id
```

## Post-run L0 checks (all runs)

```powershell
$runs = "logs/exp_0017_comprehension_v0_cloze"
$tag = "<TAG>"
$runDir = (Get-ChildItem $runs -Directory | Where-Object { $_.Name -like "*_$tag" } | Sort-Object LastWriteTimeUtc -Descending | Select-Object -First 1).FullName
Write-Host "RUN_DIR=$runDir"

python tools/analysis/exp0017_artifact_integrity_check.py --run_dir $runDir --hash
python tools/analysis/exp0017_progress_policy_eval.py --runs_root $runs --run_tags $tag --require_integrity --dataset_root $DATASET_ROOT --require_sanity

$snap = Join-Path "ui/pacman_viz/_snapshots" $tag
Get-ChildItem $snap -File | Where-Object { $_.Name -match '^snapshot_\\d{8}T\\d{6}Z\\.json$' } | Measure-Object | Select-Object Count
Get-FileHash -Algorithm SHA256 (Join-Path $snap "LATEST.json")
```

