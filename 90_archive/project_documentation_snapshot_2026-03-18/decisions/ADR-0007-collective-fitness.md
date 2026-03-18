# ADR-0007: Phase 4 Cooperative Advantage Metric Governance

Date: 2026-03-02
Status: ACCEPTED

## Context
- Phase 4 uses 2-task MVP collective setup (`cloze + entity`) with Scheme S1:
  - per-individual fitness: `max(cloze_acc, entity_acc)`,
  - population collective score: `weighted_mean(best_cloze, best_entity)`.
- TASK-1803 initially reported:
  - `delta_old_i = collective_score_i - max_individual_collective_fitness_i`.
- Under S1 with equal weights, `collective_score_i` is an arithmetic mean of task-best values and therefore cannot exceed the max component:
  - `mean(a, b) <= max(a, b)` for all `a, b`.
- Therefore `delta_old` is structurally non-positive and cannot serve as an unbiased gate comparator.

## Evidence
- Source run artifacts (no retraining):
  - `results/edp1_exp0600_multirole/aggregates/phase4_multirole_n30_summary.json`
  - `results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.json`
- TASK-1803 old comparator (N=30):
  - `mean_delta_old = -0.2966691790`,
  - `95% CI = [-0.2999079896, -0.2934303684]`.
- Recomputed symmetric metrics on same N=30:
  - `A1` CI95: `[0.0126133312, 0.0280607879]`,
  - `A2` CI95: `[0.0001794477, 0.0064231588]`,
  - `A3` Pareto rate: `0.50`.

## Decision
Adopt the following canonical Phase 4 metric governance.

### Baseline definitions
- `baseline_cloze_i = best_baseline_accuracy_i` (best cloze baseline for seed `i`).
- `baseline_entity_i = best_entity_baseline_accuracy_i` (best entity baseline for seed `i`).

### Per-seed gains
- `gain_cloze_i = max_accuracy_i - baseline_cloze_i`
- `gain_entity_i = max_entity_accuracy_i - baseline_entity_i`

### Canonical gate metrics
- **Primary metric (A2, balanced advantage):**
  - `A2_i = min(gain_cloze_i, gain_entity_i)`
  - Gate statistic: CI95 over `{A2_i}`.
- **Secondary metric (A1, summed advantage):**
  - `A1_i = gain_cloze_i + gain_entity_i`
  - Gate statistic: CI95 over `{A1_i}`.
- **Support metric (A3, Pareto quality):**
  - `A3_indicator_i = 1 if gain_cloze_i > 0 and gain_entity_i > 0 else 0`
  - `A3_magnitude_i = A2_i if A3_indicator_i = 1 else 0`
  - Report:
    - Pareto rate = mean(`A3_indicator_i`) + Wilson CI95,
    - CI95 over `{A3_magnitude_i}`.

### Gate thresholds
- **PASS:** `A2_ci95_low > 0` and `A1_ci95_low > 0`.
- **FAIL:** `A1_ci95_high <= 0` or `A2_ci95_high <= 0`.
- **INTERIM (inconclusive):** all other cases; must run role-ablation and task-suite decision step before final PASS/FAIL.

## Consequences
- Old comparator `delta_old = collective - max_individual` is retired for Phase 4 gate decisions.
- Existing N=30 run remains valid; governance fix uses deterministic re-analysis only.
- Roadmap and EXP documents must reference this ADR and interim status.
- Next mandatory step after this ADR:
  - role-ablation test and explicit decision on 2-task vs 3-task gate policy.

## Rollback
- Revert ADR-0007 commit:
  - `git revert <commit-hash-containing-ADR-0007>`
- Operationally restore prior comparator only if explicitly superseded by a newer ADR.
