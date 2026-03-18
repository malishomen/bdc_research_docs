# ADR-0012: Phase 4R Minimal Redesign Hypothesis Closure

Date: 2026-03-04  
Status: ACCEPTED

## Context
- Baseline is frozen (`TASK-1899`) with:
  - `RUN STATUS = RUN COMPLETE`
  - `GATE STATUS = FAIL` (ADR-0010).
- Root-cause analysis (`TASK-1900`) identified category-signal saturation and role interchangeability.
- Minimal redesign protocol (`ADR-0011`) defined two pre-registered smoke arms before any new full `N=30` run:
  - Arm A: balanced category metric + gain-based collective scheme + role-balance bonus.
  - Arm B: Arm A + stronger role/category emphasis.

## Evidence
- Smoke gate task: `TASK-1903-P4R-SMOKE-DETERMINISM-GATE`, `N=5` seeds (`1337..1341`).
- Determinism check: repeated identical-seed run produced identical core final metrics.
- Baseline control smoke:
  - `A2_3_mean = -0.0091229183`
  - `gain_category_mean = 0.0`
- Arm A smoke:
  - `A2_3_mean = -0.0057969843`
  - `gain_category_mean = 0.0`
- Arm B smoke:
  - `A2_3_mean = -0.0057969843`
  - `gain_category_mean = 0.0`
- Role-ablation outputs for both arms include all 3 role sections with valid verdict fields.

## Decision
Reject the current Phase 4R minimal redesign hypothesis for gate progression.

Concretely:
1. `P4R_MINIMAL_ARM_A` is closed for full gate escalation.
2. `P4R_MINIMAL_ARM_B` is closed for full gate escalation.
3. `TASK-1904-P4R-GATE-RUN-N30` is not authorized under this hypothesis.
4. `TASK-1905-P4R-GATE-DECISION` based on a new redesign N=30 is not produced.

## Rationale
- ADR-0011 stop-rule #3 requires `gain_category_mean > 0`.
- Both pre-registered redesign arms keep `gain_category_mean = 0.0`.
- Running a new full `N=30` after this would violate pre-registered governance.

## Consequences
- Phase 4 official status remains unchanged:
  - `RUN STATUS: RUN COMPLETE`
  - `GATE STATUS: FAIL` (ADR-0010).
- Further attempts require:
  - a new ADR with a new pre-registered redesign hypothesis,
  - a fresh smoke/determinism gate before any full N=30.

## Rollback
- `git revert <commit-hash-containing-ADR-0012>`
