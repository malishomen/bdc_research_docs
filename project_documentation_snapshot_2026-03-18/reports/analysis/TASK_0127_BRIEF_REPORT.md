# TASK-0127 BRIEF REPORT — quaternary logic + GPU governance scaffold (router v2) w/ batch-2 grounded rules

HEAD (start): `bb18f291d181349c43d0f331666131d633b6bd3c` (branch: `test`)

## What Changed (Artifacts)

- Spec: `docs/spec/QUATERNARY_ROUTING_AND_GPU_GOVERNANCE.md`
- Router v2 (routing-only; no execution): `experiments/exp_0008_quaternary_router_skeleton/src/quaternary_router_v2.py`
- Queue templates:
  - `experiments/exp_0008_quaternary_router_skeleton/QUEUES/templates/quaternary_task_schema.json`
  - `experiments/exp_0008_quaternary_router_skeleton/QUEUES/templates/quaternary_decision_schema.json`
  - `experiments/exp_0008_quaternary_router_skeleton/QUEUES/templates/gpu_replicate_policy.md`

## Rule Codes Added (Grounded In Batch-2 Evidence)

Evidence source (committed):
- `experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/batch2_v3_20260208T122806Z_280847f/summary.csv`

Router v2 emits these rule codes:
- `ZERO_MUTATION_OPERATOR`
  - Detects `k0p0` / `p0p0` (e.g. config ids containing `_k0p0` / `_p0p0`).
  - Policy: `status=NO` for long-run unless explicitly labeled `negative_control`.
  - Motivation: batch-2 contains multiple k=0/p=0 configs; these should be treated as negative controls, not long-run candidates.
- `KC1_FAIL_ALL_SEEDS`
  - Trigger: `seeds_total>=30`, `kc1_fail_rate==1.0`, `threshold_fail_rate==0.0` from `summary.csv`.
  - Policy: `status=MAYBE_NO` + next_action `KC1_BOUNDARY_MAP` diagnostics (do not just extend long-run).
  - Matches batch-2 pattern where `overall_pass_rate==0.0` configs are exclusively KC1-killed.
- `SANITY_BROKEN`
  - Trigger: sanity rows in summary indicate controls not passing or negative not failing (or explicit `sanity_broken=true`).
  - Policy: `status=NO` and stop.

GPU governance (non-negotiable):
- GPU replicate is `MAYBE_YES` only when replicate-only constraints are satisfied.
- GPU never affects PASS/FAIL and is never authoritative (`authoritativeness` must be `CPU`).

## How To Run (Example)

Router v2 reads a JSONL queue of tasks and writes a JSONL decision log.

Example (PowerShell):
```powershell
$q = \"experiments/exp_0008_quaternary_router_skeleton/RESULTS/_task0127_demo_queue.jsonl\"
$out = \"experiments/exp_0008_quaternary_router_skeleton/RESULTS/_task0127_demo_decisions.jsonl\"
$summary = \"experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/batch2_v3_20260208T122806Z_280847f/summary.csv\"

@'
{\"task_id\":\"demo_zero_mut\",\"task_type\":\"long_run_validation\",\"target_config_id\":\"si64_clonal_init_k_point_mutation_k0p0\",\"cpu_command\":\"python runner.py --queue ...\",\"authoritativeness\":\"CPU\",\"evidence_level\":\"L0\",\"expected_artifacts\":[\"summary.csv\"],\"do_not_merge_results\":true,\"role\":\"candidate\"}
{\"task_id\":\"demo_kc1_all\",\"task_type\":\"long_run_validation\",\"target_config_id\":\"si256_clonal_init_k_point_mutation_k1p0\",\"cpu_command\":\"python runner.py --queue ...\",\"authoritativeness\":\"CPU\",\"evidence_level\":\"L1\",\"expected_artifacts\":[\"summary.csv\"],\"do_not_merge_results\":true,\"summary_csv_path\":\"REPLACE_SUMMARY\"}
{\"task_id\":\"demo_gpu_rep\",\"task_type\":\"gpu_replicate\",\"target_config_id\":\"si64_random_init_per_locus_flip_p0p001\",\"cpu_command\":\"python cpu_runner.py --queue ...\",\"gpu_command\":\"python gpu_runner.py --queue ...\",\"authoritativeness\":\"CPU\",\"evidence_level\":\"L0\",\"expected_artifacts\":[\"metrics.csv\",\"summary.csv\"],\"do_not_merge_results\":true,\"compare_script\":\"python tools/compare_cpu_gpu.py --cpu ... --gpu ...\"}
'@ | ForEach-Object { $_ -replace \"REPLACE_SUMMARY\", $summary } | Set-Content -Encoding UTF8 $q

python experiments/exp_0008_quaternary_router_skeleton/src/quaternary_router_v2.py --in_queue $q --out_decisions $out
Get-Content $out
```

Expected highlights:
- `demo_zero_mut` => `status=NO` with `ZERO_MUTATION_OPERATOR`
- `demo_kc1_all` => `status=MAYBE_NO` with `KC1_FAIL_ALL_SEEDS` and next_action `KC1_BOUNDARY_MAP`
- `demo_gpu_rep` => `gpu_status=MAYBE_YES` (replicate-only; `do_not_merge_results=true`)

## Verification

- `pytest -q` PASS (router v2 unit tests added under `experiments/exp_0008_quaternary_router_skeleton/tests/`).

## Next Step (Not Implemented Here)

Build a GPU equivalence test harness that:
- runs CPU+GPU on identical inputs/seeds,
- produces comparable artifacts,
- runs a compare script and records PASS/FAIL,
so GPU can be upgraded from `MAYBE_YES` replicate-only to any stronger status under an explicit equivalence contract.

