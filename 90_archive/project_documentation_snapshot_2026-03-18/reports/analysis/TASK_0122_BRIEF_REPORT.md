# TASK-0122 BRIEF REPORT — exp_0016 paired V2 vs V3 validation (CPU authoritative)

HEAD: `069800936a6ae50b3d8186f6b3adb258448d8118`

## Runs (local; raw CSVs not committed)

Queue (queue11): `experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl`

Seeds: first 30 numeric seeds from `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/SEEDS.md` (paired across V2 vs V3)

Runner: `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py` (same dynamics; KC1 parameters passed via flags)

### V2 (KC1_TTT_V2, H=5, T=0.075)

- Run dir: `experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/v2_20260208T113527Z_0698009`
  - metrics.csv sha256: `d9508e04ca9a3931e273c5983100344b9f586b6b26ef23c2e529efa2a188119d`
  - summary.csv sha256: `e070176b7e600efdb3a585bba5a6bd89dfce7432d64670b4da75a1886537584a`
  - RUN_METADATA.md sha256: `c7c7b3767ff400ea6977f09aa6e4ba574cc02658b9ff954e28c5b5f02ad39484`
- Log: `logs/exp_0015/run_20260208T063527Z_0698009.log`

### V3 (KC1_TTT_V3 candidate, H=5, T=0.0725)

- Run dir: `experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/v3_20260208T113631Z_0698009`
  - metrics.csv sha256: `f88d4749c6a2fd4f2170c547574b2f592673440d55ebc62f96a16c79655928d0`
  - summary.csv sha256: `300f5ef3723cec324da695e2659e36f89d170f28b56fb64dfef052f7fbd7fe88`
  - RUN_METADATA.md sha256: `da97bd8d25589e696d26d116903d1812ca2c471f7cff0ab1eb1707af9583763d`
- Log: `logs/exp_0015/run_20260208T063632Z_0698009.log`

Note: `RUN_METADATA.md` labels `kc1_variant: KC1_TTT_V2` in both runs (runner hardcoded), but the effective gate differs by the passed `--kc1_t` value (0.075 vs 0.0725).

## Sanity (SPEC exp_0016)

Both runs:
- controls: PASS (2 control configs, overall_pass_rate=1.0)
- negative: FAIL (overall_pass_rate=0.0)

## Target Config Result (paired; from summary.csv)

Target: `si128_clonal_init_k_point_mutation_k1p0` (queue11)

- V2: kc1_fail_count=19/30 => kc1_fail_rate=0.633333; overall_pass_rate=0.366667
- V3: kc1_fail_count=2/30 => kc1_fail_rate=0.066667; overall_pass_rate=0.933333

95% CI (Wilson; via `tools/analysis/exp0015_single_config_ci.py`):
- V2 kc1_fail_rate: `[0.455136, 0.781261]`
- V3 kc1_fail_rate: `[0.018477, 0.213235]`

## Queue11 Guard Activity Proxy

Non-zero `kc1_fail_rate` configs in queue11:
- V2: 2/11 (`si128_clonal_init_k_point_mutation_k1p0`, `si64_clonal_init_per_locus_flip_p0p01`)
- V3: 2/11 (`si128_clonal_init_k_point_mutation_k1p0`, `si64_clonal_init_per_locus_flip_p0p01`)

## Decision (evidence-only)

GO for using `KC1_TTT_V3 (H=5,T=0.0725)` as vNext default in subsequent experiments: it materially reduces KC1 false negatives on the worst-case target under paired seeds while keeping sanity stable and maintaining non-zero guard activity on queue11.

## Monitoring

Commands used: `reports/analysis/TASK_0122_MONITORING_COMMANDS.md`

