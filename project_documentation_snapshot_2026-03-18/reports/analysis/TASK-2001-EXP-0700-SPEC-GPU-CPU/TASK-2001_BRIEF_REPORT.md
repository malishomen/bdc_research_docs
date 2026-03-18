# TASK-2001 BRIEF REPORT

## Scope
- Pre-register applied practical experiment protocol (EXP-0700).
- Freeze pilot definitions, budgets, seed policy, CI method, and comparators before heavy runs.

## Changes
- Added experiment spec:
  - `docs/experiments/EXP-0700_APPLIED_GPU_CPU_2026-03-04.md`

## Verification (L0)
- Command: `rg -n "ADR-0013|Pilot A|Pilot B|Diagnostic|Gate|N=10|N=30|delta_gpu|delta_cpu|CI|manifest" docs/experiments/EXP-0700_APPLIED_GPU_CPU_2026-03-04.md`
- Result: PASS

## Artifacts
- `docs/experiments/EXP-0700_APPLIED_GPU_CPU_2026-03-04.md` - pre-registered protocol.
- `reports/analysis/TASK-2001-EXP-0700-SPEC-GPU-CPU/TASK-2001_BRIEF_REPORT.md` - this report.

## Risks / Limitations
- Uses currently available local workloads; future refactors may require EXP version bump.

## Rollback
- `git revert <commit-hash-containing-task-2001>`
