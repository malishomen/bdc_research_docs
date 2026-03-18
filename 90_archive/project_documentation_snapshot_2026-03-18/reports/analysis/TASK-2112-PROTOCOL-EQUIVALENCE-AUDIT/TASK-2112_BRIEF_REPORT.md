# TASK-2112 BRIEF REPORT

## Scope
- Audit CPU/GPU baseline-vs-optimized protocol equivalence under row-level run contract v3.
- Close critical mismatches for the next diagnostic rerun protocol.

## Changes
- Added audit script:
  - `scripts/analysis/task2112_protocol_equivalence_audit.py`
- Extended matrix runner with GPU optimized LR override:
  - `scripts/applied/run_applied_matrix.py` (`--gpu_optimized_lr`).
- Produced machine-readable audit artifacts:
  - `reports/analysis/TASK-2112-PROTOCOL-EQUIVALENCE-AUDIT/protocol_audit_current.json`
  - `reports/analysis/TASK-2112-PROTOCOL-EQUIVALENCE-AUDIT/protocol_audit_current.csv`
  - `reports/analysis/TASK-2112-PROTOCOL-EQUIVALENCE-AUDIT/protocol_audit_equivalent_profile.json`
  - `reports/analysis/TASK-2112-PROTOCOL-EQUIVALENCE-AUDIT/protocol_audit_equivalent_profile.csv`

## Verification (L0)
- Command: `python scripts/analysis/task2112_protocol_equivalence_audit.py --run_index D:/projects/Bio_Digital_Core/Bio_digital_core/results/exp_0700_applied_v2/diagnostic/aggregates/run_index_v3.json --out_json results/.tmp_task2112_audit_current.json --out_csv results/.tmp_task2112_audit_current.csv`
- Result: PASS
- Output summary: `critical_equivalence_pass=False`, `critical_fail_count=10`.

- Command: `python scripts/applied/run_applied_matrix.py --level diagnostic --out_root results/.tmp_task2112_equiv_diag --base_seed 1337 --seeds 1 --pilots all --gpu_optimized_amp_mode on --gpu_optimized_batch_size 8 --gpu_optimized_steps 120 --gpu_optimized_lr 2e-5`
- Result: PASS
- Output summary: `failure_count=0`.

- Command: `python scripts/analysis/task2112_protocol_equivalence_audit.py --run_index D:/projects/Bio_Digital_Core/Bio_digital_core/results/.tmp_task2112_equiv_diag/diagnostic/aggregates/run_index_v3.json --out_json D:/projects/Bio_Digital_Core/Bio_digital_core/results/.tmp_task2112_audit_equiv_diag.json --out_csv D:/projects/Bio_Digital_Core/Bio_digital_core/results/.tmp_task2112_audit_equiv_diag.csv`
- Result: PASS
- Output summary: `critical_equivalence_pass=True`, `critical_fail_count=0`.

## Checklist Verdict
- Effective token budget parity (GPU): **PASS** (`12x80 == 8x120`).
- LR scaling parity (GPU): **PASS** (`2e-5 / 3e-5 ~= 8/12`).
- CPU population/generations/subset/lambda parity: **PASS**.
- Stochastic layer behavior parity: **PASS** (dropout fixed `0.0` in `run_once` model).

## Artifacts
- `scripts/analysis/task2112_protocol_equivalence_audit.py` - protocol checklist auditor.
- `scripts/applied/run_applied_matrix.py` - GPU optimized LR override support.
- `reports/analysis/TASK-2112-PROTOCOL-EQUIVALENCE-AUDIT/*.json|*.csv` - audit evidence before/after remediation.
- `reports/analysis/TASK-2112-PROTOCOL-EQUIVALENCE-AUDIT/TASK-2112_BRIEF_REPORT.md` - task report.

## Risks / Limitations
- Equivalence closure ensures protocol fairness but does not guarantee statistical pass on diagnostic gate.
- Subsequent robustness iteration still required (TASK-2113).

## Rollback
- Revert with: `git revert <TASK-2112_commit_hash>`
