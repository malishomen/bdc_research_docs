# TASK-0119 Monitoring Commands (Windows / PowerShell)

This task expects two terminals:

1. Terminal A: start the run (CPU authoritative).
2. Terminal B: live monitoring (tail log + quick progress counts).

## Terminal A (CPU run)

Smoke (sanity set included):

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
python experiments\exp_0015_kc1_ttt_vnext_validation\src\runner.py `
  --queue experiments\exp_0008_quaternary_router_skeleton\QUEUES\exp0011_kc2_diagnostics_cpu_queue.jsonl `
  --seeds 2 --generations 15 `
  --include_sanity
```

Long-run (CPU authoritative):

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
python experiments\exp_0015_kc1_ttt_vnext_validation\src\runner.py `
  --queue experiments\exp_0008_quaternary_router_skeleton\QUEUES\exp0011_kc2_diagnostics_cpu_queue.jsonl `
  --seeds 30 --generations 50 `
  --kc1_h 5 --kc1_t 0.075 `
  --workers 1
```

## Terminal B (monitoring)

Tail the latest exp_0015 log:

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
$log = Get-ChildItem logs\exp_0015\run_*.log | Sort-Object LastWriteTime | Select-Object -Last 1
Get-Content $log.FullName -Wait
```

Progress counter (updates every 5s; based on `progress.jsonl` in latest RESULTS run dir):

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
while ($true) {
  $runDir = Get-ChildItem experiments\exp_0015_kc1_ttt_vnext_validation\RESULTS\run_* -Directory | Sort-Object LastWriteTime | Select-Object -Last 1
  $progress = Join-Path $runDir.FullName "progress.jsonl"
  if (Test-Path $progress) {
    $n = (Get-Content $progress).Count
    $last = Get-Content $progress -Tail 1
    Write-Host ("progress_lines={0} last={1}" -f $n, $last)
  } else {
    Write-Host "progress.jsonl not found yet"
  }
  Start-Sleep -Seconds 5
}
```

