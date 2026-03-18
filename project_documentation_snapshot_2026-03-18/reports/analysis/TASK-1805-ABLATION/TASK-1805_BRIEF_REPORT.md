# TASK-1805 BRIEF REPORT

## Scope
- Complete mandatory post-ADR-0007 step: role-ablation evidence for Phase 4 necessity criterion.
- Produce reproducible ablation analytics from existing N=30 artifacts (no new training runs).
- Make formal policy decision: 2-task finalization vs 3-task required before final Phase 4 gate.

## Changes
- Added analysis script:
  - `scripts/analysis/phase4_role_ablation.py`
- Generated non-git artifacts:
  - `results/edp1_exp0600_multirole/aggregates/phase4_role_ablation_n30.json`
  - `results/edp1_exp0600_multirole/aggregates/phase4_role_ablation_n30.csv`
- Updated governance/docs:
  - `docs/project/project_roadmap.md`
  - `docs/experiments/EXP-0600_MULTI_ROLE_2026-03-01.md`
- Added report:
  - `reports/analysis/TASK-1805-ABLATION/TASK-1805_BRIEF_REPORT.md`
- Append-only logging updates:
  - `AGENTS_LOG.md`
  - `WEEKLY_STATUS.md`

## Method
Input source for reproducible ablation:
- `results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.json`

Per-seed role ablation model:
- Full collective proxy: `(max_accuracy + max_entity_accuracy)/2`
- Cloze-role ablation: `(best_baseline_accuracy + max_entity_accuracy)/2`
- Entity-role ablation: `(max_accuracy + best_entity_baseline_accuracy)/2`
- Relative degradation:
  - `degrade = (full_collective - ablated_collective) / full_collective`
- Threshold rates:
  - necessity proxy: `degrade >= 5%`
  - interchangeability proxy: `degrade <= 2%`

Additionally computed degradation for A1 and A2 derived metrics.

## Verification (L0)
- Command: `git status --short`
- Result: PASS
- Output summary: tracked changes only in expected docs/scripts/log files.

- Command: `python -m py_compile scripts/analysis/phase4_role_ablation.py`
- Result: PASS
- Output summary: script compiles.

- Command: `python scripts/analysis/phase4_role_ablation.py --in_json results/edp1_exp0600_multirole/aggregates/phase4_advantage_recomputed_n30.json --out_json results/edp1_exp0600_multirole/aggregates/phase4_role_ablation_n30.json --out_csv results/edp1_exp0600_multirole/aggregates/phase4_role_ablation_n30.csv`
- Result: PASS
- Output summary: `n_seeds=30`; policy recommendation emitted.

- Command: `python -c "import json, pathlib; d=json.loads(pathlib.Path('results/edp1_exp0600_multirole/aggregates/phase4_role_ablation_n30.json').read_text(encoding='utf-8')); print(d['n_seeds'], d['cloze_ablation']['degrade_ge_5pct_rate'], d['entity_ablation']['degrade_ge_5pct_rate'])"`
- Result: PASS
- Output summary: `30 0.0 0.03333333333333333`

- Command: `rg -n "TASK-1805-ABLATION|ce37f46|role-ablation|2-task|3-task" AGENTS_LOG.md WEEKLY_STATUS.md docs/project/project_roadmap.md docs/experiments/EXP-0600_MULTI_ROLE_2026-03-01.md`
- Result: PASS

## Results
Role-ablation aggregate (N=30):

- Cloze ablation:
  - `mean degrade = 0.0186277691`
  - `CI95 = [0.0138617264, 0.0233938118]`
  - `degrade>=5% rate = 0.0000`
  - `interchangeable<=2% rate = 0.4000`

- Entity ablation:
  - `mean degrade = 0.0081892915`
  - `CI95 = [0.0027833123, 0.0135952706]`
  - `degrade>=5% rate = 0.0333`
  - `interchangeable<=2% rate = 0.9667`

Supplementary metric degradation:
- A1 degradation rates (>=5%): cloze `0.8333`, entity `0.5333`
- A2 degradation rates (>=5%): cloze `0.5000`, entity `0.5000`

## Policy Decision
- **Decision:** 2-task final gate is not accepted.
- **Policy:** 3-task suite is required before final Phase 4 gate PASS/FAIL.
- **Why:** role necessity under collective degradation criterion is weak in 2-task MVP, with very low `>=5%` degradation rates and high interchangeability (especially entity role).

## Artifacts
- `scripts/analysis/phase4_role_ablation.py`
- `results/edp1_exp0600_multirole/aggregates/phase4_role_ablation_n30.json` (not in git)
- `results/edp1_exp0600_multirole/aggregates/phase4_role_ablation_n30.csv` (not in git)
- `docs/project/project_roadmap.md`
- `docs/experiments/EXP-0600_MULTI_ROLE_2026-03-01.md`
- `reports/analysis/TASK-1805-ABLATION/TASK-1805_BRIEF_REPORT.md`

## Risks / Limitations
- Ablation is computed from aggregate/per-seed maxima and baseline substitutions; it is reproducible but still proxy-level for full ecosystem dynamics.
- Final Phase 4 verdict remains pending until 3rd-task integration and follow-up gate.

## Rollback
- Revert task commit:
  - `git revert <TASK-1805-ABLATION-commit-hash>`
