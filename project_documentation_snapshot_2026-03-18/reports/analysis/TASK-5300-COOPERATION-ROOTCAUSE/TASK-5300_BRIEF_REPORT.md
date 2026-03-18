# TASK-5300 BRIEF REPORT

## Objective
Determine the root cause why cooperative architecture fails to produce advantage over single model in Phase-4 experiments.

## Inputs
- `reference_profile`: `gpu_profile_v4_reference`
- `seed_range`: `1337..1366`
- `phase4_manifest`: `experiments/PHASE4_MANIFEST.json`
- `phase4_results`: `results/repro_run/`
- recomputed/ablation aggregates:
  - `results/edp1_exp0600_multirole_3task/aggregates/phase4_advantage_recomputed_3task_n30.json`
  - `results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.json`

## Layer 1 - Per-Seed Decomposition

Summary table:

| task | mean gain | negative seeds |
|---|---:|---:|
| cloze | 0.004818 | 9 |
| entity | 0.003645 | 0 |
| category | 0.000146 | 0 |

Main bottleneck task:
- `category` (12/30 seeds as min-gain task)

## Layer 2 - Role Contribution

Role mapping used for compatibility with requested role names:
- `predictor -> cloze`
- `critic -> entity`
- `aggregator -> category`

Average ablation impact (`delta_fitness`, source metric = `A2_3_drop` from upstream ablation JSON):

| role | mean delta fitness |
|---|---:|
| predictor | -0.002211 |
| critic | 0.000128 |
| aggregator | 0.000128 |

Conclusion:
- `predictor` channel dominates direction of fitness shifts; `critic/aggregator` deltas are near-zero in mean, indicating weak marginal contribution under current dynamics.
- Role-effect distribution is measured in `per_seed_ablation_deltas.csv` (not only binary necessity).

## Layer 3 - Specialization

Metrics:

| metric | value |
|---|---:|
| weight divergence (mean JS to uniform role mix) | 0.149000 |
| prediction divergence (1 - mean offdiag role corr) | 0.800000 |
| task responsibility split | False |
| dominant role by task | {'cloze': 'predictor', 'entity': 'predictor', 'category': 'predictor'} |

Conclusion:
- specialization detected: `False`
- Interpretation: specialization is effectively absent because role responsibility does not split across tasks (`task_responsibility_split=false`) even when divergence metrics are non-zero.

## Layer 4 - Training Dynamics

Seeds analyzed (negative `A2_component`):
- 1337, 1341, 1342, 1345, 1354, 1360, 1361, 1365, 1366

Observed patterns:
- `gradient_norm` is clip-saturated (~1.0) across negative seeds.
- token entropy remains near zero (prediction collapse regime).
- subset of seeds shows weak train-loss progress (plateau-like behavior).

## Root Cause Hypothesis
Based on collected evidence:
- Cooperation fails primarily due to a **bottleneck concentration** (most often category/cloze minima in balanced metric) plus **functional redundancy / non-splitting roles**.
- Architecture behaves as if one channel (predictor/cloze-mapped) carries most effective signal while others provide limited incremental benefit.

## Recommended Next Experiment
Phase-5 redesign proposal (no threshold changes):
1. enforce explicit role responsibility constraints (anti-collapse regularizer or gated task-routing),
2. stress-test bottleneck task with targeted curriculum,
3. repeat ablation + JS diagnostics under same seed policy.

## Artifacts
- `results/phase4_rootcause/per_seed_gains.csv`
- `results/phase4_rootcause/per_seed_bottleneck.json`
- `results/phase4_rootcause/per_seed_ablation_deltas.csv`
- `results/phase4_rootcause/role_prediction_correlation_matrices/`
- `results/phase4_rootcause/specialization_summary.json`
- `results/phase4_rootcause/per_task_js_divergence.csv`
- `results/phase4_rootcause/training_dynamics/`
- `results/phase4_rootcause/rootcause_summary.json`

## Verification (L0)
- `python -m py_compile scripts/analysis/task5300_build_rootcause_dataset.py` -> PASS
- `python scripts/analysis/task5300_build_rootcause_dataset.py --recomputed_json results/edp1_exp0600_multirole_3task/aggregates/phase4_advantage_recomputed_3task_n30.json --ablation_json results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.json --phase4_manifest experiments/PHASE4_MANIFEST.json --metrics_json reports/metrics.json --phase4_results_root results/repro_run --out_root results/phase4_rootcause` -> PASS
- `python -c "import json,pathlib; d=json.loads(pathlib.Path('results/phase4_rootcause/rootcause_summary.json').read_text()); print(d['n_seeds'], d['most_common_bottleneck'], d['specialization']['specialization_detected'])"` -> PASS
