# TASK-0131 BRIEF REPORT — gpu_int validation on batch evidence (parity + timing) + router v2 recommendation (advisory only)

HEAD (start): `aa298767678a04677a2ebf043ed06375440da21f` (branch: `test`)

## Runs (End-to-End)

Target queue:
- Source batch queue: `experiments/exp_0016_kc1_ttt_v3_validation/QUEUES/batch2_queue.jsonl`
- Deviation due to runtime: validated on a subset queue with the **first 1 config** from batch2:
  - `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/_task0131_batch2_first1_queue.jsonl`
  - Config: `si256_clonal_init_k_point_mutation_k1p0`
  - Sanity included (`--include_sanity` adds 2 controls + 1 negative).

Params (both runs):
- seeds=30, generations=50, population=30, include_sanity, workers=1
- KC1: H=5, T=0.0725 (KC1_TTT_V3)
- seeds file: `experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md`

### CPU baseline

- out_dir: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0131_cpu_first1_20260208T161018Z_aa29876`
- wall time: 16.824 s
- summary.csv sha256: `732eeec4e6d22a4a085212c342bdfc9981b97ebc6e68eb365904f2c1de578a4d`

### gpu_int backend

- out_dir: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0131_gpuint_first1_20260208T161049Z_aa29876`
- wall time: 1878.579 s
- summary.csv sha256: `732eeec4e6d22a4a085212c342bdfc9981b97ebc6e68eb365904f2c1de578a4d`

## Parity Check

Command:
```powershell
$cpu = "experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0131_cpu_first1_20260208T161018Z_aa29876/summary.csv"
$gpu = "experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0131_gpuint_first1_20260208T161049Z_aa29876/summary.csv"
python tools/analysis/compare_cpu_gpu_equivalence.py --cpu_summary $cpu --gpu_summary $gpu --enforce_sanity_expectations
```

Result:
- `EQUIVALENCE: PASS` (summary.csv identical).

## Timing Result (Key Finding)

- CPU: 16.824 s
- gpu_int: 1878.579 s (slower end-to-end for this workload)

Interpretation:
- `gpu_int` is a compute accelerator for `D` only, but end-to-end can be slower when overhead dominates.

## Router v2 Recommendation (Advisory Only)

Change:
- `experiments/exp_0008_quaternary_router_skeleton/src/quaternary_router_v2.py` can now emit:
  - `recommended_overrides: { "hamming_backend": "gpu_int" }`
when the task indicates large expected compute (`expected_compute_high=true` or a conservative heuristic based on seeds/generations/population/L).

Constraints upheld:
- No change to status logic.
- CPU authoritativeness unchanged.
- Recommendation is non-authoritative metadata only.

Example (routing-only):
```powershell
@'
{"task_id":"demo_reco","task_type":"long_run_validation","target_config_id":"si256_random_init_per_locus_flip_p0p005","cpu_command":"python runner.py --queue ...","authoritativeness":"CPU","evidence_level":"L0","expected_artifacts":["summary.csv"],"do_not_merge_results":true,"expected_compute_high":true}
'@ | Set-Content -Encoding UTF8 experiments/exp_0008_quaternary_router_skeleton/RESULTS/_task0131_reco_demo.jsonl

python experiments/exp_0008_quaternary_router_skeleton/src/quaternary_router_v2.py `
  --in_queue experiments/exp_0008_quaternary_router_skeleton/RESULTS/_task0131_reco_demo.jsonl `
  --out_decisions experiments/exp_0008_quaternary_router_skeleton/RESULTS/_task0131_reco_demo_decisions.jsonl
Get-Content experiments/exp_0008_quaternary_router_skeleton/RESULTS/_task0131_reco_demo_decisions.jsonl
```

## Verification

- `pytest -q` PASS.

