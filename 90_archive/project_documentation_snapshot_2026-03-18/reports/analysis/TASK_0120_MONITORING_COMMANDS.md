# TASK-0120 Monitoring Commands (Windows / PowerShell)

Two terminals:

1. Terminal A: run (CPU authoritative)
2. Terminal B: monitoring (tail log + progress counters)

## Terminal A (run)

Smoke (sanity included):

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
python experiments\exp_0015_kc1_ttt_vnext_validation\src\runner.py `
  --queue experiments\exp_0015_kc1_ttt_vnext_validation\QUEUES\queue_single_si128_k1p0.jsonl `
  --seeds_file experiments\exp_0015_kc1_ttt_vnext_validation\SEEDS_TASK0120_120.md `
  --seeds 4 --generations 10 `
  --kc1_h 5 --kc1_t 0.075 `
  --include_sanity
```

Long-run (adjust seeds if needed):

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
python experiments\exp_0015_kc1_ttt_vnext_validation\src\runner.py `
  --queue experiments\exp_0015_kc1_ttt_vnext_validation\QUEUES\queue_single_si128_k1p0.jsonl `
  --seeds_file experiments\exp_0015_kc1_ttt_vnext_validation\SEEDS_TASK0120_120.md `
  --seeds 90 --generations 50 `
  --kc1_h 5 --kc1_t 0.075 `
  --include_sanity `
  --workers 1
```

Fallback seeds (if time budget forces it): `--seeds 60` then `--seeds 45`.

## Terminal B (monitoring)

Tail latest exp_0015 log:

```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
$log = Get-ChildItem logs\exp_0015\run_*.log | Sort-Object LastWriteTime | Select-Object -Last 1
Get-Content $log.FullName -Wait
```

Progress summary (updates every 5s; based on `progress.jsonl` in latest RESULTS run dir):

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
