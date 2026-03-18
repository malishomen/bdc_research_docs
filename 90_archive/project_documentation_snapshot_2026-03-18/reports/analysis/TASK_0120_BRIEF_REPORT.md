# TASK-0120 BRIEF REPORT — focused exp_0015 run on worst-case config (si128 k1p0) + CI

Commit: `c05b6eec7e47b9f6fa41d0f2632e78279121a6b0` (start of TASK-0120)

## CPU Run (authoritative)

- Runner: `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`
- Queue: `experiments/exp_0015_kc1_ttt_vnext_validation/QUEUES/queue_single_si128_k1p0.jsonl`
- Seeds file: `experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md`
- Params: seeds=90, generations=50, population=30
- Gate: `KC1_TTT_V2` (H=5, T=0.075)
- Sanity included: controls + negative (`--include_sanity`)

Artifacts (local; raw CSVs not committed):

- Run dir: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/run_20260208T060901Z_c05b6ee`
  - metrics.csv sha256: `6b8f354de1d29d55fb84204a42994f0c0a38f59851ae78f98bc7edd62a19906f`
  - summary.csv sha256: `ba529c52df950f8626ebf6f1c489261ec4802d004af45b8560a4efb0ca2c63ab`
  - RUN_METADATA.md sha256: `c177becdd93cc5eaf491a820be4c3d6c8396e59cdcc2b955e59351dfe0ecc423`

Sanity (from `summary.csv`):

- controls: PASS (overall_pass_rate=1.0 for both control configs)
- negative: FAIL (overall_pass_rate=0.0)

Target config result (from `summary.csv`):

- `si128_clonal_init_k_point_mutation_k1p0`
  - kc1_fail_count=57 / 90 => kc1_fail_rate=0.633333
  - threshold_fail_rate=0.0
  - overall_pass_rate=0.366667

## Uncertainty (95% CI for kc1_fail_rate)

Computed by: `tools/analysis/exp0015_single_config_ci.py` on the same `summary.csv`.

- Wilson 95% CI: `[0.530223, 0.725527]`
- Clopper-Pearson 95% CI: `[0.525149, 0.732478]`

## Decision (evidence-only)

GO for further investigation (KC1_TTT_V2 reduces systematic fail-all-seeds on the legacy set), but NO-GO for promotion as-is without addressing the remaining high KC1 fail rate for `si128_clonal_init_k_point_mutation_k1p0` (57/90 seeds fail KC1 under current H=5,T=0.075).

## Monitoring

See: `reports/analysis/TASK_0120_MONITORING_COMMANDS.md`

