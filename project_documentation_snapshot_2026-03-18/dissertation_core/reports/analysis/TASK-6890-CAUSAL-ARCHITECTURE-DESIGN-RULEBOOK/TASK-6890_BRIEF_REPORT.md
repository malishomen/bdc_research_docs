# TASK-6890 BRIEF REPORT

## Scope
- Synthesize practical architecture-selection rules from:
  - hybrid value (`TASK-6860`)
  - standalone failure localization (`TASK-6870`)
  - effective role-count stopping rule (`TASK-6880`)

## Changes
- Added runner: `scripts/analysis/run_phase21_causal_architecture_design_rulebook.py`.
- Added task descriptor: `tasks/TASK-6890-CAUSAL-ARCHITECTURE-DESIGN-RULEBOOK.json`.
- Added test: `tests/test_phase21_causal_architecture_design_rulebook.py`.
- Generated artifacts:
  - `results/design_rulebook/design_rules.json`
  - `results/design_rulebook/family_specific_rules.csv`
  - `results/design_rulebook/strategy_selection_matrix.csv`

## Verification (L0)
- `python -m py_compile scripts/analysis/run_phase21_causal_architecture_design_rulebook.py` -> PASS
- `pytest -q tests/test_phase21_causal_architecture_design_rulebook.py` -> PASS (`1 passed`)
- `python scripts/analysis/run_phase21_causal_architecture_design_rulebook.py --hybrid_json results/hybrid_architecture_search/hybrid_value_summary.json --limits_json results/bdc_design_failure_modes/design_limits_summary.json --stopping_json results/effective_role_count/stopping_rule_summary.json --out_root results/design_rulebook` -> PASS

## Key Results
- Extracted global design rules and family-specific guidance (`n_family_rules=7`).
- Built strategy selection matrix for direct BDC vs warm-start hybrid vs pruning.
- Rulebook anchored to validated evidence (`hybrid_value_supported=true`, failure map + stopping rule inputs).

## Artifacts
- `scripts/analysis/run_phase21_causal_architecture_design_rulebook.py`
- `tests/test_phase21_causal_architecture_design_rulebook.py`
- `results/design_rulebook/design_rules.json`

## Risks / Limitations
- Rulebook is evidence-synthesized from current benchmark regime; external domain transfer should be validated in follow-up.

## Rollback
- `git revert <TASK-6890-commit-hash>`

