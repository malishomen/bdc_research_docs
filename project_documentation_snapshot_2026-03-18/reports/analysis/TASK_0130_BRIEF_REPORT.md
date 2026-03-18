# TASK-0130 BRIEF REPORT — hybrid GPU accelerator v0 (D-only): integer pairwise-Hamming on GPU, D on CPU, parity + speed

HEAD (start): `d5c611319c8b2d310c1d84be1e36e5a018d14455` (branch: `test`)

## What Changed

- GPU integer hamming accelerator module:
  - `cognitive/gpu/hamming_accel.py`
  - GPU computes per-pair Hamming diff counts using integer ops only; CPU computes `D` from those diffs using the same per-pair float accumulation order as the reference.
- Optional runner flag (default unchanged):
  - `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`
  - New flag: `--hamming_backend cpu|gpu_int` (default `cpu`)
  - `RUN_METADATA.md` records `hamming_backend`.
- Tests:
  - `tests/test_hamming_accel_parity.py` (GPU parity test auto-skips if CUDA unavailable)
- Benchmark tool:
  - `tools/analysis/bench_hamming_backend.py` (microbench + end2end smoke)

## Parity (Required)

End-to-end smoke was run twice on the same single-config queue (seeds=5, gen=10, pop=30), once with `--hamming_backend cpu` and once with `--hamming_backend gpu_int`.

Contract check:
```powershell
$cpu = \"experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/_task0130_bench_tmp/out_cpu/summary.csv\"
$gpu = \"experiments/exp_0015_kc1_ttt_vnext_validation/RESULTS/_task0130_bench_tmp/out_gpu_int/summary.csv\"
python tools/analysis/compare_cpu_gpu_equivalence.py --cpu_summary $cpu --gpu_summary $gpu --enforce_sanity_expectations
```

Result:
- `EQUIVALENCE: PASS` (identical `summary.csv` sha256 for CPU vs gpu_int on this smoke).

## Performance (Measured; No Promises)

Microbench (pairwise-Hamming only; pop=30, L=256, iters=200):
- CPU: 1.366 s
- GPU int: 0.219 s
- speedup: **6.23x**

Microbench (pop=128, L=256, iters=50):
- CPU: 6.403 s
- GPU int: 0.183 s
- speedup: **35.0x**

End-to-end smoke (single config, seeds=5, gen=10, pop=30):
- CPU: 0.707 s
- GPU int: 0.911 s
- speedup: **0.78x** (slower; overhead dominates at this tiny run)

Repro commands:
```powershell
python tools/analysis/bench_hamming_backend.py --mode micro --pop 30 --length 256 --iters 200
python tools/analysis/bench_hamming_backend.py --mode end2end
```

## Kill-Criteria Status

- Per-seed parity vs baseline on the smoke: **PASS**.
- Speedup >= 1.2x on microbench: **PASS**.
- End-to-end speedup on tiny smoke: **FAIL** (expected overhead); this does not violate the “do not promise speedup” constraint, but it is a practical warning.

## Notes / Caveats

- The `gpu_int` backend is intentionally limited to integer diffs on GPU; RNG and mutations remain CPU-only.
- For small end-to-end runs, CPU↔GPU transfer + kernel launch overhead can dominate. Larger populations/lengths are where the microbench shows the backend is worthwhile.

## Rollback Plan

- `git restore -SW .`
- If mistaken commit: `git reset --hard HEAD~1` and log FAIL in `AGENTS_LOG.md`.

