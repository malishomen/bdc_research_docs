# TASK-0122 Monitoring Commands — exp_0016 paired V2 vs V3 (CPU-only)

Goal: keep a live view of progress while `runner.py` executes.

## Terminal A (run)

Use the exact run commands from:
- `experiments/exp_0016_kc1_ttt_v3_validation/RUN_COMMANDS.md`

## Terminal B (monitor)

After starting a run, you will have a `<RUN_DIR>` like:
`experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/v2_<timestamp>_<gitshort>`

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

### 2) Live runner log (logs/exp_0015/*.log)

The runner writes a per-run log under `logs/exp_0015/` (name includes the run UTC timestamp + git short hash).

```powershell
Get-ChildItem logs\\exp_0015\\run_*.log | Sort-Object LastWriteTime | Select-Object -Last 1
```

Then tail it:

```powershell
Get-Content <LOG_PATH> -Wait
```

### 3) Quick summary check (sanity + target config)

```powershell
python tools/analysis/exp0015_single_config_ci.py --summary_csv <RUN_DIR>\\summary.csv --config_id si128_clonal_init_k_point_mutation_k1p0
```

