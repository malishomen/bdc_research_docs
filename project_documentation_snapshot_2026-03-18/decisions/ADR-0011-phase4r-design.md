# ADR-0011: Phase 4R Minimal Redesign Protocol

Date: 2026-03-04  
Status: ACCEPTED

## Context
- Frozen baseline (`TASK-1899`) is fixed at:
  - `RUN COMPLETE`
  - `GATE FAIL` under `ADR-0010`.
- Root-cause dossier (`TASK-1900`) identified:
  1. category gain saturation (`gain_category = 0` in 29/30 seeds),
  2. balanced metric drag (`A2_3 <= 0` in 29/30 seeds),
  3. role interchangeability (`degrade>=5%` rates are 0.0 for all roles).

## Decision
Run one minimal, flag-gated redesign cycle (Phase 4R) before any broader architectural rewrite.

## What Changes

### Primary arm (`P4R_MINIMAL_ARM_A`)
- `category_metric_mode = balanced_accuracy`
  - category accuracy computed as macro-average recall over classes `{0,1}`.
- `collective_scheme = s1_gain`
  - in collective mode, per-individual fitness is based on per-task gains vs baselines, not raw accuracies.
- `role_balance_bonus = 0.15`
  - additive bonus on individual fitness scaled by role underrepresentation in current generation.

### Fallback arm (`P4R_MINIMAL_ARM_B`)
Used only if arm A fails smoke stop-rules.
- same as arm A plus:
  - `role_balance_bonus = 0.30`,
  - `collective_category_weight = 1.50`.

## What Does NOT Change
- No changes to:
  - genome parameterization (`v2` architecture),
  - mutation operators / speciation internals,
  - Phase 4 gate formulas and thresholds from `ADR-0010`,
  - dataset source and seed policy.
- Backward compatibility:
  - all new behavior is opt-in via new CLI flags;
  - default behavior remains baseline-equivalent.

## Smoke Stop-Rules (mandatory before any full N=30)

Execute `N=5` seeds smoke in deterministic mode for selected arm.

Arm is **SMOKE PASS** only if all are true:
1. deterministic replay check passes for a repeated seed run (same summary core metrics),
2. recompute/ablation/provenance pipeline completes without schema regressions,
3. `gain_category_mean > 0` and `A2_3_mean` strictly improves over frozen baseline smoke reference,
4. role-ablation JSON contains all three role sections and valid verdict fields.

If any condition fails:
- **do not** run full N=30,
- promote fallback arm (if primary failed) or terminate with FAIL pathway (`TASK-1907`).

## Full Gate Rules (unchanged governance)
- Final gate verdict still uses `ADR-0010`:
  - `PASS / FAIL / NOT PASSED YET` decided strictly by canonical `A1_3/A2_3/A3_3` and role necessity rules.
- Post-hoc threshold/formula tuning is forbidden without another ADR.

## Consequences
- Redesign scope remains minimal and reversible.
- Scientific comparability with frozen baseline is preserved.
- Full N=30 cost is paid only after smoke evidence indicates non-trivial uplift.

## Rollback
- `git revert <commit-hash-containing-ADR-0011>`
