# TASK-1812 BRIEF REPORT

## Scope
- Run full 3-role ablation (`cloze/entity/category`) on recomputed 3-task N=30 metrics.
- Produce per-role degrade rates, CI/distributions, and necessity verdicts under ADR-0010 rule.

## Changes
- Updated script:
  - `scripts/analysis/phase4_role_ablation.py`
- Recomputed artifacts:
  - `results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.json`
  - `results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.csv`

## Verification (L0)
- Command: `python -m py_compile scripts/analysis/phase4_role_ablation.py`
- Result: PASS
- Command: `python scripts/analysis/phase4_role_ablation.py --in_json results/edp1_exp0600_multirole_3task/aggregates/phase4_advantage_recomputed_3task_n30.json --out_json results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.json --out_csv results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.csv`
- Result: PASS
- Command: `python -c "import json, pathlib; d=json.loads(pathlib.Path('results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.json').read_text(encoding='utf-8')); print(d['n_seeds'], d['cloze_ablation']['necessity_verdict'], d['entity_ablation']['necessity_verdict'], d['category_ablation']['necessity_verdict'])"`
- Result: PASS
- Output summary: all three role sections present, each with explicit necessity verdict.

## Artifacts
- `scripts/analysis/phase4_role_ablation.py` - strict 3-role ablation logic.
- `results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.json` - canonical role-ablation aggregate.
- `results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.csv` - per-seed ablation table.

## Risks / Limitations
- Ablation is analytical (gain-zeroing model), not additional training with removed roles.

## Rollback
- `git revert <commit-hash-containing-task-1812>`
