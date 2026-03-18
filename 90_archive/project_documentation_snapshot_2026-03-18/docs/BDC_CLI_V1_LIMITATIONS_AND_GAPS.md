# BDC CLI v1 Limitations and Gaps

## Scope
This document freezes the known limitations of `BDC Designer CLI v1` so later `v2` work is measured against a documented baseline rather than informal memory.

## Current input surface
v1 accepts only descriptor-level inputs:
- `task_family`
- `causal_asymmetry`
- `dag_depth`
- `dag_branching`
- `budget_tier`

## Current output surface
v1 emits only:
- effective role count
- abstract role weights for `predictor`, `critic`, `aggregator`
- strategy mode
- confidence
- caution flags
- short operator report

## Structural limitations
- No support for structured case packets.
- No support for tested architecture variants.
- No support for empirical winner vs loser reasoning.
- No real role ontology beyond predictor/critic/aggregator priors.
- No merge/split role reasoning.
- No direct representation of workflow decomposition, constraints, or risk map.
- No explicit prior-versus-evidence conflict mode.
- No insufficiency mode beyond low confidence and caution flags.
- No raw-text interpretation layer.
- No implementation-facing explanation grounded in measured evidence.

## Behavioral limitations
- Role count is effectively anchored by static family rules and the stopping-rule summary.
- Strategy mode is derived from family defaults and budget adjustments, not from empirical architecture evidence.
- Unknown families default to broad fallback behavior rather than case-aware reasoning.
- Confidence is descriptor-calibrated, not evidence-calibrated.
- v1 can recommend role inflation and unnecessary search where tested case evidence would reject them.

## Canonical calibration gap
`TextAI_Auto` is the canonical failure case for v1:
- v1 recommends `5` roles
- v1 recommends `full_hybrid_search`
- the evidence-aware memo recommends `4` roles with direct architecture selection plus tuning

## Interpretation
v1 remains usable as a lightweight prior-only tool, but it is not sufficient for evidence-aware architecture recommendation on real multi-agent workflow cases.
