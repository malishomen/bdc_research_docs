# TASK-0133 MONITORING COMMANDS — full batch2 CPU vs gpu_int (exp_0015 runner)

This task runs the exp_0015 mutation-only runner on batch2 (12 configs) with sanity, twice:
- CPU baseline (`--hamming_backend cpu`)
- GPU accelerator (`--hamming_backend gpu_int --hamming_profile`)

## Terminal A (Runs)

Set shared params (PowerShell):
```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core

$queue = "experiments/exp_0016_kc1_ttt_v3_validation/QUEUES/batch2_queue.jsonl"
$seeds_file = "experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md"
$kc1_h = 5
$kc1_t = 0.0725
$seeds = 30
$generations = 50
$population = 30
$workers = 1
```

CPU baseline:
```powershell
$ts = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssZ')
$short = (git rev-parse --short HEAD)
$out_cpu = "experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0133_cpu_batch2_${ts}_${short}"

$t = Measure-Command {
  python experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py `
    --queue $queue `
    --seeds_file $seeds_file `
    --seeds $seeds --generations $generations --population $population `
    --include_sanity --workers $workers `
    --kc1_h $kc1_h --kc1_t $kc1_t `
    --hamming_backend cpu `
    --out_dir $out_cpu
}
"CPU_WALL_S=$([math]::Round($t.TotalSeconds,3)) out_dir=$out_cpu"
```

gpu_int run (accelerator; includes CUDA evidence):
```powershell
$ts = (Get-Date).ToUniversalTime().ToString('yyyyMMddTHHmmssZ')
$short = (git rev-parse --short HEAD)
$out_gpu = "experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0133_gpuint_batch2_${ts}_${short}"

$t = Measure-Command {
  python experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py `
    --queue $queue `
    --seeds_file $seeds_file `
    --seeds $seeds --generations $generations --population $population `
    --include_sanity --workers $workers `
    --kc1_h $kc1_h --kc1_t $kc1_t `
    --hamming_backend gpu_int --hamming_profile `
    --out_dir $out_gpu
}
"GPU_INT_WALL_S=$([math]::Round($t.TotalSeconds,3)) out_dir=$out_gpu"
```

## Terminal B (Progress / CUDA Evidence)

Tail progress:
```powershell
Get-Content <OUT_DIR>/progress.jsonl -Tail 25
```

Tail log (path is in `RUN_METADATA.md`):
```powershell
rg -n "log_file" <OUT_DIR>/RUN_METADATA.md
Get-Content <LOG_PATH> -Tail 80
```

CUDA evidence in gpu_int log:
```powershell
rg -n "torch_cuda_available|torch_cuda_device_name|HAMMING_PROFILE" <LOG_PATH> | Select-Object -First 30
```

## Parity Check

```powershell
python tools/analysis/compare_cpu_gpu_equivalence.py `
  --cpu_summary <CPU_OUT_DIR>/summary.csv `
  --gpu_summary <GPU_OUT_DIR>/summary.csv `
  --enforce_sanity_expectations
```

