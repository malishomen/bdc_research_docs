# Phase 4 Baseline Freeze (2026-03-04)

## Scope
- Freeze the current Phase 4 baseline before any Phase 4R redesign activity.
- Anchor governance to `ADR-0010` and current official gate verdict (`RUN COMPLETE / GATE FAIL`).

## Fixed Governance Baseline
- Comparator governance: `decisions/ADR-0010-phase4-3task-gate-governance.md`
- Official gate decision: `reports/analysis/TASK-1813-PHASE4-GATE/PHASE4_GATE_DECISION.md`
- Baseline status:
  - `RUN STATUS = RUN COMPLETE`
  - `GATE STATUS = FAIL`

## Frozen Artifacts (Runtime, Not in Git)

| Artifact | SHA256 |
|---|---|
| `results/edp1_exp0600_multirole_3task/aggregates/phase4_multirole_3task_n30_summary.json` | `33e8e82ef868a95b20de34c21cdfc7f68b55a0eab2b5251abdc52fb0b622298c` |
| `results/edp1_exp0600_multirole_3task/aggregates/phase4_multirole_3task_n30_summary.csv` | `49f22cdeb91ccbe9059c2ab36828b95f70c58e26e59ae9c6e574f52a8b10f204` |
| `results/edp1_exp0600_multirole_3task/aggregates/phase4_advantage_recomputed_3task_n30.json` | `9760e31b9ba944cd30856b86c97c514908918f60ca34f06d0fd3295d034d84eb` |
| `results/edp1_exp0600_multirole_3task/aggregates/phase4_advantage_recomputed_3task_n30.csv` | `437b3041c22ba22b1e11239168a2efa8ec68d71858f36bfcde256e8be314cb66` |
| `results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.json` | `563c7a8e29c7d2d38ac1231eb84ecdc5383ec60f09dace4eb098e984bb1dcc3c` |
| `results/edp1_exp0600_multirole_3task/aggregates/phase4_role_ablation_3task_n30.csv` | `fb8c3abc7a6bff2932600c0010afd4056c0c5cc05ad701ea136c97ba75886883` |
| `results/edp1_exp0600_multirole_3task/aggregates/phase4_n30_provenance_manifest.json` | `d245c291d13541032d0a2ad6992c77c2c2426b43056dfd86e1561e080ed490cb` |

## Freeze Rule
- No new full `N=30` attempt is allowed until:
  1. root-cause dossier (`TASK-1900`) is complete,
  2. redesign ADR (`TASK-1901`, ADR-0011) is accepted,
  3. smoke+determinism gate (`TASK-1903`) passes.
