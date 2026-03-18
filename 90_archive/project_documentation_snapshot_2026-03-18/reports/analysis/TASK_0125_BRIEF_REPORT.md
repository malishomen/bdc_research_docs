# TASK-0125 BRIEF REPORT — deferred sweep thaw (batch-1) under KC1_TTT_V3 (CPU authoritative)

HEAD: `44f0eb7c07ef85d5dc26c5325e9dec2624c363a5`

## Batch-1 Queue (pre-registered; 16 configs)

Queue file: `experiments/exp_0016_kc1_ttt_v3_validation/QUEUES/batch1_queue.jsonl`

Config IDs:
- si128_clonal_init_k_point_mutation_k1p0
- si128_clonal_init_k_point_mutation_k2p0
- si128_clonal_init_k_point_mutation_k4p0
- si128_clonal_init_per_locus_flip_p0p01
- si128_clonal_init_per_locus_flip_p0p02
- si128_clonal_init_per_locus_flip_p0p05
- si64_clonal_init_k_point_mutation_k1p0
- si64_clonal_init_k_point_mutation_k2p0
- si64_clonal_init_k_point_mutation_k4p0
- si64_clonal_init_per_locus_flip_p0p01
- si64_clonal_init_per_locus_flip_p0p02
- si64_clonal_init_per_locus_flip_p0p05
- si128_random_init_k_point_mutation_k2p0
- si128_random_init_per_locus_flip_p0p05
- si64_random_init_k_point_mutation_k2p0
- si64_random_init_per_locus_flip_p0p05

## Run (local; raw CSVs not committed)

Runner: `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`

Seeds file: `experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md`

KC1: `KC1_TTT_V3` (H=5, T=0.0725)

### Smoke

- Run dir: `experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/smoke_batch1_v3_20260208T121946Z_44f0eb7`
- Sanity: controls PASS, negative FAIL.

### Batch run (authoritative)

- Params: seeds=30, generations=50, population=30, include_sanity
- Run dir: `experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/batch1_v3_20260208T122017Z_44f0eb7`
  - metrics.csv sha256: `59ae1c600e7e3fcbeee3f418d5f79f96998a432e9cb92b8f9563a8339f1cf72a`
  - summary.csv sha256: `b8bf5ca1cf5e56d112e808f5d5c58946aa0bea5f40297dc42a66d0ab3671e552`
  - RUN_METADATA.md sha256: `6f8c68bee53ea2a9cb6b198aafdda796f49e68e030df1eb4c6c62fd2d236dbae`

## Sanity (batch run; from summary.csv)

- controls: PASS (2 control configs, overall_pass_rate=1.0)
- negative: FAIL (overall_pass_rate=0.0)

## Batch Outcomes (16 configs; set=`queue11` in summary.csv)

- overall_pass_rate min: `0.933333`
- overall_pass_rate median: `1.0`
- configs with non-zero kc1_fail_rate: `2/16`
  - `si128_clonal_init_k_point_mutation_k1p0`: kc1_fail_rate=0.066667; overall_pass_rate=0.933333
  - `si64_clonal_init_per_locus_flip_p0p01`: kc1_fail_rate=0.033333; overall_pass_rate=0.966667
- configs with non-zero threshold_fail_rate: `0/16`

## Notes (no tuning)

- Observed failures on this batch are exclusively KC1-related (threshold_fail_rate==0 for all 16).
- Guard activity remains non-zero (KC1 triggers on 2 configs), i.e. no evidence of “KC1 disappears” on this batch.

## Monitoring

Commands: `reports/analysis/TASK_0125_MONITORING_COMMANDS.md`

