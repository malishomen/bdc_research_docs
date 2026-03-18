# TASK-0133 BRIEF REPORT — full batch2 run with gpu_int accelerator (CPU authoritative): timing + parity + monitoring

HEAD (start): `ba397915a2862e21ebfa1f4b9df2d48b91e564b2` (branch: `test`)

## Monitoring

Commands: `reports/analysis/TASK_0133_MONITORING_COMMANDS.md`

## Runs (Batch-2 Full + Sanity)

Queue:
- `experiments/exp_0016_kc1_ttt_v3_validation/QUEUES/batch2_queue.jsonl` (12 configs)
- `--include_sanity` adds 2 controls + 1 negative (total 15 configs)

Params:
- seeds=30, generations=50, population=30, workers=1
- KC1: H=5, T=0.0725 (`KC1_TTT_V3`)
- seeds file: `experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md`

### CPU baseline (authoritative)

- out_dir: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0133_cpu_batch2_20260208T182131Z_ba39791`
- wall time: 83.696 s
- summary.csv sha256: `1b02f42e9afe9de903ba83ba0d2fd0f4ee2338b27be9f9efc610d30e1191dd56`

### gpu_int accelerator (CPU authoritative; D-only)

- out_dir: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0133_gpuint_batch2_20260208T182305Z_ba39791`
- wall time: 36.382 s
- summary.csv sha256: `1b02f42e9afe9de903ba83ba0d2fd0f4ee2338b27be9f9efc610d30e1191dd56`

## Parity Check

Command:
```powershell
$cpu = "experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0133_cpu_batch2_20260208T182131Z_ba39791/summary.csv"
$gpu = "experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0133_gpuint_batch2_20260208T182305Z_ba39791/summary.csv"
python tools/analysis/compare_cpu_gpu_equivalence.py --cpu_summary $cpu --gpu_summary $gpu --enforce_sanity_expectations
```

Result:
- `EQUIVALENCE: PASS` (summary.csv identical).

## CUDA Evidence (gpu_int run)

From `logs/exp_0015/run_20260208T182306Z_ba39791.log`:
- `torch_cuda_available=True`
- `torch_cuda_device_name=NVIDIA GeForce GTX 1080 Ti`
- `torch_cuda_device_capability=(6, 1)`
- `HAMMING_PROFILE ... used_gpu: true` present.

## Decision: Router Recommendation Default?

- **No**: keep router v2 recommendation as advisory/opt-in only.
- Reason: end-to-end speedups depend on workload and warm-up/overhead; `gpu_int` should be enabled per-task (or via heuristic) rather than forced globally.

