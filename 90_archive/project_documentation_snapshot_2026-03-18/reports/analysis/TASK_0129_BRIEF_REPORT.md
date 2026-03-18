# TASK-0129 BRIEF REPORT — feasibility spike: mutation-only GPU backend viability (determinism + artifact parity plan)

HEAD (start): `5ff9cf30d1302516c15741a3b99ed13a0b6cb36f` (branch: `test`)

## Status

- **Mutation-only GPU-equivalent runner:** **NOT READY**
- **Hybrid GPU accelerator (D-only):** **FEASIBLE (plan only; not implemented)**

## Why NOT READY (2-3 reasons)

1. **RNG parity blocker:** exp_0015 semantics use PiStream slicing + SHA256 + Python `random.Random`. A GPU backend using torch CUDA RNG will not match the CPU mutation decisions, so per-seed outcomes will diverge.
2. **Gate sensitivity:** KC1_TTT uses full-precision `D` for early generations; tiny numeric drift can flip `max(D)<=T` around `T≈0.0725..0.075`.
3. **Artifact parity requirement:** TASK-0128 L2 contract compares `summary.csv` rates; with `seeds_total=30`, equivalence effectively requires exact per-seed PASS/FAIL match.

## What Was Traced (CPU code path)

Reference: `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`
- Genome: base-4 digits (0..3) in Python lists.
- RNG streams: `experiments/exp_0015_kc1_ttt_vnext_validation/src/seed_streams.py` -> `random.Random`.
- Hotspot: `mean_pairwise_hamming()` is `O(pop^2 * L)` per generation.

## Minimal Plan Forward

Documented in: `docs/spec/GPU_MUTATION_ONLY_FEASIBILITY.md`

Plan (v0 hybrid accelerator):
- Keep RNG + mutation + entropy on CPU (exact semantics).
- Offload only pairwise Hamming accumulation to GPU as an **integer sum**, then compute `D` on CPU to avoid float reduction drift.
- Measure speedup; do not promise.

Kill-criteria for any GPU attempt:
- Any per-seed KC1/KC2 outcome mismatch vs CPU on identical seeds/configs => stop (non-equivalent).
- If transfer overhead dominates and speedup < 1.2x => stop (not worth complexity).

## Verification

- `pytest -q` PASS.

