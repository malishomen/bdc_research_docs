# TASK-0119 BRIEF REPORT — exp_0015 long-run validation (CPU authoritative; GPU replicate optional)

Commit: `c68247286ce0a9f3ccb361b490fc5c0649059367` (start of TASK-0119)

## CPU Run (authoritative)

- Queue: `experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl` (11 configs)
- Seeds file: `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/SEEDS.md` (first 30 numeric seeds)
- Params: seeds=30, generations=50, population=30
- Gate: `KC1_TTT_V2` (H=5, T=0.075)
- Sanity set included: controls + negative (`--include_sanity`)

Artifacts (local; raw CSVs not committed):

- Run dir: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/run_20260208T054329Z_c682472`
  - metrics.csv sha256: `d9508e04ca9a3931e273c5983100344b9f586b6b26ef23c2e529efa2a188119d`
  - summary.csv sha256: `e070176b7e600efdb3a585bba5a6bd89dfce7432d64670b4da75a1886537584a`
  - RUN_METADATA.md sha256: `2816eb9ff76bbaca6a4987a05dde246389cb3b9297c1f7c0bbfdc31312facbec`
- Logs:
  - runner log: `logs/exp_0015/run_20260208T054329Z_c682472.log`
  - wrapper log (stdout capture): `logs/exp_0015/longrun_cpu_20260208T054328Z_c682472.log`

Sanity (from `summary.csv`):

- controls: PASS (overall_pass_rate=1.0 for both control configs)
- negative: FAIL (overall_pass_rate=0.0)

Legacy fail configs (5/11) under KC1_TTT_V2 (from `summary.csv`):

- `si128_clonal_init_k_point_mutation_k1p0`: kc1_fail_rate=0.633333, overall_pass_rate=0.366667
- `si128_clonal_init_k_point_mutation_k2p0`: kc1_fail_rate=0.0, overall_pass_rate=1.0
- `si128_clonal_init_per_locus_flip_p0p01`: kc1_fail_rate=0.0, overall_pass_rate=1.0
- `si64_clonal_init_k_point_mutation_k1p0`: kc1_fail_rate=0.0, overall_pass_rate=1.0
- `si64_clonal_init_per_locus_flip_p0p01`: kc1_fail_rate=0.033333, overall_pass_rate=0.966667

Interpretation (evidence-only):

- Systematic KC1 false negatives (kc1_fail_rate==1.0) are removed for all 5 legacy-fail configs on this run, but `si128_clonal_init_k_point_mutation_k1p0` still shows a high KC1_TTT_V2 fail rate (19/30 seeds) under the new gate.

## GPU Replicate (optional; non-authoritative)

GPU inventory (current machine):

- `nvidia-smi -L`: NVIDIA GeForce GTX 1080 Ti
- Query snapshot: `NVIDIA GeForce GTX 1080 Ti, driver 566.36, compute_cap 6.1` (see TASK execution logs)

Status: NOT RUN

- Reason: exp_0015 runner (`experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`) is a mutation-only simulation and has no existing GPU-equivalent implementation or documented GPU run command for the same validation semantics. Running unrelated TRL-10 wiki GPU training would not be functionally equivalent to exp_0015.

## Monitoring

See: `reports/analysis/TASK_0119_MONITORING_COMMANDS.md`

