# exp_0012 (KC2) vs exp_0011 Overall Stack Reconciliation (Gate-Trace)

Task: TASK-0116  

## Repo State

- Repo: `d:\projects\Bio_Digital_Core\Bio_digital_core`
- Branch: `test`
- HEAD: `1426a8023d9b1412da9a67c62cbd48d57f076efb`
- `pytest -q`: PASS (`39 passed`)

## Objective (Evidence-Only)

Explain how `110/110 pass_kc2` in exp_0012 can coexist with exp_0011 “overall FAIL” signals, by applying exp_0011’s overall definition (KC1_TTT + final thresholds) to exp_0012 metrics for the same 11 queued configs.

## Definitions (Exact Sources)

Overall stack definition source:

- `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/src/kill_eval.py`

Rules used by exp_0011 `kill_eval.py`:

- **KC1_TTT early fail:** for `generation <= 3`, if 3 D-values exist and `max(D) < 0.10` then FAIL.
- **Threshold fail (KC2-like):** at final generation, FAIL if `E_genotype_bits < 2.5` or `D < 0.30`.
- **Overall PASS:** seed passes only if not KC1_TTT fail and not threshold fail.

Notes:

- exp_0012’s `kc2_failure_component` in `summary.csv` is **threshold-only** classification and does not include KC1_TTT.
- exp_0011 smoke run used `generations: 15` (see `RUN_METADATA.md` below), so its “final thresholds” are evaluated at gen=15 for smoke.

## Inputs / Evidence Artifacts

11-config queue (the comparison set for this task):

- `experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl`

exp_0012 full-run pointer and metrics:

- `experiments/exp_0012_kc2_diagnostics/RESULTS/LATEST_POINTER.md`
- Run dir: `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac`
- Metrics: `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/metrics.csv`

exp_0011 smoke artifacts (context for “overall FAIL” statement):

- `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/RESULTS/LATEST_POINTER.md`
- Smoke run dir: `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/RESULTS/smoke_20260128T075827Z_a05c1ec`
- Smoke metadata (shows generations=15): `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/RESULTS/smoke_20260128T075827Z_a05c1ec/RUN_METADATA.md`
- Smoke summary (“overall KC stack”): `experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/RESULTS/smoke_20260128T075827Z_a05c1ec/summary.csv`
- Narrative summary: `reports/analysis/EXP_0011_VNEXT_SMOKE_REPORT.md`

## Commands Run

1) Compute gate-trace on exp_0012 metrics (KC1_TTT vs thresholds) and produce derived metrics compatible with exp_0011 kill_eval:

```bash
python tools/analysis/exp0012_reconcile_kc1_ttt_vs_kc2.py ^
  --metrics_csv experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/metrics.csv ^
  --queue_jsonl experiments/exp_0008_quaternary_router_skeleton/QUEUES/exp0011_kc2_diagnostics_cpu_queue.jsonl ^
  --out_csv experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/gate_trace_all_configs.csv ^
  --out_csv_queue experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/gate_trace_queue_11_configs.csv ^
  --out_derived_metrics_for_kill_eval experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/derived_metrics_for_kill_eval_exp0011.csv
```

2) Apply exp_0011 “overall PASS/FAIL” definition (`kill_eval.py`) to the derived metrics (exp_0012 run):

```bash
python experiments/exp_0011_pistream_v3_phase0_vnext_kc1_ttt/src/kill_eval.py ^
  experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/derived_metrics_for_kill_eval_exp0011.csv ^
  --out_csv experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/derived_overall_by_kill_eval_exp0011.csv
```

## Result: Reconciliation Table (11 configs)

Source table:

- `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/gate_trace_queue_11_configs.csv`

Summary:

- For all 11 configs: `threshold_fail_rate == 0.0` (i.e., exp_0012 KC2 thresholds are reached at final gen=50).
- For 5 configs: `kc1_ttt_fail_rate == 1.0` which forces `overall_pass_rate == 0.0` under exp_0011’s overall stack.

|config_id|seeds_total|kc1_ttt_fail_rate|threshold_fail_rate|overall_pass_rate|final_generations_seen|
|---|---:|---:|---:|---:|---|
|si128_clonal_init_k_point_mutation_k1p0|10|1.0|0.0|0.0|50|
|si128_clonal_init_k_point_mutation_k2p0|10|1.0|0.0|0.0|50|
|si128_clonal_init_k_point_mutation_k4p0|10|0.0|0.0|1.0|50|
|si128_clonal_init_per_locus_flip_p0p01|10|1.0|0.0|0.0|50|
|si128_clonal_init_per_locus_flip_p0p02|10|0.0|0.0|1.0|50|
|si128_clonal_init_per_locus_flip_p0p05|10|0.0|0.0|1.0|50|
|si64_clonal_init_k_point_mutation_k1p0|10|1.0|0.0|0.0|50|
|si64_clonal_init_k_point_mutation_k2p0|10|0.0|0.0|1.0|50|
|si64_clonal_init_per_locus_flip_p0p01|10|1.0|0.0|0.0|50|
|si64_clonal_init_per_locus_flip_p0p02|10|0.0|0.0|1.0|50|
|si64_clonal_init_per_locus_flip_p0p05|10|0.0|0.0|1.0|50|

Cross-check (exp_0011 official overall definition applied to exp_0012 metrics):

- `experiments/exp_0012_kc2_diagnostics/RESULTS/run_20260208T044029Z_4ffc2ac/derived_overall_by_kill_eval_exp0011.csv`

## Conclusion (Evidence-Only)

There is no contradiction:

1) exp_0012 reports **KC2 thresholds only** (final `E>=2.5` and `D>=0.30`), which are satisfied for 110/110 seeds in the 11-config queue at `generation=50`.
2) exp_0011 “overall” includes **KC1_TTT** (early `gen<=3` diversity gate). When we apply exp_0011’s overall definition to exp_0012 metrics, **5/11 configs fail overall solely due to KC1_TTT** despite passing final thresholds.
3) Additionally, exp_0011 smoke “overall FAIL” statements are based on a **smoke run with `generations=15`**, so its “final thresholds” were evaluated at gen=15 for smoke (see smoke `RUN_METADATA.md`). That smoke context is not directly comparable to exp_0012 full diagnostics at gen=50 without explicitly aligning generations.

Diagnosis status: SUCCESS (reconciled via reproducible gate-trace; no parameter/threshold changes).

