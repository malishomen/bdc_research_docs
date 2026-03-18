# TASK-0126 BRIEF REPORT — deferred sweep thaw (batch-2 hard-mode) under KC1_TTT_V3 (CPU authoritative)

HEAD: `280847f4a2c506ac6331530319dc753cf00fa29b`

## Batch-2 Queue (12 configs; hard-mode; no overlap with batch-1)

Queue file: `experiments/exp_0016_kc1_ttt_v3_validation/QUEUES/batch2_queue.jsonl`

Config IDs:
- si256_clonal_init_k_point_mutation_k1p0
- si256_clonal_init_per_locus_flip_p0p01
- si256_random_init_k_point_mutation_k1p0
- si256_random_init_per_locus_flip_p0p005
- si128_random_init_k_point_mutation_k0p0
- si128_random_init_per_locus_flip_p0p001
- si128_clonal_init_k_point_mutation_k0p0
- si128_clonal_init_per_locus_flip_p0p0075
- si64_random_init_k_point_mutation_k0p0
- si64_random_init_per_locus_flip_p0p001
- si64_clonal_init_k_point_mutation_k0p0
- si64_clonal_init_per_locus_flip_p0p0075

## Run (local; raw CSVs not committed)

Runner: `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`

Seeds file: `experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md`

KC1: `KC1_TTT_V3` (H=5, T=0.0725)

### Smoke

- Run dir: `experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/smoke_batch2_v3_20260208T122744Z_280847f`
- Sanity: controls PASS, negative FAIL.

### Batch run (authoritative)

- Params: seeds=30, generations=50, population=30, include_sanity
- Run dir: `experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/batch2_v3_20260208T122806Z_280847f`
  - metrics.csv sha256: `399f2ade749006c999f74497ad2f9651ab28539734cbff03ab245d6e73d7708e`
  - summary.csv sha256: `1b02f42e9afe9de903ba83ba0d2fd0f4ee2338b27be9f9efc610d30e1191dd56`
  - RUN_METADATA.md sha256: `6efe5087094aceb737c9346fabe5b54748536eca12973f49dc3e3aabd844968e`

## Sanity (batch run; from summary.csv)

- controls: PASS (2 control configs, overall_pass_rate=1.0)
- negative: FAIL (overall_pass_rate=0.0)

## Outcomes (12 configs; set=`queue11` in summary.csv)

- overall_pass_rate min: `0.0`
- overall_pass_rate median: `1.0`
- configs with non-zero kc1_fail_rate: `5/12`
  - si128_clonal_init_k_point_mutation_k0p0: 1.0
  - si256_clonal_init_k_point_mutation_k1p0: 1.0
  - si64_clonal_init_k_point_mutation_k0p0: 1.0
  - si128_clonal_init_per_locus_flip_p0p0075: 0.533333
  - si64_clonal_init_per_locus_flip_p0p0075: 0.433333
- configs with non-zero threshold_fail_rate: `0/12`
  - Explicit statement: No evidence of threshold failures in batch-2 under gen=50 for configs that survive KC1.

Configs with overall_pass_rate==0.0 are exclusively KC1-killed (kc1_fail_rate==1.0; threshold_fail_rate==0.0):
- si128_clonal_init_k_point_mutation_k0p0
- si256_clonal_init_k_point_mutation_k1p0
- si64_clonal_init_k_point_mutation_k0p0

## Monitoring

Commands: `reports/analysis/TASK_0126_MONITORING_COMMANDS.md`

