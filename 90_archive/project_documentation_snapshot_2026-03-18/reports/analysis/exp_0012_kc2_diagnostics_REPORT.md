# exp_0012 KC2 Diagnostics Report (CPU-only)

Task: TASK-0115  
Local date context: 2026-02-08 (Asia/Tashkent)  

## Repo State / Preconditions

- Repo: `d:\projects\Bio_Digital_Core\Bio_digital_core`
- Branch: `test`
- HEAD: `4ffc2ac34265264ca9bcae3f415d59b7f82bf139`
- `pytest -q`: PASS (`39 passed`)

## Purpose

Diagnose KC2 outcomes (E vs D threshold failures) for configs scheduled by:

- Queue: `experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl` (11 tasks)

Constraints honored:

- CPU-only
- No tuning/selection
- No changes to exp_0007/exp_0009
- Raw CSV artifacts kept local (hashes recorded)

## Commands Run (Reproducible)

Help:

```bash
python experiments/exp_0012_kc2_diagnostics/src/kc2_diagnostic_runner.py --help
```

Mini-run (smoke):

```bash
python experiments/exp_0012_kc2_diagnostics/src/kc2_diagnostic_runner.py ^
  --queue experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl ^
  --seeds_file experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/SEEDS.md ^
  --pi_file datasets/pi_digits_10k.txt ^
  --seeds 2 --generations 10 --population 30 ^
  --out_dir experiments/exp_0012_kc2_diagnostics/RESULTS/mini_20260208T044000Z_4ffc2ac
```

Full run:

```bash
python experiments/exp_0012_kc2_diagnostics/src/kc2_diagnostic_runner.py ^
  --queue experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl ^
  --seeds_file experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/SEEDS.md ^
  --pi_file datasets/pi_digits_10k.txt ^
  --seeds 10 --generations 50 --population 30 ^
  --out_dir experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac
```

## Artifacts (Local, With Hashes)

Mini-run out dir:

- `experiments/exp_0012_kc2_diagnostics/RESULTS/mini_20260208T044000Z_4ffc2ac/metrics.csv`
  - sha256: `00017dd4493bcd3e9400e993da82d750b0dfe5e8703050a2b35a45d498fd02be`
- `experiments/exp_0012_kc2_diagnostics/RESULTS/mini_20260208T044000Z_4ffc2ac/summary.csv`
  - sha256: `da255c11031a76ce9094fbc49441eae8f8e77dec22d9805b4311a931ba8d5cc6`

Full-run out dir:

- `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/metrics.csv`
  - sha256: `d33dc1a0a2c96b3522fce8df2853e9c17adfde8f886df619b360de369f1b672c`
- `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/summary.csv`
  - sha256: `f0da0df4d813ad6a2eb8bb2fe40a947e5ccd7780c8381d80fde5a77b557bd7bc`

Full-run row counts:

- `summary.csv`: 110 rows (11 configs × 10 seeds)
- `metrics.csv`: 5500 rows (11 configs × 10 seeds × 50 generations)

Canonical pointers/metadata (tracked):

- `experiments/exp_0012_kc2_diagnostics/RESULTS/LATEST_POINTER.md`
- `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/RUN_METADATA.md`

## KC2 Classification Result

Overall (all seeds/configs):

- `pass_kc2`: 110
- `E_only`: 0
- `D_only`: 0
- `E_and_D`: 0

Per-config (10 seeds each):

|config_id|seeds|pass_kc2|E_only|D_only|E_and_D|mean_final_E|mean_final_D|median_tE>=2.5|median_tD>=0.30|
|---|---|---|---|---|---|---|---|---|---|
|si128_clonal_init_k_point_mutation_k1p0|10|10|0|0|0|4.906891|0.487615|1.0|25.0|
|si128_clonal_init_k_point_mutation_k2p0|10|10|0|0|0|4.906891|0.651472|1.0|13.0|
|si128_clonal_init_k_point_mutation_k4p0|10|10|0|0|0|4.906891|0.742022|1.0|6.0|
|si128_clonal_init_per_locus_flip_p0p01|10|10|0|0|0|4.906891|0.562425|1.0|21.0|
|si128_clonal_init_per_locus_flip_p0p02|10|10|0|0|0|4.906891|0.693847|1.0|10.0|
|si128_clonal_init_per_locus_flip_p0p05|10|10|0|0|0|4.906891|0.748150|1.0|4.0|
|si64_clonal_init_k_point_mutation_k1p0|10|10|0|0|0|4.906891|0.654684|1.0|13.0|
|si64_clonal_init_k_point_mutation_k2p0|10|10|0|0|0|4.906891|0.739173|1.0|6.0|
|si64_clonal_init_per_locus_flip_p0p01|10|10|0|0|0|4.906891|0.548204|1.0|22.0|
|si64_clonal_init_per_locus_flip_p0p02|10|10|0|0|0|4.906891|0.698434|1.0|9.0|
|si64_clonal_init_per_locus_flip_p0p05|10|10|0|0|0|4.906891|0.747134|1.0|4.0|

## Interpretation (Evidence-Only)

For the 11 configs scheduled by the exp_0011 KC2 diagnostics queue, KC2 thresholds (`E>=2.5` and `D>=0.30`) are met for all 10 seeds under CPU-only mutation-only dynamics. Therefore, these queued configs do not show KC2 failures under the current KC2 definitions.

If exp_0011 smoke still reports overall FAIL for a subset of these configs, the failure mode is more likely due to KC1_TTT (or another non-KC2 gate), not KC2.

## Diagnosis Status

SUCCESS: KC2 failure component classification is complete and reproducible for the queued 11 configs; result is "no KC2 failures observed" under exp_0012.

