# TASK-1804 BRIEF REPORT

## Scope
- Fix Phase 4 gate metric governance (R2) without retraining.
- Formalize canonical cooperative-advantage metrics in ADR-0007.
- Recompute N=30 gate statistics from existing TASK-1803 aggregate artifacts.
- Sync EXP + roadmap to corrected metric governance and interim Phase 4 status.

## Changes
- Added ADR:
  - `decisions/ADR-0007-collective-fitness.md`
- Added reproducible re-analysis script:
  - `scripts/analysis/phase4_recompute_advantage.py`
- Updated experiment doc:
  - `docs/experiments/EXP-0600_MULTI_ROLE_2026-03-01.md`
- Updated roadmap append-only:
  - `docs/project/project_roadmap.md`
- Added task report:
  - `reports/analysis/TASK-1804-GATE-FIX/TASK-1804_BRIEF_REPORT.md`

## Comparator Problem (L0)
- Old comparator used in TASK-1803:
  - `delta_old_i = collective_score_i - max_individual_collective_fitness_i`
- Under Scheme S1 setup:
  - `collective_score_i = mean(best_cloze_i, best_entity_i)`
  - `max_individual_collective_fitness_i = max(best_cloze_i, best_entity_i)`
- Identity: `mean(a,b) <= max(a,b)` for all real `a,b`.
- Therefore `delta_old_i <= 0` structurally, independent of learning quality.
- Conclusion: old comparator is methodologically biased and invalid for gate PASS/FAIL.

## Re-analysis Metrics (ADR-0007)
- `gain_cloze_i = max_accuracy_i - best_baseline_accuracy_i`
- `gain_entity_i = max_entity_accuracy_i - best_entity_baseline_accuracy_i`
- `A1_i = gain_cloze_i + gain_entity_i` (sum advantage)
- `A2_i = min(gain_cloze_i, gain_entity_i)` (balanced advantage, primary)
- `A3_i`: Pareto indicator (`both gains > 0`) + Pareto magnitude (`A2_i` if indicator else 0)

## Verification (L0)
- Command: `git status --short`
- Result: PASS
- Output summary: only expected docs/scripts/log changes tracked.

- Command: `python -m py_compile scripts/analysis/phase4_recompute_advantage.py`
- Result: PASS
- Output summary: script compiles successfully.

- Command: `python scripts/analysis/phase4_recompute_advantage.py --in_json results/edp1_exp0600_multirole/aggregates/phase4_multirole_n30_summary.json --out_json results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.json --out_csv results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.csv`
- Result: PASS
- Output summary: recompute completed for `n=30` seeds.

- Command: `python -c "import json, pathlib; d=json.loads(pathlib.Path('results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.json').read_text(encoding='utf-8')); print(d['n_seeds'], d['metrics']['A1']['ci95_low'], d['metrics']['A1']['ci95_high'])"`
- Result: PASS
- Output summary: `30 0.01261333117115333 0.02806078791904033`.

## N=30 Re-analysis Facts
- Source: `results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.json`
- `A1` CI95: `[0.0126133312, 0.0280607879]`
- `A2` CI95: `[0.0001794477, 0.0064231588]`
- `A3` Pareto rate: `0.50` (Wilson CI95 stored in artifact)
- Old comparator (for traceability): CI95 `[-0.2999079896, -0.2934303684]` from `phase4_multirole_n30_summary.json`

## Governance Outcome
- ADR-0007 accepted.
- Old comparator retired for gate decisions.
- Canonical gate metrics set to A2 (primary), A1 (secondary), A3 (support).
- Phase 4 status after metric fix: **INTERIM** (no false PASS/FAIL in this task).
- Mandatory next step: role-ablation and explicit 2-task vs 3-task gate decision.

## Artifacts
- `decisions/ADR-0007-collective-fitness.md`
- `scripts/analysis/phase4_recompute_advantage.py`
- `results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.json` (not in git)
- `results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.csv` (not in git)
- `docs/experiments/EXP-0600_MULTI_ROLE_2026-03-01.md`
- `docs/project/project_roadmap.md`
- `reports/analysis/TASK-1804-GATE-FIX/TASK-1804_BRIEF_REPORT.md`

## Risks / Limitations
- Re-analysis is constrained to existing N=30 2-task MVP artifacts; no role-ablation evidence included yet.
- Final Phase 4 gate verdict depends on next-step experiments mandated by ADR-0007.

## Rollback
- Revert this task commit:
  - `git revert <TASK-1804-GATE-FIX-commit-hash>`
