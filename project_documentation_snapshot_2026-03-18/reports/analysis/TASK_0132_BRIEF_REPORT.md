# TASK-0132 BRIEF REPORT — diagnose + optimize gpu_int end-to-end slowdown (instrumentation + scalar transfer) preserving parity

HEAD (start): `a63083de83efd47e43580b53d25c8ceef622b26e` (branch: `test`)

## Baseline (From TASK-0131)

Scenario: batch2-first1 subset queue (1 config + sanity), seeds=30, gen=50, pop=30, workers=1, KC1 H=5 T=0.0725.
- CPU wall: 16.824 s
- gpu_int wall: 1878.579 s
- Parity: `EQUIVALENCE: PASS`

## Diagnosis (Root Cause)

1. **Hot path transferred per-pair diffs back to CPU** (Python list materialization) every generation.
2. The runner’s import path logic was brittle; profiling revealed an import fallback case (fixed by correcting repo-root path injection).

## Fixes / Optimizations (No Semantic Changes)

1. **GPU returns a scalar integer `sum_diff` instead of a per-pair diff list**
   - GPU does integer-only work: compare + integer reductions.
   - CPU computes `D` using the same division ordering as the reference:
     - `total = float(sum_diff) / L`
     - `D = total / pairs`
2. Added **GPU environment diagnostics** and **per-stage profiling** (opt-in):
   - Runner flag: `--hamming_profile`
   - Logs include `torch_cuda_available`, device name/capability, and `HAMMING_PROFILE` breakdown for generation=1 per seed.

Changed files:
- `cognitive/gpu/hamming_accel.py`
- `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`

## Reproduction (Same Scenario After Fix)

Queue:
- `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/_task0131_batch2_first1_queue.jsonl`

Runs (example out_dirs from this task execution):
- CPU out_dir: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0132b_cpu_first1_20260208T175419Z_a63083d`
  - wall: 19.536 s
- gpu_int out_dir: `experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0132b_gpuint_first1_20260208T175419Z_a63083d`
  - wall: 10.769 s

Parity command:
```powershell
$cpu = "experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0132b_cpu_first1_20260208T175419Z_a63083d/summary.csv"
$gpu = "experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/task0132b_gpuint_first1_20260208T175419Z_a63083d/summary.csv"
python tools/analysis/compare_cpu_gpu_equivalence.py --cpu_summary $cpu --gpu_summary $gpu --enforce_sanity_expectations
```

Result:
- `EQUIVALENCE: PASS` (summary.csv sha256 identical on this scenario).

## Instrumentation Snapshot (Example)

From `logs/exp_0015/run_20260208T175439Z_a63083d.log`:
- For seed 1001 (warm-up): `kernel_ms≈55.7`, `total_s≈0.180`
- For subsequent seeds: `kernel_ms≈0.5..0.7`, `total_s≈0.0013..0.0019`

Interpretation:
- The earlier catastrophic slowdown was dominated by Python-side materialization/transfer overhead.
- Scalar transfer reduces per-generation overhead enough that gpu_int becomes end-to-end faster on this scenario.

## Decision (Router Recommendation)

- Keep router v2 recommendation as **advisory only** (`recommended_overrides.hamming_backend=gpu_int`).
- Recommendation remains opt-in via task fields (`expected_compute_high=true`) or heuristic; CPU authoritativeness and PASS/FAIL semantics are unchanged.

## Verification

- `pytest -q` PASS.

