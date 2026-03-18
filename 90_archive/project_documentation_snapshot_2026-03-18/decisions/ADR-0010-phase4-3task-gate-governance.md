# ADR-0010: Phase 4 3-Task Gate Governance

Date: 2026-03-04
Status: ACCEPTED

## Context
- Phase 4 transitioned from 2-task MVP to a 3-task suite (`cloze`, `entity`, `category`).
- Existing N=30 run artifacts for the 3-task suite are available and reproducible from:
  - `results/edp1_exp0600_multirole_3task/aggregates/phase4_multirole_3task_n30_summary.json`.
- Prior comparator governance (ADR-0007) was defined for 2-task setup and must be canonized for 3-task gate decisions to avoid ambiguity.

## Decision
Adopt strict 3-task canonical metrics for Phase 4 gate.

### 1) Per-seed gains
For seed `i`:
- `gain_cloze_i = max_accuracy_i - best_baseline_accuracy_i`
- `gain_entity_i = max_entity_accuracy_i - best_entity_baseline_accuracy_i`
- `gain_category_i = max_category_accuracy_i - best_category_baseline_accuracy_i`

### 2) Canonical gate metrics (3-task)
- `A1_3_i = gain_cloze_i + gain_entity_i + gain_category_i`
- `A2_3_i = min(gain_cloze_i, gain_entity_i, gain_category_i)` (primary metric)
- `A3_3_i = 1[gain_cloze_i > 0 and gain_entity_i > 0 and gain_category_i > 0]`

Reporting for `A3_3`:
- Pareto rate with Wilson 95% CI over `{A3_3_i}`
- Pareto magnitude with `A2_3_i` only for seeds where `A3_3_i = 1`, else `0`.

### 3) Role-necessity rule (unambiguous PASS/FAIL at role level)
For each role `r ∈ {cloze, entity, category}`:
- Ablate role by setting `gain_r_i = 0`, keep other gains unchanged.
- Compute `primary_drop_i(r) = A2_3_full_i - A2_3_ablated_i(r)`.
- `degrade_ge_5pct_rate(r) = mean(primary_drop_i(r) >= 0.05)`.
- `interchangeable_le_2pct_rate(r) = mean(|primary_drop_i(r)| <= 0.02)`.

Role verdict:
- `NECESSARY` iff:
  - `degrade_ge_5pct_rate(r) >= 0.80`, and
  - `CI95_low(mean(primary_drop(r))) > 0`.
- Otherwise: `NOT_NECESSARY`.

### 4) Gate decision classes
- `GATE PASS` iff all are true:
  - `CI95_low(mean(A1_3)) > 0`,
  - `CI95_low(mean(A2_3)) > 0`,
  - Role verdict is `NECESSARY` for all three roles.
- `GATE FAIL` iff any is true:
  - `CI95_high(mean(A1_3)) <= 0`, or
  - `CI95_high(mean(A2_3)) <= 0`, or
  - two or more role verdicts are `NOT_NECESSARY`.
- `GATE NOT PASSED YET` in all remaining cases.

## Governance Guardrails
- Post-hoc threshold tuning is forbidden.
- Any change to:
  - metric formulas,
  - threshold values (`0.05`, `0.02`, `0.80`),
  - gate class rules,
  requires a new ADR approved before publishing a new gate verdict.

## Consequences
- 3-task recompute and role-ablation artifacts must use `A1_3/A2_3/A3_3` and include `gain_category`.
- Old policy strings (heuristic recommendations) are non-canonical and must not be used as gate verdict logic.
- Phase 4 reports must explicitly separate:
  - `RUN COMPLETE` (execution status),
  - `GATE PASS/FAIL/NOT PASSED YET` (governance status).

## Rollback
- Revert the ADR commit:
  - `git revert <commit-hash-containing-ADR-0010>`
- Until superseded by a newer ADR, ADR-0010 remains canonical for Phase 4 3-task gate governance.
