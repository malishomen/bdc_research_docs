# TASK-2121 BRIEF REPORT

## Scope
- Formalize two-level fairness governance for applied reruns without changing ADR-0013 thresholds.

## Changes
- Added ADR:
  - `decisions/ADR-0015-applied-fairness-twolevel.md`
- Updated experiment spec doc:
  - `docs/experiments/EXP-0700_APPLIED_GPU_CPU_2026-03-04.md`

## Verification (L0)
- Command: `rg -n "ADR-0015|token/examples budget parity|advisory" decisions/ADR-0015-applied-fairness-twolevel.md docs/experiments/EXP-0700_APPLIED_GPU_CPU_2026-03-04.md`
- Result: PASS

## Artifacts
- `decisions/ADR-0015-applied-fairness-twolevel.md` - accepted governance update.
- `docs/experiments/EXP-0700_APPLIED_GPU_CPU_2026-03-04.md` - synchronized v4 governance addendum.
- `reports/analysis/TASK-2121-ADR-0015-APPLIED-FAIRNESS-TWOLEVEL/TASK-2121_BRIEF_REPORT.md` - task report.

## Risks / Limitations
- ADR changes execution governance, not model code or thresholds.
- Runtime validity still depends on contract v4 implementation and rerun evidence.

## Rollback
- Revert with: `git revert <TASK-2121_commit_hash>`
