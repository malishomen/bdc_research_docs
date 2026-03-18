# TASK-0124 Monitoring Commands — long-run queue11 under KC1_TTT_V3 (CPU-only)

Goal: keep a live view of progress while `runner.py` executes.

## Terminal A (run)

### Smoke (seeds=4, gen=10, sanity)

```powershell
$ts=(Get-Date -Format "yyyyMMddTHHmmssZ")
$short=(git rev-parse --short HEAD)
$out="experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/smoke_queue11_v3_${ts}_${short}"
python experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py `
  --queue experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl `
  --seeds 4 `
  --generations 10 `
  --population 30 `
  --include_sanity `
  --workers 1 `
  --kc1_h 5 `
  --kc1_t 0.0725 `
  --out_dir $out
echo "OUT_DIR=$out"
```

### Long-run (seeds=90, gen=50, sanity)

```powershell
$ts=(Get-Date -Format "yyyyMMddTHHmmssZ")
$short=(git rev-parse --short HEAD)
$out="experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/long_queue11_v3_${ts}_${short}"
python experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py `
  --queue experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl `
  --seeds 90 `
  --generations 50 `
  --population 30 `
  --include_sanity `
  --workers 1 `
  --kc1_h 5 `
  --kc1_t 0.0725 `
  --out_dir $out
echo "OUT_DIR=$out"
```

Fallback if time budget is exceeded: change `--seeds 90` to `--seeds 60` and re-run (record deviation in report).

## Terminal B (monitor)

Replace `<RUN_DIR>` with the printed `OUT_DIR` from Terminal A.

### 1) Live progress side-channel (progress.jsonl)

```powershell
$p="<RUN_DIR>\\progress.jsonl"
while ($true) {
  if (Test-Path $p) {
    $last = Get-Content $p -Tail 1
    if ($last) { $last }
  }
  Start-Sleep -Seconds 2
}
```

### 2) Tail latest runner log (logs/exp_0015/run_*.log)

```powershell
$log=(Get-ChildItem logs\\exp_0015\\run_*.log | Sort-Object LastWriteTime | Select-Object -Last 1).FullName
echo $log
Get-Content $log -Wait
```

### 3) Quick sanity/target readout (after summary.csv exists)

```powershell
python tools/analysis/exp0015_single_config_ci.py --summary_csv <RUN_DIR>\\summary.csv --config_id si128_clonal_init_k_point_mutation_k1p0
```

