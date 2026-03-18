# TASK-4800 BRIEF REPORT

## Scope
- Verify deterministic reproducibility for seeds `1339, 1347, 1364` via two consecutive reruns.

## Changes
- Added deterministic check runner:
  - `scripts/validation/check_phase4_determinism.py`
- Generated report:
  - `reports/determinism_check.md`

## Verification (L0)
- Command: `python scripts/validation/check_phase4_determinism.py --seeds 1339,1347,1364 --profile configs/profiles/gpu_profile_v4_reference.yaml --baseline_root results/exp_0700_applied_v4_gpu_gate/gate/gpu/baseline --tmp_root results/.tmp_task4800_determinism --report_out reports/determinism_check.md --tol 1e-6`
- Result: PASS
- Output summary: `overall_pass=true`, all per-seed delta and loss traces matched under tolerance `1e-6`.

## Artifacts
- `scripts/validation/check_phase4_determinism.py`
- `reports/determinism_check.md`

## Risks / Limitations
- Check covers target seeds only (as specified), not full 30-seed space.

## Rollback
- `git revert <commit_hash>`
