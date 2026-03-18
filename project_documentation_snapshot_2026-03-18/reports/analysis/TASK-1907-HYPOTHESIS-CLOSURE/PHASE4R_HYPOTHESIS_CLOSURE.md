# PHASE4R HYPOTHESIS CLOSURE

## Run Status
- Phase 4 baseline run: **RUN COMPLETE** (`N=30`, seeds `1337..1366`).

## Gate Status
- Phase 4 gate: **FAIL** (unchanged, per ADR-0010).

## Closure Basis
- ADR-0011 mandated smoke stop-rules before any redesign `N=30`.
- TASK-1903 showed:
  - arm A: `gain_category_mean = 0.0`,
  - arm B: `gain_category_mean = 0.0`,
  - therefore stop-rule #3 failed for both arms.

## Decision
- The Phase 4R minimal redesign hypothesis is closed as insufficient for escalation.
- No redesign full `N=30` rerun (`TASK-1904`) is authorized under this hypothesis.

## Governance
- Formalized by:
  - `decisions/ADR-0012-phase4r-hypothesis-closure.md`
- Any further redesign requires:
  - a new ADR,
  - a new pre-registered smoke gate.
