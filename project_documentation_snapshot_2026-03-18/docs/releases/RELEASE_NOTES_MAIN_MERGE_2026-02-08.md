# Release Notes — Main Merge Checkpoint (2026-02-08)

This release notes document accompanies merging `test` into `main` as a canonical checkpoint before starting the “simplified wiki” workstream.

## Merge Summary

- **Source branch:** `test`
- **Target branch:** `main`
- **test HEAD (pre-merge):** `147745806104fbeadd3db92bf7e737617267631e`
- **main HEAD (pre-merge):** `79246329c2220dced7a12242f6a3161d50c13685`
- **Merge commit:** `1faf9d82a28645616d568e0255f8c9ea94d04946`

## Safety / Canon Notes

- **CPU remains authoritative.**
- **GPU does not influence PASS/FAIL evidence.**
- `gpu_int` is a **compute accelerator only** (integer pairwise-Hamming accumulation on GPU; `D` computed on CPU).
- No raw run CSVs under `RESULTS/` were committed as part of the checkpoint.

## Key Changes Included (High-Level)

### Quaternary routing + GPU governance scaffold

- Quaternary statuses `YES/NO/MAYBE_YES/MAYBE_NO` plus evidence levels `L0/L1/L2`.
- Router v2 skeleton that routes JSONL tasks to decision JSONL without executing compute.
- Rule-codes grounded in batch evidence:
  - `ZERO_MUTATION_OPERATOR`
  - `KC1_FAIL_ALL_SEEDS`
  - `SANITY_BROKEN`

### GPU equivalence harness (compare-tool) + demo

- Minimal L2 artifact-level equivalence contract (summary.csv-first).
- Deterministic compare tool for CPU vs GPU artifacts.
- Quaternary `gpu_replicate` example using `compare_script` and `do_not_merge_results=true`.

### Mutation-only GPU feasibility + hybrid accelerator

- Feasibility spike concluded a fully GPU-equivalent mutation-only runner is **NOT READY** (RNG parity + gate sensitivity).
- Implemented and validated **hybrid D-only accelerator**:
  - `--hamming_backend gpu_int` optional runner flag
  - parity checks and benchmarks
  - full batch2 run parity PASS with improved wall time (CPU vs gpu_int) under canonical constraints

## Verification

- `pytest -q` PASS on `main` after the merge.

