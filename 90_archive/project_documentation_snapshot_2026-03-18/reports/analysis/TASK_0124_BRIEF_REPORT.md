# TASK-0124 BRIEF REPORT — long-run queue11 under KC1_TTT_V3 (CPU-only, seeds↑)

HEAD: `79bd1c46a2197b46d5c198d41d4c14ab43883a8d`

## Runs (local; raw CSVs not committed)

Runner: `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`

Queue (11 configs): `experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl`

KC1: `KC1_TTT_V3` (H=5, T=0.0725)

### Smoke

- Run dir: `experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/smoke_queue11_v3_20260208T120635Z_79bd1c4`
- Sanity (summary.csv): controls PASS, negative FAIL.

### Long-run (authoritative)

Note (deviation): default seeds file `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/SEEDS.md` contains 30 numeric seeds, so for seeds=90 this run used:
- Seeds file: `experiments/exp_0015_kc1_ttt_vnext_validation/SEEDS_TASK0120_120.md` (first 90 seeds used)

- Params: seeds=90, generations=50, population=30, include_sanity
- Run dir: `experiments/exp_0016_kc1_ttt_v3_validation/RESULTS/long_queue11_v3_20260208T121019Z_79bd1c4`
  - metrics.csv sha256: `309d05561f85975102d534d2c07d9d416fb9773b6741c95558fc6af66efc0529`
  - summary.csv sha256: `7bf56e2efc1a150cd45544fe19d56ec350ff230b2a9618e257754655960b781d`
  - RUN_METADATA.md sha256: `987b2f4326bdf7f117d2146ee0d8cc1c05b4be03f167d6aff421a054242a6a21`
- Log: `logs/exp_0015/run_20260208T071019Z_79bd1c4.log`

## Sanity (long-run; from summary.csv)

- controls: PASS (overall_pass_rate=1.0 for both)
- negative: FAIL (overall_pass_rate=0.0)

## Target Config (long-run; from summary.csv)

Target: `si128_clonal_init_k_point_mutation_k1p0`

- kc1_fail_count=2/90 => kc1_fail_rate=0.022222
- threshold_fail_rate=0.0
- overall_pass_rate=0.977778

## Guard Activity (long-run; queue11)

Non-zero `kc1_fail_rate` configs in queue11: 2/11
- `si128_clonal_init_k_point_mutation_k1p0`: 0.022222
- `si64_clonal_init_per_locus_flip_p0p01`: 0.011111

## Decision (evidence-only)

GO: KC1_TTT_V3 remains stable on queue11 with seeds increased to 90, keeps sanity stable, maintains non-zero guard activity, and keeps the target config KC1 fail rate low (2/90).

## Monitoring

Commands: `reports/analysis/TASK_0124_MONITORING_COMMANDS.md`

