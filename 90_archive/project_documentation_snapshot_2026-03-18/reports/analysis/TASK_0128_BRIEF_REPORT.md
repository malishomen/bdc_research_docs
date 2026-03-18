# TASK-0128 BRIEF REPORT — GPU equivalence harness (mutation-only runner): contract + compare tool + quaternary demo

HEAD (start): `2c65ee4d19516270a23228bf3219e252d6be1d57` (branch: `test`)

## S1 Discovery: Existing GPU Path For Mutation-Only Runner

Searches (`git grep`) for `--device`, `cuda`, `torch`, `gpu`, `nvidia` found GPU code under `cognitive/` (torch/cuda training utilities) and GPU inventory logging in `experiments/exp_0015_kc1_ttt_vnext_validation/src/runner.py`, but **no GPU-equivalent runner/flag** for the mutation-only evolution semantics used by exp_0015/exp_0016.

Conclusion:
- **Mutation-only GPU replicate is NOT READY** (no canonical GPU runner path exists today).
- This is acceptable per task kill-criteria; we stop short of inventing a GPU runner.

## L2 Equivalence Contract (Minimal)

Minimal artifact-level contract for declaring CPU vs GPU equivalence for the mutation-only runner:

1. Compare `summary.csv` keyed by `(config_id, set)`.
2. Required fields must match:
   - `seeds_total` (int)
   - `kc1_fail_rate` (float; default exact unless tolerance specified)
   - `threshold_fail_rate`
   - `overall_pass_rate`
3. Sanity outcomes must be consistent (optional but recommended to enforce):
   - `set=="control"`: `overall_pass_rate==1.0`
   - `set=="negative"`: `overall_pass_rate==0.0`
4. Trajectory/`metrics.csv` equivalence is **optional** and not required by this minimal contract.

## What Changed (Artifacts)

- Compare tool: `tools/analysis/compare_cpu_gpu_equivalence.py`
  - Compares CPU vs GPU `summary.csv` and returns exit code 0 on PASS, 2 on FAIL, 1 on ERROR.
- Quaternary gpu_replicate task example:
  - `experiments/exp_0008_quaternary_router_skeleton/QUEUES/examples/gpu_replicate_equivalence_demo.jsonl`
  - Uses `compare_script` pointing to the compare tool and sets `do_not_merge_results=true`.
- Tests: `tests/test_compare_cpu_gpu_equivalence.py`

## How To Run

Compare tool:
```powershell
python tools/analysis/compare_cpu_gpu_equivalence.py `
  --cpu_summary <CPU_OUT_DIR>/summary.csv `
  --gpu_summary <GPU_OUT_DIR>/summary.csv `
  --enforce_sanity_expectations
```

Router v2 demo (routing-only):
```powershell
python experiments/exp_0008_quaternary_router_skeleton/src/quaternary_router_v2.py `
  --in_queue experiments/exp_0008_quaternary_router_skeleton/QUEUES/examples/gpu_replicate_equivalence_demo.jsonl `
  --out_decisions experiments/exp_0008_quaternary_router_skeleton/RESULTS/_task0128_demo_decisions.jsonl
```

Expected routing behavior:
- GPU replicate is `MAYBE_YES` (replicate-only) because `do_not_merge_results=true` and `compare_script` is present.
- CPU remains authoritative; GPU cannot affect PASS/FAIL.

## Verification

- `pytest -q` PASS.

## Next Step

Separate epic/experiment to implement a **GPU-equivalent mutation-only runner** that:
- preserves seed determinism (or defines explicit tolerances),
- produces the same artifact schema (`metrics.csv`, `summary.csv`, `RUN_METADATA.md`),
- and can be checked by `tools/analysis/compare_cpu_gpu_equivalence.py`.

