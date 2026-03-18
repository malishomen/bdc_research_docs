# KC1_TTT false-negative risk quantification on queue11 (exp_0012 metrics) — Horizon/Threshold Sweep

Task: TASK-0117  

## Repo State

- Repo: `d:\projects\Bio_Digital_Core\Bio_digital_core`
- Branch: `test`
- HEAD: `03994e6ca12b59d5add32dbec0a276fe20912d9e`
- `pytest -q`: PASS (`39 passed`)

## Objective (Evidence-Only)

Quantify KC1_TTT false-negative risk on the 11-config queue by:

1) sweeping KC1_TTT horizon/threshold parameters `(H,T)` over exp_0012 metrics, and
2) computing `time_to_D_ge_0_10` distributions.

No evolution runs are executed; all computations are performed on existing `metrics.csv`.

## Inputs / Evidence Artifacts

- exp_0012 metrics (gen=50): `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/metrics.csv`
- queue (11 configs): `experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl`

Derived analysis outputs (local, under RESULTS; not committed):

- `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/analysis_task_0117/kc1_ttt_baseline_by_config.csv`
- `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/analysis_task_0117/kc1_ttt_tradeoff_summary.csv`
- `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/analysis_task_0117/kc1_ttt_sweep_by_config.csv`

## Definitions (Pre-Registered Grid)

Grid:

- `H ∈ {1,2,3,4,5}`
- `T ∈ {0.05, 0.075, 0.10, 0.125, 0.15}`

KC1 fail definition used for sweep:

- `kc1_fail(H,T)=1` iff `max(D)` over generations `<= H` is **strictly < T`.

Time-to-threshold:

- `time_to_D_ge_0_10 = first generation g where D>=0.10`, else `None`.

Baseline KC1_TTT setting (for sanity check / comparison):

- `H=3, T=0.10`

## Command Run

```bash
python tools/analysis/exp0012_kc1_ttt_horizon_sweep.py ^
  --metrics_csv experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/metrics.csv ^
  --queue_jsonl experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl ^
  --out_dir experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/analysis_task_0117
```

## Baseline (H=3,T=0.10): 11 Configs

Baseline sanity check outcome reproduces the observed split:

- `kc1_fail_rate==1.0`: 5 configs
- `kc1_fail_rate==0.0`: 6 configs

Per-config baseline table (from `kc1_ttt_baseline_by_config.csv`):

|config_id|kc1_fail_rate|time_to_D_ge_0p10_median|
|---|---:|---:|
|si128_clonal_init_k_point_mutation_k1p0|1.0|7|
|si128_clonal_init_k_point_mutation_k2p0|1.0|4|
|si128_clonal_init_k_point_mutation_k4p0|0.0|2|
|si128_clonal_init_per_locus_flip_p0p01|1.0|6|
|si128_clonal_init_per_locus_flip_p0p02|0.0|3|
|si128_clonal_init_per_locus_flip_p0p05|0.0|2|
|si64_clonal_init_k_point_mutation_k1p0|1.0|4|
|si64_clonal_init_k_point_mutation_k2p0|0.0|2|
|si64_clonal_init_per_locus_flip_p0p01|1.0|7|
|si64_clonal_init_per_locus_flip_p0p02|0.0|3|
|si64_clonal_init_per_locus_flip_p0p05|0.0|2|

Baseline time-to-D>=0.10 separation (per-config medians):

- fail group (5 configs): medians = `[7, 4, 6, 4, 7]`, median of medians = `6`
- pass group (6 configs): medians = `[2, 3, 2, 2, 3, 2]`, median of medians = `2`

## Trade-off Summary Over (H,T)

Source: `kc1_ttt_tradeoff_summary.csv`

Columns:

- `mean_fail_rate_over_11(H,T)`: mean of per-config fail rates over the 11 configs
- `configs_fail_rate_1p0(H,T)`: number of configs where all seeds fail under (H,T)

Key rows (selected):

|H|T|mean_fail_rate_over_11|configs_fail_rate_1p0|configs_fail_rate_0p0|
|---:|---:|---:|---:|---:|
|3|0.10|0.454545|5|6|
|4|0.10|0.272727|3|8|
|4|0.05|0.0|0|11|
|5|0.075|0.018182|0|10|
|5|0.10|0.272727|3|8|

Minimal removals of systematic (fail_rate==1.0) failures within this grid:

- At `H=4, T=0.05`: `configs_fail_rate_1p0 = 0` (no config has all seeds failing).
- At `H=5, T=0.075`: `configs_fail_rate_1p0 = 0` (still some non-zero mean fail rate).

## Conclusion (Evidence-Only)

On the 11-config queue (exp_0012 metrics, gen=50):

1) Under baseline `H=3, T=0.10`, KC1_TTT would systematically fail 5/11 configs even though these configs later reach `D>=0.10` (median time-to-threshold for those 5 is around generations 4–7).
2) Within the tested grid, relaxing horizon/threshold can remove “fail all seeds” behavior for all configs (e.g., `H=4,T=0.05` or `H=5,T=0.075`), but this report does not propose any threshold change; it only quantifies the trade-off surface on existing data.

