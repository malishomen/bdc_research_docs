# TASK-0126 Monitoring Commands — deferred sweep thaw batch-2 hard-mode (CPU-only, KC1_TTT_V3)

Queue:
- `experiments/exp_0016_kc1_ttt_v3_validation/QUEUES/batch2_queue.jsonl`

Seeds:
- `experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md`

KC1:
- `KC1_TTT_V3` (H=5, T=0.0725)

## Terminal A (run)

### Smoke (seeds=4, gen=10, sanity)

```powershell
$ts=(Get-Date -Format "yyyyMMddTHHmmssZ")
$short=(git rev-parse --short HEAD)
$out="experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/smoke_batch2_v3_${ts}_${short}"
python experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py `
  --queue experiments/exp_0016_kc1_ttt_v3_validation/QUEUES/batch2_queue.jsonl `
  --seeds_file experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md `
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

### Batch (seeds=30, gen=50, sanity)

```powershell
$ts=(Get-Date -Format "yyyyMMddTHHmmssZ")
$short=(git rev-parse --short HEAD)
$out="experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/batch2_v3_${ts}_${short}"
python experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py `
  --queue experiments/exp_0016_kc1_ttt_v3_validation/QUEUES/batch2_queue.jsonl `
  --seeds_file experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md `
  --seeds 30 `
  --generations 50 `
  --population 30 `
  --include_sanity `
  --workers 1 `
  --kc1_h 5 `
  --kc1_t 0.0725 `
  --out_dir $out
echo "OUT_DIR=$out"
```

## Terminal B (monitor)

Replace `<RUN_DIR>` with `OUT_DIR` from Terminal A.

### 1) Live progress (progress.jsonl)

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

### 2) Tail latest runner log

```powershell
$log=(Get-ChildItem logs\\exp_0015\\run_*.log | Sort-Object LastWriteTime | Select-Object -Last 1).FullName
echo $log
Get-Content $log -Wait
```

